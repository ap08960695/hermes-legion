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


## Report focus restoration

The report dialog now keeps its controlled Dialog root mounted and wraps the
existing snapshot-capturing button in the SDK DialogTrigger. Radix can restore
focus to that exact source-qualified opener on Escape or Close. Snapshot capture,
local outcome filtering and canonical chat actions keep their existing semantics.
No manual focus handler, timeout, global primitive change or new dependency.

Two rendered dismissal regressions fail against the original component with BODY
focused and pass with the trigger, across same-name bots from two sources.
Existing snapshot, filter, privacy and no-navigation checks remain green. A fresh
1140×620 Chrome Guest fixture with actual component/production CSS also reproduces
original Escape focus loss and verifies fixed Escape/Close focus; stored Stopped
report pixels match AX this round. These resolve the browser follow-ups above,
not the unsupported native selector or on-screen native progress/settlement gates.
If a roster change removes the opener, there is no mounted target to restore.


## Browser adapter over native lifecycle

Acceptance uses the actual Monitor and production CSS with real, fresh
profiles.list responses from the existing native lifecycle scenario. A private
test observer reuses its one authenticated socket; a locked read-only adapter
feeds the browser. The original completed-worker scenario keeps native file-read,
heartbeat, terminal/delivery/report and independent side/profile assertions.
Only model replies/timing/usage remain simulated. Production mood/source helpers
derive rows mechanically; absent current-tool data remains absent.

The fixture adds a read-only roster endpoint and an exact terminal-view receipt,
not a product API or lifecycle control. Native test completes its own worker;
terminal receipt merely lets the diagnostic test finish after UI capture.
Active-to-terminal screenshots and a rendered regression cover the same scoped
worker/report. This is browser fixture adapter acceptance, not Electron launch,
useRoster, real navigation or production billing evidence. Native release gate
remains open. No new product poller, dependency or fallback.


Browser adapter acceptance passed with fresh native roster reads: the same child
appears Working at step1/250, elapsed advances from9s to39s, then current workers
fall to0 and its Completed report opens. The original native scenario remains
byte-identical and passes heartbeat/file/ledger/delivery and nonempty side/profile
checks. The private observer serializes read-only RPC on that existing socket;
only explicit DOM-checked view receipts delay its assertions for capture. No
browser lifecycle control or SQL writes. Production current-tool data is absent
in this held-after-read phase and stays absent. Helper status is Unknown because
this adapter does not supply Electron source metadata. Three rendered settlement
cases cover Completed/Error/Stopped with stale step/tool removal. Electron,
useRoster and real navigation acceptance remain open before the feature release.


## Production roster query acceptance

Next bridge uses actual useRoster, the shared query client/provider and its
existing refresh interval/dataUpdatedAt instead of a fixture poller. A private
SDK host adapter supplies stable local/profile atoms, exact local route and
source inventory mechanically from native names, and routes only profiles.list
to the existing locked native socket. Raw results stay unchanged; the production
hook performs merging, annotation and reconciliation. Electron inventory remains
explicitly simulated. Other host work/chat capabilities are refused.

Actual Monitor uses query dataUpdatedAt and production mood/source derivation.
No cache prefill, manual refresh loop, product API/poller/dependency or fake work.
Regression follows canonical parent/child/report/source through real hook refetch.
Browser proves automatic native-to-query-to-Monitor flow; native Electron and
canonical chat navigation remain separate acceptance gates.


The source-query regression is complete: actual useRoster refetch preserves the
named parent, ended child, exact recorded report, route/source health and local
query key, without mutating the input or falling through to an ambient gateway.
Query20+Monitor24 rendered checks pass. The private real-hook integration fixture
builds, but execution is unrun and integration unproven: CUA native input returned
noWindowsAvailable and its browser host was unavailable. No gateway run was started
without a supported UI surface. Live useRoster, Electron and navigation gates
remain open. This completed development step does not release the feature.


## Monitor Open chat integration contract

Next offline seam renders actual Monitor with the same onOpen wrapper as the
workspace, then runs real openRosterBot, canonical registry resolution and routing.
Only SDK machine/RPC boundaries are mocked. Same-name bots on distinct sources,
an unavailable foreign source and distinct canonical/worker/latest-side ids guard
against wrong-owner navigation. Bot and worker controls must resolve that owner's
existing Bot Chat by exact title, then open its returned lineage tip. Rejected
registry reads must notify without opening, creating, prompting or claiming success.
No product behavior or new API; this cannot prove actual desktop navigation.

