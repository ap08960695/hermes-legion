#!/usr/bin/env python3
"""Plan or apply age-based retention for disposable Hermes home data.

Preview by default; nothing changes without --apply. No model calls, no SQL,
no service restarts. Every removal skips paths that a process of this user holds
(cwd, executable, open file or mapping) and paths listed with --protect.

Rules (days/counts are options):
  profiles/*/cache/scratch/*        entries with no file newer than --scratch-days
  profiles/*/attachments, profiles/*/lcm-large-outputs  files older than --keep-days
  backups/*                         older than --backup-days, newest --backup-keep always stay
  side-work/*                       entries with no file newer than --backup-days
  state-snapshots, profiles/*/state-snapshots  newest --snapshot-keep stay
  reports/*                         directories with no file newer than --report-days
                                    are packed losslessly into <dir>.tar.gz
Live databases, sessions, skills, memories, configs and credentials are never selected.
"""
import argparse
import gzip
import hashlib
import math
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import sys
import tarfile
import tempfile
import time
import zlib

DAY = 86400
# Session daemons the kernel marks non-dumpable, so their /proc links are closed to the
# owning user. They never open Hermes scratch, backups or reports; refusing on them left
# retention permanently unavailable on any host with an SSH login or a user systemd.
# ponytail: name allowlist; an unknown closed process still makes observation unknown.
CLOSED_SESSION_DAEMONS = frozenset({
    "systemd", "(sd-pam)", "gpg-agent", "ssh-agent", "sshd", "sshd-session", "sftp-server",
    "ping",  # file capabilities make it non-dumpable while it runs
    "PanGPS"})  # macOS: the GlobalProtect agent is invisible to the user's lsof.


def _user_processes():
    result = subprocess.run(["ps", "-U", str(os.getuid()), "-o", "pid=,stat=,lstart=,comm="],
                            capture_output=True, text=True, timeout=10)
    if result.returncode or result.stderr.strip():
        raise OSError("process inventory unavailable")
    processes = {}
    for line in result.stdout.splitlines():
        pid, state, *rest = line.split()
        if not pid.isdigit() or len(rest) < 5:
            raise ValueError("invalid process inventory")
        if not state.startswith("Z"):  # value: (lstart, command name)
            processes[pid] = (" ".join(rest[:5]), os.path.basename(" ".join(rest[5:])))
    return processes


def held_paths():
    """Absolute paths this user's processes hold open, as resolved strings."""
    held = set()
    proc = Path("/proc")
    if proc.is_dir():
        uid = os.getuid()
        try:
            processes = list(proc.iterdir())
        except OSError:
            return None
        for p in processes:
            if not p.name.isdigit():
                continue
            try:
                if p.stat().st_uid != uid:
                    continue
            except FileNotFoundError:
                continue
            except OSError:
                return None
            try:
                # Zombies cannot hold files; their cwd/exe links no longer resolve.
                if p.joinpath("stat").read_text().rsplit(")", 1)[1].split()[0] == "Z":
                    continue
            except (OSError, IndexError):
                if not p.exists():
                    continue
                return None
            try:
                os.readlink(p / "cwd")
            except PermissionError:
                try:
                    if p.joinpath("comm").read_text().strip() in CLOSED_SESSION_DAEMONS:
                        continue
                except OSError:
                    pass
                return None
            except OSError:
                pass  # Exit races are handled by the full observation below.
            for link in ("cwd", "exe"):
                try:
                    held.add(os.readlink(p / link))
                except OSError:
                    if p.exists():
                        return None
            try:
                for fd in (p / "fd").iterdir():
                    try:
                        held.add(os.readlink(fd))
                    except FileNotFoundError:
                        continue  # A descriptor can close during enumeration.
                    except OSError:
                        return None
                for line in (p / "maps").read_text(errors="replace").splitlines():
                    parts = line.split(None, 5)
                    if len(parts) == 6 and parts[5].startswith("/"):
                        held.add(re.sub(r"\\([0-7]{3})", lambda m: chr(int(m[1], 8)), parts[5]))
            except OSError:
                if p.exists():
                    return None
        return held
    try:  # macOS and other systems without /proc
        before = _user_processes()
        result = subprocess.run(["lsof", "-n", "-P", "+w", "-u", str(os.getuid()), "-F0n"],
                                capture_output=True, text=True, timeout=30)
        after = _user_processes()
    except (OSError, ValueError, subprocess.SubprocessError):
        return None
    if result.returncode or result.stderr.strip():
        return None
    fields = [field.lstrip("\n") for field in result.stdout.split("\0")]
    observed = {field[1:] for field in fields if field.startswith("p") and field[1:].isdigit()}
    stable = {pid for pid, started in before.items() if after.get(pid) == started
              and not (pid not in observed and started[1] in CLOSED_SESSION_DAEMONS)}
    if not stable or not stable.issubset(observed):
        return None
    paths = {field[1:] for field in fields if field.startswith("n/")}
    # lsof uses C escapes even with NUL fields. Do not mistake encoded names for paths.
    if any("\\" in path for path in paths):
        return None
    return paths or None


