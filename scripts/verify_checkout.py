#!/usr/bin/env python3
"""Read-only compatibility check. Never import Hermes or initialize a user home."""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import subprocess
import sys


def git(root, *args):
    result = subprocess.run(
        ["git", "--no-pager", "--no-optional-locks", "-c", "core.fsmonitor=false",
         "-C", str(root), *args],
        capture_output=True, check=True, text=True,
        env={**os.environ, "GIT_NO_LAZY_FETCH": "1", "GIT_OPTIONAL_LOCKS": "0",
             "GIT_TERMINAL_PROMPT": "0"},
    )
    return result.stdout.strip()


def verify(root, manifest, phase):
    root = root.resolve(strict=True)
    if Path(git(root, "rev-parse", "--show-toplevel")).resolve() != root:
        raise ValueError("target must be the checkout root")
    if git(root, "rev-parse", "HEAD") != manifest["upstream_commit"]:
        raise ValueError("unsupported upstream revision")
    expected = set()
    for row in manifest["files"]:
        rel = PurePosixPath(row["path"])
        if rel.is_absolute() or ".." in rel.parts or not rel.parts or rel.parts[0] == ".git":
            raise ValueError("invalid manifest target")
        if row["path"] in expected:
            raise ValueError("duplicate manifest target")
        expected.add(row["path"])
        path = root.joinpath(*rel.parts)
        if any(p.is_symlink() for p in [path, *path.parents] if p != root and root in p.parents):
            raise ValueError("symlink target refused")
        want = row["before_sha256" if phase == "base" else "after_sha256"]
        if want is None:
            if path.exists():
                raise ValueError("new target already exists")
        elif not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != want:
            raise ValueError("target content differs from manifest")
    changes = set(git(root, "diff", "--no-ext-diff", "--no-textconv", "--name-only", "HEAD").splitlines())
    untracked = set(git(root, "ls-files", "--others", "--exclude-standard").splitlines())
    if (phase == "base" and (changes or untracked)) or ((changes | untracked) - expected):
        raise ValueError("checkout contains unrelated changes")
    return len(expected)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkout", type=Path)
    parser.add_argument("--phase", required=True, choices=["base", "installed"])
    parser.add_argument("--manifest", type=Path,
                        default=Path(__file__).resolve().parents[1] / "patches/manifest.json")
    args = parser.parse_args()
    try:
        manifest = json.loads(args.manifest.read_text())
        count = verify(args.checkout, manifest, args.phase)
    except (ValueError, OSError, KeyError, TypeError, subprocess.SubprocessError):
        print("REFUSED: checkout, revision, manifest or source-state check failed", file=sys.stderr)
        return 1
    print(f"PASS: {args.phase} compatibility, {count} targets; no changes made")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
