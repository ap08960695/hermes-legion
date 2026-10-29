# Retain owner settings after config metadata failures

The effective user-config loader already recovers the last-good raw user layer
when opening or parsing YAML fails. A signature read occurs before that recovery
block. If `stat()` raised PermissionError or another OSError, the exception escaped;
the Gateway's generic fail-open wrapper then returned an empty mapping. A local
session's owner-cost scope could replace its stored effort ceiling with that empty
mapping, allowing a requested `max` onto the final request despite the previous
owner limit being `high`.

Signature I/O failures now use the same native last-good recovery path as file-open
and parse failures. Recovery uses the existing in-process raw mapping first, then
the existing native good-config backup. The raw layer still passes through the
normal environment expansion, managed overlay and model-key normalization. No new
backup, cache, registry, timer or setting is introduced. A recovered result is not
cached under a failed signature. Strict `fail_closed=True` callers still receive
the original metadata error. The normal signature/cache-hit path is unchanged.

A genuinely absent user file retains the existing empty-user-layer/managed-only
contract. Explicitly removing a limit in a valid config still removes it; lower
requested effort is not raised, and another model retains its own effort. Frozen
worker snapshots remain isolated from profile files. When no last-good mapping or
backup exists, the pre-existing warned-default fallback remains; this change does
not invent a cost policy for an unknown configuration.

## Verification

Before the fix, eight offline cases failed: four effective-reader cases (warm or
cold with a native good backup; PermissionError or OSError) and four real native
local-session cases (frozen or following), whose final request contained `max`
instead of the configured `high`. The missing-file control passed. The first
Gateway fixture accidentally had no local-adapter resolver and therefore did not
reach the intended config read; it was corrected and fault reach was asserted
before counting the Gateway cases as a product failure.

The final regression selection covers config loaders/caches/writers, reasoning
wire limits, frozen workers and additional authority/session callers:
163 files / 1,110 passed / 0 failed / 4 skips,
zero file retries. Code-health is clear. Earlier focused and historical counts
overlap and are not added to this result or treated as a whole-project green.

Installed Linux and macOS each pass thirteen production-interpreter controls with
private synthetic data and network denied. These include warm/cold native backup
recovery, strict refusal, managed-only absence, profile isolation, native SQLite
SessionAuthority final-wire clamping during faults, unchanged model/prompt/input/
tools, lower efforts, other models, and valid limit removal/reinstatement. The
original macOS Gateway is not started for proof; no Desktop bundle is rebuilt.

No model, account, quota, paid fallback, dependency or original user database is
changed. This prevents the demonstrated metadata-failure route from silently
losing known effort limits. It is not a measured dollar/token/RAM saving, a provider
cache-hit improvement, or proof of adoption by an original user conversation.
