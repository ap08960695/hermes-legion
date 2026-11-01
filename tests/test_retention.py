"""Retention removes only aged disposable data and never what a process holds."""
import importlib.util
import io
import os
from pathlib import Path
import tarfile
import tempfile
import time
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location(
    "legion_retention", Path(__file__).resolve().parents[1] / "scripts/legion_retention.py")
retention = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(retention)

NOW = 2_000_000_000.0


def make(path, age_days, text="x"):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    t = NOW - age_days * 86400
    os.utime(path, (t, t))
    return path


def age_dir(path, age_days):
    t = NOW - age_days * 86400
    os.utime(path, (t, t))


class RetentionTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.home = Path(tmp.name)
        h = self.home
        make(h / "profiles/dev/cache/scratch/old/a.txt", 10)
        age_dir(h / "profiles/dev/cache/scratch/old", 10)
        make(h / "profiles/dev/cache/scratch/mixed/old.txt", 10)
        make(h / "profiles/dev/cache/scratch/mixed/new.txt", 1)
        make(h / "profiles/dev/attachments/old.png", 20)
        make(h / "profiles/dev/attachments/new.png", 2)
        for i, age in enumerate([1, 2, 3, 9, 30]):
            make(h / f"backups/b{i}/state.db", age)
            age_dir(h / f"backups/b{i}", age)
        make(h / "reports/run1/report.txt", 5, "evidence " * 100)
        age_dir(h / "reports/run1", 5)
        make(h / "reports/fresh/report.txt", 0)
        make(h / "state.db", 100)          # live data is never a candidate
        make(h / "profiles/dev/state.db", 100)

    def run_cli(self, *extra, held=frozenset()):
        out = io.StringIO()
        with patch.object(retention, "held_paths", return_value=set(held)), redirect_stdout(out):
            retention.main(["--home", str(self.home), "--now", str(NOW), *extra])
        return out.getvalue()

    def test_preview_changes_nothing(self):
        before = sorted(self.home.rglob("*"))
        out = self.run_cli()
        self.assertEqual(before, sorted(self.home.rglob("*")))
        self.assertIn("preview", out)

    def test_apply_removes_only_aged_disposable_data(self):
        self.run_cli("--apply")
        h = self.home
        self.assertFalse((h / "profiles/dev/cache/scratch/old").exists())
        self.assertTrue((h / "profiles/dev/cache/scratch/mixed/new.txt").exists())
        self.assertFalse((h / "profiles/dev/attachments/old.png").exists())
        self.assertTrue((h / "profiles/dev/attachments/new.png").exists())
        # newest three backups stay regardless of age; older ones go only past the age limit
        self.assertEqual(sorted(p.name for p in (h / "backups").iterdir()), ["b0", "b1", "b2"])
        self.assertTrue((h / "state.db").exists() and (h / "profiles/dev/state.db").exists())
        self.assertTrue((h / "reports/fresh").is_dir())

    def test_reports_are_packed_losslessly(self):
        original = (self.home / "reports/run1/report.txt").read_text()
        self.run_cli("--apply")
        archive = self.home / "reports/run1.tar.gz"
        self.assertFalse((self.home / "reports/run1").exists())
        with tarfile.open(archive) as tar:
            self.assertEqual(tar.extractfile("run1/report.txt").read().decode(), original)

    def test_held_and_protected_paths_are_kept(self):
        held = {str((self.home / "backups/b4/state.db").resolve())}
        out = self.run_cli("--apply", "--protect", str(self.home / "backups/b3"), held=held)
        self.assertTrue((self.home / "backups/b4/state.db").exists())
        self.assertTrue((self.home / "backups/b3").exists())
        self.assertIn("in use", out)
        self.assertIn("protected", out)

    def test_unknown_process_state_keeps_everything(self):
        before = sorted(self.home.rglob("*"))
        out = io.StringIO()
        with patch.object(retention, "held_paths", return_value=None), redirect_stdout(out):
            retention.main(["--home", str(self.home), "--now", str(NOW), "--apply"])
        self.assertEqual(before, sorted(self.home.rglob("*")))


if __name__ == "__main__":
    unittest.main()
