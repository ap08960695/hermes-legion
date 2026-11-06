# Deterministic offline vision verification

The pre-existing failure reported in v0.8.6 came from
`tests/agent/test_vision_routing.py::TestTextOnlyMainSkippedForVision::test_text_only_main_skipped_when_no_aggregator`.
The test expected a known text-only model but did not supply its catalog metadata.
In a clean offline home the lookup is unknown, and production intentionally permits
unknown models so new/custom models remain usable. That observation did not prove
a defect in the production selection policy.

The replacement `test_main_route_follows_catalog_capability` supplies raw synthetic
catalog data at the catalog-fetch boundary. The real parser and auto-route must
reject a known text-only model, accept a known vision-capable model, and preserve
the permissive unknown case. It uses a fixture model identifier and closes any
constructed client. It makes no claim about the current capabilities of a commercial
model and makes no inference request.

## Verification

The original nine-case file reproduces the one failure in a network-denied, CPU-only
home. After repair the file passes eleven cases; a three-file capability selection
passes 65 cases. A thirteen-file combined vision/cache selection passes 147 tests,
including the files which reported 112 passes and one failure in v0.8.6 plus the
cache regressions. These selections overlap and are not additive. Scoped lint,
source health and the companion suite pass.

Two temporary source overlays verify that the repaired test catches incorrect
production behavior: an always-permit gate fails the text-only case; an always-deny
gate fails vision/unknown acceptance. The overlays never replace installed code.

The updated eleven-case file also passes against the installed Linux checkout.
Actual installed source and production Python on Linux and ARM64 Mac each pass
three offline catalog/route checks for text-only, vision and unknown metadata.
These instantiate clients where permitted but never send a request. Missing-credential
warnings from the isolated fallback chain are expected. The new test file is
installed on both hosts before publication and the 916-path kit matches both.

## Scope

This is a verification repair. Production Python behavior, model/provider defaults,
configuration and Desktop packages are unchanged. It does not prove actual endpoint
image acceptance, authenticated aggregator fallback, catalog/network reliability,
original-process adoption or production resource savings. Earlier live card and
full-goal acceptance gaps remain open.

No GPU, model inference, worker start, card dispatch, session resume or service
restart is used. Owner stops are preserved; no new production test card is needed
for this test-fixture-only change.
