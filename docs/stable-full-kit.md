# Consolidated stable source and Desktop kit

This is the complete **699-path** Legion source, interface and optimization alternative
for upstream Hermes **v0.22.5**, commit
`bf0203a794a07aac3ff764972ab9087baa4e4f4e`. It replaces the need to assemble the
historical cumulative kit and the smaller stable units. It is not an upstream release,
an account installer, a prebuilt application or an in-place migration script.

The [manifest](../patches/stable-full/manifest.json) pins every before/after file hash.
The [test selection](../patches/stable-full/test-selection.json) records the offline
Python and Desktop selection. No dependency or lockfile change is included.

## Included behavior

- Focus navigation, saved-chat history, always-visible device/profile context, bot
  configuration, Hub collections, native file previews, rich Markdown and Workflow.
- Role-specific THINK/ACTION plans, independent review, bounded handoffs, idempotent
  card creation, ready-work dispatch and native terminal-stop behavior.
- Bounded file and history reads, structured/CJK recall, compaction publication and
  recovery, prompt-prefix reuse, cache cohorts and privacy-preserving usage attribution.
- Profile/account-scoped metadata caches, process/cache diagnostics, derived-cache
  retention, protected active scratch work and update-preservation recovery.
- Optional per-model reasoning effort ceilings after explicit overrides, including owner-bound frozen sessions and auxiliary requests. See the [effort-limit guide](reasoning-effort-limits.md).
- Existing transport, owner/claim, review, data-clearance, quota and emergency-stop gates.

No account grants, conversations, live boards, operator profiles or production data
are bundled. Legacy technical profile identifiers remain where the native compatibility
or owner gate requires them; these are not imported personas or grants to impersonate
that owner. The English role templates are separate reference material.

## Prepare a new isolated checkout

Run from the Legion repository root. Choose an unused destination outside the running
installation. The source download is public and makes no model request.

```sh
set -eu
export LEGION_ROOT="$(pwd)"
export HERMES_CHECKOUT="/absolute/path/to/new-hermes-stable-checkout"
legion_manifest="$LEGION_ROOT/patches/stable-full/manifest.json"
legion_patch="$LEGION_ROOT/patches/stable-full/0001-stable-full.patch"
legion_base_commit="$(python3 -c 'import json; print(json.load(open("patches/stable-full/manifest.json"))["upstream_commit"])')"
test ! -e "$HERMES_CHECKOUT"
git clone --depth 1 --branch v0.22.5 --no-checkout https://github.com/NousResearch/hermes-agent.git "$HERMES_CHECKOUT"
git -C "$HERMES_CHECKOUT" checkout --detach "$legion_base_commit"
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase base --manifest "$legion_manifest"
git -C "$HERMES_CHECKOUT" apply --check "$legion_patch"
git -C "$HERMES_CHECKOUT" apply "$legion_patch"
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase installed --manifest "$legion_manifest"
```

A moved release tag, different source, unrelated edits or pre-existing added target
must refuse. Do not force, fuzz, reset another person's work or stack full alternatives.
The patch has one line of context; exact before hashes and the pinned commit remain
mandatory. Native Git attributes preserve the PowerShell checkout's CRLF exception.

