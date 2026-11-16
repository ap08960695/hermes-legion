# Consolidated stable source and Desktop kit

This is the complete **1097-path** Legion source, interface and optimization alternative
for upstream Hermes **v0.22.5**, commit
`bf0203a794a07aac3ff764972ab9087baa4e4f4e`. It replaces the need to assemble the
historical cumulative kit and the smaller stable units. It is not an upstream release,
an account installer, a prebuilt application or an in-place migration script.

The [manifest](../patches/stable-full/manifest.json) pins every before/after file hash.
The [test selection](../patches/stable-full/test-selection.json) records the offline
Python and Desktop selection. No dependency or lockfile change is included.

## Recorded task reports (unreleased)

Monitor bot rows offer Recent reports: recorded task outcomes, report/error
excerpts, completion time and local outcome filters. The last recorded issue is
separate from current work. Stopped and Unknown remain distinct; only the
backend's recorded progress-detector result is labelled stalled. A historical
failure or stalled report never makes the bot currently blocked or Working.

One read-only helper uses the existing preferred Bot Chat compression chain and
roster cache, excluding side-chats/forks/other profiles. Twenty ledger rows and
20 emitted tasks are global bounds per canonical chat. JSON reads are bounded
before decoding, existing forced redaction precedes text cuts, and only declared
snapshot fields leave the helper. Vault-value scrubbing binds the store's own
home and restores the caller context, including for sibling-profile reads. Missing/unreadable reports stay unavailable;
empty/partial history never proves no failures. The local dialog renders escaped
text and never activates a source or opens a chat. Canonical Open chat is unchanged.

