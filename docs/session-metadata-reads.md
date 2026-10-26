# Small session metadata reads

Runtime resume and onboarding sometimes need one entry from a session's
`model_config`, rather than its conversation context. The native
`get_session_model_config_value` method now selects only that JSON column.
Previously, it called the full session reader, which also resolved the stored
system prompt and tool context before returning the small value.

The normal full-session reader is unchanged. Missing sessions and keys retain
their supplied defaults, JSON null remains null, and a committed configuration
update is visible on the next read. No shared content cache, schema migration,
provider request, account selection or prompt-prefix change is introduced.

The regression uses the actual stored Codex thread-binding consumer with a
temporary native SQLite database. SQLite denies reads of the session's prompt
and tool-content columns; the binding must remain available in both normal and
read-only database modes. Controls cover missing defaults, nested values, null
and newly committed metadata. This is offline storage acceptance, not a model
conversation or provider-resume test.

## Isolated measurement

Seven alternating before/after batches each performed forty warm lookups against
the same native database, with a synthetic 1,703,936-byte system context. Median
results were:

| Metric | Full-session lookup | Metadata-only lookup |
|---|---:|---:|
| Time per lookup | 0.737608 ms | 0.010506 ms |
| Peak traced Python allocations during a batch | 1,733,644 bytes | 14,032 bytes |

These measurements describe this small read path under one synthetic fixture.
They are not whole-process RSS, total task latency, billed usage or a production
token-saving percentage. Neither the benchmark nor the regression calls a model.

Existing processes must load the source through their normal idle lifecycle.
Source installation and offline acceptance alone do not prove that an already
running Desktop or Gateway has adopted the change. Preserve active work and
verify fresh source identity and read-only readiness separately.


## Search identity reads (v0.6.8)

Native search also needs session identity rather than full context. The
`get_session_metadata` sibling selects exactly `id`, `source`, `model`, `title`,
`parent_session_id`, `started_at`, `ended_at` and `end_reason`. It retains the
native accounting flush before reading, so committed values stay fresh. The
existing full `get_session` reader is unchanged.

Title resolution now selects the exact session ID directly. It preserves native
canonical Bot Chat preference, numbered continuation ordering and escaped
wildcards. The full `get_session_by_title` API still returns full context for
callers that request it. Search uses the small API for root/lineage identity and
orientation metadata; evidence windows, privacy/profile boundaries and returned
responses stay intact.

Older adapters without the small reader keep their legacy compatibility path.
If a present small reader fails, search does not silently retry the heavy reader.
This is a storage-query change, with no content cache, schema migration, prompt
prefix change or alteration of the model's input context.

Five alternating before/after runs used the installed native modules with one
read-only synthetic SQLite fixture: 80 messages, 1,867,776 ASCII context
characters and a separate synthetic model configuration. Returned responses were
byte-equivalent.

| Median per discovery | Before | After |
|---|---:|---:|
| Native query time | 4.955 ms | 1.683 ms |
| Peak Python traced allocations | 2,016,703 bytes | 79,003 bytes |
| Full-session reader calls | 2 | 0 |
| Full-context title reader calls | 1 | 0 |
| Context characters materialized across those reads | 5,799,987 | 0 |

These are synthetic query and Python allocation measurements. They do not measure
whole-process RSS, cache-hit rate, billed tokens or production response time. A
separate existing-conversation read-only comparison also retained exactly the
same result; private titles, transcripts, IDs and workload measurements are not
published. Neither check called a model.

The final native run passed **395 tests across nine files**, zero failures and
zero file retries. Six new controls deny prompt/tool-column reads through the
SQLite authorizer in normal/read-only discovery, check small/fresh/missing
metadata, preserve legacy adapters, refuse heavyweight failure retries and cover
canonical/numbered title lookup. The wider run retains native session, title,
import, search, profile and anchored-context behavior.

```sh
scripts/run_tests.sh -j 2 \
  tests/hermes_state/test_session_search_metadata.py \
  tests/hermes_state/test_session_config_read.py \
  tests/tools/test_session_search.py \
  tests/tools/test_session_search_title_bounds.py \
  tests/agent/test_inline_session_search_profile.py \
  tests/hermes_cli/test_session_search_context_batch.py \
  tests/hermes_state/test_canonical_title_guard.py \
  tests/hermes_state/test_hermes_state.py \
  tests/hermes_state/test_session_import_keep_flags.py
```


## Notification destination checks (v0.6.9)

The native notification resolver now reuses the same small identity reader to
check the current session and candidate destinations. Those checks previously
hydrated prompt/tool context before applying the native compression-tip rule.
The resolver is used by subscription discovery, pending notification validation
and receipt-bound delivery admission; no new tool or polling mechanism is added.

The selected compression tip remains the only continuation allowed to inherit
ancestor work. Stale parents, explicit branches/delegates/resets, foreign profiles,
claimed receipts and owner holds keep their existing fences. Missing legacy
stores retain exact-key fallback, and older adapters without the small API retain
their original reader. A failure in a present metadata reader holds work without
retrying the full-context reader. Receipt identities and delivery states are not
rewritten. Poll intervals, model input and notification contents are unchanged.

Four new native regression cases exercise the real resolver with prompt/tool
column reads denied by SQLite, through both normal and named-profile read-only
store access, plus legacy compatibility and failed-reader behavior. The final
related native run passed **75 tests across ten files**, zero failures/retries,
including actual native compression/receipt/hold and retry-boundary contracts.
Those disposable offline delivery fixtures are not live Captain ACK proof.

Five alternating installed-source measurements used a synthetic owning store
with 1,867,776 context characters on both a root and its compression continuation.
Each measured call included a fresh native read-only store open/read/close.

| Median per destination resolution | Before | After |
|---|---:|---:|
| Native local query/open time | 3.951 ms | 1.713 ms |
| Peak Python traced allocations | 1,900,776 bytes | 21,140 bytes |
| Full-session reader calls | 3 | 0 |
| Context characters hydrated | 3,735,552 | 0 |

The returned destination sets were equal in every pair. A separate comparison
using an existing saved conversation and its owning store also retained the set,
without sending notifications, modifying receipts or calling a model. Private IDs,
titles, prompts and workload measurements are not published. The measurement
uses the existing native interpreter/dependency activation, while launch-time
PM preparation is disabled only in that private harness to prevent rebuilds or
relaunches. This is query acceptance, not a bootstrap/recovery test.

The measurements describe synthetic query/Python allocation work, not total RSS,
billed usage, model latency or provider cache hits. A smaller prompt-free lookup
does not reduce the context supplied to a model. Production notification delivery
and cache/usage improvements still require genuine eligible work; no receipt is
replayed to manufacture that evidence.
