# Bot Monitor

Status: development, not a released capability. Owner goal addenda 10/10b make
this the current feature project. The existing v0.33.8 release remains historical.

## What the owner will see

**Bots → Monitor** opens one dashboard instead of scanning individual cards.
It lists the visible bots and their bounded, current worker observations, with
task/step, elapsed time, tokens, model and attention/source status. Search, status
filters and sorting are local. An explicit Open chat action uses the existing
source-qualified canonical bot-chat action, including for a worker's parent bot.
Refresh and automatic updates reuse the existing roster query.

```
Bots     [Monitor] [Manage team] [Refresh]
Search bots and tasks…   Status: All   Sort: Name
Bot / worker | Status | Task / step | Elapsed | Tokens | Cost | Model / attention
writer       | Working | …           | —       | —      | —    | configured route
  worker A   | Working | read_file 3/8| 5m      | …      | —    | configured route
```

## Approach and boundaries

Extend BotsWorkspace with a sibling monitor component. Reuse `useRoster`,
`activeWorkerSessions`, `workerProgress`, source status, attention hints and
`openRosterBot`. Shared Button/SearchField/Select and table markup keep the view
accessible and flat. Cards and Manage team remain available. A separate routed
application would duplicate roster state; another card detail would miss the goal.

This is an observation dashboard, not a process census. Current eligibility stays
with the existing bounded 20-worker/150-second policy. Ended, stale, retained and
unreachable observations cannot become current workers. Missing facts remain
unavailable, never invented zero usage, percent complete, success or "stuck".
The roster's model is a configured route, not proof of a live worker binding.
Cost and last-error/stuck details require explicit backend facts; the first slice
must label their absence rather than derive them from elapsed time or prose.

No new gateway request, provider call, automatic connection, retry, storage key or
dependency. Search/sort/filter never activate a connection or open a conversation.
Only an explicit Open chat action can use the existing routing action. All nine
registered catalogs cover new chrome. Initial adoption is an isolated Local trial;
owner app/data, ai/other machines, ESTOP, pauses and timers remain untouched.

## Delivery across rounds

1. Build the accessible dashboard, current worker facts, local search/filter/sort,
   honest missing metrics and canonical chat action, with rendered regressions.
2. Finish supported cost/error/stuck facts and navigation/report acceptance against
   existing authorities. Keep unsupported fields honest and scoped.
3. Native Local before/after and live progress/settlement acceptance, including
   absent/ended/stale/unavailable data, before one minor release for the whole set.

Each round advances this feature. A source slice may be kept as unreleased work;
no minor release or daily-app adoption is implied by a component test. The native
paint/reload problem from round 126 is a live-proof blocker, not a reason to invent
a production fix. Diagnose its boundary only as needed to verify this feature.

## Current progress

