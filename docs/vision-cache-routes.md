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
