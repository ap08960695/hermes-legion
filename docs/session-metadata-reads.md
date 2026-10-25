# Small session metadata reads

Runtime resume and onboarding sometimes need one entry from a session's
`model_config`, rather than its conversation context. The native
`get_session_model_config_value` method now selects only that JSON column.
Previously, it called the full session reader, which also resolved the stored
system prompt and tool context before returning the small value.

The normal full-session reader is unchanged. Missing sessions and keys retain
their supplied defaults, JSON null remains null, and a committed configuration
update is visible on the next read. No shared content cache, schema migration,
provider request, account selection or prompt-prefix change is introduced.

The regression uses the actual stored Codex thread-binding consumer with a
temporary native SQLite database. SQLite denies reads of the session's prompt
and tool-content columns; the binding must remain available in both normal and
read-only database modes. Controls cover missing defaults, nested values, null
and newly committed metadata. This is offline storage acceptance, not a model
conversation or provider-resume test.

## Isolated measurement

Seven alternating before/after batches each performed forty warm lookups against
the same native database, with a synthetic 1,703,936-byte system context. Median
results were:

| Metric | Full-session lookup | Metadata-only lookup |
|---|---:|---:|
| Time per lookup | 0.737608 ms | 0.010506 ms |
| Peak traced Python allocations during a batch | 1,733,644 bytes | 14,032 bytes |

These measurements describe this small read path under one synthetic fixture.
They are not whole-process RSS, total task latency, billed usage or a production
token-saving percentage. Neither the benchmark nor the regression calls a model.

Existing processes must load the source through their normal idle lifecycle.
Source installation and offline acceptance alone do not prove that an already
running Desktop or Gateway has adopted the change. Preserve active work and
verify fresh source identity and read-only readiness separately.
