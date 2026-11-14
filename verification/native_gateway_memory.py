"""Copy to native tests/gateway with fixtures/on-demand-gateway.json; use its runner."""
import argparse
import contextlib
import copy
import io
import json
import os
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

FRAGMENT = Path(__file__).parent / "fixtures/on-demand-gateway.json"


class GatewayMemoryPresetTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.home = self.root / "home"
        self.home.mkdir()
        self.context = self.root / "context"
        self.context.mkdir()
        (self.context / "AGENTS.md").write_text("WORKSPACE_CONTEXT_SENTINEL: preserve สวัสดี.\n")
        (self.home / "SOUL.md").write_text("PROFILE_SOUL_SENTINEL: synthetic offline profile.\n")
        (self.home / ".env").write_text("OPENAI_API_KEY=synthetic-fixture\n")
        env = patch.dict(os.environ, {"PATH": os.defpath, "HOME": str(self.root),
                        "HERMES_HOME": str(self.home), "TMPDIR": str(self.root),
                        "HERMES_DISABLE_LAZY_INSTALLS": "1"}, clear=True)
        env.start()
        self.addCleanup(env.stop)
        from hermes_constants import set_hermes_home_override, reset_hermes_home_override
        token = set_hermes_home_override(self.home)
        self.addCleanup(reset_hermes_home_override, token)
        import hermes_logging
        hermes_logging._reset_queued_handlers()
        hermes_logging._logging_initialized = False
        self.addCleanup(self.reset_logging)
        self.before = {
            "model": {"default": "synthetic-offline", "provider": "custom",
                      "base_url": "https://example.invalid/v1", "context_length": 131072},
            "agent": {"environment_probe": False, "max_turns": 3},
            "gateway": {"multiplex_profiles": False},
            "terminal": {"cwd": str(self.context)},
            "platform_toolsets": {"cli": ["todo"]},
            "delegation": {"max_concurrent_children": 1},
            "credential_pool": {}, "fallback_model": [], "fallback_providers": [],
            "auxiliary": {"title_generation": {"enabled": False}}, "mcp_servers": {},
        }
        self.path = self.home / "config.yaml"
        self.path.write_text(json.dumps(self.before, indent=2) + "\n")
        from hermes_cli.config import config_command
        from hermes_cli.subcommands.config import build_config_parser
        self.parser = argparse.ArgumentParser()
        build_config_parser(self.parser.add_subparsers(), cmd_config=config_command)

    @staticmethod
    def reset_logging():
        import hermes_logging
        hermes_logging._reset_queued_handlers()
        hermes_logging._logging_initialized = False
        hermes_logging.clear_session_context()

    def native(self, *argv):
        args = self.parser.parse_args(["config", *argv])
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            args.func(args)
        return output.getvalue()

    def apply_fragment(self):
        fragment = json.loads(FRAGMENT.read_text())
        for section, settings in fragment.items():
            for key, value in settings.items():
                dotted = section + "." + key
                self.native("set", dotted, json.dumps(value))
                self.assertEqual(json.loads(self.native("get", dotted, "--json")), value)

    def boot_runner(self):
        from gateway import run
        # Native boot bridges once; these tests reuse that import across isolated homes.
        run._bridge_config_to_env(run._load_bridge_config(self.path))
        return run.GatewayRunner()

    async def test_preset_reaches_mcp_consumers_without_changing_unrelated_config(self):
        self.before["mcp_servers"] = {
            "stdio": {"command": "synthetic-not-launched"},
            "stateful": {"command": "synthetic-not-launched", "idle_timeout_seconds": 0},
        }
        self.path.write_text(json.dumps(self.before, indent=2) + "\n")
        self.apply_fragment()
        from hermes_cli.config import read_user_config_raw
        from tools.mcp_tool_config import _load_mcp_config
        from tools.mcp_tool_discovery import _discovery_connect_concurrency
        expected = copy.deepcopy(self.before)
        expected["agent"]["gateway_startup_warmup_timeout"] = 0
        expected["mcp"] = {"memory_saving": True, "discovery_concurrency": 1}
        self.assertEqual(read_user_config_raw(self.path), expected)
        self.assertEqual(_discovery_connect_concurrency(), 1)
        servers = _load_mcp_config()
        self.assertIs(servers["stdio"]["lazy"], True)
        self.assertNotIn("idle_timeout_seconds", servers["stdio"])
        self.assertEqual(servers["stateful"]["idle_timeout_seconds"], 0)
        self.assertFalse((self.home / "auth.json").exists())

    async def test_default_still_runs_real_startup_warmup(self):
        runner = self.boot_runner()
        try:
            runner._start_startup_warmup()
            self.assertIsNotNone(runner._startup_warmup_task)
            await runner._await_startup_warmup()
            self.assertTrue(runner._startup_warmup_task.done())
            self.assertIsNone(runner._startup_warmup_task.exception())
        finally:
            await runner.stop()

    async def test_unselected_profile_keeps_its_policy(self):
        other = self.home / "profiles" / "unselected"
        other.mkdir(parents=True)
        path = other / "config.yaml"
        original = json.dumps({"agent": {"gateway_startup_warmup_timeout": 9},
                               "mcp": {"memory_saving": False, "discovery_concurrency": 2}}).encode()
        path.write_bytes(original)
        self.apply_fragment()
        self.assertEqual(path.read_bytes(), original)
        from hermes_constants import set_hermes_home_override, reset_hermes_home_override
        token = set_hermes_home_override(other)
        try:
            self.assertEqual(json.loads(self.native("get", "agent.gateway_startup_warmup_timeout", "--json")), 9)
            self.assertIs(json.loads(self.native("get", "mcp.memory_saving", "--json")), False)
            self.assertEqual(json.loads(self.native("get", "mcp.discovery_concurrency", "--json")), 2)
        finally:
            reset_hermes_home_override(token)

    async def test_preset_overrides_ambient_bridge_and_defers_warmup(self):
        self.apply_fragment()
        os.environ["HERMES_STARTUP_WARMUP_TIMEOUT"] = "777"
        from gateway.run import _startup_warmup_timeout_secs
        runner = self.boot_runner()
        try:
            self.assertEqual(_startup_warmup_timeout_secs(), 0)
            runner._start_startup_warmup()
            await runner._await_startup_warmup()
            self.assertIsNone(runner._startup_warmup_task)
        finally:
            await runner.stop()

    async def test_first_turn_with_warmup_disabled_has_context_and_tools(self):
        self.apply_fragment()
        from gateway.config import Platform
        from gateway.session import SessionSource
        from run_agent import AIAgent
        captured = []

        def model_boundary(agent, kwargs, **unused):
            captured.append(kwargs)
            return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(
                content="OFFLINE_COMPLETION", reasoning=None, reasoning_content=None,
                reasoning_details=None, tool_calls=None), finish_reason="stop")],
                usage=None, model="synthetic-offline")

        runner = self.boot_runner()
        try:
            runner._start_startup_warmup()
            self.assertIsNone(runner._startup_warmup_task)
            source = SessionSource(platform=Platform.LOCAL, chat_id="offline-chat",
                                   user_id="synthetic-user", chat_type="dm")
            with patch.object(AIAgent, "_interruptible_api_call", model_boundary), patch.object(
                AIAgent, "_interruptible_streaming_api_call", model_boundary
            ):
                result = await runner._run_agent("FIRST_TURN_SENTINEL สวัสดี", "", [], source,
                                                 "offline-first-turn", session_key="agent:main:offline")
            self.assertEqual(len(captured), 1)
            self.assertEqual(result["final_response"], "OFFLINE_COMPLETION")
            text = json.dumps(captured[0], ensure_ascii=False)
            for sentinel in ("FIRST_TURN_SENTINEL", "WORKSPACE_CONTEXT_SENTINEL", "PROFILE_SOUL_SENTINEL", "สวัสดี"):
                self.assertIn(sentinel, text)
            tools = captured[0]["tools"]
            names = {tool.get("function", {}).get("name") for tool in tools}
            self.assertTrue({"tool_call", "tool_describe", "tool_search"} <= names)
            self.assertIn("todo_list", json.dumps(tools))
        finally:
            await runner.stop()


if __name__ == "__main__":
    unittest.main()
