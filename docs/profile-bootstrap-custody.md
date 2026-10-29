# Profile preparation retains physical I/O custody

A Gateway profile is reserved before its session authority is ready. Initialization
opens its store, advances the runtime epoch, recovers inputs and unattended turns,
backfills ownership/source metadata, and adopts any supported compression lineage.
These writes run off the event loop so other served profiles remain responsive.

Previously, authority preparation used the event loop's default thread pool for
most of these operations. Cancelling the coroutine did not stop a running physical
write, yet the caller could release the profile reservation. Native Gateway shutdown
could also miss that default-pool writer. The earlier protected store opener still
used an inner Task that whole-loop cancellation could cancel separately.

The preparation path now shields the executor Future directly and waits for its
physical completion before propagating cancellation. It copies the current profile
ContextVars and resolves the Gateway's existing executor getter for every operation.
The native shutdown pool therefore sees the writer, and its closing fence refuses
new preparation work. There is no new pool, background ticker, retry or configuration.
An incomplete authority is neither published nor bound as a cron/local owner.

The same helper drains standalone authority initialization on its ordinary executor;
production Gateway initialization explicitly supplies its owned executor getter.
Published authorities keep the existing tracked mutation path. Native ownership,
profile isolation, compression checks, recovery epochs, durability, admission and
Stop gates remain in force. A caller cancellation is not a database rollback: a
write already running may commit before cancellation is returned. Normal later
recovery handles that durable state under the original epoch and lineage checks.

## Validation

The six preparation-write phases each failed under caller-only and all-new-task
cancellation before this fix: 12 failing native cases. The opener separately passed
caller-only cancellation but failed all-new-task cancellation. The final regression
covers both cancellation scopes across all seven stages, real SQLite operations,
reservation lifetime, native shutdown visibility and absence of a published owner.
The initial compression fixture had a standalone route on a multiplex profile; it
was corrected using native registry-bound session creation before counting that
phase as a product failure.

The broad native selection has 273 files / 2,349 passed /
0 failed / 16 existing skips, zero retries. The skips comprise 15
other-host cases and one existing Python/SQLite close-checkpoint capability case.
A final 3-file selection has 26 passing cases on the final bytes; it overlaps the
broad selection and is not added to it. Native code-health is clear.

Installed Linux and macOS each pass 7 controls using their production Python,
GatewayRunner, ownership registry and private synthetic SQLite homes. At every
stage, repeated whole-task cancellation waits for the real writer, the launch
profile still answers, shutdown sees the writer, and no cancelled authority is
published. Networking is denied; no model/provider call or original-user database
is used. The original macOS Gateway is not started for proof. No Desktop bundle
rebuild is required for this backend change.

This correctness fix does not establish lower model usage, better provider cache
hits, reduced RAM, faster generation, or adoption by an existing user conversation.
There is no model, account, quota, paid fallback, effort or dependency change.
