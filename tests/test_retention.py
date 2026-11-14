"""Retention removes only aged disposable data and never what a process holds."""
import importlib.util
import gzip
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

    def test_rejected_linked_report_does_not_abandon_later_report(self):
        entry = self.home / "reports/a-linked"
        report = make(entry / "report.txt", 5, "synthetic report")
        target = self.home / "state.db"
        original = target.read_bytes()
        link = entry / "link"
        link.symlink_to(target)
        os.utime(link, (NOW - 5 * 86400,) * 2, follow_symlinks=False)
        age_dir(entry, 5)
        later = (self.home / "reports/run1/report.txt").read_bytes()
        out = io.StringIO()
        with patch.object(retention, "held_paths", return_value=set()), redirect_stdout(out):
            code = retention.main(["--home", str(self.home), "--now", str(NOW), "--apply"])
        self.assertEqual(code, 1)
        self.assertIn("failed reports/a-linked  (archive file type differs)", out.getvalue())
        self.assertEqual(report.read_text(), "synthetic report")
        self.assertTrue(link.is_symlink())
        self.assertEqual(target.read_bytes(), original)
        self.assertFalse(entry.with_name("a-linked.tar.gz").exists())
        self.assertEqual(list(entry.parent.glob(".legion-pack-*")), [])
        self.assertFalse((self.home / "reports/run1").exists())
        with tarfile.open(self.home / "reports/run1.tar.gz") as tar:
            self.assertEqual(tar.extractfile("run1/report.txt").read(), later)

    def test_corrupt_report_archive_does_not_abandon_later_report(self):
        verify = retention._verify_archive
        for corruption in ("payload", "gzip-trailer", "tar-header", "deflate", "deflate-trailer"):
            with self.subTest(corruption=corruption), tempfile.TemporaryDirectory() as tmp:
                home = Path(tmp).resolve()
                entry = home / "reports/a-corrupt"
                source = make(entry / "report.txt", 5, "synthetic evidence")
                later = make(home / "reports/z-valid/report.txt", 5, "later evidence")
                for directory in (entry, later.parent):
                    age_dir(directory, 5)

                def corrupt_then_verify(archive, original):
                    if original == entry:
                        if corruption == "payload":
                            with tarfile.open(archive, "w:gz") as tar:
                                info = tarfile.TarInfo("a-corrupt/report.txt")
                                info.size = 5
                                tar.addfile(info, io.BytesIO(b"wrong"))
                        elif corruption == "gzip-trailer":
                            archive.write_bytes(archive.read_bytes()[:-8])
                        elif corruption == "tar-header":
                            archive.write_bytes(gzip.compress(b"not a tar archive"))
                        elif corruption == "deflate-trailer":
                            archive.write_bytes(archive.read_bytes() + b"\x1f\x8b\x08\x00" + b"\x00" * 6 + b"\x07")
                        else:
                            archive.write_bytes(b"\x1f\x8b\x08\x00" + b"\x00" * 6 + b"\x07")
                    verify(archive, original)

                out = io.StringIO()
                with patch.object(retention, "_verify_archive", corrupt_then_verify), \
                        patch.object(retention, "held_paths", return_value=set()), redirect_stdout(out):
                    code = retention.main(["--home", str(home), "--now", str(NOW), "--apply"])
                self.assertEqual(code, 1)
                self.assertIn("failed reports/a-corrupt", out.getvalue())
                self.assertNotIn("failed reports/z-valid", out.getvalue())
                self.assertEqual(source.read_text(), "synthetic evidence")
                self.assertFalse(entry.with_name("a-corrupt.tar.gz").exists())
                self.assertEqual(list(entry.parent.glob(".legion-pack-*")), [])
                self.assertFalse(later.parent.exists())
                with tarfile.open(home / "reports/z-valid.tar.gz") as tar:
                    self.assertEqual(tar.extractfile("z-valid/report.txt").read(), b"later evidence")

    def test_report_activated_after_publication_keeps_both_copies(self):
        import stat
        for mode in ("held", "unknown"):
            with self.subTest(mode=mode), tempfile.TemporaryDirectory() as tmp:
                home = Path(tmp).resolve()
                source = make(home / "reports/a-active/report.txt", 5, "active synthetic report")
                later = make(home / "reports/z-later/report.txt", 5, "later synthetic report")
                live = make(home / "state.db", 100, "unrelated durable data")
                for directory in (source.parent, later.parent):
                    age_dir(directory, 5)
                original, unrelated = source.read_bytes(), live.read_bytes()
                archive = source.parent.with_name("a-active.tar.gz")
                holder, observed = [], []
                synced, unknown_sent = False, False
                real_sync = retention.os.fsync

                def sync(fd):
                    nonlocal synced
                    real_sync(fd)
                    if stat.S_ISDIR(os.fstat(fd).st_mode) and archive.exists() and not holder:
                        holder.append(source.open("rb"))
                        synced = True

                def observe():
                    nonlocal unknown_sent
                    if holder:
                        if source.exists():
                            self.assertTrue(synced and archive.exists())
                            observed.append("after-publication")
                            if mode == "unknown" and not unknown_sent:
                                unknown_sent = True
                                return None
                        return {str(source)}
                    return set()

                out = io.StringIO()
                try:
                    with patch.object(retention.os, "fsync", sync), patch.object(
                            retention, "held_paths", observe), redirect_stdout(out):
                        code = retention.main(["--home", str(home), "--now", str(NOW), "--apply"])
                    for packed, member, expected in (
                        (archive, "a-active/report.txt", original),
                        (home / "reports/z-later.tar.gz", "z-later/report.txt", b"later synthetic report"),
                    ):
                        with tarfile.open(packed) as tar:
                            self.assertEqual(tar.extractfile(member).read(), expected)
                    self.assertFalse(later.parent.exists())
                    self.assertEqual(live.read_bytes(), unrelated)
                    self.assertTrue(source.exists(), "active report was removed after archive publication")
                    self.assertEqual(source.read_bytes(), original)
                    self.assertEqual(source.stat().st_ino, os.fstat(holder[0].fileno()).st_ino)
                    self.assertEqual(source.stat().st_dev, os.fstat(holder[0].fileno()).st_dev)
                    self.assertGreater(os.fstat(holder[0].fileno()).st_nlink, 0)
                    self.assertEqual(holder[0].read(), original)
                    self.assertTrue(observed)
                    self.assertEqual(unknown_sent, mode == "unknown")
                    self.assertEqual(code, 1)
                    self.assertIn("failed reports/a-active  (source is no longer idle after archive publication; both copies retained)", out.getvalue())
                    self.assertNotIn("failed reports/z-later", out.getvalue())
                    self.assertEqual(list(archive.parent.glob(".legion-pack-*")), [])
                finally:
                    for stream in holder:
                        stream.close()

    def test_postpublication_observer_mutation_keeps_changed_source(self):
        import stat
        entry = self.home / "reports/run1"
        source = entry / "report.txt"
        original = source.read_bytes()
        archive = entry.with_name("run1.tar.gz")
        phases = []
        synced = False
        real_sync = retention.os.fsync

        def sync(fd):
            nonlocal synced
            real_sync(fd)
            if stat.S_ISDIR(os.fstat(fd).st_mode) and archive.exists():
                synced = True

        def can_remove():
            phases.append((archive.exists(), synced))
            if archive.exists():
                self.assertTrue(synced)
                source.write_bytes(b"changed during postpublication observation")
            return True

        failure = None
        with patch.object(retention.os, "fsync", sync):
            try:
                retention.pack(entry, can_remove)
            except ValueError as exc:
                failure = str(exc)
        with tarfile.open(archive) as tar:
            self.assertEqual(tar.extractfile("run1/report.txt").read(), original)
        self.assertTrue(source.exists(), "source was removed without postpublication observation")
        self.assertEqual(source.read_bytes(), b"changed during postpublication observation")
        self.assertEqual(phases, [(False, False), (True, True)])
        self.assertEqual(failure, "source changed after archive publication; both copies retained")
        self.assertEqual(list(entry.parent.glob(".legion-pack-*")), [])

    def test_encoded_archive_pressure_keeps_source_and_continues_later_report(self):
        import gzip
        reserve = 1024**3
        for mode in ("full", "unknown", "trailer", "write-error", "ample"):
            with self.subTest(mode=mode), tempfile.TemporaryDirectory() as tmp:
                home = Path(tmp).resolve()
                source = make(home / "reports/a-first/report.txt", 5, "x")
                later = make(home / "reports/z-later/report.txt", 5, "later report")
                unrelated = make(home / "state.db", 100, "durable fixture")
                for directory in (source.parent, later.parent):
                    age_dir(directory, 5)
                archive = source.parent.with_name("a-first.tar.gz")
                meters, pending = [], []
                pressure_seen = []
                usage = shutil.disk_usage(home)
                real_fdopen, real_close = retention.os.fdopen, gzip.GzipFile.close

                class Meter(io.RawIOBase):
                    def __init__(self, raw):
                        super().__init__()
                        self.raw, self.accepted, self.written = raw, 0, 0
                        self.chunks, self.closing = [], False
                        self.first = not meters
                        meters.append(self)

                    def writable(self):
                        return True

                    def fileno(self):
                        return self.raw.fileno()

                    def tell(self):
                        return self.raw.tell()

                    def write(self, data):
                        if self.first and mode == "write-error":
                            raise OSError("synthetic archive write failure")
                        count = self.raw.write(data)
                        self.written += count
                        self.chunks.append(count)
                        return count

                    def close(self):
                        try:
                            self.raw.close()
                        finally:
                            super().close()

                class Buffered(io.BufferedWriter):
                    def write(self, data):
                        count = super().write(data)
                        self.raw.accepted += count
                        return count

                def fdopen(fd, file_mode, *args, **kwargs):
                    self.assertEqual(file_mode, "wb")
                    return Buffered(Meter(real_fdopen(fd, file_mode, buffering=0)), buffer_size=8192)

                def close(gzip_file):
                    if meters and not meters[-1].closed:
                        meters[-1].closing = True
                    return real_close(gzip_file)

                def space(parent):
                    current = meters[-1] if meters and not meters[-1].closed else None
                    if current is None:
                        free = reserve + 2 if not meters and mode == "full" else reserve + 1024**2
                    else:
                        pending.append(current.accepted - current.written)
                        self.assertEqual(os.fstat(current.fileno()).st_size, current.written)
                        free = reserve + 1024**2 - current.written
                        if current.first:
                            if mode == "full":
                                free = reserve + 2 - current.written
                                if current.written:
                                    pressure_seen.append("full")
                            elif mode == "unknown" and current.written:
                                pressure_seen.append("unknown")
                                raise OSError("synthetic volume observation unavailable")
                            elif mode == "trailer" and current.closing and any(n > 8 for n in current.chunks):
                                pressure_seen.append("trailer")
                                free = reserve + 3
                    return usage._replace(free=free)

                out = io.StringIO()
                with patch.object(retention.os, "fdopen", fdopen), patch.object(
                        gzip.GzipFile, "close", close), patch.object(retention.shutil, "disk_usage", space), \
                        patch.object(retention, "held_paths", return_value=set()), redirect_stdout(out):
                    code = retention.main(["--home", str(home), "--now", str(NOW), "--apply"])
                with tarfile.open(home / "reports/z-later.tar.gz") as tar:
                    self.assertEqual(tar.extractfile("z-later/report.txt").read(), b"later report")
                self.assertFalse(later.parent.exists())
                self.assertEqual(unrelated.read_text(), "durable fixture")
                self.assertEqual(len(meters), 2)
                self.assertTrue(all(m.closed for m in meters))
                if mode == "ample":
                    self.assertFalse(source.parent.exists())
                    with tarfile.open(archive) as tar:
                        self.assertEqual(tar.extractfile("a-first/report.txt").read(), b"x")
                    self.assertEqual(code, 0)
                    self.assertGreater(meters[0].written, 1)
                else:
                    self.assertTrue(source.exists(), "source removed despite encoded-write pressure or error")
                    self.assertEqual(source.read_bytes(), b"x")
                    self.assertFalse(archive.exists())
                    self.assertEqual(code, 1)
                    self.assertIn("failed reports/a-first", out.getvalue())
                    self.assertNotIn("failed reports/z-later", out.getvalue())
                    if mode != "write-error":
                        self.assertIn(mode, pressure_seen)
                    if mode == "full":
                        self.assertEqual(meters[0].written, 2)
                self.assertEqual(pending, [0] * len(pending))
                self.assertEqual(list(archive.parent.glob(".legion-pack-*")), [])

    def test_archive_writer_boundary_flush_and_error_order(self):
        from unittest.mock import Mock
        reserve = 1024**3
        path = self.home / "encoded-boundary.bin"
        usage = shutil.disk_usage(self.home)
        observed = []
        with path.open("wb", buffering=16) as output:
            writer = retention._ArchiveWriter(output, self.home)
            def space(parent):
                size = os.fstat(output.fileno()).st_size
                observed.append(size)
                return usage._replace(free=reserve + 3 - size)
            with patch.object(retention.shutil, "disk_usage", space):
                self.assertEqual(writer.write(b"abc"), 3)
                self.assertEqual(os.fstat(output.fileno()).st_size, 0)
                with self.assertRaisesRegex(OSError, "1 GiB archive reserve"):
                    writer.write(b"d")
                self.assertEqual(os.fstat(output.fileno()).st_size, 3)
            self.assertEqual(observed, [0, 3])
        self.assertEqual(path.read_bytes(), b"abc")
        with path.open("wb") as output:
            writer = retention._ArchiveWriter(output, self.home)
            failure = OSError("synthetic space observation unavailable")
            with patch.object(retention.shutil, "disk_usage", side_effect=failure):
                with self.assertRaises(OSError) as result:
                    writer.write(b"blocked")
            self.assertIs(result.exception, failure)
        self.assertEqual(path.read_bytes(), b"")
        stream = Mock(spec=["flush", "write"])
        flush_failure = OSError("synthetic flush failure")
        stream.flush.side_effect = flush_failure
        writer = retention._ArchiveWriter(stream, self.home)
        with patch.object(retention.shutil, "disk_usage", side_effect=AssertionError("space read before flush")):
            with self.assertRaises(OSError) as result:
                writer.write(b"blocked")
        self.assertIs(result.exception, flush_failure)
        stream.write.assert_not_called()
        stream.flush.side_effect = None
        write_failure = OSError("synthetic stream write failure")
        stream.write.side_effect = write_failure
        with patch.object(retention.shutil, "disk_usage", return_value=usage._replace(free=reserve + 1024)):
            with self.assertRaises(OSError) as result:
                writer.write(b"encoded")
        self.assertIs(result.exception, write_failure)
        stream.write.assert_called_once_with(b"encoded")

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
