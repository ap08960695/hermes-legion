# Configure a team with native Hermes tools

This guide is a **manual setup recipe**. The companion scripts do not run any command below, authenticate, write a live profile, install a service or call a model. Begin with a separate supported checkout/private home, not the installation currently running your work.

You can first [preview and validate an offline setup bundle](offline-setup-tools.md). The exporter prepares files only; the native steps below remain explicit operator actions.

## Prerequisites and scope

Use the exact supported Hermes checkout from [installation](installation-and-rollback.md), with its dependencies already prepared through the upstream package manager. These examples are POSIX-shell/Linux instructions. `HERMES_BIN` must point to the native Hermes CLI belonging to that isolated installation. Changing `HERMES_HOME` alone does **not** change which checkout a launcher executes. Do not reuse a launcher that forcibly selects your active home or an unrelated checkout.

The offline acceptance covers native command parsers/handlers creating three profiles, setting and reading their config, preserving an unrelated delegation cap and copying SOUL text in temporary homes. A full packaged CLI startup and its home-bootstrap/service-manager behavior are not certified by that test. Actual OAuth login, model availability, live routing and platform/service deployment require separate operator verification and are not claimed by offline tests.

## 1. Select a fresh private home and the intended executable

Start in the Legion repository root, in a separate terminal. Set the CLI path and model IDs from your already authorized installation; model placeholders in the distributed fragments are not runnable model names. Do not paste credentials into any of these variables.

```sh
export LEGION_ROOT="$(pwd)"
# Replace this with your isolated installation's executable:
export HERMES_BIN="/path/to/isolated/hermes"
export LEGION_PRIVATE_HOME="$HOME/.config/hermes-legion-private"
```

Run the following block only after choosing that executable. It deliberately refuses an existing private home. Pick another fresh directory rather than deleting existing data. The `config path` subcommand reports the selected path and must identify the intended new root before profile creation. Native CLI startup may initialize metadata in that private home; use the isolated installation and never point it at a working home for this check.

```sh
set -eu
: "${HERMES_BIN:?Set the isolated Hermes executable}"
test -x "$HERMES_BIN"
test -f "$LEGION_ROOT/profiles/artificer/SOUL.md"
if [ -e "$LEGION_PRIVATE_HOME" ]; then
  echo "Choose a fresh LEGION_PRIVATE_HOME; existing data will not be overwritten." >&2
  exit 1
fi
export HERMES_HOME="$LEGION_PRIVATE_HOME"
legion_actual_config_path="$("$HERMES_BIN" config path)"
if [ "$legion_actual_config_path" != "$HERMES_HOME/config.yaml" ]; then
  echo "The executable did not select the requested private home. Stop and inspect it." >&2
  exit 1
fi
"$HERMES_BIN" profile create legion-artificer-codex --no-alias --description "Implementation worker: code, offline tests and artifact handoff."
"$HERMES_BIN" profile create legion-artificer-claude --no-alias --description "Implementation worker on an alternate authorized native provider."
"$HERMES_BIN" profile create legion-forge-web --no-alias --description "Public-data Web coding specialist with verified worker tools."
```

These native commands create only the three named profiles in the selected home. They do not install the full 34-profile team. Do not use `--clone`, `--clone-all`, `--clone-channels` or automatic imports as a privacy shortcut. Profile creation can notify a multiplexer serving that home; this is why a genuinely fresh home/installation is required. Do not run this recipe against active profiles.

## 2. Configure each new bot and install its role instructions

First choose three supported model IDs from existing, authorized routes. Do not run inference or an allowance probe to fill these variables.

```sh
# Replace these values; they are explanatory placeholders, not account IDs or keys:
export LEGION_CODEX_MODEL="CHOOSE_EXISTING_MODEL_ID"
export LEGION_CLAUDE_MODEL="CHOOSE_EXISTING_MODEL_ID"
export LEGION_WEB_MODEL="chatgpt-web/CHOOSE_EXISTING_WEB_MODEL_ID"
```

