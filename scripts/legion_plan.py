#!/usr/bin/env python3
"""Explain a team routing plan offline. No auth, network, dispatch or state writes."""
import argparse
import copy
import json
import math
from pathlib import Path
import re
import sys
import time


def fields(value, allowed, required=()):
    if not isinstance(value, dict) or set(value) - set(allowed) or not set(required) <= set(value):
        raise ValueError("unsupported or missing configuration field")


def alias(value):
    if not isinstance(value, str) or not re.fullmatch(r"[a-z][a-z0-9_-]{0,63}", value):
        raise ValueError("use non-identifying aliases")
    return value


def index(rows):
    if not isinstance(rows, list):
        raise ValueError("expected a list")
    result = {}
    for row in rows:
        key = alias(row.get("id")) if isinstance(row, dict) else None
        if key is None or key in result:
            raise ValueError("invalid or duplicate identity")
        result[key] = row
    return result


def strings(value):
    if not isinstance(value, list) or any(not isinstance(x, str) for x in value):
        raise ValueError("expected string list")
    return value


def validate(team, snapshot, tasks, pins):
    fields(team, {"schema_version", "kind", "quota_policy", "paid_fallback", "accounts", "profiles"},
           {"schema_version", "kind", "quota_policy", "paid_fallback", "accounts", "profiles"})
    if (team["schema_version"] != 1 or team["kind"] != "legion-offline-team"
            or team["quota_policy"] != "inherit-native" or team["paid_fallback"] is not False):
        raise ValueError("unsupported policy")
    accounts, profiles = index(team["accounts"]), index(team["profiles"])
    principals, handles = {}, {}
    for account in accounts.values():
        keys = {"id", "provider", "principal_ref", "quota_group", "auth_scope", "credential_ref"}
        fields(account, keys, keys)
        for key in keys:
            alias(account[key])
        identity = (account["provider"], account["quota_group"])
        previous = principals.setdefault(account["principal_ref"], identity)
        if previous != identity:
            raise ValueError("one principal cannot have split quota groups")
        handle = (account["provider"], account["auth_scope"], account["credential_ref"])
        owner = (account["principal_ref"], account["quota_group"])
        if handles.setdefault(handle, owner) != owner:
            raise ValueError("one native credential reference cannot have split identities")
    for profile in profiles.values():
        keys = {"id", "role", "provider", "model", "accounts", "capabilities", "data_classes", "priority"}
        fields(profile, keys, keys)
        alias(profile["role"])
        alias(profile["provider"])
        model = profile["model"]
        if (not isinstance(model, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_./:-]{0,159}", model)
                or "://" in model):
            raise ValueError("invalid model reference")
        if type(profile["priority"]) is not int or profile["priority"] < 0:
            raise ValueError("invalid preference")
        strings(profile["capabilities"])
        if not set(strings(profile["data_classes"])) <= {"public", "private"}:
            raise ValueError("unsupported data class")
        if not profile["accounts"]:
            raise ValueError("missing account reference")
        for key in strings(profile["accounts"]):
            if key not in accounts or accounts[key]["provider"] != profile["provider"]:
                raise ValueError("account/provider reference mismatch")
    index(tasks)
    for task in tasks:
        allowed = {"id", "role", "session", "state", "data_class", "requires", "request_budget", "depends_on"}
        fields(task, allowed, allowed - {"depends_on"})
        alias(task["role"])
        alias(task["session"])
        strings(task["requires"])
        strings(task.get("depends_on", []))
        if (task["state"] not in {"ready", "running", "completed", "blocked"}
                or task["data_class"] not in {"public", "private"}
                or type(task["request_budget"]) is not int or task["request_budget"] < 1):
            raise ValueError("invalid task contract")
    if not isinstance(pins, dict):
        raise ValueError("invalid session pins")
    for session, pin in pins.items():
        alias(session)
        fields(pin, {"profile", "account"}, {"profile", "account"})
        alias(pin["profile"])
        alias(pin["account"])
    if snapshot:
        keys = {"schema_version", "kind", "captured_at", "expires_at", "accounts", "profiles", "quota_groups"}
        fields(snapshot, keys, keys)
        if snapshot["schema_version"] != 1 or snapshot["kind"] not in {
                "legion-synthetic-snapshot", "legion-operator-snapshot"}:
            raise ValueError("unsupported snapshot")
        for key in ["captured_at", "expires_at"]:
            if type(snapshot[key]) not in {int, float} or not math.isfinite(snapshot[key]):
                raise ValueError("invalid snapshot time")
        for key in ["accounts", "profiles", "quota_groups"]:
            if not isinstance(snapshot[key], dict):
                raise ValueError("invalid snapshot map")
        for row in snapshot["accounts"].values():
            fields(row, {"status"}, {"status"})
        for row in snapshot["profiles"].values():
            fields(row, {"status", "verified_capabilities"}, {"status", "verified_capabilities"})
            strings(row["verified_capabilities"])
        for row in snapshot["quota_groups"].values():
            fields(row, {"max_parallel", "active", "remaining_hour", "remaining_day", "cooldown_until"})
    return accounts, profiles


