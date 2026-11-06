# Lower diagnostic read memory and latency

Kanban warning reads now select the task state and run outcome/error fields used by the diagnostic rules. Task bodies/results and run summaries/metadata remain in SQLite during those reads. Full event payloads, ordering, graph context and all warning rules remain unchanged; opening task details still returns their existing content. No cache, schema, prompt, model route, worker limit or polling interval changed.

Migrated databases can retain legacy `spawn_failures` and `last_spawn_error` columns. When present, the projection includes them so a NULL modern field still uses the existing fallback. Fresh databases need neither legacy column. Reads remain scoped to the selected board/profile, including the existing distinction between full-board nonarchived diagnostics and explicitly selected tasks.

## Measured path

A consistent snapshot of an existing board contained 2,359 nonarchived tasks. Native Linux Python measured five warm timing samples and three traced allocation samples per version. The baseline and final implementation returned identical complete diagnostic response hashes.

| Measurement | Before | After |
| --- | ---: | ---: |
| Median diagnostic read | 94.17 ms | 71.19 ms |
| Median peak traced Python allocation | 37,551,281 bytes | 16,137,584 bytes |

That is approximately 24% less elapsed time and 57% less peak allocation in this read path. A separate baseline repeat measured 95.17 ms and the same peak allocation. This does not measure whole-Gateway RSS, total application response time or provider usage.

An identical, content-free 128-task fixture with large unused bodies/results and run evidence was also checked through both installed native Python environments. It returned the same diagnostics on both hosts and versions:

| Native host | Median before | Median after | Peak allocation before → after |
| --- | ---: | ---: | ---: |
| Linux | 58.27 ms | 13.34 ms | 59,649,797 → 791,970 bytes |
| ARM64 macOS | 80.75 ms | 9.89 ms | 59,649,797 → 791,970 bytes |

These deliberately payload-heavy synthetic records demonstrate exclusion of unused data; their reductions are not a general workload forecast. Timing is host- and fixture-specific. No model request was made, networking was denied, and Linux GPU devices were unavailable.

## Validation and adoption

Fifty tests passed across five focused files, including dashboard endpoints, diagnostic rules, read admission and graph identity. New regression cases use SQLite column authorization to make unused text inaccessible while comparing the full warning output. The migrated-schema cases failed before the legacy fallback correction and pass afterward. Four additional native checks per host cover fresh/migrated schemas, full-board/selected archived diagnostics, and denied access to unused payloads. Scoped lint and source health checks pass.

Both installed source trees match the 974-path cumulative kit. The native Linux API additionally read a copy of a previously accepted simple card: its accepted delivery and two run records survived repeated reads without dispatch or new inference. This backend-only change leaves the previously verified Desktop packages intact. Existing production Gateways were preserved and may retain old imported code until their normal restart.
