# Hermes Legion v0.25.0 — fewer simultaneous backend checks

## What you will notice

Desktop backend import/version checks now wait their turn instead of starting
all their Python processes together. Default capacity is one active probe, with
up to 256 waiting jobs per Electron process. An optional launch setting,
`desktop.backend_probe_limit: 2`, permits two. Helpers start on demand and exit
after their command; no idle pool or validation-result cache is added.

Every successfully admitted request runs its own fresh check. Post-install validation cannot
reuse an earlier pending result. Commands, arguments, full selected environment
and working directory are captured at entry; generation selection remains native
PM behavior, without an atomic generation guarantee during execution.

Before starting a probe, Desktop needs a safe integer available-memory reading
of at least 512 MiB from `process.availableMemory()`. Low, missing, invalid or
throwing observations wait within an admission budget equal to the existing
probe timeout, normally 15 seconds. Once admitted, each execution attempt has
its full existing timeout. This protects slow cold starts from losing execution
time to queue waiting. The existing single timeout-only retry remains.

The reservation stays held until actual close, including both retry attempts.
Timeout sends TERM, then KILL after one additional second if needed; a zero exit
after timeout is still failure. An unclosed child retains its slot, so total
completion is not guaranteed. Memory is observed only at initial admission,
not reserved or continuously guaranteed. Queue-full/admission expiry does not
retry; existing callers still map those failures to unavailable runtime and may
fall through to another discovery rung. Sustained contention can therefore delay
or prevent selecting a runtime. Arbitrary launcher descendants, bypass paths,
other helpers and other Electron processes are outside this direct-child cap.

Apply the source kit and rebuild Desktop to adopt it. The daily Mac app was not
changed or launched. No dependency, model request, credential retry, new native
probe program or extra cold-start retry is added. There is no live reconfiguration
feature for the launch setting.

## Measured on this Mac

Four fresh Node cases ran old/current/current/old. Each requested two actual
native import probes: bootstrap, YAML, dotenv and Hermes configuration. All eight
fresh checks succeeded with identical native programs, input config backups and
unchanged final config bytes. A task-local wrapper held each process for 250 ms
**after the real import** to model a slow probe; that hold was identical in both
versions. No artificial memory buffers or inference were used.

| Controlled two-probe case, median | Before | After |
| --- | ---: | ---: |
| Maximum simultaneous Python probes | 2 | 1 |
| Sampled peak combined Node + helper RSS over Node lifetime | 194.078125 MiB | 139.875 MiB |
| Sampled peak helper-only summed RSS | 106.84375 MiB | 53.375 MiB |
| Sampled peak whole harness, including observer | 222.359375 MiB | 168.1640625 MiB |
| Two fresh probes complete, including modeled holds | 782.454 ms | 1208.474 ms |
| Probe launches / survivors | 2 / 0 | 2 / 0 |

Combined sampled peak was **54.203125 MiB / 27.93% lower**, passing the threshold
fixed before measurement: at least 5% **and** 10 MiB. Completion was about 426 ms
slower in this controlled case. This does not establish normal startup latency,
whole-app/gateway idle RAM, physical memory savings or production performance.
A separate native limit-two control preserved two-way overlap and two fresh
successes. Candidate cases used the actual healthy memory observation.

An external Python/psutil observer sampled kernel state without blocking Node.
The requested interval was 20 ms; ABBA median gaps were 37.3–45.5 ms, maximum
48.0 ms. Workload RSS sums simultaneous Node/helper readings over Node lifetime,
including startup and teardown; helper-only and observer-inclusive peaks are
separate sums. At most observer + Node + two native Python children made four
known processes; sampled total stayed below 4 GiB. The task-local Python audit
refused additional processes and networking; replacement wrappers kept the tested
topology direct. This is not an OS sandbox or an arbitrary wrapper-tree guarantee.
Shared pages, missed brief peaks, loader/allocator noise, four cases and modeled
holds limit attribution. No Hermes.app, other machine, genuine OS pressure,
provider or other-OS acceptance is claimed.

## Verification and compatibility

The old regression started two children where one was required; the corrected
owner passes the same test. Four canonical Vitest files pass 113 cases across
probe admission, existing probes, launch flags and retained ticket admission.
Full Electron type checking and scoped ESLint pass. Coverage includes FIFO and
configured capacity, overflow/expiry, memory recovery and observer races, captured
invocations, full cold-start budgets, error-before-close, synchronous throw,
timeout retry, ignored TERM/escalation, failed kills, unclosed children,
duplicate close, repeated asynchronous error containment, all three callers sharing admission and fresh post-install work.
Six native audit negative controls pass, with actual native import positives.
A close-ownership review added a failing repeated-error regression, then retained
the error listener through close while preserving the first error. Final native
preflights, ABBA and configured-two control were rerun against the resulting
module hashes. Earlier successful measurements remain private and are excluded
from the final figures.

Five native paths change: three prior targets plus the upstream probe owner and
a new admission fixture join the 1,050-target kit. All 1,045 unrelated prior rows,
bytes and patch sections remain exact. Main's only changes are the new import
and launch-policy call; related P0 SSH code and other fan-out protections remain.
Patch roundtrip, installed hashes, companion tests, tracked-only release checks,
secret scans, advisor review and preservation/cleanup gate driver handoff. Lead
owns Linux sync; no direct commit, push or publication is performed here.