def quota_available(row, budget, now):
    names = ["max_parallel", "active", "remaining_hour", "remaining_day", "cooldown_until"]
    if not row or any(type(row.get(k)) is not int or row[k] < 0 for k in names):
        return False
    return (row["cooldown_until"] <= now and row["active"] < row["max_parallel"]
            and row["remaining_hour"] >= budget and row["remaining_day"] >= budget)


def plan(team, snapshot, tasks, *, now, pins=None):
    pins = {} if pins is None else pins
    accounts, profiles = validate(team, snapshot, tasks, pins)
    if type(now) not in {int, float} or not math.isfinite(now):
        raise ValueError("invalid observation time")
    ledger = copy.deepcopy(snapshot.get("quota_groups", {}))
    result_pins = copy.deepcopy(pins)
    completed = {t["id"] for t in tasks if t["state"] == "completed"}
    busy_sessions = {t["session"] for t in tasks if t["state"] == "running"}
    decisions = []
    ordered = sorted(profiles.values(), key=lambda p: (p["priority"], p["id"]))

    def eligible(profile, account, task):
        account_state = snapshot.get("accounts", {}).get(account["id"], {})
        profile_state = snapshot.get("profiles", {}).get(profile["id"], {})
        requires = set(task["requires"])
        return (profile["role"] == task["role"] and task["data_class"] in profile["data_classes"]
                and requires <= set(profile["capabilities"])
                and requires <= set(profile_state.get("verified_capabilities", []))
                and profile_state.get("status") == "ready" and account_state.get("status") == "ready"
                and quota_available(ledger.get(account["quota_group"]), task["request_budget"], now))

    for task in tasks:
        row = {"task": task["id"], "status": "hold"}
        if task["state"] == "running":
            row.update(status="keep-running", reason="existing-worker-owns-work")
        elif task["state"] != "ready":
            row.update(status="skip", reason="not-ready")
        elif task["session"] in busy_sessions:
            row["reason"] = "session-busy"
        elif not set(task.get("depends_on", [])) <= completed:
            row["reason"] = "dependency-unfinished"
        elif not snapshot:
            row["reason"] = "snapshot-unavailable"
        elif not snapshot["captured_at"] <= now < snapshot["expires_at"]:
            row["reason"] = "snapshot-expired"
        else:
            pin = result_pins.get(task["session"])
            choices = []
            if pin:
                profile, account = profiles.get(pin["profile"]), accounts.get(pin["account"])
                if profile and account and account["id"] in profile["accounts"]:
                    choices = [(profile, account)]
            else:
                choices = [(profile, accounts[key]) for profile in ordered for key in profile["accounts"]]
            chosen = next(((p, a) for p, a in choices if eligible(p, a, task)), None)
            if chosen is None:
                row["reason"] = "pinned-route-unavailable" if pin else "no-eligible-route"
            else:
                profile, account = chosen
                group = account["quota_group"]
                ledger[group]["active"] += 1
                ledger[group]["remaining_hour"] -= task["request_budget"]
                ledger[group]["remaining_day"] -= task["request_budget"]
                row.update(status="selected", profile=profile["id"], account=account["id"],
                           quota_group=group, provider=profile["provider"], model=profile["model"],
                           reason="retained-session-pin" if pin else "eligible-role-route")
                result_pins[task["session"]] = {"profile": profile["id"], "account": account["id"]}
                busy_sessions.add(task["session"])
        decisions.append(row)
    return {"mode": "offline-only", "executed": False, "decisions": decisions,
            "session_pins": result_pins, "quota_reservations": ledger}


def read_json(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate JSON key")
            result[key] = value
        return result
    def invalid_constant(value):
        raise ValueError("nonstandard JSON number")
    return json.loads(Path(path).read_text(), object_pairs_hook=unique, parse_constant=invalid_constant)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--team", type=Path, default=Path(__file__).resolve().parents[1] / "examples/team.full.json")
    parser.add_argument("--snapshot", type=Path)
    parser.add_argument("--tasks", type=Path)
    parser.add_argument("--pins", type=Path)
    parser.add_argument("--now", type=float, default=None)
    args = parser.parse_args()
    try:
        result = plan(read_json(args.team), read_json(args.snapshot) if args.snapshot else {},
                      read_json(args.tasks) if args.tasks else [],
                      now=args.now if args.now is not None else time.time(),
                      pins=read_json(args.pins) if args.pins else None)
    except (ValueError, OSError, TypeError, KeyError, AttributeError):
        print("REFUSED: invalid team, snapshot, task or policy; input values omitted", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
