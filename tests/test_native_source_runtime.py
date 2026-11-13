"""The native acceptance fixture must reject unadmitted state before native imports."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

FIXTURE = Path(__file__).resolve().parents[1] / "verification/native_source_runtime.py"


class NativeFixtureAdmissionTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.source = self.root / "source"
        self.home = self.root / ".hermes"
        self.source.mkdir()
        self.home.mkdir()
        self.original = "# Synthetic owner-like state\nmodel: {default: synthetic-unused}\n"
        (self.home / "config.yaml").write_text(self.original)
        (self.source / "hermes_bootstrap.py").write_text(
            'from pathlib import Path\nPath(__file__).with_name("imported").write_text("unexpected")\n')
        self.env = {"PATH": os.defpath, "HOME": str(self.root), "HERMES_HOME": str(self.home),
                    "HERMES_DISABLE_LAZY_INSTALLS": "1"}

    def run_fixture(self):
        return subprocess.run(
            [sys.executable, "-I", "-B", "-S", str(FIXTURE), "seed", str(self.source), str(self.home)],
            cwd=self.root, env=self.env, capture_output=True, text=True, timeout=10)

    def assert_untouched(self):
        self.assertEqual((self.home / "config.yaml").read_text(), self.original)
        self.assertFalse((self.home / "state.db").exists())
        self.assertFalse((self.source / "imported").exists())

    def test_missing_or_wrong_admission_refused_before_native_imports(self):
        for marker in (None, "not an admitted synthetic fixture\n"):
            with self.subTest(marker=marker):
                if marker is not None:
                    (self.home / ".legion-synthetic").write_text(marker)
                result = self.run_fixture()
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("synthetic admission marker required", result.stderr)
                self.assert_untouched()

    def test_mismatched_home_refused_before_native_imports(self):
        self.env["HERMES_HOME"] = str(self.root / "other")
        result = self.run_fixture()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("HERMES_HOME must match the fixture home", result.stderr)
        self.assert_untouched()
