# Hermes Legion v0.16.0 — wait for memory before starting ticket helpers

## What you will notice

Desktop now waits before starting a new Python ticket helper when its execution
host reports less than 512 MiB available memory, or when availability is unknown.
This helps avoid overlapping new helpers with work already using memory. Existing
eligible helpers can still serve their own profile and obtain fresh native tickets.

The existing ten-second mint budget includes memory waiting. If memory does not
become available in time, the request reports the existing helper-admission timeout.
A missing API, invalid result or observation error waits too. No credential retry,
new setting, fallback observer process, dependency or pre-started pool is added.
The helper cap and idle settings from v0.15.0 retain their behavior.

This is a source patch: apply it and rebuild Desktop before an installed app uses
it. The owner's daily app was not rebuilt or launched for acceptance.

## Measured on this Mac

The matched case executes actual native Hermes CLI import work in one Python
process and a real native ticket-client request against a private synthetic
AF_UNIX control socket. The CLI import is held briefly. Only the memory observation
is modeled: unavailable while that process is alive, ample after its actual close.
The same native programs and initial ticket result are used on both sides.

| Same controlled-overlap case | Before | After |
| --- | ---: | ---: |
| Peak summed RSS, including Node controller | 157.156 MiB | 126.281 MiB |
| Peak native Python workload RSS, excluding controller | 90.359 MiB | 59.688 MiB |
| Maximum runtime processes, including controller | 3 | 2 |
| Import and ticket-helper processes overlap | yes | no |
| Ticket request latency | 136.22 ms | 1649.37 ms |
| Import plus ticket completion time | 1.846 s | 2.039 s |
| Ticket helpers after 5.2 seconds idle | 0 | 0 |
| RSS at that idle checkpoint, controller only | 94.750 MiB | 98.266 MiB |
| Surviving test runtime | 0 | 0 |

Combined sampled peak fell **19.6%** in this one modeled-overlap pair,
with a longer ticket wait. Idle retirement remains effective on both sides.
A separate actual healthy-observation case admitted normally while the import
process was alive: its observation was 9,726,918,656 bytes,
its ticket completed in 139.89 ms and its helpers also retired.

Recursive process-ancestry sampling targeted 20 ms. One `ps` observer is excluded
from the table; known topology is at most four processes including it. Summed RSS
counts shared pages, brief peaks may be missed, and the controller's sampling
allocations contribute to its RSS. The same private audit guards fence native
imports, files, subprocesses and sockets; six ticket-adapter negative controls
pass. They are not complete OS containment. No physical memory-pressure stress,
whole-update/gateway benchmark or general RAM-saving claim is made.

## Boundaries and compatibility

`process.availableMemory()` is a snapshot of the execution host, not a reservation
or a global RAM limit. Only a new bridge with an available process slot queries
it. Low or unknown observations use one scheduler-owned 100 ms poll. Queue drain,
expiry, reset and capacity waiting stop polling. The original FIFO admission,
256 waiting-request limit, actual-close slot accounting, idle timeout and monotonic
mint deadline remain in force. Captured queue head, generation and deadline are
checked again after observation, so a reset cannot dequeue replacement work or
start an obsolete helper.

Exact interpreter, cwd, full environment and profile isolation remain intact;
no native helper program, grant validation, runtime lookup or P0 SSH policy changes.
An existing bridge can still multiplex while other admissions wait, so sustained
activity can make another profile time out. Assigned-request/stdin buffering and
the separate 30-second runtime lookup remain outside this cap and mint budget.

Acceptance used standalone Node 22.23.4 and the existing PM Python 3.14.9 runtime.
Actual Electron app execution, Linux/Windows runtime behavior, whole-gateway idle
RAM, broader helper admission and MCP retirement remain open. Missing-API waiting
is tested explicitly; eventual app-runtime adoption remains a separate gate.
