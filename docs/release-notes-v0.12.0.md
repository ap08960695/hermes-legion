# Hermes Legion v0.12.0 — lighter session metadata startup

## What you will notice

Metadata-only startup can use less RAM before opening saved history. A small
helper that preserves exact API text no longer imports the turn/compression
engine just to inspect a message field. Configuration/plugin discovery and
cached MCP registration can reach readiness without that import.

No setting or dependency changes. Gateway transcript writes, gateway branches
and CLI branches use the same unchanged helper from the existing message
metadata module. Valid strings, including empty strings, retain their bytes;
missing and non-string values still produce no sidecar. The provider prompt
prefix, stored messages and branch behavior retain their existing paths.

Opening SQLite history still loads a separate compression dependency. The
measured startup saving therefore does **not** establish lower memory after
saved-session use or a lower whole-case peak. The work avoided at startup can
be paid by the first history operation.

## One matched Mac component case

Each side first populated a local stdio server's schema cache through the
installed native MCP SDK, then stopped that setup process. Fresh native clients
used separate clean homes with identical configuration, case code, peer,
bootstrap and tool schemas. The measured workload loaded configuration,
discovered cached tools, opened SQLite, saved and replayed text, appended another
message, then made two concurrent first tool calls and one warm call.

| Phase / operation | Previous source | Changed source |
| --- | ---: | ---: |
| Cached readiness, before history: summed RSS | 116.94 MiB | 101.47 MiB |
| Processes at readiness | 1 | 1 |
| Turn engine loaded at readiness | Yes | No |
| Configuration/plugin loading | 570.18 ms | 397.36 ms |
| Cached tool discovery | 10.35 ms | 5.17 ms |
| First SQLite open, save and replay | 383.66 ms | 555.87 ms |
| RSS after that history operation | 136.13 MiB | 135.94 MiB |
| Later append | 0.32 ms | 0.36 ms |
| RSS after later append | 136.13 MiB | 135.95 MiB |
| Two concurrent first calls, batch elapsed | 336.45 ms | 335.17 ms |
| Subsequent warm call | 0.58 ms | 0.62 ms |
| Whole measured workload peak summed RSS | 214.91 MiB | 214.67 MiB |
| Maximum process count | 3 | 3 |

At cached readiness the client used **15.47 MiB less RSS (13.2%)**. Later
history and peak figures are effectively unchanged. Configuration loading gets
cheaper while the first SQLite operation gets more expensive; these results
do not demonstrate an overall workload speedup. Cold schema-cache setup is
excluded from the measured workload. Do not combine this percentage with the
different v0.10.0 or v0.11.0 cases.

The saved sidecars and tool schemas matched. The same mock server returned
counters 1 and 2 to concurrent first calls, then 3 to the warm call. All case
children and the shared supervisor stopped. One paired case with 20 ms sampling
and shared RSS pages is not a statistical benchmark. This is native Python
3.14.9/MCP 2.3.0 component acceptance on the Mac, with isolated homes. No app,
gateway, SSH, other machine, external endpoint or model was used. The task Python
audit adapter is not a complete OS sandbox.

## Verification and compatibility

A fresh-process regression imports the real `SessionStore` and constructs
transcript arguments while refusing turn-engine imports. The previous source
fails at the eager dependency; the changed source passes. Tests preserve
string/non-string handling, all transcript arguments and gateway branch rows.
Real SQLite append, reopen and rewrite retain sidecars and prompt bytes across
two isolated homes with colliding session IDs. Raw SQLite retains an empty
sidecar; the existing conversation projection omits it. That distinction is
preserved. Actual CLI branch-handler acceptance uses real SQLite and stubbed
display output, preserving the parent, child sidecars and frozen system prompt.

The helper's source and AST are unchanged. Its internal location is now
`agent.message_metadata.extract_api_content_sidecar`; all three in-tree consumers
use it. The old undocumented internal import is removed under the native
repository's internal-import policy. No compatibility wrapper is added.

The scoped native set includes the previous 24 MCP cases. Canonical native
pytest and pinned Ruff remain unavailable locally; no dependencies were fetched.
See [verification](verification.md) for export, companion and release gates.
This source kit does not rebuild or modify the owner's installed app/profile.
Memory-aware helper admission, broader storage dependencies, whole-gateway idle
RAM and live UI/monitoring work remain open standing-goal items. P0 Desktop SSH
bounds remain included unchanged.