Use upstream's native package manager and matching frozen dependency groups. Do not
repair an environment with raw pip/uv or substitute a different Python/Node runtime.
Follow [test and adopt](installation-and-rollback.md#test-and-adopt) and the
[Mac guide](macos-install-update.md). Source application does not rebuild or reload an
already running Desktop or Gateway.

## Reproduce the offline selection

After preparing the existing upstream frozen test environment, run the Python selection
through the native runner, from the patched checkout. This example only forwards the
recorded paths; it does not install dependencies or call a model.

```sh
cd "$HERMES_CHECKOUT"
python3 - <<'PY'
import json, os, pathlib, subprocess
selection = pathlib.Path(os.environ["LEGION_ROOT"]) / "patches/stable-full/test-selection.json"
files = json.loads(selection.read_text())["python_test_files"]
env = {**os.environ, "HERMES_TEST_FILE_RETRIES": "0", "HERMES_TEST_WORKERS": "2"}
raise SystemExit(subprocess.call(["scripts/run_tests.sh", *files], env=env))
PY
```

For Desktop, use the same selection's `desktop_test_files` relative to `apps/desktop`
with the existing Vitest runner, then run the full native TypeScript check and Desktop
build. Test and packaging tools must already be admitted by the native package manager.
Do not use a running user's renderer or provider account as a test fixture.

## First-use interface checks

1. Open **All features → Plugins**. The bundled Desktop **Kanban** plugin is intentionally
   off by default upstream. Enable that plugin explicitly if you want Work to show the
   board and Workflow. This is a Desktop presentation opt-in, not permission to start
   the dispatcher or release an emergency stop. Without it, Work shows native agent activity.
2. In **Bots → Edit profile**, save the role, family, mode, counterpart and eligible model
   and effort. Reopen to verify persistence. Configure both sides for a reciprocal pair;
   one-way pairing is displayed honestly and is not a ready execution lane.
3. In **Work → Workflow**, select a downstream card, inspect its actual upstream links
   and recorded bot journey, then open the original card if needed. A dependency edge
   does not prove execution or completion; absent run evidence stays absent.
4. In **Hub**, create a collection, choose its members explicitly and save a page or
   import a file. Chat files stay private until shared. Removal uses recoverable trash.
5. In **History**, open a retained conversation and verify its content. Opening history
   is separate from submitting a prompt or resuming a goal.

Test within a separate synthetic home first. After acceptance, adopt the rebuilt native
application only at idle, preserving drafts, sessions and worker ownership. An updater
refusal is a gate to diagnose, not permission to bypass custody or authentication.

## Evidence and limits

The broad offline run completed 218 Python files: **2,737 passed, 13 skipped, zero
failures**, with two workers and zero file retries. Desktop completed **60 files,
383 passing tests**; full TypeScript and the native Linux renderer/main build passed.
After two synthetic scanner fixtures were clarified, their two files were separately
rerun: **33 passed**. Those cases overlap the broad selection and must not be added to it.

Native clean-base apply, installed-byte verification, reverse and reapply passed for
all 667 paths on **Linux and macOS**. These are source compatibility results, not a
claim that the entire Python/UI suite ran on macOS. Linux rendered checks use the fresh
built source-mode Electron application and its actual backend in a separate synthetic
home, with only localhost model metadata and zero inference. The 11 interaction checkpoints include explicit Kanban opt-in, upstream-card navigation,
Hub collection/page saves and retained-message reopening. Two blocked external catalog
requests produced expected DNS errors under the network-denied fixture; this is not
a claim of universally clean network logs. These checks do not certify a downloaded
packaged application, original stored sessions or every UI feature.

The suite initially exposed stale test interfaces after upstream's facade changes.
Fixtures were reconciled against the native owner-policy and bounded-read contracts;
no production permission or completion rule was weakened to satisfy them. Test-only
synthetic identifiers are not production receipts.

Matching cache keys/prefixes provide comparison evidence, not a guarantee of shared
provider cache. Idle time alone does not establish cache expiry. No universal cost,
quota, RAM, disk or latency improvement is claimed from offline tests. Use existing
real workload diagnostics before making those claims.

Model defaults are not hard effort ceilings. In particular, a Terra `high` profile can
still be overridden explicitly by a task or saved session. This kit does not silently
clamp such an override, increase a quota, introduce paid fallback, or declare a provider
ready from its family label. Preserve native limits and diagnose unsupported routes.

## Roll back an unused matching checkout

```sh
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase installed --manifest "$legion_manifest"
git -C "$HERMES_CHECKOUT" apply --reverse --check "$legion_patch"
git -C "$HERMES_CHECKOUT" apply --reverse "$legion_patch"
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase base --manifest "$legion_manifest"
```

This source reversal is not a live database restore. Keep the compact source/application
rollback until original-session acceptance; retire only owned, inactive staging after
its evidence is durable. Do not keep redundant full copies merely to repeat a test.
