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


## ID-only resume and export preflight (v0.6.10)

Native `search_sessions` now has a keyword-only `ids_only=True` projection. It
selects session ID and the existing computed `last_active`, using exactly the same
source/workspace filters, ordering, offset and limit. The regular full-context
projection remains the default. This is a selected read shape, not a content cache
or a change to model context.

The native latest-session resolver uses it for workspace-scoped selection and
its global fallback. CLI-family/oneshot and TUI behavior remain. Both the primary
CLI and Console export guards use it to find the IDs whose stored-message counts
must be checked before loading an export. Filtered export already uses a small
native candidate projection and retains its existing behavior.

Console resolves the configured per-session export bound once. If the bound is
zero, its disabled guard does not enumerate IDs at all. Successful export still
uses the full native payload: prompt/tool storage, model configuration, archived
messages, per-row flags, timing data and backup/import fidelity are preserved.
This change does not shrink backups or bypass a positive export budget. Failure
or budget refusal still leaves an existing output untouched.

Eight new native cases cover ID/recency-only reads with context columns denied in
normal/read-only modes, source/workspace/page equivalence, real MRU workspace and
oneshot/global fallback, actual parsed CLI and Console refusals before context or
output reads, complete successful backup equivalence, and no ID scan when the
Console guard is disabled. The final native run passed **349 tests across ten
files**, with zero failures/file retries, including existing MRU, export batching,
compaction round-trip, retention and full SessionDB controls.

Five alternating installed-source pairs used 32 synthetic sessions, each with a
1,245,184-character prompt and a separate 65,536-character model-configuration
value. The measured operation enumerated the IDs, then applied the same native
per-session count guard; it did not write the full backup.

| Median per enumeration and guard | Before | After |
|---|---:|---:|
| Local query time | 51.292 ms | 0.979 ms |
| Peak Python traced allocations | 42,107,726 bytes | 17,001 bytes |
| Session rows hydrated | 32 | 32 |
| Context characters hydrated | 41,943,520 | 0 |

Every pair retained the exact ID order. A separate read-only comparison against
existing saved history also retained the order and guard outcome; no private ID,
title, prompt or workload values are published, and no history export or restore
was written. These measurements cover ID enumeration/preflight only. They are
not full-export memory, whole-process RSS, model latency, cache hits or billed
usage. Full backup payloads still require their normal memory and storage.


## Chunked JSONL export (v0.6.11)

CLI and Console file exports previously built the complete serialized JSONL string
in memory after collecting the native backup payload. They now serialize one
record at a time into the existing atomic publication path for ordinary files.
Full backup fields, session order, archived-row flags, JSON formatting and export
budget checks remain intact. Prompt-only JSONL uses the same streaming writer.
Existing target metadata and symlink handling use the native writer; missing parent
directories are not created. Existing hard-linked files and special files retain
their original direct-write behavior so linked names remain coherent. A late
serialization or write failure can leave partial data on stdout, a special file
or a hard-linked target. Staging failures preserve an ordinary existing target.

This reduces the additional serialized-output allocation; it does **not** stream
the database payload itself. Peak allocation still depends on the full collected
payload and the largest individual serialized record. It does not claim reduced
backup size, total RSS, token usage or provider cache gains.

In three synthetic runs per version using the same 32-session native SQLite fixture,
the full read-and-file-export path produced identical 15,528,045-byte output.
Median peak traced Python allocation was 107,491,242 bytes before and 24,736,700
bytes after. These are local synthetic measurements, not production RAM or latency
predictions. Existing-history serialization was compared read-only without
exporting private content or invoking a model.

## Exact session ID lookups (v0.8.54)

The native `resolve_session_id` exact branch now uses the existing metadata reader
instead of loading a full session and returning only its ID. Stored prompt, tool
context and model configuration stay in SQLite. Pending token counts still flush
before the read. Exact IDs still win over longer matching IDs; unique, ambiguous,
missing and escaped literal prefixes keep their existing SQL and return rules.
The full-session reader remains available to consumers that need context.

Actual SessionDB regressions deny unused context columns during writable and
read-only exact lookup. Controls cover prefix decoys and persisted pending token
counts. Ten cases pass, alongside 28 profile/foreign-session/accounting cases and
two selected existing full-reader/prefix cases. No provider or Gateway is started.

One native ARM64 Mac Python 3.14.9 fixture stores a 1,703,936-character prompt and
a separate 1,048,576-character model-config payload. The actual old and new resolver
methods run against the same read-only database, with setup and warmup outside
measurement. Every returned ID matches. Timing and allocation are measured
separately, alternating version order:

