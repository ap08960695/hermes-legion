# Per-model reasoning effort limits

An optional effort ceiling prevents a saved session, task override, request override or
late request middleware from raising the configured model above its owner's chosen
level. It changes request metadata, without rebuilding the prompt or tools.

This feature is included in the [consolidated stable kit](stable-full-kit.md) for
upstream v0.22.5. The historical cumulative patch and smaller stable units do not
include it. Model names below are examples, not a guarantee that an account or route
can access that model. No provider call or account probe is needed to configure it.

## Configure an existing profile

Merge this mapping into the profile's existing `agent` section. Preserve its other
settings, credentials, quotas and any existing limits for other models:

```yaml
agent:
  reasoning_effort_limits:
    gpt-6.1-terra: high
```

The model remains the one the user or bot selected. A matching request for `max` or
`xhigh` becomes `high`; a request for `low` stays `low`. Other models and profiles
without a matching policy keep their existing choices. The default mapping is empty.
This is a ceiling, not a command to raise every request to `high`.

Native model spelling aliases and dated model snapshots are recognized. An exact
snapshot entry takes precedence over its general alias. An invalid matching limit
fails visibly instead of silently removing the policy. An omitted effort becomes an
explicit `medium` under an active ceiling, or the lower ceiling if applicable;
reasoning explicitly disabled stays disabled.

## What the interface shows

Once the new renderer and backend are loaded, **Bots → Edit profile** shows the
current model's limit and the effective effort. For example:

> Effort limit: high. Requested max; effective high.

Options above that current model's limit are disabled. A different model selection
is checked by the backend on Save; it does not inherit the previously displayed
model's limit. Lower efforts can be saved and reopened normally. Limits can coexist
with per-model defaults: saving one model's effort does not overwrite the generic
fallback effort used by other models.

## Runtime boundaries

- The main request is checked after request overrides and again immediately before
  execution, including the actual model in the final request.
- The existing auxiliary request builder applies the same owner-bound policy.
- Current owner limits apply to frozen session reasoning selections without
  adopting a new model, endpoint, credential, system prompt or tool list.
- A turn captures its owner's limits. Nested owner scopes remain separate, and
  existing frozen workers keep their captured state. Do not interrupt a running
  request or worker to change effort.

Use the native idle update/reload contract or a fresh eligible worker to adopt a
change. Source hashes alone do not prove that an existing session or renderer
loaded it. No timer, inference, paid fallback or quota reset is part of this feature.

A ceiling is not a dollar or token budget. Benchmark suite costs are not an account's
billing rate or subscription quota. No percentage usage saving is claimed here.

## Offline acceptance and limits

The current change has 645 passing cases in an 86-file selection, using the latest
result for each file: 84 files from the integrated run, then two corrected harness
files in a separate run. Failed earlier attempts are retained in the private work
record; overlapping runs are not summed. Three Desktop files passed 25 tests, with
native typecheck and build passing. Five source-mode Electron interaction checkpoints
used the actual backend and synthetic profiles, with zero inference requests.

These checks are not original-session adoption, a downloaded packaged application
check, provider-backed end-to-end proof or measured workload savings. One independent
inherited guard remains known: two unchanged raw YAML reads in `tools/kanban_tools.py`
fail `tests/hermes_cli/test_config_read_guard.py`. It is not suppressed or included
in the passing selection. Cross-profile and frozen-worker behavior must be preserved
when repairing those separate reads.
