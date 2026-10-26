# Shared guidance without rewriting saved prompts

New prompt builds use the v4 shared-prefix layout. Generic task, parallel-call, steering, model-wide and coding guidance stay before its common boundary. The chosen Hermes-help variant, tool-aware worker/memory/skill guidance, tool-dependent execution hints and platform/environment hints follow that boundary. Each bot keeps its own identity, applicable instructions, granted tool schemas, project context and memory scope.

The earlier layout put some role-dependent instructions before later common text. A worker and an attended chat could therefore diverge early even when they used the same route, model and tool definitions. Giving them a matching routing key alone cannot make that different request content reusable. V4 moves those variable blocks while preserving their text; it does not delete task guidance to reduce context.

Persisted v1, v2 and v3 prompts remain recognized. Restore reconstructs their own static tier, and their routing keys are unchanged. No past message or frozen tool array is reordered merely to adopt v4. Existing cache/compaction boundaries still control when a prompt may be rebuilt. Loading new source is not permission to rewrite a running conversation.

## What was measured

A synthetic same-tool-set worker/chat pair increased its exact shared leading content from **1,895 to 2,746 characters**, with total prompt lengths unchanged at **2,835 and 2,807 characters**. Six old-layout full-prompt/static hash controls and six old routing-key controls matched the previous implementation. Native installed transport assembly retained each role's own instructions and identical granted tool schemas while producing a matching v4 cohort for the two requests. Privacy-safe request diagnostics recognize the new layout/key.

Those are controlled structural measurements, not token savings, provider-cache retention or a cross-account cache demonstration. Reuse still depends on compatible account/route/model/tool schemas and the provider's actual request layout. Character counts are not billed token counts. No cache is shared across private memory or conversation stores, and no permission follows from a routing key.

Use existing real-work diagnostic records to look for new v4 requests and their reported cached input, matching the workload and observation windows. Missing usage stays unknown. Do not send new inference solely to manufacture a hit or rewrite previous conversation content to make a comparison look better. The optional TTL setting is [a separate preference](prompt-cache-policy.md); v4 changes no provider, account, quota, retention request or paid fallback policy.