| Measurement | Full-session exact branch | Metadata exact branch |
| --- | ---: | ---: |
| Median batch-average time per lookup, seven batches of 40 | 0.825658 ms | 0.008156 ms |
| Range across those batch averages | 0.813438–0.857217 ms | 0.007839–0.008747 ms |
| Median peak traced allocation, three batches of 40 | 3,824,400 bytes | 9,944 bytes |
| Range across traced peaks | 3,823,776–3,824,592 bytes | 9,656–9,976 bytes |

These are one payload-heavy synthetic read path's results, not whole-service RSS,
startup, production workload or billed savings. Consumers that subsequently load
the full session still pay for that read. At v0.8.54, classic title-or-ID resume
retained its own full-row exact lookup; v0.8.55 below removes that identity read.
No unrelated direct reader, prefix query, schema, cache, prompt or route changes.
Owner installation/adoption and Linux runtime acceptance remain separate.


## Classic resume identity (v0.8.55)

Classic `_resolve_session_by_name_or_id` now calls `get_session_metadata` for its
initial exact-ID check. The selector consumes only the returned ID. It retains
ID-before-title priority, local-prefix fallback, ambiguity/missing behavior and
compression-tip projection. Fork/delegate children still do not replace the
compression continuation. Context readers used after selection retain their cost.

Seven native tests exercise the actual selector and real read-only SessionDB.
SQLite authorizers refuse prompt/tool blob reads while permitting legitimate
lineage config reads. Exact ID, title and local prefix must reach the expected
compression tip; ambiguous/missing, read failure and absent-store controls return
None. Constructor mode, connection closure and existing database bytes are checked.
The corrected original-code run has three targeted failures/four passing controls;
all seven pass after the one-call change and after export/reapply.

Preservation starts after explicit native home initialization and an ordinary CLI
import in a setup child. Each lookup runs in a fresh process, with no setup
connections/config caches and no preexisting WAL/SHM. Complete profile file bytes
and directory inventory, including SOUL.md and logs, remain unchanged except for
precisely named derived SQLite metadata: WAL is absent/empty, SHM may appear, no
journal appears. This is not a no-filesystem-write or nonempty-WAL guarantee.
Bare-home initialization creates standard scaffolding/SOUL.md; cold CLI import
creates log files. Those existing behaviors are outside this selector change.

Actual Mac Python 3.14.9 compares the original native function, compiled from its
unaltered function AST with the same native globals, against the imported candidate.
Both execute real open/read/compression-tip/close on the same synthetic database.
Its root has a 1,703,936-character prompt and 1,048,576-character unused config
payload. Setup/import and five warmups per variant precede measurement. Seven
alternating 40-call timing batches run without tracing; three separate alternating
40-call tracing batches follow GC. Every returned tip matches; database SHA stays
unchanged, WAL absent/empty and journal absent.

| Measurement | Original full reader | Metadata reader |
| --- | ---: | ---: |
| Median batch-average selector time | 2.191502 ms | 1.355344 ms |
| Timing batch-average range | 2.174574–2.421924 ms | 1.344363–1.408475 ms |
| Median traced batch peak | 3,903,339 bytes | 256,853 bytes |

All three allocation peaks equal their respective medians. This payload-heavy
component fixture includes database open/close, excludes CLI import and later
transcript use, and establishes no whole-service RSS, startup, representative
workload, model-usage or billed saving.


## Compressed resume receipts (v0.8.56)

The three native compressed-resume cases recorded as setup errors in v0.8.55 now
execute. Their fixture replaced the config loader with a zero-argument lambda;
the native owning-profile reader supplies an explicit config path. The repair
removes that test double, seeds synthetic `platform_toolsets.cli: []` YAML and
binds the native Gateway launch-home variable to the same isolated fixture home.
Production resume, configuration, authorization and receipt code are unchanged.

The unchanged fixture reproduces exactly three setup TypeErrors. A new control
uses different synthetic launch/profile YAML values: real no-argument loader
returns low reasoning effort, explicit profile path returns high, then default
still returns low. It passes while the original three still error, detecting
ignored explicit paths or profile/cache leakage. After fixture repair, four cases
pass, including after exported patch reapplication.

Actual native Mac Python 3.14.9 executes SessionAuthority, SQLite receipts,
compression children, GatewaySessionStore and in-process control dispatch. Both
classic preload and late-load paths restore the latest segment's exact transcript
while retaining the logical owner's receipt identity; direct physical-tip
addressing still raises `storage_unavailable`. These are native synthetic storage
cases, not a running Gateway, Desktop journey, original owner conversation or
model continuation.

