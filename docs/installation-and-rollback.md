# Installation and rollback

## Supported target

The cumulative kit supports the **exact** upstream Git revision in `patches/manifest.json`. The separate [stable runtime repair](stable-runtime-repair.md) has its own pinned base and manifest; use its instructions instead for upstream v0.22.5. Compatibility with later upstream releases, arbitrary local patches or another OS is not assumed. The verification helper reads files and Git metadata only; it does not import Hermes or run a model.

For an existing Mac installation, see the [isolated macOS installation and update guide](macos-install-update.md). It distinguishes native CLI checks from Desktop packaging and activation.

## Apply to a separate clean checkout

Keep your running installation untouched. Start in the Legion repository root, choose a **new, nonexistent** checkout directory and obtain the exact public base revision. The clone requires network access but does not authenticate a provider or call a model. These are ordinary shell variables, not credentials.

```sh
set -eu
export LEGION_ROOT="$(pwd)"
# Replace this with a NEW directory outside your running installation:
export HERMES_CHECKOUT="/absolute/path/to/new-hermes-legion-checkout"
legion_base_commit="$(python3 -c 'import json; print(json.load(open("patches/manifest.json"))["upstream_commit"])')"
test ! -e "$HERMES_CHECKOUT"
git clone --no-checkout https://github.com/NousResearch/hermes-agent.git "$HERMES_CHECKOUT"
git -C "$HERMES_CHECKOUT" checkout --detach "$legion_base_commit"
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase base
git -C "$HERMES_CHECKOUT" apply --check "$LEGION_ROOT/patches/0001-legion.patch"
git -C "$HERMES_CHECKOUT" apply "$LEGION_ROOT/patches/0001-legion.patch"
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase installed
```

Do not use `--reject`, forced reset or conflict markers to bypass a refusal. Review differences and prepare a compatible patch instead. A dependency install is a separate upstream package-manager operation, outside this kit's verifier. Do not run a tool to initialize a live home just to check the patch.

## Test and adopt

Run relevant upstream tests through `scripts/run_tests.sh` in an isolated Hermes home and the upstream-managed test environment. Review the result and any platform skips. Tests must not touch your real accounts, services, workers, GPU jobs or private data.

Adopting the tested checkout into a live deployment is a separate operator-controlled operation. Back up the affected files, permissions, configuration and state through supported mechanisms. Wait for active workers, background processes and sessions to be safely idle; use the platform's normal lifecycle. The kit does not stop, signal or restart anything automatically. Native scheduled notifications may run after a session is reopened; do not describe that as zero model activity.

## Reverse on the isolated checkout

```sh
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase installed
git -C "$HERMES_CHECKOUT" apply --reverse --check "$LEGION_ROOT/patches/0001-legion.patch"
git -C "$HERMES_CHECKOUT" apply --reverse "$LEGION_ROOT/patches/0001-legion.patch"
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase base
```

Stop if source changed after installation. Never restore an old live database, rewind notification cursors or delete receipts as a rollback shortcut.

## Startup checker cache

A source launch first checks whether its application dependencies are current. If a shared PM cache selects a checker for a different launcher runtime scope, the checker can appear unavailable even while a compatible, published generation remains in the cache. That false negative can send a current installation through dependency/source completion again.

The cumulative patch preserves a healthy selected checker as the first choice. Otherwise it reads immediate published generations, matches the PM project/lock and interpreter identity, validates the existing interpreter's PM imports, and takes the normal child lease under the preparation lock. It reuses that generation without rewriting `selected.json`, selecting a different application environment or staging dependencies. Symlinked, unpublished, malformed, mismatched or unusable alternatives are refused. If none works, the existing no-bootstrap refusal or explicit preparation behavior still applies.

The installed native read-only check changed from false to true on one current installation, using the preexisting matching checker. Dependency facts, lockfiles and both selections stayed unchanged. No new PM generation, dependency preparation, model request or additional Desktop launch was used for acceptance. Native lock/temporary lease metadata is still expected. This demonstrates the repaired check, not an end-to-end startup speedup; measure the next normal launch separately.
