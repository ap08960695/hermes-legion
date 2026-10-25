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

Historical v0.2.0 team acceptance: **34 companion tests passed, zero failures**, plus **36 native configuration/parser cases passed, zero failures**. The latter cover all 34 distributed fragments, the documented native create command, and safe merging over a pre-existing legacy fallback chain. These are separate groups; prior cumulative-patch results are historical and were not rerun for this documentation/planner-only update.


## Public usability audit and fixes (v0.2.1)

The review began with an anonymous clone and public v0.2.0 release download. All six documented planner examples ran offline, but targeted regressions exposed two gaps: a plan could select another task for an already busy session, and Python's JSON reader accepted nonstandard Infinity values that could keep a snapshot eligible indefinitely. New tests failed on the published implementation before the repair.

The planner now fences sessions with running work regardless of task ordering, reserves a session after its first selection, rejects NaN/Infinity input and requires finite observation/snapshot times. It still only prints recommendations; it cannot dispatch, authenticate, enforce native credential selection or change live state.

The setup guide now gives exact fresh-home/profile commands, targeted model/pool/fallback updates, model-placeholder refusals and SOUL installation. The installation guide includes public base-checkout commands. Changing a home variable is explicitly distinguished from selecting a CLI installation. Both current and legacy fallback chains are cleared while unrelated settings are preserved.

Fresh acceptance for this update: **38 companion tests passed, zero failures**; separately, **37 native cases passed, zero failures**, covering 34 config fragments, argument parsing, legacy fallback merging and one complete three-profile setup walkthrough. The walkthrough invokes native command parsers/handlers for create, config path/set/get and verifies an existing delegation cap survives. It uses isolated homes, synthetic instructions/models, disabled container-service registration and denied network/multiplexer access. No OAuth flow, credential selection, model request or live-worker test was run.

A separately guarded full CLI entrypoint probe stopped at the native home-bootstrap boundary; it is not counted as a passing full-launch test. No live source or bootstrap behavior was changed to make it pass. Packaged launchers, platform services, provider/model availability and real authentication remain operator checks. These limitations matter when adopting a template on another machine.

The cumulative source patch and its 279-file manifest are unchanged. The previous 964 Python and 56 UI results are historical, not newly rerun for this planner/documentation fix. Files, all reachable Git history, release payloads and known private identifiers/credential values are reviewed before publication; reports remain outside the repository.


## Offline preparation and diagnostics (v0.3.0)

New tools preview/export registered config and SOUL templates to a fresh private directory and inspect explicit JSON inputs/bundle integrity. The planner adds optional per-candidate explanations while preserving its original decisions, reservations and pins. Runtime/auth readiness stays unknown. No account mapping or quota snapshot is exported, and no native config is installed automatically.

Fresh companion acceptance: **64 tests passed, zero failures**. New regressions were observed failing before implementation, including missing offline tools/explanations, empty Web model references and false readiness for an empty team. The suite covers overwrite/link/live-root refusal, model/secret-field validation, all 34 registered exports, bundle corruption and semantic fallback checks, safe diagnostic output, stale snapshots, no network/process execution on the bundle path, explanation equivalence and pinned/busy sessions.

A checkout-inspection regression proved that Git could execute a configured filesystem-monitor helper. The verifier now disables it, external diff/text conversion, lazy fetch, prompts and optional locks. The regression passes without running that helper. On a fresh isolated pinned checkout, doctor passed both the original base and exact applied-source state; no Hermes import was used for these inspections. Git apply reported existing cumulative-patch whitespace warnings, not an apply refusal; the unchanged target hashes passed.

Separately, **37 native cases passed, zero failures**, using all **34 newly generated synthetic config fragments** as the native harness inputs, plus parser/legacy-fallback/three-profile setup checks. Use the existing native verification recipe; for generated fragments, copy each `profiles/<id>/config.example.json` to the fixture directory as `<id>.config.example.json`. The approved existing upstream-managed test environment and canonical runner were used with zero retries. No dependencies were installed. This is offline config acceptance, not actual provider authorization, model capability, packaged startup or live routing.

The 279-file cumulative source patch remains unchanged. Source/profile guards are compared around the work, and public files, reachable Git history and release payloads are scanned before publishing. Historical source/UI counts above are not rerun or added to these results.


## Repeated attachment fix (after v0.3.0)

The current main branch extends the cumulative patch to 280 files. Repeated built-in
references in one message now expand once per kind, target and line range. Original
user text and reference metadata remain intact. Distinct ranges remain separate;
plugin references retain their existing behavior. No cache survives to the next message.
The 16-expansion work limit applies to distinct built-in attachments.

Offline regressions first reproduced two failures: duplicate URL extraction and
16 copies of the same file preventing a later distinct file from being attached.
The final new regression file passes 5 cases; the existing reference, plugin,
concurrency, CLI and Gateway files pass 48 cases. These are separate cases, not
summed historical test runs. No model or real URL request was made.

One synthetic 30,000-character file referenced 16 times, with a 1,000,000-token
context limit, produced these results using the native preprocessor:

| Metric | Before | After |
|---|---:|---:|
| Estimated injected tokens | 120,176 | 7,511 |
| Output characters | 480,985 | 30,340 |
| Peak traced Python allocations (bytes) | 6,134,460 | 257,107 |

This single offline sample is not a whole-process RSS benchmark, billed token
measurement or evidence of savings across production workloads. Already-running
processes must load the changed module through their normal safe lifecycle before
runtime activation can be claimed. Provider quotas and fallback settings are unchanged.
The v0.3.0 tag and release remain immutable; these results describe the newer main branch.
