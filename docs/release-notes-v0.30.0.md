# Hermes Legion v0.30.0 — Reopen delegated task outcomes

## What you will notice

When several background tasks finish, open their saved **Subagent Tasks** summary
after Reload. Each detail pairs the task number and name with its result, such
as **Interrupted**, **Completed** or **Failed**, above the existing report. You
can collapse and reopen it. Retained outcome details work even if the report has
no output. This makes a mixed batch understandable when returning to the chat.

Apply the source kit to the pinned upstream base and rebuild Desktop. The kit
does not replace the installed app or restart existing work. New completions
use the richer summary; older notifications retain their previous fallback.
It does not reconstruct old per-child outcomes or relabel the original dispatch
cards, which may still appear parked after Reload.

## Data and compatibility

The native notification producer maps each authoritative result index to its
task goal, retaining the existing terminal/truncation labels. It saves bounded
outcome/name lines in the existing display text. Titles are forced through the
existing secret redactor before shortening and render as plain text. Captions
are at most 200 characters and the whole display summary at most 2000; an ellipsis
marks clipping. Large batches may omit later task details from this short summary.
The existing report remains available.

No schema, API, query, dependency, timer or additional model request is added.
The model notification and its cached content keep their original bytes. Older
single-task and process-result presentation retain their existing behavior.
The existing report renderer is reused; inherited transcript paths/internal
notice text can still appear in reports. Cleaning those reports and showing the
saved completion summary before Reload are separate follow-ups.

## Verification and limits

A real Local UI Send created two native children. Composer Stop ended A while
B continued to its native heartbeat. A stale reply could not revive A; B completed
independently and the parent received the mixed result. Native Reload and
open/collapse/reopen showed Interrupted beside A and Completed beside B, with
B's report output. Only five model replies and their timing were simulated on
loopback. Native execution, control, lifecycle, SQLite and renderer were real;
no lifecycle/activity rows were seeded.

The cohort passed its actual 60-second Local gate with zero SSH attempts or
executions. Sampled Hermes process count stayed at most four; RSS including the
observer peaked at 1,355,825,152 bytes. These samples can miss brief transients
and do not establish physical memory or production savings. All owned processes
stopped, both loopback ports closed, and the original trial bundle/config and
strict signature were restored. No other machine or owner data was touched.

Three new UI/hydration cases fail before; all 14 nearest tests pass. Two new
backend cases plus updated batch assertions fail on the original implementation;
all three actual native test bodies pass under stdlib fixture adapters, not
canonical pytest/conftest. Scoped lint/types/build pass, with the pre-existing
Vite dynamic-import warning. Seven changed source/test sections pass pinned-base
apply/hash/reverse checks; unrelated kit sections are retained. One Python and
two Desktop test files join the explicit selection.

The whole native suite, daily-app adoption, Linux parity, external-operation
cancellation and production efficiency remain unverified. This capability covers
saved completion details after Reload; it does not redesign global Agents or
rewrite old dispatch history.
