from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/verify_frozen_pm_inputs.py"
WHEEL = "packaging-26.0-py3-none-any.whl"
ARCHIVE = "cpython-3.14.9-aarch64-apple-darwin-install_only.tar.gz"


@unittest.skipIf(sys.version_info < (3, 11), "checker requires Python 3.11 or newer")
class FrozenPMInputsTests(unittest.TestCase):
    def setUp(self):
        scratch = tempfile.TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        root = Path(scratch.name)
        self.source = root / "source"
        self.wheelhouse = root / "wheels"
        self.archives = root / "archives"
        for directory in (self.source / "pm", self.wheelhouse, self.archives):
            directory.mkdir(parents=True)
        wheel_bytes = b"synthetic wheel"
        archive_bytes = b"synthetic archive"
        (self.wheelhouse / WHEEL).write_bytes(wheel_bytes)
        (self.archives / ARCHIVE).write_bytes(archive_bytes)
        (self.source / "pm/uv.lock").write_text(
            '[[package]]\nname = "hermes-pm-runtime"\nsource = { virtual = "." }\n'
            '[[package]]\nname = "packaging"\nsource = { registry = "https://example.invalid" }\n'
            f'wheels = [{{ url = "https://example.invalid/{WHEEL}", hash = "sha256:{sha256(wheel_bytes).hexdigest()}" }}]\n'
        )
        (self.source / "pm/lock.json").write_text(json.dumps({
            "packages": {"python": {"artifacts": {"darwin-arm64": {
                "url": f"https://example.invalid/{ARCHIVE}",
                "sha256": sha256(archive_bytes).hexdigest(),
            }}}}
        }))

    def run_checker(self):
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(self.source),
             "--wheelhouse", str(self.wheelhouse), "--archives", str(self.archives)],
            capture_output=True, text=True, check=False,
        )

    def test_accepts_both_hash_matched_originals(self):
        result = self.run_checker()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.splitlines(), [f"verified {WHEEL}", f"verified {ARCHIVE}"])

    def test_reports_corrupt_wheel_and_missing_archive_in_one_run(self):
        (self.wheelhouse / WHEEL).write_bytes(b"repacked with the same filename")
        (self.archives / ARCHIVE).unlink()
        result = self.run_checker()
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertEqual(result.stdout.splitlines(), [f"hash mismatch {WHEEL}", f"missing {ARCHIVE}"])

    def test_empty_dependency_lock_cannot_pass(self):
        (self.source / "pm/uv.lock").write_text(
            '[[package]]\nname = "hermes-pm-runtime"\nsource = { virtual = "." }\n'
        )
        result = self.run_checker()
        self.assertEqual(result.returncode, 2)
        self.assertIn("no dependency wheels", result.stderr)
