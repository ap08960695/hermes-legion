# Feature catalog

The cumulative patch is one coherent compatibility unit. Do not cherry-pick arbitrary files without tracing their dependencies and testing them.

| Area | Included behavior | Boundary |
|---|---|---|
| Completion | Exact native task/run/claim/PID/fingerprint checks stop verified completed workers before another inference turn | Rejected, ambiguous, interactive and review paths retain correction behavior; submitted tool batches finish normally |
| Dispatch | Exactly-once callback invocation, ready-work wakeups, fair unlock ordering and declared input preflight | Existing profile/host capacity, cooldown, claim and approval gates remain authoritative |
| Work isolation | Declared write scopes and stale brief/input checks | A declaration is not a filesystem sandbox or global lock |
| Waiting | Durable receipt handling, self-origin notification protection and no repeated work to manufacture proof | Admission is not terminal acknowledgement; uncertain deliveries are never blindly replayed |
| Goals and decisions | Opt-in current-session native goal setup, fresh CLI post-turn metadata and an on-demand delegated-execution skill | Existing goals, pauses, turn caps and material approval gates remain; metadata setup calls no model |
| Continuation state | Atomic goal/heartbeat/loop transfer at a compression boundary; preserve checkpoint fields and existing child metadata | A confirmed transaction moves state once; unavailable storage remains unproven and does not authorize model/compression replay |
| Handoffs | Prioritized bounded summaries, artifact references and explicit omissions | Canonical full context remains recoverable; a summary grants no approval |
| File tools | Native/raw/byte reads, repeated/concurrent read suppression and document extraction bounds | Preserve path/credential scope and invalidation; no cross-user content cache |
| Search and web | Bounded result caches, extraction validation, contention protection and eviction | Cached output is not new source verification |
| Model context | Stable shared prompt/tool prefixes and atomic compaction-related publication | Do not mutate past context to manufacture cache hits |
| Usage | Read-only account views, bounded task/run diagnostics and HMAC correlation | No prompt bodies or runtime HMAC keys are shipped; missing evidence stays unknown |
| Worker phases | Persisted phase/timing readbacks and bounded visual-request reuse | Claim-to-first-tool is not provider TTFT or whole-task speed |
| Desktop | Manual suggestions, native usage presentation and clipboard/focus improvements | No automatic paid route or typing/idle inference policy |
| Operations | Profile-aware paths, durable notifications, memory-flush and entrypoint fixes | No bundled production units, state, account configuration or auto restart |
| Memory diagnosis | On-demand local process, cache, registry and available SQLite allocator counts; opt-in startup allocation tracing | Counts contain no cached values; tracing adds overhead and is disabled by default; diagnostics do not prove savings |
| Static translations | Bounded reuse of unchanged bundled locale parses with file-change checks and serialized cold reads | Each caller retains its own mutable catalog; private overlays and plugin state are not shared by this cache |
| Plugin code | Reuse immutable compiled bundled source across native profile namespaces; content changes survive restored mtime | Globals, registrations and private-plugin imports retain native isolation; cold source compilation has a cost |

Role and skills content lives at the edges. The patch does not install an additional orchestration service or replace Hermes' native Kanban source of truth.

Existing local tests helped develop these changes. Public release acceptance is separately regenerated from the exported artifact and is recorded in `verification.md`; private operational logs are not redistributed.
