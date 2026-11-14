# Hermes Legion v0.22.0 — bounded Desktop runtime lookups

## What you will notice

Switching or resetting a Desktop runtime now stops its old Python runtime lookup
and waits for the child to close before admitting another helper. Previously a
reset discarded the cached lookup promise while its Python process could remain
alive for up to 30 seconds; another generation could start alongside it.

Launcher runtime lookups now share the existing ticket-helper FIFO, process slots
and memory admission. The default is one lookup or ticket helper per Electron
process, configurable to two with `desktop.gateway_ticket_helper_limit`. Both
kinds share 256 waiting admissions. The lookup's existing 30-second budget now
includes queue waiting; the ticket-helper budget stays ten seconds. New children
require a valid execution-host availability snapshot of at least 512 MiB.

A failed, cancelled or timed-out lookup keeps its slot until actual child closure.
A backend selection that resolves after reset cannot start work for the obsolete
generation. The existing per-generation resolver cache, interpreter validation,
launcher arguments, profile binding, fresh native ticket grants and idle helper
retirement remain. No new setting, dependency, pool or model request is added.
Apply the source kit and rebuild Desktop to adopt it; the daily app was not changed.

## Measured on this Mac

Four fresh Node processes ran old/current/current/old against the same installed
Python interpreter and native CLI metadata/ticket functions. A task-local file
gate held each launcher after its real CLI import to reproduce a slow lookup;
a local Unix socket returned a synthetic fresh grant. No inference, remote host,
artificial memory buffers or modeled memory-availability values were used.

| Controlled runtime-reset case | Before | After |
| --- | ---: | ---: |
| Simultaneous live runtime lookups after reset | 2 | 1 |
| Peak runtime processes, including Node | 3 | 2 |
| Median combined request-window peak RSS | 170.296875 MiB | 131.640625 MiB |
| Median request completion | 841.325 ms | 911.354 ms |
| Helpers surviving after retirement | 0 | 0 |

The controlled median peak was **38.65625 MiB / 22.7% lower**, meeting the
preselected 5% and 10 MiB threshold. The request was about 70 ms slower. This is
one reset-overlap component workload, not normal-launch or whole-app RAM savings.
All four runs minted a fresh native-client ticket, rejected the stale request,
kept identical config bytes and used the exact same ticket-helper program.

Recursive RSS sampling ran every 20 ms; at most two Python children plus Node
and one excluded `ps` observer were present, below 4 GiB extra RSS. Shared pages,
Node loader/allocator noise, sampling gaps and four controlled runs limit the
numbers. No installed-app, real gateway owner, other-OS or production acceptance
is claimed. The file gate and grant server are fixture boundaries, not deployed code.

## Safety and verification

The old regression reproduced two children where one was required until actual
closure. Eighteen assert-based contracts import the actual TypeScript module;
46 canonical Vitest tests across admission, runtime validation and launcher argv
pass. Electron TypeScript checking and ESLint on the four changed TypeScript files
pass. Tests cover reset generations, delayed backend resolution, shared limits,
idle handoff, memory observation races, queue and active deadlines, synchronous
spawn failures, error/close accounting, overflow, captured identity and validation.
Native Python audit negative controls pass; these are not OS containment.

The existing shared scheduler is extended at its owner. Five existing native files change: three prior targets and two newly included
upstream test files. All 1,041 unrelated prior targets and P0 SSH protection stay
exact. Native patch apply/reverse/readback, companion tests, release inventory,
secret scans and advisor review gate handoff. No owner app, home, config, data,
ESTOP, pause or timer was changed; no other machine was contacted.

This does not cap backend installation/selection before lookup, requests already
assigned to a helper, other helper entrypoints or global Hermes memory. Low or
unknown memory can exhaust the existing deadline. A child slow to close retains
its reservation and can delay subsequent work; no retry or bypass is introduced.