Adjacent native compression tests include warm/cold authority reconstruction,
foreign-owner refusal and a fork with a copied owner chat ID. Together with
admitted policy/posture cases, four files pass 50 unique cases. The initial broader
run also attempts two HTTP model fixtures and fails at the unchanged network audit
guard. The admitted rerun excludes only
`test_launch_policy_reaches_real_turn_runner` and
`test_ordinary_daemon_cli_launch_policy`; those two remain network-unadmitted and
unverified. No socket permission or fallback is added, and no full native-suite,
live work, memory, speed, cache or model-usage improvement is claimed this round.


## Compression parent checks (v0.8.64)

The shared compression-child gate needs only its parent's `end_reason`. Direct
SessionDB calls now use the existing metadata reader instead of hydrating the
parent's system prompt, tool pin and model configuration. Token-count flushing
remains. Child branch, delegate, tool and reset checks still inspect the full
child before the parent read; foreign inherited markers retain their meaning.

The same algorithm is aliased by `CompressionSnapshot` inside a worker receipt.
That adapter deliberately has no metadata API and must stay on its receipt
connection. An absent or noncallable metadata reader uses the adapter's existing
full reader. A callable reader returning None or raising never retries full
context. No extra connection, flush, commit, SQL projection, cache, schema,
provider request or ownership rule is added to the snapshot path.

Seventeen original native lineage tests pass baseline. Writer/read-only SQLite
authorizers then expose ten intended unused-context failures, with 28 controls
passing. Full child rows are loaded before denying parent context columns; full
reader denial confirms the guard. The initial unconditional metadata call passes
38 focused tests but breaks two actual worker integration cases. Actual snapshot
regressions reproduce absent/noncallable-reader failures before compatibility
dispatch; callable success/None/error cases also enforce no full-reader retry.

The final seven-file selection passes 68 unique native cases, including after
export/reapply: 43 focused, lineage/export, display/resume counts, worker history/
compaction, in-process Gateway history and one selected input-ownership case.
No failed integration case is excluded. Tests preserve parent decisions, main/WAL
bytes and data version, pending-token persistence, full-reader access, exception
identity, receipt connection/transaction and absence of snapshot token flushing.
This is synthetic native storage proof, not a running Gateway or model journey.

Native Mac Python 3.14.9 compares the original function AST with the imported
final helper using the same preloaded child and a synthetic parent with a
1,703,936-byte prompt and a 1,048,576-character config payload. Setup and five
warmups per variant precede seven alternating 40-call timing batches. Three
separate 40-call tracing batches follow GC. No token delta is pending; every
result is True and database/WAL hashes remain unchanged.

| Measurement | Original parent read | Metadata parent read |
| --- | ---: | ---: |
| Median batch-average helper time | 0.786236 ms | 0.009057 ms |
| Median traced batch peak | 3,823,988 bytes | 10,142 bytes |

These payload-heavy direct-helper measurements exclude setup, import and other
lineage reads. They do not measure receipt-snapshot savings, complete resume or
Gateway latency, whole-service RSS, representative workload or provider usage.


## Declared cache-scope identity (v0.8.67)

`declared_scope_identity` needs source, parent ID and model configuration to decide
whether a host-declared cache scope can be shared. It previously used the full
session reader, hydrating prompt/tool context and doing the full row conversion.
It now selects only those three fields and retains the existing fork-marker
helper. The ordinary metadata reader is unsuitable here because it omits marker
configuration. That configuration is still read and parsed; no schema, cache,
provider key, prompt history, route, source or marker policy changes.

Direct SessionDB reads retain one token flush before lookup, including a missing
row. Missing direct rows return `(False, "")`; errors still propagate into the
caller's existing fail-closed path. Receipt snapshots use their existing bound
connection without a flush, new connection or commit. On a missing receipt row,
the original `dict(None)` TypeError remains: it must not become a false fork
verdict. The supported receipt connection supplies this distinction; no concrete
class test, flush-based adapter inference or fallback query is added.

Actual Mac Python 3.14.9 checks the original full readers and projected helper
across 84 states per direct/snapshot adapter: three raw source values, matching/
absent parents and fourteen serialized-object, SQL/JSON-null, malformed/non-object
and marker configurations. Candidate parity repeats those states. Source is tested
for fork identity before stripping, preserving the existing `" tool "` behavior.
These are overlapping characterization states, not additional pytest counts.

Baseline: 87 native cases across three files. New authorizer regressions fail on
the original for direct writer, read-only reader and receipt snapshot. The first
candidate passes 148 cases but fails an existing test that counts full-reader
calls. Its one-row-read contract is now measured with actual SQLite tracing;
that corrected test also passes against the exact original. A separate original
snapshot probe catches the initial mistaken missing-row expectation before final
repair. Corrected original red: three targeted failures and 59 controls passing
across the two affected test files. No test failure is excluded or retried.

