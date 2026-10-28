# Role-specific THINK / ACTION for stable Hermes

This optional **68-path** extension targets upstream Hermes v0.22.5, commit
`bf0203a794a07aac3ff764972ab9087baa4e4f4e`. It ships the native role lifecycle,
per-bot model/effort editor and their integration dependencies, including the
[stable runtime repairs](stable-runtime-repair.md). The
[manifest](../patches/stable-role-workflows/manifest.json) pins every input/output.
It is an alternative full patch, not a layer over another Legion full patch.
It does not install private profiles, accounts, Web adapters or a prebuilt app.

## What the feature does

A developer THINK bot plans for a developer ACTION bot; research, operations and
other roles can have their own pairs and models. There is no required global
planner/executor and no forced premium model. The Bots editor saves native model,
provider, effort and reciprocal pairing with a configuration-revision check.
Existing chats and workers retain their current bindings.

THINK completes with a validated plan on its own native task run. Captain creates
ACTION steps using `plan_task` and `plan_step`; the native run/hash/step binding is
checked at creation, claim, dispatch, execution context and terminal handoff.
Repeated identical creation reuses the same card. Plans are bounded to 16 steps
and 16 KiB; ACTION receives its selected step and shared constraints rather than
another bot's entire conversation. Independent write scopes may run together;
actual dependencies, account limits, resource locks and review gates still apply.

Independent review stays on the ACTION card. Routine changes return to ACTION;
a genuinely blocked, unusable plan can create one new THINK task with `replan_of`.
The old attempt and its evidence remain. Successful completion or review handoff
stops the worker without a follow-up inference call. A final-iteration handoff
also retains its native phase and failure budget instead of becoming a timeout.

Read the installed [native protocol](role-plan-protocol.md)
and [Captain routing guide](captain-role-routing.md) before enabling pairs.
Family labels support GPT, Claude, AGY, NIM and Web configuration; they never prove
provider access, quota, data clearance or a working execution adapter. Web routing
still needs an approved adapter and its original shared budget/controller.

## Apply to a fresh isolated checkout

Run from the Legion repository root. Select a new directory outside the running
installation. These commands fetch public source and inspect Git/files; they do
not read credentials or call a model.

```sh
set -eu
export LEGION_ROOT="$(pwd)"
export HERMES_CHECKOUT="/absolute/path/to/new-hermes-role-checkout"
legion_manifest="$LEGION_ROOT/patches/stable-role-workflows/manifest.json"
legion_patch="$LEGION_ROOT/patches/stable-role-workflows/0001-stable-role-workflows.patch"
legion_base_commit="$(python3 -c 'import json; print(json.load(open("patches/stable-role-workflows/manifest.json"))["upstream_commit"])')"
test ! -e "$HERMES_CHECKOUT"
git clone --no-checkout https://github.com/NousResearch/hermes-agent.git "$HERMES_CHECKOUT"
git -C "$HERMES_CHECKOUT" checkout --detach "$legion_base_commit"
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase base --manifest "$legion_manifest"
git -C "$HERMES_CHECKOUT" apply --check "$legion_patch"
git -C "$HERMES_CHECKOUT" apply "$legion_patch"
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase installed --manifest "$legion_manifest"
```

There is no in-place upgrader from the nine-path runtime unit in this release.
For an existing modified installation, prepare this separate checkout and use
native drain/update custody after testing. Do not reverse unrelated owner patches
or force an apply refusal. Source rollback on an unused matching checkout is:

```sh
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase installed --manifest "$legion_manifest"
git -C "$HERMES_CHECKOUT" apply --reverse --check "$legion_patch"
git -C "$HERMES_CHECKOUT" apply --reverse "$legion_patch"
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase base --manifest "$legion_manifest"
```

## Configure and adopt

Use upstream's matching frozen package-manager environments, run the native tests
and Desktop typecheck, then build/package using upstream's supported workflow.
Follow [test and adopt](installation-and-rollback.md#test-and-adopt). A patched
source checkout is not an activated Desktop, Gateway or provider acceptance.

Create or select two idle role bots using native profile management. Preserve
source account ownership, tool access, skill policies and shared limits; do not
copy OAuth grants or channel identities. In the Bots editor, give both the same
role and family, opposite THINK/ACTION modes and reciprocal counterpart names.
Choose each bot's eligible model/effort independently. For the example fragments, name the bots
`legion-artificer-think-codex` and `legion-artificer-action-codex`. The examples
[THINK](../examples/native/developer-think.fragment.json) and
[ACTION](../examples/native/developer-action.fragment.json) are role fragments,
not complete profiles or credential templates.

Inspect old unfinished assignments before converting a legacy bot. Strict ACTION
requires a real pinned plan, so repurposing a bot with old unbound work strands
that work. Use new counterparts instead. Add both halves to the existing fleet
`kanban.dispatch_profiles` only after local acceptance, preserving all old entries
and account/project gates. Saving a pairing does not edit that allowlist. Keep a
fleet ESTOP or project hold engaged until its original owner releases it.

## Verification boundary

The clean base passed 113 native Python cases across 13 files, including an actual
Gateway plus three managed workers using a scripted loopback peer. Four scoped UI
files passed 27 cases; full Desktop TypeScript checking passed. These are offline
integration results, not paid-provider or account-readiness proof. An additional
five existing profile/board/dispatch test files passed 179 cases with four skipped;
that is a separate compatibility scope.

One separately isolated, real Codex developer case passed Captain selection,
THINK, Captain pinned handoff, Terra ACTION and independent Sol review on the same
card. The five stages logged 21 API calls, zero calls after verified terminal
handoff, and no duplicate tasks. This is a bounded synthetic workload, not a
before/after usage saving, universal billing count, cross-bot cache guarantee or
proof for every role/provider. Earlier capability and finalizer failures were
retained, not relabelled successful. No private logs, account bindings, prompts or
operational fixtures are distributed here. macOS application adoption remains
separate; offline Linux tests do not establish Mac runtime/UI parity.
