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
