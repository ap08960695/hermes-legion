# Hermes Legion

**Role-based bots. Parallel work. Less wasted inference.**

Hermes Legion is an independent companion kit for [Hermes Agent](https://github.com/NousResearch/hermes-agent): reviewed source patches, reusable operating skills, and fifteen English role templates. It is not an official Hermes release or a hosted service.

The design is simple: give each bot a clear responsibility, dispatch independent ready work within existing limits, preserve a stable prompt prefix, and stop a worker when its verified native completion is already durable.

Historical source comments and release payloads received [privacy maintenance](docs/privacy-maintenance.md). Version names remain available, but corrected commit and archive hashes differ from older downloads.

## What is included

- [Cycle-safe skill discovery and declared-name preflight](docs/skill-discovery.md) shared by the skill index, catalog signature and Kanban preflight.

- [Assignee-scoped Kanban preflight](docs/assignee-preflight.md) that retains configured external skills and preserves frozen-worker fanout.

- A [compact bot settings editor](docs/desktop-bot-settings.md) that keeps model/effort visible and groups optional appearance controls.
- Optional [per-model effort ceilings](docs/reasoning-effort-limits.md), with effective/requested effort disclosure and offline request-boundary checks.
- A consolidated [956-path source and Desktop kit for upstream v0.22.5](docs/stable-full-kit.md), with pinned hashes and a reproducible test selection. It includes the interface, workflow, search, memory/cache, usage, waiting and update-preservation changes as one complete alternative.
- v0.8.0 adds live bot progress (current tool, step, elapsed, tokens), inline `chart` answers with diagram guidance, a vision result cache, cacheable compression prompts, crash-safe worker attempt markers, opt-in delegated goal decisions and fleet-wide session search. See [the update notes](docs/stable-full-kit.md#efficiency-monitoring-and-autonomy-update-v080).
- v0.8.10 records [native Desktop and bounded recall acceptance](docs/native-desktop-recall-acceptance.md), without changing the source patch.
- v0.8.13 [explains settings write failures without exposing private paths](docs/settings-write-errors.md), with native permission-failure recovery checks.
- v0.8.14 documents an optional [eager search schema for recall workers](docs/recall-tool-policy.md): one native card pair used three requests instead of four, with the source kit unchanged.
- v0.8.15 [preserves nested settings edits followed by a null section](docs/settings-null-sections.md), matching native storage behavior on Linux and Mac.
- v0.8.18 [loads only returned adaptive recall payloads](docs/adaptive-recall-hydration.md), with byte-identical answers and fewer message bodies materialized.
- v0.8.17 [stops workers after a verified blocked handoff](docs/blocked-worker-handoff.md), preserving the hold and saving one request in a bounded two-stage card test.
- v0.8.16 [preserves ordered config type changes](docs/settings-null-sections.md#ordered-type-changes-v0816), avoiding stale fields when two writes cannot safely be combined.
- v0.8.12 [preserves settings edits across navigation, reload and close](docs/settings-autosave.md), with installed Linux acceptance and matching Linux/Mac source.
- v0.8.11 [names shared settings controls for assistive navigation](docs/settings-accessibility.md), with installed Linux save/readback acceptance and native Linux/Mac packages.
- v0.8.9 [forwards worker progress through the unified Gateway roster](docs/unified-worker-progress.md), with isolated real-card acceptance.
- v0.8.8 [bounds retained token-estimate memo memory](docs/token-memo-memory.md), preserving estimates and normal cache reuse.
- v0.8.6 separates [vision caches by the active or saved connection](docs/vision-cache-routes.md), preventing stale answers after an endpoint or connection-mode change.
- v0.8.5 keeps [worker progress readable in narrow rows](docs/worker-monitor-readability.md), including long tool names and a complete hover summary.
- v0.8.4 [bounds retained search cache memory](docs/search-cache-memory.md), preserving disk reuse and releasing expired payloads on lookup.
- v0.8.3 [attributes post-turn goal judges to their owning sessions](docs/goal-usage-accounting.md), retaining cache/reasoning usage and concurrent-profile isolation without adding requests.
- v0.8.2 repairs retention guards and verifies archived payloads before retiring source files. See [storage retention safeguards](docs/storage-and-backups.md#retention-safeguards-v082).
- [Scheduled retention](docs/storage-and-backups.md#age-out-disposable-data-on-a-schedule) for scratch, backups, side builds and reports, so a busy fleet does not fill the disk.
- The historical **582-path cumulative kit** remains available for its different pinned base. See [its inventory](patches/manifest.json); do not stack it over the consolidated stable kit.
- An optional [cache-miss evidence repair for v0.22.5](docs/cache-miss-evidence.md) stops attributing misses to expiry from idle time alone; it preserves historical metrics and request/cache policy.
- A [role-specific THINK/ACTION extension for upstream v0.22.5](docs/stable-role-workflows.md) adds native bounded plans, pinned ACTION steps, independent review, re-planning and per-bot model/effort editing. It includes the runtime repairs as one alternative full patch; family labels do not prove provider readiness.
- A separate [nine-path runtime repair for upstream v0.22.5](docs/stable-runtime-repair.md) preserves rotating Codex account headers and managed-worker wire modes, and keeps routine confirmations from blocking dialogs. Its base differs from the cumulative kit. An exact upgrade from the earlier seven-path transport unit is included; do not stack full patches.
- Reuse a compatible, already published PM checker across launcher scopes without dependency preparation or changing the selected environment. See [startup cache behavior](docs/installation-and-rollback.md#startup-checker-cache).
- Native current-work Kanban with separate bounded history, integrated sidebar ownership and corrected Models/Usage destinations.
- Full native saved-chat/project managers, bot/group/section actions, an always-visible device/profile/status bar, and pane/status plugin discovery. See [feature parity](docs/desktop-feature-parity.md).
- [Shared prompt guidance](docs/shared-prompt-prefix.md) for new builds, with byte-preserving restoration of prior layouts.
- [Optional prompt-cache TTL policy](docs/prompt-cache-policy.md) with an isolated native config recipe and a minimal merge fragment.
- Resilient saved-chat search, whitespace-tolerant bot/Hub queries, local Hub type filters and explicit member-catalog loading/retry.
- [Usability repairs](docs/desktop-usability.md): full-history search handoff, file-preview Back/history, fit/focus Workflow, searchable goal skills, honest Hub search and explicit bot introductions.
- Native **Focus / Workspace** navigation, a revision-bound Goal form and evidence-based Catch up. See the [Desktop interface guide](docs/focus-workspace.md).
- Native task/run ownership checks; exactly-once dispatch; input preflight; recoverable compact handoffs; worker completion that avoids a needless follow-up model turn.
- Bounded file/status reads, cache diagnostics, task/run usage attribution, waiting without repeated model calls, and worker phase timing.
- Coalesce concurrent model-catalog reads within a profile and credential scope; bound retained catalogs and preserve explicit refresh.
- Keep provider-confirmed context windows and local probes tied to their credential and home; serialize durable window updates.
- Metadata-only session bindings, native search identity reads, notification destination checks and MRU/export preflight selection avoid hydrating full prompt and tool context for small runtime values. See [measurement and limits](docs/session-metadata-reads.md).
- Chunk JSONL file exports through native staging to avoid a whole serialized backup copy, while keeping hard-link and special-file behavior. See [export limits](docs/session-metadata-reads.md#chunked-jsonl-export-v0611).
- Recognize the GPT-6.1 Terra Codex reasoning vocabulary, including its supported max effort.
- Select and inspect reasoning effort for individual Kanban tasks, without changing a profile's default.
- Stop verified completed workers at budget checkpoints without an extra model call.
- Continue bounded usage reports when a log rotates during file selection.
- Include explicitly selected additional Kanban databases in read-only usage attribution.
- Set per-task reasoning effort when creating cards through the native Kanban CLI.
- Report privacy-preserving cross-profile cache cohorts from existing bounded diagnostics.
- Keep verified live goal waits parked and pause unverified waits without another model turn.
- Preserve older recovery snapshots when a critical file is skipped or cannot be captured.
- Keep active task claims and explicit holds safe during autonomous reassignment.
- Show routine task status without waking an assistant; retain actionable handoffs.
- Prevent concurrent duplicate task creation for the same idempotency key.
- Respect emergency stop and shared capacity across dispatch entry points.
- Keep new work paused when the emergency-stop sentinel cannot be inspected.
- Report unconfirmed pause and resume operations truthfully.
- Honor global pause from every profile in the same fleet.
- Keep linked emergency stops active without overwriting their targets.
- Check fresh bot availability in the owning fleet when reassigning.
- Resolve session links within the caller fleet and reject conflicting profiles.
- Preserve the originating profile when generating session links.
- Search within a specific session to recover compacted context.
- Keep slow-search telemetry useful without recording the search text.
- Bound full-text search snippets while retaining a genuine match highlight.
- Use a healthy existing CJK index for read-only cross-profile session search.
- Discover structured text and encoded tool arguments with bounded, source-linked excerpts.
- Keep repeated history scans from retaining per-row native Blob bookkeeping.
- Preserve quoted phrases and Latin prefix searches through indexed search fallbacks.
- Search text in multimodal messages and page matching tool arguments without loading image payloads into the result.
- Recover large history messages in bounded pages that respect visibility and profile boundaries.
- Keep demoted tool results recoverable through compaction.
- Restore an older session outside the loaded sidebar page when its owner is verified, without discarding uncertain remembered navigation.
- [Bounded conversation title recall](docs/session-recall.md) preserves orientation evidence while avoiding full-transcript reads and applying metadata exclusions before payload reads.
- Reuse of unchanged bundled locale parses across profiles, with independent mutable catalogs and private overlays. Local counters make this reuse observable without reading translations.
- Reuse of immutable bundled plugin code across profile namespaces, preserving separate module globals, private-plugin imports and native activation gates.
- Icon-led bot activity with bounded worker details, terminal/offline fences and compression-tip metadata that follows the displayed session. See [bot activity](docs/bot-activity.md).
- Fifteen renamed role templates and eleven reusable English skills. They contain no account configuration, credentials, personal persona or production transcripts.

Read the [feature catalog](docs/features.md), [role guide](docs/bot-roles.md), and [verification record](docs/verification.md). Use the [deployment acceptance checklist](docs/acceptance-checklist.md) to distinguish installed code, runtime adoption and measured workload results. A feature's inclusion does not establish a live performance saving for your workload.

Use [native goals, skills and delegated decisions](docs/goals-and-delegated-decisions.md) to let a Captain carry an authorized objective through verification within current quotas and approval gates.

Use the [storage and backup guide](docs/storage-and-backups.md) to avoid redundant full backups and review the offline helper for compacting explicitly selected older standalone snapshots.

Review the [optional external-memory pilot guide](docs/external-memory-pilot.md) before adding capture hooks or another memory service. It separates project isolation, automatic imports, authentication and evidence from installing or expanding an integration.

## Try the offline examples from a public download

Clone the release and run from its repository root; the same commands work after extracting the release archive and entering its top-level directory. Only Python and Git are needed for this companion-only walkthrough. Native profile setup has the additional upstream prerequisites documented separately.

```sh
git clone --branch v0.8.10 --single-branch https://github.com/ap08960695/hermes-legion.git
cd hermes-legion
python3 scripts/verify_release.py
python3 scripts/legion_plan.py --team examples/team.full.json --snapshot examples/snapshots/synthetic-ready.json --tasks examples/scenarios/parallel-production.json --now 1
```

The walkthrough pins v0.8.10. The consolidated stable kit is an alternative to the historical cumulative patch and the smaller stable units; select exactly one matching manifest. Source application, a running application, original-session adoption and measured workload improvements remain separate evidence. See the [verification record](docs/verification.md).

For an existing Mac, follow the [isolated source installation and update guide](docs/macos-install-update.md). It keeps native CLI, Desktop packaging and production activation evidence separate.

Use [on-demand memory diagnostics](docs/runtime-memory-diagnostics.md) to distinguish process memory from native cache counts without reading conversations or starting inference. Optional allocation tracing is disabled by default and belongs in an idle maintenance window.

## Prepare and diagnose a team offline

Use the [doctor and setup bundle guide](docs/offline-setup-tools.md) to inspect placeholders, preview a new-file diff and export config/SOUL into a fresh private directory. Nothing is installed or authenticated. The starter team and model map below are synthetic; model availability and runtime readiness remain unknown.

```sh
python3 scripts/legion_setup.py --team examples/team.small.json --models examples/models.small.synthetic.json
python3 scripts/legion_plan.py --team examples/team.full.json --snapshot examples/snapshots/synthetic-codex-cooldown.json --tasks examples/scenarios/sticky-session.json --pins examples/session-pins.synthetic.json --now 1 --explain
```

See [idle-only Gateway updates](docs/idle-updates.md) for the native opt-in request that refuses live or unreadable background work without forcing a restart.

## Start safely

1. Use an **isolated checkout**, not the installation currently running your work.
2. Follow [installation and rollback](docs/installation-and-rollback.md). Compatibility is deliberately narrow; mismatched source must fail rather than be force-patched.
3. Review the role templates and use only accounts and provider lanes you already have permission to use. Templates are reference material, not an automatic account/profile installer.
4. Keep your existing quotas, approvals, ownership and publication gates. Paid fallback is disabled by policy, not supplied as a hidden recovery route.

No model call, account login, live session resume, service restart, dependency installation or user configuration change is performed by this repository's verification scripts.

## A Captain-led team, not just role names

The [full team example](examples/team.full.json) describes **34 profiles**: Captain/planner, native-provider twins for thirteen specialist families, and six purpose-specific Web bots. Code, analysis, research, review, testing, documents, media, voice preparation, operations and maintenance have distinct responsibilities. No private bot names, accounts, avatars or persona files are copied.

- [Team and workflow](docs/team-workflow.md) · [complete role roster](docs/bot-roles.md)
- [Multiple accounts and native pool ownership](docs/multi-account.md)
- [Manual native setup with config fragments](docs/setup-multi-account.md)
- [Session stability and shared quota](docs/shared-quota.md)
- [Offline routing dry-run](docs/offline-planner.md)

```sh
python3 scripts/legion_plan.py --team examples/team.full.json \
  --snapshot examples/snapshots/synthetic-ready.json \
  --tasks examples/scenarios/parallel-production.json --now 1
```

The dry-run makes no model request or live change. Synthetic examples do not certify runtime routing: actual account selection, quotas, ownership and dispatch remain native. The patch itself remains the same pinned compatibility unit.

## Privacy and licensing

This repository contains generic source changes and synthetic examples. Live databases, conversations, logs, account inventories, secret stores and private Git history are excluded. See [security policy](SECURITY.md), [privacy review process](docs/privacy-review.md), and [third-party notices](THIRD_PARTY_NOTICES.md).

MIT licensed. Preserve the upstream copyright notice when redistributing included Hermes code. This project does not grant permission to bypass a provider's terms or limits.

Native UI guides: [Hub and shared collections](docs/shared-spaces.md), [Rich answers](docs/rich-answers.md), and [Focus and Workflow](docs/focus-workspace.md).

Hosted Group Chats now keep empty profiles thread-free behind the native ready gate. See [idle hosted rooms](docs/hosted-room-idle.md) for discovery, stop fencing and measured limits.

Repeated plugin manifest reads now reuse the native YAML file cache while each caller keeps private mutable metadata. See [manifest metadata reuse](docs/plugin-manifest-cache.md) for validation and measured limits.

Cold profile SQLite opens now run off the event loop with native cancellation and shutdown custody. See [profile startup I/O](docs/profile-startup-io.md) for verification; the former standby/control issue is resolved in [ready standby group controls](docs/standby-group-controls.md).

Ready standby coordinators now accept canonical group creation and messages through their native owner without allocating idle supervisor threads. See [standby group controls](docs/standby-group-controls.md).

Fresh SQLite schema declarations now commit atomically with less initialization overhead; existing stores retain their native reconciliation path. See [fresh schema startup](docs/fresh-schema-startup.md) for measurements and limits.

Profile initialization now retains physical database-write custody through cancellation and native shutdown. See [profile bootstrap custody](docs/profile-bootstrap-custody.md) for behavior and verification limits.

Additional direct session-authority callers now have host-independent offline fixtures. See [authority caller verification](docs/authority-caller-verification.md) for the baseline classification and final selection.

Config metadata I/O failures now retain native last-good owner settings, including effort ceilings. See [config metadata recovery](docs/config-metadata-recovery.md) for behavior and limits.

Config backups now publish complete generations with collision-free names and fresh rotation after concurrent copies. See [config backup publication](docs/config-backup-publication.md).

Good config backups now preserve the exact generation a native reader parsed, preventing later concurrent edits from being mislabeled as validated. See [validated config snapshots](docs/config-backup-snapshot.md).

Completed profile retirement now releases only its old config cache entries while parked homes and unfinished writers retain recovery state. See [profile config cache retirement](docs/profile-config-cache-retirement.md).

MCP schema-cache publishers now retain peer server entries across concurrent processes. See [concurrent MCP schema publication](docs/mcp-schema-publication.md).

Auxiliary Codex requests preserve selected reasoning effort and owner ceilings through SDK serialization. See [auxiliary effort fidelity](docs/auxiliary-codex-effort.md).

Known mandatory native auxiliary models now start at their cheap supported floor. See [native auxiliary floor](docs/native-auxiliary-reasoning-floor.md).

Managed workers now pin their owning source after environment sanitization. See [managed-worker source pinning](docs/managed-worker-source-pinning.md).

Inspect saved role pairs and dispatch policy with one [native routing snapshot](docs/profile-routing-snapshot.md), without a model call.

A [bounded real-provider parallel case](docs/parallel-native-acceptance.md) completed with native THINK/ACTION binding, independent review and measured request overlap. The report distinguishes this result from production adoption or measured savings.

[Async auxiliary retries](docs/async-auxiliary-retries.md) now respect the configured zero budget while keeping the existing one-retry ceiling.

[Cross-board goal waiting](docs/goal-kanban-awareness.md) counts followed work through read-only native SQLite probes while retaining worker board fences.

[Gateway goal destination identity](docs/goal-notification-identity.md) keeps history IDs separate from the platform/chat/thread/profile that subscribed to work.

[Resume goal decisions after completed card-result turns](docs/goal-result-waits.md) without waking a model from passive polls or overriding explicit waits.

[Local result wakes use their owning Gateway](docs/local-result-wake.md), preserving the native FIFO and queued human input.
