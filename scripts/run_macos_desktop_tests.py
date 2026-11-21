#!/usr/bin/env python3
"""Run Desktop Vitest inside a prepared macOS loopback sandbox."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys


def run(checkout, scratch, fence, hermes_python, test_args):
    scratch = scratch.resolve(strict=True)
    desktop = checkout.resolve(strict=True) / "apps" / "desktop"
    vitest = desktop / "../../node_modules/.bin/vitest"
    fence = fence.resolve(strict=True)
    # A prepared venv launcher may symlink to the base interpreter.
    hermes_python = hermes_python.absolute()
    node = shutil.which("node")
    if not node or not all(os.access(item, os.X_OK) for item in (vitest, hermes_python)):
        raise ValueError("prepared Node, Vitest and Hermes Python are required")
    if any(scratch.iterdir()):
        raise ValueError("scratch directory must be empty")

    home, temp, sockets, runtime, tools = [scratch / name for name in ("h", "t", "u", "r", "bin")]
    for directory in (home, temp, sockets, runtime, tools):
        directory.mkdir(mode=0o700)

    # macOS sandboxed tests cannot exec the setuid system ps.
    probe = tools / "ps"
    shutil.copyfile("/bin/ps", probe)
    probe.chmod(0o755)
    subprocess.run(["/usr/bin/codesign", "--force", "--sign", "-", str(probe)], check=True)

    env = {
        "PATH": os.pathsep.join([
            str(tools), str(Path(node).absolute().parent), str(hermes_python.parent),
            "/Library/Developer/CommandLineTools/usr/bin", "/opt/homebrew/bin",
            "/usr/bin", "/bin", "/usr/sbin", "/sbin",
        ]),
        "HOME": str(home),
        "CFFIXED_USER_HOME": str(home),
        "TMPDIR": str(temp),
        "XDG_RUNTIME_DIR": str(runtime),
        "HERMES_TEST_SOCKET_TMPDIR": str(sockets),
        "HERMES_PYTHON": str(hermes_python),
        "HERMES_TEST_PYTHON": str(hermes_python),
        "UV_CACHE_DIR": str(scratch / "uv"),
        "UV_OFFLINE": "1",
        "GIT_CEILING_DIRECTORIES": str(scratch.parent),
        "GIT_CONFIG_NOSYSTEM": "1",
    }
    command = [
        "/usr/bin/sandbox-exec", "-f", str(fence),
        str(vitest), "run", "--configLoader", "runner", "--no-cache", "--no-color",
        "--maxWorkers", "1", *test_args,
    ]
    return subprocess.run(command, cwd=desktop, env=env, check=False).returncode


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkout", type=Path, help="prepared stable-full source checkout")
    parser.add_argument("scratch", type=Path, help="empty, short scratch directory admitted by the sandbox")
    parser.add_argument("fence", type=Path, help="sandbox profile for loopback and the scratch directory")
    parser.add_argument("hermes_python", type=Path, help="prepared Hermes test interpreter")
    parser.add_argument("test_args", nargs=argparse.REMAINDER, help="Vitest flags and file filters")
    args = parser.parse_args()
    if sys.platform != "darwin":
        parser.error("this runner requires macOS")
    try:
        test_args = args.test_args[1:] if args.test_args[:1] == ["--"] else args.test_args
        return run(args.checkout, args.scratch, args.fence, args.hermes_python, test_args)
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        print(f"Desktop test setup failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
