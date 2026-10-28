# macOS: isolated source installation and update

This guide starts from an **existing, working native Hermes installation**. It is not a bootstrap installer for a blank Mac. The companion tools need Python 3.9 or newer and Git; native Hermes needs its own upstream-managed interpreter and dependencies. The accepted pilot used Apple Silicon, macOS 27, the system Python 3.9 for companion tools, and an existing Python 3.13 for Hermes. No provider authentication, quota change or model request was used.

## Choose the patch base first

The numbered source-apply walkthrough below uses the historical cumulative
patch. The optional role-workflow unit uses a different upstream base:

| Patch | Required upstream | Preparation instructions |
| --- | --- | --- |
| Cumulative kit | v0.22.2, pinned in `patches/manifest.json` | Sections 1–4 below |
| Role-specific THINK/ACTION | v0.22.5, pinned in `patches/stable-role-workflows/manifest.json` | [Fresh role-workflow checkout](stable-role-workflows.md#apply-to-a-fresh-isolated-checkout) |

Choose one full patch for a fresh matching checkout. Do not apply the cumulative
patch to v0.22.5, stack it with the role unit, or reuse the old Python 3.13 pilot
interpreter as evidence that a new upstream environment is compatible. Prepare
the matching frozen environment through native Hermes PM, preserving the
installation's existing extras and plugin selection. CLI, Desktop and adoption
checks below remain separate requirements for either route.

The pilot applied public releases **v0.6.43 and v0.6.44** to separate clean checkouts, launched each CLI, and reopened the same synthetic session/search database after switching versions. That proves source installation and fixture continuity. It does not prove authentication, a real bot loop or production migration. **Use v0.6.45 or newer for the repaired Python 3.13 Desktop startup:** the subsequent native Desktop test found a missing `Path` import in the earlier backend. Read the [verification record](verification.md) for the repair and Desktop acceptance limits.

## 1. Select an existing runtime and a fresh trial directory

Keep the original source, application bundle and private home intact. Quit nothing and copy no credentials or history. Replace the two runtime paths below with your existing installation's paths, not a newly selected system Python.

```sh
set -eu
export HERMES_EXISTING_SOURCE="$HOME/.hermes/hermes-agent"
export HERMES_NATIVE_PYTHON="$HERMES_EXISTING_SOURCE/venv/bin/python"
export LEGION_TRIAL="$HOME/HermesLegionTrial"
test -d "$HERMES_EXISTING_SOURCE/.git"
test -x "$HERMES_NATIVE_PYTHON"
test ! -e "$LEGION_TRIAL"
umask 077
mkdir "$LEGION_TRIAL"
mkdir "$LEGION_TRIAL/runtime-home"
```

Use a physical output parent. On macOS, temporary paths spelled through `/var` can resolve under `/private/var`; the setup exporter intentionally refuses linked ancestors. Resolve your chosen parent before creating a new output directory. Do not relax the symlink guard or reuse an incomplete output.

## 2. Prepare one version beside the original

Start in an already downloaded Legion release, whose inventory you have verified. Use the [installation guide](installation-and-rollback.md) for a public upstream clone. When the exact base objects already exist locally, this alternative avoids another network transfer:

```sh
export LEGION_ROOT="$(pwd -P)"
python3 "$LEGION_ROOT/scripts/verify_release.py"
export HERMES_CHECKOUT="$LEGION_TRIAL/source-first"
legion_base_commit="$(python3 -c 'import json; print(json.load(open("patches/manifest.json"))["upstream_commit"])')"
test ! -e "$HERMES_CHECKOUT"
GIT_NO_LAZY_FETCH=1 GIT_OPTIONAL_LOCKS=0 git -c core.hooksPath=/dev/null -c maintenance.auto=false clone --shared --no-checkout "$HERMES_EXISTING_SOURCE" "$HERMES_CHECKOUT"
GIT_NO_LAZY_FETCH=1 GIT_OPTIONAL_LOCKS=0 git -C "$HERMES_CHECKOUT" -c core.hooksPath=/dev/null -c core.autocrlf=false -c gc.auto=0 checkout --detach "$legion_base_commit"
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase base
git -C "$HERMES_CHECKOUT" apply --check "$LEGION_ROOT/patches/0001-legion.patch"
git -C "$HERMES_CHECKOUT" apply "$LEGION_ROOT/patches/0001-legion.patch"
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase installed
```

A shared clone borrows the original Git object store. Keep that store available and do not prune it while the trial depends on it. This is an experiment-space saving, not an independent backup. Missing objects, a different base or changed files must stop preparation; do not force a checkout, fetch implicitly or patch the running installation.

## 3. Check the native CLI without private state

The following child receives no inherited token variables. Its home is the fresh trial home, and its source and interpreter are explicit. `--version` checks native startup, not provider access. Lazy dependency installation is disabled; if prerequisites are missing, stop and use the upstream package manager separately.

```sh
env -i PATH=/usr/bin:/bin:/usr/sbin:/sbin \
  HOME="$LEGION_TRIAL/runtime-home" \
  HERMES_HOME="$LEGION_TRIAL/runtime-home/.hermes" \
  PYTHONPATH="$HERMES_CHECKOUT" PYTHONDONTWRITEBYTECODE=1 \
  HERMES_DISABLE_LAZY_INSTALLS=1 GIT_NO_LAZY_FETCH=1 GIT_OPTIONAL_LOCKS=0 \
  LANG=en_US.UTF-8 \
  "$HERMES_NATIVE_PYTHON" -B -m hermes_cli.main --version
```

The reported Hermes/upstream version is **not** the Legion release identifier. Keep the release inventory, applied-source manifest and loaded module path as the source identity evidence. In the pilot, an additional Python audit hook denied network and optional installer/tool subprocesses; a single synthetic SessionDB row and search result were verified before and after the update. No real conversation was read or copied.

## 4. Test an update without overwriting the old version

Download and verify the next Legion release into another directory. Repeat step 2 with its `LEGION_ROOT` and a **new** `HERMES_CHECKOUT`, such as `$LEGION_TRIAL/source-next`. Repeat step 3 with the same trial home and the newly selected source. Keep both source directories. The pilot selected versioned source directories between separate CLI processes; it did not modify code in a running process.

Use only synthetic fixture data for compatibility testing. Do not open the same SQLite database concurrently in old and new trials. Retaining a fixture is not enough to prove compatibility with every existing production database or future schema change. A source rollback must never restore an old live database or rewind notification receipts.

## 5. Keep Desktop activation separate

Passing the CLI checks does not rebuild an installed `.app`. Desktop needs native Apple Silicon/Intel dependencies, a build of the patched renderer/main/preload and the normal platform packaging lifecycle. A Linux build or a copied renderer alone is insufficient.

For a trial, use a distinct application directory and isolated user-data/home. Inspect build input receipts and lockfiles before reusing prepared dependencies. The native build pipeline can consume admitted cached inputs; it must not silently download missing suppliers or change an existing environment. A successful local package is not Apple notarization or a public signed distribution. Never overwrite the original application, change its credentials, force-quit work or unlock the screen merely to finish a test.

The pilot reused APFS copy-on-write copies of existing workspace dependencies and prepared native/packager inputs. Both dependency lockfiles and the native/packaging recipe identities matched before admitting the copied inputs in the trial. It did not copy an existing `dist`, provider configuration or user home. This is narrower than a fresh dependency installation; do not just copy a receipt to another source path or mark unknown inputs current.

After preparing dependencies and admitting receipts **for the trial source**, these are the native build/package entrypoints used. Choose an existing supported Node executable and a fresh package output; the prepared packager path below targets Apple Silicon. An Intel Mac requires its own `darwin-x64` inputs. Every build child has external networking denied here.

```sh
export HERMES_NODE="$(command -v node)"
test -x "$HERMES_NODE"
export LEGION_MAC_OUTPUT="$LEGION_TRIAL/desktop-package"
test ! -e "$LEGION_MAC_OUTPUT"
mkdir "$LEGION_TRIAL/build-home" "$LEGION_TRIAL/build-tmp"
cd "$HERMES_CHECKOUT/apps/desktop"
legion_mac_build() {
  env -i PATH=/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin \
    HOME="$LEGION_TRIAL/build-home" TMPDIR="$LEGION_TRIAL/build-tmp" \
    NODE_OPTIONS=--max-old-space-size=4096 CSC_IDENTITY_AUTO_DISCOVERY=false \
    GIT_NO_LAZY_FETCH=1 GIT_OPTIONAL_LOCKS=0 \
    ELECTRON_SKIP_BINARY_DOWNLOAD=1 npm_config_offline=true \
    HERMES_DISABLE_LAZY_INSTALLS=1 \
    sandbox-exec -p '(version 1)(allow default)(deny network*)' "$HERMES_NODE" "$@"
}
legion_mac_build scripts/build.mjs
legion_mac_build scripts/run-electron-builder.mjs \
  --prepared build/packager/darwin-arm64/prepared.json \
  --native-deps build/native-deps --dir --mac --arm64 --publish never \
  "-c.directories.output=$LEGION_MAC_OUTPUT"
```

The child environment excludes inherited provider and Apple credentials. The renderer used a 4 GiB Node heap ceiling; the upstream packaging wrapper sets its own larger ceiling. Neither ceiling is a measured RSS result or a limit on Hermes workers.

Disabling certificate discovery can leave an unsigned bundle. In the pilot, the initial package completed but failed `codesign --verify --deep --strict`; packaging exit zero was insufficient. A **separate copied trial package** was sealed using the already installed `@electron/osx-sign` library, ad-hoc identity `-`, native main/inherited entitlement files, no timestamp, and disabled automatic entitlement/provisioning-profile changes. Its strict signature check passed. This uses no Apple account and is not notarization. Do not pass `-c.mac.identity=-` to this pinned electron-builder 27: that obsolete field is rejected by its schema. Do not change the native signing configuration or use a real certificate as a workaround.

For that **local-only** signing check, after the build/package commands succeed:

```sh
export LEGION_MAC_SIGNED="$LEGION_TRIAL/desktop-package-signed"
test ! -e "$LEGION_MAC_SIGNED"
/bin/cp -cR "$LEGION_MAC_OUTPUT" "$LEGION_MAC_SIGNED"
export LEGION_MAC_APP="$LEGION_MAC_SIGNED/mac-arm64/Hermes.app"
env -i PATH=/usr/bin:/bin:/usr/sbin:/sbin \
  HOME="$LEGION_TRIAL/build-home" TMPDIR="$LEGION_TRIAL/build-tmp" \
  sandbox-exec -p '(version 1)(allow default)(deny network*)' \
  "$HERMES_NODE" --input-type=module - "$HERMES_CHECKOUT" "$LEGION_MAC_APP" <<'JS'
import path from 'node:path';
import {createRequire} from 'node:module';
import {pathToFileURL} from 'node:url';
const [source, app] = process.argv.slice(2);
const require = createRequire(path.join(source, 'apps/desktop/package.json'));
const {sign} = await import(pathToFileURL(require.resolve('@electron/osx-sign')));
await sign({
  app, platform: 'darwin', identity: '-', identityValidation: false,
  preAutoEntitlements: false, preEmbedProvisioningProfile: false,
  strictVerify: true, batchCodesignCalls: false,
  optionsForFile(file) {
    return {
      timestamp: 'none', hardenedRuntime: true,
      entitlements: path.join(source, 'apps/desktop/electron',
        file === app ? 'entitlements.mac.plist' : 'entitlements.mac.inherit.plist')
    };
  }
});
JS
/usr/bin/codesign --verify --deep --strict "$LEGION_MAC_APP"
```

Keep this application in the trial directory. This command does not launch it or configure which source/private home a future GUI launch will use. Do not double-click it as a shortcut around the isolated-home/runtime selection checks.

After the backend import repair, two native Electron interaction tests passed on the Mac: answer cards fit beside an open artifact in a narrow chat tile, and the freshly packaged app cold-restored a synthetic older session absent from the first history page. Local mock-provider requests remained zero. Tests used an isolated home and a network sandbox that permitted loopback/Unix IPC but denied external networking. An earlier guard that also blocked Chromium's local singleton socket was a harness error, not evidence that a real owner instance should be terminated. These two checks are not a full Mac UI audit, signed distribution or production-app migration.

Adopt only after the [deployment acceptance checklist](acceptance-checklist.md) passes in the intended environment. Keep the exact previous source/package until the new version has been accepted, then retire only explicitly owned trial outputs. See [storage and backups](storage-and-backups.md) for retention boundaries.

For template-only preparation on macOS, the [offline setup recipe](offline-setup-tools.md) was also exercised: the bundle was written to a fresh physical path and doctor returned `offline_ready: true`, with `runtime_ready: unknown`. It generated no native credentials or live profile configuration.

## Later ARM64 deployment checkpoint

A later native deployment used the v0.22.5 base and its own PM-selected Python
3.14.9 environment, retaining the existing extras. The source and application
were switched while idle; the previous source and application were retained by
rename, and only small launcher/control files needed additional backup copies.
No live database was restored. The normal CLI then reported the new source and
interpreter.

The installed `.app` passed strict recursive signature verification after
local ad-hoc signing with the existing entitlement files. That same installed
application, using isolated user data and a loopback mock catalog, passed role,
model and effort Save/reopen; reciprocal THINK/ACTION linking; compact-window
Save hit testing and Cancel; and Work/Bots/Hub/Chat navigation. No inference
request was made. Two intentionally blocked external resources, an optional
font and the plugin catalog, were recorded explicitly.

This deployment also carried local customizations outside the public role unit.
It is not a clean-base Mac certification of every public patch, a complete UI
audit, provider/account acceptance, notarization, or proof that the owner's
original sessions adopted new rules. The original data-home Gateway was not
started for the test. Do not start a held fleet, resume a conversation or send a
model request merely to turn an installed-code check into an adoption claim.

For production adoption, use an independent source checkout. A shared clone from
section 2 still depends on the old object-store path; renaming or pruning that
store can break it. Retire trial environments only after checking that current
interpreters, launchers, prepared inputs and live processes do not borrow them.
