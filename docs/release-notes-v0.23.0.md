# Hermes Legion v0.23.0 — wait for memory before source update checks

## What you will notice

Desktop source update checks now wait before starting Python when the execution
host reports less than 512 MiB available memory, or the observation is missing,
invalid or throws. Work starts once a valid observation recovers. Checks remain
on demand; no new setting, dependency, worker, pool or model request is added.
Apply the source kit and rebuild Desktop to adopt this behavior; the daily Mac
app was not rebuilt, launched or changed.

The existing queue still permits one active operation and 256 pending operations
per Electron process. Adjacent identical ordinary requests join; force checks,
channel changes and distinct execution identities retain their FIFO barriers.
Nonadjacent duplicates remain separate operations. Each caller parses its own
response, and completed results are discarded by this queue. Python's existing
update cache, launcher/bootstrap program and channel-selection policy remain.

The six-minute active budget now covers observation, memory waiting and execution.
It begins after the preceding operation settles. Time waiting behind earlier
operations stays outside this budget. A child receives only the positive whole
milliseconds remaining; zero is never passed because it disables Node's timeout.
A slow observation cannot authorize an expired launch. Admission expiry says the
source check timed out waiting for available memory; execution failures keep
their original reasons. There is no automatic process or credential retry.

## Measured on this Mac

Four fresh Node cases ran old/current/current/old against the same actual
installation-generated launcher and native `hermes_cli.source_check`. Two
identical cached requests shared one check in each arm, with matching status
objects, identical initial config/cache backups and unchanged final bytes.

A real native CLI import stayed resident for 1.5 seconds. Only the Node memory
observation was modeled: low while that process lived, healthy after its confirmed
closure. In both arms a task-local audit gate prevented Git from spawning until
the background process had actually closed. Native launcher, imports, source
check, cache reading and subsequent Git commands executed normally. The gate
keeps the experiment within the process ceiling; it is not deployed code.

| Controlled cached-check overlap | Before | After |
| --- | ---: | ---: |
| Source-check Python overlaps resident CLI | yes | no |
| Native source-check launches for two requests | 1 | 1 |
| Median combined request-window peak RSS | 229.6015625 MiB | 175.2109375 MiB |
| Median completion, including fixture phase gate | 1712.236 ms | 1975.052 ms |
| Peak runtime process count, including Node | 3 | 3 |
| Surviving test runtime | 0 | 0 |

Median peak was **54.390625 MiB / 23.7% lower**, passing the threshold fixed
before measurement: at least 5% and 10 MiB. Completion was roughly 263 ms slower
in this controlled fixture. This does not establish production latency, genuine
OS pressure response, normal-launch or whole-app RAM savings. A separate native
positive control used the actual healthy `process.availableMemory()` observer.

Recursive RSS samples ran every 20 ms. At most Node plus two Python children,
or Node plus source-check Python and Git, were live; one excluded `ps` observer
made four known measured processes. The outer orchestrator was excluded; sampled
RSS including that orchestrator and observer remained below 4 GiB. Shared pages,
Node loader/allocator variation, short-lived children between samples, four cases,
the modeled observation and the phase gate limit these numbers. No artificial
memory buffers, app launch, other machine, inference or real update/apply was used.

## Safety and verification

The old canonical regression started one child below the memory floor, where
zero were required. The updated queue has 27 passing cases, including exact
threshold, malformed/missing/throwing observations, recovery, observer/deadline
races, the last full millisecond, expiry without spawning, fresh successor budgets,
failed predecessors, single polling ownership and captured command/environment.
Existing joining, force/channel ordering, overflow and error contracts remain.

Across queue, source-channel integration and legacy fixtures, canonical Vitest
runs 31 tests: 30 pass and one native Windows-only test is skipped on Mac.
Electron TypeScript checking and ESLint on the four changed TypeScript files
pass. The source-channel fixture uses a local Git origin and redirects publication
HTTP to loopback; no external service is tested. Eight native Python audit
negative controls and a SQLite positive control pass; these are not OS containment.

Three prior native kit targets change and two upstream test files join the kit:
1,048 targets total, with all 1,043 unrelated prior targets and P0 SSH protection
exact. Native patch roundtrip, companion tests, release inventory, secret scans,
protected-state/process checks and final advisor review gate driver handoff.

The memory snapshot does not reserve RAM. Low or unavailable observations can
exhaust the budget. This covers source checks only, not backend selection,
actual updates, every helper or other Electron processes. Existing child-process
termination behavior is preserved; the timeout is not a new hard process-tree
termination guarantee. Installed-app, full updater workload and other-OS
acceptance remain open. Owner config/data, ESTOP, pauses and timers were untouched.
