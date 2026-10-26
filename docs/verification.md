# Verification record

## Initial cumulative patch acceptance (v0.1.0)

This record describes the exported artifact's offline acceptance. It contains no production logs, prompts, accounts, task/run IDs or private machine paths.

| Check | Result | Scope |
|---|---|---|
| Patch base verification | PASS | Exact publicly available upstream commit and all 279 before hashes |
| Normal Git apply check and apply | PASS | Separate disposable checkout, not a running installation |
| Installed source verification | PASS | All 279 resulting hashes match the export manifest |
| Reverse apply and base restoration | PASS | All original bytes and absence states restored, then reapplied for regressions |
| Python source syntax | PASS | 242 changed/added Python source and test files |
| Exported Hermes Python regressions | 964 passed, 0 failed | 109 input files through the canonical per-file runner, zero retries, three workers |
| Desktop UI unit regressions | 56 passed, 0 failed | Seven changed UI test files; no rendered desktop/model test |
| Companion tool regressions | 11 passed, 0 failed | Wrong revision, unrelated work, existing new targets, traversal, symlinks, changed/missing/unlisted files |
| Roles and skills | Eight roles, ten skills | Rewritten English templates; no live persona/configuration export |
| Working-tree secret scan | PASS | Gitleaks 8.30.1, default rules, fully redacted output, allow-comment bypass disabled |
| Privacy review | PASS for reviewed identifiers and file inventory | Every public file plus full patch contents; separate private identifiers review |
| Historical-secret detection control | PASS | A synthetic local-only credential was committed then deleted; current-tree scan was clean and all-history scan detected it |

macOS-tagged Python checks in five files were skipped on the Linux test host. This is not macOS acceptance, a full upstream test-suite result, or a whole-repository lint/build claim. The desktop tests are unit tests, not visual or live-session acceptance.

Three test files were generalized for distribution: a machine-specific home assertion became a portable assertion, a diagnostic sentinel became short synthetic data, and a credential-redaction fixture now constructs unmistakably artificial input at runtime. No live source file was edited for these export changes.

The dedicated scanner checks both the exact committed tree and all reachable Git history before publication. The initial history is created fresh with a neutral project author/committer, and the final archive is generated from Git's explicit tree rather than a working-directory copy. `RELEASE-MANIFEST.json` records every payload file's SHA-256; the manifest itself is bound by the Git commit and archive hash.

All upstream-base source tests used the existing approved test environment. The test runner's normal isolation created temporary homes; no model acceptance job, provider/allowance probe, dependency install or service restart was used to create evidence. Private source hashes were compared afterward and remained unchanged.

No general token-saving percentage, billing saving, cross-bot provider-cache origin, unlimited cache retention or live startup speedup is established by this release. Measure actual authorized work with matched identities and honest coverage if evaluating impact on your own installation.

## Team and multi-account update (v0.2.0)

The cumulative 279-file Hermes patch is unchanged. This update adds a standard-library-only offline planner, fifteen public role templates, a 34-profile topology, six Web specialists, native config fragments and English setup guides. Account identities, usage snapshots, tasks and budgets are synthetic. No live profile/account is exported or changed.

The companion's full unittest suite covers new-session route choice, public/private gates, capability readiness, shared account budgets/duplicate aliases, hour/day/parallel limits, cooldown, missing/stale evidence, exact session pins, existing running work, dependency waits, provider mismatch, secret-field rejection and no network/input mutations. New behavior was observed failing before implementation, including a reproduced duplicate-handle/split-budget case. Current release acceptance is regenerated after all files are finalized; previous Hermes regression counts above are not added to the new companion-test count or represented as newly rerun.

The planner is not a native account selector or live quota enforcement layer. Setup documentation separates native pool ownership and manual profile configuration from offline recommendations. A real-bot/model acceptance run was not requested or performed for this update.

### Reproduce native config compatibility offline

In the isolated, supported Hermes checkout, copy `verification/native_profile_examples.py` to `tests/hermes_cli/test_legion_native_profile_examples.py` and copy the 34 `profiles/native/*.config.example.json` files to `tests/hermes_cli/fixtures/legion-native-fragments/`. Run that test file through the checkout's canonical `scripts/run_tests.sh` and existing managed test environment, with retries disabled. This uses Hermes' own isolated-home fixtures, effective config loader, pool-strategy reader and profile argument parser; no actual credential pool is loaded, no account is logged in, and socket creation is denied during effective-config checks. The test refuses a missing fragment directory instead of reporting an empty run as success.

Historical v0.2.0 team acceptance: **34 companion tests passed, zero failures**, plus **36 native configuration/parser cases passed, zero failures**. The latter cover all 34 distributed fragments, the documented native create command, and safe merging over a pre-existing legacy fallback chain. These are separate groups; prior cumulative-patch results are historical and were not rerun for this documentation/planner-only update.


## Public usability audit and fixes (v0.2.1)

The review began with an anonymous clone and public v0.2.0 release download. All six documented planner examples ran offline, but targeted regressions exposed two gaps: a plan could select another task for an already busy session, and Python's JSON reader accepted nonstandard Infinity values that could keep a snapshot eligible indefinitely. New tests failed on the published implementation before the repair.

The planner now fences sessions with running work regardless of task ordering, reserves a session after its first selection, rejects NaN/Infinity input and requires finite observation/snapshot times. It still only prints recommendations; it cannot dispatch, authenticate, enforce native credential selection or change live state.

The setup guide now gives exact fresh-home/profile commands, targeted model/pool/fallback updates, model-placeholder refusals and SOUL installation. The installation guide includes public base-checkout commands. Changing a home variable is explicitly distinguished from selecting a CLI installation. Both current and legacy fallback chains are cleared while unrelated settings are preserved.

Fresh acceptance for this update: **38 companion tests passed, zero failures**; separately, **37 native cases passed, zero failures**, covering 34 config fragments, argument parsing, legacy fallback merging and one complete three-profile setup walkthrough. The walkthrough invokes native command parsers/handlers for create, config path/set/get and verifies an existing delegation cap survives. It uses isolated homes, synthetic instructions/models, disabled container-service registration and denied network/multiplexer access. No OAuth flow, credential selection, model request or live-worker test was run.

A separately guarded full CLI entrypoint probe stopped at the native home-bootstrap boundary; it is not counted as a passing full-launch test. No live source or bootstrap behavior was changed to make it pass. Packaged launchers, platform services, provider/model availability and real authentication remain operator checks. These limitations matter when adopting a template on another machine.

The cumulative source patch and its 279-file manifest are unchanged. The previous 964 Python and 56 UI results are historical, not newly rerun for this planner/documentation fix. Files, all reachable Git history, release payloads and known private identifiers/credential values are reviewed before publication; reports remain outside the repository.


## Offline preparation and diagnostics (v0.3.0)

New tools preview/export registered config and SOUL templates to a fresh private directory and inspect explicit JSON inputs/bundle integrity. The planner adds optional per-candidate explanations while preserving its original decisions, reservations and pins. Runtime/auth readiness stays unknown. No account mapping or quota snapshot is exported, and no native config is installed automatically.

Fresh companion acceptance: **64 tests passed, zero failures**. New regressions were observed failing before implementation, including missing offline tools/explanations, empty Web model references and false readiness for an empty team. The suite covers overwrite/link/live-root refusal, model/secret-field validation, all 34 registered exports, bundle corruption and semantic fallback checks, safe diagnostic output, stale snapshots, no network/process execution on the bundle path, explanation equivalence and pinned/busy sessions.

A checkout-inspection regression proved that Git could execute a configured filesystem-monitor helper. The verifier now disables it, external diff/text conversion, lazy fetch, prompts and optional locks. The regression passes without running that helper. On a fresh isolated pinned checkout, doctor passed both the original base and exact applied-source state; no Hermes import was used for these inspections. Git apply reported existing cumulative-patch whitespace warnings, not an apply refusal; the unchanged target hashes passed.

Separately, **37 native cases passed, zero failures**, using all **34 newly generated synthetic config fragments** as the native harness inputs, plus parser/legacy-fallback/three-profile setup checks. Use the existing native verification recipe; for generated fragments, copy each `profiles/<id>/config.example.json` to the fixture directory as `<id>.config.example.json`. The approved existing upstream-managed test environment and canonical runner were used with zero retries. No dependencies were installed. This is offline config acceptance, not actual provider authorization, model capability, packaged startup or live routing.

The 279-file cumulative source patch remains unchanged. Source/profile guards are compared around the work, and public files, reachable Git history and release payloads are scanned before publishing. Historical source/UI counts above are not rerun or added to these results.


## Repeated attachment fix (after v0.3.0)

The current main branch extends the cumulative patch to 280 files. Repeated built-in
references in one message now expand once per kind, target and line range. Original
user text and reference metadata remain intact. Distinct ranges remain separate;
plugin references retain their existing behavior. No cache survives to the next message.
The 16-expansion work limit applies to distinct built-in attachments.

Offline regressions first reproduced two failures: duplicate URL extraction and
16 copies of the same file preventing a later distinct file from being attached.
The final new regression file passes 5 cases; the existing reference, plugin,
concurrency, CLI and Gateway files pass 48 cases. These are separate cases, not
summed historical test runs. No model or real URL request was made.

One synthetic 30,000-character file referenced 16 times, with a 1,000,000-token
context limit, produced these results using the native preprocessor:

| Metric | Before | After |
|---|---:|---:|
| Estimated injected tokens | 120,176 | 7,511 |
| Output characters | 480,985 | 30,340 |
| Peak traced Python allocations (bytes) | 6,134,460 | 257,107 |

This single offline sample is not a whole-process RSS benchmark, billed token
measurement or evidence of savings across production workloads. Already-running
processes must load the changed module through their normal safe lifecycle before
runtime activation can be claimed. Provider quotas and fallback settings are unchanged.
The v0.3.0 tag and release remain immutable; these results describe the newer main branch.


## Cache memory boundary correction (after v0.3.0)

