# Hermes Legion v0.21.0 — bounded idle cache cleanup

## What you will notice

When several cached chats become idle together, the gateway now submits one
idle-cleanup job per runner. It commits and releases one cached agent at a time
instead of launching a separate daemon thread for every expired chat. Agents
waiting for cleanup stay cached; a new turn, recent activity or unflushed history
protects them when the worker checks again.

The existing housekeeping executor owns this job, including shutdown draining
and protection against closing SQLite while a writer remains alive. Each agent
still commits memory before releasing clients under its own profile. Persisted
history and session tool resources keep the existing soft-eviction behavior.

There is no new setting, dependency, pool, timer, forced trim or model call. Apply
the source kit and use the updated gateway runtime; the daily Mac app was not
rebuilt or launched. Other eviction paths retain their existing policies.

## Measured on this Mac

Four fresh processes ran old/current/current/old using the same native cache,
executor, eviction and SQLite methods. Four synthetic durably saved sessions had
a fixed 200 ms provider callback delay. Only that callback is synthetic: there
is no inference, real provider integration or artificial memory allocation.
Every session committed and closed exactly once, with matching native history
readback and identical unchanged config bytes.

| Same four-session component case | Before | After |
| --- | ---: | ---: |
| Concurrent idle-sweep memory commits | 4 | 1 |
| Peak sampled native threads, including main | 5 | 2 |
| Median cleanup completion | 213.076 ms | 846.627 ms |
| Median lifetime peak RSS | 117.726562 MiB | 117.593750 MiB |
| Median RSS after cleanup | 117.164062 MiB | 117.140625 MiB |
| Surviving native processes after shutdown | 0 | 0 |

RSS was essentially unchanged: **no RAM-saving claim**. Cleanup takes longer
because callbacks run sequentially. This proves bounded idle-sweep concurrency,
not a global cleanup limit, improved throughput or whole-gateway RAM reduction.
The existing shared executor can delay cleanup behind other housekeeping work
and retains idle threads until normal shutdown; no new pre-started pool is added.

An external observer sampled recursive native ancestry and RSS every 20 ms.
There was one native process and one excluded observer, with extra RSS below
4 GiB. Shared pages, sampling gaps, allocator noise and four controlled cases
limit these measurements. No installed-app, adapter, model or other-OS acceptance
is claimed. No other machine was contacted.

## Safety and verification

The old behavior regression failed because all four agents had left the cache
while the first callback was blocked; three should remain owned there. Eleven
post-change standalone native unittest cases pass. They exercise serialization,
repeated sweeps, activity/persistence/replacement checks, per-profile ownership,
commit-before-release, soft provider failure, submission failure and stale work,
queued cancellation, immediate completion and reservation reuse.

The native shutdown phase actually finalizes the three waiting agents. A blocked
fourth remains a live executor writer: the real DB-close guard skips closure
under an explicit two-second test drain budget. After release, all four commit
and close once; native SQLite closes and reopens with matching history and no
remaining housekeeping workers. These are native component/phase tests, not a
full application shutdown or a real memory-provider acceptance test.

Two existing pytest tests now wait for asynchronous completion and close their
owned executor. The selected runtime has no pytest or Ruff; their full canonical
suite/lint pass is not claimed. Standalone contracts, companion tests, release
inventory, native patch roundtrip and secret scans gate the driver handoff.

Unexpected worker failure is logged and releases its reservation; unclaimed
agents stay cached. Existing best-effort failure semantics remain: a failed
claimed teardown is not reported as successful. LRU, pressure and explicit
boundary cleanup remain separate and may run concurrently.
