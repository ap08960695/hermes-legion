# Bot activity

## Parallel observed workers (v0.33.0)

Full Bots cards now list recent observed workers with individual task titles
and progress, plus an activity count. Compact rows show the latest eligible
stamp and a count for multiple observations. A stopped newest worker no longer
hides another eligible worker or makes its bot idle. Working still counts bots.

The existing read/cache adds optional `worker_sessions` (at most 20), keeping
`worker_session` for older clients. Canonical reads bound worker rows; the legacy
reader keeps its existing 20 mixed-row window. Shared client eligibility excludes
ended, stale and unavailable observations. Explicit empty/null stays empty; only
an absent parallel field falls back to singular. These are observations, not a
complete process census. More bounded metadata is carried; no savings claim.

Native Local before/after UI Send, Stop A while B continues, heartbeat and final
Refresh passed with real lifecycle/storage and controlled loopback model replies.
Private prompts were not projected. Apply the kit, restart the updated gateway
and rebuild Desktop. [Evidence and limits](release-notes-v0.33.0.md).

## Native Local sibling acceptance (v0.33.5 follow-up)

A real UI Send in `scope-b` created one native delegated child. After selecting
`default`, Bots showed default Ready and scope-b Working, with the child task
separate from its parent's message preview. A narrowly scoped task observer
recorded the actual default roster authority, its readable scope-b sibling, and
`_sibling_sessions` returning the same child ID stored in scope-b's SessionDB.
The displayed profile label alone was not used as routing proof.

The child's native heartbeat advanced while its controlled model reply waited.
Refresh showed the waiting description. Releasing that reply produced the native
child result, terminal timestamp and parent delivery; another Refresh showed both
bots Ready, Working 0 and no active-worker detail. Default's session/message/
delegation tables stayed empty. Four model replies had controlled content and
timing on loopback; lifecycle and status records were not seeded.

