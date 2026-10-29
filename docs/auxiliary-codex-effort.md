# Preserve auxiliary Codex reasoning effort

The auxiliary client used by goal judging, compression and other side tasks
first builds a chat-compatible request and then translates it to Responses.
That translation previously accepted only `extra_body.reasoning`. A selected
`reasoning_effort` at the top level, including an owner ceiling, could disappear
before the SDK serialized the request. The upstream default then applied.

The adapter now understands the existing top-level chat effort, an effort inside
`extra_body`, and a top-level Responses reasoning object. Existing explicit
nested reasoning keeps its precedence. Per-model vocabulary, explicit reasoning
disablement, unsupported-model omission and source request immutability remain.
No new setting, account, tool, provider or dependency is introduced.

## Owner ceilings

Keep the existing model and account route. A ceiling can be configured with:

```yaml
agent:
  reasoning_effort_limits:
    gpt-6.1-terra: high
```

Lower efforts and explicit `none` stay lower/off. Another model does not inherit
the Terra ceiling. The public kit does not install private bot profiles or change
quotas. An effort ceiling is not a total-token or monetary budget: input length,
number of calls and retries still matter. This patch measures request fidelity,
not production savings or subscription quota conversion.

Auxiliary transient retries are controlled by the existing global
`auxiliary.transient_retries`; a task-level `retries` field does not override that
setting. Preserve the owner's retry policy rather than assuming an unknown key
has disabled retries.

## Verification and limits

- Regression first reproduced seven failures with three safety controls passing.
- Focused selection: four files, 62 passing cases. These counts overlap the broad
  run and must not be added together.
- Broad selection: 73 files, 840 passed and 15 failed. The exact same 15 failing
  cases reproduce on the prior source in three files: `test_auxiliary_client.py`,
  `test_auxiliary_client_nous_401_cache_key.py`, and
  `test_auxiliary_fallback_multihop.py`. No global-green claim is made, and their
  assertions or fallback policy were not changed to make this release pass.
- Five native task-config-to-SDK serialization controls each on Linux and macOS:
  Terra high, max bounded to high, low, none, and a different model at max.
  These use synthetic credentials and stop before network; no model calls.
- The triggering bounded native Captain acceptance made six actual model
  requests, created its own goal and launched two independent process lanes.
  Its transport guard rejected the judge's missing effort. It paused at its
  configured three-turn limit; automatic goal completion was not proven.
  That attempt was retained as failed and was not replayed for a green result.

Native process overlap is not evidence of parallel dispatch across all bots.
The installed Desktop backend and auxiliary converter are exercised here;
original user-session adoption and a successful provider-backed goal continuation
remain separate acceptance requirements. No original paused project is resumed.