The first dashboard source slice is implemented with nine rendered regressions
and the nearest workspace/worker checks. Successful existing roster refreshes
also expire unchanged observations using the query's success timestamp. It is
ready as an unreleased development commit, not as the completed Bot Monitor
capability. Native attempts were blocked by stale captured presentation; neither
the initial nor software-GPU comparison established visible Monitor acceptance.
[Verification scope](verification.md#bot-monitor-first-dashboard-slice--unreleased).
Next finish error/stuck/report facts and obtain native layout and
actual progress/settlement proof before the single feature release.

## Recorded worker usage slice

Expose the SessionDB row's existing recorded estimate, recorded provider-reported
amount and recorded model through the bounded roster read. Extend the shared
projection used by unified/legacy readers and optional wire contracts; no extra
query/provider call. Positive finite amounts survive an unknown/included latest
pricing status. Zero estimate requires latest estimated status; zero reported
amount requires latest actual status. Other missing/default/invalid values stay
null. Display both amounts separately as recorded USD, with a persistent partial
coverage/not-invoice hint; never sum them or infer whole-session free usage.
Worker model is a recorded route, distinct from the configured bot model and from
a live binding. Existing current-worker eligibility and canonical opening stay.

A separate usage request would duplicate the roster read; pricing in the renderer
would invent authority and network work. This extends existing rows only. Real
temporary DB legacy/unified parity plus rendered regressions prove the slice;
error/stuck/report authorities and full native acceptance remain later work.

Recorded usage slice is now implemented with real temporary-DB legacy/unified
parity and rendered UI checks. Native final-artifact verification stopped when
the single titlebar coordinate probe returned noWindowsAvailable; focus was
unconfirmed, so no Monitor visual acceptance is claimed. Source slice remains
unreleased; error/stuck/report and native layout/lifecycle work follow.

## Canonical bot usage slice

Bot rows consume the resolved named Bot Chat row's recorded tokens, estimate,
provider-reported amount and model. Extract the existing five usage fields into
a shared projection; worker progress delegates to it unchanged, and canonical
readers use their already-selected compression-tip row. Ordinary latest-session
summaries stay unchanged; a canonical alias may share its own summary. No new
query or billing/routing authority.

Each UI entry selects worker or canonical usage once for both display and token
sorting. Never select newest side-chat usage, add workers to the bot, combine
root/tip totals or fill missing worker fields from canonical data. Keep configured
bot route and recorded Bot Chat model separately labelled. Canonical usage does
not prove current work: elapsed/tool/iteration remain worker-only. Visible hint
names stored Bot Chat values, not lifetime totals/worker sums/live model binding.

Real temporary/read-only DB parity covers named identity, compression, distinct
homes, ordinary summaries, missing/zero and privacy; rendered tests cover source
selection, token sorting, no false activity/elapsed and exact canonical opening.
Native conditions have not changed since the CUA noWindowsAvailable failure;
no blind retry or live/release claim this round. Full Monitor stays unreleased.


## Recorded task reports slice

Monitor bot rows offer a local Recent reports dialog from their named Bot Chat's
durable async-delegation ledger. The existing preferred compression walker
provides exact eligible chain ids; reuse it in place of the existing tip-only
walk, preserving identity and excluding reset/branch/delegate forks. Both roster
readers use the same read-only extraction and existing roster cache. Ordinary
latest-session summaries and current-worker eligibility remain unchanged.

At most20terminal ledger rows and20task snapshots per canonical conversation.
Bound task/result JSON reads before decoding; malformed/oversized content never
falls back to raw JSON. Force existing secret redaction before clipping goal256,
summary2048 and error512characters. Only id/task index, normalized recorded
status, completion time and those text fields leave the helper. No transcript
paths/config, additional gateway request/poll/provider, storage or control API.

Per-task statuses override unit completion (mixed batches can contain failures).
Only explicit recorded successes are Completed; error/failed/timeout are Error,
interrupted is Stopped, stalled is Recorded stalled, everything else Unknown.
History cannot establish current blockage or Working; absent/partial records
never prove no failures. Missing/legacy/read-error report data stays unavailable
without losing canonical identity/usage. Empty readable history means only no
reports in this bounded snapshot.

Reports open only on explicit click, as escaped plain text in the existing
Dialog primitive, with bot/source and stored-snapshot scope. No connection or
chat navigation; canonical Open chat keeps its existing identity action. Task
reports use the shared Select to filter locally by recorded outcome; current bot/worker filters
still describe their existing current observations. All nine catalogs cover new
chrome. Retained/offline history remains clearly captured/stored, not live proof.

Approaches: badge-only is smaller but lacks durable task reports; a separate
report request/poller duplicates existing roster authority. Shared bounded
read-only snapshot plus local dialog is the smallest complete report slice.
Owner's standing autonomy delegates this call; advisor264supports it. Source
checks/DB parity and rendered UI prove this slice, not native/layout/billing.
Native capture condition unchanged; no blind retry or feature release this round.


Recorded-report source slice is implemented. Twelve new DB cases plus24nearby
checks and19Monitor+31nearby UI cases pass. Missing task status/index in a completed
batch stays unknown/unbound instead of borrowing the unit or another task.
Report/error text is labelled as excerpts. Redaction binds the owning store's
home and restores the caller's context, preserving per-profile vault-value
isolation without secret hydration or process-environment changes. Native layout, on-screen worker
progress/settlement and feature-release acceptance remain open.

## Native backend integration

The lifecycle-to-report boundary now has one repeatable integration regression.
It uses the public gateway lifecycle, real private-control tickets and WebSocket
API, native agents/delegation, a real fixture-file read, durable heartbeat,
terminal ledger and the same canonical report consumed by Monitor. Three native
outcomes now share the scenario: successful completion, provider rejection after
the file read, and authenticated per-child Stop while its model reply is held.
The stopped child ends before release; the stale successful reply cannot replace
its terminal record or result. Failed/interrupted task states normalize to
Error/Stopped reports even though both single-child batches record unit error.
Nonempty side-chat and sibling-profile controls cannot substitute for the task.
No test code seeds or repairs the main task's sessions, progress or ledger.

Model responses, timing and usage come from a bounded loopback fixture. The
gateway shares the isolated per-file pytest process; this does not cover CLI
daemon launch, subprocess isolation or native UI paint. Native visual and
on-screen progress/settlement acceptance still gate the feature release. With
CUA returning `Invalid app` for the uniquely identified trial, another native
launch needs changed supported target-selection evidence first.


## Browser layout acceptance

The actual component with production CSS exposed a model-column defect in an
offline Chrome Guest preview: table layout squeezed model cells to 60.89 CSS
pixels, splitting ordinary labels into short fragments. The model cell now uses
the existing `min-w-48` utility, retaining `break-all` for long routes. This gives
it a 12rem minimum within the existing horizontal scroll region. No columns,
fields, data authority, sorting, filtering or routing behavior changed.

The same browser geometry assertion fails before and passes after at 1140×620
and 480×620 iframe viewports: 60.89px becomes 192px in that fixture. Matched images
and the horizontally revealed narrow view show readable configured/recorded
models. The fixture uses saved synthetic native outcomes from the prior native
integration, separately labelled simulated layout workers and an explicit local
locale client; it has no Electron bridge or backend. It proves component layout,
not an installed-app launch or live work. No class-mirror test or new framework.

Search, current-status controls and report filtering were exercised through CUA.
The initial long Thai/plain-text report painted correctly. Later report pixels
stayed on an older dialog despite newer AX state; those images do not establish
Stopped-report visual acceptance. Escape dismissed the dialog but focus was
observed on the HTML document, so focus return needs follow-up. These remain
open alongside native progress/settlement acceptance before a feature release.
