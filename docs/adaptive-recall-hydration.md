# Load only the recall payloads that will be returned

v0.8.18 removes unused neighbor payloads from adaptive session discovery.
The first result retains its full window and bookends. Later compact results now
load only their matching message; bounded ID-only reads preserve their existing
before/after counts. Previously every result loaded the full payload window and
bookends before the compact response discarded them.

The reads share the existing SQLite snapshot and visibility predicates. Message
caps, snippets, ranking, links, profile boundaries, compaction access and rewind
exclusion are unchanged. Explicit full-detail discovery keeps its full windows.
No tool schema, search policy, database schema or model call is added.

## Measured acceptance

A synthetic three-session fixture with 41 messages per session produced:

| Adaptive discovery | Before | After |
|---|---:|---:|
| Payload rows materialized | 51 | 19 |
| Content characters materialized | 45,234 | 15,122 |
| Returned JSON bytes | 19,029 | 19,029 |

That is 62.7% fewer payload rows and 66.6% fewer content characters loaded for
this fixture. The complete returned JSON has the same SHA-256 before and after
on Linux and ARM64 Mac. Full-detail control results are also byte-identical,
with their original 51 payload rows and 53,294-byte response.

One regression failed before repair; 214 relevant Python cases pass across 12
files without retries, including visibility, scoped and structured recall,
read-only stores, candidate saturation and profile boundaries. The test uses the
registered tool and the real session database.

A fresh isolated native Linux card recovered all three saved synthetic codes in
three physical model requests. Its search materialized 19 payload rows. The
worker could only read its card, search the synthetic history and complete the
card; production work and GPU devices remained unavailable. Both installations
match all 956 source-kit paths, and the full patch applies, reverses and reapplies
against its pinned base.

These are payload-materialization measurements, not process RSS, disk I/O,
end-to-end latency or billing measurements. The response and its token content
remain unchanged. Model acceptance is one bounded Linux card; Mac acceptance is
native offline before/after verification and source parity. No Desktop interface
change or new visual acceptance is included.
