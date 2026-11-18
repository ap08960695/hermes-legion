# Source kit and verification index

This is the detailed source-kit reference. Each entry records the evidence
available for that implementation step. See the [product README](../README.md)
for current highlights, the [changelog](../CHANGELOG.md) for released changes,
and the [verification record](verification.md) for acceptance boundaries.
The project retained its version names after [privacy maintenance](privacy-maintenance.md).
Earlier commit and archive hashes may differ from current downloads.

## Bot Monitor source kit — v0.34.0

This source kit includes the [Bot Monitor dashboard](design-bot-monitor.md):
Bots → Monitor gathers current bot/worker observations into one searchable,
sortable table. It now shows recorded worker estimates/provider-reported amounts
separately, with a partial-coverage hint. Bot rows now show their stored Bot Chat
tokens/cost and recorded model beside the configured bot model. Worker usage stays
separate; these are recorded row values, not lifetime totals. Missing facts stay
unavailable. Recent reports now opens recorded task outcomes and bounded report/
error excerpts, with local outcome filters and recorded-stalled/Stopped/Unknown
labels. Historical issues stay separate from current work. A native gateway
regression follows real delegation and file reading into completed, rejected and
explicitly stopped task reports, including independent side-chat/profile controls.
Its stopped case keeps saved child state unchanged after the held server response
handler finishes; arrival at the canceled client completion handler is unproven. The successful case retains a real heartbeat. Model
columns now keep a readable minimum width instead of squeezing labels into a few
letters; narrow tables keep their existing horizontal scroll. Browser fixture
before/after checks cover this layout. Closing reports with Escape or Close now
returns keyboard focus to the report button. Model replies and usage are fixtures;
a browser adapter also follows a real native worker from Working/step into its
completed report. Native wide Completed/Error reports and failed-refresh recovery
now pass. A fresh native narrow Stop scenario also passes its final ACK, with
nonempty worker search/Working filtering, elapsed sorting and keyboard reach to
hidden actions. Recorded-issue filtering and Error-excerpt search now have guarded
native observations, but that trial's report-click admission failed before input.
A separate focused native trial now reopens the existing nonempty named Bot Chat,
matching its saved session/profile/transcript without creating a session or model
call. Feature-batch review retains the failed Error-control scenario boundary;
see the [release gate audit](design-bot-monitor.md#release-gate-audit--2026-11-17).
The Bot Monitor batch is tagged v0.34.0. Daily-app adoption is tracked
separately. [Release notes](release-notes-v0.34.0.md).

The [agent-desktop diagnostics slice](design-agent-desktop.md) is also
unfinished and opt-in: `hermes computer-use status --backend agent-desktop` finds an existing
installation and reports permission states. Configure a binary/release directory
with `hermes config set computer_use.agent_desktop.path /path/to/agent-desktop`.
This does not select a runtime provider or establish snapshot/action support.
An opt-in AX ref provider is now included: select `computer_use.backend:
agent-desktop`, then call `computer_use` capture with `mode=ax` and an explicit
application name. Add a numeric native `window_id` to select a window within that
app; window-only requests are refused before the native probe. Semantic
`click(element)`, `set_value(value, element)` and
`type(text, element)` consume one captured ref set, then require a fresh capture.
Text travels through stdin; type inserts at the caret, while set_value replaces
its value. Targeted type requires a TypeText ref and at most 10,000 UTF-8 bytes.
Scroll now accepts a captured `scrollarea` element, one direction and 1–50 units;
its ref is consumed and a fresh capture is required. Coordinates/focus are refused.
Host/sandbox boundaries remain enforced. Native input success, screenshots and
other input forms remain unverified or unimplemented; see the design note.
Workspace snapshot-ref writes and the canonical native input lease need separate
authorization in the isolated trial. Full-production Local Monitor capture now
passes through the provider/common tool with 50 native refs and a CUA comparison.
App + window selection passes three foreground Monitor captures in one session.
Three minimized-window native AX reads also pass, with own-window telemetry and
a restored CUA comparison; this does not establish minimized pixels or cold start.
Use a unique app scope and a fresh trusted native window ID; IDs can be reused.
Earlier window-only output proof did not establish inventory isolation. Input
acceptance remains open. See the [capture boundary](design-agent-desktop.md#snapshot-and-input-write-authorization).
When a native window lacks an accessibility element, capture now reports that
specific limitation and directs you to inspect the target app's accessibility
support. Native titles and guidance stay private; no automatic focus or retry.
Cold inactive-window acceptance remains failed; see the [background diagnosis](design-agent-desktop.md#background-capture-diagnosis).

## What is included

- [Per-bot characters in Monitor previews](design-bot-characters.md#per-bot-installed-characters--unreleased): Edit Profile lists installed packs without contacting Petdex. Monitor uses the selected pack for the bot and its workers. Local Desktop request routing and saves pass isolated Mac tests. Native screen acceptance remains open.
- [Bot character preview — source step](design-bot-characters.md#active-character-overlay-preview-offline-source-step): Monitor can opt into five source-qualified bot/worker characters using the installed pet and existing overlay. Source checks pass. A guarded native trial reached overlay loading and exposed a theme-font request, now suppressed only for the pet overlay; native confirmation and performance acceptance remain open.
- [Character pack creation](character-pack.md): `hermes pets validate IMAGE|DIRECTORY` checks local atlas/creator metadata without installation. `pets show --pack DIRECTORY --cycle --once` previews before installation; `pets import DIRECTORY SLUG` adds a new entry without replacing/selecting a pet. Includes a blank manifest, original CC0 example generator and a self-contained [character-pack-creator skill](../skills/character-pack-creator/SKILL.md); full pack/runtime support remains in development.
- [Pet picker source isolation](design-bot-characters.md#pet-picker-source-isolation-completed-offline-prerequisite): Edit Profile/New Bot read the intended pet library; equal slugs from different profiles have separate thumbnails, and late selection results cannot overwrite a new choice. Source checks and contained native gallery/thumbnail handlers pass. Desktop screen acceptance remains open.
- [Pet creator preview](design-bot-characters.md#first-completed-slice-creator-state-preview): `hermes pets show --cycle --once` previews all seven activity states once. Native terminal before/after checks pass; the desktop characters capability remains in development.
- [Captain work in Catch up](goals-and-delegated-decisions.md#read-the-captain-plan-and-delegated-activity-unreleased-work): see the current chat's received plan, worker progress and latest finished results, including failures after Captain follow-up. Native Local before/after checks pass; the complete autonomy capability remains unreleased.
- [Captain autonomy controls](goals-and-delegated-decisions.md#check-every-intended-captain): two independent profile permissions in **Settings → Safety → Captain autonomy**. Defaults, pauses and budgets stay unchanged. This is the first step of the [autonomy capability](design-captain-autonomy.md), not a completed workflow release. The [real-provider acceptance contract](goals-and-delegated-decisions.md#prepare-real-provider-acceptance) records the remaining quota and evidence gates.
- [Stop Captain work](goals-and-delegated-decisions.md#stop-the-sessions-current-work): the working composer adds direct Stop while its workers run, preserving Send and drafts. Session Stop also pauses the active goal. Native Local direct Stop, paused goal and unchanged state after the held server reply now pass; the full autonomy capability remains unreleased.
- [v0.34.0: Bot Monitor](release-notes-v0.34.0.md), one dashboard for task/progress/usage, recorded issues/reports and source-qualified chat actions. Source release prepared for driver handoff.
- [v0.33.8: keep attachment size edits when closing Settings](release-notes-v0.33.8.md), saves the focused preview limit before Escape closes the page.
- [v0.33.7: report group membership save failures](release-notes-v0.33.7.md), keeps a failed membership change visible and offers explicit Retry.
- [v0.33.6: announce compact bot work correctly](release-notes-v0.33.6.md), aligns row names and name tooltips with existing work state.
- [v0.33.5: keep list edits when closing Settings](release-notes-v0.33.5.md), preserves a focused comma-separated list when Escape closes Settings.
- [v0.33.4: nudge compression ratios precisely](release-notes-v0.33.4.md), makes Threshold and Target arrows change by one percentage point.
- [v0.33.3: scope Settings config actions](release-notes-v0.33.3.md), makes Export and Reset use the displayed Applies to profile and names the Reset target.
- [v0.33.2: keep untouched settings visible after import](release-notes-v0.33.2.md), preserves switches and budgets through partial and repeated config imports.
- [v0.33.1: confirm config imports after saving](release-notes-v0.33.1.md), removes premature success on cancelled or failed Settings imports.
- [v0.33.0: see parallel bot work](release-notes-v0.33.0.md), lists observed workers and their progress, with consistent activity counts and status when one stops.

- [v0.32.0: read and enlarge chat charts](release-notes-v0.32.0.md), opens charts in the existing pan/zoom viewer and exposes full labels and parsed values through Details.
- [v0.31.1: keep same-goal delegation cards separate](release-notes-v0.31.1.md), shows each native child's own progress and outcome when two calls have identical goals.
- [v0.31.0: name and reopen Local groups](release-notes-v0.31.0.md), creates and reopens canonical rooms, with a new Rename control that keeps the room identity, members and unsent chat draft.
- [v0.30.2: show background reports without Reload](release-notes-v0.30.2.md), refreshes the saved completion after the parent reply finishes; task outcomes and reports appear in the current chat.
- [v0.30.1: clean saved background reports](release-notes-v0.30.1.md), hides the canonical gateway notice and terminal trace path while keeping task outcomes and report output.
- [v0.30.0: reopen delegated task outcomes](release-notes-v0.30.0.md), expand a saved completion after Reload to see each task's outcome beside its name and the existing report.
- [v0.29.5: show stopped delegated responses](release-notes-v0.29.5.md), uses a neutral stopped label instead of Error for an interrupted child; native Stop A / keep B working checked.

- [v0.29.4: show delegated bot work](release-notes-v0.29.4.md), reports native delegated children as Working and clears their detail after completion; actual Local UI lifecycle checked with loopback replies.

- [v0.29.3: keep bot model labels readable](release-notes-v0.29.3.md), keeps long provider/model text inside its dropdown with visible arrows and full-name tooltips; native Local wide/narrow layout and menu dismissal checked.

- [v0.29.2: save bot descriptions without a helper](release-notes-v0.29.2.md), uses the existing gateway writer, confirms each write and retains failed drafts; native Local Thai/English Save and reopen checked.

- [v0.29.1: keep bot edits after a failed save](release-notes-v0.29.1.md), retains the draft and avoids a false success when a profile section fails; native Local rejected-write handling and title Save/reopen checked.

- [v0.29.0: activity on bot cards](release-notes-v0.29.0.md), reported description/tool/step/time/token facts beside the canonical preview; native Local display and ended-record transitions checked with controlled records, not real worker execution.

- [v0.28.1: readable bot card status](release-notes-v0.28.1.md), fixes status text squeezed beside the action buttons; checked on the native Local Mac app at wide and narrow widths.

- [v0.28.0: easier Settings actions without losing your draft](release-notes-v0.28.0.md), named Export/Import/Reset actions, keyboard continuation after Cancel, and first-visit Local draft preservation, checked in wide and narrow native Mac windows.

- [v0.27.0: on-demand host toolchain facts](release-notes-v0.27.0.md), disabled gateway warmup now defers five unused startup checks; first-use facts remain, with longer first-turn time and no proven RAM saving.

- [v0.26.0: Local startup leaves saved remotes on demand](release-notes-v0.26.0.md), passive roster and Bot Relay work no longer initializes unused remote connections; explicit remote work remains available.

- [v0.25.0: bounded fresh backend checks](release-notes-v0.25.0.md), configurable probe concurrency and memory admission; controlled native Mac cases used 27.93% less combined peak RSS, with slower completion.

- [v0.24.0: bounded Desktop ticket backlogs](release-notes-v0.24.0.md), one unanswered frame per helper and shared admission for busy reuse; native Mac 64-grant parity and 257/43 overload recovery, with unchanged RAM.

- [v0.23.0: source-check memory admission](release-notes-v0.23.0.md), waiting for low or unknown RAM within the existing active budget; four controlled native Mac overlap cases used 23.7% less median peak RSS, with longer completion.

- [v0.22.0: bounded Desktop runtime lookups](release-notes-v0.22.0.md), sharing ticket-helper admission and stopping stale generations; four controlled native Mac cases used 22.7% less median peak RSS, with slower request completion.

- [v0.21.0: bounded idle cache cleanup](release-notes-v0.21.0.md), one idle-sweep cleanup job per runner using the existing executor; four native Mac cases reduced concurrent idle callbacks from four to one, with longer cleanup and essentially unchanged RSS.

- [v0.20.0: on-demand local dashboard loading](release-notes-v0.20.0.md), an opt-out from background dashboard warmup; four canonical Mac startup cases used 14.0% less median idle RSS, with a slower first dashboard request.
- [v0.19.0: gateway memory diagnostics](release-notes-v0.19.0.md), reading one native local snapshot from the CLI, with current RSS available on macOS; no polling or model call.
- [v0.18.0: optional on-demand gateway preset](release-notes-v0.18.0.md), using existing controls to defer turn warmup and cached MCP startup; one native initialized-runner Mac pair used 19.2% less idle RSS, with longer first-use initialization.
- [v0.17.0: profile defaults for MCP idle retirement](release-notes-v0.17.0.md), an opt-in timeout that releases idle stdio peers and their supervisor; one native Mac component pair used 24.7% less idle RSS, with longer next-call latency.
- [v0.16.0: ticket-helper memory admission](release-notes-v0.16.0.md), waiting for low/unknown execution-host memory within the existing mint deadline; one controlled native Mac overlap case used 19.6% less sampled peak RSS.
- [v0.15.0: on-demand Desktop ticket helpers](release-notes-v0.15.0.md), configurable helper limits and short idle retirement; one native three-profile Mac case used 46.3% less request-window peak RSS and left zero helpers idle.
- [v0.14.0: shared Desktop source-update checks](release-notes-v0.14.0.md), reusing identical running checks and queueing distinct work; one native cached two-request Mac case used 50.2% less peak RSS and launched one interpreter instead of two.

- [v0.13.0: memory-aware Desktop checks](release-notes-v0.13.0.md), waiting below a 512 MiB execution-host threshold; one modeled-pressure native Mac case used 37.1% less peak RSS, with longer completion time.

- [v0.12.0: lighter session metadata startup](release-notes-v0.12.0.md), avoiding a turn-engine import for saved-message metadata; one cached-startup case used 13.2% less RSS before opening history, with storage and peak memory essentially unchanged.

- [v0.11.0: lighter cached MCP startup](release-notes-v0.11.0.md), leaving the SDK unloaded until a connection is needed; one fresh Mac client used 22.8% less RSS before first use, with that import cost deferred to the call.

- [v0.10.0: on-demand MCP startup](release-notes-v0.10.0.md), a profile opt-in that leaves unused cached stdio servers stopped; one Mac component case used 30.7% less RSS before first use, with connection latency moved to that call.

- [v0.9.0: bounded Desktop SSH checks](release-notes-v0.9.0.md), sharing compatible transports and queueing helpers; one measured Mac check burst used 70.4% less peak RSS, with longer completion time.

- [Overflowing web-cache TTL recovery](search-cache-memory.md#overflowing-ttl-configuration-v0876), keeping the normal search/cache path usable when a configured integer cannot convert to float.

- [Request-cache admission before locking](vision-cache-routes.md#request-cache-completion-admission-v0875), evaluating each owner result once while independent cache consumers can progress.

- [Vision content-cache byte budget](vision-cache-routes.md#retained-analysis-byte-budget-v0874), bounding retained analysis payload while returning fresh results unchanged.

- [Gateway compression-tip metadata](session-metadata-reads.md#gateway-compression-tip-liveness-v0873), checking liveness without hydrating unused prompt, tool or configuration payloads.

- [Web index write admission](storage-and-backups.md#web-index-write-admission-v0872), retaining the prior atomic index when its volume cannot admit a conservative serialized-byte budget.

- [Web full-text write admission](storage-and-backups.md#web-full-text-write-admission-v0871), preserving prior cache/paging files and fresh extraction results when space is low or unavailable.

- [Encoded archive reserve checks](storage-and-backups.md#encoded-archive-reserve-v0870), checking each gzip/tar write against observed free space and retaining reports on pressure or observation failure.

- [Malformed web-cache timestamp recovery](search-cache-memory.md#oversized-disk-timestamps-v0869), treating overflowing metadata as a cache miss while preserving the selected search provider and normal reuse.

- [Postpublication report activity checks](storage-and-backups.md#report-activity-after-publication-v0868), retaining source reports and verified archives when activity becomes busy or unknown during publication.

- [Prompt-cache identity projections](session-metadata-reads.md#declared-cache-scope-identity-v0867), avoiding unused prompt/tool context while preserving fork isolation and worker receipt semantics.

- [Mixed-name MCP filter fingerprints](mcp-schema-publication.md#mixed-name-filter-fingerprints-v0866), keeping cache discovery consistent with registration's existing string conversion while preserving ordinary string keys.

- [Planner numeric-input refusals](offline-setup-tools.md#oversized-planner-timestamps-v0865), keeping oversized snapshot integers inside the existing value-free CLI error path.

- [Metadata-only compression parent checks](session-metadata-reads.md#compression-parent-checks-v0864), avoiding unused parent context while retaining receipt-local worker reads and lineage decisions.

- [Stable snapshot home selection](storage-and-backups.md#bind-cli-selection-to-one-physical-home-v0863), keeping preflight and every selected snapshot in the same physical home if its explicit alias changes.

- [Snapshot path revalidation](storage-and-backups.md#revalidate-snapshot-paths-during-compaction-v0862), retaining originals when a backup root or parent becomes a symlink during compaction.

- [Case-alias profile links](session-recall.md#case-alias-profile-links-v0861), retaining the original conversation when a case-variant profile path produces a link that is reopened after switching profiles.

- [Recall with unusable start times](session-recall.md#nonfinite-session-start-times-v0860), preserving title/scoped/message-page access while retaining existing metadata date filters.

- [Boolean judge wait targets](goal-result-waits.md#boolean-judge-wait-targets-v0859), preventing JSON booleans from selecting PID or time 1 while retaining valid alias fallback.

- [Streaming vision content keys](vision-cache-routes.md#streaming-content-keys-v0858), preserving cache identity while avoiding a full prepared-image allocation during hashing.

- [Overflow-safe MCP schema-cache expiry](mcp-schema-publication.md#overflow-safe-expiry-metadata-v0857), keeping malformed TTL metadata from interrupting other lazy server registrations.

- [Native compressed-resume acceptance](session-metadata-reads.md#compressed-resume-receipts-v0856), proving logical receipt ownership and retained history through native synthetic storage and config loaders.

- [Metadata-only classic resume identity lookup](session-metadata-reads.md#classic-resume-identity-v0855), preserving title/prefix and compression-tip selection with less transient context allocation.

- [Metadata-only exact session ID lookup](session-metadata-reads.md#exact-session-id-lookups-v0854), avoiding prompt/config hydration while preserving ID and prefix resolution rules.

- [Bounded TUI Git-label memory](chat-rendering-surfaces.md#bounded-git-label-cache-v0853), preserving branch labels and five-second freshness while retaining at most 128 directories.

- [Backup-root link refusal](storage-and-backups.md#backup-root-boundary-v0852), keeping snapshot compaction inside the selected physical backup directory.

- [Overflow-safe judge wait targets](goal-result-waits.md#overflowing-judge-wait-targets-v0851), preserving alias fallback and wait priority instead of raising outside the judge return contract.

- [Timestamp-safe goal-judge memo keys](goal-judge-memo.md#preserve-timestamp-evidence-v0850), preserving evidence while reusing verdicts across generated-clock changes.

- [Retention failure isolation](storage-and-backups.md#report-validation-failures-v0849), keeping rejected reports intact while processing later eligible entries.

- [Explicit patch-manifest selection in the offline doctor](offline-setup-tools.md#select-the-matching-patch-manifest-v0848), preserving historical defaults and strict source checks.

- [PM-managed Mac source install/update checks](macos-install-update.md#managed-runtime-acceptance-v0847), with synthetic settings/profile/search continuity and no provider work.

- [Release history checks that disable repository fsmonitor hooks](privacy-review.md#read-only-history-check-v0846), with disposable-Git regressions.

- [Private credential-store paths for auxiliary refresh tests](auxiliary-refresh-test-isolation.md), preserving the native lock and refresh assertions.
- [UTF-8 state files with optional BOMs](utf8-state-files.md), preserving quota observations and recovery checks.
- [Passing native checks and bounded test memory](native-checks-and-test-memory.md), preserving ownership checks and Python module caching.

- [Optional compact card-worker schemas](compact-worker-schemas.md), with a native configuration fragment and one bounded comparison showing 21.22% lower total input; general performance remains unproven.

- [Official Codex alias usage without unnecessary pricing-catalog reads](codex-alias-usage.md), with installed Linux/Mac checks and bounded real-card acceptance.

- [Complete Captain skill installation and offline copy checks](captain-skill-installation.md).

- [Automatic review continuation and verified maintenance retirement](native-maintenance-continuation.md).

- [Lower diagnostic read memory and latency](diagnostic-read-efficiency.md).

- [Work tracking and independently reviewed delivery](tracked-delivery.md).

- [Refined charts, tables and diagrams](rich-output-presentation.md).


- [Cycle-safe skill discovery and declared-name preflight](skill-discovery.md) shared by the skill index, catalog signature and Kanban preflight.

- [Assignee-scoped Kanban preflight](assignee-preflight.md) that retains configured external skills and preserves frozen-worker fanout.

- A [compact bot settings editor](desktop-bot-settings.md) that keeps model/effort visible and groups optional appearance controls.
- Optional [per-model effort ceilings](reasoning-effort-limits.md), with effective/requested effort disclosure and offline request-boundary checks.
- A consolidated [1064-path source and Desktop kit for upstream v0.22.5](stable-full-kit.md), with pinned hashes and a reproducible test selection. It includes the interface, workflow, search, memory/cache, usage, waiting and update-preservation changes as one complete alternative.
- v0.8.0 adds live bot progress (current tool, step, elapsed, tokens), inline `chart` answers with diagram guidance, a vision result cache, cacheable compression prompts, crash-safe worker attempt markers, opt-in delegated goal decisions and fleet-wide session search. See [the update notes](stable-full-kit.md#efficiency-monitoring-and-autonomy-update-v080).
- v0.8.10 records [native Desktop and bounded recall acceptance](native-desktop-recall-acceptance.md), without changing the source patch.
- v0.8.13 [explains settings write failures without exposing private paths](settings-write-errors.md), with native permission-failure recovery checks.
- v0.8.14 documents an optional [eager search schema for recall workers](recall-tool-policy.md): one native card pair used three requests instead of four, with the source kit unchanged.
- v0.8.15 [preserves nested settings edits followed by a null section](settings-null-sections.md), matching native storage behavior on Linux and Mac.
- v0.8.21 [reduces Unicode validation work in session recall](recall-unicode-work.md), preserving returned content and malformed-data recovery.
- v0.8.20 [reports missing worker skills as actionable failures](missing-skill-worker-results.md), settling known setup failures without a model request.
- v0.8.19 [stops workers after scheduling and revision handoffs](scheduled-review-handoffs.md), preserving native landing states and avoiding a follow-up model request.
- v0.8.18 [loads only returned adaptive recall payloads](adaptive-recall-hydration.md), with byte-identical answers and fewer message bodies materialized.
- v0.8.17 [stops workers after a verified blocked handoff](blocked-worker-handoff.md), preserving the hold and saving one request in a bounded two-stage card test.
- v0.8.16 [preserves ordered config type changes](settings-null-sections.md#ordered-type-changes-v0816), avoiding stale fields when two writes cannot safely be combined.
- v0.8.42 [starts a /goal turn with its contract and evidence rule](live-captain-cards-20261109.md#after-the-owner-raised-the-ceiling-to-48), so a finished card is not sent back for one more turn for lack of evidence.
- v0.8.41 records [live Captain card evidence](live-captain-cards-20261109.md): an owner `/goal` set the goal, and the Captain chose a wording, commented and completed the card. The judge verdict is still pending quota.
- v0.8.39 [shows a running subagent's tool and step in the TUI agents panel](chat-rendering-surfaces.md#tui-agents-panel-shows-what-a-subagent-is-doing-v0839), matching the Desktop bot row.
- v0.8.38 [renders tables on the web dashboard and tells the TUI model not to send diagram fences](chat-rendering-surfaces.md).
- v0.8.37 [reuses the goal-judge verdict for an identical input](goal-judge-memo.md), so a repeated response costs no second judge call.
- v0.8.35–v0.8.36 [make retention actually run](storage-and-backups.md#retention-that-can-actually-run-v0835) on hosts with SSH, user systemd or a VPN agent; Linux Hermes home 43 GB to 33 GB, Mac 11 GB to 8.6 GB.
- v0.8.12 [preserves settings edits across navigation, reload and close](settings-autosave.md), with installed Linux acceptance and matching Linux/Mac source.
- v0.8.11 [names shared settings controls for assistive navigation](settings-accessibility.md), with installed Linux save/readback acceptance and native Linux/Mac packages.
- v0.8.9 [forwards worker progress through the unified Gateway roster](unified-worker-progress.md), with isolated real-card acceptance.
- v0.8.8 [bounds retained token-estimate memo memory](token-memo-memory.md), preserving estimates and normal cache reuse.
- v0.8.6 separates [vision caches by the active or saved connection](vision-cache-routes.md), preventing stale answers after an endpoint or connection-mode change.
- v0.8.5 keeps [worker progress readable in narrow rows](worker-monitor-readability.md), including long tool names and a complete hover summary.
- v0.8.4 [bounds retained search cache memory](search-cache-memory.md), preserving disk reuse and releasing expired payloads on lookup.
- v0.8.3 [attributes post-turn goal judges to their owning sessions](goal-usage-accounting.md), retaining cache/reasoning usage and concurrent-profile isolation without adding requests.
- v0.8.2 repairs retention guards and verifies archived payloads before retiring source files. See [storage retention safeguards](storage-and-backups.md#retention-safeguards-v082).
- [Scheduled retention](storage-and-backups.md#age-out-disposable-data-on-a-schedule) for scratch, backups, side builds and reports, so a busy fleet does not fill the disk.
- The historical **582-path cumulative kit** remains available for its different pinned base. See [its inventory](../patches/manifest.json); do not stack it over the consolidated stable kit.
- An optional [cache-miss evidence repair for v0.22.5](cache-miss-evidence.md) stops attributing misses to expiry from idle time alone; it preserves historical metrics and request/cache policy.
- A [role-specific THINK/ACTION extension for upstream v0.22.5](stable-role-workflows.md) adds native bounded plans, pinned ACTION steps, independent review, re-planning and per-bot model/effort editing. It includes the runtime repairs as one alternative full patch; family labels do not prove provider readiness.
- A separate [nine-path runtime repair for upstream v0.22.5](stable-runtime-repair.md) preserves rotating Codex account headers and managed-worker wire modes, and keeps routine confirmations from blocking dialogs. Its base differs from the cumulative kit. An exact upgrade from the earlier seven-path transport unit is included; do not stack full patches.
- Reuse a compatible, already published PM checker across launcher scopes without dependency preparation or changing the selected environment. See [startup cache behavior](installation-and-rollback.md#startup-checker-cache).
- Native current-work Kanban with separate bounded history, integrated sidebar ownership and corrected Models/Usage destinations.
- Full native saved-chat/project managers, bot/group/section actions, an always-visible device/profile/status bar, and pane/status plugin discovery. See [feature parity](desktop-feature-parity.md).
- [Shared prompt guidance](shared-prompt-prefix.md) for new builds, with byte-preserving restoration of prior layouts.
- [Optional prompt-cache TTL policy](prompt-cache-policy.md) with an isolated native config recipe and a minimal merge fragment.
- Resilient saved-chat search, whitespace-tolerant bot/Hub queries, local Hub type filters and explicit member-catalog loading/retry.
- [Usability repairs](desktop-usability.md): full-history search handoff, file-preview Back/history, fit/focus Workflow, searchable goal skills, honest Hub search and explicit bot introductions.
- Native **Focus / Workspace** navigation, a revision-bound Goal form and evidence-based Catch up. See the [Desktop interface guide](focus-workspace.md).
- Native task/run ownership checks; exactly-once dispatch; input preflight; recoverable compact handoffs; worker completion that avoids a needless follow-up model turn.
- Bounded file/status reads, cache diagnostics, task/run usage attribution, waiting without repeated model calls, and worker phase timing.
- Coalesce concurrent model-catalog reads within a profile and credential scope; bound retained catalogs and preserve explicit refresh.
- Keep provider-confirmed context windows and local probes tied to their credential and home; serialize durable window updates.
- Metadata-only session bindings, native search identity reads, notification destination checks and MRU/export preflight selection avoid hydrating full prompt and tool context for small runtime values. See [measurement and limits](session-metadata-reads.md).
- Chunk JSONL file exports through native staging to avoid a whole serialized backup copy, while keeping hard-link and special-file behavior. See [export limits](session-metadata-reads.md#chunked-jsonl-export-v0611).
- Recognize the GPT-6.1 Terra Codex reasoning vocabulary, including its supported max effort.
- Select and inspect reasoning effort for individual Kanban tasks, without changing a profile's default.
- Stop verified completed workers at budget checkpoints without an extra model call.
- Continue bounded usage reports when a log rotates during file selection.
- Include explicitly selected additional Kanban databases in read-only usage attribution.
- Set per-task reasoning effort when creating cards through the native Kanban CLI.
- Report privacy-preserving cross-profile cache cohorts from existing bounded diagnostics.
- Keep verified live goal waits parked and pause unverified waits without another model turn.
- Preserve older recovery snapshots when a critical file is skipped or cannot be captured.
- Keep active task claims and explicit holds safe during autonomous reassignment.
- Show routine task status without waking an assistant; retain actionable handoffs.
- Prevent concurrent duplicate task creation for the same idempotency key.
- Respect emergency stop and shared capacity across dispatch entry points.
- Keep new work paused when the emergency-stop sentinel cannot be inspected.
- Report unconfirmed pause and resume operations truthfully.
- Honor global pause from every profile in the same fleet.
- Keep linked emergency stops active without overwriting their targets.
- Check fresh bot availability in the owning fleet when reassigning.
- Resolve session links within the caller fleet and reject conflicting profiles.
- Preserve the originating profile when generating session links.
- Search within a specific session to recover compacted context.
- Keep slow-search telemetry useful without recording the search text.
- Bound full-text search snippets while retaining a genuine match highlight.
- Use a healthy existing CJK index for read-only cross-profile session search.
- Discover structured text and encoded tool arguments with bounded, source-linked excerpts.
- Keep repeated history scans from retaining per-row native Blob bookkeeping.
- Preserve quoted phrases and Latin prefix searches through indexed search fallbacks.
- Search text in multimodal messages and page matching tool arguments without loading image payloads into the result.
- Recover large history messages in bounded pages that respect visibility and profile boundaries.
- Keep demoted tool results recoverable through compaction.
- Restore an older session outside the loaded sidebar page when its owner is verified, without discarding uncertain remembered navigation.
- [Bounded conversation title recall](session-recall.md) preserves orientation evidence while avoiding full-transcript reads and applying metadata exclusions before payload reads.
- Reuse of unchanged bundled locale parses across profiles, with independent mutable catalogs and private overlays. Local counters make this reuse observable without reading translations.
- Reuse of immutable bundled plugin code across profile namespaces, preserving separate module globals, private-plugin imports and native activation gates.
- Icon-led bot activity with bounded worker details, terminal/offline fences and compression-tip metadata that follows the displayed session. See [bot activity](bot-activity.md).
- Fifteen renamed role templates and twelve reusable English skills. They contain no account configuration, credentials, personal persona or production transcripts.

Read the [feature catalog](features.md), [role guide](bot-roles.md), and [verification record](verification.md). Use the [deployment acceptance checklist](acceptance-checklist.md) to distinguish installed code, runtime adoption and measured workload results. A feature's inclusion does not establish a live performance saving for your workload.

Use [native goals, skills and delegated decisions](goals-and-delegated-decisions.md) to let a Captain carry an authorized objective through verification within current quotas and approval gates.

Use the [storage and backup guide](storage-and-backups.md) to avoid redundant full backups and review the offline helper for compacting explicitly selected older standalone snapshots.

Review the [optional external-memory pilot guide](external-memory-pilot.md) before adding capture hooks or another memory service. It separates project isolation, automatic imports, authentication and evidence from installing or expanding an integration.

## Try the offline examples from a public download

Clone the release and run from its repository root; the same commands work after extracting the release archive and entering its top-level directory. Only Python and Git are needed for this companion-only walkthrough. Native profile setup has the additional upstream prerequisites documented separately.

```sh
git clone --branch v0.9.0 --single-branch https://github.com/ap08960695/hermes-legion.git
cd hermes-legion
python3 scripts/verify_release.py
python3 scripts/legion_plan.py --team examples/team.full.json --snapshot examples/snapshots/synthetic-ready.json --tasks examples/scenarios/parallel-production.json --now 1
```

The walkthrough pins v0.9.0. The consolidated stable kit is an alternative to the historical cumulative patch and the smaller stable units; select exactly one matching manifest. Source application, a running application, original-session adoption and measured workload improvements remain separate evidence. See the [verification record](verification.md).

For an existing Mac, follow the [isolated source installation and update guide](macos-install-update.md). It keeps native CLI, Desktop packaging and production activation evidence separate.

Use [on-demand memory diagnostics](runtime-memory-diagnostics.md) to distinguish process memory from native cache counts without reading conversations or starting inference. Optional allocation tracing is disabled by default and belongs in an idle maintenance window.

## Prepare and diagnose a team offline

Use the [doctor and setup bundle guide](offline-setup-tools.md) to inspect placeholders, preview a new-file diff and export config/SOUL into a fresh private directory. Nothing is installed or authenticated. The starter team and model map below are synthetic; model availability and runtime readiness remain unknown.

```sh
python3 scripts/legion_setup.py --team examples/team.small.json --models examples/models.small.synthetic.json
python3 scripts/legion_plan.py --team examples/team.full.json --snapshot examples/snapshots/synthetic-codex-cooldown.json --tasks examples/scenarios/sticky-session.json --pins examples/session-pins.synthetic.json --now 1 --explain
```

See [idle-only Gateway updates](idle-updates.md) for the native opt-in request that refuses live or unreadable background work without forcing a restart.

## Start safely

1. Use an **isolated checkout**, not the installation currently running your work.
2. Follow [installation and rollback](installation-and-rollback.md). Compatibility is deliberately narrow; mismatched source must fail rather than be force-patched.
3. Review the role templates and use only accounts and provider lanes you already have permission to use. Templates are reference material, not an automatic account/profile installer.
4. Keep your existing quotas, approvals, ownership and publication gates. Paid fallback is disabled by policy, not supplied as a hidden recovery route.

No model call, account login, live session resume, service restart, dependency installation or user configuration change is performed by this repository's verification scripts.

## A Captain-led team, not just role names

The [full team example](../examples/team.full.json) describes **34 profiles**: Captain/planner, native-provider twins for thirteen specialist families, and six purpose-specific Web bots. Code, analysis, research, review, testing, documents, media, voice preparation, operations and maintenance have distinct responsibilities. No private bot names, accounts, avatars or persona files are copied.

- [Team and workflow](team-workflow.md) · [complete role roster](bot-roles.md)
- [Multiple accounts and native pool ownership](multi-account.md)
- [Manual native setup with config fragments](setup-multi-account.md)
- [Session stability and shared quota](shared-quota.md)
- [Offline routing dry-run](offline-planner.md)

```sh
python3 scripts/legion_plan.py --team examples/team.full.json \
  --snapshot examples/snapshots/synthetic-ready.json \
  --tasks examples/scenarios/parallel-production.json --now 1
```

The dry-run makes no model request or live change. Synthetic examples do not certify runtime routing: actual account selection, quotas, ownership and dispatch remain native. The patch itself remains the same pinned compatibility unit.

## Privacy and licensing

This repository contains generic source changes and synthetic examples. Live databases, conversations, logs, account inventories, secret stores and private Git history are excluded. See [security policy](../SECURITY.md), [privacy review process](privacy-review.md), and [third-party notices](../THIRD_PARTY_NOTICES.md).

MIT licensed. Preserve the upstream copyright notice when redistributing included Hermes code. This project does not grant permission to bypass a provider's terms or limits.

Native UI guides: [Hub and shared collections](shared-spaces.md), [Rich answers](rich-answers.md), and [Focus and Workflow](focus-workspace.md).

Hosted Group Chats now keep empty profiles thread-free behind the native ready gate. See [idle hosted rooms](hosted-room-idle.md) for discovery, stop fencing and measured limits.

Repeated plugin manifest reads now reuse the native YAML file cache while each caller keeps private mutable metadata. See [manifest metadata reuse](plugin-manifest-cache.md) for validation and measured limits.

Cold profile SQLite opens now run off the event loop with native cancellation and shutdown custody. See [profile startup I/O](profile-startup-io.md) for verification; the former standby/control issue is resolved in [ready standby group controls](standby-group-controls.md).

Ready standby coordinators now accept canonical group creation and messages through their native owner without allocating idle supervisor threads. See [standby group controls](standby-group-controls.md).

Fresh SQLite schema declarations now commit atomically with less initialization overhead; existing stores retain their native reconciliation path. See [fresh schema startup](fresh-schema-startup.md) for measurements and limits.

Profile initialization now retains physical database-write custody through cancellation and native shutdown. See [profile bootstrap custody](profile-bootstrap-custody.md) for behavior and verification limits.

Additional direct session-authority callers now have host-independent offline fixtures. See [authority caller verification](authority-caller-verification.md) for the baseline classification and final selection.

Config metadata I/O failures now retain native last-good owner settings, including effort ceilings. See [config metadata recovery](config-metadata-recovery.md) for behavior and limits.

Config backups now publish complete generations with collision-free names and fresh rotation after concurrent copies. See [config backup publication](config-backup-publication.md).

Good config backups now preserve the exact generation a native reader parsed, preventing later concurrent edits from being mislabeled as validated. See [validated config snapshots](config-backup-snapshot.md).

Completed profile retirement now releases only its old config cache entries while parked homes and unfinished writers retain recovery state. See [profile config cache retirement](profile-config-cache-retirement.md).

MCP schema-cache publishers now retain peer server entries across concurrent processes. See [concurrent MCP schema publication](mcp-schema-publication.md).

Auxiliary Codex requests preserve selected reasoning effort and owner ceilings through SDK serialization. See [auxiliary effort fidelity](auxiliary-codex-effort.md).

Known mandatory native auxiliary models now start at their cheap supported floor. See [native auxiliary floor](native-auxiliary-reasoning-floor.md).

Managed workers now pin their owning source after environment sanitization. See [managed-worker source pinning](managed-worker-source-pinning.md).

Inspect saved role pairs and dispatch policy with one [native routing snapshot](profile-routing-snapshot.md), without a model call.

A [bounded real-provider parallel case](parallel-native-acceptance.md) completed with native THINK/ACTION binding, independent review and measured request overlap. The report distinguishes this result from production adoption or measured savings.

[Async auxiliary retries](async-auxiliary-retries.md) now respect the configured zero budget while keeping the existing one-retry ceiling.

[Cross-board goal waiting](goal-kanban-awareness.md) counts followed work through read-only native SQLite probes while retaining worker board fences.

[Gateway goal destination identity](goal-notification-identity.md) keeps history IDs separate from the platform/chat/thread/profile that subscribed to work.

[Resume goal decisions after completed card-result turns](goal-result-waits.md) without waking a model from passive polls or overriding explicit waits.

[Local result wakes use their owning Gateway](local-result-wake.md), preserving the native FIFO and queued human input.
