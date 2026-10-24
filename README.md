# Hermes Legion

**Role-based bots. Parallel work. Less wasted inference.**

Hermes Legion is an independent companion kit for [Hermes Agent](https://github.com/NousResearch/hermes-agent): a reviewed cumulative patch, reusable operating skills, and eight English role templates. It is not an official Hermes release or a hosted service.

The design is simple: give each bot a clear responsibility, dispatch independent ready work within existing limits, preserve a stable prompt prefix, and stop a worker when its verified native completion is already durable.

## What is included

- **279 patched or added source/test files** against one explicitly pinned upstream revision, including 109 Python test files. See [patch inventory](patches/manifest.json) for the exact files and hashes.
- Native task/run ownership checks; exactly-once dispatch; input preflight; recoverable compact handoffs; worker completion that avoids a needless follow-up model turn.
- Bounded file/status reads, cache diagnostics, task/run usage attribution, waiting without repeated model calls, and worker phase timing.
- Eight renamed role templates and ten reusable English skills. They contain no account configuration, credentials, personal persona or production transcripts.

Read the [feature catalog](docs/features.md), [role guide](docs/bot-roles.md), and [verification record](docs/verification.md). A feature's inclusion does not establish a live performance saving for your workload.

## Start safely

1. Use an **isolated checkout**, not the installation currently running your work.
2. Follow [installation and rollback](docs/installation-and-rollback.md). Compatibility is deliberately narrow; mismatched source must fail rather than be force-patched.
3. Review the role templates and use only accounts and provider lanes you already have permission to use. Templates are reference material, not an automatic account/profile installer.
4. Keep your existing quotas, approvals, ownership and publication gates. Paid fallback is disabled by policy, not supplied as a hidden recovery route.

No model call, account login, live session resume, service restart, dependency installation or user configuration change is performed by this repository's verification scripts.

## Roles

| Name | Responsibility |
|---|---|
| Legatus | Coordination and independent ready-work dispatch |
| Strategist | Planning and dependency decomposition |
| Scout | Research and source verification |
| Artificer | Implementation and bounded offline testing |
| Auditor | Independent review and evidence checks |
| Scribe | Writing, documentation and compact handoffs |
| Prism | Visual analysis when an eligible route supports it |
| Sentinel | Operations, health observation and safe recovery planning |

Roles and providers are separate. A Web label does not prove capability, authorization, available quota, audio support or guaranteed free access.

## Privacy and licensing

This repository contains generic source changes and synthetic examples. Live databases, conversations, logs, account inventories, secret stores and private Git history are excluded. See [security policy](SECURITY.md), [privacy review process](docs/privacy-review.md), and [third-party notices](THIRD_PARTY_NOTICES.md).

MIT licensed. Preserve the upstream copyright notice when redistributing included Hermes code. This project does not grant permission to bypass a provider's terms or limits.
