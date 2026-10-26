# Optional prompt-cache TTL policy

This recipe exposes an existing Hermes setting. It does not add a new cache implementation or change a profile's default policy automatically. The distributed fragment is synthetic and contains only the requested setting: [prompt-cache-auto.fragment.json](../examples/native/prompt-cache-auto.fragment.json). It is a merge fragment, not a complete config or a replacement for any user's config.

## What `auto` requests

```yaml
prompt_caching:
  cache_ttl: auto
```

At agent initialization, Hermes resolves the session's native source, including an explicit session-source override when present. `auto` requests `5m` for `subagent`, `cron`, `oneshot`, `webhook`, `kanban`, `api`, `tool` and `batch`; other sources request `1h`. A desktop-hosted Kanban worker still has a machine-paced source. Existing provider/model compatibility clamps apply after this choice, and a route may reduce an unsupported `1h` request to `5m`.

This setting participates in Hermes' existing Anthropic-compatible cache-marker path. It does not change the active model, account, toolset, native quota, routing or fallback chain. It does not set OpenAI retention, promise permanent provider storage or make independent accounts share a cache. Actual hits still depend on the destination, model and matching request prefix.

Choose the policy deliberately: longer-lived cache writes can consume a different billed or subscription allowance than shorter-lived writes. A requested TTL is not proof of provider support, lower total usage or a cache hit. Compare existing real-work read/write usage under the same route before claiming a saving. Do not generate model calls to populate a demonstration cache.

## Apply to an explicitly selected home or profile

Use the already supported Hermes CLI and review its `config path` output first. Root-home settings do not silently rewrite each profile's separate `config.yaml`. Opt in only the intended homes; do not loop over all installed profiles.

For an existing synthetic example profile from the Legion setup guide:

```sh
: "${HERMES_BIN:?Select the supported native Hermes executable}"
"$HERMES_BIN" --profile legion-legatus config path
# Continue only if that output identifies the intended profile.
"$HERMES_BIN" --profile legion-legatus config set prompt_caching.cache_ttl auto
"$HERMES_BIN" --profile legion-legatus config get prompt_caching.cache_ttl
```

For another selected profile, replace the synthetic name explicitly. For a root home, use its explicitly configured native launcher and first confirm `config path` points to that root. Avoid publishing a full `config get`/config dump: unrelated settings may contain private values.

Before modifying a working home, preserve the selected file's previous setting and one appropriately scoped recoverable copy. Use the native per-key setter rather than replacing an entire config from this fragment. Leave credentials, model selection, service controls, delegation limits and both fallback chains untouched. Roll back only this key to its recorded previous value with the same selected native CLI; do not restore a whole old config over concurrent changes.

New agent initialization reads the selected home's configuration. An already initialized agent may retain its previous choice. Do not interrupt active sessions or restart services simply to force this preference. If a supported idle reload is needed, treat package adoption, configuration adoption and actual provider-cache measurement as separate checks.

## Evidence and limits

Offline native acceptance used separate temporary homes: the real config setter preserved unrelated settings, a root edit did not opt in an unselected profile, and explicitly selected profiles resolved eleven session-source controls through the native initialization helper. Existing provider clamps were retained. Socket/model access and arbitrary subprocesses were denied; only exact local read-only version metadata commands were allowed.

The test did not instantiate a live model client, validate an account, restart a gateway or demonstrate provider retention. No production prompt, session identifier, bot persona, account mapping, measurement dataset or credential is distributed with this recipe. Prompt reordering and external memory integrations are separate proposals; they are not claimed as implemented by this setting.
