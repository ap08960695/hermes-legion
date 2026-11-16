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
