# Release config memory after profile retirement

Completed profile deletion and rename now release that old home's parsed config
copies and parse-warning records from the process. The multiplexer releases them
only after the native authority retirement verdict permits teardown. A still-live
home parked temporarily keeps its last-good recovery state; an unfinished writer
keeps its state and reservation. A recreated live home is checked again before
removal. Other profiles retain their existing cache objects. Canonical path aliases
are handled, and alias resolution occurs outside the shared config lock.

No new cache, registry, TTL, background sweeper, forced garbage collection, model
call, setting or dependency. This affects config-memory lifecycle, not provider
prompt caching. Profiles and session/routing identities keep their native operation
order; no user database or file is deleted by this cache helper.

Five new behavioral cases cover CLI delete/rename and Gateway retired, parked and
unfinished-authority controls. Three regressions were red and two safety controls
passed on the old code. Final latest-per-file regression is 256 files / 1,855 pass /
0 fail / 7 existing platform/capability skips, zero file retries. The integrated run
had 1,854 pass and one old fixture failure; exact prior source reproduced the same
TypeError. Only its optional-home fixture signature was corrected, then its two
cases passed. Counts replace that file's result rather than summing overlapping runs.

Production-Python isolated native delete and rename measurements compare the exact
saved prior runtime bytes against the candidate. A synthetic 2,000-entry profile
previously retained five target cache entries (2,115,396 deduplicated reachable
Python-object bytes) plus three alias entries after each operation. The candidate
retains zero target or alias entries; another live profile's cache identities stay
unchanged. These are component allocations, not process RSS/PSS, measured original
workload RAM savings, or provider-backed tests.

## Installed and interface acceptance

Linux and macOS installed sources each pass five production-Python controls with
private synthetic profiles and network denied: native CLI delete and rename,
Gateway retired-home teardown, parked-home preservation and unfinished-authority
preservation. Other live profile cache identities stay unchanged. No original user
profile is deleted or renamed by these checks, and no original macOS Gateway is
started. Existing active-user session adoption is not proved by source hashes.

The installed packaged Desktop renderer was also exercised in an isolated Linux
instance, with a private full-source backend copy and synthetic HOME. Eight UI
checkpoints cover profile selection, rename, bot editing with the Terra high cap,
compact-window confirmation, cancel, delete and reload. A count-only wrapper
around the exact candidate helper observed five naturally warmed config cache
entries becoming zero for both rename and delete. The observer delegates the
unmodified implementation; this instrumented private-copy check is separate from
the uninstrumented installed native checks. No inference requests occurred.

Earlier UI harness attempts are retained privately: they clicked behind the
Profiles overlay or observed only the launcher instead of its child backend.
Those attempts are not counted as passes or attributed to application defects.

No new account/model/quota/fallback changes, dependencies, background work or
provider prompt-cache policy. The Python change needs normal idle backend adoption;
no renderer rebuild is required. This is config-memory lifecycle cleanup, not a
claim about original-workload RSS/PSS, response latency or dollar/token savings.
