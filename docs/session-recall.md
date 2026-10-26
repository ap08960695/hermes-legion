# Bounded conversation title recall

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