The offline integration contract passes: bot and worker controls resolve the
local owner's fresh registry tip, excluding stale snapshot/side/worker identities;
the foreign same-name action stays disabled. Registry failure notifies without
open, draft, create, prompt or success claim. Actual data/routing/canonical/action
modules run; SDK machine/RPC effects are mocked. This closes a test seam only.
Current CUA inventory still has no browser host, so no input/app launch retry or
live navigation acceptance was attempted.


## Automatic query-to-workspace reconciliation

The connected offline regression renders actual BotsWorkspace under an isolated
TanStack client/provider, selects Monitor and waits for the unchanged five-second
useRoster interval. The first source-qualified response carries a working child;
the next ends that child and adds its canonical parent's recorded report. No
manual refetch, invalidation, cache injection or prop replacement drives the view.
Working/step/elapsed appear, then the worker and step disappear; the exact local
Completed report opens while a same-name unavailable foreign bot remains separate.

Only SDK host state/route/inventory/RPC boundaries and avatar presentation are
synthetic. Focus/reconnect refetches are disabled so they cannot impersonate the
interval. The test refuses ambient RPC, activation, navigation and draft creation.
Production workspace, query, merging, source/mood derivation and reports run.
This connects the earlier manual-refetch and prop-driven tests; it does not prove
actual gateway polling, Electron, browser paint or native navigation. Current CUA
browser host remains unavailable, so live acceptance still gates the batch release.


## Retained Monitor after refresh failure

A failed roster refresh must keep the last successful snapshot and stored task
reports readable, with current activity explicitly unavailable. Reuse the query's
cached data: the workspace keeps its existing ErrorState only when no data exists,
otherwise passes a stale flag to Monitor. A successful empty roster is still data.
Monitor shows a localized status notice, retained-snapshot row status, no current
worker/step/elapsed/Working projection, and disabled chat Open. Local report
controls and the mounted dialog's captured snapshot/focus identity remain intact.
Working/unavailable filters use the stale classification; no cached worker is
ended, mutated or given a report by this presentation change.

Existing Refresh/interval/retry policy stays authoritative. Stale notice and
restrictions persist while a recovery read is pending and clear only on success.
No raw query error appears in product copy. Nine existing monitor catalogs cover
one new notice; no new cache/store/API/dependency/poller. A separate retained
store duplicates query state; retaining the current full error screen prevents
reading stored reports. The optional presentation flag is the smallest complete
approach. Standing owner autonomy delegates this choice; advisor281 supports it.

Tests first cover retained report/dialog identity, current-work suppression and
filters, no-data/empty-data distinction, unchanged cache and recovery. Actual
workspace/useRoster query must exhaust existing retries, retain stale UI during
a held Refresh, then restore current work on success. Only affected checks plus
required owner gates run. Current CUA host remains unavailable; source/rendered
checks do not replace native/browser acceptance or authorize release/adoption.

The retained-failure source slice is implemented. Three new regressions fail
before and pass after: preserved report/dialog and stale filtering/recovery,
absent-versus-empty data, and real query retry exhaustion/held Refresh/success.
Stored reports remain available through All/Unavailable. Existing row/filter
lifetime still applies when a filter removes an opener; no global dialog owner
is introduced. Thirty-one affected cases, scoped lint and renderer types/build
pass. Native/browser acceptance remains open; no release or daily-app adoption.


## Native gateway through actual query: component acceptance

The next integration closes the data-flow seam without inventing another product
feature: unchanged native delegation/read_file/heartbeat/terminal/ledger/report
scenario -> one serialized authenticated gateway socket -> read-only loopback
adapter -> actual useRoster/TanStack five-second interval -> actual BotsWorkspace
and Monitor in JSDOM. Only SDK host state/route/inventory and avatar presentation
are synthetic; native roster payloads pass through unchanged. No manual refetch,
cache injection, prop replacement or component-controlled lifecycle completion.

