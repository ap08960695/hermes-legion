# Installation and rollback

## Supported target

This first release supports the **exact** upstream Git revision in `patches/manifest.json`. Compatibility with later upstream releases, arbitrary local patches or another OS is not assumed. The verification helper reads files and Git metadata only; it does not import Hermes or run a model.

## Apply to a separate clean checkout

Keep your running installation untouched. Prepare a new checkout of upstream Hermes and check out the pinned revision. Set `LEGION_ROOT` and `HERMES_CHECKOUT` to your two directories. These are ordinary shell variables, not credentials.

```sh
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