Final seven-file selection: 149 pass, also after actual exported reapplication,
12.7 seconds, one worker. Positive identity and exact native declared-scope outputs
accompany denied prompt/tool SQL reads. Seventeen explicit marker/source cases run
through writer and read-only handles; main/WAL bytes stay exact. Snapshot checks
retain an uncommitted source update on the same connection, savepoint rollback,
unchanged total changes and queued tokens, exact missing error and read-error
identity. Direct controls verify queued 17-token/one-call deltas are flushed once
before each present/missing read; query/flush errors retain fail-closed behavior.
Existing authorized worker lineage/foreign-target denial and full-context reads
remain covered. No ownership, receipt or runtime wire format changes.

For one isolated identity-path measurement, the original function is compiled
from its exact AST and compared with the normally imported final method. Both
read the same native read-only database: a 1,806,336-byte synthetic prompt, a
1,048,576-character configuration payload and 4,096 pinned synthetic tool names.
Initialization and five warmups per variant precede measurement. Seven alternating
40-call timing batches run without tracing; three separate alternating 40-call
allocation batches follow GC. Every identity matches; main/WAL hashes and empty
pending queues remain unchanged.

| Identity-path measurement | Full session reader | Selected fields |
| --- | ---: | ---: |
| Median batch-average time | 1.255107 ms | 0.560297 ms |
| Batch-average time range | 1.252620–1.281984 ms | 0.558785–0.560969 ms |
| Median traced batch peak | 4,000,638 bytes | 2,107,076 bytes |
| Traced peak range | 4,000,046–4,000,830 bytes | 2,106,788–2,107,108 bytes |

The scope resolver memoizes per segment. This measures identity resolution, not
an every-request saving, higher provider cache-hit rate, billed usage, whole-process
RSS or end-to-end latency. Marker configuration still contributes to allocation.
No live model, MCP, fleet, service, UI or original owner-session work is performed.
Owner controls, ESTOP/pauses and stopped timers remain unchanged; adoption and
Linux/workload proof remain separate.


## Gateway compression-tip liveness (v0.8.73)

The Gateway transcript rerouter now calls `get_session_metadata(tip)` on the
parent's proven owner database. It previously called the full reader and hydrated
prompt/tool payloads and parsed configuration, although it inspected only whether
the row exists and `ended_at is None`. The transitive compression resolver still
runs first and legitimately reads configuration for lineage classification.

This is one production-line change. It preserves the owner handle, resolver,
return values, pending accounting flush and shared read/flush error propagation.
An epoch-zero end time remains closed. There is no child-by-ID ambient lookup,
new fallback or cache. Production registry handles are native `SessionDB` objects;
the existing backlog fixture now implements the established metadata method.
The full reader and other context-consuming paths remain unchanged.

Two invariant tests add seven cases to the existing Gateway session file. Six
cases use real native SQLite databases in normal/read-only modes with live,
epoch-zero and later closed tips. After resolving the real lineage, only that
unchanged resolver seam is held fixed while SQLite denies prompt, tool and model
configuration reads. The original full reader fails at the liveness gate; the
candidate succeeds and a full-reader control remains denied. Database bytes stay
unchanged. The other case exercises actual owner routing/reroute with unpublished
child IDs colliding with a closed ambient tip, preserving ambient rows/messages
and ordered owner output. It also checks pending token drainage, absent/same/no
tip, missing DB and shared error propagation. Existing multi-hop, closed-tip and
backlog assertions remain.

The native baseline passed 59 cases. Initial fixture setup used unsupported
creation keywords; it was corrected to native tool/config update methods before
product edit. The meaningful red run has six hydration failures and 60 passes.
After actual exported reverse/base/reapplication, five complete files pass 136
cases, zero failures/skips/retries/exclusions, with one worker in 13.4 s. This
includes profile isolation, canonical history/resume and compression lineage.

Seven alternating forty-call batches compare the original method, extracted with
its original module globals and binding, with the imported candidate against the
same flushed native database. Both include real compression-tip resolution. The
fixture has a 1,835,008-byte prompt and a separate 1 MiB configuration value; three
separate traced-allocation batches keep tracing overhead out of the latency runs.

| Median component metric | Original | Metadata reader |
|---|---:|---:|
| Time per liveness lookup | 1.111593 ms | 0.219958 ms |
| Peak traced allocations per forty-call batch | 4,028,144 bytes | 17,848 bytes |

Outputs match, token queues remain empty and database/WAL hashes are unchanged.
These are synthetic component latency and Python allocation measurements, not
whole-process RSS, end-to-end response time, billed usage or workload savings.
Tests use isolated Mac PM-selected Python 3.14.9 and synthetic homes; no Gateway,
service, provider or model is launched. Existing processes need normal idle source
loading; current read-only comparison finds 974/1004 kit targets matching and 30
awaiting normal lead adoption/Linux validation. Owner state and controls remain.
