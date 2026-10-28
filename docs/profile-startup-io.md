# Responsive profile database startup

Opening a cold profile's native SQLite store previously ran on the Gateway event
loop. Slow storage or schema initialization could delay reads and control requests
for profiles that were already served. Profile bring-up now opens the same native
cached store through the Gateway's existing context-preserving owned executor.

The launch profile still initializes first and secondary order is unchanged. This
is not a new parallel startup scheduler. Profile home, secret/terminal ContextVars,
store ownership and the one-writer handle cache retain their existing semantics.
The existing native database unwrap helper is reused; no second writer is created.

Cancellation observes one shielded opener until its physical work finishes, even
if cancellation is requested repeatedly, then propagates cancellation without
publishing an authority. The Gateway's existing executor shutdown fence rejects
new opens, and its drain counts an opener that is still running. Failed-store park
reasons and native priming remain intact. There are no new model calls, tools,
accounts, configuration knobs, dependencies or fallback routes.

## Validation and limitations

The focused regression passed 16 files / 48 tests with no retries. A wider caller
and lifecycle selection ran 37 files: 159 tests passed and 3 failed. All three are
in `tests/gateway/test_hosted_group_members.py` and fail identically before this
change: canonical group controls treat an armed, idle room coordinator as absent.
That pre-existing standby/control integration issue remains unresolved in this
release; it is not hidden by changing the assertions or weakening readiness gates.
Do not interpret this result as a globally green Gateway suite. Counts overlap.

Native installed Linux and macOS acceptance each passed 8 controls using real
private SQLite files, real profile reservations and the production interpreter,
with network access denied and no inference. It covers loop responsiveness,
distinct profile stores, context propagation, physical ownership, repeated
cancellation, shutdown visibility, no cancelled publication and refusal after the
shutdown fence closes. The original macOS Gateway was not started. No Desktop
bundle is changed by this backend fix. Native code-health comparison is clear.

In three matched controlled storage-barrier trials, reads from the already served
owner waited approximately 2.18-2.19 seconds before the fix and 0.05-0.11 ms after.
A separate thread held the new profile open for a bounded two-second observation
window. This demonstrates event-loop responsiveness under injected I/O delay;
it does not measure production disk speed, total Gateway readiness, model latency,
tokens, cache hit rates or whole-process RAM savings.
