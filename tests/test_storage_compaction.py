"""Storage maintenance preserves exact backup bytes and leaves live state alone."""
import gzip
import importlib.util
import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location(
    "legion_storage", Path(__file__).resolve().parents[1] / "scripts/legion_storage.py")
storage = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(storage)


class BackupCompactionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.home = Path(self.tmp.name)
        self.path = self.home / "backups" / "old" / "snapshot.db"
        self.path.parent.mkdir(parents=True)
        with sqlite3.connect(self.path) as db:
            db.execute("CREATE TABLE fixture(value)")
            db.execute("INSERT INTO fixture VALUES (?)", ("PRIVATE_SENTINEL_DO_NOT_ECHO",))
        old = time.time() - 48 * 3600
        os.utime(self.path, (old, old))
        self.before = self.path.read_bytes()

    def run_compaction(self, **kwargs):
        return storage.compact_backup(self.home, "old/snapshot.db", **kwargs)

    def test_plan_is_read_only_and_contains_no_database_content(self):
        before = sorted(p.relative_to(self.home) for p in self.home.rglob("*"))
        result = self.run_compaction()
        self.assertEqual(result["source_bytes"], len(self.before))
        self.assertEqual(result["status"], "planned")
        self.assertEqual(self.path.read_bytes(), self.before)
        self.assertEqual(before, sorted(p.relative_to(self.home) for p in self.home.rglob("*")))
        self.assertNotIn("PRIVATE_SENTINEL_DO_NOT_ECHO", json.dumps(result))

    def test_apply_retains_exact_bytes_and_restore_metadata(self):
        result = self.run_compaction(apply=True)
        self.assertFalse(self.path.exists())
        archive = self.path.with_name("snapshot.db.gz")
        with gzip.open(archive, "rb") as stream:
            self.assertEqual(stream.read(), self.before)
        metadata = json.loads(self.path.with_name("snapshot.db.gz.metadata.json").read_text())
        self.assertEqual(metadata["source_bytes"], len(self.before))
        self.assertEqual(metadata["source_name"], "snapshot.db")
        self.assertEqual(result["sha256"], metadata["sha256"])
        self.assertNotIn("PRIVATE_SENTINEL_DO_NOT_ECHO", json.dumps(result))

    def test_recent_and_live_sidecar_files_are_refused(self):
        self.path.with_name("snapshot.db-wal").write_bytes(b"active")
        with self.assertRaises(ValueError):
            self.run_compaction(apply=True)
        self.path.with_name("snapshot.db-wal").unlink()
        os.utime(self.path, None)
        with self.assertRaises(ValueError):
            self.run_compaction(apply=True)
        self.assertEqual(self.path.read_bytes(), self.before)

    def test_existing_archive_is_never_overwritten(self):
        archive = self.path.with_name("snapshot.db.gz")
        archive.write_bytes(b"existing restore point")
        with self.assertRaises(ValueError):
            self.run_compaction(apply=True)
        self.assertEqual(archive.read_bytes(), b"existing restore point")
        self.assertEqual(self.path.read_bytes(), self.before)

    def test_escape_and_symlink_are_refused(self):
        with self.assertRaises(ValueError):
            storage.compact_backup(self.home, "../outside.db", apply=True)
        link = self.path.parent / "link.db"
        try:
            link.symlink_to(self.path)
        except (OSError, NotImplementedError):
            return
        with self.assertRaises(ValueError):
            storage.compact_backup(self.home, "old/link.db", apply=True)
        self.assertEqual(self.path.read_bytes(), self.before)

    def test_low_space_preserves_original_and_creates_no_archive(self):
        from collections import namedtuple
        usage = namedtuple("Usage", "total used free")(100, 99, 1)
        with patch("shutil.disk_usage", return_value=usage):
            with self.assertRaises(OSError):
                self.run_compaction(apply=True)
        self.assertEqual(self.path.read_bytes(), self.before)
        self.assertFalse(self.path.with_name("snapshot.db.gz").exists())

    def test_hard_links_and_non_sqlite_files_are_refused(self):
        link = self.path.parent / "other.db"
        try:
            os.link(self.path, link)
        except OSError:
            return
        with self.assertRaises(ValueError):
            self.run_compaction(apply=True)
        link.unlink()
        self.path.write_bytes(b"not a database")
        old = time.time() - 48 * 3600
        os.utime(self.path, (old, old))
        with self.assertRaises(ValueError):
            self.run_compaction(apply=True)
        self.assertEqual(self.path.read_bytes(), b"not a database")

    def test_source_change_during_compression_preserves_changed_original(self):
        original_gzip = gzip.GzipFile
        source = self.path

        class ChangingGzip(original_gzip):
            writes = 0

            def write(self, data):
                self.writes += 1
                if self.writes > 3:
                    raise AssertionError("compression must not chase a continuously growing source")
                with source.open("ab") as stream:
                    stream.write(b"changed")
                return super().write(data)

        with patch.object(storage.gzip, "GzipFile", ChangingGzip):
            with self.assertRaises(ValueError):
                self.run_compaction(apply=True)
        self.assertTrue(self.path.read_bytes().startswith(self.before))
        self.assertFalse(self.path.with_name("snapshot.db.gz").exists())
        self.assertEqual(list(self.path.parent.glob(".legion-compact-*")), [])

    def test_sync_failure_retains_both_original_and_verified_archive(self):
        with patch.object(storage, "_sync_directory", side_effect=OSError("sync failed")):
            with self.assertRaises(OSError):
                self.run_compaction(apply=True)
        self.assertEqual(self.path.read_bytes(), self.before)
        with gzip.open(self.path.with_name("snapshot.db.gz"), "rb") as stream:
            self.assertEqual(stream.read(), self.before)

    def test_duplicate_cli_aliases_are_refused_before_any_mutation(self):
        result = subprocess.run([
            sys.executable, str(Path(storage.__file__)), "--home", str(self.home),
            "--apply", "old/snapshot.db", "./old/snapshot.db"], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue(self.path.exists())
        self.assertEqual(self.path.read_bytes(), self.before)

    def test_cli_plan_can_be_followed_by_apply_without_echoing_contents(self):
        command = [sys.executable, str(Path(storage.__file__)), "--home", str(self.home), "old/snapshot.db"]
        planned = subprocess.run(command, capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(planned.stdout)["files"][0]["status"], "planned")
        self.assertTrue(self.path.exists())
        applied = subprocess.run([*command, "--apply"], capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(applied.stdout)["files"][0]["status"], "compacted")
        self.assertFalse(self.path.exists())
        self.assertNotIn("PRIVATE_SENTINEL_DO_NOT_ECHO", applied.stdout + applied.stderr)


if __name__ == "__main__":
    unittest.main()
