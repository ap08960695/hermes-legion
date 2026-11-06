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
