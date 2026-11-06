# Less interpreter work when validating recalled text

v0.8.21 replaces the Python character-by-character surrogate scan in session
recall with a compiled regular expression over the same Unicode range. Traversal
of nested lists, tuples and dictionary keys/values stays unchanged. Malformed
legacy text is still omitted from UTF-8 tool payloads with its existing paging
recovery; valid text, ranking, windows and tool schemas are unchanged.

The change targets CPU work during recall, not prompt-cache policy or model
usage. It introduces no dependency, model call, database migration or UI change.

## Verification

A real registered full-detail search over three synthetic sessions reduced
profiled function calls from **96,989 to 6,521**, with byte-equivalent canonical
JSON. These counts include Python and C function events reported by cProfile;
they are not CPU instructions or a whole-application speedup percentage. A
separate portable multilingual regression failed on the previous implementation
(105,188 calls against a 20,000-call budget) and passed after the change. The
budget allows substantial headroom for database/tool plumbing and avoids a
wall-clock assertion.

The 12 related test files passed 212 cases; the added regression passed separately,
for **213 cases across 13 files**, without retries. Exhaustive comparison covered
all 1,114,112 Python Unicode code points, plus 92 nested message-shaping cases,
on native Linux and ARM64 Mac Python. The new registered-tool regression also
passed on native Mac. These are scoped checks, not the full upstream suite.

A fresh isolated Linux card searched full-detail synthetic histories containing
Thai, CJK and emoji text, recovered all three requested codes, and completed in
three physical provider requests. All returned HTTP 200; no request followed
completion. The worker and private Gateway stopped, with no remaining claim.
GPU devices and production cards were unavailable to this fixture. This is one
bounded recall task, not sustained production throughput or a billing result.

Both hosts received the runtime change and regression before publication. All
959 source-kit paths match the pinned manifest. Existing production services
were not restarted; already-imported modules retain their previous code until
normal reload. Desktop packages are unchanged, and this release makes no new
Mac interactive-UI claim. One prototype timing pair is insufficient for a new
latency percentage; only the measured interpreter-work reduction is claimed.
