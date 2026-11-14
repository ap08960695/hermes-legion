# Vision cache connection boundaries

Auxiliary image analysis has two reuse layers: a request cache for a caller's local
file and a content cache for the prepared image. The content cache omitted the main
connection's endpoint, API mode and authentication mode; the request cache omitted
those values when they came from saved model settings. With the same image, prompt,
provider and model, changing a connection could therefore return the old analysis.

Both layers now use the existing read-only main-field lookup for `base_url`,
`api_mode` and `auth_mode`. Context-local values take precedence over the saved
`model` section. This reads metadata without resolving a provider client or acquiring
credentials. Existing profile/caller boundaries, TTLs, capacities, image processing,
provider selection and prompt history remain unchanged. A required lint correction
uses equivalent `removeprefix` handling for local `file://` input.

## Evidence

Thirteen of fourteen new cases fail on the original source. Twelve cover endpoint
and mode changes in live-context metadata and saved configuration through both the
direct analysis function and the registered tool handler. Two synchronize concurrent
requests to different endpoints and then repeat them; the direct path fails before
repair while the request cache already protects the registered concurrent case.

The repaired cache selection passes 32 tests across three files. A separate ten-file
vision/routing selection passes 112 tests and fails one pre-existing case:
`tests/agent/test_vision_routing.py::TestTextOnlyMainSkippedForVision::test_text_only_main_skipped_when_no_aggregator`.
That same failure reproduces with both changed production files replaced by their
original versions: the resolver returns a DeepSeek client where the test expects
none. This release does not change that resolver and does not claim the entire
vision suite is green. Scoped lint and source-health checks pass.

The actual installed source and production Python on Linux and ARM64 macOS each
pass twelve offline checks, including real image preparation, `file://` input,
read-only configuration, scoped runtime bindings, response extraction and registered
tool dispatch. Only the external LLM boundary supplies fixed SDK responses. Four
requests across route A, route B, repeated B and restored A produce the expected
route-specific answers from two fixture completions. This is reuse correctness,
not measured production usage, speed or RAM improvement.

The 915-path kit matches both installed source trees before publication. Native
apply/reverse/reapply, companion tests and release/privacy checks are separate
gates. No Desktop source changed; the previously installed v0.8.5 UI packages were
retained.

## Limits

All new execution is CPU-only and offline, with no real model call, GPU computation,
worker start, dispatch, session resume or service restart. Owner stops and settings
are preserved. Existing simple test cards remain parked; live card execution and
adoption by already-running processes are unverified. No extra production card is
created merely to repeat this offline fixture.

The tested route inputs are context-local runtime fields and the saved `model`
section. Environment-only endpoint changes without a runtime binding, provider
fallback selection, credential rotation and changes during an in-flight request
are not newly validated by this release.


## Streaming content keys (v0.8.58)

The prepared-image cache key now streams the file through `hashlib.file_digest`
instead of creating a full `read_bytes()` copy for SHA-256. The repository already
uses this stdlib pattern and requires Python 3.11 or newer. Existing metadata is
resolved before opening the file; its final identity list, JSON serialization and
key SHA stay identical. Profile, prompt, model, endpoint/mode/auth and crop inputs,
capacity/TTL, preparation, provider selection and history remain unchanged.

Five native regression cases cover no whole-file read, same-size changed valid PNG
with preserved mtime, actual stream closure on success/digest failure, and missing/
open-error fallback. Original source has two expected stream-path failures and
five passing controls; candidate and reapply pass all seven content cases. Together
with existing saved/runtime/direct/registered/concurrent route and request-cache
cases, 37 native tests pass across three files. External LLM calls use fixed
responses; native route cases retain real preparation, extraction and cache behavior.
No provider request is issued.

Actual native Mac Python 3.14.9 prepares a valid 2048×2048 synthetic uncompressed
RGB PNG. Input and prepared file are each 12,589,062 bytes. The original function
is compiled from its exact unaltered AST with the same native globals; candidate
is imported normally. Both hash the same native-prepared path/home/route/prompt.
Every key matches and prepared bytes remain unchanged. Generation, preparation,
imports and five warmups per variant precede measurement. Seven alternating
10-call timing batches run without tracing; three separate alternating 10-call
allocation batches follow GC.

| Key-path measurement | Whole-file bytes | Streamed file |
| --- | ---: | ---: |
| Median batch-average time | 4.738133 ms | 4.601042 ms |
| Batch-average time range | 4.720092–4.763554 ms | 4.576067–4.632033 ms |
| Median traced batch peak | 12,665,605 bytes | 470,798 bytes |

All three allocation peaks equal their respective medians. This is one large
synthetic prepared-image key component. It establishes no whole-service RSS,
complete vision-workload peak, startup, production cache-hit-rate or billed saving.
Image ingestion, normalization, base64 and provider processing retain their normal
cost. Linux parity, original owner-session continuation and app adoption remain
separate.


## Retained analysis byte budget (v0.8.74)

The auxiliary content cache already limited itself to 256 entries and a one-hour
TTL, but had no byte budget. The outer request cache's result-size limit does not
bound this inner cache: the inner result is stored before the outer admission
check. After each put, the content cache retains at most 32 MiB of charged key/entry payload,
alongside the existing entry count, TTL and lookup promotion.

A small local helper uses native `sys.getsizeof` for the key, timestamp, outer
entry tuple, result tuple, analysis string and optional scale-note string. The
producer's result shape remains `(analysis, scale_note)`. Shared objects can be
counted more than once, conservatively. Accounting does not encode, copy or
truncate results. Under the existing lock, each put recomputes charges over at
most 257 records (256 prior entries plus the candidate) and evicts oldest entries
until both limits hold. Equality is
admitted. An individually oversized replacement removes only the matching key;
unrelated useful hits remain. No counter, secondary size map or new cache layer
is needed.

