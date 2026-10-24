"""Copy into a disposable Hermes tests/hermes_cli tree; use its native runner."""
import argparse
import json
from pathlib import Path
import socket
import shutil

import pytest

from agent import credential_pool
from hermes_cli import config, profiles, profile_cmd
from hermes_constants import set_hermes_home_override, reset_hermes_home_override
from hermes_cli.subcommands.profile import build_profile_parser
from hermes_cli.subcommands.config import build_config_parser

FIXTURES = Path(__file__).parent / "fixtures/legion-native-fragments"
FILES = sorted(FIXTURES.glob("*.config.example.json"))


@pytest.mark.parametrize("fragment", FILES, ids=lambda path: path.stem)
def test_effective_native_config_preserves_model_pool_and_no_fallback(monkeypatch, fragment):
    raw = json.loads(fragment.read_text())
    target = config.get_config_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(raw))

    def denied(*args, **kwargs):
        raise AssertionError("network forbidden during offline configuration validation")

    monkeypatch.setattr(socket, "socket", denied)
    effective = config.load_config()
    assert effective["model"]["provider"] == raw["model"]["provider"]
    assert effective["model"]["default"] == raw["model"]["default"]
    assert effective["fallback_providers"] == []
    assert credential_pool.get_pool_strategy(raw["model"]["provider"]) == "fill_first"


def test_documented_profile_creation_uses_the_existing_native_parser():
    assert FILES, "copy the Legion native JSON fragments into the documented fixtures directory"
    parser = argparse.ArgumentParser()
    build_profile_parser(parser.add_subparsers(), cmd_profile=lambda: None)
    args = parser.parse_args(["profile", "create", "legion-artificer-codex", "--no-alias",
                              "--description", "Synthetic implementation worker"])
    assert args.profile_name == "legion-artificer-codex" and args.no_alias
    assert not args.clone and not args.clone_all and not args.clone_channels


def test_merging_a_fragment_disables_a_preexisting_legacy_fallback():
    assert FILES, "native fragments required"
    raw = json.loads(FILES[0].read_text())
    previous = {"fallback_model": {"provider": "example-provider", "model": "unapproved-route"}}
    previous.update(raw)
    target = config.get_config_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(previous))
    assert not config.load_config().get("fallback_model")


def test_actual_create_configure_and_soul_walkthrough(monkeypatch, tmp_path, capsys):
    # A host without a container service manager; service startup is outside this test.
    monkeypatch.setattr(profiles, "_s6_runtime_manager", lambda: None)

    class ExternalOperationForbidden(BaseException):
        pass

    def deny(*args, **kwargs):
        raise ExternalOperationForbidden("external operation blocked")

    monkeypatch.setattr(socket, "socket", deny)
    import gateway.control_socket
    monkeypatch.setattr(gateway.control_socket, "rescan_gateway_profiles", deny)
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    build_profile_parser(subparsers, cmd_profile=profile_cmd.cmd_profile)
    build_config_parser(subparsers, cmd_config=config.config_command)

    def native(*args):
        parsed = parser.parse_args(args)
        parsed.func(parsed)

    home = profiles._get_default_hermes_home().resolve()
    assert home.is_relative_to(tmp_path.resolve())
    capsys.readouterr()
    native("config", "path")
    assert capsys.readouterr().out.strip() == str(home / "config.yaml")
    names = ["legion-artificer-codex", "legion-artificer-claude", "legion-forge-web"]
    for name in names:
        native("profile", "create", name, "--no-alias", "--description", "Synthetic test duty")
        target = profiles.get_profile_dir(name)
        assert target.is_relative_to(home) and target.is_dir()
        assert profiles.read_profile_meta(target)["description"] == "Synthetic test duty"
        provider = "anthropic" if "claude" in name else "openai-codex"
        model = "chatgpt-web/example-model" if name.endswith("web") else "example-model"
        token = set_hermes_home_override(target)
        try:
            # A pre-existing operator cap must survive the documented targeted updates.
            native("config", "set", "delegation.max_concurrent_children", "2")
            for key, value in [
                ("model.provider", provider), ("model.default", model),
                ("fallback_providers", "[]"), ("fallback_model", "[]"),
                ("credential_pool_strategies." + provider, "fill_first"),
            ]:
                native("config", "set", key, value)
            effective = config.load_config()
            assert effective["model"]["provider"] == provider
            assert effective["model"]["default"] == model
            assert effective["fallback_providers"] == [] and not effective.get("fallback_model")
            assert effective["delegation"]["max_concurrent_children"] == 2
            assert credential_pool.get_pool_strategy(provider) == "fill_first"
            for key, expected in [("model.provider", provider), ("model.default", model),
                                  ("fallback_providers", []), ("fallback_model", [])]:
                capsys.readouterr()
                native("config", "get", key, "--json")
                assert json.loads(capsys.readouterr().out) == expected
        finally:
            reset_hermes_home_override(token)
        source = tmp_path / ("synthetic-" + name + ".md")
        source.write_text("# Synthetic role instructions\n")
        shutil.copy2(source, target / "SOUL.md")
        assert (target / "SOUL.md").read_text() == "# Synthetic role instructions\n"
    assert not (home / "auth.json").exists()
