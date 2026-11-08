# Native checks and bounded QA memory

All twelve native blocking check groups pass on Linux against the previous native
commit, using the pinned tools, read-only source files and one check at a time.
The previous 41 Ruff findings and nine ownership/platform findings are resolved;
code health reports zero blocking findings and zero advisories across 33 changed
paths. No new checker suppression or production permission exception is added.

Eight existing consumers now obtain the live numeric Unix UID from the lightweight
`hermes_platform.host.identity.current_user_id()` fact. UID zero remains valid;
an unavailable UID does not match a numeric file owner. Ownership, private-mode,
symlink, locking and existing POSIX-only branches remain in place. The fact is not
cached and reads no environment, user name, subprocess or hardware probe. Native
Linux and macOS tests compare it with a file created by that process. The Windows
case is marked for Windows and was not executed here; no Windows runtime support
is claimed.

The remaining lint edits preserve behavior: native fixture registration remains
explicit, subprocess result assertions remain after explicit `check=False`, raw
Unicode escapes preserve their output, and the compression context retains the
same slots. Existing assertions are retained.

## Test import memory

The Desktop control test fixture previously restored the entire `sys.modules`
dictionary after each import. That discarded newly loaded transitive modules and
caused repeated imports throughout the file. It now restores only its two mocked
module entries, retaining normal module caching and the existing session cleanup.

An isolated old-fixture control crossed the unchanged 768 MiB aggregate descendant
RSS guard at 768.4 MiB and was stopped. With the fixture repair, the complete same
file passes all 33 cases at 286.6 MiB sampled aggregate RSS. This is a bounded test
process observation, not a production Hermes memory or latency claim.

## Native verification scope

Linux passes 497 cases across 33 selected files, aggregated from separate complete
file runs: 26 files/437 cases, six files/27 cases and one file/33 cases. The first
broader run stopped at its memory guard; six Gateway-area files initially could
not write their native test-guard cache. Those failures are retained. A private
cache mount fixes the harness permission issue without changing the guard or its
assertions. Successful files were not replayed merely to produce one green log.

ARM64 macOS completes one 33-file run with 496 passes, zero failures and two host
skips. It reaches 305.3 MiB sampled aggregate descendant RSS and retains at least
36 percent memory-pressure free pages. Tests use a short private scratch path,
a private native guard cache, local Unix sockets and the previously documented
read-only native process-query exception. A negative control confirms TCP bind
is denied. Production writes and external model networking remain prohibited.

Both hosts use existing separately managed test environments, one test worker and
zero automatic file retries. The original duration cache and production homes are
retained. Source-file hashes match the tested candidate.

`tests/gateway/test_worker_transport_retry_policy.py` is **not run** in this
acceptance: it starts a real private Gateway and managed worker against a local
stub. Its edit only makes the existing subprocess default explicit; its result
assertions remain. All authorized real-card slots are already consumed. The
selected tests exercise temporary databases and mocked/native components without
starting a test Gateway or calling an external model. This is not the full native
suite or a new live Captain acceptance.

## Installed delivery

Fifteen runtime files and eighteen test files are installed on Linux and macOS.
The complete kit pins 980 paths, including the new identity fact and its native
regression file. Desktop assets, dependency locks and cached prompt policy are
unchanged.

Linux verifies 904 protected paths unchanged through its transaction. Mac stops
after fifteen replacements when a new temporary file receives an additional
`com.apple.provenance` attribute. Atomic replacement is retained; the resumed
segment preserves every original owner, mode, ACL and xattr value and records
three newly added OS provenance attributes. New-file metadata is checked and
recorded. A durable pending record recovers a stopped before/after replacement;
three native private controls prove both recovery paths and refusal to overwrite
an unknown image.

The Mac resume compares a persisted 217-path protected-state baseline. The first
segment held its baseline only in memory and stopped before its final comparison,
so no complete after-hash comparison is claimed for that first segment. The
original partial receipt, failure diagnostics and the small reverse patch remain
available. Installation writes are limited to source files and private receipts;
production Gateways remain closed.

No new real card or physical model request is made. The current batch remains
17/32 requests with all twelve authorized card slots consumed. Linux GPU devices
are unavailable to QA. Live Captain adoption and broader cache, memory, latency
and throughput effects remain separate, unproven acceptance items.
