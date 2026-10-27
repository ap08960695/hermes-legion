# Hermes Legion

**Role-based bots. Parallel work. Less wasted inference.**

Hermes Legion is an independent companion kit for [Hermes Agent](https://github.com/NousResearch/hermes-agent): a reviewed cumulative patch, reusable operating skills, and fifteen English role templates. It is not an official Hermes release or a hosted service.

The design is simple: give each bot a clear responsibility, dispatch independent ready work within existing limits, preserve a stable prompt prefix, and stop a worker when its verified native completion is already durable.

## What is included

- **512 patched or added source/test files** against one explicitly pinned upstream revision, including 156 Python test files. See [patch inventory](patches/manifest.json) for the exact files and hashes.
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
- Restore an older session outside the loaded sidebar page when its owner is verified, without discarding uncertain remembered navigation.
- [Bounded conversation title recall](docs/session-recall.md) preserves orientation evidence while avoiding full-transcript reads and applying metadata exclusions before payload reads.
- Reuse of unchanged bundled locale parses across profiles, with independent mutable catalogs and private overlays. Local counters make this reuse observable without reading translations.
- Reuse of immutable bundled plugin code across profile namespaces, preserving separate module globals, private-plugin imports and native activation gates.
- Icon-led bot activity with bounded worker details, terminal/offline fences and compression-tip metadata that follows the displayed session. See [bot activity](docs/bot-activity.md).
- Fifteen renamed role templates and eleven reusable English skills. They contain no account configuration, credentials, personal persona or production transcripts.

Read the [feature catalog](docs/features.md), [role guide](docs/bot-roles.md), and [verification record](docs/verification.md). A feature's inclusion does not establish a live performance saving for your workload.

Use [native goals, skills and delegated decisions](docs/goals-and-delegated-decisions.md) to let a Captain carry an authorized objective through verification within current quotas and approval gates.

Use the [storage and backup guide](docs/storage-and-backups.md) to avoid redundant full backups and review the offline helper for compacting explicitly selected older standalone snapshots.

Review the [optional external-memory pilot guide](docs/external-memory-pilot.md) before adding capture hooks or another memory service. It separates project isolation, automatic imports, authentication and evidence from installing or expanding an integration.

## Try the offline examples from a public download

Clone the release and run from its repository root; the same commands work after extracting the release archive and entering its top-level directory. Only Python and Git are needed for this companion-only walkthrough. Native profile setup has the additional upstream prerequisites documented separately.

```sh
git clone --branch v0.6.23 --single-branch https://github.com/ap08960695/hermes-legion.git
cd hermes-legion
python3 scripts/verify_release.py
python3 scripts/legion_plan.py --team examples/team.full.json --snapshot examples/snapshots/synthetic-ready.json --tasks examples/scenarios/parallel-production.json --now 1
```

The walkthrough pins the immutable v0.6.23 release. Its native Desktop interface, session metadata reads, bot activity display, bundled locale/code reuse, local memory diagnostics and verification limits are described in the [verification record](docs/verification.md).

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