The current main branch now contains 282 patched or added files. Automatic cache
budgeting uses the smaller finite memory.high/memory.max value in the selected
cgroup, rather than blindly preferring memory.high. The own-cgroup/root lookup
order and v1 fallback remain unchanged. This does not add ancestor traversal or
change operator-configured limits, quotas, provider selection or fallback policy.

The Linux [cgroup v2 documentation](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
distinguishes the high throttling threshold from the maximum memory boundary.
An offline regression with memory.high=8 GiB and memory.max=2 GiB previously
produced a 5,324 MiB auto budget; it now produces 1,331 MiB, preserving the existing
65% headroom policy. Three control combinations retained their expected budgets.
All 43 tests across the boundary regression and existing cache-pressure suite pass.
No model calls or live memory-limit changes are involved. These are correctness
results, not measured production RSS savings. Immutable release tags are unchanged.


## Durable idle-cache eviction (after v0.3.0)

Idle-TTL and cache-size eviction now use the same persisted-transcript check as
memory-pressure eviction. Previously, both paths could remove the only current
copy of a conversation while the session DB lagged behind. Unflushed or unknown
transcript state now retains the agent; a later sweep may evict it once the flush
index catches up. Active agents remain protected. Explicit user-directed session
reset/model changes retain their existing semantics.

Two native regression cases first failed on the prior source (one per policy),
then passed with the fix. All 73 cases across the new durability regression,
existing agent-cache tests and cache-pressure tests pass offline. Three existing
eviction fixtures now explicitly represent persisted transcripts; their original
release-order and bounded-cache assertions remain intact. No model calls are used.

This intentionally favors conversation preservation over RAM reduction during a
persistence failure. It does not repair a failed database or impose a hard memory
limit. No production memory-savings percentage is claimed.


## Explicit usage-log coverage (after v0.3.0)

The read-only usage attribution CLI now accepts an explicit log-file budget:

```sh
python -m hermes_cli.usage_attribution --home /path/to/hermes-home --hours 24 --max-log-files 512
```

The default remains 32 recent uncompressed files. The accepted range is 1–512,
with at most 2 MiB read per file. The report includes the chosen budget, files
sampled, omitted files, cut tails and unknown time coverage. An expanded scan can
read up to 1 GiB; use it for a deliberate audit rather than frequent polling.
Compressed logs and profiles beyond the existing 128-profile bound are still not
read. Zero omitted files does not establish complete time-window coverage.

Five new offline cases verify expanded CLI collection, unchanged lightweight
defaults, invalid-budget rejection before I/O and private-record exclusion.
Together with the existing attribution tests, all 13 cases pass. The installed
standalone CLI was exercised read-only against existing logs before publication;
no Desktop or Gateway restart is required. No model calls, new keys, database
initialization, quota changes or paid fallback are involved.

Compare before/after using equal coverage and matched time windows. More observed
attempts after increasing the budget means improved visibility, not increased
usage; fewer rows in a partial scan do not prove savings. Runtime logs, identifiers
and measurements from private projects are not part of this public package.

## v0.3.1 release verification

This release includes the four post-v0.3.0 changes above: repeated attachment
deduplication, correct cache memory-boundary selection, durable idle-cache
eviction and an explicit usage-log scan budget. The cumulative inventory contains
287 source/test files, including 115 Python test files. Earlier release tags
remain unchanged.

The release integration run passed 143 distinct native cases in 12 relevant
test files, with zero failures and zero retries. The companion tools and examples
are checked separately; historical overlapping runs are not added to this count.
The source patch and pinned upstream revision are unchanged by release packaging.

Memory-boundary detection does not configure MemoryHigh or MemoryMax. An operator's
MemoryHigh can throttle work; MemoryMax can trigger an OOM kill. This release
preserves active agents and unflushed conversations during automatic cache
eviction. It does not promise that an externally imposed hard limit is safe for
every workload.

The locally installed runtime files were compared with the public inventory
before release. Offline results establish regression coverage, not measured
production RAM, latency, billing or cross-bot cache savings. No model requests
are used for release verification, and no live limits or provider settings are
changed by packaging.


## Growing-file preview bounds (after v0.3.1)

A pre-read file size is advisory: an ordinary log can grow between stat and open.
Bare file references now bound the actual decoded read to the existing inline
character budget plus one sentinel character. Oversized content retains the
existing on-disk guidance rather than injecting a partial preview. Folder-entry
line counting likewise reads at most its existing 4 MiB ceiling plus one sentinel
byte; growth beyond that produces a fresh byte-size summary. Binary sniffing,
BOM decoding, allowed-root checks and SQLite read admission remain in place.

Two native regressions reproduced the unbounded reads before the fix; five final
cases cover growth and unchanged small/BOM/Unicode/exact-boundary behavior. All
67 cases in eight relevant reference, CLI, Gateway and SQLite inspection test
files pass offline with zero failures and zero retries. Ruff reports no findings
for the changed source and new regression file.

A synthetic file grew from six bytes to 8,388,614 bytes at the stat/open boundary.
With an existing 2,048-character inline budget, decoded text consumed fell from
8,388,614 to 2,049 characters. After warming the same metadata/import path, peak
traced Python allocations for this attachment sample fell from 16,920,866 to
209,393 bytes. Metadata-only reading fell from 8,388,620 to 4,194,311 bytes, including
the binary sniff. These are deterministic offline samples, not production RSS,
billed token or latency savings. No model requests, quota changes or paid
fallback are involved. The immutable v0.3.1 download does not include this newer
main-branch change.

## Explicit backup compaction (after v0.3.1)

The companion storage helper previews or compacts explicitly selected old SQLite
backup files. It streams compression and decompression, verifies exact SHA-256
and source identity, publishes an archive plus restoration metadata without
overwriting existing outputs, syncs before unlinking the original, and preserves
a free-space reserve. It does not operate on live databases or introduce SQL,
model calls, retention timers, provider changes or paid fallback.

Eleven offline cases cover read-only planning, byte-exact recovery, private-content
exclusion, sidecar/recent/link/path refusal, low space, existing outputs, source
growth, sync failure and canonical duplicate selections. The CLI examples are
also exercised against temporary synthetic SQLite snapshots. The native source
patch remains unchanged; this helper is newer than the immutable v0.3.1 release.


## Active and resumable scratch retention (after v0.3.1)

Automatic scratch retention no longer reaps processes by idle mtime. It checks
same-user working directories, executables, open files and command paths; unknown
process visibility defers the sweep. Git worktrees, environment/project markers
and `.keep` markers are preserved, including their registrations and uncommitted
files. Incomplete workspace scans retain data. Explicit operator-directed reaping
utilities remain separate from automatic retention.

Fresh entries skip recursive traversal. The native Gateway housekeeping table
runs protected scratch cleanup hourly under each served profile, with no added
startup sweep from that table. Existing opportunistic boot retention uses the
same protected policy. The original 24-hour idle threshold for eligible disposable
entries is unchanged. No extra model turn, provider, quota or fallback is involved.

Five failures on the old source reproduced live-process termination, deletion of
an open file, deletion of the caller's cwd, deletion after failed ownership
inspection and loss of resumable workspace data. Fifteen final regressions use
real kernel-backed child processes and controlled process visibility, and cover
missing inspectors, incomplete scans, normal disposal and fresh-entry behavior.
Four further failures exposed symlink/relative command paths; six combinations
now verify that the same process resumes reading its input after the sweep.
An additional cadence/scope test verifies two profile homes after the first hour.
All 58 cases across nine relevant native files pass offline, with zero retries.
Existing explicit reaping tests still verify their audit and cleanup contract;
the worktree test now verifies retention rather than automatic destruction.

These checks do not establish recovered production bytes or response-time savings.
An unreadable process must remain unknown. No live sweep should bypass that refusal
to manufacture a successful cleanup. The immutable v0.3.1 release is unchanged.


## v0.3.2 release verification

This release packages growing-file preview bounds, active/resumable scratch
retention and the explicit offline backup-compaction helper. The cumulative
source inventory contains 295 files, including 120 native Python test files.
A fresh integration run passed 215 distinct cases in 23 relevant native files,
with zero failures and zero retries. Companion tools and examples separately
passed all 75 cases. These counts do not add earlier overlapping runs.

The full patch passed fresh base/apply/installed verification on the pinned
upstream revision. Locally installed runtime bytes were matched against all
175 runtime inventory entries. Installed-source retention was separately
exercised with network/process/signal actions denied. Unknown process ownership
correctly deferred deletion; this is preservation evidence, not reclaimed bytes.
Runtime lifecycle acceptance is deployment-specific and does not certify an
actual hourly sweep or production usage/RAM/latency improvements.

Release files, reachable Git history, private-identifier checks and known private
credential comparisons are reviewed before publication. Runtime data, backup
archives, local configuration and operational receipts are excluded from the
public archive. Earlier releases remain immutable.


## Derived-cache disk-pressure preservation (after v0.3.2)

The first post-v0.3.2 change added one regression file, bringing that inventory to 296
source/test files, including 121 native Python test files. A fresh relevant native
run passed 59 cases across eight files, with zero failures and zero retries. These
cover document conversion, persistent search reuse, cross-process exclusion and
existing expiry/profile boundaries. Eight new cases cover low/unknown free-space
measurements, failed temporary-file creation/publication, replacement at capacity,
normal quota enforcement and encoded-byte admission at the reserve boundary.

Five cases first failed on the prior implementation; a separate encoded-byte
boundary case also failed before the fix. Disposable derived-cache payloads now
leave a one-GiB free-space reserve on their own filesystem. Replacement publication
finishes before evicting other hits, and replacement accounting excludes the old
version of that same key. Existing per-entry, total-byte, count and TTL policies
remain in place under the existing index lock. An in-progress publication can
temporarily require one additional bounded file; admission accounts for its full
encoded size.

Installed-source offline acceptance used real temporary cache files with network,
process and signal actions denied. In the synthetic failed-publication workload,
three conversion executions before the fix became two with the installed fix
because the previous hit survived. A simulated full filesystem produced zero
new cache payloads. These results do not establish production token, RAM or
latency savings. The reserve gates derived-cache payloads; it does not govern all
other application or filesystem writers. No new model requests, paid fallback,
quota changes, hard RAM limits or embedding-service actions are introduced.

The v0.3.2 release and its archive remain immutable. This post-release change is
identified separately on main and passes fresh full-patch compatibility checks
against the same pinned upstream revision before publication.


## v0.3.3: storage pressure and idle-only update safety

The cumulative patch now contains 300 source/test files, including 122 native
Python test files. A fresh combined run passed 144 native cases across 15
relevant files with zero failures and zero retries; two existing platform cases
were skipped on the test host. The 75 companion cases are checked separately.
Earlier overlapping results above are historical and are not added to this count.

Two reproduced predicate failures showed that unreadable background-process or
delegation observations could be interpreted as idle. The predicate now keeps
the host awake on either failure. The new opt-in control request uses a separate
verb, so an older server cannot ignore an idle condition and silently run the
legacy bounded-drain request. Admission checks native work on the Gateway loop
immediately before restart. Old explicit pause behavior remains covered.

New control tests use the production socket setup and a real native registry
process: an idle-only update is refused while its script is alive, then the same
script resumes and finishes after release. Other cases cover active agents,
unreadable cron/API work, clean idle acceptance, older servers and expired queued
callbacks. The first legacy test harness used a different temporary home than
the serving socket; correcting its home made the unchanged legacy control pass.
That harness failure is not counted as a runtime defect.

Local publication backs up only affected source files and records prior absence
for a new sibling. Bootstrap of the first strict-capable server requires a fresh
idle audit; future automatic activation requests require its strict ACK and do
not fall back to signals or legacy pause. Serving-process identity, canonical
source binding, file hashes and unchanged configuration are verified separately.
No model calls or live workload are created to manufacture acceptance.

The prior two native completed-card samples have incomplete log coverage and
predate these fixes; they do not establish after-patch RAM, latency or usage
savings. Production impact and autonomous goal/skill behavior remain separate
acceptance work. Public archives contain source/examples only, never private
operational receipts, live databases or credential stores.

## Native Captain goals and delegated decisions (v0.3.4)

The Captain policy and new on-demand goal-driven-execution skill describe authority for reversible implementation choices, bounded correction, parallel ready work and verified delivery. Material scope/cost/access/irreversibility and rights/review/publication decisions retain their gates. This is guidance within existing native permissions, not a guarantee of autonomous model behavior.

The native `hermes goal status|show|ensure` command uses the current bound session/profile and existing GoalState/contract store. Self-setting defaults off and requires profile opt-in. It preserves active/paused/cleared goals, existing caps and concurrent owner changes. Status avoids transcript/system-prompt materialization. Setting metadata invokes no judge, kickoff, dispatch or model. The CLI refreshes goal state at its existing post-turn boundary, preserving cached state and skipping evaluation if observation fails.

Final new-file acceptance: **26 native tests passed, zero failures**, with zero retries. Controls cover actual SQLite state/contract persistence, parser integration, profile/session scope, missing/closed sessions, disabled profiles, preserved pauses and budgets, concurrent writes, worker refusal, bounded stdin, stale CLI state and a committed write whose readback fails. The initial adoption harness used the wrong mixin; after correction, all three stale-state cases failed against the unchanged implementation and passed with the fix. A separate full relevant goal/parser run passed **182 cases in eleven files**, including the earlier 25-case revision of the new file. These overlapping results are not added together.

Installed-source acceptance used native read-only session metadata and skill discovery/view with network denied. Existing retained paused goal metadata remained byte-identical; when its session record was absent, the helper correctly refused to reactivate it. A current existing open session was inspected without setting a test goal. The profile changed only its explicit self-management permission plus generic instruction/skill content; models, quotas and existing turn caps were preserved. Source-only rollback backed up approximately 529 KB of source and two small profile files, with no database snapshot.

No model request or live synthetic worker was used for these checks. Skill discovery and metadata inspection do not prove that an existing cached Captain has already read new guidance or completed autonomous work. Use normal authorized work to establish that evidence, and retain the idle activation and prompt-prefix constraints described in the goal guide. The patch inventory now contains 305 source/test targets: 182 runtime files and 123 Python test files. Historical acceptance counts above remain historical.

## Atomic continuation controls (v0.3.5)

Native goal, heartbeat and loop migration previously used separate best-effort child-copy and parent-clear writes. The save functions suppressed write errors, so migration could report success and clear the parent after a refused child write. Refusing the parent archive could instead leave both rows active. An unreadable child value could also be mistaken for absence and overwritten. Real temporary SQLite triggers and simultaneous native writer calls reproduced these failures before implementation; no live incident or model request was created.

The three existing migration entrypoints now use one native SessionDB transaction. Reads, exact child-value insertion and parent archival share the native writer's lock, commit/rollback and storage-identity guards. Any existing child metadata is preserved, including cleared or unreadable state. Pauses, counters, caps, waits, routing and unknown checkpoint fields remain intact. Concurrent continuation attempts commit at most one child. A failed or unconfirmed transaction returns false; it is not permission to replay compression or model calls. Compression itself retains its existing best-effort behavior. Recovery of continuation scheduling after persistent storage failure still requires normal-work evidence; this change protects durable state and does not establish automatic recovery for every storage fault.

Fresh native acceptance: **228 passed, zero failures, six files, zero retries**. This includes **30 new cases** for child/parent write refusal, full rollback, existing child data, active/paused/done/cleared states, concurrent continuations and profile isolation. The other files exercise existing goal, heartbeat, loop, self-goal and real compression-rotation paths with model boundaries replaced offline. The new file initially produced 23 failures and seven passing controls on the unchanged implementation; those overlapping development runs are not summed.

Installed canonical-source acceptance passed **12 cases** using an explicitly isolated native store, with network denied and no live goal changes. Existing source baseline bytes were reused for rollback: **132,249 bytes** covering three original files plus one original absence, without a database snapshot. All 97 observed config/SOUL hashes stayed unchanged during installation.

A trace of the actual native SQLite writer measured these successful single-migration workloads:

| Control | Before committed transactions | After committed transactions |
|---|---:|---:|
| Goal | 2 | 1 |
| Heartbeat | 2 | 1 |
| Loop | 2 | 1 |

This is an offline transaction-count measurement, not production usage, disk-byte, latency or RAM savings. The observed retained live orphan-goal metadata has not been attributed to this failure class and was left unchanged. Current public inventory: **309 source/test targets**, including **185 runtime files and 124 Python test files**. Historical acceptance above remains historical.

## Local memory attribution (v0.3.6)

The private Gateway control socket now accepts an explicit `memory-stats` request.
It reads scalar process/cache/tool/registry observations without formatting cached
values, opening a session database, trimming memory or starting inference. Normal
status stays unchanged. The optional allocation query observes an existing Python
profiler; it never enables one. A registered native startup option permits a
deliberate idle profiling window and defaults to disabled. The Gateway's runtime
settings initialization moved into a small sibling, reusing one effective config
snapshot for timing and diagnostic settings while retaining existing getters.

Fresh native acceptance passed **72 cases across nine relevant files**, with
zero failures, zero retries and **one legitimate skip**. Eighteen passing cases
in the new file cover real local-socket dispatch, private-value exclusion,
nonblocking registry counts, unavailable SQLite tracking, no database/trim side
effects, allocation-path sanitization, bounded startup settings and real native
Gateway configuration consumption. The SQLite allocator integration case skips
when the host extension does not export the required symbols; a skip is not a
successful allocator measurement. Companion examples/tools are checked separately
and historical overlapping test counts are not added.

Installed-source acceptance observed the actual Gateway through its native local
socket after an idle-only lifecycle change, matched the runtime source inventory
and preserved configuration. A temporary startup profiling window produced
aggregate allocation metadata without a model request. Returning to a normal
process was verified separately. Profiling itself consumes RAM/CPU; its overhead
must not be presented as a leak, workload speed or savings. These observations
identify areas for further investigation and do not establish a root cause or
production reduction in memory, tokens or latency.

The cumulative inventory contains **312 source/test targets: 187 runtime files
and 125 Python test files**. Full patch compatibility is checked against the same
pinned upstream revision. Public release artifacts include generic source,
examples and documentation only; private runtime measurements, configuration,
backup files and operational receipts remain excluded.

## Reuse immutable bundled locale parses (v0.3.7)

An isolated native 36-home workload reproduced repeated parsing of the same
bundled English source. Every home retained a separate set of flattened keys and
translation strings even though the file was unchanged. Three new tests first
failed on repeated profile reads, overlay resets and concurrent cold loads; five
other controls already passed. Sharing whole merged catalogs would mix private
overlays, and sharing plugin modules would change plugin state isolation, so
neither is part of this repair.

A small sibling now reuses the native parser's immutable result for a verified
source file. A serialized standard-library LRU retains at most 32 source versions;
file identity, size, modification/change stamps and ownership/mode invalidate its
key. Each caller receives a new mutable dictionary. Existing overlay/plugin
precedence, missing-file fallback, packaged locale roots and error reporting are
preserved. No configuration switch, provider route or model tool was added.

One offline reproduction before and after the change measured this specific
cold locale-loading path:

| Measurement, 36 homes | Before | After |
|---|---:|---:|
| Bundled file parses | 36 | 1 |
| Distinct mutable catalog dictionaries | 36 | 36 |
| Retained traced Python bytes | 29,041,096 | 6,687,904 |
| Elapsed seconds with allocation tracing disabled | 5.308 | 0.161 |

The retained-allocation difference is 22,353,192 bytes (about 21.3 MiB) in this
synthetic workload. Timing and allocation measurements use separate processes;
the timing row excludes profiler overhead. These single-run results describe
this path, not overall Gateway startup, provider response time, token use or
all production RAM. No inference or live task was created for measurement.

Fresh combined native acceptance passed **163 cases across fourteen relevant
files**, with zero failures, zero retries and one existing SQLite-symbol skip.
This includes eight new locale cases and two new observation cases. Controls
cover private overlays, caller mutation, same-size edits with restored mtime,
atomic replacement, packaged roots, concurrent reads, failed/missing sources,
bounded reuse, plugin precedence and CLI/TUI/Gateway consumers. Historical
overlapping runs are not added to this count.

Installed canonical-source acceptance compared all 3,433 entries across 36
isolated native catalogs and verified overlay isolation, with network/process
actions and live-state reads denied. The first acceptance harness refused a
required managed Python library read before reaching behavior checks; permitting
only the interpreter's declared library directories corrected that harness.
No runtime workaround or dependency change was needed.

After native idle-only activation, the actual Gateway's local observation showed
one populated bundled cache, one computation miss and repeated hits. The new
counter reads an already-loaded cache and exposes no paths, translation values or
profile identities. Runtime source hashes, source permissions and unchanged
configuration were checked separately. Process RSS snapshots across a restart
are not a controlled production savings benchmark, so no causal whole-process
reduction is claimed from them.

Only affected source files were backed up; no database snapshot was made. The
complete inventory is **315 source/test targets: 189 runtime files and 126 Python
test files** against the same pinned upstream revision. Release files, reachable
history, metadata and archives undergo the existing privacy review before
publication. User goals/pauses, quotas, accounts, models, project gates and
embedding services remain outside this change.

## Share immutable bundled plugin code (v0.3.8)

Native plugin discovery followed by Gateway configuration materializes platform
adapters under separate profile namespaces. A four-home reproduction created
328 modules from 82 source files with no messaging platform enabled. The dominant
allocation site was Python's repeated bytecode decoding. Module isolation is
intentional: sharing module objects or skipping configuration hooks would change
behavior. This repair shares only immutable compiled code and its constants.

Eligible bundled imports use Python's existing per-directory importer cache with
a bounded source loader. Each execution receives a new native module/globals
dictionary. Source paths, content digests and interpreter optimization distinguish
code versions; current source access is checked on hits. Changed files cannot
inherit stale timestamp-only bytecode. Old sibling modules remain unchanged until
their own reload. Native private-plugin imports, host routing, custom importers,
extension/sourceless loaders, permissions and activation/registration gates are
preserved. The cache does not store module globals or live configuration.

A controlled offline comparison ran the original loader and the installed
candidate's logic in fresh processes, with networking and process actions denied
apart from native checkout-local read-only version metadata. The original loader
was observed loaded before restoring the isolated development checkout; canonical
runtime source was not changed by the baseline experiment. Both workloads served
36 synthetic homes, materialized 2,952 scoped modules from 82 source files, kept
the same registry/compatibility outcomes and enabled zero messaging platforms.

| Untraced offline workload, 36 homes | Original | Candidate |
|---|---:|---:|
| Process RSS after discovery/configuration | 486,899,712 bytes | 224,198,656 bytes |
| Process PSS at the same stage | 475,310,080 bytes | 212,675,584 bytes |
| Elapsed discovery/configuration | 10.161 s | 8.985 s |

This single-run workload observed about **250.5 MiB less RSS** and a shorter
component startup time. Allocation tracing was disabled for these rows. The first
cold profile incurred extra compilation/allocator cost; benefits are established
for this multi-profile reproduction, not every single-profile process, end-user
response time or token usage. The cache retains at most 128 code versions and
loads sources above one MiB without caching; it is not an application-wide RAM cap.

Fresh native acceptance passed **242 cases across thirteen relevant files**, with
zero failures, zero retries and one existing SQLite-symbol skip. Four initial
reuse/reload tests failed on the prior implementation; a later initializer control
also failed before its corresponding change. The new file now passes fourteen
cases covering independent scopes/state, nested imports, force reload, same-size
edits with restored mtime, unaffected siblings, concurrent loads, current source
read refusal, custom finders/loaders, large sources, failure cleanup, sourceless
imports, cache eviction and private-plugin passthrough. Two new diagnostic cases
verify count-only observation and no initialization of an absent cache. Existing
plugin lifecycle, historical compatibility, event, host-isolation, registry and
config-loader tests are included; earlier overlapping runs are not added.

Installed canonical-source offline acceptance separately verified code reuse,
independent profile state, fresh reload and preservation of a sibling's old code,
with live-state reads and network actions denied. Native idle-only activation then
produced positive code-cache reuse counters from the actual Gateway. Runtime
source hashes and unchanged configuration were checked. Idle RSS snapshots across
that restart are operational observations, not a controlled benchmark for every
production workload. No inference work was created to obtain evidence.

Only three affected runtime source paths were installed after small source-only
backups; no database snapshot was made. Cumulative inventory: **318 source/test
targets, including 191 runtime files and 127 Python test files**, against the same
pinned upstream revision. Public files, reachable history, metadata and release
archives are reviewed before publication; private measurements, source locations,
configuration, credentials and operational receipts remain excluded. Quotas,
models, accounts, goals, user pauses, project gates and embedding services are
unchanged by this source repair.

## Trustworthy compact bot activity (v0.3.9)

The cumulative inventory now has **332 source/test targets**, including **131
Python test files**. This update fixes three reproduced presentation boundaries:
compression-tip rows retaining root activity fields; worker projections omitting
bounded detail and terminal time; and recently completed/offline workers still
qualifying for worker-driven activity. Bot rows now use the native tools icon
with a short description and a full localized tooltip, keeping the canonical
conversation preview and opening route unchanged.

Regressions were observed failing before implementation. Fresh offline native
acceptance passed **64 cases across seven files**, with zero failures or retries.
Separately, **67 renderer cases across six files** passed, including canonical
opening, no pre-warm on paint, terminal/offline behavior and locale coverage.
The renderer type check and production renderer build passed; the changed scope's
native code-health comparison reported zero new findings. These are separate
checks, not a sum of historical suites.

The installed native source was then checked with **nine cases across two files**
using the canonical runner. This is a subset repeated against the installed
location, not nine additional unique cases. Only selected source/test files were
published locally; permissions and ownership were restored, configuration hashes
were preserved and no database backup/restore was performed.

Browser validation used actual native components, production-generated styles
and synthetic data. Active detail, terminal clearing, offline exclusion, title
fallback and unchanged canonical preview were verified; the final observed
console had no errors or warnings. Private fixture issues were corrected without
changing production behavior: home isolation was incomplete, a generated Vite
cache was eligible for source transformation, and rebuild output was being watched
as fixture styles. The same 2 GiB child heap cap was retained; no dependencies,
model requests, quota settings or paid routes were added.

Native worker recency is not process-liveness proof. No end-to-end live workload
or model-token saving is claimed from this UI change. The current local source
is installed, but activation of the already-open Desktop and Gateway remains a
separate idle-lifecycle check; the redesigned Workbench mockup is not deployed.
Historical benchmark and regression counts above remain separate.

## Metadata-only runtime bindings (v0.3.10)

The cumulative patch now has **333 source/test targets**, including **132 Python
test files**. Small model-config reads no longer hydrate a session's full system
prompt or tool context. The full-session reader and existing runtime binding
semantics are preserved; this is a projection change, not an additional cache.

Two native read-policy regressions first failed on the previous implementation
when SQLite denied prompt access. Fresh acceptance passed **73 cases across seven
files**, with zero failures or retries. The new file contains three cases:
normal/read-only thread binding under the read policy, plus default/null/nested
value and committed-update controls. Existing read-pool, session-route and
onboarding consumers are covered by the wider run. The scoped native code-health
comparison found no new findings.

The same three new cases then passed against the installed canonical source.
This installed check is a subset, not three additional unique cases. Installation
changed one source file and one test file after fresh idle/ownership checks, with
a small source-only rollback, exact permission restoration and unchanged
configuration. No database copy or restore was performed.

The [isolated measurement](session-metadata-reads.md) uses a synthetic context and
reports lookup time and traced Python allocations only. It does not establish a
whole-process RAM, production token, total response-time or billing improvement.
No model call or provider/allowance probe was made for this change. Existing
quotas, fallback policy, session models, user gates and embedding services remain
unchanged. Runtime activation is a separate native idle-lifecycle observation.

The new release inventory carries its own version label; earlier immutable tags
and archives are not rewritten. The redesigned Focus/Workspace interface remains
an interactive prototype and is not included as a deployed redesign in this
source release. Prior overlapping test counts remain historical.


## Native Focus and Workspace (v0.4.0)

The exported patch now contains **352 source/test targets**, including **134 Python test files**. Unlike the earlier prototype-only work, this release contains native renderer components and an owned-session configuration intent. The original composer, transcript, bot roster, layout tree and plugin routes remain in use.

Fresh UI acceptance passed **85 cases across ten files**, with zero failures. These cover navigation and native session doors, late plugin registration, separate layout scopes, goal drafts and explicit saves, busy/stale refusal behavior, Ctrl/Cmd+Enter containment, unknown evidence and existing session-control behavior. A render regression exercises 100 unrelated streaming updates without another shell commit or an implicit read while Catch up is closed. This is a component-level observation, not a whole-app speed or token measurement.

The native session-control file passed **31 cases**, including the new goal form, preserved counters/gates/waits, busy refusal, stale revision, declared input shape, configured turn limits and malformed-limit refusal. Generated TypeScript/OpenRPC checks also passed. A wider goal-command/gate run passed during development; its overlapping counts are not added here.

Renderer typechecking and the production renderer build passed. The scoped before/after code-health comparison covered 23 changed files with no new blocking or advisory findings. No dependencies, account bindings, quotas, fallback routes or embedding services were changed.

Rendered review used the actual native presentation components with synthetic data and no live transport. It covered desktop Focus/Workspace, goal and feature dialogs, and 320/360-pixel child viewports. Review found and corrected a wrapped rail caption, crowded secondary form fields and narrow-screen navigation overflow. Browser tests used a test-only registered language pack to check the Thai strings; production language selection was not altered. The desktop package was built using existing admitted tools and verified staged assets; replacing or loading an already-open app remains a separate graceful idle-lifecycle step.

English guides and the complete cumulative patch are distributed; private host reports, configuration, conversations and screenshot fixtures are not. Public files, all reachable Git history, and the exact release archive are reviewed before publication. Companion/archive acceptance is recorded separately from native regression evidence. Real workload billing, cross-bot cache sharing and live model behavior are not inferred from these tests.


## Goal draft ownership (v0.4.1)

An offline native-component regression reproduced a dismissed Goal draft appearing in a second chat when both chats already had cached, empty control snapshots. Empty native controls legitimately share an empty state revision, so a revision check alone cannot identify which chat owns an unsaved form.

The editor now starts a separate component instance when its pinned runtime session changes. Reopening it in the same chat still retains the dismissed draft; opening it in another chat starts from that chat's native goal state. Background state updates continue to leave the open, pinned draft alone. No model prompt, automatic goal start, quota change or new persistence store was added.

The regression failed before the change and passed afterward. The relevant UI suite passed **85 cases across ten files**, with zero failures; this run overlaps the v0.4.0 evidence and is not an additional 85 independent cases. The full renderer TypeScript check passed, and the two-file native health comparison reported zero blocking or advisory findings. Native Python behavior was unchanged and its earlier suites were not repeated. Desktop package loading remains a separate graceful lifecycle step.


## Per-Captain setup checks (v0.4.2)

This documentation update makes profile-scoped goal opt-in and skill discovery explicit for every intended Captain, including the terminal's current launch home. A Desktop selection does not select the terminal profile. The native source patch, its 352 targets and all default permissions are unchanged. The guide supplies a short on-demand instruction pointer instead of copying the whole execution method into every conversation prefix.

A separate local adoption check used the native configuration writer to enable only the requested profile's self-management permission. A raw semantic comparison preserved every other configuration value, including model/provider settings and existing limits. The existing published skill was installed without modification, and native skill discovery/view resolved the exact published bytes. Session-database access and network/model actions were denied during those checks; no goal was created, resumed or replaced. A plugin initializer was refused by the strict inspection guard, so this is not whole-plugin runtime acceptance. Existing file permissions and process identities were checked separately.

These are configuration and discoverability results, not evidence that a cached Captain has consumed the guidance or completed autonomous work. Actual behavior still needs a normal authorized task. No source or UI suite was repeated for this documentation-only update. Earlier test counts remain historical; exact release inventory, archive, privacy and Git-history checks are performed for this release.


## Compatible startup checker reuse (v0.4.3)

The cumulative inventory now contains **354 targets**, including **135 Python test files**. One runtime source file and one regression file extend the prior release. A selected PM checker can belong to a different launcher scope while a matching published checker remains cached. Previously, no-bootstrap resolution refused that cache and bootstrap resolution tried preparation. Two regressions reproduced those behaviors before the fix.

The resolver now reuses an exact compatible published generation under the existing preparation lock and child lease, without rewriting the current selection. The native application dependency check still decides whether dependencies are current. The regression matrix covers no-bootstrap and bootstrap cache hits, selected-generation priority, corrupt/non-object/missing/mismatched publication metadata, directory/marker symlinks, unusable interpreters, selection preservation and collector protection.

An eight-file native PM/source-launch run passed **55 tests**, with zero failures and one existing Windows-only skip on Linux, using the canonical per-file runner with zero retries. After a test-only table refactor required by code health, the final new regression file passed all **10 cases**. A separate existing symlinked-home alias regression passed. These runs overlap and are not summed. No dependency bootstrap integration test requiring installation was executed. Scoped code health reported zero new blocking or advisory findings.

After a guarded two-file local source adoption, an actual native `venv_is_current` request under the existing Desktop wrapper runtime scope returned true where the preceding observation had returned false. It used one preexisting unselected compatible checker and the normal native read-only worker. PM selection, application environment selection, dependency facts, lockfiles and 99 guarded configuration/skill inputs stayed unchanged; no PM generation was created. The normal validation/worker lease mechanism was allowed. Desktop/Gateway identities were preserved. No model request, service restart or additional Desktop launch was performed.

This establishes repair of the false stale-dependency check. The earlier observed launch delay is not assigned entirely to this defect, and no end-to-end latency or token saving is claimed. The next normal launch and authorized work remain the acceptance path for those measurements. Public payload, history, archive and identifier/credential review are performed separately before publication.

## Native work-surface correction (v0.4.4)

The original Focus release changed navigation, but a real user report showed that the old Sessions navigation and a dense Kanban still competed with it. New regressions reproduced 2,000 completed cards mounted on the current-work canvas, the Sessions pane remaining open beside Work, mismatched Models/Usage destinations and a Bots rail selection that did not follow the actual visible pane. These cases failed before correction.

The cumulative export now contains **369 source/test targets**, including **135 Python test files**. The patch retains the same pinned upstream base. It changes native presentation and navigation, not credentials, quotas, task ownership, dispatch or model routing.

Current offline acceptance: **483 cases passed across 66 native UI test files** covering Focus, the real sidebar and Kanban components, compact Intro, and affected existing fixtures. The navigation file was rechecked after a TypeScript-only fixture correction. TypeScript checking and the scoped 21-file code-health ratchet passed. These overlapping runs are not added together.

A broader UI run completed with 10,911 passing cases, five failures and two asynchronous fixture-teardown errors. The identified title/fixture problems were corrected and their targeted tests passed. A later full run ended with SIGTERM before its summary, for an unproven reason. This release therefore does **not** claim an all-upstream UI-suite pass. Existing storage/provider/dialog fixtures retain their behavior assertions; no failing test was removed or weakened to force a green result.

A separate real Electron main/preload/renderer and real native backend were launched with disposable home, user-data and account directories. **40 entry/interaction checks and 71 settings subpages passed** after waiting for each actual surface. Checks included the parked fixture card's native detail dialog, search and restoration, empty History return, New task open/cancel, feature search, Models/Usage selection, Bots highlighting, and laptop-width rendering. No renderer exception or failed native HTTP response was observed in the final journey.

The fixture task was explicitly blocked and unassigned in the disposable database. It had no worker, run, fabricated completion or production receipt. Model metadata requests went only to a local test server; inference endpoints were not called. External backend networking and optional tool installation were denied. Earlier harness attempts had readiness, viewport and navigation-selector mistakes; their failures were retained privately and are not counted as application regressions or passing acceptance.

This is real isolated-app acceptance, **not** hands-on control of an existing production window. It does not test authenticated provider calls, paid fallback, sending messages, execution/scheduling, downloads, audio, GPU work or destructive actions. Hosted catalogs and update checks can report unavailable under offline guards. Opening those screens is not proof of their external services. Deployment still requires a normal idle lifecycle; source or staged-package readiness does not prove that an already-open Desktop loaded the correction.

No prompt, production screenshot, session/task/run identity, machine-specific test launcher, private log or account data is distributed with this record. The public patch contains portable native component regressions. No model call, quota probe, new dependency or paid fallback was used to produce this acceptance.

## Native Spaces, Workflow and richer chat (v0.5.0)

The cumulative patch contains **413 source/test targets**, including **138 Python test files**, against the same pinned upstream base. Workflow exposes actual dependency edges and recorded attempt history. The full Bots workspace and one Focus rail use native navigation. Library disables unready previews; chat retains native Markdown/Mermaid with optional literal-data cards. Spaces adds explicitly shared local pages/file copies and read-only member access.

| Acceptance | Result | Boundary |
| --- | --- | --- |
| Relevant native UI tests | 201 passed across 34 files | Workflow ancestry/history, navigation, preview transport, answer cards, session-picker clicks and Spaces |
| Current native Python tests | 38 passed, 6 platform skips across 3 files | Board API, filesystem and Spaces; canonical runner, zero retries |
| TypeScript | Passed | Complete Desktop typecheck |
| Scoped code health | No new blocking or advisory findings across 47 paths | Compared with exact prior installed bytes/absence |
| Isolated real Electron UI | 55 flows and 71 settings pages passed | Actual main/preload/renderer and native backend with disposable homes |
| Model calls / external-app opens | 0 / 0 | Inference POSTs counted; external application opening refused and counted |
| Renderer exceptions | 0 | Final candidate journey |

Native UI checks covered fork/join dependency paths, recorded bot attempts, selection of a destination's upstream path, native-card opening, missing/archive files disabled before preview, text/nested folders, sanitized HTML, PDF, audio, images, Bots groups/search, session selection with a stationary pointer, a real native chat displaying a table/cards/Mermaid, and desktop/narrow layouts. The recorded task attempts are canonical native test fixtures; no bot or worker was spawned and no production execution receipt was manufactured.

Spaces acceptance created a Space with two explicitly selected profiles, wrote a page, imported a chosen fixture file, opened it internally, removed it after confirmation, restored it and verified the original file bytes stayed unchanged. The owned test app's file-chooser selection was supplied by the harness; actual native file reads, import API, storage, preview, trash and restore were exercised. Separate backend regressions use two genuine named-profile environments to read the same canonical store/content hash, deny a nonmember and a revoked member, reject stale writes, bound text reads and refuse export overwrite. This proves API/CLI policy on test profiles, not operating-system isolation or a live model's behavior.

A delayed preview arriving after switching Spaces is discarded. An actual stationary-pointer session selection failure was reproduced in the isolated app and fixed at the native command-menu pointer policy, rather than forcing the test to click through it. Earlier harness launch/profile-seed and double-serialized preview-body failures were retained privately; the final real journey passed after correcting them. Existing wider upstream-suite limitations from v0.4.4 remain in force. Earlier overlapping counts are not added to this acceptance.

No production conversation, screenshot, task/run identity, credential, machine-specific launcher or private log is shipped. Source adoption, packaged build, fresh-process activation and isolated interactions remain distinct evidence. No direct production-window visual control is claimed where enabled native controls are unavailable. No model request, allowance probe, dependency installation, quota/fallback change or embedding-service action was used for this acceptance.


## Unified Hub and persistent Focus sidebar correction (v0.5.1)

A real user report identified the exact trigger: pressing the old top-left sidebar toggle restored the legacy Sessions/Bots column despite the new Focus rail. Two offline regressions reproduced it through the real positional layout action with an already-closed sidebar preference and through the actual titlebar control. Both failed before the correction.

Focus now omits the old titlebar trigger, refuses the legacy positional/sidebar toggle actions in the main window, and observes the actual collapsed-side state in addition to the old per-pane flag. Wide and secondary-window controls keep their existing behavior. A separate real-store regression reproduced a stale Focus listener closing the Wide sidebar during the mode switch; the callback now rechecks the current mode before closing anything. Its draft-preservation and mode-switch cases passed, including a real isolated-app round trip. The layout scope, sessions, draft text and running backends are not destroyed to hide a panel. Existing right-side/flip/persistence tests retain their behavior checks.

Hub combines Library chat outputs and shared collection items in one destination, header, search and type filters. Named collections retain explicit bot membership; chat outputs are not automatically copied or shared. Existing `/artifacts` and `/spaces` links resolve to the Hub surface. The new owner aggregate returns at most 1,000 non-trashed metadata records in one query, with no content bytes or bot CLI privilege change. The existing bounded transcript index and native file viewers are reused.

Fresh acceptance: **97 native UI tests across 16 files**, **35 native Python tests with six existing platform skips across two files**, complete Desktop typecheck, and scoped health checks across **20 paths** with no new blocking/advisory findings. An isolated real Electron/backend journey passed **57 flows and 71 settings pages**, including the missing titlebar trigger, sidebar keyboard action, mixed-source search, internal previews, collection membership, import, trash and restore. No inference POST or external application open was used. An initial harness expected an exact page name without its new collection-provenance caption; correcting the accessible-name match exercised the same real control successfully.

The cumulative export has **419 source/test targets** and the same pinned upstream base. Companion and fresh-checkout patch acceptance are regenerated separately. Earlier overlapping counts are historical, not added here. No model prompt, toolset, quota, fallback policy, user gate or embedding service is changed. Source installation, package preparation, graceful activation and isolated visual checks remain separate evidence.

## Main-window history access and quiet Slack status (v0.5.2)

The remaining sidebar trigger was reproduced in main Wide mode. It is now omitted in both main modes, and the legacy column stays closed through mode changes and the sidebar shortcut; secondary-window controls keep their native behavior. A direct History door restores saved-chat access without bringing back the crowded column.

A native database regression seeded an older conversation followed by 205 newer ones. The prior route ignored the requested search and returned 50 newer records; the corrected route finds the original saved title or ID. History requests bounded 50-row pages, searches only after explicit submission, surfaces read errors, and binds results/cache/selection to the captured connection and profile. A delayed old-owner response is discarded. The isolated real application searched and opened the older saved transcript by its existing ID without inference.

The Slack regression exercised the actual base-adapter/runner lifecycle with an in-memory wire transport. Turning off automatic status notices previously still sent the paused boilerplate; it now emits nothing while the emergency stop remains engaged. Default-on behavior, other-platform notices, recognized control commands and multiplexed per-profile notice routing retain their tested contracts. This is offline wire-policy evidence, not a live Slack delivery test.

Fresh verification covers 203 native Python tests for the history route and existing web server, 10 relevant Gateway tests, the targeted native UI tests, complete Desktop typecheck, and 19-path scoped health with no new blocking/advisory findings. An isolated real Electron/backend journey passed 58 flows and 71 settings pages with zero renderer exceptions, inference POSTs or external application opens. These counts describe separate suites and are not combined with previous overlapping acceptance totals.

The cumulative patch contains 432 source/test targets against the same pinned upstream base. Production adoption, graceful Gateway reload, packaged Desktop activation and isolated UI interaction remain separate evidence. No production conversation, credentials, Slack message identifiers, private configuration, screenshots or cleanup reports are exported. Companion tests and fresh pinned-checkout patch acceptance are regenerated separately before publication.


## Native feature parity and older-search pinning (v0.6.0)

Twelve gaps were confirmed by a separate read-only comparison of the original interface, native routes/actions and the new presentation. The release restores the full saved-chat/project manager in both modes; native history row actions, filters, pins and archived view; bot/group/section/Screen entries; visible device/profile context; combined goal/loop/heartbeat controls; pane/status-only plugin discovery; cache accounting display; and friendly route labels. See [the usage matrix](desktop-feature-parity.md).

Fresh final UI acceptance: **34 files, 303 tests passed, zero failures**. This includes profile/connection routing, project creation and native project/worktree menus, bot sections/groups, Screen identity boundaries, plugin registration/error isolation, session actions and pin synchronization, cache unknown/invalid/zero arithmetic, retained drafts, and delayed control submission bound to the original chat. Historical overlapping runs are not added to this total. Type checking passed. Scoped source-health review reports zero blocking findings and zero advisories against this change's baseline.

The actual isolated Electron main, preload, compiled renderer and native backend passed **21 interaction steps**, with zero inference POSTs, zero unexpected external applications and zero renderer errors. Checks include search outside the newest 200 rows, native row menus, an actual older-chat rename/pin, filters, a single project dialog, native bot/group forms, actual local section creation, the New Bot palette path, context selection without changing owner, synthetic pane/status plugins, a disabled-plugin boundary, provider-reported cache display from synthetic counters, combined paused goal/loop/heartbeat state, Focus/Workspace and a narrow viewport. Some earlier UI harness selectors used a visible caption instead of its accessibility name; corrected selectors are retained separately from the product regression.

The interaction review exposed an additional product defect: a search-only older conversation lost its visible pin after search was cleared. Regression tests first reproduced dropped profile metadata and the absent adoption path. The repair retains the native search owner and makes the row available before existing pin synchronization. The final native rename/pin journey passes. Fresh loaded records and a same-ID record belonging to another profile are preserved.

The cumulative patch contains **466 source/test targets**, including **326 paths outside the Python test tree and 140 Python test paths**, against the unchanged pinned upstream base. Private production source adoption changes 47 exact files, preserves 99 configuration/instruction inputs and existing process identities, and copies no databases. Packaged activation remains a distinct graceful-lifecycle step. Gateway/backend routing and scheduler code are unchanged by this UI release.

These checks do not authorize or prove a native introductory model call, remote Screen connectivity, real private-monitor behavior, production cache savings or cross-bot cache sharing. The model-free form checks open and cancel native bot creation. Private installed plugins are inspected for registration compatibility; synthetic plugins test their registration shapes without executing private behavior or enabling a monitor. Existing pause, quota, review, owner and no-paid-fallback gates remain in force. No local embedding service is changed.


## Always-visible workspace context (v0.6.1)

The owner requested device/profile information on screen without opening an information popover. Eight source/test paths replace that dialog with a permanent context row above the native workspace. It displays real device/profile names and existing gateway connection state; the named profile selector invokes the established native selection action only after an explicit different choice. No new polling, profile fetch loop, model call or provider configuration is added.

Fresh offline acceptance: **11 files, 46 tests passed**; type checking and scoped source-health review passed. Regressions cover immediate visibility, native status updates, display-name updates, exact canonical profile selection, no owner action on mount or opening, no reset when reselecting the current profile, pending-selection refusal, placement outside the rail and retained native chat drafts. Existing connection-selector cases cover its routing and confirmation paths.

The real isolated Electron main/preload/compiled renderer/native backend passed **7 checks**, with zero inference POSTs, external application opens or renderer errors. It verifies the visible values before any click, readable checked menu entries, Focus/Workspace placement, opening an existing transcript and retaining an unsent draft. A 560-pixel responsive context check lowers the minimum window size only in the disposable QA application, then verifies the actual inner width and lack of context-row overflow; it does not change production minimum window settings or certify the entire app for mobile use. Light/dark screenshots are private QA evidence.

The cumulative patch now contains **469 source/test targets**: **329 paths outside the Python test tree plus 140 Python test paths**. Exact source publication, native package construction, graceful lifecycle activation and isolated UI interaction remain separately recorded. Existing runtime identities and 99 configuration/instruction inputs are preserved during source publication. No database copy or restoration, allowance probe, paid fallback or local embedding-service action is performed.


## User-perspective usability repairs (v0.6.2)

The review repaired nine usability areas: preview Back/history, full-history search discovery, Workflow fit/focus, explicit model usage at bot creation, skill selection and footer visibility, scoped Hub no-match recovery, reported bot model/provider badges, visible New chat and compact permanent context. Further interaction review removed automatic chat/profile navigation from create-only bot creation and delayed graph focusing until its layout is committed.

Offline regression coverage includes real native component behavior, profile/revision boundaries, exact-query search handoff and deliberate create-only versus introduction choices. Native isolated Electron acceptance uses more than 200 saved conversations, 17 task cards and installed skills, with inference denied. See the [usability guide](desktop-usability.md) for the actual controls and limits. UI checks do not certify remote Screen access, live provider authorization or production savings.

Final acceptance for this release: **15 UI files, 58 tests passed**, scoped source-health review reports no new findings, and renderer type checking passed. The actual isolated Electron main/preload/renderer/backend passed **10 journey checks** at 1280×900, 1280×720 and a 640-pixel narrow fixture viewport, with zero inference POSTs, renderer errors or external-application opens. A real disposable bot was created with introduction off, retaining the current profile and returning to the bot cards. The context row measured 45 pixels at laptop height, down from the reviewed 74 pixels. These results establish behavior in the isolated test; they do not establish production performance savings. The cumulative patch contains **479 source/test paths**, comprising **339 outside the Python test tree and 140 Python tests**.


## Follow-up interaction review (v0.6.3)

The baseline isolated UI reproduced three new behavior defects: Zoom out increased a fitted graph from about 27% to 35%, a repeated New chat retained the same unsent draft/tab, and Escape discarded an unsaved Hub document. The native create/preview/trash/restore lifecycle already worked and is preserved. Membership discovery and current-navigation/short-window access were also improved.

Final offline coverage: **9 UI files, 45 tests passed**; renderer type checking and scoped source-health review passed. Tests cover monotonic zoom, material discard confirmation, pending-save input locks and refusal retention, local member search with hidden/absent selections, route indication, exact native action forwarding and unchanged plugin restrictions.

The actual isolated Electron main/preload/renderer/backend passed **7 checks**, including the initial shell and six interaction journeys, at 1280×900 and 1024×600. The real disposable membership write, page save, edit discard, trash/restore and draft-preserving new tab all passed. Inference POSTs, renderer errors and external-application opens were zero. Source installation, package readiness and native activation remain separate evidence; these isolated interactions do not establish provider allowance or production token savings.

The cumulative patch contains **481 source/test paths**, comprising **341 outside the Python test tree and 140 Python test paths**, against the same pinned upstream base.


## Search and loading resilience (v0.6.4)

A fresh review reproduced whitespace-sensitive bot/Hub searches, redundant Hub filter reads, missing loading feedback and stale saved-chat search state on failed requests. New offline controls failed against the preceding behavior before repair. The first hook harness needed a partial module mock; that setup failure is not counted as a product failure.

Final scoped offline coverage: **6 UI test files, 30 tests passed**. Renderer type checking and source-health comparison passed with zero new blocking findings. Coverage includes query/profile isolation, late responses, explicit retry without timer retry, pasted searches, local filter reads, Trash routing, pending member catalogs and retained selections on read failure. Historical overlapping suites are not added to this count.

The exact renderer and native Electron main/preload/backend passed **six isolated real-app checks** with synthetic chats and collections. A test-only wrapper exposed the native Node HTTP client to inject bounded delay and HTTP 503 responses; an earlier Electron net.fetch hook did not intercept this transport and supplies no fault evidence. The accepted run observed actual transport interception, no stale prior search hit, manual recovery, zero new item-list reads across four local type-filter changes, zero renderer errors, zero external-app opens and zero inference POSTs. A separate regression measured three redundant type-filter reads before repair and zero afterward. These are request-count controls, not production latency or LLM-token savings measurements.

Nine exact source/test files were installed locally with permissions restored and configuration inputs preserved, and the native package was built from the installed source. The existing owner Desktop remained on its earlier package because enabled native controls could not unambiguously address its Wayland window for normal Quit; it was not signalled or force-killed. Source installation, staged package readiness and active-window adoption remain separate. This release does not certify that a production window has loaded the new renderer.

The cumulative patch contains **484 source/test paths**, comprising **344 outside the Python test tree and 140 Python test paths**, against the same pinned upstream base. Public inventory, Git history and release archives are checked independently before/after publication. No private UI evidence or operational paths are included in the public artifact.


## Portable prompt-cache preference (v0.6.5)

A companion review found a local configuration-only opt-in to an already existing native `prompt_caching.cache_ttl: auto` feature. The public addition is a minimal synthetic merge fragment and an English per-home/profile recipe. Full live configs, chat transcripts and private measurements were not copied. No new Hermes runtime patch is claimed by this release; the cumulative source/test patch remains 484 paths.

Offline native acceptance exercised three isolated home cases with eleven source controls each. The native per-key setter preserved unrelated settings; a root edit left an unselected profile at its existing default, and explicit opt-ins reached the native initialization helper. Existing destination clamps remained effective. Network/model access and arbitrary subprocesses were denied. Preliminary harness controls refused additional local Git metadata during import, and a fixture then mutated a returned read-only config mapping. Those harness failures are retained privately and are not counted as product failures; the accepted controls permit only local read-only metadata and compare config values without mutating them. No dependency was installed or model called.

The CLI parser/profile-selection path was already covered by the earlier setup acceptance; these new controls exercise the real setter and initializer directly, not a full packaged CLI launch. Existing live opt-in values were inspected read-only. Previously initialized production agents, provider TTL support, cross-bot cache reuse and token savings remain unmeasured. Existing Desktop renderer activation from v0.6.4 is still pending; no restart is implied by exporting a setting.


## Versioned shared-guidance prefix (v0.6.6)

Four new controls failed against the preceding builder: worker guidance, skill-dependent help and surface hints split the common prefix, and request diagnostics did not recognize v4. The fix uses v4 for newly permitted prompt builds while retaining v1/v2/v3 restoration. Applicable role, skill, execution and surface instructions remain in the full prompt; permissions, frozen tools, routes, quotas and TTL preferences remain unchanged.

The final canonical offline run covered **10 files / 142 passed / 0 failed**, zero file retries, including native fake-provider tool-loop prefix contracts, restore, model-switch and atomic compaction controls. Existing tests that asserted role/surface hints lived specifically in the old static tier now assert their continued presence in the full new-layout prompt; legacy byte/key controls remain separate. Scoped source-health review reported zero new findings. The installed-source smoke assembled two native v4 transport requests without sending them, retained own-role content and tool schemas, and matched six original v1/v2/v3 cache keys. All six synthetic old full-prompt/static hash controls also matched.

The synthetic shared leading text grew from 1,895 to 2,746 characters without changing either full prompt's length. This is not a provider cache-hit percentage or a production token/latency reduction. A bounded read-only historical-record inspection supplied no v4 adoption/savings proof and its private data was not exported. No new model/provider request was used to measure adoption.

Five exact source/test files were installed locally under native update custody before public export, with target-only rollback files and restored mode/ownership. Configuration/instruction hashes and running process identities were preserved. Fresh imports can build v4; already cached prompts remain as they were. Existing pending Desktop renderer adoption is independent and was not forced. The cumulative patch now has **485 source/test paths: 344 outside the Python test tree and 141 Python tests**, on the same pinned upstream base.


## Bounded native title recall (v0.6.7)

A native fixture reproduced full-transcript hydration before a small title-match response and before rejecting excluded history. The repair uses the existing message-bookend API, preserves the anchored view and continuation counts, and filters time/exclusion metadata before payload reads. Failure in a present bounded API reports unavailable history without retrying the full transcript.

The final native run passed **4 files / 76 tests / zero failures**, with zero file retries. Native live-import acceptance used five alternating before/after runs against one synthetic 256-message SQLite fixture: median 6.74→2.00 ms, 4.52→0.37 MiB peak Python traced allocations and 265→17 hydrated rows, with byte-equivalent returned responses. Both metadata-filter controls loaded zero message rows. The measurements are synthetic query/allocation results, not total-process RAM, billing, cache-hit or model-latency savings. A separate read-only existing-conversation check also preserved the result; no private title, transcript, ID, response hash or workload measurement was exported.

The exact runtime and regression file were installed locally under native update custody before export, preserving target permissions/ownership and target-only rollback evidence. Scope health reported zero new findings. Relocated maintenance artifacts retained their original-path aliases and source hashes; the native title-recall regression file passed its eight tests again after relocation. No provider request, quota change, paid fallback or embedding-service action was used.

The cumulative patch now has **486 source/test paths: 344 outside the Python test tree and 142 Python tests**, on the same pinned upstream base. Public checkout/apply acceptance, companion tests, complete Git history, archives and anonymous release readbacks are verified separately; overlapping runs are not added together. A fresh authenticated runtime status check found idle mounted chats, while the running Desktop package still differed from the prepared UI package. This release does not claim that the pending renderer was activated.

## Portable review of external memory and storage

The optional memory guide was checked against ai-memory v3.2.5's published configuration source. Its TOML example is parsed offline and names reviewed top-level, authentication and maintenance fields. This is not an end-to-end Hermes adapter or service deployment test. Native memory/search remain available without the optional service. The review does not enable providers, hooks, history backfill, MCP or protected embedding services, and no existing private configuration or memory store is copied into the release. A longer matched-work comparison is still required before claiming a recall/usage benefit or expanding a pilot.

The storage guide describes explicit inactive-artifact relocation and post-acceptance disposal boundaries. It publishes neither machine paths nor local migration inventories, firmware data, database snapshots, private logs or rollback contents.


## Context-free search metadata (v0.6.8)

The native SQLite authorizer reproduced prompt/tool hydration while search only
needed session identity. Fixing the search helper alone left title discovery
failing, exposing a second full-context reader in title-to-ID resolution. Both
call paths now use narrow native queries. Existing full-session/title APIs remain
unchanged; canonical Bot Chat priority, numbered continuation ordering, wildcard
escaping, freshness and legacy adapters are preserved. A failed present metadata
reader does not retry the heavyweight path.

The final native run passed **9 files / 395 tests / zero failures**, with zero
file retries. Six new controls exercise normal/read-only public discovery under
SQLite column denial, exact small/fresh/missing metadata, legacy compatibility,
failure without heavy retry and canonical/numbered titles. Scoped health reported
zero new findings. The newly exported title module's original bytes matched the
pinned upstream blob available locally; no history fetch was needed.

Five alternating installed-module runs against one synthetic read-only fixture
preserved the exact response. Median query time was 4.955→1.683 ms and peak Python
traced allocations 2,016,703→79,003 bytes. Two full-session reads plus one full
title read became zero, with context materialization 5,799,987→0 characters. These
measure local synthetic query/allocation work, not RSS, billed tokens, cache hits,
model input context or production latency. A separate real saved-conversation
read-only comparison retained the result; no private evidence or workload numbers
are published. No manual model request was made.

Four exact source/test files were installed under native update custody before
export, with target-only rollback and restored permissions/ownership. The
cumulative patch contains **488 source/test paths: 345 outside the Python test
tree and 143 Python tests**, against the same pinned upstream base. Companion
acceptance, base/apply/installed manifests, public history and release archives
are checked separately; overlapping test runs are not added together.


Local adoption was then checked at an idle boundary with no worker turn active.
Gateway used its existing native idle-only update control; Desktop exited through
its normal native Quit menu and reopened once with the already tested package.
Fresh source/process identity, authenticated read-only readiness and the same
saved-session/model binding were observed. Configuration/instruction hashes
remained intact, and no model or manual session-resume call was used. This is
source/readiness/continuity acceptance; it does not claim every production screen
was visually exercised or every bot has already used the optimized query path.


## Notification destination metadata (v0.6.9)

Native destination resolution still read full prompt/tool context merely to
check that the current/candidate session existed. A SQLite-authorizer regression
failed in both normal and named-profile read-only paths. The resolver now reuses
the native small metadata API; missing extensions keep legacy compatibility,
while failure in a present reader holds work without a heavy retry.

The final native run passed **10 files / 75 tests / zero failures**, zero file
retries. Four new controls join the existing compression delivery, stale-parent,
branch/delegate, foreign-profile, claimed-receipt/no-replay, owner-hold, stopped-turn,
retry and terminal-release contracts. These offline fixtures do not establish a
live intended-session ACK. Scoped source health reported zero new findings.

Installed-source paired acceptance used the existing production interpreter and
native dependency activation, with launch preparation frozen only in the private
measurement process to prevent PM rebuild/relaunch. Earlier guarded preparation
and unactivated-interpreter failures are retained privately and are not product
failures or accepted benchmark runs. The final five alternating synthetic pairs
included native read-only store open/read/close: median 3.951→1.713 ms, peak Python
allocations 1,900,776→21,140 bytes, full session reads 3→0, hydrated context
characters 3,735,552→0, with the same destination set. A separate real saved-chat
owning-store comparison also retained the set, with no notification, receipt,
model or inference action. No private evidence/workload values are published.
These measurements are not RSS, token, cache-hit or production latency savings.

The exact runtime and regression files were installed locally before export,
with target-only rollback and restored mode/ownership; configuration/instruction
hashes and active process identities were preserved. The cumulative patch now
contains **489 source/test paths: 345 outside the Python test tree and 144 Python
test paths**. Companion, base/apply/installed, complete history, archive and
anonymous readback checks are performed separately. Native source adoption and
visual/behavior acceptance remain distinct.


At the next verified idle boundary Desktop exited through one normal native tray
Quit event and reopened once with the same tested package. Fresh source/process
identity, native backend/main-renderer readiness, the original durable session and
model binding, and 99 protected configuration/instruction hashes were verified.
Gateway retained its existing process identity. A transient read-only observation
lost the backend listener during normal shutdown; its exact original app/backend
were then observed terminal before launching. No repeated Quit, signal, model or
manual resume call was used. This is source/readiness/continuity acceptance, not a
full production visual journey or a manufactured notification-delivery receipt.


## MRU selection and export preflight IDs (v0.6.10)

Native latest-session lookup and the two unfiltered export preflight paths read
full session context merely to obtain IDs. The regular `search_sessions` API now
also supports an explicit ID/recency-only projection; source/workspace predicates,
ordering and pagination remain shared. Actual resume, backup, import and full
session readers keep their original payloads. Filtered export already uses a
narrow candidate query and remains intact. Console also resolves its configured
per-session bound before enumeration, so a disabled guard issues no ID scan.

The final native run passed **10 files / 349 tests / zero failures**, zero file
retries. Eight new cases include actual SQLite prompt/tool/model-config read
denial, native ID ordering/page equivalence and MRU/oneshot/workspace fallback,
actual parsed CLI and Console budget refusals without touching existing output,
full successful backup equality and disabled-guard behavior. Existing batching,
compacted backup/import round-trip, retention/export selection and SessionDB
controls passed. Preliminary fixture signature/parser-wiring mistakes are retained
privately, not counted as product bugs. Scoped health reported zero new findings.

Five alternating installed-module pairs against a 32-session synthetic SQLite
fixture preserved the exact ID order and native count-guard result. Median local
query time was 51.292→0.979 ms; peak Python allocations 42,107,726→17,001 bytes;
session rows remained 32 while hydrated context characters fell 41,943,520→0.
The measured path is ID enumeration plus preflight, not the full backup payload,
RSS, model input, tokens or cache-hit rate. A separate existing-history read-only
comparison preserved the order/guard without writing an export/restore or calling
a model. Private workload data and identifiers are excluded.

Five exact source/test files were installed locally under native update custody
before export, preserving target mode/ownership, target-only rollback and
configuration/process guards. The two newly exported runtime modules' original
bytes matched the locally available pinned upstream blobs. The cumulative patch
contains **492 source/test paths: 347 outside the Python test tree and 145 Python
test paths**. Companion, pinned base/apply/installed, Git history, archive and
anonymous-public checks remain separate. No quota/provider/paid-fallback,
embedding-service, schema or model-context change was made.


Fresh CLI imports use the installed source directly. At an idle boundary Desktop
also exited through one normal native Quit event and reopened once with the same
tested UI package. Fresh process/source identity, authenticated native backend
and main-renderer readiness, the original saved session/model and 99 protected
configuration/instruction hashes were verified. Gateway retained its process
identity; no database snapshot, forced stop, model or manual resume call was used.
This source/readiness acceptance is separate from a full production visual journey.


## Chunked JSONL export and Terra reasoning (v0.6.11)

The native export suite passed **57 tests in 11 files**, with zero failures and
file retries. A subsequent hard-link regression exposed an inode-semantics
change; after repair, a focused four-file run passed **21 tests**, zero failures.
The runs overlap and must not be summed. Tests cover native CLI/Console export,
Unicode bytes, empty output, prompt-only/stdout behavior, staged serializer and
fsync failures, symlinks, hard links, read-only targets, missing parents, special
files and deleted-profile guards. Existing backup/import, retention and formats
remain covered. Scoped health reported zero new blocking findings or advisories.

Three full synthetic SQLite-to-JSONL exports per version produced identical bytes.
Median traced Python peak decreased from 107,491,242 to 24,736,700 bytes for this
fixture. A fresh installed-source run also matched the same synthetic output,
and a bounded read-only existing-history comparison matched full and prompt-only
serialization without persisting private history. These measurements include
payload load and serialization, but are not whole-process RSS, production usage,
model latency, cache-hit, or billing evidence.

An independent native transport regression caught Terra's `max` being clamped to
`xhigh`. Its compatibility change and controls passed **79 tests in seven files**,
zero failures. Fresh installed request construction preserves the configured
effort; this offline check is not an inference or quota-consumption benchmark.
The two source changes were installed locally under native custody with scoped
rollback. Runtime activation for already-running processes is separate from fresh
CLI import acceptance. The cumulative patch contains **496 paths: 349 outside
the Python test tree and 147 Python test paths**.

## Per-task reasoning effort (v0.6.12)

Five offline native test files passed **118 tests**, with one existing skip and
no failures. A later focused run passed **3 tests**; the runs overlap and must
not be summed. The focused tests use an isolated Kanban database and actual
tool registration and worker argument construction: they cover Sol and Terra,
normalization of `HIGH`, rejection before card creation for invalid effort, and
inheritance when omitted. They do not dispatch a production task or call a model.

The change was installed locally with a scoped rollback before publication. A
fresh process can load the installed code; a previously mounted agent may retain
cached tool definitions until its normal lifecycle refresh. Offline validation
does not prove a live Captain has selected a model or that a bot completed a task.

## Verified completion at budget checkpoints (v0.6.13)

An offline native regression suite passed 113 tests across five files; a later 21-test run of one of those files overlaps and is not an additional total. Tests cover iteration and wall-clock checkpoints and rejected or unverified ownership. One representative real worker completed a synthetic task at the iteration checkpoint with no subsequent tool or model call. This is not a measurement of every profile or a long-term usage reduction.

## Usage reporting during log rotation (v0.6.14)

A deterministic regression reproduced a file disappearing between enumeration and sorting. The native offline suite passed 31 tests across four related files after the fix. A read-only before-and-after check over the same real 24-hour window returned the same sample counts; no log rotated during that check, and the existing file budget left some files unsampled. This does not establish complete usage or a reduction in model calls.

## Older session restoration (v0.6.15)

The related offline suite passed 82 tests across three files, including owner changes, list readiness, lookup failure and stale navigation. A packaged Electron build was closed and relaunched against an isolated backend seeded with 55 synthetic sessions; the oldest session, omitted from the first page of 50, was restored. The mock provider received no prompts. This is not evidence that a particular existing session was restored or a live workload benefited. The source and package were installed locally before publication with a scoped rollback; actual UI behavior remains a separate check.

## Explicit usage attribution boards (v0.6.16)

Four related files passed 26 offline cases, including a synthetic external board, aliases, missing and non-regular paths, a symlink loop, and the 64-board limit. A separate Python 3.12 check covered symlink-loop resolution. The exact installed files passed the same suite in a read-only, network-isolated environment; these overlapping runs are not summed. In one identical existing seven-day sample, an explicitly selected isolated test board increased exact matched attempts from 7 to 91. One other board was unavailable in the sandbox, 52 log tails were cut, and compressed logs were not read. This is provenance coverage for a selected test board, not a model-usage saving or full production coverage. No model call was made for the measurement.

## Captain routing guidance (v0.6.17)

The Captain role template exposes the optional planner/executor split in its own loaded identity rather than relying solely on an external reference. This is static template guidance; offline template and package checks do not demonstrate live Captain compliance, real-bot orchestration or usage savings. Profile identities, model selection and dispatch remain operator-controlled.

## Per-task CLI reasoning (v0.6.18)

Five related test files passed 22 offline cases against the candidate and the same 22 cases against installed source in a network-isolated environment; these are overlapping runs. The new cases cover normalized effort, `none`, invalid input without card creation, omitted effort and propagation from CLI to task and worker arguments. No live dispatch, model call or quota measurement was performed.
