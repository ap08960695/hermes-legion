"""Check the isolated Desktop test launch configuration."""
from importlib.util import module_from_spec, spec_from_file_location
import os
from pathlib import Path
from subprocess import CompletedProcess
import tempfile
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/run_macos_desktop_tests.py"
SPEC = spec_from_file_location("run_macos_desktop_tests", SCRIPT)
runner = module_from_spec(SPEC)
SPEC.loader.exec_module(runner)


class MacDesktopRunnerTests(unittest.TestCase):
    def test_launch_uses_the_fence_short_paths_and_unprivileged_probe(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            checkout = root / "source"
            scratch = root / "s"
            fence = root / "loopback.sb"
            hermes_python = root / "venv/bin/python"
            (checkout / "apps/desktop").mkdir(parents=True)
            scratch.mkdir()
            fence.touch()
            selected_node = root / "selected/node"
            selected_node.parent.mkdir()
            versioned_node = root / "node22"
            versioned_node.touch()
            selected_node.symlink_to(versioned_node)
            with (
                patch.object(runner.shutil, "which", return_value=str(selected_node)),
                patch.object(runner.os, "access", return_value=True),
                patch.object(runner.shutil, "copyfile", side_effect=lambda _, dest: dest.touch()),
                patch.object(runner.subprocess, "run", return_value=CompletedProcess([], 7)) as run,
            ):
                result = runner.run(checkout, scratch, fence, hermes_python, ["--project", "electron"])

            self.assertEqual(result, 7)
            probe = scratch / "bin/ps"
            self.assertEqual(probe.stat().st_mode & 0o7777, 0o755)
            self.assertEqual(run.call_args_list[0].args[0][-1], str(probe))
            command = run.call_args.args[0]
            self.assertEqual(command[:3], ["/usr/bin/sandbox-exec", "-f", str(fence)])
            self.assertEqual(command[-2:], ["--project", "electron"])
            env = run.call_args.kwargs["env"]
            self.assertEqual(env["HOME"], str(scratch / "h"))
            self.assertEqual(env["HERMES_TEST_SOCKET_TMPDIR"], str(scratch / "u"))
            self.assertEqual(env["HERMES_TEST_PYTHON"], str(hermes_python))
            self.assertEqual(env["PATH"].split(os.pathsep)[:2],
                             [str(probe.parent), str(selected_node.parent)])
