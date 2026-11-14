# Bound search cache memory without losing disk reuse

The search memo previously kept every distinct successful response until TTL cleanup
on another store. A lookup removed only its own expired query, so other expired results
could stay resident indefinitely in an otherwise idle process. Busy traffic could grow
the memo without a count or byte ceiling during the TTL window.

The in-process tier now retains at most 256 entries and 32 MiB of Python key/response
objects, measured after making the existing caller-independent copy. It evicts least
recently read entries and skips oversized results. Expiry cleanup also runs on lookup;
it does not wait for another successful provider request. The expiry index immediately
releases evicted query references, and hits reuse the canonical key rather than keeping
extra copies of long queries.

The existing profile-local disk tier still receives successful results, including
results too large for the RAM tier. A RAM miss checks that tier before issuing a vendor
request. Disk TTL, capacity, free-space guards, provider selection, response slicing,
profile isolation and in-flight request reservations are unchanged. No prompt, history,
model route or new configuration is introduced. The limit is process-wide, not per bot.

## Evidence and limits

- Five tests fail on the preceding source. The final focused and adjacent selections
  pass 75 and 332 tests, including TTL, LRU, oversized results, replacement/clear, long
  query references, reserved flight locks, real disk reuse and registry dispatch.
- Installed Linux and macOS source each pass four offline native checks using their
  production Python, temporary homes and real disk caches. Provider/fallback boundaries
  reject calls; network and GPU access are denied. No worker or service is started.
- A CPU-only fixture stores 512 distinct responses, each with 32 results containing
  4,096-character descriptions. Disk storage is stubbed only for this allocation
  measurement. The real disk tier is covered separately by tests and native checks.
  Traced retained allocations fall from 72,212,954 bytes (512 entries) to 33,623,906 bytes
  (238 entries), about 53%. Peak traced allocation falls from 72,354,897 to 33,932,232 bytes.
  After advancing beyond TTL and looking up an unseen query, the old memo still retains
  512 entries; the repaired memo has zero and retains 46,032 traced bytes.
- In that single fixture run, preparing all entries took about 0.31 seconds before and
  0.39 seconds after. Size accounting adds cold-store work; there is no claimed latency
  improvement. Cached slicing still copies only the requested result subset.

The 32 MiB limit covers retained keys and JSON response objects. Container bookkeeping,
active callers, in-flight responses and transient serialization allocations are separate;
this is not a total process RSS ceiling. Cleanup is opportunistic on cache activity, not
a background timer. A cold result can still require another vendor request if its disk
copy is unavailable, expired, oversized, or evicted. No global usage savings are claimed.

The 913-path source kit matches both installed hosts. Existing Gateway processes were
not restarted, so adoption by already-imported modules and live workload memory remain
unverified. Owner stop switches remain in place; real execution is limited to simple
test cards and has not been started as part of this repair.


## Oversized disk timestamps (v0.8.69)

A disposable disk-cache entry can contain valid JSON with an integer timestamp
too large for the existing float subtraction. Previously, that `OverflowError`
escaped cache lookup and prevented a requested search from reaching its selected
provider. An actual isolated Mac reproduction confirms the direct disk/fresh-memo
error and the registered search error before any provider invocation; a different
healthy query still succeeds with its fixed provider response.

The existing disk lookup exception tuple now includes only `OverflowError` in
addition to its previous errors. Bad metadata becomes an ordinary miss. Direct
lookup keeps its bytes unchanged; a successful normal provider response can replace
that entry through the existing store path. No migration, deletion, new key, numeric
cap, retry or paid fallback is added. Provider invocation stays outside the cache
catch. Existing profile/config/provider/query/bucket boundaries, TTL, flight locks,
read checks, byte/count/reserve limits, slicing and valid-hit behavior remain.

Native baseline: 47 passes across disk-sharing and result-cache tests. Six of
sixteen added cases fail on the original: both signs in actual disk reads and
registered success/error paths. Ten new and four existing controls pass. Both signs use `10**400`
(401 decimal digits), within the parser's digit limit. New controls retain fresh,
exact-TTL-boundary, expired, future, missing/null/malformed and nonfinite timestamp
behavior. Direct/fresh-memo misses leave all seeded cache bytes unchanged while a
healthy different key still hits.

