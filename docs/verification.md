# Verification record

## Initial cumulative patch acceptance (v0.1.0)

This record describes the exported artifact's offline acceptance. It contains no production logs, prompts, accounts, task/run IDs or private machine paths.

| Check | Result | Scope |
|---|---|---|
| Patch base verification | PASS | Exact publicly available upstream commit and all 279 before hashes |
| Normal Git apply check and apply | PASS | Separate disposable checkout, not a running installation |
| Installed source verification | PASS | All 279 resulting hashes match the export manifest |
| Reverse apply and base restoration | PASS | All original bytes and absence states restored, then reapplied for regressions |
| Python source syntax | PASS | 242 changed/added Python source and test files |
| Exported Hermes Python regressions | 964 passed, 0 failed | 109 input files through the canonical per-file runner, zero retries, three workers |
| Desktop UI unit regressions | 56 passed, 0 failed | Seven changed UI test files; no rendered desktop/model test |
| Companion tool regressions | 11 passed, 0 failed | Wrong revision, unrelated work, existing new targets, traversal, symlinks, changed/missing/unlisted files |
| Roles and skills | Eight roles, ten skills | Rewritten English templates; no live persona/configuration export |
| Working-tree secret scan | PASS | Gitleaks 8.30.1, default rules, fully redacted output, allow-comment bypass disabled |
| Privacy review | PASS for reviewed identifiers and file inventory | Every public file plus full patch contents; separate private identifiers review |
| Historical-secret detection control | PASS | A synthetic local-only credential was committed then deleted; current-tree scan was clean and all-history scan detected it |

macOS-tagged Python checks in five files were skipped on the Linux test host. This is not macOS acceptance, a full upstream test-suite result, or a whole-repository lint/build claim. The desktop tests are unit tests, not visual or live-session acceptance.

Three test files were generalized for distribution: a machine-specific home assertion became a portable assertion, a diagnostic sentinel became short synthetic data, and a credential-redaction fixture now constructs unmistakably artificial input at runtime. No live source file was edited for these export changes.

The dedicated scanner checks both the exact committed tree and all reachable Git history before publication. The initial history is created fresh with a neutral project author/committer, and the final archive is generated from Git's explicit tree rather than a working-directory copy. `RELEASE-MANIFEST.json` records every payload file's SHA-256; the manifest itself is bound by the Git commit and archive hash.

All upstream-base source tests used the existing approved test environment. The test runner's normal isolation created temporary homes; no model acceptance job, provider/allowance probe, dependency install or service restart was used to create evidence. Private source hashes were compared afterward and remained unchanged.

No general token-saving percentage, billing saving, cross-bot provider-cache origin, unlimited cache retention or live startup speedup is established by this release. Measure actual authorized work with matched identities and honest coverage if evaluating impact on your own installation.

## Team and multi-account update (v0.2.0)

The cumulative 279-file Hermes patch is unchanged. This update adds a standard-library-only offline planner, fifteen public role templates, a 34-profile topology, six Web specialists, native config fragments and English setup guides. Account identities, usage snapshots, tasks and budgets are synthetic. No live profile/account is exported or changed.

The companion's full unittest suite covers new-session route choice, public/private gates, capability readiness, shared account budgets/duplicate aliases, hour/day/parallel limits, cooldown, missing/stale evidence, exact session pins, existing running work, dependency waits, provider mismatch, secret-field rejection and no network/input mutations. New behavior was observed failing before implementation, including a reproduced duplicate-handle/split-budget case. Current release acceptance is regenerated after all files are finalized; previous Hermes regression counts above are not added to the new companion-test count or represented as newly rerun.

The planner is not a native account selector or live quota enforcement layer. Setup documentation separates native pool ownership and manual profile configuration from offline recommendations. A real-bot/model acceptance run was not requested or performed for this update.

### Reproduce native config compatibility offline

In the isolated, supported Hermes checkout, copy `verification/native_profile_examples.py` to `tests/hermes_cli/test_legion_native_profile_examples.py` and copy the 34 `profiles/native/*.config.example.json` files to `tests/hermes_cli/fixtures/legion-native-fragments/`. Run that test file through the checkout's canonical `scripts/run_tests.sh` and existing managed test environment, with retries disabled. This uses Hermes' own isolated-home fixtures, effective config loader, pool-strategy reader and profile argument parser; no actual credential pool is loaded, no account is logged in, and socket creation is denied during effective-config checks. The test refuses a missing fragment directory instead of reporting an empty run as success.

Current team acceptance: **34 companion tests passed, zero failures**, plus **36 native configuration/parser cases passed, zero failures**. The latter cover all 34 distributed fragments, the documented native create command, and safe merging over a pre-existing legacy fallback chain. These are separate groups; prior cumulative-patch results are historical and were not rerun for this documentation/planner-only update.