def source_stamp(path):
    """Bounded-memory identity of a complete tree; unreadable trees are retained."""
    digest = hashlib.sha256()

    def add(item):
        info = item.lstat()
        # Links inside a tree (node_modules/.bin) are removed as links; rmtree never follows them.
        inner_link = stat.S_ISLNK(info.st_mode) and item != path
        if not (stat.S_ISREG(info.st_mode) or stat.S_ISDIR(info.st_mode) or inner_link):
            raise ValueError("links and special files require manual retention")
        if inner_link:
            digest.update(os.fsencode(os.readlink(item)))
        if info.st_uid != os.getuid():
            raise ValueError("another user's files require manual retention")
        if item.name in {".keep", ".git"}:
            raise ValueError("retained workspace marker")
        values = (str(item.relative_to(path)), info.st_dev, info.st_ino, info.st_mode,
                  info.st_size, info.st_mtime_ns, info.st_ctime_ns, info.st_uid, info.st_gid,
                  info.st_nlink)
        digest.update(repr(values).encode("utf-8", "surrogateescape"))

    def failed(error):
        raise error

    add(path)
    if path.is_dir():
        for root, dirs, files in os.walk(path, onerror=failed, followlinks=False):
            dirs.sort()
            for name in sorted(dirs + files):
                add(Path(root) / name)
    return digest.digest()


def newest_mtime(path):
    """Newest mtime of path and everything below it (symlinks are not followed)."""
    newest = path.lstat().st_mtime
    if path.is_dir() and not path.is_symlink():
        def failed(error):
            raise error
        for root, dirs, files in os.walk(path, onerror=failed):
            for name in dirs + files:
                try:
                    newest = max(newest, os.lstat(os.path.join(root, name)).st_mtime)
                except OSError:
                    return time.time()  # An incomplete scan cannot prove age.
    return newest


class Plan:
    def __init__(self, home, held, protect, now):
        self.home, self.held, self.protect, self.now = home, held, protect, now
        self.actions = []  # (kind, path, reason)
        self.stamps = {}

    def blocked(self, path):
        text = str(path.resolve())
        if not Path(text).is_relative_to(self.home):
            return "outside home"
        if any(p.is_symlink() for p in (path, *path.parents) if p != self.home and self.home in p.parents):
            return "symlink path"
        if any(text == p or text.startswith(p + os.sep) or p.startswith(text + os.sep)
               for p in self.protect):
            return "protected"
        if self.held is None:
            return "process check unavailable"
        if any(h == text or h.startswith(text + os.sep) or h == text + " (deleted)"
               for h in self.held):
            return "in use"
        return None

    def add(self, kind, path, reason):
        why = self.blocked(path)
        if not why:
            try:
                self.stamps[path] = source_stamp(path)
            except (OSError, ValueError) as exc:
                why = f"retained tree: {exc}"
        self.actions.append(("keep" if why else kind, path, why or reason))

    def idle_for(self, path, days):
        try:
            return self.now - newest_mtime(path) > days * DAY
        except OSError:
            return False


def build_plan(home, args, held):
    plan = Plan(home, held, [str(Path(p).resolve()) for p in args.protect], args.now)
    for entry in sorted(home.glob("profiles/*/cache/scratch/*")):
        if plan.idle_for(entry, args.scratch_days):
            plan.add("remove", entry, f"scratch idle >{args.scratch_days}d")
    for sub in ("attachments", "lcm-large-outputs"):
        for root in sorted(home.glob(f"profiles/*/{sub}")):
            for f in sorted(p for p in root.rglob("*") if p.is_file() and not p.is_symlink()):
                if args.now - f.lstat().st_mtime > args.keep_days * DAY:
                    plan.add("remove", f, f"{sub} file >{args.keep_days}d")
    backups = sorted((p for p in (home / "backups").glob("*")), key=lambda p: p.lstat().st_mtime, reverse=True)
    for entry in backups[args.backup_keep:]:
        if args.now - entry.lstat().st_mtime > args.backup_days * DAY:
            plan.add("remove", entry, f"backup >{args.backup_days}d")
    for entry in sorted((home / "side-work").glob("*")):
        if plan.idle_for(entry, args.backup_days):
            plan.add("remove", entry, f"side-work idle >{args.backup_days}d")
    for snaps in [home / "state-snapshots", *sorted(home.glob("profiles/*/state-snapshots"))]:
        entries = sorted(snaps.glob("*"), key=lambda p: p.lstat().st_mtime, reverse=True)
        for entry in entries[args.snapshot_keep:]:
            plan.add("remove", entry, f"snapshot beyond newest {args.snapshot_keep}")
    for entry in sorted((home / "reports").glob("*")):
        if entry.is_dir() and not entry.is_symlink() and plan.idle_for(entry, args.report_days):
            plan.add("pack", entry, f"report idle >{args.report_days}d")
    return plan


def _digest(stream):
    digest = hashlib.sha256()
    for chunk in iter(lambda: stream.read(1024 * 1024), b""):
        digest.update(chunk)
    return digest.digest()


