# Hermes Legion

**Role-based bots. Parallel work. Less wasted inference.**

Hermes Legion is an independent companion kit for [Hermes Agent](https://github.com/NousResearch/hermes-agent): a reviewed cumulative patch, reusable operating skills, and fifteen English role templates. It is not an official Hermes release or a hosted service.

The design is simple: give each bot a clear responsibility, dispatch independent ready work within existing limits, preserve a stable prompt prefix, and stop a worker when its verified native completion is already durable.

## What is included

- **295 patched or added source/test files** against one explicitly pinned upstream revision, including 120 Python test files. See [patch inventory](patches/manifest.json) for the exact files and hashes.
- Native task/run ownership checks; exactly-once dispatch; input preflight; recoverable compact handoffs; worker completion that avoids a needless follow-up model turn.
- Bounded file/status reads, cache diagnostics, task/run usage attribution, waiting without repeated model calls, and worker phase timing.
- Fifteen renamed role templates and ten reusable English skills. They contain no account configuration, credentials, personal persona or production transcripts.

Read the [feature catalog](docs/features.md), [role guide](docs/bot-roles.md), and [verification record](docs/verification.md). A feature's inclusion does not establish a live performance saving for your workload.

Use the [storage and backup guide](docs/storage-and-backups.md) to avoid redundant full backups and review the offline helper for compacting explicitly selected older standalone snapshots.

## Try the offline examples from a public download

Clone the release and run from its repository root; the same commands work after extracting the release archive and entering its top-level directory. Only Python and Git are needed for this companion-only walkthrough. Native profile setup has the additional upstream prerequisites documented separately.

```sh
git clone --branch v0.3.2 --single-branch https://github.com/ap08960695/hermes-legion.git
cd hermes-legion
python3 scripts/verify_release.py
python3 scripts/legion_plan.py --team examples/team.full.json --snapshot examples/snapshots/synthetic-ready.json --tasks examples/scenarios/parallel-production.json --now 1
```

## Prepare and diagnose a team offline

Use the [doctor and setup bundle guide](docs/offline-setup-tools.md) to inspect placeholders, preview a new-file diff and export config/SOUL into a fresh private directory. Nothing is installed or authenticated. The starter team and model map below are synthetic; model availability and runtime readiness remain unknown.

```sh
python3 scripts/legion_setup.py --team examples/team.small.json --models examples/models.small.synthetic.json
python3 scripts/legion_plan.py --team examples/team.full.json --snapshot examples/snapshots/synthetic-codex-cooldown.json --tasks examples/scenarios/sticky-session.json --pins examples/session-pins.synthetic.json --now 1 --explain
```

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
