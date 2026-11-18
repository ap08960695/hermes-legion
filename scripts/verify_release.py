#!/usr/bin/env python3
"""Verify the exact release inventory and neutral Git metadata. Not a secret scanner."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys

MANIFEST = "RELEASE-MANIFEST.json"
IGNORED_DIRS = {".git", "__pycache__"}
ALLOWED_SUFFIXES = {".md", ".py", ".json", ".yaml", ".yml", ".patch"}
SPECIAL = {"LICENSE", ".gitignore"}
IMAGE_SUFFIXES = {".webp", ".gif"}
MAX_IMAGE_BYTES = 500_000


def read_documentation_image(path):
    with path.open("rb") as stream:
        data = stream.read(MAX_IMAGE_BYTES + 1)
    if len(data) > MAX_IMAGE_BYTES:
        raise ValueError("documentation image too large")
    if path.suffix == ".webp":
        valid = (data.startswith(b"RIFF") and data[8:12] == b"WEBP"
                 and int.from_bytes(data[4:8], "little") == len(data) - 8)
    else:
        valid = data.startswith((b"GIF87a", b"GIF89a")) and data.endswith(b";")
    if not valid:
        raise ValueError("invalid documentation image")
    return data


def verify(root, *, history=False):
    root = root.resolve(strict=True)
    manifest = json.loads((root / MANIFEST).read_text())
    rows = manifest["files"]
    expected = {}
    for row in rows:
        rel = PurePosixPath(row["path"])
        if rel.is_absolute() or ".." in rel.parts or row["path"] in expected:
            raise ValueError("invalid or duplicate release path")
        expected[row["path"]] = row["sha256"]
    observed = set()
    for path in root.rglob("*"):
        rel = path.relative_to(root)
        if ".git" in rel.parts:
            continue
        if path.is_symlink():
            raise ValueError("symlink refused")
        if "__pycache__" in rel.parts or path.suffix == ".pyc":
            continue
        if path.is_dir():
            continue
        name = rel.as_posix()
        if name == MANIFEST:
            continue
        if rel.parent == Path("docs/images") and path.suffix in IMAGE_SUFFIXES:
            data = read_documentation_image(path)
        else:
            if path.name not in SPECIAL and path.suffix not in ALLOWED_SUFFIXES:
                raise ValueError("unexpected file type")
            data = path.read_bytes()
            if b"\0" in data:
                raise ValueError("binary content refused")
            data.decode("utf-8")
        observed.add(name)
        if hashlib.sha256(data).hexdigest() != expected.get(name):
            raise ValueError("unlisted or changed release file")
    if observed != set(expected):
        raise ValueError("release inventory differs")
    additional = manifest.get("additional_patch_manifests", [])
    if not isinstance(additional, list):
        raise ValueError("additional patch manifests must be a list")
    manifests = ["patches/manifest.json", *additional]
    if any(not isinstance(name, str) or name not in expected for name in manifests):
        raise ValueError("patch manifest is outside the release inventory")
    if len(set(manifests)) != len(manifests):
        raise ValueError("duplicate patch manifest")
    for name in manifests:
        patch_manifest = json.loads((root / name).read_text())
        checks = [("patch_file", "patch_sha256")]
        if "upgrade_patch_file" in patch_manifest or "upgrade_patch_sha256" in patch_manifest:
            checks.append(("upgrade_patch_file", "upgrade_patch_sha256"))
        for path_key, hash_key in checks:
            patch_file = patch_manifest.get(path_key)
            if not isinstance(patch_file, str) or patch_file not in expected:
                raise ValueError("patch is outside the release inventory")
            patch = root / patch_file
            if hashlib.sha256(patch.read_bytes()).hexdigest() != patch_manifest.get(hash_key):
                raise ValueError("patch hash differs")
    if history:
        result = subprocess.run(
            ["git", "--no-optional-locks", "-C", str(root), "log", "--all",
             "--format=%an%x00%ae%x00%cn%x00%ce"],
            check=True, capture_output=True, text=True,
        )
        allowed = ["Hermes Legion", "hermes-legion@users.noreply.github.com"] * 2
        if not result.stdout.strip() or any(line.split("\0") != allowed for line in result.stdout.splitlines()):
            raise ValueError("non-neutral Git identity")
        status = subprocess.check_output(
            ["git", "--no-optional-locks", "-c", "core.fsmonitor=false",
             "-C", str(root), "status", "--porcelain"], text=True)
        if status.strip():
            raise ValueError("release checkout is not clean")
    return len(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--history", action="store_true")
    args = parser.parse_args()
    try:
        count = verify(args.root, history=args.history)
    except (ValueError, OSError, KeyError, TypeError, subprocess.SubprocessError):
        print("REFUSED: release inventory or metadata differs", file=sys.stderr)
        return 1
    print(f"PASS: {count} release files; no changes made")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
