# Evidence-based cache miss attribution

The optional four-path unit in `patches/stable-cache-evidence/manifest.json`
targets upstream v0.22.5 at the exact commit in that manifest. It changes one
runtime classifier, its native integration test, one regression file and the
upstream metric documentation. It does not change requests, prompt prefixes,
provider retention, account selection, reasoning effort, quotas or fallbacks.

## The defect

After a warm cache read followed by zero cached tokens on the same route,
upstream efficiency metrics inferred `cache_expired` from a 300-second idle gap.
That interval does not prove expiry: a provider can use another retention period,
evict an entry, or miss for another reason. The classifier has no evidence that
separates these causes.

Unexplained warm-to-cold transitions now remain `provider_reported_miss`, including
after long gaps. Existing compression, model-switch, toolset-change and prompt
rebuild attribution remains intact. First reads, cross-route transitions and
cache hits keep their existing handling. Historical `cache_expired` records and
the accepted metric vocabulary remain readable; historical records are not
rewritten. Collection and sending consent are unchanged.

This does not guarantee any cache lifetime or establish that two bots share a
provider-side cache. It fixes causal reporting, not the hit rate or token bill.

## Prepare a separate source checkout

Run from the Legion repository root. Use a new directory outside the live
installation; the verifier refuses unrelated changes and mismatched base bytes.
This standalone unit is not a cumulative UI kit or an in-place upgrade of another
patch pack. Do not stack full patches or reverse unrelated owner changes. A
custom composite installation needs its own reviewed manifest and native update
custody.

```sh
set -eu
export LEGION_ROOT="$(pwd)"
export HERMES_CHECKOUT="/absolute/path/to/new-hermes-cache-checkout"
legion_manifest="$LEGION_ROOT/patches/stable-cache-evidence/manifest.json"
legion_patch="$LEGION_ROOT/patches/stable-cache-evidence/0001-cache-miss-evidence.patch"
legion_base_commit="$(python3 -c 'import json; print(json.load(open("patches/stable-cache-evidence/manifest.json"))["upstream_commit"])')"
test ! -e "$HERMES_CHECKOUT"
git clone --depth 1 --branch v0.22.5 --no-checkout https://github.com/NousResearch/hermes-agent.git "$HERMES_CHECKOUT"
git -C "$HERMES_CHECKOUT" checkout --detach "$legion_base_commit"
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase base --manifest "$legion_manifest"
git -C "$HERMES_CHECKOUT" apply --check "$legion_patch"
git -C "$HERMES_CHECKOUT" apply "$legion_patch"
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase installed --manifest "$legion_manifest"
```

Use the matching upstream package-manager test environment and
`scripts/run_tests.sh` for `tests/hermes_cli/test_cache_miss_evidence.py`,
`tests/hermes_cli/test_shared_metrics_efficiency.py`,
`tests/hermes_cli/test_relay_shared_metrics_runtime.py` and
`tests/hermes_cli/test_relay_shared_metrics.py`. Do not install dependencies with
raw pip or uv. Follow [test and adopt](installation-and-rollback.md#test-and-adopt)
for native idle-only adoption. This Python-only repair requires no renderer
rebuild. Already-running backends retain imported code until a safe native reload.
Do not restart a working session just to produce an activation receipt.

Rollback only the unused matching trial checkout:

```sh
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase installed --manifest "$legion_manifest"
git -C "$HERMES_CHECKOUT" apply --reverse --check "$legion_patch"
git -C "$HERMES_CHECKOUT" apply --reverse "$legion_patch"
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase base --manifest "$legion_manifest"
```

## Verification boundary

The long-idle regressions and native relay-storage expectation failed before the
repair. Four native files passed 172 cases with zero retries on the local custom
source; the same focused suite passed on the separately prepared clean public
base. These overlapping runs are not added together. Apply, reverse, base
verification and reapply matched all four manifest paths.

Linux and ARM64 macOS production-interpreter checks confirmed the two long-idle
behaviors after scoped source installation. The idle Linux Gateway was reloaded
through native control. No original macOS Gateway or user session was started for
proof. Original configurations, auth, holds and quotas remained unchanged. No
provider request was made. This is not all-platform acceptance, proof that old
sessions adopted every policy, or a measured usage/cache/performance saving.
