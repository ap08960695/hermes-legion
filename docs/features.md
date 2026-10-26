# Feature catalog

The cumulative patch is one coherent compatibility unit. Do not cherry-pick arbitrary files without tracing their dependencies and testing them.

| Area | Included behavior | Boundary |
|---|---|---|
| Desktop interface | Focus/Workspace, four primary destinations and a searchable native/plugin feature catalog | Existing chat, canonical bot sessions, layout scopes and advanced tools remain native; no implicit plugin enable or worker dispatch |
| Goal form | Owner-scoped skills, explicit completion criteria and revision-checked idle saves | Preserves existing turn counters, limits, gates and waits; no model kickoff or budget override |
| Catch up | Existing event-backed goal/wait state and links to original conversations, runs and outputs | Unknown stays unknown; a finished reply is not a completed goal or publication approval; no added polling |
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
| Session metadata | Small runtime bindings select only model configuration, avoiding full prompt/tool-context hydration | Full session reads, per-session identities and freshly committed values retain their native behavior; no shared content cache |
| Usage | Read-only account views, bounded task/run diagnostics and HMAC correlation | No prompt bodies or runtime HMAC keys are shipped; missing evidence stays unknown |
| Bot activity | An icon with bounded recent-worker detail, separate from the canonical conversation preview; compression-tip activity follows the displayed session | A recent stamp is not live process proof; finished and unreachable workers are excluded; no new poll or model request |
| Worker phases | Persisted phase/timing readbacks and bounded visual-request reuse | Claim-to-first-tool is not provider TTFT or whole-task speed |
| Desktop | Manual suggestions, native usage presentation and clipboard/focus improvements | No automatic paid route or typing/idle inference policy |
| Operations | Profile-aware paths, durable notifications, memory-flush and entrypoint fixes | No bundled production units, state, account configuration or auto restart |
| Memory diagnosis | On-demand local process, cache, registry and available SQLite allocator counts; opt-in startup allocation tracing | Counts contain no cached values; tracing adds overhead and is disabled by default; diagnostics do not prove savings |
| Static translations | Bounded reuse of unchanged bundled locale parses with file-change checks and serialized cold reads | Each caller retains its own mutable catalog; private overlays and plugin state are not shared by this cache |
| Plugin code | Reuse immutable compiled bundled source across native profile namespaces; content changes survive restored mtime | Globals, registrations and private-plugin imports retain native isolation; cold source compilation has a cost |

Role and skills content lives at the edges. The patch does not install an additional orchestration service or replace Hermes' native Kanban source of truth.

Existing local tests helped develop these changes. Public release acceptance is separately regenerated from the exported artifact and is recorded in `verification.md`; private operational logs are not redistributed.

## Reuse a ready startup checker

Different launcher runtime scopes can share one PM checker cache. A ready checker matching the requested PM lock and interpreter is now reused even when another launcher's generation is selected. The current selected checker keeps priority; matching published alternatives must pass native import validation and receive the normal child lease. This prevents a false stale-dependency result from starting unnecessary preparation. It does not weaken application dependency validation, retain unused generations indefinitely or change environment selections.

## Native work-surface correction

The actual Kanban canvas now separates current work from bounded completed history, and native Sessions/Bots navigation shares one global owner. Models and Usage open their named native sections. Empty-state and compact Chat presentation changes are described in the [Desktop guide](focus-workspace.md#current-work-and-task-history). No task lifecycle, provider selection, quota or inference behavior changes.

### Native Workflow and internal file library

The [Focus guide](focus-workspace.md) describes the Workflow dependency graph, the selected card's recorded bot-run history, focus-aware navigation and Library's internal read-only file/folder browser. They reuse existing native stores and APIs; no additional model, quota, paid fallback or dispatcher is introduced. Unsupported file formats remain explicit and no Office conversion is bundled.

## Shared content and native navigation

- [Shared Spaces](shared-spaces.md): explicit bot readers, pages, imported copies, bounded read-only CLI, revision conflicts, trash and restore.
- [Rich answers](rich-answers.md): existing native tables/diagrams plus opt-in literal-data cards with sources.
- Full Bots workspace, single Focus rail, working first-click session selection, Workflow ancestry and truthful running-only motion, and availability-gated internal file previews.
