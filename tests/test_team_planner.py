"""Offline routing contracts; synthetic account aliases only."""
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

ROOT = Path(__file__).resolve().parents[1]


def fixture():
    team = {
        "schema_version": 1, "kind": "legion-offline-team", "quota_policy": "inherit-native",
        "paid_fallback": False,
        "accounts": [
            {"id": "account-a", "provider": "openai-codex", "principal_ref": "principal-a", "quota_group": "group-a", "auth_scope": "root", "credential_ref": "local-label-a"},
            {"id": "account-a-alias", "provider": "openai-codex", "principal_ref": "principal-a", "quota_group": "group-a", "auth_scope": "root", "credential_ref": "local-label-a"},
            {"id": "account-b", "provider": "openai-codex", "principal_ref": "principal-b", "quota_group": "group-b", "auth_scope": "root", "credential_ref": "local-label-b"},
        ],
        "profiles": [
            {"id": "build-web", "role": "artificer", "provider": "openai-codex", "model": "chatgpt-web/CHOOSE_MODEL", "accounts": ["account-a-alias"], "capabilities": ["text", "tools"], "data_classes": ["public"], "priority": 0},
            {"id": "build-native", "role": "artificer", "provider": "openai-codex", "model": "CHOOSE_MODEL", "accounts": ["account-a", "account-b"], "capabilities": ["text", "tools"], "data_classes": ["public", "private"], "priority": 10},
            {"id": "research-native", "role": "scout", "provider": "openai-codex", "model": "CHOOSE_MODEL", "accounts": ["account-a"], "capabilities": ["text", "tools"], "data_classes": ["public", "private"], "priority": 10},
        ],
    }
    snapshot = {
        "schema_version": 1, "kind": "legion-synthetic-snapshot", "captured_at": 100, "expires_at": 200,
        "accounts": {x["id"]: {"status": "ready"} for x in team["accounts"]},
        "profiles": {x["id"]: {"status": "ready", "verified_capabilities": ["text", "tools"]} for x in team["profiles"]},
        "quota_groups": {name: {"max_parallel": 1, "active": 0, "remaining_hour": 2, "remaining_day": 3, "cooldown_until": 0}
                         for name in ["group-a", "group-b"]},
    }
    return team, snapshot


def task(name="work-a", role="artificer", session="session-a", **changes):
    return {"id": name, "role": role, "session": session, "state": "ready", "data_class": "public",
            "requires": ["text", "tools"], "request_budget": 1, **changes}


