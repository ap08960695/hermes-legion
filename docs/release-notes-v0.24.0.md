# Hermes Legion v0.24.0 — bounded Desktop ticket backlogs

## What you will notice

When many connections need fresh tickets for the same profile, Desktop sends
one request at a time to that Python helper. Further requests share the existing
256-job admission queue with runtime lookups. Previously a busy cached helper
bypassed that queue and accepted every frame into its pending/stdin path.
Overflow now reports `Gateway ticket helper queue is full`; a later request can
succeed after the queue drains. Each successful request still gets a fresh grant.

Apply the source kit and rebuild Desktop to adopt this behavior. No setting,
dependency, pre-started pool, retry or model request is added. The daily Mac app
was not changed or launched. The default helper limit remains one, configurable
to two. At a fixed configuration each helper has one unanswered written request;
lowering two to one retains the existing retirement behavior.

Ticket admission and exchange share ten seconds from mint-helper entry; earlier
backend selection and runtime lookup are outside that budget. Runtime lookups
keep their separate 30-second deadline. Queued work is FIFO: a busy head can hold
up later profiles. An idle cached helper can still bypass waiting admissions,
so sustained activity may cause queue expiry. Native error reasons, profile and
execution identity, generation reset and actual-close slot accounting remain.

## Measured on this Mac

Four fresh Node cases ran old/current/current/old using the actual native Python
ticket client and an owned Unix control socket returning synthetic fresh grants.
The first reply was held until all 64 calls entered and at least 100 ms passed.
Both arms had one native RPC in progress; these were not 64 parallel native RPCs.

| Same 64 ordinary ticket requests | Before | After |
| --- | ---: | ---: |
| Peak submitted frames without a reply | 64 | 1 |
| Waiting in admission before first reply | 0 | 63 |
| Fresh grants completed | 64 | 64 |
| Median sampled peak combined Node + helper RSS over Node lifetime | 120.46875 MiB | 120.8203125 MiB |
| Median mint completion, including reply hold | 175.935 ms | 178.750 ms |
| Native helper launches / survivors | 1 / 0 | 1 / 0 |

RSS was essentially unchanged; **no RAM saving or speed improvement is claimed**.
This feature bounds submitted work. Caller promises and queued metadata still
use memory; other helper entrypoints and Electron processes have their own limits.

A separate 300-call overload control accepted and completed all 300 before the
change. Afterward it completed 257, rejected 43 with queue-full errors, and minted
a fresh recovery grant after draining. This is an overload contract, not an equal
work or RAM comparison. All native cases used actual healthy memory observations,
identical initial config backups, unchanged final config, one helper and no survivors.

RSS came from an external Python/psutil observer, with a requested 20 ms sampling
interval and observed median gaps about 35.5–36.1 ms (maximum 40.5 ms). Peaks sum
simultaneous Node/helper RSS over Node's whole lifetime, including startup and
idle retirement; they exclude the observer. Node, helper and observer made three
known processes; sampled total including observer stayed below 4 GiB. Shared
pages, missed brief peaks, loader/allocator noise, four cases and a synthetic owner
limit these measurements. An earlier synchronous Node/ps sampler blocked replies;
its timing/RSS cohort and overload failure were retained privately and excluded.
No app, other machine, model/provider, physical memory pressure or production
performance acceptance is claimed.

## Verification and compatibility

The old canonical regression wrote two unanswered frames where one was required;
the two admission guards make it pass. Canonical Vitest passes 64 cases across
admission, runtime and argv fixtures. They cover shared capacity, fresh mixed
purpose/instance grants, head/non-head expiry, reason-preserving and fatal errors,
reset/close ownership, head blocking and idle fast-path bypass, memory, captured
identity, size validation and stable two-helper capacity. Full Electron type
checking and scoped ESLint pass. Mac canonical Unix helper fixtures hard-code
`/tmp` outside the authorized writes and were not run; the owned native fixture
covers the actual client/protocol. Six Python audit negatives pass; this is not
OS containment or full app acceptance.

Three existing native targets change, with 1,048 targets total and all 1,045
unrelated prior rows, bytes and patch sections preserved, including P0 SSH fan-out
protection. Patch roundtrip, installed hashes, companion tests, tracked-only
release verification, secret scans, advisor review and process/config preservation
gate driver handoff. No remote host was contacted; lead owns Linux sync.
