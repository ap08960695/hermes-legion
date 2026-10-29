# Known native auxiliary reasoning floor

Some native models require reasoning. Auxiliary callers such as smart approval
prefer to disable thinking for a short verdict. The previous converter omitted
an unsupported disable, leaving effort to the provider default. The owner ceiling
could then be absent from the final request, and a strict request guard refused it.

The existing auxiliary floor policy now recognizes the native route vocabulary
before its first request. On a known mandatory native model it explicitly sends
`low`. This uses local metadata, without a catalog, allowance probe, failed request,
or new provider. It preserves explicit task effort, Terra's supported `none`,
non-reasoning models, custom relay contracts and existing learned/catalog floors.
It changes no APPROVE/DENY/ESCALATE decision rule or human approval requirement.

## Verification

- Regression first reproduced five failures and three safety controls passed.
- Four focused files / 24 passed. Broad 74-file selection: 848 passed, 15 inherited
  failures, the same named failures documented in v0.7.18. They remain visible in
  the selection metadata; no assertion or fallback policy was relaxed.
- Five installed native controls each on Linux/macOS start at the actual smart
  approval entry and stop before SDK transport. Native Sol selects low, Terra
  keeps none, explicit high stays high, and a foreign relay keeps its own contract.
  Zero model/network calls for those controls. No new code-health findings.

## Real Captain case and evidence boundaries

The bounded provider-backed Captain case completed its native goal, verified its artifact, and made 9 requests. Its pending process barrier lasted 15.26 seconds without a model request. It resumed without another user prompt, with no duplicate job and no request during the 15-second post-completion observation.

The case uses synthetic files and an isolated home with the existing subscription
account through native memory-only credential access, no paid fallback and a hard
12-request ceiling. The original fleet stop state and user sessions are preserved.
Two earlier failed cases remain failed: one exposed missing effort conversion;
the next proved quiet waiting/resumption but paused after an approval timeout.
They were not resumed, overwritten, or reclassified as success.

Local process overlap is not proof of parallel dispatch across all bot families.
A successful isolated case is not original-user workload adoption, cross-bot cache
attribution, billing savings or lower production RAM. Broader acceptance remains.
