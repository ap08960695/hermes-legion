# Stop after scheduled and revision handoffs

v0.8.19 extends verified native worker termination to `kanban_schedule` and
`kanban_request_changes`. After a successful durable handoff, the worker returns
the recorded reason without another model request. Scheduled cards remain parked;
review changes return the card to the native recorded implementer with normal
parent gating. Neither state is reported as card completion.

The existing task/run/claim/PID/birth-time verification remains mandatory,
including managed-worker binding. Failed, foreign and uncommitted results do not
stop inference. Budget notices preserve verified tool-result JSON, and a handoff
on the final iteration retains its outcome and failure counter.

This extends the [blocked-handoff behavior from v0.8.17](blocked-worker-handoff.md).
No scheduling authority, unblock operation, review provenance, goal restriction,
retry policy or production dispatch setting changes.

## Verification and limits

Four regression cases failed before repair: scheduling and returning review
changes, each with ordinary and final-iteration budgets. After repair, 473 Python
tests pass across 12 related files without retries, including native tool gates,
review lifecycle, terminal proof, persistence and finalizer behavior.

One bounded pair of fresh synthetic native Linux cards each read its own card,
discovered the scheduling tool and parked with the same reason. Before repair it
used four physical model requests, including one after scheduling. After repair
it used three, with zero after scheduling. A native dispatch check left both
scheduled cards parked without spawning another attempt.

Uncached input was 10,814 tokens before and 10,601 after (about 2% lower); cached
input was 29,056 before and 18,816 after. Saving one request in this pair does not
establish a general billing or latency reduction. No actual revision worker was
run: that path is covered by offline native lifecycle/agent tests and Mac checks.

Linux and ARM64 Mac installations match all 957 source-kit paths. Eight offline
native Mac checks exercise both actual registered handoff tools and refuse
foreign claims, delegated contexts and wrong process identities. The complete
patch applies, reverses and reapplies against its pinned base. No GPU was used,
production queues were not started and the existing Gateway was not restarted.
This Python-only change does not rebuild or retest the Desktop interface.
