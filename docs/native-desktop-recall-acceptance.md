# Native Desktop and bounded recall acceptance

Version v0.8.10 adds verification evidence only. Source patches, dependencies,
models, production quotas, configuration and installed Desktop assets are unchanged.
The v0.8.9 source kit still matches all 919 paths on Linux and ARM64 Mac.

## Installed Desktop

The installed Linux Electron application connected through its native private
Gateway to a disposable home. Settings (model, memory and compression), the bot
roster, the worker panel and its close action, and saved-chat history were exercised.
A synthetic stored chat contained the exact rich response from the earlier real card.
Opening it through history displayed its table, bar chart and Mermaid diagram at
1280- and 640-pixel window widths. The saved response remained unchanged.

This used the packaged application and native backend, not a standalone component
mock. The test process ran without GPU devices in an isolated local network
namespace. No model request was made. The external Google Fonts stylesheet was
unavailable as expected; bundled icons were verified after their font loaded.
An early screenshot did not show the close glyph; fresh screenshots after font
readiness and a native close click passed. No source change was justified by that transient observation.

The application and private Gateway were closed afterwards. This covers the listed
read/navigation flows on Linux, not every settings edit, Mac Desktop interaction,
semantic recall, or adoption of an original production session.

## One small native recall card

A new isolated worker received the title of a synthetic saved conversation and was
asked to recover its agreed confirmation code. The answer was absent from the task
prompt. The archive contained 256 messages dated about 30 days earlier. The native
worker searched it once, returned the correct code and completed its card.

The successful run lasted 16 seconds and made four physical cloud requests at low
effort. Its executed tools were `kanban_show`, `tool_describe`, `session_search`, and
`kanban_complete`. No model request followed the terminal handoff. There was no
provider fallback, production queue activation or GPU exposure.

Native session and per-model accounting agreed on:

| Counter | Observed tokens |
| --- | ---: |
| Uncached input | 13,913 |
| Cache-read input | 30,592 |
| Cache-write input | 0 |
| Total input | 44,505 |
| Output | 109 |

Cache-read input was about 68.7% of total input for this case. These are observed
canonical token counts, not a billing statement, cross-bot-cache claim, or a matched
before/after savings estimate.

An earlier separate fixture recovered the code but exhausted its three tool rounds
before completion: the private execution fence had rejected normal read-only task
and tool-discovery calls. It remains a failed run. A new corrected fixture admitted
those native reads and used five tool rounds with a six-physical-request ceiling.
The original failed run was not resumed or rewritten; no production limit changed.
The failed case used four requests, so this recall acceptance round used eight in
all. Its test-wrapper failures are not product-performance baselines.

## Same-result offline query measurement

The live worker's search runs through the agent's inline executor, bypassing the
initial generic registry observer. No in-worker query timing is claimed. Instead,
the native search was replayed five times against the same read-only database with
network and GPU access absent. Each decoded response exactly matched the real
worker's recorded tool result.

The observer counted 20 materialized rows carrying message content, including
bookend/window overlap, and zero unbounded transcript reads per replay. The response
was 11,954 UTF-8 bytes. Median query time was 2.48 ms and median traced peak Python
allocation was 72,063 bytes. The first sample included cold setup (12.70 ms and
1,199,582 traced bytes); later samples were warm. Instrumentation adds overhead.
These are isolated query measurements, not whole-process RSS, end-to-end latency
improvement, or a new before/after comparison. Earlier controlled comparisons are
in [bounded title recall](session-recall.md) and [token memo memory](token-memo-memory.md).

The test preserved 414 protected configuration/authentication/persona/stop files and
the production Gateway's identity and idle state. Runtime adoption, continuous
Captain scheduling and broad production retention cleanup remain separate work.
