# Hermes Legion v0.29.4 — Show delegated bot work

## What you will notice

Bots shows **Working** while a native delegated child runs, even after the
parent acknowledges background dispatch. The card shows the child's observed
title or activity and elapsed time. After the child ends, Refresh returns the
card to Ready and removes its active-worker detail. The parent's conversation
preview stays separate.

Native children use the `subagent` session source. The canonical roster omitted
that source; the legacy roster filtered children before classifying them. The
repair admits subagents to the existing worker summary in both paths. Canonical
own and sibling rows share the fix. Global human-listing rules, profile routing,
hidden/archived filters, recency policy and terminal checks remain unchanged.
No new query, timer, model request or telemetry field is added.

Apply the source kit to its pinned base and adopt the backend through its
supported idle update path. The existing renderer consumes the same fields;
no renderer rebuild is needed. This kit does not replace the installed app or
restart an owner's running session.

## Native Local acceptance

An actual UI Send made the native parent call `delegate_task`, creating and
running a real child. Only model reply content/timing was simulated by a
loopback HTTP fixture. Sessions, lineage, activity, completion, gateway reads
and rendering stayed native. No session, heartbeat or terminal row was seeded.

Before repair, the child's native heartbeat advanced while Bots still showed
Ready / No active work after Refresh. After repair, the same flow showed
Working 1 and the child title. Independent read-only SQLite checks confirmed
its profile, parent linkage and advancing heartbeat. Refresh displayed the
native waiting activity. Releasing the reply persisted the child's result and
terminal timestamp, delivered native asynchronous completion to the parent,
and let Refresh clear the worker detail while retaining the parent preview.

The completed after trial used four deterministic loopback replies, including
normal completion delivery. Its actual 60-second gate recorded zero SSH
attempts/executions, at most four sampled Hermes processes and sampled RSS below
4 GiB. Owned processes/model thread stopped, both loopback ports closed, and
the original trial bundle/task config were restored. No other host or owner
app/data was used. Private images and receipts remain in the local work report.

## Regression and limits

Four new active/ended child cases failed before repair. Fourteen cases in two
native test files pass with real SessionDB stores: own/sibling and legacy
projection, parent preview preservation, hidden/archived exclusion and bounded
worker fields. Pytest was unavailable in the managed interpreter; a task-local
assertion runner executed the synchronous test bodies with isolated fixtures,
without pytest or conftest. This is not a canonical pytest-suite claim. Both
formal files remain selected for the normal runner. Four changed patch sections
apply, match their hashes and reverse to the pinned base; other sections remain.

This proves one native delegation lifecycle with simulated model replies, not
provider quality, managed-worker subprocess behavior or production savings.
Heartbeat recency remains an observation rather than proof every reported worker
is alive. Live older-backend/sibling acceptance, cancellation/tool progress,
canonical group membership editing, owner-app adoption and Linux parity remain open.
