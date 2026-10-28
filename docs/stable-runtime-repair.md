# Stable runtime repair

This independent nine-path patch targets upstream Hermes **v0.22.5**, commit
`bf0203a794a07aac3ff764972ab9087baa4e4f4e`. It includes the
[earlier transport repair](stable-transport-repair.md) and a notification-layer fix.
Its exact [manifest](../patches/stable-runtime/manifest.json) is separate from the
historical cumulative Legion kit. It does not ship the full custom UI or
THINK/ACTION orchestration. Do not stack full patches or force through a refusal.

## What changes

The seven transport source/test paths are unchanged from v0.6.48: rotating Codex
workspace headers follow the actual bearer, and managed workers keep their frozen
provider wire mode, endpoint and credential boundaries.

Two additional frontend source/test paths keep ambient success/info confirmations
below the modal backdrop. A confirmation from a previous Save can no longer steal
clicks from a reopened dialog's Save button. Errors, warnings and notifications
with primary or secondary actions retain their over-modal surface. Dismissal,
action callbacks and bounded notification stacks remain available.

No account, quota, fallback, application process or service is configured or
restarted by the kit. Adoption still waits for idle applications and workers and
uses native update custody. The existing compatibility checks read source and Git
metadata only; they do not import Hermes, read credentials or request a model.

## New clean checkout

Start in the Legion repository root. Choose a new, nonexistent directory outside
your running installation. Fetching public source does not call a model.

```sh
set -eu
export LEGION_ROOT="$(pwd)"
export HERMES_CHECKOUT="/absolute/path/to/new-hermes-stable-checkout"
legion_manifest="$LEGION_ROOT/patches/stable-runtime/manifest.json"
legion_patch="$LEGION_ROOT/patches/stable-runtime/0001-stable-runtime.patch"
legion_base_commit="$(python3 -c 'import json; print(json.load(open("patches/stable-runtime/manifest.json"))["upstream_commit"])')"
test ! -e "$HERMES_CHECKOUT"
git clone --no-checkout https://github.com/NousResearch/hermes-agent.git "$HERMES_CHECKOUT"
git -C "$HERMES_CHECKOUT" checkout --detach "$legion_base_commit"
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase base --manifest "$legion_manifest"
git -C "$HERMES_CHECKOUT" apply --check "$legion_patch"
git -C "$HERMES_CHECKOUT" apply "$legion_patch"
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase installed --manifest "$legion_manifest"
```

## Upgrade an unchanged v0.6.48 transport installation

Use this section instead if the target already has the exact seven-path transport
patch. Run from the new Legion release root and set the existing isolated checkout
path. The first command refuses unrelated modifications. The final command verifies
all nine paths, preserving the transport changes throughout.

```sh
set -eu
export LEGION_ROOT="$(pwd)"
export HERMES_CHECKOUT="/absolute/path/to/existing-stable-transport-checkout"
legion_old_manifest="$LEGION_ROOT/patches/stable-transport/manifest.json"
legion_manifest="$LEGION_ROOT/patches/stable-runtime/manifest.json"
legion_upgrade="$LEGION_ROOT/patches/stable-runtime/0002-from-stable-transport.patch"
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase installed --manifest "$legion_old_manifest"
git -C "$HERMES_CHECKOUT" apply --check "$legion_upgrade"
git -C "$HERMES_CHECKOUT" apply "$legion_upgrade"
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase installed --manifest "$legion_manifest"
```

To reverse only this upgrade on that isolated checkout:

```sh
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase installed --manifest "$legion_manifest"
git -C "$HERMES_CHECKOUT" apply --reverse --check "$legion_upgrade"
git -C "$HERMES_CHECKOUT" apply --reverse "$legion_upgrade"
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase installed --manifest "$legion_old_manifest"
```

A fresh full-patch installation can instead reverse `legion_patch`, using installed
verification before and base verification afterward. Never rewind a database,
notification cursor, credential store or conversation as source rollback.

## Build and acceptance

Use upstream's matching, frozen package-manager environments. Run the scoped native
notification component/store tests and Desktop typecheck, then build/package via
upstream's prepared-input workflow. Do not substitute a new dependency selection
or treat a source hash check as a rebuilt application. Follow the separate
[adoption and rollback guidance](installation-and-rollback.md#test-and-adopt).
The kit does not include a prebuilt application or private rollback image.

The [verification record](verification.md#ambient-confirmations-and-stable-upgrade-v0649)
separates the clean-source checks, installed Linux package interactions, historical
transport results and untested Mac/production-workload boundaries.
