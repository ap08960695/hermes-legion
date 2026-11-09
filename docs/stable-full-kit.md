# Consolidated stable source and Desktop kit

This is the complete **980-path** Legion source, interface and optimization alternative
for upstream Hermes **v0.22.5**, commit
`bf0203a794a07aac3ff764972ab9087baa4e4f4e`. It replaces the need to assemble the
historical cumulative kit and the smaller stable units. It is not an upstream release,
an account installer, a prebuilt application or an in-place migration script.

The [manifest](../patches/stable-full/manifest.json) pins every before/after file hash.
The [test selection](../patches/stable-full/test-selection.json) records the offline
Python and Desktop selection. No dependency or lockfile change is included.

## Goal-judge verdict reuse (v0.8.37)

The kit now covers 983 paths. `hermes_cli/goals_judge_memo.py` reuses the judge's
`done`/`blocked`/`continue` verdict for an input identical except for its clock, so
a repeated response does not cost a second judge call. See
[goal-judge memo](goal-judge-memo.md).

## Retention parity on macOS (v0.8.36)

The companion retention helper now also runs when lsof cannot see a closed vendor
agent, and when a short-lived `ping` is active. Native source and patch are unchanged.

## Retention runs again (v0.8.35)

The companion retention helper no longer gives up on non-dumpable session daemons,
continues past an entry it cannot remove, and removes links inside idle trees without
following them. Native source and the stable-full patch are unchanged. See
[storage and backups](storage-and-backups.md#retention-that-can-actually-run-v0835).

## Goal ensure usage (v0.8.34)

The goal-driven-execution skill now shows the exact `hermes goal ensure` form:
contract text as one argument or heredoc on stdin, with `outcome:` and
`verification:` lines. In an isolated live Captain card, the model read the
skill, checked `hermes goal status`, then guessed nonexistent `--outcome` and
`--verification` flags that native argparse rejects. Native source and the
stable-full patch are unchanged.

## Verification update (v0.8.33)

All twelve native check groups pass on Linux. Shared numeric owner checks and
bounded Desktop-test imports preserve existing behavior. Native verification
covers 497 Linux cases across separate file runs and 496 macOS cases in one
33-file run, with host-specific skips. Fifteen runtime and eighteen test files
are installed on both hosts; the kit now pins 980 paths. Desktop assets and
lockfiles remain unchanged. See [the exact scope and installation limits](native-checks-and-test-memory.md).

## Included behavior

- [Official Codex alias usage accounting](codex-alias-usage.md), avoiding unnecessary pricing-catalog reads while retaining actual token usage.

- [Lower diagnostic read memory and latency](diagnostic-read-efficiency.md).

- [Work tracking and independently reviewed delivery](tracked-delivery.md).

- [Refined charts, tables and diagrams](rich-output-presentation.md).


- [Bounded interpreter work for recall Unicode validation](recall-unicode-work.md), without per-character Python callbacks.

- [Missing-skill worker results](missing-skill-worker-results.md), settling known preload failures with an actionable diagnostic.
- [Scheduled and revision handoff termination](scheduled-review-handoffs.md), preserving native landing states without a follow-up model acknowledgement.

- [Adaptive recall payload loading](adaptive-recall-hydration.md), keeping compact result counts without loading discarded neighbor bodies.

- [Verified blocked-worker handoffs](blocked-worker-handoff.md), returning the saved blocker without an extra model call and preserving final-iteration holds.

- [Null-section settings merge parity](settings-null-sections.md), preserving an accepted nested edit when a later null section is ignored by the native API.
- [Ordered config type changes](settings-null-sections.md#ordered-type-changes-v0816), retaining separate writes when combining them would revive removed fields.

- Focus navigation, saved-chat history, always-visible device/profile context, bot
  configuration, Hub collections, native file previews, rich Markdown and Workflow.
- Role-specific THINK/ACTION plans, independent review, bounded handoffs, idempotent
  card creation, ready-work dispatch and native terminal-stop behavior.
- Bounded file and history reads, structured/CJK recall, compaction publication and
  recovery, prompt-prefix reuse, cache cohorts and privacy-preserving usage attribution.
- Profile/account-scoped metadata caches, process/cache diagnostics, derived-cache
  retention, protected active scratch work and update-preservation recovery.
- Optional per-model reasoning effort ceilings after explicit overrides, including owner-bound frozen sessions and auxiliary requests. See the [effort-limit guide](reasoning-effort-limits.md).
- Existing transport, owner/claim, review, data-clearance, quota and emergency-stop gates.

No account grants, conversations, live boards, operator profiles or production data
are bundled. Legacy technical profile identifiers remain where the native compatibility
or owner gate requires them; these are not imported personas or grants to impersonate
that owner. The English role templates are separate reference material.

## Prepare a new isolated checkout

Run from the Legion repository root. Choose an unused destination outside the running
installation. The source download is public and makes no model request.

```sh
set -eu
export LEGION_ROOT="$(pwd)"
export HERMES_CHECKOUT="/absolute/path/to/new-hermes-stable-checkout"
legion_manifest="$LEGION_ROOT/patches/stable-full/manifest.json"
legion_patch="$LEGION_ROOT/patches/stable-full/0001-stable-full.patch"
legion_base_commit="$(python3 -c 'import json; print(json.load(open("patches/stable-full/manifest.json"))["upstream_commit"])')"
test ! -e "$HERMES_CHECKOUT"
git clone --depth 1 --branch v0.22.5 --no-checkout https://github.com/NousResearch/hermes-agent.git "$HERMES_CHECKOUT"
git -C "$HERMES_CHECKOUT" checkout --detach "$legion_base_commit"
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase base --manifest "$legion_manifest"
git -C "$HERMES_CHECKOUT" apply --check "$legion_patch"
git -C "$HERMES_CHECKOUT" apply "$legion_patch"
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase installed --manifest "$legion_manifest"
```

A moved release tag, different source, unrelated edits or pre-existing added target
must refuse. Do not force, fuzz, reset another person's work or stack full alternatives.
The patch has one line of context; exact before hashes and the pinned commit remain
mandatory. Native Git attributes preserve the PowerShell checkout's CRLF exception.

Use upstream's native package manager and matching frozen dependency groups. Do not
repair an environment with raw pip/uv or substitute a different Python/Node runtime.
Follow [test and adopt](installation-and-rollback.md#test-and-adopt) and the
[Mac guide](macos-install-update.md). Source application does not rebuild or reload an
already running Desktop or Gateway.

## Reproduce the offline selection

After preparing the existing upstream frozen test environment, run the Python selection
through the native runner, from the patched checkout. This example only forwards the
recorded paths; it does not install dependencies or call a model.

```sh
cd "$HERMES_CHECKOUT"
python3 - <<'PY'
import json, os, pathlib, subprocess
selection = pathlib.Path(os.environ["LEGION_ROOT"]) / "patches/stable-full/test-selection.json"
files = json.loads(selection.read_text())["python_test_files"]
env = {**os.environ, "HERMES_TEST_FILE_RETRIES": "0", "HERMES_TEST_WORKERS": "2"}
raise SystemExit(subprocess.call(["scripts/run_tests.sh", *files], env=env))
PY
```

For Desktop, use the same selection's `desktop_test_files` relative to `apps/desktop`
with the existing Vitest runner, then run the full native TypeScript check and Desktop
build. Test and packaging tools must already be admitted by the native package manager.
Do not use a running user's renderer or provider account as a test fixture.

## Owner-safe history and draft recovery

A link with an explicit connection/profile opens that owner's retained history.
If a same-ID conversation is already open for another owner, the native app
opens a separate window instead of retargeting the original runtime. Repeated
same-owner links reuse the existing window. An unavailable window bridge
reports an error and leaves the original window intact.

Unsent text and uncertain-send retry identity are isolated by connection,
profile, target profile and session. Reloading or closing a window restores
only that owner's saved text. Retention is capped at 50 saved scopes per owner;
updates do not scan every saved draft. Attachments remain memory-only. Accepted sends
never clear a newer draft after the clicked text was already consumed. External
submissions do not own or clear the editor draft.

Older unassigned drafts are retained separately, never attributed to the current
profile automatically. When an unassigned draft exists and the editor is empty,
use the recovery notice to copy it into the current editor. Review the content
before sending. Recovery never sends automatically and keeps the original.
Profile rename and compression lineage transfers preserve the source if writing
the destination fails. Keep existing quotas and disable paid fallback as before.

## First-use interface checks

1. Open **All features → Plugins**. The bundled Desktop **Kanban** plugin is intentionally
   off by default upstream. Enable that plugin explicitly if you want Work to show the
   board and Workflow. This is a Desktop presentation opt-in, not permission to start
   the dispatcher or release an emergency stop. Without it, Work shows native agent activity.
2. In **Bots → Edit profile**, save the role, family, mode, counterpart and eligible model
   and effort. Reopen to verify persistence. Configure both sides for a reciprocal pair;
   one-way pairing is displayed honestly and is not a ready execution lane.
3. In **Work → Workflow**, select a downstream card, inspect its actual upstream links
   and recorded bot journey, then open the original card if needed. A dependency edge
   does not prove execution or completion; absent run evidence stays absent.
4. In **Hub**, create a collection, choose its members explicitly and save a page or
   import a file. Chat files stay private until shared. Removal uses recoverable trash.
5. In **History**, open a retained conversation and verify its content. Opening history
   is separate from submitting a prompt or resuming a goal.

Test within a separate synthetic home first. After acceptance, adopt the rebuilt native
application only at idle, preserving drafts, sessions and worker ownership. An updater
refusal is a gate to diagnose, not permission to bypass custody or authentication.

## Evidence and limits

The broad offline run completed 218 Python files: **2,737 passed, 13 skipped, zero
failures**, with two workers and zero file retries. Desktop completed **60 files,
383 passing tests**; full TypeScript and the native Linux renderer/main build passed.
After two synthetic scanner fixtures were clarified, their two files were separately
rerun: **33 passed**. Those cases overlap the broad selection and must not be added to it.

Native clean-base apply, installed-byte verification, reverse and reapply passed for
all 667 paths in the original baseline on **Linux and macOS**. These are source compatibility results, not a
claim that the entire Python/UI suite ran on macOS. Linux rendered checks use the fresh
built source-mode Electron application and its actual backend in a separate synthetic
home, with only localhost model metadata and zero inference. The 11 interaction checkpoints include explicit Kanban opt-in, upstream-card navigation,
Hub collection/page saves and retained-message reopening. Two blocked external catalog
requests produced expected DNS errors under the network-denied fixture; this is not
a claim of universally clean network logs. These checks do not certify a downloaded
packaged application, original stored sessions or every UI feature.

The suite initially exposed stale test interfaces after upstream's facade changes.
Fixtures were reconciled against the native owner-policy and bounded-read contracts;
no production permission or completion rule was weakened to satisfy them. Test-only
synthetic identifiers are not production receipts.

Matching cache keys/prefixes provide comparison evidence, not a guarantee of shared
provider cache. Idle time alone does not establish cache expiry. No universal cost,
quota, RAM, disk or latency improvement is claimed from offline tests. Use existing
real workload diagnostics before making those claims.

Model defaults are not hard effort ceilings. In particular, a Terra `high` profile can
still be overridden explicitly by a task or saved session. This kit does not silently
clamp such an override, increase a quota, introduce paid fallback, or declare a provider
ready from its family label. Preserve native limits and diagnose unsupported routes.

## Roll back an unused matching checkout

```sh
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase installed --manifest "$legion_manifest"
git -C "$HERMES_CHECKOUT" apply --reverse --check "$legion_patch"
git -C "$HERMES_CHECKOUT" apply --reverse "$legion_patch"
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase base --manifest "$legion_manifest"
```

This source reversal is not a live database restore. Keep the compact source/application
rollback until original-session acceptance; retire only owned, inactive staging after
its evidence is durable. Do not keep redundant full copies merely to repeat a test.


The draft/history repair retains an earlier unconfirmed message separately when the
editor has newer input. Restore is manual, into an empty matching owner, and never
sends; an unchanged explicit retry retains the original identity. Inactive history
cursors are retired. Browsing survives a transient runtime reattachment only for the
same owner and durable conversation, including when its loaded history shrinks.
Current source and native packages are installed on Linux and macOS. The Linux
draft/history flow passes twelve interaction steps. Both platforms pass a separate
17-step rich-content, bot-control and navigation selection, including both Mac launch
locations. These private synthetic checks do not establish original-user adoption
or production token/RAM savings. See the versioned verification record for scope.


## Compact-window navigation regression

Normal spacing must not override the existing narrow-window rule. Short labels
(Chat, Work, Bots and Hub) stay on one line; longer labels may wrap. Settings
remains reachable through All features, and History remains visible. The repair
does not change profiles, open a prompt or submit work.

After the existing native Desktop build, run the added E2E regression using the
already prepared, pinned test tools (no dependency installation):

```sh
cd "$HERMES_CHECKOUT/apps/desktop"
npm exec --offline --no -- playwright test e2e/core/focus-navigation-layout.spec.ts
```

The core harness supplies a private home and local mock catalog. Linux needs
its normal test display (or the documented native headless display setup).
The public test checks 320/580-pixel layouts and refuses inference; separate
native package acceptance also covers 900 pixels and saved history. Original
application processes and worker adoption are separate from this test.


## Import-free plugin source windows

Entry-point and directory metadata probes consume at most their existing 8,192
character window instead of decoding an entire source file first. They still do
not import or execute plugin code. Explicit kinds, provider markers, text
encoding and failure behavior retain the existing contracts; no new source
cache can hide an edited file or a permission change.

The added resource regression runs with the existing prepared test environment:

```sh
cd "$HERMES_CHECKOUT"
HERMES_TEST_FILE_RETRIES=0 scripts/run_tests.sh tests/hermes_cli/test_plugin_source_window.py
```

The test reads actual temporary source files through the real classifier. Large
source allocation measurements and four existing bundled manifests are recorded
separately in the verification note. No production RSS or token saving is inferred.


## Auxiliary usage and cached input

Native Codex/Claude auxiliary responses retain reported cache read/write and
reasoning counters when projected onto the existing Chat Completions contract.
Claude cache buckets are separate from uncached input; their sum is its prompt
total. Billing-provider identity does not select the shape of an already
normalized response. A fully cached call still contributes one call count;
reasoning is already included in output, and excluded MoA work is not counted
a second time.

Run the regression with the existing prepared offline environment:

```sh
cd "$HERMES_CHECKOUT"
HERMES_TEST_FILE_RETRIES=0 scripts/run_tests.sh tests/agent/test_auxiliary_usage_buckets.py
```

Only fixed provider-response fixtures are used; no inference or pricing lookup
is requested. The verification note distinguishes these arithmetic checks from
actual provider cache evidence. Existing historical omissions are not invented
or backfilled, and a larger corrected usage total does not imply more calls.


## Efficiency, monitoring and autonomy update (v0.8.0)

This update keeps the same upstream base and adds these changes to the consolidated kit:

- **Bot monitoring.** The roster's worker detail carries optional `current_tool`,
  `iteration`/`max_iterations`, `started_at` and input/output token totals taken from
  the session row the roster already reads; no extra database reads. The Desktop shows
  them as one icon-led line (tool, step i/max, elapsed, tokens), and Kanban run history
  shows each run's duration. `profiles.list` no longer violates its own wire contract
  (`last_activity_description`/`ended_at` were sent but undeclared).
- **Rich answers.** A `chart` fence and a platform hint that names the existing rich
  blocks. See [rich answers](rich-answers.md#inline-charts-and-diagram-guidance).
- **Fewer repeated model calls.** `vision_analyze` caches successful results in memory
  (256 entries, one hour) keyed by image bytes, prompt and model route; errors and empty
  results are not stored and a hit is marked `"cached": true`. The compact `kanban_show`
  view also clips long event payloads and older run fields while keeping the latest run,
  task body and newest comments intact.
- **Cacheable compression.** The context compressor sends its fixed instructions before
  the variable transcript, so providers with prefix caching can reuse them.
- **Worker exits.** A worker that exits cleanly without a terminal Kanban call and left a
  final message is held for a decision with that message attached, instead of being
  respawned blind. The dispatcher writes a `[kanban-worker-start]` marker before each
  attempt, so an older attempt's `rc=0` trailer is no longer booked for a SIGKILLed
  attempt and crash diagnostics quote only the attempt that crashed.
- **Delegated goal decisions.** `goals.delegated_decisions: true` (default `false`) tells
  the goal judge that in-scope choices are the agent's to make; a verdict that only waits
  for a user decision is continued with a "decide within authority" note at most twice per
  goal. Credentials, destructive or out-of-scope actions, spending and reserved
  publication gates still pause.
- **Fleet session search.** `session_search` accepts `scope="fleet"` to search the other
  profiles of the same Hermes home read-only, with per-profile limits and a time budget;
  each hit names its profile. The default scope is unchanged.
- **Usage pricing never fails a turn.** A failed cost lookup records an unknown cost
  instead of turning a delivered response into a failed attempt that re-sends the prompt.
- Plugin manifests may declare `provides_middleware` without a warning.

Run the focused checks from a patched checkout:

```sh
cd "$HERMES_CHECKOUT"
HERMES_TEST_FILE_RETRIES=0 scripts/run_tests.sh \
  tests/tui_gateway/test_profiles_worker_session_contract.py \
  tests/tools/test_vision_analysis_content_cache.py tests/tools/test_kanban_show_compact_clip.py \
  tests/hermes_cli/test_kanban_clean_exit_final_message.py \
  tests/e2e/core/kanban/test_kanban_worker_sigkill.py \
  tests/hermes_cli/test_goal_delegated_decisions.py tests/tools/test_session_search_fleet_scope.py \
  tests/agent/test_context_compressor_prompt_cache_prefix.py \
  tests/hermes_cli/test_plugin_manifest_provides_middleware.py tests/agent/test_run_agent.py
cd apps/desktop && npx vitest run src/lib/chart-spec.test.ts \
  src/plugins/hermes-bots/bot-worker-progress.test.ts src/plugins/kanban/bot-journey
```

These are offline checks. They show the code paths work; they do not measure a
production saving, which depends on your workload.


## Usability update from a user walkthrough (v0.8.1)

A scripted walkthrough of the real Desktop against a live Hermes home found these
problems, now fixed:

- **Global pause is visible.** When the emergency stop is engaged, `/api/status` reports
  `estop: {engaged_at, reason}` (reason only on local connections) and the Desktop shows a
  persistent strip plus a composer note saying new work is on hold until `hermes resume`.
  There is no resume button in the app.
- **Bot roster reports every bot's model, provider and description.** Sibling profiles
  discovered by the authority gateway previously had these fields hard-coded empty, so
  128 of 129 bot cards said "not reported". They now come from each profile's cached
  config and `profile.yaml`.
- Bots: provider and model fields no longer overlap; filter counts follow the search.
- Kanban: the new-task assignee picker filters as you type and marks THINK/ACTION bots;
  the card drawer's Comments/Activity/Runs/Log switcher is a real tab list placed above the
  long description; the History view uses the full width.
- Navigation: New chat and History selections highlight the right sidebar item; the
  Workflow detail panel no longer hides the graph.
- The floating pet stays below dialogs and away from the composer and status bar.
- Search hides empty groups and ranks title matches while typing; Catch up explains an
  empty goal state instead of showing "Not reported".
- Settings: the long "Applies to" profile list has a filter and a collapsed view.

## Retention companion update (v0.8.2)

This release updates the standalone retention helper and its tests, with no changes to
the 909-path upstream patch or Desktop assets. See [retention safeguards](storage-and-backups.md#retention-safeguards-v082) and the [verification record](verification.md).

## Goal judge accounting update (v0.8.3)

Post-turn goal judges now record auxiliary usage on the owning goal or worker session
and restore the surrounding accounting context. The complete kit contains 912 paths.
See [goal usage accounting](goal-usage-accounting.md) for the failure, test evidence and
runtime-adoption limits. No extra model requests or Desktop rebuilds are introduced.

## Search cache memory update (v0.8.4)

The search memo now keeps at most 256 entries and a 32 MiB budget for retained Python
keys/responses. Cold entries still use the existing bounded disk tier. Expired payloads
are released on lookup, including unrelated expired queries. The complete kit contains
913 paths; see [measurement and limits](search-cache-memory.md).

## Worker monitor readability update (v0.8.5)

Long tool names no longer push step, elapsed time and token facts outside narrow
roster rows. Facts wrap within the available width, and the existing hover summary
includes all displayed progress facts. The consolidated kit contains 914 paths.
See [verification and limits](worker-monitor-readability.md).

## Vision cache route update (v0.8.6)

Both auxiliary vision cache layers include the main connection's endpoint, API mode
and authentication mode, with context-local values taking precedence over saved
model settings. Unchanged routes still reuse successful results. The consolidated
kit contains 915 paths; see [verification and limits](vision-cache-routes.md).

## Offline vision verification update (v0.8.7)

The capability-routing regression now supplies synthetic catalog data for text-only,
vision-capable and unknown models. This removes a live-catalog assumption from the
offline test while keeping production routing unchanged. The complete kit contains
916 paths; see [verification](vision-routing-verification.md).

## v0.8.8 — Bound retained token-estimate memo memory

The global token-estimate memo now limits retained key/value objects to 32 MiB as well as 4,096 entries. Oversized messages are estimated normally without being cached. See the [measurement and adoption boundaries](token-memo-memory.md).
