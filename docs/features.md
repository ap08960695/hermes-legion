# Feature catalog

The cumulative patch is one coherent compatibility unit. Do not cherry-pick arbitrary files without tracing their dependencies and testing them.

| Area | Included behavior | Boundary |
|---|---|---|
| Desktop interface | Focus/Workspace, full native history/project managers, bot/group/section/Screen controls, visible context and loaded pane/status discovery | Existing chat, canonical bot sessions, layout scopes and advanced tools remain native; no implicit plugin enable or worker dispatch |
| Goal form | Owner-scoped skills, explicit completion criteria and revision-checked idle saves | Preserves existing turn counters, limits, gates and waits; no model kickoff or budget override |
| Catch up | Native goal/loop/heartbeat controls, event-backed wait state and links to original conversations, runs and outputs | Unknown stays unknown; a finished reply is not a completed goal or publication approval; no added polling |
| Completion | Exact native task/run/claim/PID/fingerprint checks stop verified completed workers before another inference turn | Rejected, ambiguous, interactive and review paths retain correction behavior; submitted tool batches finish normally |
| Dispatch | Exactly-once callback invocation, ready-work wakeups, fair unlock ordering and declared input preflight | Existing profile/host capacity, cooldown, claim and approval gates remain authoritative |
| Work isolation | Declared write scopes and stale brief/input checks | A declaration is not a filesystem sandbox or global lock |
| Waiting | Durable receipt handling, self-origin notification protection and no repeated work to manufacture proof | Admission is not terminal acknowledgement; uncertain deliveries are never blindly replayed |
| Goals and decisions | Opt-in current-session native goal setup, fresh CLI post-turn metadata and an on-demand delegated-execution skill | Existing goals, pauses, turn caps and material approval gates remain; metadata setup calls no model |
| Continuation state | Atomic goal/heartbeat/loop transfer at a compression boundary; preserve checkpoint fields and existing child metadata | A confirmed transaction moves state once; unavailable storage remains unproven and does not authorize model/compression replay |
| Handoffs | Prioritized bounded summaries, artifact references and explicit omissions | Canonical full context remains recoverable; a summary grants no approval |
| File tools | Native/raw/byte reads, repeated/concurrent read suppression and document extraction bounds | Preserve path/credential scope and invalidation; no cross-user content cache |
| Search and web | Bounded result caches, extraction validation, contention protection and eviction | Cached output is not new source verification |
| Model context | Versioned shared prompt/tool prefixes, role-aware v4 guidance placement and atomic compaction-related publication | Do not mutate past context to manufacture cache hits |
| Session metadata | Small runtime bindings and search identity reads select only needed columns, avoiding full prompt/tool-context hydration | Full session reads, per-session identities and freshly committed values retain their native behavior; no shared content cache |
| Usage | Read-only account views, reported cache totals/share, bounded task/run diagnostics and HMAC correlation | No prompt bodies or runtime HMAC keys are shipped; missing evidence stays unknown |
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

- [Hub and shared collections](shared-spaces.md): explicit bot readers, pages, imported copies, bounded read-only CLI, revision conflicts, trash and restore.
- [Rich answers](rich-answers.md): existing native tables/diagrams plus opt-in literal-data cards with sources.
- Full Bots workspace, single Focus rail, working first-click session selection, Workflow ancestry and truthful running-only motion, and availability-gated internal file previews.

### Unified Hub navigation (v0.5.1)

The former Library and Spaces share a single Hub destination, header and search. Chat output provenance and private-by-default collection membership stay distinct. Old links resolve to Hub. As of v0.5.2, both main-window modes hide the legacy sidebar trigger and column; secondary windows retain their native layout controls.

## Saved-chat access and quiet Slack status (v0.5.2)

**History** is a direct native door to existing chats, with bounded older pages and explicit server-side title/ID search across profiles on the selected connection. Resuming a result preserves its saved ID and captured owner. The main Focus and Wide modes no longer expose the old sidebar button or column.

Slack can silence automatic paused refusals with an adapter-local preference while preserving the pause, authorized control commands, approvals and normal task replies. The opt-out is described in [the Slack status guide](slack-status-notices.md). It does not disable Slack or silently authorize paused work.

See [Desktop feature parity](desktop-feature-parity.md) for the restored native workflows and verification limits.


