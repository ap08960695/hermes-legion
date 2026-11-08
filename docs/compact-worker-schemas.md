# Optional compact card-worker schemas

A short Kanban worker can repeatedly send full schemas for board creation,
attachments and linking even when its card only reads state and completes.
The optional [configuration fragment](../skills/goal-driven-execution/references/compact-kanban-worker.config.fragment.json)
uses native tool search to load six such schemas on demand. Eight common
lifecycle/recall tools remain direct. The underlying granted capabilities and
native permission checks stay available within that dispatcher-worker surface.

Use the [fresh-profile recipe](../skills/goal-driven-execution/references/compact-worker-schemas.md)
for a dedicated Kanban/session-recall worker. It is not a configuration for a
Captain, an existing/held conversation, or a worker that needs terminal/files.
The explicit defer list replaces the native default. It must be reviewed when
changing the pinned source kit; it is not an automatic future-default merge.
No model, account, quota, fallback or self-goal permission is supplied.
The CLI toolset path matches the native dispatcher cases exercised here;
messaging and Desktop platform toolsets are outside this recipe.

## Bounded native evidence

One completed pair used actual installed Hermes v0.22.5 with the 976-path
v0.8.28 kit, `gpt-6.1-sol`, low effort, the same existing account/route and a
small arithmetic card. The compact case ran first. Both native cards/runs
completed with `SCHEMA-5`, with the task/run/session chain checked separately
from response-body EOF and client exit.

| Per completed card | Baseline | Compact worker |
|---|---:|---:|
| Total input, including cached input | 21,242 | 16,734 |
| Uncached input | 11,258 | 9,054 |
| Cached input | 9,984 | 7,680 |
| Output tokens | 70 | 71 |
| Physical model requests | 2 | 2 |
| Canonical wire schema bytes | 33,262 | 21,404 |
| Dispatch to observed client exit | 10.241 s | 10.747 s |
| Sampled total owned-process peak RSS | 356.4 MiB | 360.9 MiB |

Total input decreased **21.22%**, uncached input **19.58%**, and schema bytes
**35.65%** in this pair. Native session `input_tokens` excludes cached input;
the totals above include it and agree with the per-request diagnostics. The
subscription route reported included usage, not an external invoice saving.

Four fresh simple-card slots were authorized. Two control cases stopped before
any physical model request: the test address-space cap conflicted with default
allocator reservations, and a strict test checker initially missed native
Responses' reserved-name alias. Both stopped cases were retained and never
replayed. Only the two unstarted slots were used after offline corrections.
This used four additional physical requests, 17 cumulative with the previous
13; the original ceiling was 32. Unused requests did not grant another card.

The controls retain the 1 GiB per-process address-space cap, an 8 GiB available
RAM startup reserve and 4 GiB running reserve. The Linux test-only allocator
setting allowed waiting threads under that same cap; it was not installed as
a production setting. The largest sampled owned-process total across all four
cases was 372.9 MiB. Linux GPU devices were unavailable to the tests. Production
Gateways and all private test Gateways remained closed after acceptance, and
900 protected production paths were unchanged.

This is **one pair**, not the planned two counterbalanced pairs. The instruction
payloads differed by 32 canonical JSON bytes, output by one token, and client
exit was observed with 0.5-second polling. The compact case was not faster and
did not use less measured RAM; its whole-card cache-read fraction was 45.89%
versus 47.00% for baseline. No cache, latency, RAM or general workload improvement
is established. Tasks that need deferred tools can add discovery turns and
cancel the input saving. Actual Captain use of the method is also unproven.

The native source kit is unchanged. This companion addition provides a reusable
opt-in fragment and on-demand guidance; it does not switch live profiles or
restart services. The existing [skill-copy doctor](captain-skill-installation.md)
checks the complete directory, including the new reference and fragment.

## Offline native compatibility

Two behavior checks pass on both Linux and ARM64 macOS in separately managed
test environments. Linux uses an isolated native checkout whose 976 pinned
source paths match the installed kit; macOS uses the installed native source.
These are offline compatibility checks, not production-session execution.
They exercise fresh-profile creation, the three
native config setters and JSON readback, preservation of unrelated settings,
native tool assembly with explicitly selected Kanban/recall toolsets, retention
of the deferred schemas in the catalog, and Responses serialization. They do
not prove profile-to-dispatcher propagation or exercise search/describe/call.
These checks start no Gateway, make no model request
and run without network access or retries, with one test worker.

To repeat against this pinned kit, copy
`verification/native_compact_worker_fragment.py` into native
`tests/hermes_cli/test_legion_compact_worker_fragment.py` and the fragment into
`tests/hermes_cli/fixtures/legion-compact-worker.json`. Use the native
`scripts/run_tests.sh` with the separately managed test interpreter. Bound both
the runner's precompilation CPU count and `HERMES_TEST_WORKERS` to one, and set
`HERMES_TEST_FILE_RETRIES=0`. Use an isolated home and prevent networking and
Gateway startup. The verification does not establish live Captain adoption.
