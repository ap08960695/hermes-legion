# Hermes Legion v0.30.2 — Show background reports without Reload

## What you will notice

After Hermes finishes replying to a background-task completion, its saved summary
and report appear in the current chat. Open **Subagent Tasks** to read each task's
outcome beside its name, partial output and the report, without reloading the app.
A later Reload keeps one copy. This fixes the missing live summary observed on
the native Local app.

Apply the source kit and rebuild Desktop. This kit does not replace the installed
app or restart existing work.

## Behavior and tradeoff

The gateway already sends an explicit completion kind at the start of its
backend-originated turn. Desktop now marks delegated and process completion turns
as adopted, reusing the existing bounded history refresh after the parent reply
ends. The stored projection owns the card's identity, report and deduplication;
no second live-card format or synthetic-row binding is added.

Recognized completion turns can perform that existing history refresh even when
the parent reply streamed here. Ordinary streamed turns add no read through this
rule. Stop settlement clears the flag before subsequent work. Existing execution,
interruption, error and empty-final gates remain in force; they can defer refresh.
The report appears after the parent's terminal reply, not immediately when a child
finishes. Older gateways without the completion kind retain their existing path.

No backend, model input, cached context, schema, API, dependency, timer or model
request is changed. The renderer type now describes the existing wire field.
Original dispatch cards may still appear parked after history restoration; the
completion report carries the authoritative outcome detail.

## Verification and limits

Two new cases fail on the original handler. Seven initial new cases cover report
visibility, one hydrate invocation, refresh deduplication, ordinary/no-producer
turns, stale/Stop guards and preserved prior adoption. A subsequent Stop-latch
case failed on the first candidate; a one-line interrupted-settlement reset fixes
it. All 25 nearest tests pass across three files. Scoped lint, renderer types and
build pass, with the inherited dynamic-import warning. The initial type check
caught the missing wire-field declaration, which was added before final build.

Fresh native UI Send started a parent and two delegated children in one isolated
Local home. Composer Stop ended A; its late reply could not revive it. B completed
and the parent received the native mixed result. After the streamed parent reply,
the report was visible and opened before any manual Reload/Refresh, with both
outcomes, partial text and B's report. Native Reload/reopen then showed one summary.
Only five model requests and their timing were simulated on loopback. Agents,
control, lifecycle, SQLite, renderer and history reads remained native; no lifecycle
or activity rows were seeded. The stored model body matched its delivered content.
There was no cross-home copy or profile_mismatch in this acceptance.

The initial preparatory cohort passed its 60-second gate but was stopped before
app CUA actions to complete the Stop fix and rebuild. It submitted no model request.
The final cohort passed its actual 60-second Local gate with zero SSH attempts or
executions. Across 1283 samples, Hermes count stayed at most four and RSS including
the observer peaked at 1,396,719,616 bytes. Samples can miss transients; no physical
RAM, production latency or usage saving is claimed. All owned processes stopped,
both loopback ports closed, and original trial bundles/signatures and baseline
configs were restored. Owner data, other machines and existing stops were untouched.

Four changed source/test sections pass scoped pinned-base apply/hash/reverse checks;
three existing upstream files join the kit for 1080 targets. The regression file
joins the Desktop selection. Unchanged source and mock checks were not repeated.
Process-result behavior is unit-verified; new native shell-process acceptance,
whole native suite, daily-app adoption, Linux parity, immediate external-operation
cancellation and production efficiency remain open.
