# Preserve MCP schema caches across concurrent publishers

A Gateway, Desktop backend or fresh worker can discover MCP schemas in separate
processes for the same profile. The previous cache writer held only a Python
thread lock around its read-modify-write. Two processes could read the same old
manifest, each add a different server and both report success, while the later
atomic file replacement silently discarded the peer's server entry. Atomic
publication prevents partial JSON; it does not merge concurrent snapshots.

The writer now takes a profile-local native file lock across the complete
read-modify-publish cycle. It rereads the current manifest after acquisition and
retains the existing atomic JSON writer and private file permissions. A persistent
sidecar inode survives replacement of the JSON file. Closing the descriptor also
releases the lock after an exception or process exit; the sidecar is not unlinked
while peers could still be using it.

## Preserved boundaries

- No server connection, tool invocation, account lookup or model request runs under
  this lock. Existing manifest reads remain atomic-file reads without a file lock.
- The writer waits outside the Python thread lock, allowing another profile's
  manifest reads to proceed. The native filesystem primitive bounds acquisition
  to five seconds; refusal never falls through to an unlocked overwrite. Existing
  live-registration error handling can leave this optional cache update unwritten.
- Fingerprints, tool parameters, utility tools, server TTLs, profile scope and
  identical non-TTL write suppression keep their existing behavior.
- One small lock sidecar per cache file; no dependency, daemon, setting, provider,
  model, quota, paid fallback, prompt or active-session tool-surface changes.
- Native POSIX owner/mode validation applies on Linux/macOS. Windows uses the
  existing native byte-lock primitive; Windows end-to-end acceptance is not claimed.

## Historical publication verification

A real two-process test first failed with only one of two server entries surviving.
The repaired test retains both, including each schema. Failure injection preserves
the previous good JSON and releases the writer; acquisition refusal cannot rewrite
it. A held same-profile publisher does not block another profile's cache reads.

The final scoped regression passes 911 cases in 98 files, zero failures, one
existing platform skip, zero file retries. Code-health reports no new findings.
Focused and historical selections overlap and are not added to that count.

Production Python on installed Linux and macOS each passes five native controls:
concurrent peer publication, fresh lazy registration with required parameters,
identical-write suppression, fingerprint rejection and TTL-zero expiration.
The exact prior module retains one peer and provides one cached tool; the repaired
module retains both and provides two. The cold registry imports actual native code
without opening either MCP server, making a network request or calling a model.

The harness first initializes native version provenance through narrowly permitted
checkout-local read-only Git commands, with lazy fetching disabled. Its subsequent
cold-registration boundary denies all subprocess and network work. Earlier harness
refusals are retained privately and are not counted as application failures or
passing acceptance. The concurrency fixture deliberately pauses one publisher;
its elapsed duration is not a startup latency or throughput benchmark.

These checks use synthetic private HOME directories and actual native processes,
files and registries. They do not prove original-user conversation adoption,
production cache-hit rates, fewer model calls or measured usage/RAM savings. Normal
idle backend adoption or freshly started workers use the installed Python patch;
no Desktop renderer rebuild is required.


## Overflow-safe expiry metadata (v0.8.57)

The native reader validates optional `ttl_ms` and `written_at` before lazy schema
registration. Arbitrarily large JSON integers can overflow Python's finite-number
conversion. The normal writer accepts integer TTL hints; a persisted value such
as `10**400` previously raised from both the reader and the lazy-discovery loop,
preventing later healthy cached servers from registering.

A narrow `except OverflowError` now covers only the existing TTL validation and
deadline arithmetic, returning the ordinary cache-miss sentinel. Type/finite checks,
exact expiry, no-TTL entries, fingerprints, defensive copies, locks and cache bytes
retain their behavior. The caller leaves the invalid server in its normal eager
set and continues healthy lazy registration. No server connection is attempted by
this cache-only helper; actual eager connection remains the existing later stage.
There is no new TTL cap, metadata coercion, cache deletion or retry policy.

Actual native Mac Python 3.14.9 baseline passes five TTL tests. Persisted signed
huge integers in either field and two mixed-discovery callers produce six targeted
overflow failures with fourteen passing controls. After repair, all twenty pass.
Controls retain text/null/infinity/NaN misses, exact expiry and defensive-copy
isolation. Mixed bad-first/healthy-second discovery uses real disk reader and real
ToolRegistry registration: bad remains eager, healthy required parameters survive,
cache bytes stay unchanged, and transport traps record no spawn/connect/bind calls.

Adjacent cache SDK and publication cases give 33 unique native passes across three
files with one Linux-only skip, including actual two-process publication. Two
initial publication attempts exposed temporary wrapper issues: duplicated Python
flags, then concurrent startup selfchecks sharing a probe filename. The corrected
wrapper accepts only redundant leading `-B/-S/-I`, rejects unknown flags and uses
one positive probe per process. All admission/negative/null checks remain active;
owned failure-child and concurrent-wrapper checks pass. Both actual publisher
children exit zero and are joined. The guard is
application-scoped; OS/native-extension containment is not established.

Reapplied export passes twenty focused cases again. This proves synthetic native
cache/discovery behavior, not a running MCP server, owner-app adoption, Linux parity,
cache-hit-rate improvement, startup timing, reduced RAM or fewer model requests.


## Mixed-name filter fingerprints (v0.8.66)

Native registration accepts include/exclude lists and converts each entry to a
string. A filter such as `["lookup", 7]` therefore selects the names `lookup` and
`7`. Cache fingerprinting previously sorted the raw entries, raising TypeError
when numeric and string values were mixed. The lazy-discovery caller computes
that fingerprint before its per-server registration guard, so a first mixed
server could prevent a later healthy cached server from registering.

The shared fingerprint now converts entries with `str` before sorting, for both
include and exclude. No schema/filter acceptance, fingerprint field, JSON/hash,
trust, credential binding, retry or eager-discovery policy changes. All-string
lists, duplicate entries and legacy bare-string fingerprints keep their exact
keys. Mixed list/tuple/set permutations and equal-text numeric/string values are
deterministic. Registration's existing include-over-exclude behavior remains.

A prior numeric-only cache key can differ from its normalized key and return an
ordinary miss. Existing eager discovery may refresh it later; this release does
not rewrite entries, migrate old keys or prove transport recovery. A populated
entry with the equivalent string-filter fingerprint can be used without a new
connection. Cache bytes remain unchanged during measured reads/discovery.

Actual native Mac Python 3.14.9 baseline passes 29 cache/TTL cases with one Linux
skip. New tests produce 14 targeted failures with 15 controls/one skip before
repair: mixed fingerprints, old-key transitions and both real lazy-discovery
callers. Corrected fixture red reproduces the same failures. Final three-file
selection passes 53 cases/one Linux skip, including after export/reapply. It
retains native SDK schema roundtrip, TTL behavior and two-process publication.

Discovery uses actual YAML loading, disk cache and ToolRegistry. Both servers
are unregistered before the call; mixed is first, healthy second. Include and
exclude paths retain exact tool names and required parameters, config/cache bytes,
and zero spawn/connect/bind attempts during measured lazy registration. Loader
setup may import urllib3's local IPv6 capability probe; the unchanged native audit
guard denies that setup bind. Transport counting starts after setup/cache seeding,
without registration prewarming or a permission exception. This is fresh-process,
populated-cache, unregistered-server proof, not whole-startup zero-attempt behavior.
No running MCP service, owner-app adoption, Linux parity, provider-cache gain or
model-usage/latency/RAM saving is claimed.