One bounded completed scenario passes. Rendered same-child Working/step1/250 and
elapsed7s ->12s progress settle to removed worker/step and exact Completed report
under the same named parent. Native real file read,60s heartbeat, true completion,
durable delivery, parent terminal state and nonempty side/profile controls retain
their original assertions. Four relevant source hashes remain exact. A Node
thread-pool consumer runs in one PID after native helper exit, preserving resource
limits; DOM acknowledgments pause only observer return after releasing its lock.

This verifies real native-to-production-query-to-component reconciliation through
a private transport adapter. It is complementary to137browser adapter paint proof,
not their composition into browser/Electron acceptance. Actual browser query paint,
degraded refresh visuals, Electron host inventory/transport and canonical desktop
navigation still gate the Monitor batch release. Current CUA host is unavailable.


## Retained native snapshot through a simulated read fault

A second connected acceptance follows the retained-refresh feature through actual
query failure and recovery over real native data. After initial active rendering,
the private adapter returns503 for exactly one three-attempt read/retry cycle.
These refusals send no gateway RPC and leave the native socket/lifecycle running.
Actual query error retains its prior cache, marks Monitor unavailable for current
work, hides worker/progress, disables chat Open and keeps captured reports readable.
An empty native report snapshot remains explicitly empty, not a no-failures claim.

Existing Refresh waits on a bounded diagnostic response barrier. Stale notice and
Open restriction persist for at least one second; fresh successful native read
restores the same worker, then original native heartbeat/completion/report settle
normally. Read-only task-owned SQLite probes at error/pending acknowledgments
confirm the child has no ended_at. No observer lifecycle writes or source change.

One native and one JSDOM consumer case pass; four relevant source hashes stay
exact. This proves retained/pending/recovery behavior with real native data plus
simulated adapter fault/timing. It does not prove native gateway/socket failure,
reconnect or browser/Electron behavior. Native Error/Stopped query report cases
and remaining browser/Electron/navigation acceptance remain separate.


## Native Error/Stopped through the production query

The remaining negative lifecycle outcomes now use the same actual-query/component
bridge as completed work. Each separately observes the same active child across
one unchanged five-second interval before the native test owns rejection or Stop.
Terminal polling removes worker/step and opens exactly that canonical Error or
Stopped report. Raw multiline summary/error text and parent/child/delegation/
helper identities match fresh native receipts; independent side/profile controls
and delayed-success rejection remain native assertions. No new product behavior,
heartbeat-advance claim for these short cases or feature release.

Both labelled saved-native preflights and two native/JSDOM cases pass within the
existing process/RAM/time/network/write guards. Browser host is still unavailable;
this closes negative outcome data-flow acceptance only. Actual browser query and
degraded-refresh paint, Electron host inventory/transport and canonical navigation
remain the batch release gates. [Evidence scope](verification.md#native-error-and-stopped-reports-through-production-query--component-acceptance).


## Recorded issue context in the dashboard

The existing Last recorded issue badge names only Error or Recorded stalled.
Add the same captured issue's task, stored report timestamp and short error
excerpt in that existing report cell, so the user can identify the problem before
opening Recent reports. Keep context in that cell: a new column widens the
already scrollable dashboard, while dialog-only detail keeps the problem hidden.
Use the existing canonical bounded report list and first error/stalled selection;
a later success does not erase its history. This does not
establish a current blockage or attention state and never fills worker rows.

Task text is bounded to120characters; the error (or summary fallback) is plain
escaped text, whitespace-normalized and bounded to160characters. Existing labels
identify the recorded issue and error/report excerpt in all nine catalogs. Show
the stored timestamp with that issue, without calling a stalled task completed. Missing
text/time remains unavailable; no extra request, store, dependency or authority.
The dialog still opens its own captured full bounded snapshot and keeps focus
identity. Tests cover owner/order, history versus current work, fallback/absence,
clipping/escaping and refresh versus captured dialog. Current CUA input failure
prevents paint acceptance; keep this source slice unreleased.


Recorded issue context source slice is implemented. Three added cases plus the
strengthened captured-snapshot case fail against the prior source and pass with
the change. Monitor29and nearby query/open5cases pass; the corrected nullable
fixture, scoped lint, renderer types/build and two-section roundtrip pass. Native
Chrome reads are available but input still returns noWindowsAvailable; no Guest
or gateway launch, visual proof or feature release this round.
