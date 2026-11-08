"""Copy into native tests/hermes_cli with the JSON fixture; use scripts/run_tests.sh."""
import argparse
import copy
import json
from pathlib import Path
import socket

from hermes_cli import config, profiles, profile_cmd
from hermes_constants import reset_hermes_home_override, set_hermes_home_override
from hermes_cli.subcommands.config import build_config_parser
from hermes_cli.subcommands.profile import build_profile_parser

FRAGMENT = Path(__file__).parent / 'fixtures/legion-compact-worker.json'
DIRECT = {'kanban_show', 'kanban_complete', 'kanban_block', 'kanban_request_review',
    'kanban_request_changes', 'kanban_heartbeat', 'kanban_comment', 'session_search'}
LATER = {'kanban_list', 'kanban_create', 'kanban_link', 'kanban_attach',
    'kanban_attach_url', 'kanban_attachments'}


def test_native_create_apply_and_readback_preserve_unrelated_settings(monkeypatch, tmp_path, capsys):
    home = tmp_path / '.hermes'
    home.mkdir()
    monkeypatch.setattr(Path, 'home', lambda: tmp_path)
    monkeypatch.setenv('HERMES_HOME', str(home))
    monkeypatch.setattr(profiles, '_s6_runtime_manager', lambda: None)

    def denied(*args, **kwargs):
        raise AssertionError('No network or Gateway action in offline configuration verification')

    monkeypatch.setattr(socket, 'socket', denied)
    import gateway.control_socket
    monkeypatch.setattr(gateway.control_socket, 'rescan_gateway_profiles', denied)
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers()
    build_profile_parser(commands, cmd_profile=profile_cmd.cmd_profile)
    build_config_parser(commands, cmd_config=config.config_command)

    def native(*args):
        parsed = parser.parse_args(args)
        parsed.func(parsed)
        return capsys.readouterr().out

    capsys.readouterr()
    native('profile', 'create', 'compact-card-worker', '--no-alias', '--description',
        'Small Kanban and session-recall cards only')
    target = profiles.get_profile_dir('compact-card-worker')
    assert target.resolve().is_relative_to(tmp_path.resolve())
    token = set_hermes_home_override(target)
    try:
        native('config', 'set', 'model.provider', 'openai-codex')
        native('config', 'set', 'model.default', 'approved-fixture-model')
        native('config', 'set', 'delegation.max_concurrent_children', '2')
        native('config', 'set', 'goals.allow_self_management', 'false')
        before = copy.deepcopy(config.load_config())
        fragment = json.loads(FRAGMENT.read_text())
        values = [('toolsets', fragment['toolsets']),
            ('platform_toolsets.cli', fragment['platform_toolsets']['cli']),
            ('tools.tool_search.defer', fragment['tools']['tool_search']['defer'])]
        for key, value in values:
            native('config', 'set', key, json.dumps(value))
            assert json.loads(native('config', 'get', key, '--json')) == value
        after = copy.deepcopy(config.load_config())
        for item in (before, after):
            for keys in [('toolsets',), ('platform_toolsets', 'cli'),
                    ('tools', 'tool_search', 'defer')]:
                branch = item
                parents = []
                for key in keys[:-1]:
                    if key not in branch:
                        break
                    parents.append((branch, key))
                    branch = branch[key]
                else:
                    branch.pop(keys[-1], None)
                    for parent, key in reversed(parents):
                        if not parent[key]:
                            del parent[key]
        assert after == before
        assert not (target / 'auth.json').exists()
    finally:
        reset_hermes_home_override(token)


def test_native_worker_keeps_lifecycle_recall_and_deferred_capabilities(monkeypatch):
    import model_tools
    from tools import kanban_tools
    from tools.tool_search import assemble_tool_defs, session_tool_names, ToolSearchConfig
    from tools.tool_search_catalog import build_catalog
    from agent.shared_prompt_cache import canonical_tools
    from agent.transports import get_transport

    fragment = json.loads(FRAGMENT.read_text())
    path = config.get_config_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({**fragment, '_config_version': config.DEFAULT_CONFIG['_config_version']}))
    monkeypatch.setenv('HERMES_KANBAN_TASK', 'synthetic-offline-selection')
    monkeypatch.setattr(model_tools, '_is_dispatcher_owned_worker', lambda: True)
    monkeypatch.setattr(kanban_tools, '_is_dispatcher_owned_worker', lambda: True)
    raw = model_tools.get_tool_definitions(enabled_toolsets=['kanban', 'session_search'],
        quiet_mode=True, skip_tool_search_assembly=True)
    previous = copy.deepcopy(raw)
    result = assemble_tool_defs(raw, config=ToolSearchConfig.from_raw(fragment['tools']['tool_search']))
    eager = session_tool_names(result.tool_defs)
    assert DIRECT <= eager and not LATER & eager
    catalog = {entry.name: entry.schema for entry in build_catalog(raw)}
    assert LATER <= set(catalog)
    assert session_tool_names(raw) <= eager | set(catalog)
    wire = get_transport('codex_responses').build_kwargs(model='gpt-6.1-sol',
        messages=[{'role': 'user', 'content': 'Offline serialization only'}],
        tools=canonical_tools(result.tool_defs), is_codex_backend=True,
        base_url='https://chatgpt.com/backend-api/codex')
    assert {tool['name'] for tool in wire['tools']} == (
        set(eager) - {'tool_search'} | {'hermes_tool_search'})
    assert raw == previous
