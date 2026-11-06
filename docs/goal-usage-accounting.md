# Goal judge usage belongs to the owning session

A goal judge runs between agent turns. The completed turn has already released its
auxiliary-accounting context, so the judge previously lost its usage record when no
context remained, or charged an unrelated surrounding session when one did remain.
The native managed-worker goal loop had the same gap between nested turns.

The goal manager now binds its profile-scoped session store and session ID around the
judge. The worker loop binds the worker's existing store/session around its between-turn
judges. Both restore the prior context in `finally`; a missing store clears inherited
ownership instead of billing another session. Concurrent profile judges retain separate
stores. The existing auxiliary response validator remains the single accounting writer.

No judge prompt, route, model, effort, timeout, turn budget, continuation decision or
request placement changes. Waiting goals and terminal cards still make no judge call.
Recorded usage can increase because previously missing successful responses are now
counted; this is not an increase in requests or a claim of new savings. Existing rows
are neither backfilled nor repriced, and failures without returned usage do not invent
charges.

## Verification

On the current pre-repair source, five ownership regressions fail. The repaired focused
selection passes 10 tests, including missing stores, provider failure, escaping exceptions,
concurrent profile stores, a three-turn worker with two judges, and no calls after completion
or while waiting. A separate adjacent selection passes 142 tests across goals, delegated
decisions, gates, waits, worker recovery, affinity, usage storage and cache/reasoning buckets.
Scoped lint and source-health checks pass for the repair.

For an offline fixture, each successful judge reports 100 input tokens: 40 uncached and
60 cached, plus 20 output tokens containing seven reasoning tokens. Exactly one call lands
in the goal owner's usage rows, and a subsequent outer-owner probe returns to its original
session. The multi-turn worker fixture records two judge calls on its own session, without
charging the outer session.

The actual installed source and production Python pass four additional offline native
checks on each of Linux and macOS. They use real SQLite stores and OpenAI response objects
with a fixed provider-response fixture and unknown pricing; network access is denied.
Linux exposes no GPU devices to the test; the macOS test denies IOKit access. No production
model call, session resume, dispatch, GPU workload or service restart occurred. A small
native smoke card remains blocked with no worker/run, so live provider acceptance is pending.

The complete kit now contains 912 paths. Both hosts have the same installed source payload.
The existing Gateway process was not restarted, so adoption by already-imported modules is
not inferred from file parity. Desktop assets are unchanged; this is a Python accounting
repair. Owner pauses, configuration, credentials and other project data are preserved.
