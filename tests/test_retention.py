"""Retention removes only aged disposable data and never what a process holds."""
import importlib.util
import io
import os
import shutil
import subprocess
import sys
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
        self.home = Path(tmp.name).resolve()
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

    def test_protected_child_preserves_parent_backup(self):
        target = self.home / "backups/b4/state.db"
        self.run_cli("--apply", "--protect", str(target))
        self.assertTrue(target.exists())

    def test_new_holder_after_preview_preserves_candidate(self):
        args = type("Args", (), dict(protect=[], now=NOW, scratch_days=7,
                    keep_days=14, backup_days=7, backup_keep=3,
                    snapshot_keep=3, report_days=3))()
        plan = retention.build_plan(self.home, args, set())
        target = self.home / "backups/b4/state.db"
        with patch.object(retention, "held_paths", return_value={str(target.resolve())}):
            retention.apply(plan)
        self.assertTrue(target.exists())

    def test_modified_source_after_preview_is_kept(self):
        args = type("Args", (), dict(protect=[], now=NOW, scratch_days=7,
                    keep_days=14, backup_days=7, backup_keep=3,
                    snapshot_keep=3, report_days=3))()
        plan = retention.build_plan(self.home, args, set())
        target = self.home / "backups/b4/state.db"
        target.write_text("new data from a resumed job")
        with patch.object(retention, "held_paths", return_value=set()):
            retention.apply(plan)
        self.assertTrue(target.exists())
        self.assertEqual(target.read_text(), "new data from a resumed job")

    def test_failed_process_observer_is_unknown(self):
        original = Path.is_dir
        def without_proc(path):
            return False if path == Path("/proc") else original(path)
        failed = type("Result", (), dict(returncode=1, stdout="", stderr="denied"))()
        with patch.object(Path, "is_dir", without_proc), patch.object(
                retention.subprocess, "run", return_value=failed):
            self.assertIsNone(retention.held_paths())

    def test_lsof_file_record_delimiters_preserve_paths(self):
        original = Path.is_dir
        def without_proc(path):
            return False if path == Path("/proc") else original(path)
        result = type("Result", (), dict(returncode=0, stderr="",
            stdout="p123\0\nn/tmp/open file\0\nn/tmp/another\0\n"))()
        process_result = type("Result", (), dict(returncode=0, stderr="",
            stdout="123 S Fri Nov 6 12:00:00 2026\n"))()
        with patch.object(Path, "is_dir", without_proc), patch.object(
                retention.subprocess, "run", side_effect=lambda command, **kw:
                process_result if command[0] == "ps" else result):
            self.assertEqual(retention.held_paths(), {"/tmp/open file", "/tmp/another"})

    def test_lsof_omitting_stable_process_is_unknown(self):
        original = Path.is_dir
        def without_proc(path):
            return False if path == Path("/proc") else original(path)
        process_result = type("Result", (), dict(returncode=0, stderr="",
            stdout="123 S Fri Nov 6 12:00:00 2026\n456 S Fri Nov 6 12:00:00 2026\n"))()
        lsof_result = type("Result", (), dict(returncode=0, stderr="",
            stdout="p123\0\nn/tmp/open\0\n"))()
        with patch.object(Path, "is_dir", without_proc), patch.object(
                retention.subprocess, "run", side_effect=lambda command, **kw:
                process_result if command[0] == "ps" else lsof_result):
            self.assertIsNone(retention.held_paths())

    def test_lsof_closed_session_daemon_is_not_unknown(self):
        original = Path.is_dir
        def without_proc(path):
            return False if path == Path("/proc") else original(path)
        process_result = type("Result", (), dict(returncode=0, stderr="",
            stdout="123 S Fri Nov 6 12:00:00 2026 /usr/bin/python3\n"
                   "456 S Fri Nov 6 12:00:00 2026 /Applications/GlobalProtect.app/Contents/Resources/PanGPS\n"))()
        lsof_result = type("Result", (), dict(returncode=0, stderr="",
            stdout="p123\0\nn/tmp/open\0\n"))()
        with patch.object(Path, "is_dir", without_proc), patch.object(
                retention.subprocess, "run", side_effect=lambda command, **kw:
                process_result if command[0] == "ps" else lsof_result):
            self.assertEqual(retention.held_paths(), {"/tmp/open"})

    def test_lsof_escaped_filename_is_unknown(self):
        original = Path.is_dir
        def without_proc(path):
            return False if path == Path("/proc") else original(path)
        process_result = type("Result", (), dict(returncode=0, stderr="",
            stdout="123 S Fri Nov 6 12:00:00 2026\n"))()
        lsof_result = type("Result", (), dict(returncode=0, stderr="",
            stdout="p123\0\nn/tmp/line\\nbreak\0\n"))()
        with patch.object(Path, "is_dir", without_proc), patch.object(
                retention.subprocess, "run", side_effect=lambda command, **kw:
                process_result if command[0] == "ps" else lsof_result):
            self.assertIsNone(retention.held_paths())

    @unittest.skipUnless(Path("/proc").is_dir(), "Linux process observation")
    def test_partial_proc_visibility_is_unknown(self):
        original = Path.read_text
        def deny_maps(path, *args, **kwargs):
            if str(path) == f"/proc/{os.getpid()}/maps":
                raise PermissionError("denied")
            return original(path, *args, **kwargs)
        with patch.object(Path, "read_text", deny_maps):
            self.assertTrue(retention.held_paths() is None, "partial observation must remain unknown")

    @unittest.skipUnless(Path("/proc").is_dir(), "Linux process observation")
    def test_closed_session_daemon_does_not_disable_observation(self):
        script = ("import ctypes,sys,time\n"
                  "libc = ctypes.CDLL(None)\n"
                  "libc.prctl(15, sys.argv[1].encode(), 0, 0, 0)\n"
                  "libc.prctl(4, 0, 0, 0, 0)\n"
                  "print(flush=True)\n"
                  "time.sleep(30)\n")
        for name, observable in (("gpg-agent", True), ("unknown-closed", False)):
            child = subprocess.Popen([sys.executable, "-c", script, name], stdout=subprocess.PIPE)
            try:
                child.stdout.readline()
                with self.assertRaises(PermissionError):
                    os.readlink(f"/proc/{child.pid}/cwd")
                self.assertEqual(retention.held_paths() is not None, observable, name)
            finally:
                child.kill()
                child.wait()

    def test_stuck_entry_does_not_abandon_the_rest_of_the_plan(self):
        h = self.home
        original = shutil.rmtree
        def stuck(path, *args, **kwargs):
            if Path(path).name == "old":
                raise PermissionError(13, "Permission denied")
            return original(path, *args, **kwargs)
        out = io.StringIO()
        with patch.object(retention.shutil, "rmtree", stuck), \
                patch.object(retention, "held_paths", return_value=set()), redirect_stdout(out):
            code = retention.main(["--home", str(h), "--now", str(NOW), "--apply"])
        self.assertEqual(code, 1)
        self.assertIn("failed profiles/dev/cache/scratch/old", out.getvalue())
        self.assertEqual(sorted(p.name for p in (h / "backups").iterdir()), ["b0", "b1", "b2"])

    def test_another_users_tree_is_retained(self):
        foreign = os.getuid() + 1
        real_lstat = Path.lstat
        def lstat(path):
            info = real_lstat(path)
            if "scratch/old" not in str(path):
                return info
            return os.stat_result((*info[:4], foreign, *info[5:]))
        with patch.object(Path, "lstat", lstat):
            out = self.run_cli("--apply")
        self.assertTrue((self.home / "profiles/dev/cache/scratch/old/a.txt").exists())
        self.assertIn("keep   profiles/dev/cache/scratch/old", out)

    def test_inner_links_are_removed_without_touching_targets(self):
        outside = make(self.home.parent / (self.home.name + "-target.txt"), 10)
        self.addCleanup(outside.unlink)
        tree = self.home / "profiles/dev/cache/scratch/app"
        make(tree / "node_modules/pkg/cli.js", 10)
        (tree / "node_modules/.bin").mkdir()
        (tree / "node_modules/.bin/cli").symlink_to("../pkg/cli.js")
        (tree / "outside").symlink_to(outside)
        for d in (tree / "node_modules/.bin", tree / "node_modules/pkg", tree / "node_modules", tree):
            age_dir(d, 10)
        for link in (tree / "node_modules/.bin/cli", tree / "outside"):
            os.utime(link, (NOW - 10 * 86400,) * 2, follow_symlinks=False)
        self.run_cli("--apply")
        self.assertFalse(tree.exists())
        self.assertTrue(outside.exists())

    def test_report_modified_during_archive_is_not_removed(self):
        entry = self.home / "reports/run1"
        target = entry / "report.txt"
        original_add = tarfile.TarFile.add
        def changing_add(tar, name, *args, **kwargs):
            result = original_add(tar, name, *args, **kwargs)
            if Path(name) == entry:
                target.write_text("new evidence")
            return result
        with patch.object(tarfile.TarFile, "add", changing_add):
            with self.assertRaises((ValueError, OSError)):
                retention.pack(entry)
        self.assertEqual(target.read_text(), "new evidence")

    def test_readable_archive_with_wrong_payload_preserves_source(self):
        entry = self.home / "reports/run1"
        original = (entry / "report.txt").read_bytes()
        def wrong_add(tar, name, **kwargs):
            info = tarfile.TarInfo("run1/report.txt")
            info.size = 5
            tar.addfile(info, io.BytesIO(b"wrong"))
        with patch.object(tarfile.TarFile, "add", wrong_add):
            with self.assertRaises((ValueError, OSError)):
                retention.pack(entry)
        self.assertEqual((entry / "report.txt").read_bytes(), original)

    def test_truncated_gzip_trailer_preserves_source(self):
        entry = self.home / "reports/run1"
        verify = retention._verify_archive
        def truncate_then_verify(archive, source):
            data = archive.read_bytes()
            archive.write_bytes(data[:-8])
            verify(archive, source)
        with patch.object(retention, "_verify_archive", truncate_then_verify):
            with self.assertRaises((ValueError, OSError, EOFError)):
                retention.pack(entry)
        self.assertTrue((entry / "report.txt").exists())

    def test_nonfinite_age_is_refused_without_changes(self):
        before = sorted(self.home.rglob("*"))
        with self.assertRaises(SystemExit) as result:
            self.run_cli("--apply", "--scratch-days", "nan")
        self.assertNotEqual(result.exception.code, 0)
        self.assertEqual(before, sorted(self.home.rglob("*")))

    def test_symlinked_profile_cannot_remove_external_files(self):
        with tempfile.TemporaryDirectory() as outside:
            target = make(Path(outside) / "attachments/old.png", 30)
            (self.home / "profiles/linked").symlink_to(outside, target_is_directory=True)
            self.run_cli("--apply")
            self.assertTrue(target.exists())

    def test_workspace_marker_preserves_old_scratch(self):
        entry = self.home / "profiles/dev/cache/scratch/old"
        make(entry / ".keep", 10)
        age_dir(entry, 10)
        self.run_cli("--apply")
        self.assertTrue((entry / "a.txt").exists())

    def test_unknown_process_state_keeps_everything(self):
        before = sorted(self.home.rglob("*"))
        out = io.StringIO()
        with patch.object(retention, "held_paths", return_value=None), redirect_stdout(out):
            retention.main(["--home", str(self.home), "--now", str(NOW), "--apply"])
        self.assertEqual(before, sorted(self.home.rglob("*")))


if __name__ == "__main__":
    unittest.main()
