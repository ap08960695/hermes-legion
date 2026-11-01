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
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile
import time

DAY = 86400


def held_paths():
    """Absolute paths this user's processes hold open, as resolved strings."""
    held = set()
    proc = Path("/proc")
    if proc.is_dir():
        uid = os.getuid()
        for p in proc.iterdir():
            if not p.name.isdigit():
                continue
            try:
                if p.stat().st_uid != uid:
                    continue
            except OSError:
                continue
            for link in ("cwd", "exe"):
                try:
                    held.add(os.readlink(p / link))
                except OSError:
                    pass
            try:
                for fd in (p / "fd").iterdir():
                    try:
                        held.add(os.readlink(fd))
                    except OSError:
                        pass
                for line in (p / "maps").read_text(errors="replace").splitlines():
                    parts = line.split(None, 5)
                    if len(parts) == 6 and parts[5].startswith("/"):
                        held.add(parts[5])
            except OSError:
                pass
        return held
    try:  # macOS and other systems without /proc
        out = subprocess.run(["lsof", "-n", "-w", "-u", str(os.getuid()), "-Fn"],
                             capture_output=True, text=True, timeout=120).stdout
    except (OSError, subprocess.SubprocessError):
        return None
    return {line[1:] for line in out.splitlines() if line.startswith("n/")}


def newest_mtime(path):
    """Newest mtime of path and everything below it (symlinks are not followed)."""
    newest = path.lstat().st_mtime
    if path.is_dir() and not path.is_symlink():
        for root, dirs, files in os.walk(path):
            for name in dirs + files:
                try:
                    newest = max(newest, os.lstat(os.path.join(root, name)).st_mtime)
                except OSError:
                    pass
    return newest


class Plan:
    def __init__(self, home, held, protect, now):
        self.home, self.held, self.protect, self.now = home, held, protect, now
        self.actions = []  # (kind, path, reason)

    def blocked(self, path):
        text = str(path.resolve())
        if any(text == p or text.startswith(p + os.sep) for p in self.protect):
            return "protected"
        if self.held is None:
            return "process check unavailable"
        if any(h == text or h.startswith(text + os.sep) for h in self.held):
            return "in use"
        return None

    def add(self, kind, path, reason):
        why = self.blocked(path)
        self.actions.append(("keep" if why else kind, path, why or reason))

    def idle_for(self, path, days):
        return self.now - newest_mtime(path) > days * DAY


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


def pack(entry):
    target = entry.with_name(entry.name + ".tar.gz")
    if target.exists():
        raise FileExistsError(target)
    tmp = entry.with_name(entry.name + ".tar.gz.tmp")
    with tarfile.open(tmp, "w:gz") as tar:
        tar.add(entry, arcname=entry.name)
    with tarfile.open(tmp, "r:gz") as tar:  # verify the archive reads back completely
        members = sum(1 for _ in tar)
    if members == 0:
        raise ValueError(f"empty archive for {entry}")
    os.replace(tmp, target)
    shutil.rmtree(entry)


def apply(plan):
    for kind, path, _ in plan.actions:
        if kind == "remove":
            if path.is_dir() and not path.is_symlink():
                shutil.rmtree(path)
            else:
                path.unlink()
        elif kind == "pack":
            pack(path)


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
    if min(args.keep_days, args.scratch_days, args.backup_days, args.report_days) < 1 or min(args.backup_keep, args.snapshot_keep) < 1:
        ap.error("ages must be >= 1 day and keep counts >= 1")
    home = Path(args.home).resolve(strict=True)
    plan = build_plan(home, args, held_paths())
    for kind, path, reason in plan.actions:
        print(f"{kind:6} {path.relative_to(home)}  ({reason})")
    counts = {k: sum(1 for a in plan.actions if a[0] == k) for k in ("remove", "pack", "keep")}
    print(f"summary: remove={counts['remove']} pack={counts['pack']} keep={counts['keep']}"
          + ("" if args.apply else " (preview; add --apply)"))
    if args.apply:
        apply(plan)
    return 0


if __name__ == "__main__":
    sys.exit(main())
