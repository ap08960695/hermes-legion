# Assignee-scoped Kanban preflight

Kanban checks a target bot's configured tools and installed skills before creating a
card. Reading raw YAML skipped managed overlays and environment expansion; a legacy
skill reader also imported a YAML package the native runtime no longer uses. As a
result a valid external skill could be removed from the card and later work could
start with incomplete instructions.

The consolidated stable kit now uses the native merged, cached config reader inside
the assignee's profile scope. Profile paths follow the currently served fleet rather
than another launch root. No credential hydration command, provider/catalog check or
model request is introduced. The native secret/config scope resolves existing values;
no prompt, account, quota, fallback or model selection is changed.

## Workers and dispatcher gates

A managed worker retains its frozen execution config. Its snapshot cannot represent
another bot. When that worker creates a child for another assignee, unavailable frozen
capability inspection is deferred at creation only. The native dispatcher still
requires the actual target's declared tools before claiming or spawning the child.
Missing tools still hold the card without consuming a model attempt. Current native
role and ownership metadata checks remain live and are not replaced by the worker's
execution snapshot.

Unknown profiles or unreadable config retain the existing advisory unknown behavior
for legacy skill/tool hints. Explicit required-tool contracts remain enforced by the
dispatcher; this is not a grant to bypass a capability, role, review or owner gate.

## Evidence and limits

Regression cases covered managed overlays, target-only environment expansion,
routed fleets, a real registry/SQLite create retaining an external skill, concurrent
profile reads, unknown/unreadable config and fresh ordinary/safe/config-only worker
processes. Frozen preflight probes made no config-file opens. Card creation may read
current fleet role metadata under the pre-existing ownership gates.

A single-host, synthetic warm metadata benchmark made 500 calls: config-file opens
fell from 500 to zero. Median time changed from about 95.7 to 125.8 microseconds;
P95 changed from about 201.8 to 130.8 microseconds. Scope validation adds work, so
these numbers do not prove faster user workloads, token savings or cache-hit gains.
The native cache still owns file/managed-policy/environment invalidation.

Installed native Python acceptance used the actual tool registry and SQLite on Linux
and macOS in private synthetic homes, with network calls denied and no inference.
This is separate from original-session or provider-backed workload acceptance.
The UI is unchanged from v0.7.2; no Desktop bundle rebuild is required for this backend
source change. Restart an owning backend only through the native idle/update path.
