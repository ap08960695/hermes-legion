"""An installed skill must include the current entry point and its supporting files."""
import hashlib
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from legion_doctor import diagnose
from legion_setup import ROOT


class SkillCopyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.copy = Path(self.temp.name) / 'goal-driven-execution'
        shutil.copytree(ROOT / 'skills/goal-driven-execution', self.copy)

    def test_entry_point_without_reference_fails(self):
        (self.copy / 'references/tracked-delivery.md').unlink()
        result = diagnose(skill_copy=self.copy)
        self.assertFalse(result['offline_ready'])
        self.assertIn('references/tracked-delivery.md', result['checks'][0]['missing_files'])

    def test_older_entry_point_is_reported(self):
        (self.copy / 'SKILL.md').write_text('An older installed instruction.')
        result = diagnose(skill_copy=self.copy)
        self.assertFalse(result['offline_ready'])
        self.assertIn('SKILL.md', result['checks'][0]['different_files'])

    def test_complete_copy_passes_without_changing_files_or_claiming_runtime(self):
        before = {p.relative_to(self.copy): hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in self.copy.rglob('*') if p.is_file()}
        result = diagnose(skill_copy=self.copy)
        self.assertTrue(result['offline_ready'])
        self.assertEqual(result['runtime_ready'], 'unknown')
        self.assertFalse(result['executed'])
        self.assertEqual(before, {p.relative_to(self.copy): hashlib.sha256(p.read_bytes()).hexdigest()
                                  for p in self.copy.rglob('*') if p.is_file()})

    def test_extra_owner_reference_is_preserved(self):
        owner_file = self.copy / 'references/owner-note.md'
        owner_file.write_text('Keep this owner note.')
        self.assertTrue(diagnose(skill_copy=self.copy)['offline_ready'])
        self.assertEqual(owner_file.read_text(), 'Keep this owner note.')
