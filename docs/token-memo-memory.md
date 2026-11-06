# Bound retained token-estimate memo memory

The token-estimate memo pins message strings so identity-based fingerprints stay sound.
Its previous 4,096-entry limit could retain large message bodies even after a caller
released its own temporary message list. Close/compression release already existed,
but it did not bound retention while conversations remained open.

The memo now admits at most 32 MiB of conservatively counted key/value objects and
4,096 entries. Oldest entries are evicted first, and a single oversized entry is not
cached. Estimation still processes the complete message and returns the same number.
Shared objects count once within an entry and conservatively again across entries.
Wide Unicode uses its Python object size, not its character count. Cache bookkeeping,
active callers and transient objects are outside this accounting; it is not an RSS cap.

The native fingerprint, image-cost recalibration, prompt, model selection, context
compression policy and provider calls are unchanged. Reads keep immutable pins alive;
mutation/accounting is locked and lifecycle eviction uses snapshots. Close/compression
can still race an already-in-flight estimate that later reinserts its result; the new
bound limits retention but does not introduce a lifecycle fence or cancel other work.

## Evidence

Two regressions fail on the preceding implementation: 80 rotating half-MiB messages
retain over 40 MB of pinned strings, and an oversized 33 MiB message is admitted.
The final eight-file related selection passes 143 tests. Controls cover estimates,
image repricing, Unicode, shared references, FIFO/count limits, warm reuse, close,
compression and capacity after clear/removal. Nine overlapping installed Linux tests
also pass. This is a targeted selection, not the entire upstream suite.

A network/GPU-denied production-Python fixture creates 128 distinct half-MiB message
bodies and releases the caller references. Three samples per version give median
retained traced Python allocations of 67,225,582 bytes before and 33,096,077 after,
about 51% lower. The returned estimate sum is identical. Retained entries fall from
128 to 63; clearing the memo releases its entries. This is synthetic allocation
measurement, not a whole-process RAM or production usage claim.

A separate fitting warm workload traverses 128 smaller messages 100 times with zero
estimator recomputations on both versions. Its single measured duration is 13.48 ms
before and 14.76 ms after. Locking adds overhead; no latency improvement is claimed.
A workload larger than the byte budget can recompute more estimates. It makes no
additional model request merely because an entry was evicted.

Installation and acceptance use existing production Python environments, isolated
homes and no model requests. Existing Gateway processes are not restarted; live
adoption and end-to-end card execution remain separate requirements. Owner stops
stay in place. No GPU, worker start, dispatch, resume or model call is part of this repair.

The 918-path kit matches installed AI and ARM64 Mac source. Both production Python
environments complete the same offline retention, warm-cache and release fixture.
Source health, scoped lint, 100 companion tests and patch apply/reverse/reapply pass.
Desktop packages are unchanged.

## Fresh-process RSS follow-up

Five fresh native Linux Python processes per version, alternating baseline and
candidate, repeat the same 128 half-MiB message workload without tracing enabled.
Median retained process RSS is 103,916 KiB before and 71,024 KiB after (31.7% lower).
Median growth from each process's pre-workload RSS is 66,100 versus 33,284 KiB
(49.6% lower). All ten returned estimate sums match; retained entries remain
128 versus 63. Network and GPU devices are unavailable and no model requests run.

These are whole-process measurements of a controlled native Python fixture, not
the running production Gateway or Mac. They establish neither general latency
improvement nor provider quota savings.