## Bounded recall and optional memory review (v0.6.7)

[Conversation title recall](session-recall.md) uses the existing bounded native bookend API, checks metadata exclusions before payload reads, preserves normal orientation evidence and reports unavailable history without an unbounded retry. No external service or new tool is required.

The [external-memory pilot guide](external-memory-pilot.md) documents a separate, opt-in evaluation boundary: explicit project/profile scope, backfill and auto-wiring disabled, private token files, unchanged native gates, failure isolation, and matched-work measurements before expansion. It includes a pinned upstream TOML example and local embedding-authentication cautions; no service, hook, MCP tool or model is automatically enabled.


## Context-free search identity (v0.6.8)

[Native session search metadata](session-metadata-reads.md#search-identity-reads-v068)
selects eight identity fields and resolves exact titles with ID-only queries.
Canonical Bot Chat selection, numbered continuations, bounded evidence and legacy
adapter compatibility remain. A failed present small reader never retries the
full-context path. This reduces local hydration without changing model input,
quota, providers or paid fallback.


## Prompt-free notification routing (v0.6.9)

[Destination existence checks](session-metadata-reads.md#notification-destination-checks-v069)
reuse native identity metadata before the existing compression-tip check. Current
session ownership, profile/branch/hold fences and receipt identity remain intact;
no delivery replay, polling-frequency change or new model call is introduced.


## Lightweight resume and export selection (v0.6.10)

[ID-only discovery](session-metadata-reads.md#id-only-resume-and-export-preflight-v0610)
keeps native MRU/workspace/oneshot selection and export-budget preflight from
loading context they do not consume. A disabled Console guard skips its ID scan;
positive per-session budgets and full backup/export fidelity remain.


## Chunked JSONL output and Terra effort (v0.6.11)

JSONL file exports serialize one record at a time through the native staged writer.
Backup payloads, record order, formatting and per-session guards stay intact.
Existing hard-linked outputs and special files use direct writing to preserve their
original semantics; stdout is inherently non-atomic. The full database payload is
still materialized. See [measured scope and limitations](session-metadata-reads.md#chunked-jsonl-export-v0611).

The Codex reasoning-effort mapping recognizes GPT-6.1 Terra so a configured `max`
reaches the request rather than being reduced to `xhigh`. This is compatibility
for the native provider, not a model assignment or a new account/fallback.

## Per-task reasoning effort (v0.6.12)

The native `kanban_create` tool accepts an optional `reasoning_effort` for one
task, and returns the persisted model, provider and effort so the caller can
verify the selection. Supported values are `none`, `minimal`, `low`, `medium`,
`high`, `xhigh`, `max` and `ultra`; omitting the field retains the profile's
setting. The existing provider-specific compatibility rules still apply. Task
details include the effort; compact task lists do not gain another field.

This feature does not add a bot, change a profile, bypass dispatch eligibility,
change quotas or authorize a provider fallback. A worker that is already running
retains its existing invocation.

## Verified completion at budget checkpoints (v0.6.13)

Preserve a verified worker completion result when an iteration or time budget checkpoint is reached. The existing ownership and completion checks continue to decide whether the worker can stop. Unverified results retain the normal warnings.

## Usage reporting during log rotation (v0.6.14)

If a log disappears or cannot be inspected while selecting the newest logs, continue with available files and report the number that could not be inspected. Sampling, the file budget and the explicit unknown-coverage caveat remain in place.

## Older session restoration (v0.6.15)

Cold startup can resolve a remembered session outside the loaded sidebar page when its connection and profile are validated. It preserves remembered navigation when ownership is uncertain or lookup fails, and ignores stale results after the user moves away. An unambiguous ID prefix may resolve to its canonical session.

## Explicit usage attribution boards (v0.6.16)

For an intentionally selected additional database, pass `--board /path/to/kanban.db` to the read-only usage attribution CLI; the option is repeatable. Paths are resolved and deduplicated before reading, and explicit paths take priority within the existing 64-board cap. Missing or non-regular files are reported unavailable and never created. Existing default discovery does not expand.

## Per-task CLI reasoning (v0.6.18)

`hermes kanban create "Task" --assignee PROFILE --reasoning-effort high` sets reasoning for that card without changing the profile default. Omit the option to inherit the profile; `none` explicitly requests no reasoning where supported. Invalid levels are rejected before a card is created. Existing model, provider, quota and ownership gates remain in force.

## Cross-profile cache cohorts (v0.6.19)

Add `--cross-profile` to the read-only usage attribution command to summarize existing diagnostic cohorts. A cohort requires matching installation namespace, route, declared-account fingerprint, cache key, common prefix, tools and options, with at least two returned requests with known usage from each of at least two profiles. The new section emits aggregate counts and token totals, not fingerprints or prompts. Conflicting copies, incomplete fields and unknown usage are excluded. Existing bounded log coverage applies. Declared headers do not prove authenticated account identity; matching prepared metadata and positive cached tokens do not prove which bot populated the provider cache or establish cost savings.

## Verified goal waits (v0.6.20)

A PID or process-session wait remains parked while its original target is verified live or its watch trigger has not fired. PID identity combines boot and process start information to recognize reuse. A missing, legacy or unreadable identity does not imply completion: after a bounded period the goal pauses for inspection, preserving the wait target and budget, without scheduling a model turn. Desktop and CLI show a single pause notice. An explicit timed wait and a verified process exit or watch trigger retain their existing continuation behavior.

## Snapshot integrity and traversal (v0.6.21)

Quick snapshots record critical file, directory and database capture failures and oversized skips. An incomplete snapshot cannot prune older snapshots, and restore reports an incomplete outcome when a listed file was not restored or the snapshot was incomplete at capture. Other files may still be restored; the result does not imply transactional rollback. Intentionally excluded board workspace and attachment trees are pruned from traversal, avoiding needless metadata scans.

## Safe autonomous reassignment (v0.6.22)

Captain reassignment refuses running tasks rather than interrupting an active claim based on a bot-status snapshot. Reassignment checks the observed status and owner inside the write transaction. Automatic recovery from a provider failure checks that the same failure and target remain, preserves explicit holds and sticky operator gates, and distinguishes a released historical hold from an active one. Explicit operator reclaim is unchanged.

## Passive intermediate task status (v0.6.23)

For TUI and Desktop subscriptions, plain todo, ready, running and scheduled status changes remain visible as status updates without creating an assistant turn. Outcomes, review handoffs, invalidation events, changed routing and unknown or additional metadata retain their existing wake behavior. Task events and the subscription cursor remain durable; the passive status display is transient and may be missed across a process crash. Existing delivery receipts are not rewritten.

## Concurrent task idempotency (v0.6.24)

For a given board, concurrent creation requests using the same nonempty idempotency key resolve to the same existing non-archived task. The lookup is checked again under the database write transaction. Different keys remain independent. Keys are board-scoped, archived keys may be reused, and historical duplicates are not modified. This does not deduplicate requests without a shared key.

## Dispatch pause and shared capacity (v0.6.25)

The shared dispatcher honors the emergency stop before a tick and before each new admission; it leaves existing workers alone. The dashboard nudge and standalone daemon pass the configured host, board and per-profile limits. Within a shared Kanban home, a short nonblocking admission lock serializes capacity rechecks and claims across cooperating updated dispatchers. Read-only capacity checks include running tasks on known active boards. When an active board cannot be read or the admission lock cannot be used, capped dispatch defers new claims and reports why. A board omitted by the underlying enumeration cannot be counted, and manual claims outside the dispatcher are not governed by these caps.

## Emergency-stop inspection failures (v0.6.26)

Treat an inaccessible or uninspectable emergency-stop sentinel as paused; only a missing sentinel permits work. This protects cron, gateway turns and Kanban admission without interrupting in-flight work. The operator can still use the existing pause controls.

## Honest pause and resume status (v0.6.27)

Pause controls confirm that an emergency-stop file is visible before claiming a pause. Resume controls check whether any known sentinel remains or cannot be inspected before reporting success. An unreadable state produces a clear warning, and a reason is shown only when it was actually read from a sentinel. Existing in-flight work is not interrupted.

## Global pause across profiles (v0.6.28)

A global pause requested from a profile writes the fleet-root sentinel so other profiles on that root observe it. Existing local profile sentinels remain independent. Resume clears the fleet and current profile sentinels, while pauses belonging to other profiles remain. Unknown home or root resolution keeps automatic work paused and is reported as unconfirmed. Separate roots, unpatched processes and existing manual operator overrides are outside this behavior.
