"""Run with existing Hermes dependencies and an explicitly admitted synthetic home."""
import argparse
import contextlib
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import sys
import sysconfig
import tempfile
import time


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_committed_selection(home):
    from pm.environments import committed_venv, install_state_dir, venv_python

    with tempfile.TemporaryDirectory(prefix="runtime-selection-", dir=home) as scratch:
        project = Path(scratch) / "source"
        project.mkdir()
        state = install_state_dir(project)
        selected = state / "environments" / "synthetic" / "venv"
        selected.mkdir(parents=True)
        (selected / "pyvenv.cfg").write_text("# synthetic metadata fixture\n")
        facts = state / "facts.json"
        facts.write_text(json.dumps({"packages": {"venv": {"environment": str(selected)}}}))
        assert not (project / "venv/bin/python").exists()
        assert committed_venv(project) == selected
        assert venv_python(selected) == selected / "bin/python"

        # An invalid committed generation must not fall back to a legacy directory.
        (project / "venv").mkdir()
        facts.write_text(json.dumps({"packages": {"venv": {"environment": str(project / "venv")}}}))
        try:
            committed_venv(project)
        except RuntimeError:
            pass
        else:
            raise AssertionError("invalid committed environment accepted")
        shutil.rmtree(state)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase", choices=("seed", "verify"))
    parser.add_argument("source", type=Path)
    parser.add_argument("home", type=Path)
    args = parser.parse_args()
    source, home = args.source.resolve(), args.home.resolve()
    assert os.environ.get("HERMES_DISABLE_LAZY_INSTALLS") == "1"
    assert Path(os.environ["HERMES_HOME"]).resolve() == home, "HERMES_HOME must match the fixture home"
    marker = home / ".legion-synthetic"
    assert marker.is_file() and marker.read_text() == "Hermes Legion synthetic native acceptance\n", \
        "synthetic admission marker required"
    assert sys.prefix != sys.base_prefix, "use the existing dependency-carrying interpreter"
    sys.path[:0] = [str(source), sysconfig.get_path("purelib"), sysconfig.get_path("platlib")]
    import hermes_bootstrap  # noqa: F401 - activate the native startup contract
    from hermes_cli import config, profile_cmd, profiles
    from hermes_cli.subcommands.config import build_config_parser
    from hermes_cli.subcommands.profile import build_profile_parser
    from hermes_constants import get_hermes_home
    from hermes_state import SessionDB
    from tools.registry import registry
    import tools.session_search_tool  # noqa: F401 - register the real tool

    assert Path(config.__file__).resolve().is_relative_to(source)
    assert get_hermes_home().resolve() == home
    check_committed_selection(home)
    native = argparse.ArgumentParser()
    commands = native.add_subparsers()
    build_config_parser(commands, cmd_config=config.config_command)
    build_profile_parser(commands, cmd_profile=profile_cmd.cmd_profile)

    def command(*argv):
        parsed = native.parse_args(argv)
        with contextlib.redirect_stdout(io.StringIO()):
            parsed.func(parsed)

    profile = profiles.get_profile_dir("legion-runtime-synthetic")
    session = "legion-runtime-retained"
    content = "Retained violetmarker47 decision: keep the blue plan. แผนเดิม"
    witness = home / "runtime-witness.json"
    if args.phase == "seed":
        assert not witness.exists(), "do not replay an already seeded fixture"
        command("config", "set", "delegation.max_concurrent_children", "2")
        command("config", "set", "model.default", "synthetic-unused-model")
        command("config", "set", "fallback_providers", "[]")
        command("config", "set", "fallback_model", "[]")
        command("profile", "create", "legion-runtime-synthetic", "--no-alias", "--no-skills",
                "--description", "Synthetic retained runtime profile")
        db = SessionDB(home / "state.db")
        try:
            db.create_session(session, source="cli")
            assert db.set_session_title(session, "Synthetic retained runtime decision")
            db.append_message(session, role="assistant", content=content)
            db._conn.execute("UPDATE sessions SET started_at = ? WHERE id = ?",
                             (time.time() - 30 * 86400, session))
            db._conn.commit()
        finally:
            db.close()
        files = [home / "config.yaml", home / "state.db",
                 *(p for p in profile.rglob("*") if p.is_file())]
        witness.write_text(json.dumps({p.relative_to(home).as_posix(): digest(p) for p in files}))

    expected = json.loads(witness.read_text())
    effective = config.load_config()
    assert effective["delegation"]["max_concurrent_children"] == 2
    assert effective["model"]["default"] == "synthetic-unused-model"
    assert effective["fallback_providers"] == [] and not effective.get("fallback_model")
    assert profile.resolve().is_relative_to(home)
    assert profiles.read_profile_meta(profile)["description"] == "Synthetic retained runtime profile"
    db = SessionDB(home / "state.db", read_only=True)
    try:
        assert db.get_session(session)["started_at"] < time.time() - 28 * 86400
        result = json.loads(registry.dispatch(
            "session_search", {"query": "violetmarker47", "detail": "full"}, db=db))
        assert result["success"] is True
        assert content in json.dumps(result, ensure_ascii=False)
        missing = json.loads(registry.dispatch("session_search", {"session_id": "missing-synthetic"}, db=db))
        assert missing["success"] is False
    finally:
        db.close()
    assert all(digest(home / name) == value for name, value in expected.items())
    print("PASS: committed runtime selection; native settings/profile/search continuity; fixture bytes preserved")


if __name__ == "__main__":
    main()