class PlannerTests(unittest.TestCase):
    def setUp(self):
        path = ROOT / "scripts/legion_plan.py"
        self.assertTrue(path.exists(), "offline team planner has not been implemented")
        spec = importlib.util.spec_from_file_location("legion_plan", path)
        self.mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.mod)
        self.team, self.state = fixture()

    def plan(self, tasks, **kwargs):
        return self.mod.plan(self.team, self.state, tasks, now=150, **kwargs)

    def test_public_work_prefers_suitable_web_profile(self):
        row = self.plan([task()])["decisions"][0]
        self.assertEqual((row["status"], row["profile"], row["account"]),
                         ("selected", "build-web", "account-a-alias"))

    def test_private_work_cannot_use_public_only_web_lane(self):
        row = self.plan([task(data_class="private")])["decisions"][0]
        self.assertEqual(row["profile"], "build-native")

    def test_two_roles_and_duplicate_alias_share_one_account_budget(self):
        rows = self.plan([task(), task("research", "scout", "session-r")])["decisions"]
        self.assertEqual([x["status"] for x in rows], ["selected", "hold"])

    def test_new_session_can_use_other_available_account_without_raising_caps(self):
        rows = self.plan([task(), task("work-b", session="session-b")])["decisions"]
        self.assertEqual([x["account"] for x in rows], ["account-a-alias", "account-b"])

    def test_sticky_session_retains_existing_native_route(self):
        pins = {"session-a": {"profile": "build-native", "account": "account-a"}}
        row = self.plan([task()], pins=pins)["decisions"][0]
        self.assertEqual((row["profile"], row["account"]), ("build-native", "account-a"))

    def test_unavailable_pinned_account_holds_instead_of_switching(self):
        self.state["accounts"]["account-a"]["status"] = "unavailable"
        pins = {"session-a": {"profile": "build-native", "account": "account-a"}}
        self.assertEqual(self.plan([task()], pins=pins)["decisions"][0]["status"], "hold")

    def test_missing_budget_and_expired_snapshot_never_mean_unlimited(self):
        del self.state["quota_groups"]["group-a"]["remaining_day"]
        del self.state["quota_groups"]["group-b"]["remaining_day"]
        self.assertEqual(self.plan([task()])["decisions"][0]["status"], "hold")
        self.state["expires_at"] = 149
        self.assertEqual(self.plan([task()])["decisions"][0]["reason"], "snapshot-expired")

    def test_account_cooldown_is_not_cleared_or_retried(self):
        self.state["quota_groups"]["group-a"]["cooldown_until"] = 190
        self.state["quota_groups"]["group-b"]["cooldown_until"] = 190
        before = copy.deepcopy(self.state)
        self.assertEqual(self.plan([task()])["decisions"][0]["status"], "hold")
        self.assertEqual(self.state, before)

    def test_request_reservation_consumes_hour_and_day_together(self):
        self.state["quota_groups"]["group-a"].update(max_parallel=4, remaining_hour=1)
        self.state["quota_groups"]["group-b"]["remaining_day"] = 0
        rows = self.plan([task(), task("research", "scout", "session-r")])["decisions"]
        self.assertEqual([x["status"] for x in rows], ["selected", "hold"])

    def test_in_progress_work_is_never_reassigned(self):
        row = self.plan([task(state="running")])["decisions"][0]
        self.assertEqual(row["status"], "keep-running")
        self.assertNotIn("profile", row)

    def test_declared_vision_without_verified_vision_is_not_eligible(self):
        for p in self.team["profiles"]:
            p["capabilities"].append("image")
        self.assertEqual(self.plan([task(requires=["image"])])["decisions"][0]["status"], "hold")

    def test_dependency_wait_does_not_block_other_ready_work(self):
        rows = self.plan([task(depends_on=["research"]), task("other", "scout", "session-o")])["decisions"]
        self.assertEqual([x["status"] for x in rows], ["hold", "selected"])

    def test_duplicate_task_ids_and_split_identity_budgets_are_refused(self):
        with self.assertRaises(ValueError):
            self.plan([task(), task()])
        self.team["accounts"][1]["quota_group"] = "group-b"
        with self.assertRaises(ValueError):
            self.plan([task()])

    def test_cross_provider_account_reference_is_refused(self):
        self.team["accounts"][0]["provider"] = "anthropic"
        with self.assertRaises(ValueError):
            self.plan([task()])

    def test_same_native_handle_cannot_be_disguised_as_another_budget(self):
        self.team["accounts"][1].update(principal_ref="pretend-other-account", quota_group="group-b")
        with self.assertRaises(ValueError):
            self.plan([task()])

    def test_unknown_readiness_does_not_launch_a_route(self):
        self.state["profiles"] = {}
        self.assertEqual(self.plan([task()])["decisions"][0]["status"], "hold")

    def test_boolean_quota_is_not_an_integer_capacity(self):
        for value in self.state["quota_groups"].values():
            value["max_parallel"] = True
        self.assertEqual(self.plan([task()])["decisions"][0]["status"], "hold")

    def test_secret_fields_and_paid_fallback_are_refused(self):
        self.team["accounts"][0]["access_token"] = "synthetic-not-a-real-credential"
        with self.assertRaises(ValueError):
            self.plan([task()])
        del self.team["accounts"][0]["access_token"]
        self.team["paid_fallback"] = True
        with self.assertRaises(ValueError):
            self.plan([task()])

    def test_pure_plan_does_not_mutate_inputs_or_contact_network(self):
        before = copy.deepcopy((self.team, self.state))
        with patch.object(socket, "socket", side_effect=AssertionError("network forbidden")):
            result = self.plan([task()])
        self.assertFalse(result["executed"])
        self.assertEqual((self.team, self.state), before)

    def test_cli_returns_safe_error_without_echoing_private_input(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "team.json"
            self.team["accounts"][0]["api_key"] = "synthetic-private-canary"
            path.write_text(json.dumps(self.team))
            result = subprocess.run([sys.executable, str(ROOT / "scripts/legion_plan.py"),
                                     "--team", str(path), "--now", "150"], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertNotIn("synthetic-private-canary", result.stdout + result.stderr)


class PublishedExamplesTests(unittest.TestCase):
    def run_example(self, scenario, snapshot="synthetic-ready", pins=None):
        command = [sys.executable, str(ROOT / "scripts/legion_plan.py"), "--team",
                   str(ROOT / "examples/team.full.json"), "--tasks",
                   str(ROOT / f"examples/scenarios/{scenario}.json"), "--now", "1"]
        if snapshot:
            command += ["--snapshot", str(ROOT / f"examples/snapshots/{snapshot}.json")]
        if pins:
            command += ["--pins", str(ROOT / "examples/session-pins.synthetic.json")]
        result = subprocess.run(command, text=True, capture_output=True, check=True)
        return json.loads(result.stdout)

    def test_parallel_production_keeps_review_and_existing_workers_fenced(self):
        result = self.run_example("parallel-production")
        by_task = {x["task"]: x for x in result["decisions"]}
        for key in ["build-module", "prepare-document", "analyze-findings", "prepare-media"]:
            self.assertEqual(by_task[key]["status"], "selected")
        self.assertEqual(by_task["review-build"]["status"], "hold")
        self.assertEqual(by_task["existing-operator"]["status"], "keep-running")
        self.assertFalse(result["executed"])

    def test_published_pinned_cooldown_scenario_holds(self):
        result = self.run_example("sticky-session", "synthetic-codex-cooldown", pins=True)
        self.assertEqual(result["decisions"][0]["status"], "hold")
        self.assertEqual(result["decisions"][0]["reason"], "pinned-route-unavailable")

    def test_published_scenario_without_snapshot_does_not_select_work(self):
        result = self.run_example("parallel-production", snapshot=None)
        self.assertFalse(any(x["status"] == "selected" for x in result["decisions"]))


if __name__ == "__main__":
    unittest.main()