Twelve changed sections roundtrip;1097targets, unrelated patch sections exact.
One new Python test appends, prior selection order/metadata retained.36focused
Python and50UIcases pass, plus scoped lint/types/build/generated/health checks.
No new provider/request/poll/timer/dependency/schema/control. This is unreleased
source work; native layout/lifecycle acceptance and one feature batch follow.
[Design](design-bot-monitor.md#recorded-task-reports-slice).

## Canonical bot usage (unreleased)

Bot rows show recorded tokens, estimates, provider-reported amounts and model
from their named Bot Chat's resolved row. Configured model stays separately
labelled. Worker values remain separate, and token sorting uses the same source
as the displayed values. Missing usage stays unavailable; zero stays zero.
These are stored row values, not lifetime totals, worker sums or a current model
binding. Elapsed/tool/step remain worker-only.

The existing shared row projection and scoped canonical readers supply five
optional fields without new queries, providers, timers or storage changes.
Eleven changed sections roundtrip against the pinned base; unrelated sections
are retained. The kit now has 1094 targets and appends one Python regression,
keeping prior test selection metadata and order. Forty-eight focused Python
and 45 UI cases pass. Native acceptance remains blocked under unchanged capture
conditions; no new trial or release is claimed.
[Design and limits](design-bot-monitor.md#canonical-bot-usage-slice).

## Recorded Monitor usage (unreleased)

Worker rows show recorded USD estimates and provider-reported amounts separately,
with a persistent partial-coverage/not-invoice hint. Positive recorded amounts
survive unknown/included latest pricing; storage-default zero stays unavailable
unless the corresponding pricing status supports a recorded zero. The model
column distinguishes stored worker routes from configured bot models. Missing,
negative and nonfinite amounts stay unavailable; positive sub-cent amounts never
round to zero. No new query/provider call, polling, storage or dependency.

The existing shared row projection reaches both legacy and unified roster reads;
optional wire fields and generated TypeScript/OpenRPC artifacts agree, including
already-declared parallel observations. Twelve changed source/test sections,
1093 targets; two Python regressions append to the existing selection. This is
unreleased source work toward the same Monitor batch, with no runtime version
bump or daily-app adoption. [Design and limits](design-bot-monitor.md#recorded-worker-usage-slice).

## Bot Monitor dashboard (unreleased)

Bots → Monitor gathers the current roster and bounded worker observations into a
single table, with local search, status filters and Name/Elapsed/Tokens sorting.
Only explicit Open chat actions use the existing source-qualified bot route.
Reported task, tool, step, elapsed and token facts remain distinct from missing
metrics; cost is unavailable and the model column names the configured bot route.
Cards and Manage team remain accessible. No new API, polling, storage key or
dependency is introduced. Seven source/test sections change, including three new
files: 1091 targets. The Desktop selection appends the rendered Monitor regression
while retaining prior entries and metadata. This is development work toward one
feature batch, with no runtime version bump or daily-app adoption.
[Design, scope and remaining acceptance](design-bot-monitor.md).

## Keep the attachment size draft (v0.33.8)

The device-wide preview/image limit blurs on non-composing Escape before the
Settings overlay closes, reusing its existing normalization and IPC commit.
No cleanup save, propagation change, API, schema or dependency is added. Two
existing source/test sections change; 1088 targets and test selection remain.
Apply the kit and rebuild Desktop. [Checks and native limits](release-notes-v0.33.8.md).

## Confirm group membership saves (v0.33.7)

Per-Bot Manage groups consumes the existing save outcome, serializes its three
mutation controls and retains an explicit failure with a captured-action Retry.
Local fallback and room records remain; no backend/API/schema or polling change.
The existing message contract and nine catalogs include conditional sync copy and
failure guidance. Five changed source/test sections, 1088 targets and one Desktop
test addition; prior selection metadata/order retained. Apply the kit and rebuild
Desktop. [Checks and native limits](release-notes-v0.33.7.md).

## Compact work names (v0.33.6)

BotRow's shared accessible name/name tooltip uses the existing translated Working
label for an available, non-idle bot mood; other source labels remain. Activity
eligibility, canonical chat identity, previews, polling and backend lifecycle are
unchanged. Two existing source/test sections change; 1086 targets and selection
remain. Apply the kit and rebuild Desktop. [Checks and limits](release-notes-v0.33.6.md).

## List drafts survive Escape (v0.33.5)

Shared ListField handles a non-composing Escape through the existing synchronous
blur/parse/commit path before the overlay closes. Enter, draft-only typing,
parsing and unrelated unmounts retain their behavior. No writer, schema, API,
locale or dependency change. Apply the kit and rebuild Desktop. Two existing
sections change; 1086 targets and selection remain.
[Checks and native limits](release-notes-v0.33.5.md).

## Fractional compression stepping (v0.33.4)

One shared ConfigField input attribute gives the two known compression-ratio
fields a 0.01 step. Other numeric fields retain native unit stepping. No schema,
backend, conversion, dependency or locale changes. Apply the source kit and
rebuild Desktop. Two existing source/test sections change; 1086 targets and the
explicit test selection stay unchanged. [Checks and limits](release-notes-v0.33.4.md).

## Scoped Settings actions (v0.33.3)

Export and Reset capture the selected config owner before awaiting reads or
confirmation. The defaults helper accepts an optional existing request scope;
its no-argument callers keep ambient behavior and read-origin binding. Reset
names the captured profile and requires a successful acknowledgement. Apply the
kit and rebuild Desktop. Four source/test sections change, including one existing
upstream route-binding regression newly included in the kit: 1086 targets. The
Desktop selection adds that test. [Checks and limits](release-notes-v0.33.3.md).

## Complete partial-import drafts (v0.33.2)

Import uses the house merge to preserve untouched displayed values, including
after an identical import. Existing version/generation counters discard stale
file reads after an edit or unmount. The shared native writer is unchanged.
Apply the kit and rebuild Desktop. Two existing source/test sections change;
1085 targets and test selection remain. Native Local same-page imports, next
edit, sparse disk readback and reopen pass.
[Checks and limits](release-notes-v0.33.2.md).

## Acknowledged Settings imports (v0.33.1)

The shared config editor returns its existing current save acknowledgement;
Import waits before announcing success. Cancelled, failed and superseded imports
cannot report success, and non-object JSON cannot submit write intent. Apply the
kit and rebuild Desktop. Two existing source/test sections change; 1085 targets
and test selection remain unchanged. Native Local cancellation, real permission
refusal, retry and reopen passed. [Checks and limits](release-notes-v0.33.1.md).

## Parallel observed bot work (v0.33.0)

Full Bots cards list bounded worker observations with their own titles/activity/
progress. Compact rows add a count for multiple workers. One eligibility rule
keeps counts, stamps and Working status consistent after an individual stop.
The existing cached roster read adds an optional list while retaining singular
compatibility and separate conversation previews. Apply the kit to the gateway
and Desktop, restart the updated gateway, and rebuild Desktop. Twelve existing
sections change; 1085 targets and test selection remain. Native Local two-to-one-
to-none monitoring passes. [Checks and limits](release-notes-v0.33.0.md).

## Readable chat charts (v0.32.0)

Chart fences reuse the house full-view pan/zoom controls and offer an on-demand
Details table from the same validated spec. Full labels and unrounded parsed
values remain available even when dense axes omit category ticks. The shared
viewer registers its opening button with the Dialog root for focus restoration.
Four existing source/test sections change; 1085 targets and the test selection
stay unchanged. Apply the kit and rebuild Desktop.
[Adoption, checks and limits](release-notes-v0.32.0.md).

## Separate same-goal delegation cards (v0.31.1)

Chat cards use the native receipt's existing child IDs before any legacy match.
Two same-name calls keep their own progress and outcome; an unresolved advertised
identity never claims a different worker. Older no-ID receipts retain the old
fallback. Apply the source kit and rebuild Desktop. Three existing source/test
sections change; 1085 targets and the explicit test selection stay unchanged.
Scoped apply/hash/reverse and native Local before/after acceptance pass.
[Checks and limits](release-notes-v0.31.1.md).

## Local group naming workflow (v0.31.0)

The canonical room has a capability-gated Rename dialog using the existing
owning gateway. Confirmation keeps the room ID and members, retains the unsent
message, and updates its header and open tab without remounting the workspace.
Earlier create/cancel/reopen behavior joins the same checked Local workflow.
Seven changed source/test sections include five newly carried upstream paths,
for 1085 targets; one regression joins the Desktop selection. No membership API,
backend migration or model request is added. Rebuild Desktop including the SDK.
[Adoption, checks and limits](release-notes-v0.31.0.md).

## Live background report refresh (v0.30.2)

Desktop recognizes a native completion turn as backend-originated, so its existing
bounded post-reply history refresh loads the saved report without Reload. Stop
clears that adoption flag. Ordinary turns retain their read behavior. Apply the
source kit and rebuild Desktop. Four source/test sections change, adding three
existing upstream paths for 1080 total; one Desktop regression file joins the
explicit selection. [Adoption, evidence and limits](release-notes-v0.30.2.md).

## Clean background reports (v0.30.1)

The renderer removes canonical terminal gateway provenance before splitting a
saved background report. This repairs transcript-tail cleanup and process wrapper
closing without changing stored/model content or per-task outcome metadata.
Apply the source kit and rebuild Desktop. Two existing patch sections change;
1077 targets and the explicit test selection are retained. Only those changed
sections were checked. [Checks and adoption](release-notes-v0.30.1.md).

## Retained child outcome details (v0.30.0)

Saved batch completions now carry per-task outcome/name pairs. After Reload,
expand the compact summary to read them beside the existing report; collapse
and reopen it, including when the report has no output. Adopt the backend source
and rebuild Desktop. Older payloads retain their fallback and original dispatch
cards remain parked. [Adoption and limits](release-notes-v0.30.0.md).
Seven existing upstream source/test files join the patch: 1077 paths. Only those
sections were checked against the pinned base with apply/hash/reverse. One Python
and two Desktop files join the explicit test selection. No dependency or schema
change; the model's notification content is unchanged.

## Stopped delegation cards (v0.29.5)

An explicit interrupted child shows Response stopped with a neutral stop icon
rather than Error. The card preserves partial output and distinguishes real
failures/completions. Apply the source kit and rebuild Desktop. Native Local
composer Stop A / keep B running, late-reply rejection and parent delivery were
checked before/after. [Adoption and history limits](release-notes-v0.29.5.md).
Four existing upstream source/test files join the patch: 1070 paths. Their
scoped apply/hash/reverse proof passes; unrelated sections are retained. Two
Desktop test files join the explicit selection. No backend/dependency change.

## Activity on bot cards (v0.29.0)

Cards reuse the compact roster's activity description and reported tool, step,
elapsed time and token facts. Canonical preview and chat navigation stay separate.
Controlled native records verified wide/narrow display and hiding after a record
ended and Refresh was clicked. This does not prove actual worker lifecycle.
[Adoption, checks and limits](release-notes-v0.29.0.md). Two existing source/test
sections change; the kit remains 1064 paths, with unrelated sections retained.

## Readable bot card status (v0.28.1)

A layout fix gives the existing status a full row above the card actions.
Native Mac before/after images show the inactive status fits instead of
splitting into four lines; a narrow-window check also passes.
[Adoption, checks and limits](release-notes-v0.28.1.md). One existing source
section changes; the kit remains 1064 paths and unrelated sections are retained.
Bot monitoring and the full Config/Bots/Chat walkthrough remain incomplete.

## Settings actions keep your place (v0.28.0)

The grouped Settings capability adds named Actions, keyboard continuation after
Reset Cancel, and first-visit Local draft preservation. The corrected renderer
passed native Mac acceptance with isolated data in wide and narrow windows.
[Behavior, adoption and limits](release-notes-v0.28.0.md). Nine source/test targets
change from v0.27.0, including six added kit paths; unrelated patch sections are
retained. The changed sections apply, match their hashes and reverse to the
pinned base. Rebuild Desktop to adopt; older differently owned drafts are not
migrated. Remote transport policy is unchanged and no other host was contacted.

## On-demand host facts (v0.27.0)

Nonpositive gateway startup warmup now defers eager host toolchain probing;
first local use retains facts and cache. Positive policy starts only after PID
admission and logging. [Behavior, native ABBA measurements and tradeoff](release-notes-v0.27.0.md).
One prior runtime target changes; a native regression and configuration guide
join the kit. All 1,055 unrelated targets, including P0 transport protections,
remain exact. Five unused boot commands disappear; RAM saving is not established.

## Local startup keeps saved remotes on demand (v0.26.0)

Passive roster enumeration and Bot Relay no longer initialize unused SSH, URL
or cloud connections on a cold Local launch. Cached rows and SSH seed routes
remain; explicit remote selection, Test, updates and actual queued-message
delivery retain their existing dialing paths. [Behavior, isolated native Mac
launch proof and limits](release-notes-v0.26.0.md). Six existing upstream files
join the kit, four prior targets change and all 1,046 unrelated targets remain
exact. Rebuild Desktop to adopt it. This does not close existing authorized
remote work or certify the separate Config/Bots/Chat screen walkthrough.

## Bounded fresh backend checks (v0.25.0)

Import/version probes share default-one/configurable-two admission, a 256-job
FIFO and an initial 512 MiB observation gate. Admitted callers execute fresh;
full cold-start budgets and one existing timeout retry remain. [Behavior,
controlled native memory measurements and limits](release-notes-v0.25.0.md).
Three prior targets change and two join; all 1,045 unrelated targets remain exact.
Main changes only launch-policy wiring; P0 SSH behavior remains. Adoption needs a
Desktop rebuild; arbitrary wrapper descendants and other helpers are not capped.

## Bounded Desktop ticket backlogs (v0.24.0)

Busy cached helpers now send one unanswered ticket frame at a time and share the
existing 256-job FIFO. Fresh grants, deadlines, reset and actual-close ownership
remain. [Behavior, native Mac parity/overload evidence and limits](release-notes-v0.24.0.md).
Three existing targets change; all 1,045 unrelated targets and P0 remain exact.
Measured RSS is essentially unchanged; no new setting or dependency is added.

## Source-check memory admission (v0.23.0)

The existing Desktop source-check queue waits for at least 512 MiB observed
execution-host availability before starting Python. Memory waiting consumes the
six-minute active budget; force/channel ordering and per-caller parsing remain.
[Behavior, controlled native overlap measurements and limits](release-notes-v0.23.0.md).
Three prior targets change and two upstream test files join; all 1,043 unrelated
prior targets and P0 remain exact. No new setting, dependency or pre-started pool.

## Shared Desktop runtime-lookup admission (v0.22.0)

Installation-launcher lookups share the existing ticket-helper slots, FIFO and
memory gate. Reset stops obsolete lookups; capacity returns only on actual close.
[Behavior, controlled native measurements and limits](release-notes-v0.22.0.md).
Three prior targets change and two existing upstream test files join the kit;
all 1,041 unrelated prior targets and P0 remain exact.
No new setting or dependency; installed Desktop adoption requires rebuilding.

## Bounded idle cache cleanup (v0.21.0)

Idle sweeps submit one cleanup job per runner to the existing housekeeping
executor. Waiting agents stay cached and are checked before each claim; native
profile, persistence and shutdown protections remain. [Behavior, measurements
and limits](release-notes-v0.21.0.md). Four existing targets change and two join
the kit; all 1,038 unrelated prior targets and P0 remain exact. RSS is essentially
unchanged in the controlled native case; this is a concurrency bound.

## On-demand dashboard loading (v0.20.0)

`gateway.dashboard_warmup: false` skips optional post-READY dashboard warmup,
using the existing lazy first-request mount. Default warmup and auth-required
preload remain intact. [Native canonical startup measurements and first-use
tradeoff](release-notes-v0.20.0.md). Two existing targets change and four join
the kit; all 1,036 unrelated prior targets and P0 protection remain exact.

## Gateway memory diagnostics (v0.19.0)

`hermes gateway memory` exposes the existing private local diagnostic in one
command. A platform-owned, on-demand current-RSS fallback supplies Mac readings
without changing pressure admission or trimming. [Usage and measured component
behavior](release-notes-v0.19.0.md). One existing target changes and eight join
the kit; all unrelated prior targets and P0 Desktop protection remain exact.
No production RAM saving, whole-gateway or installed-app acceptance is claimed.

## On-demand gateway preset (v0.18.0)

The companion adds an [optional native preset and application recipe](on-demand-gateway.md)
for existing warmup, cached MCP lazy startup and bounded discovery controls, with
an executable native consumer/first-turn fixture. [Measured behavior and limits](release-notes-v0.18.0.md).
No native runtime payload changes: the patch and 1,030 target hashes remain exact,
including P0. This does not automatically change installed profiles or enable
idle retirement for stateful servers.

## Profile MCP idle defaults (v0.17.0)

An opt-in profile timeout supplies existing idle retirement to eligible stdio
servers. Explicit server policies win; HTTP/events receive no inherited timeout.
Pair with cached lazy startup only for servers whose state may be discarded.
[Behavior, native idle measurements and restart tradeoffs](release-notes-v0.17.0.md).
Five existing default/loader/test/doc targets change; the kit stays at 1,030
targets. P0 SSH protection and all unrelated targets remain exact. Whole-gateway
idle RAM and daily-app adoption remain separate acceptance items.

## Ticket-helper memory admission (v0.16.0)

New Desktop ticket helpers wait below 512 MiB observed execution-host availability
or on unknown observations, within the existing mint deadline. One bounded poll
runs only for memory-blocked admissions with capacity. Existing helper reuse,
FIFO, reset and actual-close slot accounting stay intact. [Behavior, native
controlled-overlap measurements and limits](release-notes-v0.16.0.md). Three
existing source/test/doc targets change; the kit remains at 1,030 targets.

## On-demand ticket helpers (v0.15.0)

Desktop starts one Python ticket helper at a time by default and retires unused
helpers after five seconds. Both limits are launch-configurable; exact profile
and runtime isolation and fresh native grants remain intact. Waiting admissions
are bounded and share one mint deadline. [Behavior, measured native case and
limits](release-notes-v0.15.0.md). Three runtime paths, one new behavior test and
the native Desktop guide change; four targets are added to the cumulative kit.
This is not whole-gateway or OS-wide memory admission.

## Shared source-update checks (v0.14.0)

Adjacent identical ordinary Desktop source checks share one running native
process. Distinct requests serialize across installations; force and channel
changes remain independent ordering barriers. Caller results are parsed
separately, and completed results are not retained. [Behavior, measured native
case and limits](release-notes-v0.14.0.md). One production target changes and one
colocated behavior test is added; launcher recovery and P0 SSH paths are unchanged.

## Memory-aware Desktop checks (v0.13.0)

POSIX guarded commands wait for at least 512 MiB of observed execution-host
memory before starting a helper. Unknown observations wait within the existing
deadline; cancellation prevents a late launch. The prior one-slot fan-out and
transport policies stay intact. [Behavior, measured modeled-pressure case and
limits](release-notes-v0.13.0.md). Five existing source/test targets change; no
new runtime target, setting, dependency or installed-app change is included.

## On-demand MCP startup (v0.10.0)

`mcp.memory_saving: true` defaults configured stdio servers to lazy startup when
valid schemas are cached. Explicit server settings, HTTP/events and stateful
sessions retain their policy; idle teardown remains a per-server opt-in.
Concurrent first calls join one handshake. SDK model defaults no longer create
an invented zero cache TTL. [Configuration, measured phases and limits](release-notes-v0.10.0.md).

Six targets join the previous 1,013; the existing config-defaults target also
changes. No dependency/lockfile or installed-app change is included. Broader
MCP scale-to-zero and gateway idle-memory acceptance remain open.

## Bounded Desktop SSH checks (v0.9.0)

Compatible profiles now share one process-owned transport. Programmatic probes
and payloads queue, remote kernel admission survives client loss until cleanup,
and missing mux sockets cannot silently dial another connection. POSIX helper
groups are reaped; detached serves keep a separate session on Darwin as well.
[Behavior, measured memory/latency and platform boundaries](desktop-ssh-resources.md).
[Plain-language release notes and grouped v0.8.46–.73 changes](release-notes-v0.9.0.md).

Nine targets join the previous 1,004: five existing upstream files and four new
runtime/test files. The existing Desktop main target also changes. No dependency
or lockfile changes. This is a source kit, not an installed/rebuilt Mac app.
Gateway idle memory, MCP lifecycle, Windows remote cleanup and the UI walkthrough
remain separate acceptance work.

## Web-cache TTL conversion recovery (v0.8.76)

Unrepresentable integers in `web.cache_ttl_minutes` now use the existing20-minute
invalid-conversion default. The shared reader no longer aborts search or usable
extraction-cache hits with `OverflowError`. [Actual config, expiry and registry
proof](search-cache-memory.md#overflowing-ttl-configuration-v0876).
Representable values, strings, clamp behavior and every cache/provider control
remain. Same1004 targets/base/selection: only the existing runtime/disk-sharing test
after hashes/sections change. No new dependency, config, range, fallback or cache.

## Request-cache completion admission (v0.8.75)

The vision request cache now computes each owner's admission once before taking
its shared cache lock, then uses that decision for publication and logging.
[Native cross-thread progress, follower/error and registry proof](vision-cache-routes.md#request-cache-completion-admission-v0875).
Publication, policy, TTL, capacity, reservations, cancellation, native pixel bypass
and the separate inner payload budget remain. Same1004 targets/base/selection:
only the existing request-cache runtime/test after hashes and sections change.
No new public file, dependency, lock, config, cache layer or asynchronous offload.
Component measurements do not establish whole-tool latency or fewer model calls.

## Vision analysis byte budget (v0.8.74)

The auxiliary content cache now combines its existing count/TTL/LRU limits with a
32 MiB charged key/entry payload budget. Large results still return in full; an
oversized replacement removes only its own key. Other useful hits survive.
[Native boundaries, retention and put-cost measurements](vision-cache-routes.md#retained-analysis-byte-budget-v0874).
Same 1004 targets/base/selection: only the existing vision runtime and content-cache
regression after hashes/sections change. No public file, dependency, lock, schema
or configuration is added. Fewer retained hits can cause more later provider work;
this is a payload budget, not a process RSS or production saving guarantee.

## Gateway compression-tip liveness (v0.8.73)

The transcript rerouter now uses the existing metadata reader for its tip-liveness
check on the parent's proven owner handle. Resolution, closed-tip handling, token
flush and error propagation remain. [SQL, ownership and component measurement](session-metadata-reads.md#gateway-compression-tip-liveness-v0873).
Two existing upstream files join the patch with pinned before hashes: the runtime
and its existing regression file. All previous 1002 rows/sections stay exact;
three existing Gateway test files join the selection. No dependency, schema,
configuration, context cache, fallback or public file is added. Normal idle loading
and Linux adoption remain lead-owned; source hashes do not prove running adoption.

## Web index write admission (v0.8.72)

The optional extraction index now checks volume space after its existing trimming
and before the original atomic writer creates a temporary file. Escaped JSON ASCII
length conservatively budgets both native UTF-8 and lone-surrogate fallback, with
an observed 1 GiB reserve. Denial keeps prior index bytes and normal fresh results.
[Native boundary, serialization and caller checks](storage-and-backups.md#web-index-write-admission-v0872).
Same 1002 targets/base/selection; only the existing cache runtime and pressure-test
after hashes/sections change. Native atomic serialization/mode/fsync/replace, locks,
payload guards and cache policy remain. No hard quota, total-cache bound or prune.

## Web full-text write admission (v0.8.71)

Both extraction-cache payloads and full-text paging copies now check the containing
volume before overwriting. Admission counts final UTF-8 bytes, including the paging
cap suffix, and leaves an observed 1 GiB margin. Low or unknown space retains prior
files; the requested extraction still returns its fresh result with an accurate
storage-failure footer. [Native preservation and boundary proof](storage-and-backups.md#web-full-text-write-admission-v0871).
Same 1002 targets/base and selection: only two existing runtime after hashes and
the existing storage-pressure test after hash change. Generic spill semantics,
derived cache, JSON-index persistence and cache policy remain unchanged. This is
payload admission, not a quota, total-cache-size bound or automatic pruning.

## Oversized web-cache timestamps (v0.8.69)

Disposable search-cache metadata with an overflowing integer timestamp now causes
an ordinary miss, preserving the normal selected-provider path. Good entries,
keys, profile boundaries, TTL, flight locks and fallback policy remain. See
[registered search and disk-reuse proof](search-cache-memory.md#oversized-disk-timestamps-v0869).
The same 1002 targets remain: only the existing runtime and disk-sharing regression
after hashes change; every before hash, unrelated after hash and selection stays.

## Declared cache-scope identity (v0.8.67)

The shared identity read selects source, parent ID and marker configuration without
hydrating prompt/tool context. Direct token flushing, source/fork rules and the
receipt snapshot's connection, transaction and missing-row error remain intact.
See [native parity checks and measured component costs](session-metadata-reads.md#declared-cache-scope-identity-v0867).
Two existing upstream regression files join the patch, giving 1002 targets. Only
one previous runtime after hash changes; all previous 1000 before/other-after
hashes, pinned base and native selection bytes remain unchanged.

## Mixed-name MCP filter fingerprints (v0.8.66)

Cache fingerprints stringify include/exclude entries before sorting, matching
registration's existing name conversion. Mixed string/numeric filters no longer
interrupt lazy discovery. Existing all-string keys remain; older nonstring-only
keys can incur one ordinary cache miss. See [compatibility and native proof](mcp-schema-publication.md#mixed-name-filter-fingerprints-v0866).
One existing runtime after hash changes and an existing upstream regression file
becomes a patch target, giving 1000. All previous 999 before hashes and other
after hashes remain; pinned base and native test-selection bytes stay unchanged.

## Compression parent metadata (v0.8.64)

The shared compression-child gate uses the existing metadata reader when callable,
while receipt-local snapshots retain their existing reader and transaction. Child
fork/reset/delegate checks and failures keep their behavior. See [native proof and
measurement](session-metadata-reads.md#compression-parent-checks-v0864).
One existing runtime after hash changes; its existing upstream regression file is
added as a patch target, giving 999. The previous 998 before hashes and other after
hashes stay unchanged. Pinned base and native test-selection bytes remain.

## Case-alias profile links (v0.8.61)

Recall compares the validated named-profile directory with its context home using
filesystem identity, so native case aliases retain their canonical profile label.
See [registered-handler reopening checks](session-recall.md#case-alias-profile-links-v0861).
Only existing search runtime/link-regression after hashes change. All 998 targets,
before hashes, pinned base and native test-selection bytes remain.

## Nonfinite recall timestamps (v0.8.60)

The existing session-start conversion helper returns its None sentinel when a
nonfinite numeric value cannot become an integer. Title/scoped/message-page
recall can recover unfiltered history; existing metadata date bounds still reject
unknown starts. See [native persistence and filter checks](session-recall.md#nonfinite-session-start-times-v0860).
Only existing search runtime/title-regression after hashes change. All 998 targets,
before hashes, pinned base and native test-selection bytes remain.

## Boolean judge wait targets (v0.8.59)

The shared wait-target parser skips JSON booleans before integer conversion. Valid
later aliases and session/PID/time priority remain, including integer 1, numeric
strings and legacy done:true. See [native regressions](goal-result-waits.md#boolean-judge-wait-targets-v0859).
Only existing goals runtime/regression after hashes change. All 998 targets,
before hashes, pinned base and native test-selection bytes remain.

## Streaming vision content keys (v0.8.58)

Native content-key hashing streams the prepared image through the existing stdlib
file-digest pattern, preserving key bytes, route/profile boundaries and error fallback.
See [native regressions and measured key-path allocation](vision-cache-routes.md#streaming-content-keys-v0858).
Only existing vision runtime/regression after hashes change. All 998 paths, before
hashes, pinned base and native test selection remain; no dependency change.

## Overflow-safe MCP cache expiry (v0.8.57)

The shared cache reader treats numeric overflow in existing TTL validation as a
cache miss. Healthy cached servers still register through native lazy discovery.
See [regressions and boundaries](mcp-schema-publication.md#overflow-safe-expiry-metadata-v0857).
The cache runtime after hash changes and one existing upstream TTL regression target
is added: 998 paths on the same base. All previous before hashes and other after
hashes remain. Native test selection already contained the TTL file and is unchanged.

## Native compressed-resume acceptance (v0.8.56)

The native compressed-resume fixture uses a synthetic config file and the actual
loader instead of a stale zero-argument stub. Existing history/receipt assertions
now run; a distinct default/explicit-profile control checks real loader separation.
See [native coverage and limitations](session-metadata-reads.md#compressed-resume-receipts-v0856).
This adds one existing upstream test target and its selection: 997 paths, with all
previous 996 before/after rows unchanged. No production or dependency hash changes.

## Classic resume identity lookup (v0.8.55)

The classic title-or-ID selector now uses the existing small metadata reader for
its initial exact-ID check. ID/title/local-prefix priority and compression-tip
projection remain intact. See [native regression and measured selector limits](session-metadata-reads.md#classic-resume-identity-v0855).
The existing main module after hash changes and one new regression target is added:
996 paths on the same v0.22.5 base. Every prior before hash remains, and all other
prior after hashes are unchanged. Native test selection includes the new file.

## Metadata-only exact session ID lookup (v0.8.54)

The shared native resolver reuses the existing small metadata reader for exact ID
matches, preserving token flushing, prefix SQL and returned IDs. See the
[regression and measured read-path limits](session-metadata-reads.md#exact-session-id-lookups-v0854).
Only the existing runtime and regression after hashes change; the v0.22.5 base,
all 995 target paths/before hashes and native test selection remain unchanged.

## Bounded terminal Git-label memory (v0.8.53)

The shared native Git-label helper retains at most 128 cwd entries while preserving
its five-second TTL and direct-file branch/worktree resolution. See the
[regression and allocation evidence](chat-rendering-surfaces.md#bounded-git-label-cache-v0853).
The existing runtime and regression files add two pinned targets, bringing the kit
to 995 paths on the same v0.22.5 base. All previous 993 before/after rows remain
unchanged. The native test selection now explicitly includes the Git-label file.

## Overflow-safe judge wait targets (v0.8.51)

The native goal judge skips integer-conversion overflow in its existing shared
wait-target parser. Later valid aliases, session/PID/time priority and no-target
continuation retain their behavior. See [wait-target handling](goal-result-waits.md#overflowing-judge-wait-targets-v0851).
Only one runtime line and its existing regression file change. The v0.22.5 base,
993 targets, native test selection and v0.8.50 memo repair remain intact.

## Preserve judge timestamp evidence (v0.8.50)

The native goal judge now renders a separate canonical memo prompt with only its
generated clock field empty. Timestamps in goal, response, criteria, contract and
background evidence stay in the key; outgoing judge prompts are unchanged. This
prevents false verdict reuse without disabling valid clock-only reuse. See
[memo boundaries](goal-judge-memo.md#preserve-timestamp-evidence-v0850).
The v0.22.5 base and 993 targets remain; two existing runtime files and their
existing regression file change within the consolidated patch.

## Report retention failure isolation (v0.8.49)

The companion retention helper now reports known archive-validation failures per
entry and continues later eligible work, while retaining a failed run status.
Rejected reports stay intact; archive validation and process/ownership guards are
unchanged. See [storage safeguards](storage-and-backups.md#report-validation-failures-v0849).
The upstream base, 993 native targets, patches and test selection are unchanged.

## Explicit offline doctor manifest (v0.8.48)

The doctor can now check this kit with
`--manifest patches/stable-full/manifest.json`, preserving the historical default
for cumulative-kit users. It reuses the existing source verifier and keeps runtime
readiness unknown. See [manifest selection](offline-setup-tools.md#select-the-matching-patch-manifest-v0848).
The pinned v0.22.5 base, 993 targets, native patch and test selection are unchanged.

## Managed Mac runtime compatibility (v0.8.47)

The [Mac recipe](macos-install-update.md#managed-runtime-acceptance-v0847) now
resolves the existing committed PM dependency interpreter instead of assuming an
in-tree venv. A reusable native fixture verifies settings/profile/search continuity
between pinned source versions using synthetic state. The public kit still covers
993 targets on v0.22.5; native patch bytes and test selection are unchanged.

## Release inspection and live judge evidence (v0.8.46)

The companion release verifier disables repository fsmonitor hooks while checking
Git status. See the [offline regression scope](privacy-review.md#read-only-history-check-v0846).
The [live-card open items](live-captain-cards-20261109.md#what-remains-unproven)
also distinguish two recorded judge verdicts from unproven identical-input memo
reuse. These companion changes were prepared together; v0.8.45 was an unpublished
intermediate, not a separate release.
Native source, stable-full patch, pinned v0.22.5 base, all 993 target hashes and
native test selection are unchanged.

## First goal turn sees its contract (v0.8.42)

The kit covers 993 paths. `/goal` with a completion contract now starts the first turn
with the contract and the evidence rule, not just the headline. A live judge had
answered `continue` for a finished card whose reply carried no evidence. See
[live Captain cards](live-captain-cards-20261109.md).

## TUI agent activity (v0.8.39)

The kit covers 989 paths. The TUI agents panel shows a running subagent's tool and
step. See [chat rendering surfaces](chat-rendering-surfaces.md#tui-agents-panel-shows-what-a-subagent-is-doing-v0839).

## Chat rendering across surfaces (v0.8.38)

The kit covers 986 paths. The web dashboard renders tables and labels fenced
blocks, and the TUI hint stops the model from sending unrenderable mermaid or chart
fences. See [chat rendering surfaces](chat-rendering-surfaces.md).

## Goal-judge verdict reuse (v0.8.37)

The kit now covers 983 paths. `hermes_cli/goals_judge_memo.py` reuses the judge's
`done`/`blocked`/`continue` verdict for an input identical except for its clock, so
a repeated response does not cost a second judge call. See
[goal-judge memo](goal-judge-memo.md).

## Retention parity on macOS (v0.8.36)

The companion retention helper now also runs when lsof cannot see a closed vendor
agent, and when a short-lived `ping` is active. Native source and patch are unchanged.

## Retention runs again (v0.8.35)

The companion retention helper no longer gives up on non-dumpable session daemons,
continues past an entry it cannot remove, and removes links inside idle trees without
following them. Native source and the stable-full patch are unchanged. See
[storage and backups](storage-and-backups.md#retention-that-can-actually-run-v0835).

## Goal ensure usage (v0.8.34)

The goal-driven-execution skill now shows the exact `hermes goal ensure` form:
contract text as one argument or heredoc on stdin, with `outcome:` and
`verification:` lines. In an isolated live Captain card, the model read the
skill, checked `hermes goal status`, then guessed nonexistent `--outcome` and
`--verification` flags that native argparse rejects. Native source and the
stable-full patch are unchanged.

## Verification update (v0.8.33)

All twelve native check groups pass on Linux. Shared numeric owner checks and
bounded Desktop-test imports preserve existing behavior. Native verification
covers 497 Linux cases across separate file runs and 496 macOS cases in one
33-file run, with host-specific skips. Fifteen runtime and eighteen test files
are installed on both hosts; the kit now pins 980 paths. Desktop assets and
lockfiles remain unchanged. See [the exact scope and installation limits](native-checks-and-test-memory.md).

## Included behavior

- [Official Codex alias usage accounting](codex-alias-usage.md), avoiding unnecessary pricing-catalog reads while retaining actual token usage.

- [Lower diagnostic read memory and latency](diagnostic-read-efficiency.md).

- [Work tracking and independently reviewed delivery](tracked-delivery.md).

- [Refined charts, tables and diagrams](rich-output-presentation.md).


- [Bounded interpreter work for recall Unicode validation](recall-unicode-work.md), without per-character Python callbacks.

- [Missing-skill worker results](missing-skill-worker-results.md), settling known preload failures with an actionable diagnostic.
- [Scheduled and revision handoff termination](scheduled-review-handoffs.md), preserving native landing states without a follow-up model acknowledgement.

- [Adaptive recall payload loading](adaptive-recall-hydration.md), keeping compact result counts without loading discarded neighbor bodies.

- [Verified blocked-worker handoffs](blocked-worker-handoff.md), returning the saved blocker without an extra model call and preserving final-iteration holds.

- [Null-section settings merge parity](settings-null-sections.md), preserving an accepted nested edit when a later null section is ignored by the native API.
- [Ordered config type changes](settings-null-sections.md#ordered-type-changes-v0816), retaining separate writes when combining them would revive removed fields.

- Focus navigation, saved-chat history, always-visible device/profile context, bot
  configuration, Hub collections, native file previews, rich Markdown and Workflow.
- Role-specific THINK/ACTION plans, independent review, bounded handoffs, idempotent
  card creation, ready-work dispatch and native terminal-stop behavior.
- Bounded file and history reads, structured/CJK recall, compaction publication and
  recovery, prompt-prefix reuse, cache cohorts and privacy-preserving usage attribution.
- Profile/account-scoped metadata caches, process/cache diagnostics, derived-cache
  retention, protected active scratch work and update-preservation recovery.
- Optional per-model reasoning effort ceilings after explicit overrides, including owner-bound frozen sessions and auxiliary requests. See the [effort-limit guide](reasoning-effort-limits.md).
- Existing transport, owner/claim, review, data-clearance, quota and emergency-stop gates.

No account grants, conversations, live boards, operator profiles or production data
are bundled. Legacy technical profile identifiers remain where the native compatibility
or owner gate requires them; these are not imported personas or grants to impersonate
that owner. The English role templates are separate reference material.

## Prepare a new isolated checkout

Run from the Legion repository root. Choose an unused destination outside the running
installation. The source download is public and makes no model request.

```sh
set -eu
export LEGION_ROOT="$(pwd)"
export HERMES_CHECKOUT="/absolute/path/to/new-hermes-stable-checkout"
legion_manifest="$LEGION_ROOT/patches/stable-full/manifest.json"
legion_patch="$LEGION_ROOT/patches/stable-full/0001-stable-full.patch"
legion_base_commit="$(python3 -c 'import json; print(json.load(open("patches/stable-full/manifest.json"))["upstream_commit"])')"
test ! -e "$HERMES_CHECKOUT"
git clone --depth 1 --branch v0.22.5 --no-checkout https://github.com/NousResearch/hermes-agent.git "$HERMES_CHECKOUT"
git -C "$HERMES_CHECKOUT" checkout --detach "$legion_base_commit"
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase base --manifest "$legion_manifest"
git -C "$HERMES_CHECKOUT" apply --check "$legion_patch"
git -C "$HERMES_CHECKOUT" apply "$legion_patch"
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase installed --manifest "$legion_manifest"
```

A moved release tag, different source, unrelated edits or pre-existing added target
must refuse. Do not force, fuzz, reset another person's work or stack full alternatives.
The patch has one line of context; exact before hashes and the pinned commit remain
mandatory. Native Git attributes preserve the PowerShell checkout's CRLF exception.

Use upstream's native package manager and matching frozen dependency groups. Do not
repair an environment with raw pip/uv or substitute a different Python/Node runtime.
Follow [test and adopt](installation-and-rollback.md#test-and-adopt) and the
[Mac guide](macos-install-update.md). Source application does not rebuild or reload an
already running Desktop or Gateway.

## Reproduce the offline selection

After preparing the existing upstream frozen test environment, run the Python selection
through the native runner, from the patched checkout. This example only forwards the
recorded paths; it does not install dependencies or call a model.

```sh
cd "$HERMES_CHECKOUT"
python3 - <<'PY'
import json, os, pathlib, subprocess
selection = pathlib.Path(os.environ["LEGION_ROOT"]) / "patches/stable-full/test-selection.json"
files = json.loads(selection.read_text())["python_test_files"]
env = {**os.environ, "HERMES_TEST_FILE_RETRIES": "0", "HERMES_TEST_WORKERS": "2"}
raise SystemExit(subprocess.call(["scripts/run_tests.sh", *files], env=env))
PY
```

For Desktop, use the same selection's `desktop_test_files` relative to `apps/desktop`
with the existing Vitest runner, then run the full native TypeScript check and Desktop
build. Test and packaging tools must already be admitted by the native package manager.
Do not use a running user's renderer or provider account as a test fixture.

## Owner-safe history and draft recovery

A link with an explicit connection/profile opens that owner's retained history.
If a same-ID conversation is already open for another owner, the native app
opens a separate window instead of retargeting the original runtime. Repeated
same-owner links reuse the existing window. An unavailable window bridge
reports an error and leaves the original window intact.

Unsent text and uncertain-send retry identity are isolated by connection,
profile, target profile and session. Reloading or closing a window restores
only that owner's saved text. Retention is capped at 50 saved scopes per owner;
updates do not scan every saved draft. Attachments remain memory-only. Accepted sends
never clear a newer draft after the clicked text was already consumed. External
submissions do not own or clear the editor draft.

Older unassigned drafts are retained separately, never attributed to the current
profile automatically. When an unassigned draft exists and the editor is empty,
use the recovery notice to copy it into the current editor. Review the content
before sending. Recovery never sends automatically and keeps the original.
Profile rename and compression lineage transfers preserve the source if writing
the destination fails. Keep existing quotas and disable paid fallback as before.

## First-use interface checks

1. Open **All features → Plugins**. The bundled Desktop **Kanban** plugin is intentionally
   off by default upstream. Enable that plugin explicitly if you want Work to show the
   board and Workflow. This is a Desktop presentation opt-in, not permission to start
   the dispatcher or release an emergency stop. Without it, Work shows native agent activity.
2. In **Bots → Edit profile**, save the role, family, mode, counterpart and eligible model
   and effort. Reopen to verify persistence. Configure both sides for a reciprocal pair;
   one-way pairing is displayed honestly and is not a ready execution lane.
3. In **Work → Workflow**, select a downstream card, inspect its actual upstream links
   and recorded bot journey, then open the original card if needed. A dependency edge
   does not prove execution or completion; absent run evidence stays absent.
4. In **Hub**, create a collection, choose its members explicitly and save a page or
   import a file. Chat files stay private until shared. Removal uses recoverable trash.
5. In **History**, open a retained conversation and verify its content. Opening history
   is separate from submitting a prompt or resuming a goal.

Test within a separate synthetic home first. After acceptance, adopt the rebuilt native
application only at idle, preserving drafts, sessions and worker ownership. An updater
refusal is a gate to diagnose, not permission to bypass custody or authentication.

## Evidence and limits

The broad offline run completed 218 Python files: **2,737 passed, 13 skipped, zero
failures**, with two workers and zero file retries. Desktop completed **60 files,
383 passing tests**; full TypeScript and the native Linux renderer/main build passed.
After two synthetic scanner fixtures were clarified, their two files were separately
rerun: **33 passed**. Those cases overlap the broad selection and must not be added to it.

Native clean-base apply, installed-byte verification, reverse and reapply passed for
all 667 paths in the original baseline on **Linux and macOS**. These are source compatibility results, not a
claim that the entire Python/UI suite ran on macOS. Linux rendered checks use the fresh
built source-mode Electron application and its actual backend in a separate synthetic
home, with only localhost model metadata and zero inference. The 11 interaction checkpoints include explicit Kanban opt-in, upstream-card navigation,
Hub collection/page saves and retained-message reopening. Two blocked external catalog
requests produced expected DNS errors under the network-denied fixture; this is not
a claim of universally clean network logs. These checks do not certify a downloaded
packaged application, original stored sessions or every UI feature.

The suite initially exposed stale test interfaces after upstream's facade changes.
Fixtures were reconciled against the native owner-policy and bounded-read contracts;
no production permission or completion rule was weakened to satisfy them. Test-only
synthetic identifiers are not production receipts.

Matching cache keys/prefixes provide comparison evidence, not a guarantee of shared
provider cache. Idle time alone does not establish cache expiry. No universal cost,
quota, RAM, disk or latency improvement is claimed from offline tests. Use existing
real workload diagnostics before making those claims.

Model defaults are not hard effort ceilings. In particular, a Terra `high` profile can
still be overridden explicitly by a task or saved session. This kit does not silently
clamp such an override, increase a quota, introduce paid fallback, or declare a provider
ready from its family label. Preserve native limits and diagnose unsupported routes.

## Roll back an unused matching checkout

```sh
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase installed --manifest "$legion_manifest"
git -C "$HERMES_CHECKOUT" apply --reverse --check "$legion_patch"
git -C "$HERMES_CHECKOUT" apply --reverse "$legion_patch"
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase base --manifest "$legion_manifest"
```

This source reversal is not a live database restore. Keep the compact source/application
rollback until original-session acceptance; retire only owned, inactive staging after
its evidence is durable. Do not keep redundant full copies merely to repeat a test.


The draft/history repair retains an earlier unconfirmed message separately when the
editor has newer input. Restore is manual, into an empty matching owner, and never
sends; an unchanged explicit retry retains the original identity. Inactive history
cursors are retired. Browsing survives a transient runtime reattachment only for the
same owner and durable conversation, including when its loaded history shrinks.
Current source and native packages are installed on Linux and macOS. The Linux
draft/history flow passes twelve interaction steps. Both platforms pass a separate
17-step rich-content, bot-control and navigation selection, including both Mac launch
locations. These private synthetic checks do not establish original-user adoption
or production token/RAM savings. See the versioned verification record for scope.


## Compact-window navigation regression

Normal spacing must not override the existing narrow-window rule. Short labels
(Chat, Work, Bots and Hub) stay on one line; longer labels may wrap. Settings
remains reachable through All features, and History remains visible. The repair
does not change profiles, open a prompt or submit work.

After the existing native Desktop build, run the added E2E regression using the
already prepared, pinned test tools (no dependency installation):

```sh
cd "$HERMES_CHECKOUT/apps/desktop"
npm exec --offline --no -- playwright test e2e/core/focus-navigation-layout.spec.ts
```

The core harness supplies a private home and local mock catalog. Linux needs
its normal test display (or the documented native headless display setup).
The public test checks 320/580-pixel layouts and refuses inference; separate
native package acceptance also covers 900 pixels and saved history. Original
application processes and worker adoption are separate from this test.


## Import-free plugin source windows

Entry-point and directory metadata probes consume at most their existing 8,192
character window instead of decoding an entire source file first. They still do
not import or execute plugin code. Explicit kinds, provider markers, text
encoding and failure behavior retain the existing contracts; no new source
cache can hide an edited file or a permission change.

The added resource regression runs with the existing prepared test environment:

```sh
cd "$HERMES_CHECKOUT"
HERMES_TEST_FILE_RETRIES=0 scripts/run_tests.sh tests/hermes_cli/test_plugin_source_window.py
```

The test reads actual temporary source files through the real classifier. Large
source allocation measurements and four existing bundled manifests are recorded
separately in the verification note. No production RSS or token saving is inferred.


## Auxiliary usage and cached input

Native Codex/Claude auxiliary responses retain reported cache read/write and
reasoning counters when projected onto the existing Chat Completions contract.
Claude cache buckets are separate from uncached input; their sum is its prompt
total. Billing-provider identity does not select the shape of an already
normalized response. A fully cached call still contributes one call count;
reasoning is already included in output, and excluded MoA work is not counted
a second time.

Run the regression with the existing prepared offline environment:

```sh
cd "$HERMES_CHECKOUT"
HERMES_TEST_FILE_RETRIES=0 scripts/run_tests.sh tests/agent/test_auxiliary_usage_buckets.py
```

Only fixed provider-response fixtures are used; no inference or pricing lookup
is requested. The verification note distinguishes these arithmetic checks from
actual provider cache evidence. Existing historical omissions are not invented
or backfilled, and a larger corrected usage total does not imply more calls.


## Efficiency, monitoring and autonomy update (v0.8.0)

This update keeps the same upstream base and adds these changes to the consolidated kit:

- **Bot monitoring.** The roster's worker detail carries optional `current_tool`,
  `iteration`/`max_iterations`, `started_at` and input/output token totals taken from
  the session row the roster already reads; no extra database reads. The Desktop shows
  them as one icon-led line (tool, step i/max, elapsed, tokens), and Kanban run history
  shows each run's duration. `profiles.list` no longer violates its own wire contract
  (`last_activity_description`/`ended_at` were sent but undeclared).
- **Rich answers.** A `chart` fence and a platform hint that names the existing rich
  blocks. See [rich answers](rich-answers.md#inline-charts-and-diagram-guidance).
- **Fewer repeated model calls.** `vision_analyze` caches successful results in memory
  (256 entries, one hour) keyed by image bytes, prompt and model route; errors and empty
  results are not stored and a hit is marked `"cached": true`. The compact `kanban_show`
  view also clips long event payloads and older run fields while keeping the latest run,
  task body and newest comments intact.
- **Cacheable compression.** The context compressor sends its fixed instructions before
  the variable transcript, so providers with prefix caching can reuse them.
- **Worker exits.** A worker that exits cleanly without a terminal Kanban call and left a
  final message is held for a decision with that message attached, instead of being
  respawned blind. The dispatcher writes a `[kanban-worker-start]` marker before each
  attempt, so an older attempt's `rc=0` trailer is no longer booked for a SIGKILLed
  attempt and crash diagnostics quote only the attempt that crashed.
- **Delegated goal decisions.** `goals.delegated_decisions: true` (default `false`) tells
  the goal judge that in-scope choices are the agent's to make; a verdict that only waits
  for a user decision is continued with a "decide within authority" note at most twice per
  goal. Credentials, destructive or out-of-scope actions, spending and reserved
  publication gates still pause.
- **Fleet session search.** `session_search` accepts `scope="fleet"` to search the other
  profiles of the same Hermes home read-only, with per-profile limits and a time budget;
  each hit names its profile. The default scope is unchanged.
- **Usage pricing never fails a turn.** A failed cost lookup records an unknown cost
  instead of turning a delivered response into a failed attempt that re-sends the prompt.
- Plugin manifests may declare `provides_middleware` without a warning.

Run the focused checks from a patched checkout:

```sh
cd "$HERMES_CHECKOUT"
HERMES_TEST_FILE_RETRIES=0 scripts/run_tests.sh \
  tests/tui_gateway/test_profiles_worker_session_contract.py \
  tests/tools/test_vision_analysis_content_cache.py tests/tools/test_kanban_show_compact_clip.py \
  tests/hermes_cli/test_kanban_clean_exit_final_message.py \
  tests/e2e/core/kanban/test_kanban_worker_sigkill.py \
  tests/hermes_cli/test_goal_delegated_decisions.py tests/tools/test_session_search_fleet_scope.py \
  tests/agent/test_context_compressor_prompt_cache_prefix.py \
  tests/hermes_cli/test_plugin_manifest_provides_middleware.py tests/agent/test_run_agent.py
cd apps/desktop && npx vitest run src/lib/chart-spec.test.ts \
  src/plugins/hermes-bots/bot-worker-progress.test.ts src/plugins/kanban/bot-journey
```

These are offline checks. They show the code paths work; they do not measure a
production saving, which depends on your workload.


## Usability update from a user walkthrough (v0.8.1)

A scripted walkthrough of the real Desktop against a live Hermes home found these
problems, now fixed:

- **Global pause is visible.** When the emergency stop is engaged, `/api/status` reports
  `estop: {engaged_at, reason}` (reason only on local connections) and the Desktop shows a
  persistent strip plus a composer note saying new work is on hold until `hermes resume`.
  There is no resume button in the app.
- **Bot roster reports every bot's model, provider and description.** Sibling profiles
  discovered by the authority gateway previously had these fields hard-coded empty, so
  128 of 129 bot cards said "not reported". They now come from each profile's cached
  config and `profile.yaml`.
- Bots: provider and model fields no longer overlap; filter counts follow the search.
- Kanban: the new-task assignee picker filters as you type and marks THINK/ACTION bots;
  the card drawer's Comments/Activity/Runs/Log switcher is a real tab list placed above the
  long description; the History view uses the full width.
- Navigation: New chat and History selections highlight the right sidebar item; the
  Workflow detail panel no longer hides the graph.
- The floating pet stays below dialogs and away from the composer and status bar.
- Search hides empty groups and ranks title matches while typing; Catch up explains an
  empty goal state instead of showing "Not reported".
- Settings: the long "Applies to" profile list has a filter and a collapsed view.

## Retention companion update (v0.8.2)

This release updates the standalone retention helper and its tests, with no changes to
the 909-path upstream patch or Desktop assets. See [retention safeguards](storage-and-backups.md#retention-safeguards-v082) and the [verification record](verification.md).

## Goal judge accounting update (v0.8.3)

Post-turn goal judges now record auxiliary usage on the owning goal or worker session
and restore the surrounding accounting context. The complete kit contains 912 paths.
See [goal usage accounting](goal-usage-accounting.md) for the failure, test evidence and
runtime-adoption limits. No extra model requests or Desktop rebuilds are introduced.

## Search cache memory update (v0.8.4)

The search memo now keeps at most 256 entries and a 32 MiB budget for retained Python
keys/responses. Cold entries still use the existing bounded disk tier. Expired payloads
are released on lookup, including unrelated expired queries. The complete kit contains
913 paths; see [measurement and limits](search-cache-memory.md).

## Worker monitor readability update (v0.8.5)

Long tool names no longer push step, elapsed time and token facts outside narrow
roster rows. Facts wrap within the available width, and the existing hover summary
includes all displayed progress facts. The consolidated kit contains 914 paths.
See [verification and limits](worker-monitor-readability.md).

## Vision cache route update (v0.8.6)

Both auxiliary vision cache layers include the main connection's endpoint, API mode
and authentication mode, with context-local values taking precedence over saved
model settings. Unchanged routes still reuse successful results. The consolidated
kit contains 915 paths; see [verification and limits](vision-cache-routes.md).

## Offline vision verification update (v0.8.7)

The capability-routing regression now supplies synthetic catalog data for text-only,
vision-capable and unknown models. This removes a live-catalog assumption from the
offline test while keeping production routing unchanged. The complete kit contains
916 paths; see [verification](vision-routing-verification.md).

## v0.8.8 — Bound retained token-estimate memo memory

The global token-estimate memo now limits retained key/value objects to 32 MiB as well as 4,096 entries. Oversized messages are estimated normally without being cached. See the [measurement and adoption boundaries](token-memo-memory.md).
