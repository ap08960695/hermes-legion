# Bounded conversation title recall

For dedicated recall workers, an optional [eager search schema recipe](recall-tool-policy.md)
can avoid a tool-discovery turn. It uses existing native settings and has a separate
bounded card comparison; the search implementation below is unchanged.

Use native `session_search` to find earlier work and then request the relevant
anchored messages. A title match should not load a whole long conversation just
to return a small orientation window.

From v0.6.7, the cumulative patch uses the existing native message-bookend API for
title discovery: five head messages, three tail messages and the total count.
The existing anchored view still provides its own bounded evidence window.
Time and explicit session exclusions are checked from metadata before loading a
title's message payload. Existing profile, hidden-source and compression-lineage
boundaries continue to apply.

Normal successful responses keep their message IDs, content caps, total-based
continuation counts and orientation evidence. An older database adapter without
the bookend API keeps the legacy compatibility path. If a present bounded API
fails, the tool reports unavailable history rather than retrying a full transcript
or treating the conversation as empty. A genuinely empty conversation remains a
successful empty result.

## What was measured

An offline native SQLite fixture contains 256 messages with 16,384 filler
characters each. Five alternating before/after runs in the same process produced
byte-equivalent responses:

| Median | Before | After |
|---|---:|---:|
| Native query time | 6.74 ms | 2.00 ms |
| Peak Python traced allocations | 4.52 MiB | 0.37 MiB |
| Message rows hydrated | 265 | 17 |
| Unbounded transcript reads | 1 | 0 |

Counts include the existing anchored-view hydration. Metadata-filter controls
read zero message rows. These measurements used the canonical installed module
against a synthetic read-only database; they describe neither whole-process RSS
nor production model latency, cache hits or token savings.

A separate read-only check of an existing saved conversation also matched the
original result and avoided the unbounded read. No title, transcript, session ID,
response hash or private workload measurement is included in this repository.
No provider request was needed for either check.

## Regression and adoption boundaries

The final targeted native run passed 76 tests across four files, with zero file
retries. It covers title hydration, time/exclusion filtering, continuation counts,
inactive rows, older adapters, empty history, bounded-read failure and existing
search/profile/context behavior. Use the pinned checkout's normal test runner:

```sh
scripts/run_tests.sh -j 2 \
  tests/tools/test_session_search_title_bounds.py \
  tests/tools/test_session_search.py \
  tests/agent/test_inline_session_search_profile.py \
  tests/hermes_cli/test_session_search_context_batch.py
```

The local runtime and regression file were installed before export, preserving
their permissions and ownership with target-only rollback copies. A fresh native
import uses the installed code. A long-lived process can still have the previous
module cached: preserve active turns and use the existing idle-update procedure
when adoption is needed. Source installation and a read-only recall check do not
prove that every already running bot has re-imported the module.


From v0.6.8, title and lineage identity also use
[context-free metadata reads](session-metadata-reads.md#search-identity-reads-v068).
The bounded message window above remains unchanged. Exact title-to-ID resolution
preserves canonical Bot Chat and numbered-continuation behavior without resolving
the full prompt or tool context merely to select the session.


## Nonfinite session start times (v0.8.60)

A saved SQLite REAL infinity in `sessions.started_at` previously escaped the
shared timestamp conversion as `OverflowError`. Title lookup, explicit
session-plus-query search and message paging could all fail even without a date
filter. The helper already promises None for an unusable timestamp; it now catches
failed numeric conversion and overflowing numeric text consistently.

These metadata checks retain their existing policy: an unknown start passes when
no date bound is requested and fails when a bound is requested. Finite matching
dates still work. Exact integer values, including large integers, finite float
truncation, numeric strings, ISO dates/datetimes and boolean/empty handling remain.
This does not repair or rewrite stored timestamps, change the global FTS query,
ranking, profile or visibility policy, or add a model call or retry.

Actual native Mac Python 3.14.9 stores signed infinity in a synthetic database and
reproduces failure in all three modes. Twenty direct conversion cases and 36
registered-handler cases cover signed infinity plus finite controls, writer and
actual read-only handles, and unbounded/matching-bound requests. After correcting
a test-only attribute typo before the production edit, original source gives 31
conversion failures and 33 passing controls; repaired and reapplied focused files
pass all 64. Numeric NaN is covered directly; SQLite converts it to NULL, so it is
not claimed as persisted numeric-NaN evidence.

The native read-only handles reject UPDATE with SQLITE_READONLY and close on
success/error. Main/WAL bytes and a separate observer's data_version stay unchanged
across calls; reader closure precedes byte comparison. The seed writer remains
open during observation, so its final close/checkpoint is outside that comparison.
Derived shared-memory sidecars are not claimed byte-immutable. Tests use synthetic
history only; no owner conversation or inference request is used.

A seven-file admitted search selection passes 214, zero failures/skips/retries,
with one exact mixed-case symlink fixture deselected. Initial baseline records
54 passes/one FileExistsError: this filesystem cannot create `WoRk` beside `work`.
That case fails before its behavior assertion and remains unchanged/unverified,
not a green full-native-suite result. See the [verification record](verification.md)
for exact selection, export and release gates. Original-session continuation,
owner-process adoption, UI, Linux parity and workload gains remain separate.
