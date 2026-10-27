# Verify your own Hermes deployment

Installing the patch, loading it, completing an offline test, and improving a real workload are separate results. Keep evidence for each applicable row below. A release inventory or a green CI run does not establish all of them.

| Requirement | Evidence to collect | What remains unproven without it |
|---|---|---|
| Exact source installation | Verify the pinned upstream base, apply the patch, then run the installed-phase checkout verifier. Preserve unrelated local changes. | A downloaded archive alone does not show which source is installed. |
| Desktop and Gateway adoption | Use the normal idle lifecycle; verify the package, owning process, source age and native readiness. Keep the original session/model binding. | A source hash does not show that an older process loaded it. Readiness alone does not prove an interactive journey. |
| Usable interface | Exercise History, Bots, Hub, Work/Workflow, goals, settings and the chat formats you use; include keyboard access, short windows, failed reads and draft retention. | Isolated synthetic UI checks do not certify every production integration. |
| Clear bot activity | Compare the displayed card, bot, phase and recorded run with native task/run evidence. Follow a selected card's real dependency and bot history. | Current assignment or an animated edge does not prove execution. |
| Autonomous goals | Use an authorized native goal, verify its saved scope and limits, then observe planning, independent work, review, waits and terminal outcome. Keep approval gates and holds. | A policy, skill or configured goal does not prove that a mounted Captain consumed it or finished work. |
| Parallel work and startup | On authorized independent work, record ready, claim, process-start, first action and completion times. Demonstrate overlap without shared-resource conflicts. | Dispatch fixtures and process readiness do not measure real startup delay or sustained concurrency. |
| Fewer calls | Count calls through the completed task/run, including retries and any calls after verified completion. Compare equivalent successful work. | One stopped worker does not prove every role, provider or controller behaves the same. |
| Think/action routing | Trace the Captain's actual planner choice, bounded executor handoff, specialist/reviewer choice and completion. Verify the task's resolved model and effort. | An offline role matrix, profile default or forced model on a test card is not autonomous selection. |
| Lower usage with equivalent results | Use covered, comparable before/after windows and completed-card results. Report calls/tokens per completed card and per equal time window, alongside quality and failures. | Token totals alone cannot separate lower usage from fewer or easier tasks. Synthetic timings are not billed savings. |
| Cache behavior | Collect valid reported input/cached usage with route, profile, task/run and request metadata. Keep unknown values distinct from zero. | Matching prefixes and cache hits in two profiles do not identify which bot populated provider cache or prove cross-bot reuse. |
| Context and memory continuity | Retrieve an authorized older result through native scoped search and bounded paging, checking session/profile, source field, visibility and returned content. Test continued work against its original requirements. | A synthetic match or a metadata lookup does not prove that a bot retained the task's meaning or resumed correctly. |
| Lower RAM and latency | Compare the same path and workload; distinguish traced Python allocations, process RSS and whole-service memory. Include repeat behavior and latency regressions. | A bounded reader or smaller fixture peak is not a whole-system memory or response-time result. |
| Bounded disk growth | Verify configured retention, actual cache-volume admission and safe scheduled cleanup. Record exact eligible bytes reclaimed; preserve active work, ambiguous ownership and required rollback points. | A changed free-space reading does not attribute a saving. A fail-closed cleanup is preservation evidence, not reclaimed bytes. |
| Safe public delivery | Review the exact files, historical paths and reachable Git content, release metadata, manual asset and automatic source archive. Scan for secrets and compare known private identifiers/credentials locally. Verify anonymous readback and the intended publisher. | A scanner with no findings is not a guarantee that every type of personal information was detected. |

## Measure without manufacturing a result

Start with existing native evidence and state its coverage, missing logs, unknown bindings and test/production distinction. Keep prompts, transcripts, tokens and private identifiers out of public reports. Do not issue extra model requests merely to make a cache hit or complete a graph.

When real acceptance needs model work, use only explicitly authorized work within existing quotas and provider rules. An emergency stop, project hold, missing permission or unavailable controller remains a gate. Do not clear a pause, replay ambiguous work, enable paid fallback or move a running worker just to finish a checklist. A stopped system can still support offline checks; label the untested runtime requirements as unproven.

Compare equivalent results, not just lower counters. Compression can reduce total input while the first subsequent request has a lower cache ratio; a memory repair can trade some latency for bounded retention. Report both sides. See the [verification record](verification.md), [cache policy and limits](prompt-cache-policy.md), [native goals](goals-and-delegated-decisions.md), [bot activity](bot-activity.md), and [storage guide](storage-and-backups.md).

## Versioned documentation

Feature sections record the version in which behavior changed. Follow later entries when they supersede an older limitation; for example, structured global recall in v0.6.41 extends the scoped structured search introduced in v0.6.36. The latest release's source inventory remains the authority for its included files. This checklist adds no runtime behavior, background polling, model call or default configuration.