After replacing the placeholders, use native `config set` rather than overwriting the whole YAML file. The function preserves unrelated native settings/caps and explicitly clears both current and legacy fallback chains. It operates only on the fresh profiles created above.

```sh
legion_configure_profile() {
  legion_profile="$1"
  legion_provider="$2"
  legion_model="$3"
  legion_soul="$4"
  case "$legion_model" in
    *CHOOSE*|"") echo "Choose a supported authorized model ID first." >&2; return 1 ;;
  esac
  "$HERMES_BIN" -p "$legion_profile" config set model.provider "$legion_provider"
  "$HERMES_BIN" -p "$legion_profile" config set model.default "$legion_model"
  "$HERMES_BIN" -p "$legion_profile" config set fallback_providers '[]'
  "$HERMES_BIN" -p "$legion_profile" config set fallback_model '[]'
  "$HERMES_BIN" -p "$legion_profile" config set "credential_pool_strategies.$legion_provider" fill_first
  cp "$legion_soul" "$HERMES_HOME/profiles/$legion_profile/SOUL.md"
}
legion_configure_profile legion-artificer-codex openai-codex "$LEGION_CODEX_MODEL" "$LEGION_ROOT/profiles/artificer/SOUL.md"
legion_configure_profile legion-artificer-claude anthropic "$LEGION_CLAUDE_MODEL" "$LEGION_ROOT/profiles/artificer/SOUL.md"
legion_configure_profile legion-forge-web openai-codex "$LEGION_WEB_MODEL" "$LEGION_ROOT/profiles/web/forge-web/SOUL.md"
"$HERMES_BIN" -p legion-artificer-codex config get model.provider --json
"$HERMES_BIN" -p legion-artificer-codex config get model.default --json
"$HERMES_BIN" -p legion-artificer-codex config get fallback_providers --json
"$HERMES_BIN" -p legion-artificer-codex config get fallback_model --json
```

`profiles/native/*.config.example.json` contains the equivalent native settings for the other profiles; JSON is valid YAML. Use the selected provider/model and empty fallback fields without replacing an existing entire config file. A model placeholder may parse as a string but does not certify a live model. Review the corresponding family `SOUL.md` / Web instructions, add only applicable reusable skills, and set an explicit English worker description. Do not use `profile describe --auto` when additional model calls are prohibited.

## 3. Authenticate through the native flow

For a shared root pool, run the supported interactive authentication flow in the selected private root. Choose accounts you already own or are authorized to use; do not paste keys into shell command arguments or into the repository.

```sh
"$HERMES_BIN" auth add openai-codex
"$HERMES_BIN" auth add anthropic
```

Repeat only to add a genuinely different already-authorized account when the provider supports it. Re-authenticating the same underlying account does not create extra quota and can replace a single-use grant. For an intentionally independent profile-owned pool, use the native profile-specific flow instead:

```sh
"$HERMES_BIN" -p legion-artificer-codex auth add openai-codex
```

A profile-specific login changes that profile's pool ownership; do not assume it remains part of a shared root pool. Resolve actual native account IDs/labels privately and keep all bots sharing an account in the same planning quota group. Never copy OAuth refresh tokens between profiles. `hermes auth list` is a status view; do not use refresh/reset commands or model requests as setup probes.

## 4. Review routes without inference

Run the [offline dry-run](offline-planner.md) with synthetic data first. Then prepare non-identifying local reference files if needed, using already available native readiness/capability/cooldown facts. No state means hold. This does not activate a real bot or certify that a chosen model supports tools, vision or audio.

## 5. Adopt only at a safe boundary

When an operator chooses to use the prepared team, preserve running workers and saved session/model/goal bindings. Follow the normal idle-only lifecycle and current native ownership checks. The Captain uses existing Kanban tasks, role descriptions and permitted Web/native profiles; the offline planner does not dispatch them. Before any live execution, native eligibility and actual credential selection must be checked again. New real-model acceptance is separate authorization; it is not part of this offline-only update.
