"""Copy into a disposable Hermes tests/hermes_cli tree; use its native runner."""
import argparse
import json
from pathlib import Path
import socket

import pytest

from agent import credential_pool
from hermes_cli import config
from hermes_cli.subcommands.profile import build_profile_parser

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
