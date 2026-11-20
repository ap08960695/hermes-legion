"""Check the records from an isolated macOS Local split reconnect trial."""

import argparse
import json
from pathlib import Path


def verify(evidence: Path) -> None:
    def read(name):
        return json.loads((evidence / f"native-{name}.json").read_text())

    ready = read("walk-ready")
    assert ready["mode"] == "local" and ready["instance"], "missing Local gateway"
    assert {"gateway_running", "gateway_pid"} <= set(ready["statusKeys"])

    records = [read(name) for name in ("primary-type", "split-type", "reconnect", "replace")]
    for record in records:
        assert not record.get("error") and record["windowFocused"], "native focus was not established"
        assert record["loads"] == 1 and record["renderer"] == ready["rendererPid"], "renderer reloaded"

    primary, selected, reconnect, replaced = [record["result"] for record in records]
    pending, restored = reconnect["pending"], reconnect["restored"]
    assert primary["documentFocused"] and primary["main"]["focused"] and primary["main"]["hit"]
    assert primary["main"]["draft"] == "Primary draft stays here"

    for state in (selected, restored, replaced):
        assert state["status"] == "connected" and state["foreground"] == ready["profile"]
        assert state["route"] == primary["route"] and state["primaryTranscript"] and state["splitTranscript"]
        assert state["documentFocused"] and state["split"]["focused"] and state["split"]["hit"]
        assert state["activeTarget"] == selected["activeTarget"] and state["activeTarget"].startswith("tile:")
        assert state["main"]["draft"] == primary["main"]["draft"], "primary draft changed"

    assert reconnect["newGateway"] is True, "gateway instance did not change"
    assert pending["hold"] and pending["localGeneration"] and not pending["split"]["visible"]
    assert selected["bindings"][-1] and pending["bindings"] == selected["bindings"] + [None], (
        "split did not unbind in order"
    )
    runtime = reconnect["boundRuntime"]
    assert runtime and restored["bindings"] == replaced["bindings"] == pending["bindings"] + [runtime]
    assert restored["hold"] is False, "focus handoff did not finish"
    for state in (selected, restored):
        assert state["split"]["draft"] == "Review the draft"
        assert state["selected"] == "draft" and state["backward"], "backward selection was lost"
    assert replaced["split"]["draft"] == "Review the plan" and replaced["selected"] == ""

    process = read("result")
    assert process["walk_completed"] and process["failure"] is None
    assert process["unique_gateways"] == 2 and process["survivors"] == 0
    assert 0 < process["sampled_peak_hermes_processes"] <= 4
    assert 0 < process["sampled_peak_rss_with_observer_bytes"] < 4 * 1024**3
    assert process["elapsed_seconds"] >= 60, "native observation was too short"
    assert (evidence / "native-ssh-count.txt").read_text().strip() == "0", "Desktop SSH remained active"


def main():
    if not __debug__:
        raise SystemExit("Run this verifier with assertions enabled.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("evidence", type=Path, help="directory containing the split reconnect records")
    verify(parser.parse_args().evidence)
    print("PASS: Local split rebound, restored selection, and replaced only the selected text.")


if __name__ == "__main__":
    main()