Fresh analyses still return unchanged. When both cache layers decline a result,
a repeated request can call the provider again; fewer retained hits are an
explicit memory/reuse tradeoff. Routes, content keys, TTL, native multimodal
bypass, error handling and the outer cache remain unchanged. The budget excludes
map/lock overhead, interpreter memory, temporary provider results and concurrent
in-flight work. It is not an RSS limit or a promise about total Hermes memory.

Native Mac baseline: 68 cases across five complete files. Two new invariant tests
add twelve cases before product edit; all twelve fail meaningfully on the original
cache and all seven prior content-cache cases pass. Tests use small controlled
budgets for exact equality/one-byte denial, ASCII/Thai/non-BMP and scale notes,
byte/count LRU, replacement, expiry and concurrent puts. Direct and actual registry
dispatch keep fresh oversized analyses exact, preserve a small useful hit and the
source image, leave no pending reservation, and retain provider errors. The
registered cases also verify that outer reuse is active for the small result.
After true exported reverse/base/reapplication, all 80 cases across the same five
files pass in 8.2 s, with no failures, skips, retries or exclusions. Existing saved/
runtime route, concurrent-route, request, native-pixel and history-budget tests run.

Three alternating, separate GC/tracemalloc phases compare the original native put
function, compiled from its exact saved AST with the same unchanged globals/lock,
with the imported candidate. Both receive the same 256 distinct ASCII analyses,
each with 250,000 filler characters, plus identical keys and metadata. Surviving
result values are identical; admission intentionally retains fewer entries.

| Median fixture metric | Original | Byte-budgeted |
|---|---:|---:|
| Retained entries | 256 | 134 |
| Charged key/entry bytes | 64,081,298 | 33,542,612 |
| Traced retained allocations | 64,069,122 bytes | 33,541,294 bytes |
| Traced transient peak | 64,319,428 bytes | 34,042,341 bytes |

A separate seven alternating batches of 256 puts, with 256 small entries already
resident and tracing disabled, measure the accounting cost: median per put rises
from 0.000141 ms to 0.104933 ms. No timing assertion is added. These are synthetic
cache-component measurements, not whole-process RSS, response latency, cache-hit
rate, billed usage or production savings. All external provider calls in behavior
tests use fixed responses; the measurement makes none.

Source/runtime dependencies are borrowed read-only through PM-selected Python
3.14.9, with private synthetic homes and unchanged scoped audit negatives. No
service, Gateway, UI or real model workload is launched. Existing processes need
normal idle adoption; current read-only source comparison finds 974/1004 matching
kit targets and 30 pending normal lead adoption/Linux validation.


## Request-cache completion admission (v0.8.75)

The outer request cache previously encoded and parsed each owner's result while
holding the shared cache lock, then repeated admission for its completion log.
It now computes the existing `cacheable(result)` decision once, before taking the
lock and inside the original exception/cleanup scope. Publication and logging
consume the same decision. No policy, byte check, JSON check or cache key changes.

The owner keeps its pending reservation while admission runs. Publication and
LRU eviction remain under the lock, TTL still starts at publication, followers
still await the same future, and failures still settle that future and remove
the reservation. Existing constructor budgets, capacity fallback, cancellation,
provider behavior, native pixel bypass and the separate inner cache remain.
Admission is still synchronous: the active event loop pays its encoding/parsing
cost. Consumers on other threads/event loops can use unrelated cached entries or
reserve new work while that preparation runs; no new await or offload is added.

The original native probe observes two validations for one owner: first with the
lock held, then without it. The candidate observes one lock-free validation.
Both return the same result on a cached repeat, call the producer once and leave
no pending reservation. Two invariant tests add five cases before product edit;
all five fail meaningfully on the original, while the prior sixteen cases pass.

A controlled gate pauses only target-owner validation. Another consumer probes
the lock without blocking; a real cached hit and independent new-key completion
finish before gate release. Same-key followers remain waiting and then receive
the owner's result or the native admission error. The gate releases in `finally`.
Actual registry dispatch with a real temporary PNG/preparation/key/extraction
uses fixed external-provider responses. ASCII/Thai/non-BMP success is admitted
once and a hit adds no admission/provider call; rejected provider-error results
are evaluated once per explicitly repeated owner. Outputs, source PNG and pending
cleanup remain intact. Existing cancellation, result-size, TTL, route, inner-byte,
native-pixel and history cases run in the same complete selection.

Native baseline:80 passes/five files. After actual exported reverse/base/
reapplication:85 passes/five files, zero failures/skips/retries/exclusions,8.7s.
Counts are request21,content19,route14,native20,history11. Actual imported module
path/hash matches the exported manifest.

Seven alternating untraced timing batches compare the original exact AST-bound
async method, using the same unchanged module globals and native policy, with the
imported candidate. Each batch has64 distinct cold keys and the same200,033-byte
JSON result containing200,000 ASCII analysis characters. Separate counted batches
verify equivalent outputs,64 retained keys,64 producer calls and empty reservations.

| Component fixture metric | Original | Prepared admission |
|---|---:|---:|
| Median owner completion | 0.167342 ms | 0.084298 ms |
| Validations per64-owner counted batch | 128 | 64 |
| Producer calls per counted batch | 64 | 64 |

There is no allocation/RSS measurement or external provider call in this benchmark.
These are component timings and Python validation counts, not whole-tool response
time, physical model requests, billed usage or a production cache-hit improvement.
Tests use isolated PM-selected Mac Python3.14.9 and private synthetic homes with
unchanged scoped audit negatives. No service, Gateway, UI or real model workload
is launched. Read-only owner source comparison finds972/1004 matching targets;
32 await normal lead adoption and Linux validation.
