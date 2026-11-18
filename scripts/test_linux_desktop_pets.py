#!/usr/bin/env python3
"""Stage and run the Linux desktop character fixture without a Hermes gateway."""

import argparse
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import tempfile

KIT = Path(__file__).resolve().parents[1]


def prepare(source: Path, out: Path, cosmic_capture: bool) -> None:
    desktop = source / "apps/desktop"
    fixture = desktop / "electron/pet-overlay-linux-fixture"
    dist = desktop / "dist"
    if not (dist / "index.html").is_file():
        raise SystemExit("Build apps/desktop before preparing the fixture.")
    out.mkdir(mode=0o700, parents=True, exist_ok=False)
    subprocess.run(
        [source / "node_modules/.bin/esbuild", fixture / "launch.mjs", "--bundle",
         "--platform=node", "--format=esm", "--external:electron", f"--outfile={out / 'launch.mjs'}"], check=True,
    )
    for name in ("backdrop.html", "native.py", "absolute-pointer.py", "gnome-capture.py"):
        shutil.copy2(fixture / name, out / name)
    shutil.copytree(dist, out / "dist", ignore=shutil.ignore_patterns("node_modules", "electron-main.mjs"))
    if cosmic_capture:
        build_cosmic_capture(fixture, out)
    environment = {**os.environ, "PYTHONPATH": str(source)}
    with tempfile.TemporaryDirectory(dir=out) as temporary:
        pack = Path(temporary) / "lanternling"
        subprocess.run([sys.executable, KIT / "examples/character-pack/make_example.py", pack],
                       env=environment, check=True)
        from PIL import Image
        with Image.open(pack / "spritesheet.png") as sheet:
            channels = dict(zip("RGBA", sheet.split()))
            for index, order in enumerate(("RGBA", "GRBA", "BGRA", "RBGA", "GBRA")):
                Image.merge("RGBA", tuple(channels[channel] for channel in order)).save(out / f"atlas-{index}.png")


def build_cosmic_capture(fixture: Path, out: Path) -> None:
    protocols = Path("/usr/share/wayland-protocols/staging")
    with tempfile.TemporaryDirectory(dir=out) as temporary:
        generated = Path(temporary)
        files = []
        for name in ("ext-image-capture-source", "ext-image-copy-capture", "ext-foreign-toplevel-list"):
            xml = protocols / name / f"{name}-v1.xml"
            header, code = generated / f"{name}.h", generated / f"{name}.c"
            subprocess.run(["wayland-scanner", "client-header", xml, header], check=True)
            subprocess.run(["wayland-scanner", "private-code", xml, code], check=True)
            files.append(code)
        subprocess.run([os.environ.get("CC", "cc"), "-O2", "-Wall", "-Wextra",
                        "-I", generated, fixture / "cosmic-capture.c", *files,
                        "-o", out / "cosmic-capture", "-lwayland-client"], check=True)
    shutil.copy2(fixture / "cosmic-capture.sh", out / "cosmic-capture.sh")


def run(args: argparse.Namespace) -> int:
    out = args.output.resolve()
    out.mkdir(mode=0o700, parents=True, exist_ok=False)
    args.fixture = args.fixture.resolve(strict=True)
    args.electron = args.electron.resolve(strict=True)
    mem = next(line for line in Path("/proc/meminfo").read_text().splitlines() if line.startswith("MemAvailable:"))
    if int(mem.split()[1]) <= 6_000_000:
        raise SystemExit("This fixture needs over 6 GB MemAvailable.")

    with tempfile.TemporaryDirectory(prefix="home-", dir=out) as home:
        env = {**os.environ, "HOME": home, "HERMES_HOME": str(Path(home, "hermes")),
               "XDG_CONFIG_HOME": str(Path(home, "config")), "XDG_DATA_HOME": str(Path(home, "data")),
               "XDG_CACHE_HOME": str(Path(home, "cache")), "PET_TRIAL_OUT": str(out),
               "PET_TRIAL_INPUT": args.input}
        if args.capture_command:
            env["PET_TRIAL_CAPTURE"] = str(args.capture_command.resolve(strict=True))
        else:
            env.pop("PET_TRIAL_CAPTURE", None)

        command = [str(args.electron), "--disable-gpu", f"--ozone-platform={args.backend}"]
        if args.no_sandbox:
            command.append("--no-sandbox")
        command.append(str(args.fixture / "launch.mjs"))
        log = out / "run.jsonl"
        with log.open("w") as stdout, (out / "stderr.log").open("w") as stderr:
            proc = subprocess.Popen(command, cwd=args.fixture, env=env, stdout=stdout, stderr=stderr,
                                    start_new_session=True)
            try:
                status = proc.wait(timeout=85)
            finally:
                if proc.poll() is None:
                    os.killpg(proc.pid, signal.SIGTERM)
                    try:
                        proc.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        os.killpg(proc.pid, signal.SIGKILL)
                        proc.wait(timeout=5)
        events = [json.loads(line) for line in log.read_text().splitlines()]
        for event in events:
            print(json.dumps(event))
        return status or int(not events or events[-1]["event"] != "done")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    stage = commands.add_parser("prepare", help="make a portable fixture from an already-built patched checkout")
    stage.add_argument("source", type=Path)
    stage.add_argument("output", type=Path)
    stage.add_argument("--cosmic-capture", action="store_true", help="build the optional Wayland screenshot helper")
    launch = commands.add_parser("run", help="launch the staged fixture in an isolated HOME")
    launch.add_argument("fixture", type=Path)
    launch.add_argument("electron", type=Path)
    launch.add_argument("output", type=Path)
    launch.add_argument("--backend", choices=("x11", "wayland"), default="x11")
    launch.add_argument("--input", choices=("xtest", "uinput"), default="xtest")
    launch.add_argument("--no-sandbox", action="store_true", help="use with a local unpacked test binary")
    launch.add_argument("--capture-command", type=Path, help="optional executable receiving output PNG path and strip height")
    args = parser.parse_args()
    if args.command == "prepare":
        prepare(args.source.resolve(strict=True), args.output.resolve(), args.cosmic_capture)
        return 0
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
