"""Behavior checks use disposable repositories only; no Hermes or model imports."""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


checkout = load("verify_checkout")
release = load("verify_release")


class CheckoutTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.git("init", "-q", "--initial-branch=main")
        (self.root / "module.py").write_text("result = 1\n")
        self.git("add", "module.py")
        self.git("-c", "user.name=Hermes Legion", "-c",
                 "user.email=hermes-legion@users.noreply.github.com", "commit", "-qm", "Fixture")
        self.manifest = {"upstream_commit": self.git("rev-parse", "HEAD"), "files": [
            {"path": "module.py", "before_sha256": self.sha("result = 1\n"),
             "after_sha256": self.sha("result = 2\n")},
            {"path": "new.py", "before_sha256": None, "after_sha256": self.sha("new = True\n")},
        ]}

    def git(self, *args):
        return subprocess.check_output(["git", "--no-optional-locks", "-C", str(self.root), *args],
                                       text=True, stderr=subprocess.DEVNULL).strip()

    @staticmethod
    def sha(value):
        return hashlib.sha256(value.encode()).hexdigest()

    def test_clean_base_and_exact_installed_bytes(self):
        self.assertEqual(checkout.verify(self.root, self.manifest, "base"), 2)
        (self.root / "module.py").write_text("result = 2\n")
        (self.root / "new.py").write_text("new = True\n")
        self.assertEqual(checkout.verify(self.root, self.manifest, "installed"), 2)

    def test_readonly_verifier_does_not_run_a_checkout_fsmonitor_hook(self):
        hook = self.root / '.git' / 'monitor-hook'
        marker = self.root / '.git' / 'monitor-called'
        hook.write_text('#!/bin/sh\ntouch "' + str(marker) + '"\nexit 0\n')
        hook.chmod(0o700)
        self.git('config', 'core.fsmonitor', str(hook))
        self.assertEqual(checkout.verify(self.root, self.manifest, 'base'), 2)
        self.assertFalse(marker.exists(), 'read-only inspection executed a configured helper')

    def test_wrong_revision_refused(self):
        self.manifest["upstream_commit"] = "0" * 40
        with self.assertRaises(ValueError):
            checkout.verify(self.root, self.manifest, "base")

    def test_unrelated_work_refused_without_modification(self):
        (self.root / "other.py").write_text("private = True\n")
        with self.assertRaises(ValueError):
            checkout.verify(self.root, self.manifest, "base")
        self.assertEqual((self.root / "other.py").read_text(), "private = True\n")

    def test_preexisting_new_target_refused(self):
        (self.root / "new.py").write_text("new = True\n")
        with self.assertRaises(ValueError):
            checkout.verify(self.root, self.manifest, "base")

    def test_symlink_and_traversal_refused(self):
        (self.root / "module.py").unlink()
        (self.root / "module.py").symlink_to(ROOT / "README.md")
        with self.assertRaises(ValueError):
            checkout.verify(self.root, self.manifest, "base")
        self.manifest["files"][0]["path"] = "../outside.py"
        with self.assertRaises(ValueError):
            checkout.verify(self.root, self.manifest, "base")

    def test_subdirectory_is_not_the_checkout_root(self):
        (self.root / "sub").mkdir()
        with self.assertRaises(ValueError):
            checkout.verify(self.root / "sub", self.manifest, "base")


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "patches").mkdir()
        (self.root / "README.md").write_text("Synthetic public fixture\n")
        (self.root / "patches/change.patch").write_text("synthetic patch\n")
        (self.root / "patches/manifest.json").write_text(json.dumps({
            "patch_file": "patches/change.patch",
            "patch_sha256": hashlib.sha256(b"synthetic patch\n").hexdigest(),
        }))
        rows = [{"path": p.relative_to(self.root).as_posix(),
                 "sha256": hashlib.sha256(p.read_bytes()).hexdigest()}
                for p in self.root.rglob("*") if p.is_file()]
        (self.root / release.MANIFEST).write_text(json.dumps({"files": rows}))

    def test_exact_inventory(self):
        self.assertEqual(release.verify(self.root), 3)

    def test_changed_file_refused(self):
        (self.root / "README.md").write_text("Changed\n")
        with self.assertRaises(ValueError):
            release.verify(self.root)

    def test_unlisted_secret_file_refused_without_exporting_content(self):
        (self.root / ".env").write_text("SYNTHETIC=not-a-real-credential\n")
        with self.assertRaises(ValueError):
            release.verify(self.root)

    def test_missing_file_refused(self):
        (self.root / "README.md").unlink()
        with self.assertRaises(ValueError):
            release.verify(self.root)

    def test_symlink_refused(self):
        (self.root / "extra.md").symlink_to(self.root / "README.md")
        with self.assertRaises(ValueError):
            release.verify(self.root)


if __name__ == "__main__":
    unittest.main()
