# Stop after a verified blocked handoff

v0.8.17 stops a dispatcher-owned worker immediately after a successful
`kanban_block` whose native run, claim and process identity are verified. The
saved blocker becomes the final response. Previously the worker asked the model
for an extra acknowledgement after the board had already recorded the hold.

Blocked and review handoffs now retain distinct turn exit reasons. A completed
conversation turn does not mean the card is done: its native state remains
blocked or in review. A handoff on the last allowed iteration also preserves the
run outcome and failure counter. Budget notices cannot corrupt the verified tool
result before it is persisted.

The existing task/run/claim/PID/birth-time checks remain controlling, including
managed-worker binding. Failed tools, uncertain ownership and delegated children
do not qualify. No unblocking, retry, goal-judge or scheduling authority is added.
Scheduling and request-changes tools were outside the v0.8.17 change;
the [v0.8.19 extension](scheduled-review-handoffs.md) covers those handoffs.

## Verification

- Two regressions failed before repair. After repair, 383 tests passed across nine
  relevant Python files, with retries disabled. The suite covers final-iteration
  holds, budget notices, rejected/foreign proof, completion and review.
- One fresh native two-stage card used four physical model requests instead of
  five in the preceding equivalent fixture. Stage one read the card and stored a
  blocked checkpoint; stage two read the same card and completed with the correct
  checkpoint. No model request followed either verified terminal tool.
- Only the external test controller released its own stage-two gate, after the
  first worker exited. The worker could not unblock tasks. The second task body
  omitted the checkpoint, which remained available in native prior-run context.
- Linux and ARM64 Mac installations match all 955 source-kit paths. Native Mac
  checks verified three handoff outcomes and refusal of foreign locks, delegated
  contexts and mismatched processes (12 checks, no model requests).
- The full patch applied, reversed and reapplied against its pinned base. No GPU
  was used, and the existing production Gateway was not restarted.

This is one synthetic pair with distinct worker sessions on the same card. It
proves bounded durable-context continuation, not same-session resumption,
long-interval recall, autonomous Captain continuation, or general latency and
billing savings. The native model acceptance ran on Linux; Mac evidence is source
parity and offline native verification. This Python change does not rebuild or
retest the Desktop interface.
