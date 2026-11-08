# UTF-8 state files with optional BOMs

Valid state files saved with a leading UTF-8 byte-order mark (BOM) could be
mistaken for missing or unreadable data. In particular, refreshing a configured
native quota adapter could discard other adapters' observations when the prior
snapshot contained a BOM. An attention policy could be refused, an update
capsule could be missed or fail to parse, and a valid positive daemon PID could
be rejected.

Seven existing readers now explicitly use `utf-8-sig`, which accepts ordinary
UTF-8 and strips an optional leading BOM. The existing native quota writer uses
UTF-8. No new refresh, retry, model request, authorization rule, ownership rule,
process signal or recovery permission is introduced. Invalid capsule identities,
foreign checkout roots and nonpositive/invalid PIDs remain rejected.

## Native verification

Five complete affected test files failed eight cases against the previous native
source on Linux; all 29 cases pass after repair on Linux and ARM64 macOS. Five
additional updater files pass 43 cases on each host, including real temporary Git
repositories, interrupted updates, foreign edits and live update-lock holders.
The current scope is **72 passing cases across ten files per host**, not the
entire native suite. Native imports use temporary Hermes homes and separately
managed test environments, with one worker and no automatic file retry.

The first broader Mac run had 24 passes and 19 failures because the private test
policy denied execution of macOS's setuid `/bin/ps`. The unchanged native guard
correctly retained the source index lock when process observation was unavailable.
A read-only diagnostic reproduced this difference with the same private lock.
The corrected test policy allows only the native `/bin/ps` process queries to
execute outside the child policy, while Python and the tested recovery processes
retain network and production-write restrictions. The existing Command Line Tools
Git is invoked directly to avoid the system wrapper's global temporary-cache
attempts. With those test-harness changes, the full five-file updater run passes
43 cases. No production guard or test assertion was weakened; the original failed
run is retained as evidence.

The final passing Linux runs reached 301.9 MiB sampled aggregate descendant RSS
and retained at least 14,991,290,368 bytes of system-available RAM. The final
passing Mac runs reached 256.8 MiB; the earlier policy-limited run reached
262.9 MiB. The Mac memory-pressure free percentage stayed at least 62 throughout
these runs. These are bounded QA observations, not a general RAM or speed
improvement claim. Source and original duration caches remain unchanged by QA.

All twelve native static-check groups were executed. Pinned Ruff still reports
41 existing findings in files unchanged by this repair; the platform checker
falls from 16 to nine existing ownership/platform findings after the seven
encoding fixes. Code health reports zero blocking findings and zero advisories
for the ten changed files. This release does not claim full native static-check
success or Windows/non-UTF-8-locale runtime acceptance.

## Installation and operating scope

The five runtime files and five test files are installed on Linux and macOS,
preserving existing file metadata and protected user state. Two new regression
files bring the complete source kit to **978 pinned paths**. The previous
auxiliary-refresh fixture repair, Desktop assets and dependency locks are
unchanged.

Production Gateways remain closed. This work adds zero real cards and zero
physical model requests: the current card batch remains at 17 requests against
the original 32-request ceiling, with all twelve authorized card slots already
consumed. Linux GPU devices were unavailable to Linux QA. Existing emergency
stops, held work, accounts and quotas are retained. Live Captain adoption and
broader cache, latency, memory and throughput effects remain unproven.