Registered dispatch uses actual cache files, private profile paths, native memo/
flight/store/bucket/slice behavior and a fixed selected-provider boundary. Successful
recovery calls it exactly once with bucket 10, returns the requested three results,
stores a finite timestamp/full ten-result response, and serves five results to a
fresh memo on a normalized repeat without another invocation. Under an explicitly
rescue-disabled fixture config, the provider's error remains its error; the bad
entry remains unchanged. No keyless request or managed paid fallback is performed.
Unrelated bytes and configuration remain exact. This is fixture behavior, not
provider authorization, live search, a workload hit rate or billed-call savings.

The final six-file selection passes 89 cases, including after export/reapplication
(5.7 seconds), and covers disk sharing, result cache, flight lifetime,
RAM budget, store contention and derived-cache pressure. Existing four-process
sharing, different-profile isolation, caller mutation, busy-flight refusal and
storage-pressure controls remain. Python runs use private HOME/HERMES_HOME/TMPDIR,
one worker, no file retries and the unchanged scoped audit guard. OS/native-extension
containment and live service/model/UI use remain unverified. Installation/adoption
and Linux/workload validation are separate; owner controls remain untouched.


## Overflowing TTL configuration (v0.8.76)

The shared web-cache TTL reader now catches `OverflowError` alongside its existing
conversion errors. A JSON/YAML integer such as `10**400` or its negative survives
normal config loading but cannot convert to a Python float. Previously, a cold search with caching enabled
failed before reaching its selected provider, and otherwise usable stored
extraction entries could fail during their TTL check. Both signs now use the
established20-minute invalid-conversion default.

This is an exception-tuple-only change. It does not rewrite config, introduce a
numeric limit, sign-clamp the original integer, or alter normal TTL policy. A
representable high value still clamps to1440 minutes; low values still clamp to
one minute. Infinity/numeric strings retain their original conversion/clamp
behavior, including a string such as `1e400`. Null, bad strings/types, booleans,
fractional values and the existing NaN behavior remain. Defaulting a conversion
failure is distinct from clamping a value that converted successfully.

Two invariant tests add24 cases to the existing disk-sharing file before product
edit. Each fixture writes a real synthetic `config.yaml` and verifies the raw
value through both native config readers; no replacement TTL/config getter can
hide the failure. Signed direct TTL cases and four enabled actual registry cases
fail on the original (six failures/38 passes), while fourteen other config controls,
four cache-disabled controls and all20 previous cases pass. Source config bytes
remain unchanged. Native config loading can create its ordinary synthetic
last-known-good backup inside the isolated home; no owner config is involved.

Controlled wall and monotonic clocks plus aligned derived-file mtimes verify
memory memo, a separate memo's disk reuse, and extraction hits just before and
exactly at expiry. Read/expiry operations preserve seeded cache bytes. Actual
registry search uses the configured fixture backend, normal provider selection,
fixed provider responses and the original managed-fallback policy; keyless rescue
is disabled and trapped. Success/error/repeat counts, returned provider errors,
healthy-query isolation and `cache_enabled=False` retain their expected behavior.
No external provider, model or network request runs.

The baseline has102 passes/five files. After exported reverse/base/reapplication,
all126 cases in those complete files pass in6.9s, zero failures/skips/retries/
exclusions: result43,sharing44,metadata18,eviction11,batch10. A separate native
post-reapplication probe reads both signed real configs, returns1200 seconds and
preserves their bytes; imported runtime path/hash matches the exported manifest.

No performance, workload cache-hit-rate, billed saving, full native suite, live
provider or application result is claimed. Cache keys, clocks, byte/count/reserve
limits, locks, profiles, safety/authorization, selected provider and fallback
rules remain unchanged. This restores the normal requested provider path where
config conversion previously aborted; it does not add retries or another provider.
Tests use private homes and borrowed read-only PM-selected Mac Python3.14.9/deps.
Current read-only owner comparison is972/1004 matching targets,32 pending normal
lead adoption and Linux validation. Owner state and controls remain untouched.