The existing v0.33.5 renderer and source kit were reused. This adds acceptance
for canonical multiplexed Local sibling reads, without a new runtime release.
It does not prove a real provider, legacy backend, managed-worker subprocess,
remote/ai, Linux or daily-app behavior. [Checks and limits](verification.md#native-local-sibling-bots-acceptance--v0335-follow-up).

## Earlier worker monitoring

From v0.29.4, native `subagent` runs also reach the existing worker summary.
Canonical own/sibling reads and the legacy roster admit these children without
widening human conversation listings. A child can keep the bot Working after
its parent acknowledges background dispatch. Refresh removes worker detail
after its terminal timestamp; the parent preview stays separate.

Controlled native Local UI Send now covers real delegation, an advancing native
heartbeat, completion delivery and terminal Refresh. Only model reply content
and timing were simulated on loopback; no activity rows were seeded. See the
[v0.29.4 notes](release-notes-v0.29.4.md) for test-runner and live-proof limits.

A later native Local check also exercised a child calling `read_file` on a
synthetic task file. The result persisted through the real tool and SessionDB
paths. While its next model response was held, Bots showed Working and step
1/250; Refresh after the normal heartbeat showed the model-wait description,
without advertising `read_file` as still running. Native completion returned the
bot to Ready / Working 0 and removed worker details; the parent received its
result. Model content and timing were controlled on loopback. This proves
completed-tool progress and the waiting/terminal transitions, not visibility
during the brief file read or scoped cancellation. No runtime change was needed.

The Bots rail keeps a bot's canonical conversation preview and opening behavior.
A separate tools icon and short worker description show a recent observed worker
stamp. The full localized context is available in the existing tooltip; the row
avoids repeating "Worker activity" before every description. If a description is
missing, the worker title is used; with neither, a localized activity label remains.

The roster projection reuses its existing bounded session read. It includes only
the worker description (at most 120 characters) and terminal timestamp alongside
existing identity/title/activity fields. It adds no model request, timer, extra
query, account lookup or provider fallback. The usual roster refresh owns updates.

The earlier singular full-card display added reported tool, step, elapsed
time and token facts below the canonical preview. Native Local acceptance used
controlled SessionDB records and checked display at both widths and removal
after ending a record and clicking Refresh. That earlier v0.29.0 check did not
exercise an actual worker lifecycle. See [v0.29.0 notes](release-notes-v0.29.0.md).

## Separate calls with the same goal

From v0.31.1, a native dispatched receipt's `subagent_ids` identify the exact
children shown by its chat cards. Two separate calls with identical goals no
longer claim the same live child. Stopping A leaves B Running, then B Done.
An absent live record or an unresolved advertised identity stays parked; it
cannot borrow a same-name or same-position worker. IDs are opaque and positional;
missing slots keep their neighbors, and malformed/duplicate/misaligned lists
remain unresolved. Receipts with no identity field keep legacy matching.

Native Local before/after Send, per-child Stop, late-response refusal, B completion
and parent delivery were checked with controlled loopback replies. Reloaded
history without live children still does not infer outcomes from dispatch alone.
No new API, poll, backend field, model request or stored-content change.
[Adoption and evidence](release-notes-v0.31.1.md).

## Stop one delegated child

From v0.29.5, a chat delegation card with an explicit `interrupted` outcome shows
Response stopped with a neutral stop icon. Partial activity stays available;
genuine errors remain errors. The same presentation applies to explicit settled
results without a live roster.

In Layout editor, select Advanced and Done. In the parent chat, expand the
Subagents shelf, select a child there and choose Stop. The existing native
control targets that child; a two-child Local check verified the other child and
parent continued, and a late reply could not revive the stopped child. This does
not undo finished work or prove immediate cancellation of external operations.
Native async history without per-child status retains its parked rows; this
change does not reconstruct an outcome from notification text.
[Checks and adoption](release-notes-v0.29.5.md).

## Read saved child outcomes

From v0.30.0, expand the saved **Subagent Tasks** completion in chat after Reload.
The detail starts with each task's number, terminal outcome and bounded, redacted
task name, followed by the existing report. Collapse and reopen it when needed.
A batch with no report output can still show its retained outcomes. The source
kit and a Desktop rebuild are required.

The producer pairs each authoritative result index with its goal before saving
the display text. It does not guess an outcome from report prose, rewrite the
model notification or add a database field. Older saved notifications keep their
fallback. Original dispatch cards can still appear parked; the new detail belongs
to the completion notification. The v0.30.0 capability covers restored history; v0.30.2 adds the live refresh described below.
[Adoption and checks](release-notes-v0.30.0.md).

## Clean background reports (v0.30.1)

The saved-report view removes the canonical trailing gateway notice from its
local display input before parsing a producer envelope. This lets the existing
terminal transcript-path cleanup work and keeps process-log brackets intact.
Task outcomes and partial/report output remain. Stored history and model text
keep their original content. Unwrapped legacy reports and embedded, near-match
or suffixed notice text retain their existing treatment. Rebuild Desktop after
applying the source kit. [Checks and limits](release-notes-v0.30.1.md).

## See a completion without Reload (v0.30.2)

After the parent finishes replying to a native background completion, Desktop
uses its existing bounded history refresh to load the saved notice and report.
Open the **Subagent Tasks** summary in the current chat. Its outcome/name pairs,
partial output and report use the same saved projection as Reload; later refresh
keeps one copy. Native process completions use the same adopted-turn handling.

Only recognized completion kinds mark a backend-originated turn as adopted.
Ordinary streamed turns add no refresh through this rule; Stop settlement clears
the flag. Existing execution, interruption, error and empty-final gates remain.
This refresh follows the parent reply's terminal frame, not the instant a child
finishes. [Adoption and checks](release-notes-v0.30.2.md).

## Meaning and limits

- A worker with a terminal timestamp does not show current-worker detail or a
  worker-driven busy mood, even if its last activity is recent.
- Retained, missing-source and explicitly unreachable rows do not advertise a
  worker stamp as current. Their conversation preview remains available.
- Other workers retain the native 150-second recency policy. Recent activity is
  an observation, not proof of a still-running process, live tool, delivered
  result or successful task completion.
- The description is separate from the canonical chat preview. Clicking the bot
  still resolves the same native canonical conversation; it does not open the
  worker's transient session.
- Older backends may omit the new optional fields. Existing title/recency
  behavior remains; no new transport capability is required.

Compression-lineage projection also takes activity timestamp, description and
provenance from the displayed tip. Otherwise a row could display the tip's ID and
title beside the root's outdated activity. This repair applies to both compact
and full native session read paths without adding a query or schema migration.

## Verify locally

Use an isolated checkout and the pinned patch installation procedure. Run the
following through the checkout's native test runner and existing managed test
environment, with retries disabled:

```sh
HERMES_TEST_FILE_RETRIES=0 scripts/run_tests.sh -j 2 \
  tests/hermes_state/test_session_activity_projection.py \
  tests/tui_gateway/test_profiles_list_worker_session.py
```

These tests use temporary native SQLite state. They exercise terminal and active
workers, compact/full compression projection, payload boundaries and canonical
conversation preservation. They do not create a real task or call a provider.

Renderer checks live with `workspace.test.tsx`, `bot-worker-activity.test.tsx`,
`bot-row.test.tsx` and `row-helpers.test.ts` under the
native Desktop package. Follow upstream's dependency setup; the companion does
not install those dependencies. The rendered fixture used during development
also exercised active, terminal, unreachable and older-backend states with
synthetic data and the native diagram renderer.

Source installation, renderer compilation and activation are separate steps.
An existing Desktop or Gateway process must load changed modules through its
supported idle lifecycle. Do not hotpatch, signal a worker or force a restart to
make a status display current. This release does not replace the Desktop layout.
