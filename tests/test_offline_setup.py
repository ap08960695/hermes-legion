"""User-visible offline setup contracts; only disposable paths and synthetic data."""
import copy
import importlib.util
import json
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from test_team_planner import fixture, task

ROOT = Path(__file__).resolve().parents[1]


class SetupTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.team = json.loads((ROOT / 'examples/team.small.json').read_text())
        self.models = {p['id']: ('chatgpt-web/example-model' if p['id'].endswith('web') else 'example-model')
                       for p in self.team['profiles']}

    def cli(self, script, *args):
        self.assertTrue((ROOT / 'scripts' / script).exists(), 'offline setup tool is missing')
        return subprocess.run([sys.executable, str(ROOT / 'scripts' / script), *map(str, args)],
                              capture_output=True, text=True)

    def inputs(self):
        t = self.base / 'team.json'; t.write_text(json.dumps(self.team))
        m = self.base / 'models.json'; m.write_text(json.dumps(self.models))
        return t, m

    def generate(self, dest=None):
        t, m = self.inputs()
        args = ['--team', t, '--models', m]
        if dest is not None:
            args += ['--output', dest]
        return self.cli('legion_setup.py', *args)

    def test_preview_shows_new_file_diff_without_writing_a_bundle(self):
        result = self.generate()
        self.assertEqual(result.returncode, 0, result.stderr)
        out = json.loads(result.stdout)
        self.assertFalse(out['written'])
        self.assertIn('--- /dev/null', out['diff'])
        self.assertIn('+++ profiles/legion-artificer-codex/config.example.json', out['diff'])
        self.assertEqual(sorted(x.name for x in self.base.iterdir()), ['models.json', 'team.json'])

    def test_generated_configs_are_targeted_no_fallback_and_doctor_accepts_bundle(self):
        dest = self.base / 'bundle'
        result = self.generate(dest)
        self.assertEqual(result.returncode, 0, result.stderr)
        cfg = json.loads((dest / 'profiles/legion-artificer-codex/config.example.json').read_text())
        self.assertEqual(cfg['model'], {'provider': 'openai-codex', 'default': 'example-model'})
        self.assertEqual(cfg['fallback_providers'], [])
        self.assertEqual(cfg['fallback_model'], [])
        self.assertNotIn('delegation', cfg)
        self.assertTrue((dest / 'profiles/legion-forge-web/SOUL.md').read_text().strip())
        self.assertFalse(any(x.name in ['auth.json', '.env', 'config.yaml'] for x in dest.rglob('*')))
        result = self.cli('legion_doctor.py', '--bundle', dest)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue(json.loads(result.stdout)['offline_ready'])
        self.assertEqual(json.loads(result.stdout)['runtime_ready'], 'unknown')
        self.assertEqual(dest.stat().st_mode & 0o777, 0o700)
        self.assertEqual((dest / 'bundle.json').stat().st_mode & 0o777, 0o600)

    def test_existing_destination_is_refused_without_overwriting(self):
        dest = self.base / 'bundle'; dest.mkdir(); (dest / 'keep').write_text('existing data')
        result = self.generate(dest)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual((dest / 'keep').read_text(), 'existing data')
        self.assertEqual([x.name for x in dest.iterdir()], ['keep'])

    def test_linked_destination_parent_is_refused(self):
        real = self.base / 'real'; real.mkdir()
        link = self.base / 'link'; link.symlink_to(real, target_is_directory=True)
        self.assertNotEqual(self.generate(link / 'bundle').returncode, 0)
        self.assertEqual(list(real.iterdir()), [])

    def test_model_placeholders_refused_before_any_output_directory_is_created(self):
        self.models = {}
        dest = self.base / 'bundle'
        self.assertNotEqual(self.generate(dest).returncode, 0)
        self.assertFalse(dest.exists())

    def test_secret_fields_are_not_copied_into_output_or_errors(self):
        self.team['accounts'][0]['access_token'] = 'synthetic-private-canary'
        result = self.generate(self.base / 'bundle')
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn('synthetic-private-canary', result.stdout + result.stderr)
        self.assertFalse((self.base / 'bundle').exists())

    def test_unknown_model_override_is_refused(self):
        self.models['unknown-profile'] = 'example-model'
        self.assertNotEqual(self.generate(self.base / 'bundle').returncode, 0)

    def test_doctor_template_has_missing_models_and_unknown_runtime(self):
        t, _ = self.inputs()
        result = self.cli('legion_doctor.py', '--team', t)
        self.assertNotEqual(result.returncode, 0)
        out = json.loads(result.stdout)
        self.assertFalse(out['offline_ready'])
        self.assertEqual(out['runtime_ready'], 'unknown')
        self.assertIn('model-placeholder', [x['code'] for x in out['checks']])

    def test_doctor_rejects_each_missing_altered_or_extra_payload(self):
        for change in ['missing', 'altered', 'extra', 'symlink']:
            with self.subTest(change=change):
                dest = self.base / change
                self.assertEqual(self.generate(dest).returncode, 0)
                soul = dest / 'profiles/legion-artificer-codex/SOUL.md'
                if change == 'missing': soul.unlink()
                if change == 'altered': soul.write_text('changed')
                if change == 'extra': (dest / 'extra.json').write_text('{}')
                if change == 'symlink':
                    soul.unlink(); soul.symlink_to(ROOT / 'profiles/artificer/SOUL.md')
                self.assertNotEqual(self.cli('legion_doctor.py', '--bundle', dest).returncode, 0)

    def test_doctor_semantics_reject_fallback_even_when_inventory_hash_is_updated(self):
        import hashlib
        dest = self.base / 'bundle'; self.assertEqual(self.generate(dest).returncode, 0)
        rel = 'profiles/legion-artificer-codex/config.example.json'; f = dest / rel
        raw = json.loads(f.read_text()); raw['fallback_model'] = [{'provider': 'example'}]
        f.write_text(json.dumps(raw)); manifest = json.loads((dest / 'bundle.json').read_text())
        for row in manifest['files']:
            if row['path'] == rel: row['sha256'] = hashlib.sha256(f.read_bytes()).hexdigest()
        (dest / 'bundle.json').write_text(json.dumps(manifest))
        self.assertNotEqual(self.cli('legion_doctor.py', '--bundle', dest).returncode, 0)

    def test_doctor_does_not_report_an_empty_team_as_ready(self):
        self.team['profiles'] = []
        t, _ = self.inputs()
        result = self.cli('legion_doctor.py', '--team', t)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(json.loads(result.stdout)['offline_ready'])

    def test_doctor_input_errors_do_not_echo_rejected_values(self):
        t, _ = self.inputs(); t.write_text('{"secret":"synthetic-private-canary"}')
        result = self.cli('legion_doctor.py', '--team', t)
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn('synthetic-private-canary', result.stdout + result.stderr)

    def test_registered_full_roster_generates_all_34_profiles(self):
        self.team = json.loads((ROOT / 'examples/team.full.json').read_text())
        self.models = {p['id']: ('chatgpt-web/example-model' if p['id'].endswith('web') else 'example-model')
                       for p in self.team['profiles']}
        dest = self.base / 'bundle'
        self.assertEqual(self.generate(dest).returncode, 0)
        self.assertEqual(len(list((dest / 'profiles').iterdir())), 34)
        self.assertEqual(self.cli('legion_doctor.py', '--bundle', dest).returncode, 0)

    def test_known_live_home_and_kit_destinations_are_refused(self):
        t, m = self.inputs()
        import os
        live = self.base / 'live'; live.mkdir()
        result = subprocess.run([sys.executable, str(ROOT / 'scripts/legion_setup.py'), '--team',
                                 str(t), '--models', str(m), '--output', str(live / 'nested')],
                                env={**os.environ, 'HERMES_HOME': str(live)}, capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(list(live.iterdir()), [])
        self.assertNotEqual(self.generate(ROOT / 'must-not-be-created').returncode, 0)
        self.assertFalse((ROOT / 'must-not-be-created').exists())

    def test_empty_web_model_suffix_is_refused(self):
        self.models['legion-forge-web'] = 'chatgpt-web/'
        self.assertNotEqual(self.generate(self.base / 'bundle').returncode, 0)

    def test_doctor_reports_incompatible_checkout_without_modifying_it(self):
        from test_release_tools import CheckoutTests
        fixture = CheckoutTests(); fixture.setUp()
        self.addCleanup(fixture.temp.cleanup)
        before = (fixture.root / 'module.py').read_bytes()
        result = self.cli('legion_doctor.py', '--checkout', fixture.root, '--phase', 'base')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('checkout-incompatible', [x['code'] for x in json.loads(result.stdout)['checks']])
        self.assertEqual((fixture.root / 'module.py').read_bytes(), before)

    def test_doctor_reports_stale_snapshot_without_pretending_to_refresh_it(self):
        # A synthetic registered team is configured, but observation time is outside its snapshot.
        for p in self.team['profiles']: p['model'] = self.models[p['id']]
        t, _ = self.inputs()
        state = json.loads((ROOT / 'examples/snapshots/synthetic-ready.json').read_text())
        snapshot = self.base / 'state.json'; snapshot.write_text(json.dumps(state))
        before = snapshot.read_bytes()
        result = self.cli('legion_doctor.py', '--team', t, '--snapshot', snapshot, '--now', '999999999')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('snapshot-expired', [x['code'] for x in json.loads(result.stdout)['checks']])
        self.assertEqual(snapshot.read_bytes(), before)

    def test_setup_and_doctor_do_not_contact_network_or_start_processes(self):
        scripts = str(ROOT / 'scripts'); sys.path.insert(0, scripts)
        try:
            import legion_setup
            import legion_doctor
            with patch.object(socket, 'socket', side_effect=AssertionError('network forbidden')), \
                 patch.object(subprocess, 'Popen', side_effect=AssertionError('process forbidden')):
                files = legion_setup.make_files(self.team, self.models)
                legion_setup.write_bundle(self.base / 'bundle', files)
                report = legion_doctor.diagnose(bundle=self.base / 'bundle')
            self.assertTrue(report['offline_ready'])
            self.assertFalse(report['executed'])
        finally:
            sys.path.remove(scripts)


class ExplainTests(unittest.TestCase):
    def setUp(self):
        spec = importlib.util.spec_from_file_location('planner', ROOT / 'scripts/legion_plan.py')
        self.mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(self.mod)
        self.team, self.snapshot = fixture()

    def explain(self, tasks, **kw):
        self.assertIn('explain', __import__('inspect').signature(self.mod.plan).parameters,
                      'planner has no explanation interface')
        return self.mod.plan(self.team, self.snapshot, tasks, now=150, explain=True, **kw)

    def test_explanation_preserves_all_original_decisions_pins_and_budgets(self):
        tasks = [task(data_class='private'), task('second', session='session-b')]
        before = copy.deepcopy((self.team, self.snapshot, tasks))
        expected = self.mod.plan(self.team, self.snapshot, tasks, now=150)
        with patch.object(socket, 'socket', side_effect=AssertionError('network forbidden')):
            actual = self.explain(tasks)
        self.assertEqual((self.team, self.snapshot, tasks), before)
        for row in actual['decisions']: row.pop('explanation')
        self.assertEqual(actual, expected)

    def test_per_candidate_reasons_identify_privacy_and_role_failures(self):
        row = self.explain([task(data_class='private')])['decisions'][0]
        by_profile = {x['profile']: x for x in row['explanation']['candidates']}
        self.assertIn('data-class-not-permitted', by_profile['build-web']['reasons'])
        self.assertIn('role-mismatch', by_profile['research-native']['reasons'])

    def test_cooldown_and_budget_reasons_are_distinct(self):
        self.snapshot['quota_groups']['group-a']['cooldown_until'] = 190
        self.snapshot['quota_groups']['group-b']['remaining_day'] = 0
        row = self.explain([task()])['decisions'][0]
        reasons = {r for c in row['explanation']['candidates'] for r in c['reasons']}
        self.assertIn('account-cooldown', reasons)
        self.assertIn('day-budget-exhausted', reasons)
        self.assertEqual(row['status'], 'hold')

    def test_unverified_tools_and_unknown_profile_readiness_are_explained(self):
        self.snapshot['profiles'] = {}
        row = self.explain([task()])['decisions'][0]
        reasons = row['explanation']['candidates'][0]['reasons']
        self.assertIn('profile-not-ready', reasons)
        self.assertIn('capability-unverified', reasons)

    def test_busy_session_explains_gate_without_proposing_another_route(self):
        row = self.explain([task(), task('running', state='running')])['decisions'][0]
        self.assertEqual(row['explanation'], {'gate': 'session-busy', 'candidates': []})

    def test_pinned_unavailable_account_does_not_explain_other_accounts_as_choices(self):
        self.snapshot['accounts']['account-a']['status'] = 'unavailable'
        pins = {'session-a': {'profile': 'build-native', 'account': 'account-a'}}
        row = self.explain([task()], pins=pins)['decisions'][0]
        self.assertEqual(len(row['explanation']['candidates']), 1)
        self.assertIn('account-not-ready', row['explanation']['candidates'][0]['reasons'])


class ExplainCliTests(unittest.TestCase):
    def test_public_cli_explain_holds_a_cooling_pinned_session(self):
        args = [sys.executable, str(ROOT / 'scripts/legion_plan.py'), '--team',
                str(ROOT / 'examples/team.full.json'), '--snapshot',
                str(ROOT / 'examples/snapshots/synthetic-codex-cooldown.json'), '--tasks',
                str(ROOT / 'examples/scenarios/sticky-session.json'), '--pins',
                str(ROOT / 'examples/session-pins.synthetic.json'), '--now', '1', '--explain']
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        out = json.loads(result.stdout)
        self.assertFalse(out['executed'])
        row = out['decisions'][0]
        self.assertEqual(row['status'], 'hold')
        self.assertEqual(len(row['explanation']['candidates']), 1)
        self.assertIn('account-cooldown', row['explanation']['candidates'][0]['reasons'])
