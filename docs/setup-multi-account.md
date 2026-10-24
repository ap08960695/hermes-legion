# Configure a team with native Hermes tools

This guide is a **manual setup recipe**. The companion scripts do not run any command below, authenticate, write a live profile, install a service or call a model. Begin with a separate supported checkout/private home, not the installation currently running your work.

## 1. Keep the home outside Git

Choose an operator-owned persistent private directory outside the Legion repository. In a separate terminal, point `HERMES_HOME` at that fresh directory before using the installed Hermes CLI. Do not clone/export an existing personal profile into this repository.

```sh
export HERMES_HOME="$HOME/.config/hermes-legion-private"
hermes profile create legion-artificer-codex --no-alias --description "Implementation worker: code, offline tests and artifact handoff."
hermes profile create legion-artificer-claude --no-alias --description "Implementation worker on an alternate authorized native provider."
hermes profile create legion-forge-web --no-alias --description "Public-data Web coding specialist with verified worker tools."
```

These supported commands create profiles under the chosen home. Do not use `--clone`, `--clone-all`, `--clone-channels` or automatic imports as a privacy shortcut. Profile creation can notify a running multiplexer, so use a genuinely separate fresh home/checkout and do not apply this recipe to active profiles.

## 2. Merge the relevant native fragment

Files under `profiles/native/*.config.example.json` contain only native `model`, `fallback_providers`, legacy `fallback_model` and `credential_pool_strategies` keys. JSON is valid YAML, but **merge these fields into the newly created private `config.yaml`**, preserving other native settings and caps. Replace every `CHOOSE_EXISTING_MODEL_ID` / Web model placeholder with an existing authorized supported model. Do not run a placeholder model. Keep both `fallback_providers: []` and `fallback_model: []` (clearing any legacy chain), and the native `fill_first` strategy unless an already-authorized policy requires another strategy.

For the family instructions, review the corresponding `profiles/<role>/SOUL.md`; Web specialist instructions live under `profiles/web/`. Add only applicable reusable skills. Use explicit English `--description` or `hermes profile describe NAME --text "..."` for the worker's duty. Do not use `profile describe --auto` when additional model calls are prohibited.

## 3. Authenticate through the native flow

For a shared root pool, run the supported interactive authentication flow in the selected private root. Choose accounts you already own or are authorized to use; do not paste keys into shell command arguments or into the repository.

```sh
hermes auth add openai-codex
hermes auth add anthropic
```

Repeat only to add a genuinely different already-authorized account when the provider supports it. Re-authenticating the same underlying account does not create extra quota and can replace a single-use grant. For an intentionally independent profile-owned pool, use the native profile-specific flow instead:

```sh
hermes -p legion-artificer-codex auth add openai-codex
```

A profile-specific login changes that profile's pool ownership; do not assume it remains part of a shared root pool. Resolve actual native account IDs/labels privately and keep all bots sharing an account in the same planning quota group. Never copy OAuth refresh tokens between profiles. `hermes auth list` is a status view; do not use refresh/reset commands or model requests as setup probes.

## 4. Review routes without inference

Run the [offline dry-run](offline-planner.md) with synthetic data first. Then prepare non-identifying local reference files if needed, using already available native readiness/capability/cooldown facts. No state means hold. This does not activate a real bot or certify that a chosen model supports tools, vision or audio.

## 5. Adopt only at a safe boundary

When an operator chooses to use the prepared team, preserve running workers and saved session/model/goal bindings. Follow the normal idle-only lifecycle and current native ownership checks. The Captain uses existing Kanban tasks, role descriptions and permitted Web/native profiles; the offline planner does not dispatch them. Before any live execution, native eligibility and actual credential selection must be checked again. New real-model acceptance is separate authorization; it is not part of this offline-only update.
