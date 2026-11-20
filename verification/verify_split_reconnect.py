"""Check the records from an isolated macOS Local split reconnect trial."""

import argparse
import json
from pathlib import Path


def verify(evidence: Path, *, switch_pane: bool = False) -> None:
    def read(name):
        return json.loads((evidence / f"native-{name}.json").read_text())

    ready = read("walk-ready")
    assert ready["mode"] == "local" and ready["instance"], "missing Local gateway"
    assert {"gateway_running", "gateway_pid"} <= set(ready["statusKeys"])

    def native(name):
        record = read(name)
        assert not record.get("error") and record["windowFocused"], "native focus was not established"
        assert record["loads"] == 1 and record["renderer"] == ready["rendererPid"], "renderer reloaded"
        return record["result"]

    primary, selected, reconnect, replaced = map(native, ("primary-type", "split-type", "reconnect", "replace"))
    pending, restored = reconnect["pending"], reconnect["restored"]
    assert primary["documentFocused"] and primary["main"]["focused"] and primary["main"]["hit"]
    assert primary["main"]["draft"] == "Primary draft stays here"

    def view(state, pane, target):
        assert state["status"] == "connected" and state["foreground"] == ready["profile"]
        assert state["route"] == primary["route"] and state["primaryTranscript"] and state["splitTranscript"]
        assert state["documentFocused"] and state[pane]["focused"] and state[pane]["hit"]
        assert state["activeTarget"] == target

    assert reconnect["newGateway"] is True, "gateway instance did not change"
    assert pending["hold"] and pending["localGeneration"] and pending["split"]["visible"] is False
    assert selected["bindings"][-1] and pending["bindings"] == selected["bindings"] + [None], (
        "split did not unbind in order"
    )
    runtime = reconnect["boundRuntime"]
    assert runtime and restored["bindings"] == replaced["bindings"] == pending["bindings"] + [runtime]
    assert restored["hold"] is False, "focus handoff did not finish"

    split_target = selected["activeTarget"]
    assert split_target.startswith("tile:")
    view(selected, "split", split_target)
    assert selected["main"]["draft"] == primary["main"]["draft"], "primary draft changed"
    assert selected["split"]["draft"] == "Review the draft"
    assert selected["selected"] == "draft" and selected["backward"], "initial split selection was lost"

    if switch_pane:
        before_switch, switched, settled = map(native, ("pending", "switch", "settled"))
        assert before_switch["documentFocused"] and before_switch["main"]["focused"] is False
        assert before_switch["main"]["draft"] == primary["main"]["draft"]
        for state in (before_switch, switched):
            assert state["bindings"] == pending["bindings"] and state["hold"] and state["localGeneration"]
            assert state["split"]["visible"] is False, "switch must precede the rebind"
        for state in (switched, pending, restored, settled):
            view(state, "main", "main")
            assert state["main"]["draft"] == primary["main"]["draft"], "primary draft changed"
            assert state["mainSelected"] == "here" and state["backward"], "primary selection changed"
            assert state["mainSelectionOffsets"] == [24, 20], "primary selection offsets changed"
        assert settled["bindings"] == restored["bindings"] and settled["hold"] is False
        assert settled["selectionWatchSeconds"] >= settled["postRebindSeconds"] >= 60
        assert settled["violations"] == [], "primary focus or selection changed during rebind"
        view(replaced, "main", "main")
        assert replaced["main"]["draft"] == "Primary draft stays intact" and replaced["mainSelected"] == ""
        for state in (restored, settled, replaced):
            assert state["split"]["draft"] == "Review the draft", "split draft changed"
    else:
        for state in (restored, replaced):
            view(state, "split", split_target)
            assert state["main"]["draft"] == primary["main"]["draft"], "primary draft changed"
        assert restored["split"]["draft"] == "Review the draft"
        assert restored["selected"] == "draft" and restored["backward"], "backward selection was lost"
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
    parser.add_argument("--switch-pane", action="store_true", help="verify switching to the primary pane during rebind")
    args = parser.parse_args()
    verify(args.evidence, switch_pane=args.switch_pane)
    if args.switch_pane:
        print("PASS: Primary focus and selection survived the Local split rebind and native replacement.")
    else:
        print("PASS: Local split rebound, restored selection, and replaced only the selected text.")


if __name__ == "__main__":
    main()
