# Hermes Legion v0.31.1 — Keep same-goal delegation cards separate

## What you will notice

Two delegated calls with the same task name now show their own child's progress
and outcome. Stop the first child: its card says **Response stopped**, while the
second continues running and later shows its own completion. Previously both
cards could follow the first child and incorrectly show Stopped together.

Apply the source kit and rebuild Desktop. This renderer fix uses IDs already
returned by the native dispatcher; the installed daily app is not replaced.

## Behavior and compatibility

A native dispatched receipt's `subagent_ids` match only the exact live child IDs.
They are opaque values, paired in their original positions. A missing slot does
not shift the following IDs. A missing live child or an unresolved advertised
identity stays parked rather than borrowing a worker by goal, position or
synthetic tool-call key. Malformed, duplicate or misaligned ID lists remain
unresolved. A receipt without the field retains its existing legacy matching;
identical-goal ambiguity on that older path remains.

Saved dispatch history without live records still cannot tell how those children
finished; saved completion reports remain the source for historical outcomes.
No backend API, schema, dependency, poll, model call, prompt, context or stored
message change. Native Stop and completion delivery keep their existing behavior.

## Verification

Eleven regressions fail on the original matcher with 17 existing controls passing.
All 28 nearest tests pass after the fix. Model and component cases cover two
separate same-goal calls, reversed live order, exact ID misses, missing slots,
malformed/duplicate/misaligned lists, opaque IDs, legacy fallback and history.
Scoped lint, types and renderer build pass. The inherited dynamic-import warning
remains. Three existing source/test sections pass apply/hash/reverse checks on
the pinned upstream base; the kit retains 1085 paths and its test selection.
Unchanged suites and the complete source inventory were not repeated.

Before/after native Mac runs each used a fresh empty Local home and actual UI
Send to dispatch two separate calls with the exact same goal. Native dispatcher
IDs, child lifecycle, per-child Stop, state persistence and parent delivery were
real; only model reply content/timing were controlled through the same loopback
fixture. The first child's transcript identified context A before Stop. Its late
reply did not win or add a completed API call. B remained running and completed
with its own output; both completion notifications reached the parent. Each run
made seven controlled requests. The fixture limits the parent to two tool calls;
its forced final-summary hint is not evidence of production autonomy or quality.
Synthetic usage counters are not provider-usage or savings measurements.

The baseline showed both cards Stopped after B completed. The final renderer
showed A Stopped / B Running, then A Stopped / B Done before releasing the held
parent reply. Private images are r104-10-wrong-second-terminal-card.jpg,
r104b-09-stop-a.jpg and r104b-10-separate-terminal-cards.jpg under the local UI
evidence directory. Their dimensions/hashes and native before/after receipts are
retained separately from the public source kit.

Both launches passed actual 60-second Local gates with zero SSH attempts or
executions and no connection to another host. They stayed within four sampled
Hermes processes and 4 GiB extra RSS. Before/after observers collected 2742/2227
samples with maxima of 1,224,884,224/1,295,679,488 bytes including observer. These are
resource-bound samples, not a continuous peak or a memory-saving comparison.
All owned identities ended; gateway and model ports closed; original 313-entry
trial bundle, strict signature and exact config baselines were restored. The
owner's app/home/data, ESTOP, pauses and timers stayed untouched.

Daily-app adoption, Linux parity, ai connectivity, legacy/sibling monitoring,
the full native suite and production efficiency remain open.
