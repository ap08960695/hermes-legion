#!/usr/bin/env python3
"""Compare assertion and suite failures in two Vitest JSON reports."""
import argparse
from collections import Counter
import json
from pathlib import Path
import sys


def failure_headline(message, roots):
    # Stack locations vary between checkouts. Keep the reported error headline.
    headline = message.partition("\n")[0]
    for root in roots:
        headline = headline.replace(root, "<checkout>")
    return headline


def read_report(path, root):
    root = root.absolute()
    real_root = root.resolve()
    roots = sorted({str(root), str(real_root)}, key=len, reverse=True)
    data = json.loads(path.read_text(encoding="utf-8"))
    executed = Counter()
    failures = Counter()
    total = failed = 0
    for suite in data["testResults"]:
        path_in_report = Path(suite["name"])
        if path_in_report.is_relative_to(root):
            source = path_in_report.relative_to(root).as_posix()
        else:
            source = path_in_report.resolve().relative_to(real_root).as_posix()
        suite_failures = 0
        for test in suite["assertionResults"]:
            total += 1
            status = test["status"]
            identity = (source, *test["ancestorTitles"], test["title"])
            if status in ("passed", "failed"):
                executed[identity] += 1
            elif status not in ("pending", "skipped", "todo"):
                raise ValueError("unknown assertion status")
            if status == "failed":
                suite_failures += 1
                reason = tuple(failure_headline(message, roots) for message in test["failureMessages"])
                failures[("assertion", identity, reason)] += 1
        failed += suite_failures
        if suite["status"] == "failed" and (suite["message"] or not suite_failures):
            reason = (failure_headline(suite["message"], roots),)
            failures[("suite", (source,), reason)] += 1
    if not executed or total != data["numTotalTests"] or failed != data["numFailedTests"]:
        raise ValueError("missing assertions or inconsistent Vitest totals")
    return executed, failures


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for side in ("baseline", "candidate"):
        parser.add_argument(side, type=Path, help=f"{side} Vitest JSON report")
        parser.add_argument(f"{side}_root", type=Path, help=f"{side} Desktop test directory")
    args = parser.parse_args()
    try:
        before, before_failures = read_report(args.baseline, args.baseline_root)
        after, after_failures = read_report(args.candidate, args.candidate_root)
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        print(f"Invalid Vitest report: {exc}", file=sys.stderr)
        return 2

    missing = before - after
    regressions = after_failures - before_failures
    for identity, count in sorted(missing.items()):
        print(f"Missing or skipped assertion ({count}): {' :: '.join(identity)}")
    for (kind, identity, reasons), count in sorted(regressions.items()):
        print(f"New or changed {kind} failure ({count}): {' :: '.join(identity)}")
        for reason in filter(None, reasons):
            print(f"  {reason}")
    if missing or regressions:
        return 1
    print("Recorded assertions and suite failures match baseline or improved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
