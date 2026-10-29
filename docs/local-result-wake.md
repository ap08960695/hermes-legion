# Local card results return through the owning Gateway

A shared-owner automation test exposed a missing adapter binding. Local session
adapters are created lazily when a session is restored; boot-time messaging
adapters instead receive their Gateway runner during startup. The lazy adapter
had no runner, so a genuine completed-card wake skipped native session admission
and fell back to a classic message handler that local sessions do not have.
The wake was correctly refused, leaving the result unseen and the goal waiting.

After validating that the cached adapter belongs to the restored session's
actual authority, restoration now binds it to that authority's runner. Existing
wake delivery can then commit the original result through the native authority
FIFO. No second message handler, force-auth path, alternate queue, route registry,
receipt rewrite or automatic replay is introduced. Queued human input remains
intact; unowned chats and profiles cannot borrow another route's authority.

## Evidence and boundaries

A fresh real-provider discovery case used a single native Gateway session client
and the embedded automatic dispatcher. THINK and independent Analyst model calls
overlapped for about 16 seconds, without manual staged dispatch. The case used
14 physical requests and did not complete: the local wake was refused, and the
private Analyst fixture separately lacked a calculation/execution tool required
by its own verification. The original failed tasks are retained and never
replayed. A prior zero-request harness also correctly refused a second TUI owner
on the Gateway's home; the supported shared-owner client avoids that conflict.
None of these failed cases is reported as a successful full loop.

The regression exercises actual local creation/restore, authenticated viewer
membership, SQLite admission and deliver_wake, with only model scheduling held.
Before the fix, two valid-destination cases failed while two foreign-route
controls passed. After the fix the related 32-file selection has 114 latest
per-file passes, zero failures and retries. The changed shared-fixture export
was checked again separately; overlapping runs are not summed. One inherited
served-profile fixture failed on the unchanged parent because its root resolver
stub rejected the current home keyword; only that stub signature was repaired.
Scoped source health has no new findings.

Linux and macOS production Python each pass four installed-source checks: idle
result admission, admission behind queued human input, foreign chat rejection
and foreign profile rejection. These use real session authority/SQLite/FIFO,
with model scheduling held and zero model/network requests. They prove native
admission, not execution or terminal acknowledgement of a new model turn.
A fresh bounded provider-backed full-loop reacceptance remains separate work.
Original-session adoption, every provider's role pairs, production usage savings
and cross-bot cache causality are not established by these checks.

Both hosts verify the consolidated public patch and installed source parity.
Linux activation is idle-only; the original macOS Gateway remains off. Existing
models, effort ceilings, quotas, fallback rules, emergency stops, workers and
review/publication gates are preserved. The fix needs no renderer rebuild.
Earlier broad auxiliary testing still has twenty documented inherited failures;
this scoped passing selection is not a globally green upstream test suite.
