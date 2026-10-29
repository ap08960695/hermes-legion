# Canonical group controls and ready standby

An empty, ready hosted-room coordinator is intentionally armed without a supervisor
thread. This keeps idle profiles from creating one thread each. Canonical group
controls previously treated that standby state as a missing worker: creation wrote
room metadata through the fallback path without waking its owner, and sending a
message then returned `runtime_coordination_required`.

The existing runtime status snapshot now distinguishes `armed` from `running`.
Canonical controls accept a running or armed coordinator unless it is stopping.
Native room creation and admission therefore reach the existing service and its
single-flight wake path. Only the owning coordinator starts; other empty profiles
stay in standby. No new scheduler, polling loop, executor, model request or config
option is added. The ordinary legacy TUI service explicitly starts its worker and
keeps its existing lifecycle.

An unarmed coordinator before the all-profile ready gate still refuses execution.
Explicit Stop disarms the owner and cannot be undone by a late ready callback or
ordinary wake. Room ownership, host/profile grants, retiring/draining behavior,
attachments, task generation, unknown-result fences and quota/provider policy remain
native. The added armed field is internal runtime health metadata; per-room wire
contracts are unchanged.

## Validation

The regression selection passed 51 files / 283 tests with zero retries. It includes
the three native multi-bot group tests that failed before this fix, standby resource
checks, ready/Stop controls, profile retirement, canonical wire contracts, native
HTTP routing, attachments, peer transport and the prior cold-profile I/O fix.
Native code-health comparison reported no findings. These results are scoped;
older overlapping counts are not added to this selection.

Installed Linux and macOS acceptance each passed 8 controls through real canonical
authorities, groups, native SQLite stores, routed admission and terminal publication.
Each uses exactly one deterministic offline member execution. Network is denied and
no provider/model request is made; this proves the runtime control path, not model
quality or original-user session execution. Controls cover pre-ready refusal,
thread-free ready capability, owner-only wake, routed member completion, durable
same-event idempotency, coordinator reuse, owner refusal and Stop preservation.
The original macOS Gateway was not started, and no Desktop bundle was rebuilt.

This resolves the pre-existing group-control issue documented in v0.7.8 while
retaining its standby resource behavior. No general token, RAM or latency savings
are inferred from these synthetic controls.