def _verify_archive(archive, entry):
    expected = {entry, *entry.rglob("*")}
    seen = set()
    with gzip.open(archive, "rb") as compressed, tarfile.open(fileobj=compressed, mode="r:") as tar:
        for member in tar:
            source = entry.parent / member.name
            if source not in expected or source in seen:
                raise ValueError("archive inventory differs")
            seen.add(source)
            if member.isdir() and source.is_dir():
                continue
            if not (member.isfile() or member.islnk()) or not source.is_file():
                raise ValueError("archive file type differs")
            with source.open("rb") as original, tar.extractfile(member) as packed:
                if _digest(original) != _digest(packed):
                    raise ValueError("archive payload differs")
        # Tar stops at its end marker before gzip's CRC/length trailer is consumed.
        for _ in iter(lambda: compressed.read(1024 * 1024), b""):
            pass
    if seen != expected:
        raise ValueError("archive inventory incomplete")


def pack(entry, can_remove=None):
    before = source_stamp(entry)
    source_bytes = sum(p.stat().st_size for p in entry.rglob("*") if p.is_file())
    if shutil.disk_usage(entry.parent).free < source_bytes + 1024 ** 3:
        raise OSError("insufficient free space to preserve the 1 GiB archive reserve")
    target = entry.with_name(entry.name + ".tar.gz")
    if os.path.lexists(target):
        raise FileExistsError(target)
    fd, name = tempfile.mkstemp(prefix=".legion-pack-", dir=entry.parent)
    tmp = Path(name)
    try:
        with os.fdopen(fd, "wb") as output:
            with tarfile.open(fileobj=output, mode="w:gz") as tar:
                tar.add(entry, arcname=entry.name)
            output.flush()
            os.fsync(output.fileno())
        _verify_archive(tmp, entry)
        if source_stamp(entry) != before:
            raise ValueError("source changed during packing")
        if can_remove is not None and not can_remove():
            raise ValueError("source is no longer idle")
        # Publish without overwriting an archive created by another retention run.
        os.link(tmp, target)
        dir_fd = os.open(entry.parent, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
        try:
            os.fsync(dir_fd)
        finally:
            os.close(dir_fd)
        if source_stamp(entry) != before:
            raise ValueError("source changed after archive publication; both copies retained")
        shutil.rmtree(entry)
    finally:
        tmp.unlink(missing_ok=True)


def apply(plan):
    failed = 0
    for kind, path, _ in plan.actions:
        try:
            _apply_one(plan, kind, path)
        except (OSError, ValueError, EOFError, tarfile.TarError, zlib.error) as exc:  # A rejected entry must not abort later cleanup.
            failed += 1
            print(f"failed {path.relative_to(plan.home)}  ({getattr(exc, 'strerror', None) or exc})")
    return failed


def _apply_one(plan, kind, path):
    if kind == "keep":
        return
    plan.held = held_paths()
    why = plan.blocked(path)
    try:
        unchanged = source_stamp(path) == plan.stamps[path]
    except (OSError, ValueError):
        unchanged = False
    if why or not unchanged:
        print(f"keep   {path.relative_to(plan.home)}  ({why or 'source changed'})")
        return
    if kind == "remove":
        if path.is_dir() and not path.is_symlink():
            shutil.rmtree(path)
        else:
            path.unlink()
    elif kind == "pack":
        def can_remove():
            plan.held = held_paths()
            return not plan.blocked(path)
        pack(path, can_remove)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--home", required=True, help="Hermes home (HERMES_HOME)")
    ap.add_argument("--apply", action="store_true", help="perform the plan (default: preview)")
    ap.add_argument("--keep-days", type=float, default=14)
    ap.add_argument("--scratch-days", type=float, default=7)
    ap.add_argument("--backup-days", type=float, default=7)
    ap.add_argument("--backup-keep", type=int, default=3)
    ap.add_argument("--snapshot-keep", type=int, default=3)
    ap.add_argument("--report-days", type=float, default=3)
    ap.add_argument("--protect", action="append", default=[], help="path to never touch (repeatable)")
    ap.add_argument("--now", type=float, default=None, help=argparse.SUPPRESS)
    args = ap.parse_args(argv)
    args.now = time.time() if args.now is None else args.now
    ages = (args.keep_days, args.scratch_days, args.backup_days, args.report_days)
    if any(not math.isfinite(age) or age < 1 for age in ages) or min(args.backup_keep, args.snapshot_keep) < 1:
        ap.error("ages must be >= 1 day and keep counts >= 1")
    home = Path(args.home).resolve(strict=True)
    plan = build_plan(home, args, held_paths())
    for kind, path, reason in plan.actions:
        print(f"{kind:6} {path.relative_to(home)}  ({reason})")
    counts = {k: sum(1 for a in plan.actions if a[0] == k) for k in ("remove", "pack", "keep")}
    print(f"summary: remove={counts['remove']} pack={counts['pack']} keep={counts['keep']}"
          + ("" if args.apply else " (preview; add --apply)"))
    if args.apply and apply(plan):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
