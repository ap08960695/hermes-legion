#!/usr/bin/env python3
"""Plan or compact explicitly selected old SQLite snapshots under HOME/backups.

No SQL queries, live database changes, model calls or automatic backup deletion.
Apply replaces only the selected uncompressed snapshot with verified gzip bytes
and restoration metadata. Keep the newest and any held rollback points separately.
"""
import argparse
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import stat
import tempfile
import time

_CHUNK = 1024 * 1024
_RESERVE = 1024 * 1024 * 1024


def _identity(info):
    return (info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns,
            info.st_ctime_ns, info.st_mode, info.st_uid, info.st_gid, info.st_nlink)


def _check_sidecars(path):
    if any(os.path.lexists(str(path) + suffix) for suffix in ("-wal", "-shm", "-journal")):
        raise ValueError("SQLite sidecar present; only closed backup snapshots are eligible")


def _candidate(home, relative, min_age_hours):
    if (isinstance(min_age_hours, bool) or not isinstance(min_age_hours, (float, int))
            or not math.isfinite(min_age_hours) or min_age_hours < 1):
        raise ValueError("minimum age must be at least one finite hour")
    root = (Path(home).resolve(strict=True) / "backups").resolve(strict=True)
    rel = Path(relative)
    if rel.is_absolute() or ".." in rel.parts or not rel.parts:
        raise ValueError("select a relative file inside the backup directory")
    path = root / rel
    if any(p.is_symlink() for p in (path, *path.parents) if p != root and root in p.parents):
        raise ValueError("symlink backup paths are refused")
    if not path.resolve(strict=True).is_relative_to(root):
        raise ValueError("backup path escapes the selected root")
    info = path.lstat()
    if (not stat.S_ISREG(info.st_mode) or info.st_nlink != 1
            or (hasattr(os, "getuid") and info.st_uid != os.getuid())):
        raise ValueError("backup must be a regular, unshared file owned by this user")
    if path.suffix.lower() not in {".db", ".sqlite", ".sqlite3"}:
        raise ValueError("only explicit SQLite snapshot files are supported")
    if time.time() - info.st_mtime < min_age_hours * 3600:
        raise ValueError("backup is too recent or its timestamp is in the future")
    _check_sidecars(path)
    archive = path.with_name(path.name + ".gz")
    metadata = path.with_name(path.name + ".gz.metadata.json")
    if os.path.lexists(archive) or os.path.lexists(metadata):
        raise ValueError("archive or restoration metadata already exists; refusing to overwrite")
    with path.open("rb") as stream:
        if stream.read(16) != b"SQLite format 3\x00":
            raise ValueError("file is not a SQLite snapshot")
        if _identity(os.fstat(stream.fileno())) != _identity(info):
            raise ValueError("backup changed during inspection")
    return path, info, archive, metadata


def _require_space(parent):
    if shutil.disk_usage(parent).free < _RESERVE + 2 * _CHUNK:
        raise OSError("insufficient free space to preserve the 1 GiB reserve")


def _sync_directory(parent):
    if os.name == "posix":
        fd = os.open(parent, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
        try:
            os.fsync(fd)
        finally:
            os.close(fd)


def compact_backup(home, relative, *, apply=False, min_age_hours=24):
    path, info, archive, metadata = _candidate(home, relative, min_age_hours)
    report = {"file": str(relative), "source_bytes": info.st_size, "status": "planned"}
    if not apply:
        return report
    _require_space(path.parent)
    fd, name = tempfile.mkstemp(prefix=".legion-compact-", dir=path.parent)
    temp = Path(name)
    metadata_temp = None
    try:
        digest = hashlib.sha256()
        with os.fdopen(fd, "wb") as output:
            with path.open("rb") as source:
                if _identity(os.fstat(source.fileno())) != _identity(info):
                    raise ValueError("backup changed before compression")
                with gzip.GzipFile(filename="", fileobj=output, mode="wb", compresslevel=3, mtime=0) as packed:
                    remaining = info.st_size
                    while remaining:
                        chunk = source.read(min(_CHUNK, remaining))
                        if not chunk:
                            raise ValueError("backup shrank during compression; original retained")
                        _require_space(path.parent)
                        digest.update(chunk)
                        packed.write(chunk)
                        remaining -= len(chunk)
                    if source.read(1):
                        raise ValueError("backup grew during compression; original retained")
                if _identity(os.fstat(source.fileno())) != _identity(info):
                    raise ValueError("backup changed during compression; original retained")
            output.flush()
            os.fsync(output.fileno())
        verified = hashlib.sha256()
        with gzip.open(temp, "rb") as stream:
            for chunk in iter(lambda: stream.read(_CHUNK), b""):
                verified.update(chunk)
        if verified.digest() != digest.digest():
            raise ValueError("compressed backup verification failed; original retained")
        restore = {"schema_version": 1, "source_name": path.name,
                   "source_bytes": info.st_size, "sha256": digest.hexdigest(),
                   "mode": stat.S_IMODE(info.st_mode), "uid": info.st_uid, "gid": info.st_gid,
                   "mtime_ns": info.st_mtime_ns}
        _require_space(path.parent)
        meta_fd, meta_name = tempfile.mkstemp(prefix=".legion-compact-", dir=path.parent)
        metadata_temp = Path(meta_name)
        with os.fdopen(meta_fd, "w", encoding="utf-8") as stream:
            json.dump(restore, stream, indent=2)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        # Exclusive publication never overwrites a raced or pre-existing output.
        os.link(temp, archive)
        os.link(metadata_temp, metadata)
        _sync_directory(path.parent)
        _check_sidecars(path)
        if _identity(path.lstat()) != _identity(info):
            raise ValueError("backup changed before removal; original and verified archive retained")
        path.unlink()
        _sync_directory(path.parent)
        report.update(status="compacted", archive_bytes=archive.stat().st_size,
                      sha256=digest.hexdigest(),
                      allocated_bytes_reclaimed=getattr(info, "st_blocks", 0) * 512
                      - getattr(archive.stat(), "st_blocks", 0) * 512
                      - getattr(metadata.stat(), "st_blocks", 0) * 512)
        return report
    finally:
        temp.unlink(missing_ok=True)
        if metadata_temp is not None:
            metadata_temp.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--home", type=Path, required=True)
    parser.add_argument("--apply", action="store_true", help="replace selected old snapshots with verified gzip archives")
    parser.add_argument("--min-age-hours", type=float, default=24)
    parser.add_argument("backup_files", nargs="+", help="explicit relative paths under HOME/backups")
    args = parser.parse_args()
    if len(set(args.backup_files)) != len(args.backup_files):
        parser.error("duplicate backup selection")
    try:
        # Inspect every selection before the first mutation. Each apply rechecks it.
        selected = [_candidate(args.home, name, args.min_age_hours)[0] for name in args.backup_files]
        if len(set(selected)) != len(selected):
            raise ValueError("duplicate resolved backup selection")
        results = []
        for index, name in enumerate(args.backup_files, 1):
            if args.apply:
                import sys
                print(f"Compacting selected backup {index}/{len(args.backup_files)}", file=sys.stderr, flush=True)
            results.append(compact_backup(args.home, name, apply=args.apply, min_age_hours=args.min_age_hours))
    except (OSError, ValueError) as exc:
        parser.exit(1, f"REFUSED: {exc}\n")
    print(json.dumps({"files": results, "model_calls": 0, "sql_queries": 0,
                      "automatic_selection": False}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
