"""Check the receipt comparator through its command-line entry point."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/compare_desktop_receipts.py"


class CompareDesktopReceiptsTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)

    def report(self, name, failed, *, message="AssertionError: comparison failed"):
        root = self.root / name
        root.mkdir()
        reports = self.root / f"{name}.json"
        reports.write_text(json.dumps({
            "numTotalTests": 2,
            "numFailedTests": len(failed),
            "testResults": [{
                "name": str(root / "src" / "fixture.test.ts"),
                "status": "failed" if failed else "passed",
                "message": "",
                "assertionResults": [{
                    "ancestorTitles": ["group"],
                    "title": test,
                    "status": "failed" if test in failed else "passed",
                    "failureMessages": [f"{message}\n    at {root}/fixture:12:1"] if test in failed else [],
                } for test in ("one", "two")],
            }],
        }))
        return reports, root

    def compare(self, baseline, candidate):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *map(str, (*baseline, *candidate))],
            capture_output=True, text=True, check=False,
        )

    def test_equal_failure_counts_can_hide_a_new_failing_test(self):
        result = self.compare(self.report("before", {"one"}), self.report("after", {"two"}))
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn("src/fixture.test.ts :: group :: two", result.stdout)
        self.assertNotIn("group :: one", result.stdout)

    def test_existing_failure_matches_across_checkout_roots(self):
        result = self.compare(self.report("before", {"one"}), self.report("after", {"one"}))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_report_paths_may_use_a_checkout_symlink(self):
        baseline = self.report("before", set())
        report, checkout = self.report("after", set())
        alias = self.root / "alias"
        alias.symlink_to(checkout, target_is_directory=True)
        report.write_text(report.read_text().replace(str(checkout), str(alias)))
        result = self.compare(baseline, (report, alias))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_same_test_with_a_different_failure_requires_review(self):
        result = self.compare(self.report("before", {"one"}),
                              self.report("after", {"one"}, message="TypeError: new cause"))
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn("TypeError: new cause", result.stdout)

    def test_incomplete_report_refused(self):
        baseline = self.report("before", {"one"})
        candidate = self.report("after", set())
        data = json.loads(candidate[0].read_text())
        data["testResults"][0]["assertionResults"].pop()
        candidate[0].write_text(json.dumps(data))
        result = self.compare(baseline, candidate)
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)

    def test_new_collection_error_and_lost_assertion_require_review(self):
        baseline = self.report("before", set())
        candidate = self.report("after", set())
        data = json.loads(candidate[0].read_text())
        suite = data["testResults"][0]
        suite["assertionResults"][0]["status"] = "skipped"
        data["testResults"].append({
            "name": str(candidate[1] / "src" / "collection.test.ts"),
            "status": "failed",
            "message": "Failed to import fixture",
            "assertionResults": [],
        })
        candidate[0].write_text(json.dumps(data))
        result = self.compare(baseline, candidate)
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn("Missing or skipped assertion (1): src/fixture.test.ts :: group :: one", result.stdout)
        self.assertIn("New or changed suite failure (1): src/collection.test.ts", result.stdout)
