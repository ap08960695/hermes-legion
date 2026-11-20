"""Check the evidence from an isolated macOS Local gateway Retry trial."""

import argparse
import ipaddress
import json
from pathlib import Path
from urllib.parse import urlsplit


def verify(evidence: Path) -> None:
    def read(name):
        return json.loads((evidence / f"native-recovery-{name}.json").read_text())

    first, probes, repaired = (read(name) for name in ("first", "probes", "repaired-before-retry"))
    for sample in (first, probes, repaired):
        assert sample["ensures"] == 1 and sample["resets"] == 0, "failure did not stay latched"
        assert sample["result"]["retryable"] is False
    assert first["result"]["retryEnabled"] and repaired["result"]["retryEnabled"]
    failures = probes["result"]["errors"]
    assert [row["origin"] for row in failures] == ["connection", "api"] * 3
    assert len({row["diagnostic"] for row in failures}) == 1

    assert read("retry")["result"]["clicked"] is True
    assert read("reset") == {"resets": 1, "ensures": 1}
    trace = evidence / "native-recovery-ensure-trace.jsonl"
    launches = [json.loads(row) for row in trace.read_text().splitlines()]
    assert [(row["ensures"], row["resets"], row["repaired"]) for row in launches] == [
        (1, 0, False), (2, 1, True)
    ]

    recovered, drafted, steady = (read(name) for name in ("recovered", "drafted", "steady"))
    connection = recovered["result"]["connection"]
    endpoint = urlsplit(connection["baseUrl"])
    assert connection["mode"] == "local" and connection["instance"]
    assert endpoint.scheme == "http" and endpoint.port and ipaddress.ip_address(endpoint.hostname).is_loopback
    for sample in (recovered, drafted, steady):
        assert sample["loads"] == first["loads"] + 1
        assert sample["ensures"] == 2 and sample["resets"] == 1
        result = sample["result"]
        assert result["connection"] == connection and result["connected"] and result["composer"]
        assert {"gateway_running", "gateway_pid"} <= set(result["statusKeys"])
    assert drafted["result"]["draft"] == steady["result"]["draft"] == "Local recovery fixture draft"

    process = read("process")
    assert process["walk_completed"] and process["failure"] is None
    assert process["unique_gateways"] == 1 and process["survivors"] == 0
    assert process["sampled_peak_hermes_processes"] <= 4
    assert process["sampled_peak_rss_with_observer_bytes"] < 4 * 1024**3
    assert process["elapsed_seconds"] >= 60


def main():
    if not __debug__:
        raise SystemExit("Run this verifier with assertions enabled.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("evidence", type=Path, help="directory containing the Local Retry trial records")
    verify(parser.parse_args().evidence)
    print("PASS: Local Retry recovered a usable composer on one loopback gateway.")


if __name__ == "__main__":
    main()
