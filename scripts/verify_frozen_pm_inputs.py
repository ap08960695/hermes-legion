#!/usr/bin/env python3
"""Verify local upstream artifacts for the frozen Apple Silicon PM release check."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit


def locked_inputs(source, wheelhouse, archives):
    import tomllib

    with (source / "pm/uv.lock").open("rb") as stream:
        packages = tomllib.load(stream)["package"]
    wheels = []
    for package in packages:
        if "virtual" in package["source"]:
            continue
        wheel, = package["wheels"]
        name = Path(urlsplit(wheel["url"]).path).name
        if not name.endswith("-none-any.whl"):
            raise ValueError(f"{package['name']} needs a universal wheel")
        prefix, _, expected = wheel["hash"].partition(":")
        if prefix != "sha256":
            raise ValueError(f"{package['name']} needs a SHA-256 wheel digest")
        wheels.append((wheelhouse / name, expected))
    if not wheels:
        raise ValueError("no dependency wheels in pm/uv.lock")

    tools = json.loads((source / "pm/lock.json").read_text(encoding="utf-8"))
    python = tools["packages"]["python"]["artifacts"]["darwin-arm64"]
    name = Path(urlsplit(python["url"]).path).name
    if not name.endswith(".tar.gz"):
        raise ValueError("darwin-arm64 Python needs a .tar.gz archive")
    return [*wheels, (archives / name, python["sha256"])]


def artifact_status(path, expected):
    try:
        if not path.is_file():
            return "missing"
        with path.open("rb") as stream:
            actual = hashlib.file_digest(stream, "sha256").hexdigest()
    except FileNotFoundError:
        return "missing"
    except OSError:
        return "unreadable"
    return "verified" if actual == expected else "hash mismatch"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="patched upstream checkout")
    parser.add_argument("--wheelhouse", type=Path, required=True, help="directory of original wheels")
    parser.add_argument("--archives", type=Path, required=True, help="directory with the original Python archive")
    args = parser.parse_args(argv)
    if sys.version_info < (3, 11):
        parser.error("Python 3.11 or newer is required")

    try:
        inputs = locked_inputs(args.source, args.wheelhouse, args.archives)
        if any(not re.fullmatch("[0-9a-f]{64}", digest) for _, digest in inputs):
            raise ValueError("invalid SHA-256 digest in lock")
    except (KeyError, OSError, TypeError, ValueError) as error:
        parser.error(f"cannot read frozen PM inputs: {error}")

    passed = True
    for path, digest in inputs:
        status = artifact_status(path, digest)
        print(f"{status} {path.name}")
        passed &= status == "verified"
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
