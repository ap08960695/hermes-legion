# v0.7.38: owner-safe history windows and composer drafts

Opening another profile's same-ID history could leave the first runtime bound
while changing its displayed owner. Separate windows also shared draft keys.
Explicit history owners are now checked before route or read-marker changes.
Conflicting owners open through the existing native window bridge; repeated
same-owner links focus the existing window. Original histories remain bound.

Draft text and retry identity use connection, profile, target profile and
session ownership. Debounce, teardown, reload, undo, prepared-image recovery,
SDK fallback and deferred send results retain the editor's captured owner.
Lineage/profile moves retain the source if destination storage fails. Storage
events and updates touch one key; retention scans occur when adding a saved
scope and never prune another owner's drafts. Unassigned legacy drafts stay
separate and require explicit recovery into an empty editor. No automatic
submission or model request is added. Attachments remain memory-only.

The final related UI selection passed **30 files /496 tests**, zero failures
and zero retries, with frozen source hashes checked before and after. The
native window-registry selection separately passed **one file /24 tests**.
Native TypeScript/build checks passed; scoped health has no findings. Lint
has zero errors and seven previously existing warnings. These selections
are separate evidence and are not a summed universal test count.

Both Linux and macOS received the exact 55-path combined history/draft
cohort before publication (47 paths in the latest draft change). Rebuilt,
installed native applications passed ten isolated interaction checkpoints on
each platform, including same-ID owner windows, draft isolation, reload,
reopen and duplicate-window prevention. Both Mac launch locations have the
same locally signed package; this is ad-hoc signing, not notarization. The
existing memory admission threshold was met without lowering it. The screen
was not unlocked and the original Mac Gateway was not started.

All fixtures use private synthetic homes with zero provider inference. No
original human session, real worker adoption, causal production usage, cache,
RAM or latency saving is inferred. No dependency, tool, RPC, quota, model,
provider or paid-fallback change is included. Raw histories, screenshots,
host details and credentials remain private.

---

# v0.7.37: session links keep their profile and source

A named-profile history link could resolve the correct title but open a
same-ID conversation from the default profile. Two navigation seams dropped
the owner: the reference click discarded its profile, then the shared tab
opener forwarded explicit routes only for Bot workspaces. Links now capture
the existing source resolver before asynchronous loading and pass their
profile through the existing tab-opening path. A legacy source keeps its
profile-only routing; no connection is invented. Unqualified links retain
their existing behavior. Tab metadata now matches the explicit owner before
reusing a cached row, so same-ID titles from another profile or connection
cannot suppress the existing bounded metadata lookup. No new RPC, tool, dependency, quota or fallback.

The installed native Linux application reproduces the wrong-profile result
before the repair using two separately owned, same-ID CLI histories in an
isolated home. Four real-store owner-routing regressions fail before the fix;
one ordinary-link control already passes. A further same-ID title case also
fails before the metadata repair; its five existing slice controls pass. The final related selection passes
twelve files / one hundred twenty-five tests without retries. Lint and native typechecking
pass. The replacement Linux image must pass the same native title-and-click
acceptance before installation and again after installation, with no model
inference and no original session/profile data used. These are private native
acceptance histories, not proof of original-user-window adoption.

Seven exact source paths are installed on Linux and macOS before publication,
with target-only rollback and original file metadata preserved. The Linux
renderer is rebuilt from native prepared inputs without external networking.
The macOS renderer remains pending under the already recorded resource hold;
this release does not repeat the refused build, lower its headroom gate,
unlock the screen or start the original Mac Gateway. Source parity and
renderer adoption remain separate claims. No production token, cache-hit,
RAM or latency reduction is inferred from this correctness fix. Raw histories,
host details, credentials, screenshots and personal data are not published.

---

# v0.7.36: usable session links inside quoted answers

An actual native recall reply returned a session reference as a JSON string.
The installed Desktop swallowed the closing quote into the session identifier,
so the link could not resolve its title or open the intended conversation.
The bare-reference matcher now stops at quote delimiters. Explicitly quoted
values with spaces, inline/fenced code, punctuation, profile boundaries and
normal session links retain their existing behavior. No new tool, prompt,
dependency, account, quota, model call or fallback is added by this fix.

Four quote regressions fail before the repair; nineteen controls already pass.
The related native UI selection passes six files / fifty-nine tests with no
retry, and the native Linux typecheck and offline prepared build pass. The
actual prior reply and new packaged UI are checked in an isolated home with
external network denied. A copied local-session receipt remains bound to its
original owner: it is not authorization to resume that session under a new
profile. The click-through control uses a new same-owner native CLI transcript
replaying the prior verification answer and a separate derived reply that links
to that control. Importing foreign local authority is not claimed as accepted. No owner
gate is weakened, and this is not original-user-window adoption.

Exact two-file source installation on Linux and macOS precedes publication,
with scoped rollback and original permissions preserved. The installed Linux image passes nine rendered checkpoints: actual JSON
reference resolution, same-owner click-through, native profile rename, overlay
dismissal, compact delete/cancel, target-only deletion and reload persistence.
The image was validated before installation; no model request was made by the UI
acceptance. Expected font/plugin-list fetches fail because external network is
deliberately denied; no application exception is observed. The existing macOS image is intentionally kept:
its build was refused before starting because available RAM was below the
existing six-GiB build headroom gate. No process was stopped to force a build,
and the locked Mac screen was not unlocked. macOS renderer adoption remains
pending; source parity is a separate verified claim.

A separate native provider-backed recall check used one fresh user prompt and
four physical requests, under a hard five-request cap. It recovered five exact
facts and the source reference from thirty-four messages of a genuinely
completed private test workflow, using two complementary history searches in
13.46 seconds. Observed main-call input was 20,747 tokens, including 11,648
reported cached tokens. These are one-case observations, not a causal production
before/after reduction, cross-bot cache-sharing proof or months-long retention.
The raw transcript, session identifiers, profile data, screenshots and private
host details are excluded from this repository.

---

# v0.7.35: faster ASCII history verification with unchanged matching

A large ASCII argument miss still called the Python character classifier once per
character even after the earlier positive-match optimization. Two native SQLite
resource regressions reproduce this unnecessary work through decoded and raw field
checks. The verifier now consumes bounded ASCII word/gap runs with a compiled
standard-library regex, preserving the exact existing ASCII letters/digits rule.
Non-ASCII chunks retain the native Unicode61 codepoint classifier and CJK boundary
handling. No extra index, database connection, dependency or model call is added.

Prefix matching, phrases across long punctuation/chunk boundaries, words split
between chunks, Unicode folding, complete character/UTF-8 byte metadata, binary
flags, suffix validation and loud deadlines remain checked. Token buffers retain
their original query-sized bounds; huge word runs are sliced only to that bound.
No full field hydration or matching-policy change is introduced.

The final related selection passes 241 files / 2316 tests,
zero failures, 16 existing skips and zero file retries with four
workers. Scoped source health and test Ruff pass; the existing runtime FURB167
alias warning is unchanged. Overlapping selections are not summed. Native production
Python on Linux and macOS each passes fifteen installed controls, including real
registry discovery, decoded/raw negative work bounds, exact cross-chunk offsets,
prefix/late/malformed/deadline behavior and full Unicode/binary metadata.
Both hosts install the exact two paths with scoped rollback and metadata restored
before publication. Full-kit apply/reverse/reapply and installed parity are verified
on both hosts. Linux activation is native and idle-only; original Mac Gateway stays
off. No renderer, quota, model, account, tool schema or prompt-prefix change is made.

Four sequential uninstrumented ABBA component samples preserve boolean results:

| Synthetic case | Before, ms | After, ms |
|---|---|---|
| 500k-character ASCII word miss | 112.24 / 111.05 | 41.56 / 41.44 |
| 500k-character single ASCII word miss | 64.50 / 65.23 | 2.07 / 2.14 |
| 200k-character Unicode control miss | 78.70 / 68.56 | 74.53 / 70.12 |
| Early positive with 500k-character suffix | 2.09 / 1.97 | 2.01 / 1.99 |

These are small-sample component observations, not original-workload latency, RAM,
model-token or provider-cache evidence. The Unicode/positive controls establish no
general performance ranking. The earlier original Captain baseline timeout remains
a separate preserved condition; it has not been replayed, and candidate success
on that original query is not claimed. The broader Hermes objective stays active.

---

# v0.7.34: avoid redundant work after verified argument matches

Boolean tool-argument checks previously kept tokenizing or case-folding unrelated
suffixes after all requested terms were already found. A synthetic valid SQLite
tool-call fixture reproduces two excessive-work failures, one for Unicode61 tokens
and one for Thai substring matching. Candidate review also caught a raw-field path
that continued through the rest of its read chunk; matching now stops at the first
conclusive token boundary in that chunk as well.

The remaining decoded stream is still consumed and validated. Full character and
UTF-8 byte lengths and binary/surrogate flags remain correct for excerpts and
paging. An early positive match cannot hide invalid UTF-8 or malformed JSON later.
Missing terms, late matches, prefixes, phrases, multiple query terms, native CJK
semantics, caller transactions and deadline failures retain their contracts.
The same matching logic covers decoded argument fields and legacy native fields;
no full JSON hydration, higher deadline or extra model call is introduced.

Final related tests: 240 files / 2308 passed, zero failures,
16 existing skips, zero file retries and four workers. Scoped code
health and test Ruff pass. The runtime module retains its pre-existing FURB167
alias warning; no new lint finding is introduced. Overlapping suites are not summed.
Linux and macOS production Python each pass twelve installed native controls,
including actual registry discovery, negative/prefix/late results, invalid suffixes,
full Unicode metadata and expired deadlines. Both hosts install the exact two
paths with scoped rollback and restored permissions before publication. The full
consolidated patch is checked for apply/reverse/reapply and installed parity on
both hosts. Original models, quotas, resource gates and prompt/tool schemas stay.
Linux activation remains native and idle-only; original Mac Gateway stays off.

In one synthetic 500,000-character unrelated suffix fixture, instrumented ABBA
samples classify 500,056 characters before versus thirty after, returning the same
boolean result. Observations were 98.19/99.33 ms before and 2.36/2.17 ms after,
including instrumentation. This is a component result, not an original-workload
latency, RAM, model-token or provider-cache claim. The earlier original Captain
baseline timeout remains a separate preserved result; it has not been replayed
and candidate success on that original query is not claimed. The broader Hermes
improvement objective remains active.

---

# v0.7.33: reliable and bounded session discovery

Discovery previously capped raw matching messages at 300 before excluding current
context, inspected lineages or duplicate sessions. One busy session could hide
older conversations, an in-place compacted message, or an interactive conversation
behind scheduled-task chatter. Six native SQLite scenarios reproduce the failure
on the parent, through the actual tool registry. A separate review caught and
fixed two candidate-only regressions: a refill must not broaden an AND query when
an exact hit already exists, including an exact scheduled-task hit.

The repair applies lineage and live-context eligibility in every native search
route before row pagination. It refills by excluding selected lineage roots, asks
for at most the remaining output slots per query, and prioritizes interactive
sessions before scheduled ones at each matching tier. Exact, substring and relaxed
matching tiers are exhausted globally in that order, preserving fallback precision.
The requested output cap remains ten. Recursive lineage membership terminates on
cycles. Hidden/rewound rows, active delegation context, profile ownership, temporal
bounds and bounded excerpt hydration retain their guards. Older adapters retain
their bounded compatibility path. No tool schema or prompt-prefix change is made.

The final related selection passes 239 files / 2297 tests,
zero failures and 16 existing skips, with zero file retries and four
workers. Scoped code health and Ruff pass. Overlapping runs are not summed.
Linux and macOS production Python each pass eighteen installed native controls:
six saturation conditions in Latin, Thai and CJK, using readonly fixture databases.
No model/provider requests are made. The full consolidated patch is checked for
apply, reverse and reapply on both hosts, with scoped rollback and exact modes.
Linux activation is native and idle-only; the original Mac Gateway remains off.
No renderer rebuild, dependency, model, quota or resource-gate change is needed.

An additional synthetic 301-message fixture returns the same top-one message
before and after. Four ABBA samples reduce candidate rows crossing into Python
from 300 to one per query. Traced peak allocations were 458,145 and 334,362 bytes
before, versus 45,938 and 45,642 after; elapsed observations were 14.36/10.29 ms
before and 3.30/2.95 ms after. These component observations were taken alongside
offline tests, not a controlled original-workload latency or whole-process RAM
benchmark. They establish no model-token savings, provider cache hits or original
session adoption. The broader improvement objective remains active.

---

# v0.7.32: leaner plugin cleanup and accurate review-block metadata

Every registration previously allocated a fresh cleanup closure that captured its
manager. The same cleanup operation is now cached once per manager with the native
cached_property mechanism. Managers keep distinct callbacks and all registrations
retain their own release operation. Cleanup still late-binds the owner's method,
always runs after a release failure, and remains idempotent.

The new callback-memory test failed before the repair; two lifecycle controls
passed. The broader run also exposed an older workflow mismatch: the existing
backend accepts review-to-block moves but its workflow metadata denied them. The
metadata now agrees with that existing verb without changing kernel gates or
mutating any live card. Three multiplex-status fixtures now use an isolated
launcher directory, keeping the original-home I/O protection active. Those four
failures were reproduced on the parent code; no assertion or guard was relaxed. The final related selection passes 344 files / 3528
tests, zero failures, 8 existing skips and zero file retries.
Scoped source health and Ruff pass. Overlapping selections are not added together.

Linux and macOS production Python each pass seven installed native controls:
callback allocation bound, cross-owner ledger isolation, repeated disposal,
complete cleanup, persistent late dispatch, failed-release cleanup, and native
review-to-block behavior matching the published workflow. No model
or provider request is made. Exact scoped rollback and permissions are preserved;
Linux activation is native and idle-only, while original Mac Gateway stays off.
The full consolidated patch is applied/reversed/reapplied and installed parity is
checked on both hosts. No renderer rebuild or dependency/config change is needed.

The sixteen-manager / 8,192-handle component fixture retains 2,158,464 fewer Python
bytes. Four sequential native 116-profile fresh startup measurements (ABBA) show
mean PSS 336,038,912 before versus 333,786,624 after, zero swap. That controlled
series is not an original-user workload benchmark or a general latency/RAM claim.
No model-usage, provider-cache or inference-speed improvement is inferred.
Original models, quotas, effort ceilings, fallback and resource gates remain.
The broader improvement objective stays active.

---

# v0.7.31: make auxiliary and compaction test fixtures faithful

Twenty inherited failures were caused by dynamically fabricated MagicMock
attributes, rather than demonstrated production failures. Ordinary auxiliary
clients now explicitly declare that they do not own the main-context compression
recovery boundary. Three single-model conversation fixtures explicitly declare
that they have no MoA aggregator slot. All assertions and behavioral expectations
are unchanged. Only six test files change; runtime, credentials, retry/fallback
policy, models, quotas and resource gates are unchanged.

The same six-file baseline had 286 passes and 20 failures; corrected fixtures
pass all 306 cases. The final related selection passes 125 files / 1,290 tests,
zero failures, zero skips and zero file retries. Selections overlap and must not
be added together. Structural comparison verifies that the only AST changes are
the explicit mock-constructor fields. Scoped code health and Ruff pass.

Both installed hosts have the exact six test files and pass two additional
production-Python checks against actual synchronous and asynchronous SDK client
constructors. The real clients have neither fabricated ownership nor aggregator
attributes. No HTTP request or model inference is attempted. These are SDK-contract
checks, not a new full-loop model benchmark. The complete consolidated patch is
applied, reversed and reapplied on both hosts, with full installed-source parity.

No Gateway or Desktop restart is required for this test-only maintenance. Original
process identities, settings and protected files are preserved. No RAM, cache-hit,
token-cost or latency reduction is claimed by this release. The earlier twenty
failures remain recorded in historical reports below; this release resolves that
specific inherited set. The broader improvement objective remains active.

---

# v0.7.30: batch the fresh deferred index/trigger phase

Fresh store initialization previously committed each deferred index and trigger
separately. A failure could leave an earlier trigger committed even though the
phase failed. Initialization now identifies a genuinely empty declared schema and
runs its later deferred phase in one BEGIN IMMEDIATE transaction with rollback on
BaseException. The declared-table phase remains a separate earlier transaction.
Existing stores keep ordinary behavior, so settled checks do not gain a mandatory
write lock. Later FTS/migrations, schema version, ownership and durability stay native.

Two new native tests failed before the change: fresh triggers were created outside
a transaction, and an injected second-trigger denial left the first committed.
The existing-store/data control passed. The final related selection passes
274 files / 2353 tests, zero failures and zero file retries,
with 16 existing skips. Scoped source health and Ruff pass.

Linux and macOS production Python each pass six installed-source controls: fresh
transaction/integrity, native history and FTS, settled/read-only reopen, injected
deferred rollback and ordinary recovery, existing owner data and transaction
behavior, and a settled opener behind another writer. Private synthetic databases
and denied networking are used; no original-user store or model is called.
Linux activation is idle-only and original Mac Gateway remains off. The complete
consolidated patch is applied/reversed/reapplied and installed parity is checked
on both hosts. Companion tests are a separate selection; no renderer rebuild.

Diagnostic ABBA trials on sixteen fresh native stores reduced the open phase by
about 36.6 percent. One untraced matched native Gateway startup pair with 116 fresh synthetic profiles took 24.44 seconds before and 19.43 seconds after (about 20.5 percent lower). This is a single controlled pair, not a production or already-settled-store latency result. PSS did not improve; no RAM saving is claimed.
No original-workload latency, RAM, usage or provider-cache gain is inferred from
that component result. Original quota, model, effort, fallback and resource gates
are preserved. Earlier twenty inherited broad auxiliary failures remain documented;
historical overlapping test selections below are not summed. Full goal stays active.

---

# v0.7.29: bound long-lived profile lock buffers

Native synthetic startup allocation attribution found that profile reservation
held a filesystem-sized text I/O buffer for every lock descriptor. The repair
bounds that existing buffer to 4096 bytes. It does not remove locks, change lock
records, reduce the served fleet, interrupt active work, or alter any model,
quota, effort, fallback, ownership, review or resource gate.

The regression failed before the repair at 2,152,541 retained bytes for sixteen
real reservations. The related native test selection passes 7 files / 46 tests,
zero failures and zero retries, with six existing other-OS skips. It covers native
exclusion, partial-reservation rollback, stale and foreign locks, inode lifetime,
bootstrap, shutdown and endpoint identity. Scoped source health and Ruff pass.

Linux and macOS production interpreters each pass six installed-source checks:
bounded retained allocation, externally visible durable records/private mode,
exclusion, rollback, same-inode reacquisition/late cleanup, and a record larger
than the buffer. These operate on synthetic private homes with networking denied.
No model call or original user database is used. Original Mac Gateway stays off.
The complete consolidated patch is applied, reversed and reapplied on both hosts;
installed parity is a separate check. No renderer rebuild is required.

The allocation reduction is directly measured. Whole-Gateway PSS did not show a
stable equally sized improvement in the initial raw startup pairs. Allocator and
measurement effects must remain visible; this release makes no quantified original
workload RAM, startup latency, usage, or provider-cache saving claim. Full Hermes
acceptance and representative workload measurement remain ongoing. Earlier twenty
inherited broad auxiliary failures remain documented. Historical overlapping test
selections below are not added together.

---

# v0.7.28: discover the role-plan contract before creating work

A retained failed automatic-dispatch case showed Captain prescribing an internal
step ID that contradicted the validator. THINK then asked the user to resolve
that technical conflict. The repair makes the existing native routing CLI expose
the plan contract once, only when its bounded admitted roster includes THINK.
Its example and pattern come from the native role-plan module. The same module
supplies ID-choice ownership and external-name guidance in the THINK worker brief.
No global tool schema, account, quota, provider, model, approval or validator
change is introduced. No existing conversation prefix or worker is reloaded.

Before the change, two new behavior checks failed. The final related native
selection passes 9 files / 68 tests, with zero failures and zero file retries.
A third control keeps legacy-only discovery free of the planning contract.
The CLI test consumes the advertised ID through a real SQLite THINK completion
and checks that profile configuration remains byte-identical. Existing empty,
unadmitted, corrupt-peer, bounded-roster and secret-output controls still pass.
The worker test keeps exact externally required file/API names intact.
Scoped source health and Ruff pass.

Linux and macOS production Python each pass eight installed-source checks with
zero network/model requests, including native CLI contract discovery and a
legacy-only omission, a durable native plan using its advertised ID, strict
invalid-ID refusal, completed-review readback and foreign-assignee rejection.
The complete 759-path patch is checked by apply/reverse/reapply on both hosts,
with installed parity checked separately. Linux activation is idle-only; the
original Mac Gateway stays off. No renderer rebuild is needed.

A fresh provider-backed private GPT role loop now completed end to end using the
same frozen source and its actual embedded dispatcher: three original cards,
four native runs, a validated THINK plan, independent Analyst reference, paired
ACTION, independent review on the same card, Captain verification and native
goal done. Only the initial user prompt was submitted; there were no manual
staged dispatch calls, retries, additional human prompts or paid fallback.

The case used 39 physical requests under an unchanged hard limit of 42 physical requests.
The private fixture allowed six goal turns and actually completed in five.
This does not change any original account quota or live profile limit. A preceding
fresh case used 40 requests, reached the same artifact/review work, then correctly
paused at its five-turn fixture cap when the judge requested more explicit
verification confirmation. It was retained and never replayed. Different inputs
and responses prevent attributing the later success or request count solely to
the fixture cap or this patch.

Actual THINK/Analyst model calls overlapped for about 5.06 seconds. Captain called
the native routing CLI once and received its planning contract. Captain and the
independent reviewer each have an actual successful verify.py tool receipt;
all seven artifact cases passed. Four original-card result admissions reached
terminal completed state. Every worker's last tool was its successful native
handoff, with zero observed subsequent model starts for that native session.
After goal done, a fifteen-second observation saw zero additional requests.
The private owner then exited through its genuine idle-only native stop path.

Among 34 returned main calls with known input usage, the provider reported 552,925
input tokens and 471,552 cached input tokens (about 85.3 percent). This is observed
synthetic-workload input caching, not a billed-cost saving, a production before/
after improvement, complete auxiliary-token accounting, or cross-bot cache
causality. All protected original files and supplied inputs remained unchanged;
no auth files were copied and no raw credential matches were found in the case.

This acceptance covers one isolated GPT coordinator/planner/analyst/action/reviewer
graph on frozen installed-equivalent code. It does not prove original Captain
adoption, all provider families, all workloads or completion of the broader
maintenance objective.

Provider-backed acceptance above is separate from the offline/native checks.
These offline/native checks alone do not prove model autonomy, original-session
adoption, all provider pairs, production usage savings or cross-bot cache causality.
Earlier twenty inherited broad auxiliary failures remain documented. Historical
selections below overlap and must not be summed.

---

# v0.7.27: keep completed independent review evidence readable

A later fresh automatic-dispatch case reached all original role handoffs:
THINK complete, independent Analyst complete, ACTION requesting review, and the
independent reviewer completing the same card. All seven artifact checks passed.
It used 37 physical requests, and real THINK/Analyst calls overlapped for about
2.91 seconds. Four local automation admissions actually reached terminal
completed state. Captain then could not inspect the completed original card:
validation still treated the reviewer as an unrelated ACTION assignee. The
native goal correctly paused. This failed case is retained without replay;
it does not establish successful whole-goal completion.

The validator now recognizes a completed independent review only when the latest
native run is completed, has an end timestamp, matches the current assignee and
has the native claimed-event provenance of a review run. It keeps the original
actor, parent/run/hash, step, dependencies and write scope intact. Foreign
terminal assignees remain refused. No alternate role registry, status rewrite,
model request, automatic retry or authority bypass is introduced.

The new real-world regression failed before the fix while two foreign-assignee
controls passed. The final combined related selection has 8 files / 58 passes,
zero failures and zero file retries. Linux and macOS production Python each
pass six installed-source checks with zero network/model requests, including
completed-review readback and foreign completed-assignee refusal. The same
release includes the strict step-ID brief/error clarification described below.
Full provider-backed reacceptance remains separate; original-session adoption,
all provider pairs, production usage savings and shared-cache causality are
not established. Historical overlapping suites must not be summed.

A subsequent fresh bounded case stopped before ACTION because Captain's brief
introduced an underscore-containing internal step ID as an explicit requirement.
THINK detected its conflict with the strict grammar and asked for clarification.
The private case drained after 21 physical requests and was not replayed. This
separate coordination/policy issue remains open: routine internal identifiers
should not require owner intervention, while externally meaningful identifiers
and material authority gates must remain protected. No approval rule or identifier
validator was weakened to make the case pass.

---

# v0.7.27: advertise strict THINK step IDs before handoff

A fresh bounded automatic-dispatch case completed the independent Analyst work,
but the THINK bot submitted an underscore-containing step ID. The unchanged
validator correctly refused it. Its former error said only “unique lowercase id,”
and the worker brief omitted the accepted grammar, so the bot unnecessarily
asked the user about a technical formatting rule. That failed case used 22
physical requests after its private workers drained; it is retained, never
replayed, and is not reported as a successful full loop.

The brief and error now state `[a-z][a-z0-9-]{0,63}` and explicitly exclude
underscores. The existing validator, exact plan hash, run binding, write scopes,
independent review, quotas, effort ceilings and approval policy are unchanged.
No tool, parser relaxation, retry or model call is added by the repair.

Two new tests failed on the unchanged parent. The final related selection has
8 files / 58 passes / zero failures and file retries. Scoped source health and
Ruff pass. Linux and macOS production Python each pass six installed-source
checks using native SQLite/configuration/handoff APIs, with no network or model
requests: brief grammar, atomic invalid-ID refusal, durable valid plan, and
legacy completion. These checks do not establish provider-backed autonomy.

A separate earlier case used 18 requests and stopped at an inline Python command
approval refusal. The policy remains deny. Existing jq passed the real native
Terminal path for read-only JSON aggregation while inline Python remained
blocked. Capability selection must preserve approval boundaries; it is not
permission to disable them or replay a failed task.

The complete 759-path public patch is verified by apply/reverse/reapply on both
hosts, and installed source parity is checked separately. Linux activation is
idle-only. The original macOS Gateway stays off. Fresh provider-backed full-loop
acceptance remains separate work. Original-session adoption, all provider pairs,
production usage savings and cross-bot cache causality are not established.
Earlier broad auxiliary testing retains twenty documented inherited failures;
this scoped passing selection is not a globally green upstream suite.
Historical selections below overlap and must not be summed.

---

# v0.7.26: lazy local adapter owner binding

Consolidated kit:759 source paths. Related native wake/local/notifier selection:
32 files /114 latest per-file passes, zero failures/retries; final changed fixture
four passes. Scoped health clear. Linux and macOS production Python each verify
four real authority/FIFO scenarios with model scheduling held and no model calls.
Full public apply/reverse/reapply and installed parity are checked on both hosts.

A real fourteen-request discovery case found the bug and achieved actual model
overlap, but failed its full loop. It is retained and never replayed. Provider
reacceptance of the corrected loop and original-session adoption remain unproven.
See [the owner-binding repair and evidence limits](local-result-wake.md).
Historical selections below overlap and must not be summed.

---

# v0.7.25: completed card-result goal waits

The consolidated kit has 756 source paths. Related goal, viewer and loop
selection: 30 files / 302 passes, zero failures and file retries. Scoped source
health has no new findings. Linux and macOS native installed acceptance each
verify nine scenarios with real isolated SQLite and controlled judge decisions;
no real model or external provider calls. Full public apply/reverse/reapply and
installed parity are checked on both hosts. Original-session adoption and a
continuous autonomous bot graph remain unproven.

See [the advisory wait repair and limits](goal-result-waits.md). Earlier evidence
below is historical, overlaps this selection and must not be summed.

---

# v0.7.24: Gateway goal notification identity

The consolidated kit pins 752 source paths. Goal/board/notification/multiplex:
35 files / 373 passes, zero failures and file retries; scoped code-health has no
new findings. Linux and macOS installed native acceptance each pass 12 checks,
including two real Gateway-hook/synthetic-route cases with controlled judges.
No real model or external provider calls for this release. Both hosts pass full
public-patch apply/reverse/reapply. Installed parity per host:751 exact plus one
pre-existing comment-only AST-equivalent tool difference, zero missing files.

See [the identity repair and evidence limits](goal-notification-identity.md).
Historical selections below overlap and are not summed. Their broader inherited
failures, original-session and continuous-graph limitations remain visible.

---

# v0.7.23: bounded retries and cross-board goal waiting

The consolidated kit now pins 750 source paths. The new goal/board/notification
selection passes 290 cases across 15 files, zero failures and file retries.
Code-health reports zero new findings for the three scoped source/test paths.
Native installed acceptance on Linux and macOS each passes ten SQLite/goal
checks; both hosts also pass the five real-SDK controlled-loopback retry checks.
No real model or external provider is called for this release.

The async repair has a separate three-file/24-pass focused selection. Its broader
125-file selection has 1,270 passes and 20 inherited failures, all reproduced on
the unchanged parent in the same six failed files; zero new failures. The exact
inherited names are in the test selection. Overlapping selections are not summed,
and this is not a globally green upstream suite.

Both native hosts apply, reverse and reapply the 750-path public patch using the
unchanged checkout verifier. Each original installed tree has 749 exact files and
one pre-existing comment-only, Python-AST-equivalent Kanban tool difference; zero
missing files. No source-wide restore or replacement was performed. Linux Gateway
loaded the scoped source during confirmed idle; the original macOS Gateway stayed
stopped. Existing stop state, profiles, models, quotas, credentials and work were
preserved. This does not prove an original session adopted the new behavior.

See [goal waiting](goal-kanban-awareness.md) and [auxiliary retry policy](async-auxiliary-retries.md).
These cases establish retry admission and native advisory-count/wait mechanics,
not workload billing/cache/RAM savings or a continuous autonomous bot graph.
The previously bounded real-provider graph below remains separate historical
proof; it was not replayed or charged again for this release.

---

# v0.7.22: bounded real native parallel evidence

Evidence-only update; the exact 748-path source patch payload is unchanged from
v0.7.21. A new synthetic Linux case completed six native cards / seven runs with
36 physical high-effort requests, zero retries/fallback and nine artifact checks.
Native run overlap was 18 seconds and main model request overlap 13.839283 seconds.
No tools or model requests followed terminal handoffs; final quiet observation was
15 seconds. Original model/configuration/quotas/holds remained unchanged.
See [the case, method and limits](parallel-native-acceptance.md). This is not
continuous production scheduling, all-family adoption, cross-bot cache causality
or measured workload savings. Source regression/native Linux/macOS acceptance
below remains historical evidence on the same bytes, not repeated test totals.

# v0.7.21: compact saved profile routing

748 pinned paths. Broader profile/workflow selection: 84 files / 738 pass / six
existing platform skips / zero failures and retries. Seven installed native CLI
checks each on Linux/macOS pass with network denied. See [routing snapshot](profile-routing-snapshot.md).
Final integrated selection: 88 files / 835 pass / eleven existing skips / zero failures and retries. Actual-owner tool-shell CLI checks pass on both hosts. The real coordinator correctly blocked on the pre-repair stale CLI after seven requests; no parallel completion or usage reduction is proven. No global-green
or original-user adoption claim.

# v0.7.20: managed-worker source pinning

742 pinned paths. Full managed-worker selection: 40 files / 124 pass / 0 fail,
zero retries. Installed native source/secret isolation checks pass on Linux and
macOS with zero model/network requests. See [source pinning](managed-worker-source-pinning.md).
The new real coordinator reached the provider and created THINK, then gave_up at the private iteration cap after eight requests. Parallel-bot completion is NOT_PROVEN; no global-green, original-user adoption or workload savings claim.

# v0.7.19: known native auxiliary reasoning floor

740 pinned paths. Four focused files / 24 pass; broad 74-file selection / 848 pass
and 15 inherited failures, zero retries and no new failures. Five native installed
smart-approval serialization controls each on Linux/macOS pass offline.
See [native floor and actual Captain acceptance](native-auxiliary-reasoning-floor.md)
for the result and its limits. No global-green or production savings claim.

# v0.7.18: auxiliary Codex effort fidelity

738 pinned paths. The final Responses request retains top-level chat effort,
including owner ceilings, lower efforts and explicit disablement. Focused 62
cases pass; the broad 73-file selection has 840 passes and 15 inherited failures,
reproduced unchanged on the prior source. Five native offline serialization
controls each on Linux/macOS pass without model calls. No new code-health
findings. No production usage savings or successful real Captain goal completion
is claimed. See [acceptance and known limitations](auxiliary-codex-effort.md).

# v0.7.17: preserve concurrent MCP schema entries

736 pinned paths. A profile-local native lock covers manifest read-modify-write;
no lock is held during server discovery or tool execution. Final scoped native
regression: 98 files / 911 passed / 0 failed / 1 existing skip, zero retries.
Five installed production-Python controls each on Linux/macOS retain both peer
entries and cold-register both required tool schemas with zero server starts,
network requests or model calls. Code-health reports no new findings.
See [concurrent MCP schema publication](mcp-schema-publication.md).
This is synthetic native acceptance, not original-workload usage or latency proof.
Historical/focused counts overlap and are not summed.

# v0.7.16: retire old profile config caches

735 pinned paths. Completed delete/rename and permitted Gateway retirement
release old config cache values and warning records. Parked live homes,
unfinished authorities and sibling profiles retain their recovery state.
Latest-per-file regression: 256 files / 1,855 passed / 0 failed / 7 existing skips,
zero retries. Five installed production-Python controls each on Linux/macOS;
eight packaged-renderer checkpoints with a separately instrumented private backend.
No inference or measured original-workload RSS/PSS savings claimed.
See [profile config cache retirement](profile-config-cache-retirement.md).
Historical counts and focused runs overlap and are not summed.

# v0.7.15: preserve the validated config generation

731 pinned paths. Both native readers now back up their parsed bytes and
descriptor metadata instead of reopening the source path after validation.
Native regression: 174 files / 1,234 passed / 0 failed /
4 existing platform skips, zero retries. Installed Linux/macOS:
eleven production-interpreter controls each, network denied. Code-health clear.
See [validated config snapshots](config-backup-snapshot.md). No original-user
conversation adoption or measured savings claimed. Historical counts overlap.

# v0.7.14: complete, ordered config backup publication

729 pinned paths. Rapid same-second saves no longer collide; readers do not
see partial copies; failed copies preserve the previous good backup; rotation
uses a fresh completed-file listing. Default retention five and unchanged-content
deduplication remain. Native regression: 173 files / 1,230
passed / 0 failed / 4 skips, zero retries. Installed Linux/macOS:
seven production-interpreter controls each, zero providers. Code-health clear.
See [config backup publication](config-backup-publication.md). No measured disk,
RAM, usage or cache saving claimed. Historical counts overlap.

# v0.7.13: preserve last-good config through metadata failures

727 pinned paths. Signature I/O failures now reuse native last-good raw config/
backup recovery; strict readers, missing-file semantics, worker snapshots and the
normal cache path remain unchanged. Native regression: 163 files /
1,110 passed / 0 failed / 4 skips, zero retries. Installed
Linux/macOS: thirteen controls each, zero providers and code-health clear. See
[config metadata recovery](config-metadata-recovery.md). No measured usage/RAM/cache
saving or original-user conversation adoption is claimed. Historical counts overlap.

# v0.7.12: isolated authority caller fixtures

724 pinned paths; runtime source unchanged from v0.7.11. Seventeen test files repair
native config-loader signatures, unavailable-primary isolation and launcher-aware
client PATH assertions. Additional direct callers: 122 files / 719 passed /
0 failed, zero retries; code-health clear. The original 58 failures reproduce on
pre-v0.7.11 runtime bytes. See [authority caller verification](authority-caller-verification.md).
No model calls, production quota/fallback changes or Gateway restart. Historical
counts below overlap and are not a whole-project green claim.

# v0.7.11: profile preparation cancellation and shutdown custody

707 pinned paths. All bootstrap writes and the store opener drain their physical
executor Future before cancellation releases profile custody. Native regression:
273 files / 2,349 passed / 0 failed / 16 existing
skips, zero retries. Final focused selection: 26 passed, overlapping the broad
selection. Installed Linux/macOS: 7 native controls each; code-health clear and
zero provider calls. See [profile bootstrap custody](profile-bootstrap-custody.md).
No original-user conversation adoption or usage/RAM/cache saving is claimed.
Historical results below overlap.

# v0.7.10: atomic fresh schema with fewer initialization commits

703 pinned paths. An empty SQLite schema gets one native declaration transaction;
existing stores retain their previous lock/reconcile behavior. See [fresh schema startup](fresh-schema-startup.md) for the 35.4% fresh-only median improvement and
limits. Native regression: 272 files / 2,335 passed / 0 failed / 16 existing platform
skips, zero retries; code-health clear. Installed Linux/macOS: 8 native controls each,
network denied, zero providers. This is not a whole-Gateway RAM/token/cache/latency
or original-user adoption claim. Historical results below overlap.

# v0.7.9: canonical groups work with ready standby

701 pinned paths. Canonical room controls distinguish an armed standby coordinator
from an unarmed or stopped runtime. Native create/admission wakes its owner once;
empty profiles retain zero idle supervisor threads. See [standby group controls](standby-group-controls.md) for scope. The current selection passes 51 files / 283
tests, zero retries, including all three group failures recorded in v0.7.8. Installed
Linux/macOS acceptance each passes 8 controls and one deterministic offline member
execution, with zero provider calls. Code-health is clear. Original macOS Gateway
and Desktop bundle adoption remain separate; no original-user workload savings claim.
Historical counts below overlap and are retained as history.

# v0.7.8: keep served profiles responsive during cold SQLite open

699 pinned paths. Existing owned executor and scope-aware handle cache; cancellation
drains physical opens and shutdown retains writer visibility. See [profile startup
I/O](profile-startup-io.md) for measured scope and the pre-existing group-control
failure reproduced on the before version. Focused regression: 16 files / 48 passed;
wider selection: 159 passed / 3 existing failures; native Linux/macOS: 8 controls
each, zero inference; native code-health clear. Historical counts below overlap.
No universal startup, RAM, token or original-session adoption claim is made.

# v0.7.7: reuse static plugin manifest metadata

The consolidated stable kit contains 696 pinned paths. Manifest discovery reuses
the existing YAML file cache, then copies metadata for each caller. Native reload,
permission, profile and plugin execution gates stay in place. See [manifest metadata
reuse](plugin-manifest-cache.md) for measured scope and limits.

Current validation: 15 regression files / 203 passed, zero retries; 8 installed
synthetic-home controls per Linux/macOS, zero inference; native code-health clear.
Overlapping historical counts below are not summed. Whole-Gateway task/token/RAM
savings and original-user model-backed adoption remain unproven.

# v0.7.6: demand-start hosted room supervisors

The consolidated stable kit contains 694 pinned paths. Empty canonical hosted
profiles remain ready without a supervisor thread. Existing producers wake
immediately; persisted-room fallback uses the existing watcher. Stop and profile
ownership fences are preserved. See [hosted standby](hosted-room-idle.md) for scope.

Current validation: 9 native test files / 102 passed, zero retries; 6 installed
synthetic-home controls on Linux and 6 on macOS, zero inference. Native code-health
reported no findings. These counts overlap earlier evidence and must not be summed.
Original-user task savings and model-backed adoption remain unproven.

# v0.7.5 native skill aliases on Kanban cards

The consolidated stable kit contains 689 pinned paths. Preflight keeps declared
names accepted by the native loader and reuses the existing catalog cache for
unresolved names. Canonical same-file symlink aliases agree across catalog/loader;
different-file ambiguity and owner/frozen-worker gates remain native.
See [skill discovery](skill-discovery.md) for cold/warm measurements and limits.

The current selection passed 26 files / 472 cases, zero retries. Installed native
Linux/macOS acceptance each passed 17 controls with zero inference. Scoped native
code-health comparison reported no findings, and strict Ruff found no new issues.
Earlier records below are historical; overlapping counts are not summed. This is a
backend-only change; the previously verified Desktop package is unchanged.

# v0.7.4 cycle-safe skill discovery

The consolidated stable kit contains 687 pinned paths. One physical-identity,
branch-local traversal is shared by skill indexing, catalog signature checks and
Kanban preflight. It bounds symlink cycles without dropping independent aliases
or deeply nested valid skills, and retains native dependency/support exclusions.
See [skill discovery](skill-discovery.md) for measurements and evidence limits.

The relevant selection passed 25 files / 463 cases, zero retries. Native installed
Linux/macOS checks each passed 11 controls in isolated homes with zero inference.
No new strict scoped lint findings were introduced; an existing Kanban finding
remains. Earlier test/UI records below are historical and were not rerun or summed.

# v0.7.3 assignee-scoped preflight

The consolidated stable kit contains 683 pinned paths. Native config resolution replaces
two raw YAML behavior reads and preserves configured external skills at card creation.
Frozen workers keep their own snapshot; cross-profile creation defers unavailable
capability inspection to the native dispatcher, which still checks before claim/spawn.
Existing role/ownership metadata gates remain in place. See the [guide](assignee-preflight.md).

The relevant Python selection has 18 files / 208 passing cases by latest per-file
results, zero retries. The source guard passes. Native installed Linux/macOS tool,
config and SQLite acceptance each passed eight controls using synthetic files with
zero inference requests. Candidate runs and repeated hosts are not summed. Earlier
policy/UI suites below are historical baseline, not newly rerun for this change.

# v0.7.2 compact bot settings

Two Desktop presentation paths keep model/effort ahead of expanded role fields and
place optional avatar controls in an Appearance disclosure. See the [editor guide](desktop-bot-settings.md).
Native Linux/macOS typecheck and build, prepared offline packaging, local Mac signature
verification, and rendered packaged-app interaction checks are recorded separately.
The installed packages each passed the same 11 interaction checkpoints in isolated
synthetic homes with zero inference requests. These overlapping host/candidate runs
are not summed. The initial compact editor was checked after fonts settled; model
and effort settings, Save/Cancel, navigation, Workflow, Hub and History were covered.
This revision makes no Python runtime, dependency, account or quota changes. The
v0.7.1 policy suite below is prior evidence; overlapping runs are never summed.

# v0.7.1 optional reasoning effort ceilings

The consolidated stable kit now contains 681 pinned paths. See the [effort-limit guide](reasoning-effort-limits.md) for policy, request boundaries and exact evidence limits. Current change: an 86-file Python selection has 645 passing cases by latest per-file results; 84 files passed the integrated run and two repaired child-environment harness files passed separately. Desktop: 3 files / 25 PASS, typecheck/build PASS, and 5 rendered source-mode checkpoints with an actual isolated backend, zero inference. Historical v0.7.0 broad-suite counts below are baseline evidence, not a rerun on this revision; do not sum overlapping scopes. A separate inherited raw-YAML source guard remains failing and is documented explicitly in the guide. Original-session, packaged-public-build and provider workload acceptance remain separate.

# v0.7.0 consolidated stable kit

See the [complete stable guide](stable-full-kit.md) and [667-path inventory](../patches/stable-full/manifest.json). Broad offline Python: 218 files, 2737 PASS, 13 SKIP, zero failures; UI: 60 files, 383 PASS; typecheck/build PASS. Later two synthetic-only fixture edits: 33 PASS, overlapping the broad scope, not additional unique cases. Native apply/reverse/reapply passed on Linux and macOS. Linux rendered source-mode checks passed 11 interaction checkpoints, including explicit Kanban opt-in, upstream-card navigation, a native Hub page save, and retained-message reopening. They use the actual backend and a separate synthetic home, with no inference; original-session and packaged-public-build adoption remain separate acceptance.

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

## Cross-profile cache cohorts (v0.6.19)

Five related test files passed 32 offline cases on the candidate and the same 32 cases on installed source in a network-isolated environment; these overlapping runs are not summed. Cases cover distinct profiles, duplicate and conflicting records, missing fields, invalid values, unknown accounts, failed calls, CLI opt-in and output privacy. The feature reads existing logs only and performs no provider request. Cohort equality is observational evidence, not a claim of shared cache origin or savings.

## Verified goal waits (v0.6.20)

Eleven related test files passed 298 cases with 4 Windows-only skips on both the offline candidate and installed source in isolated Linux runs; the runs overlap and are not summed. Cases include a real isolated sleeper, saved state, PID reuse, registry error or missing handle, watch triggers, legacy targets and CLI/Desktop pause notices without dispatch. No provider request was made. An idle preflight is required for source installation; existing processes need a safe reload before they use new code. These tests do not establish live task behavior or measured token savings.

## Snapshot integrity and traversal (v0.6.21)

Nine related test files passed 141 offline cases on the candidate and on installed source in isolated Linux runs; these overlapping runs are not summed. Cases cover failed file and database copies, missing or inaccessible state, oversized files, unreadable directories, excluded subtrees, preserving the older snapshot, and incomplete restoration. Read-only enumeration of one existing board root returned the same included file names while skipping excluded subtrees; its timing is a single local sample, not a general backup-speed or disk-savings claim. No production backup was restored, no existing recovery snapshot was removed, and no provider request was made.

## Safe autonomous reassignment (v0.6.22)

Thirteen related test files passed 235 offline cases with one skip on the candidate and on installed source in isolated Linux runs; the overlapping runs are not summed. Regressions cover a live isolated sleeper and manual claims, stale bot status, concurrent completion, claims and reassignment, new and prior explicit holds, released historical holds, and sticky failures. No live card was reassigned and no provider request was made. These tests do not prove production behavior, current bot availability, or usage savings.

## Passive intermediate task status (v0.6.23)

Seventeen related files passed 183 offline cases against installed source in an isolated Linux run. An earlier candidate suite passed 182 cases, followed by 18 focused cases including a real dashboard transition; these runs overlap and are not summed. Cases cover passive status visibility, actual completion and review delivery, parent invalidation, changed-lane and unknown metadata, busy sessions, renderer failure, and pre-existing pending or ambiguous receipts. No live task or provider call was used for verification. One read-only seven-day sample found no matching historical status receipts in the boards inspected, so runtime usage savings remain unmeasured.

## Concurrent task idempotency (v0.6.24)

The previous implementation produced two tasks in isolated simultaneous two-connection and two-process reproductions. After the fix, 16 related files passed 270 tests with one Windows-only skip against the installed source on Linux. Coverage includes existing-key read-only fast paths, distinct keys, archived reuse, nested graph transactions and rollback. No production task or model call was created for this verification; production usage savings were not measured.

## Dispatch pause and shared capacity (v0.6.25)

Twenty-four related test files passed 279 offline cases with one Windows-only skip against installed source on Linux. Cases cover direct and dashboard pause, an existing worker, a pause during a tick, root pause, resume, dashboard and daemon caps, independent profiles, two simultaneous processes on separate boards, unavailable or contended locks, unknown board capacity, and read-only WAL counts. In a small synthetic tmpfs sample, five runs of 16 fake admissions across four boards took a median 134.401 ms before and 143.475 ms after; this does not measure production latency. Actual behavior under a resumed live dispatcher and usage impact remain unverified.

## Emergency-stop inspection failures (v0.6.26)

Thirteen related test files passed 148 offline cases against installed source on Linux; macOS-specific tests were skipped. Injected filesystem errors exercised profile and fleet-root paths, cron, gateway and Kanban admission. The tests do not establish that an I/O failure occurred in production or measure production usage.

## Honest pause and resume status (v0.6.27)

Twenty-one related files passed 264 offline tests against installed Linux source; macOS-specific tests were skipped. Tests cover CLI and gateway responses, partial deletion, unreadable state, unsaved reasons, localization catalog parity, and a real mode-000 directory in an isolated temporary home. These cases do not prove a production I/O failure occurred or measure usage savings.

## Global pause across profiles (v0.6.28)

Twenty-two related files passed 282 offline tests against installed Linux source; macOS-specific tests were skipped. Tests cover CLI and gateway controls, separate profiles and roots, cron and Kanban guards, existing work, failed root resolution, concurrent creation, reason preservation and localization parity. A separate isolated multi-process smoke used installed code and a real temporary process; no production model request was created.

## Linked emergency-stop safety (v0.6.29)

Eighteen related files passed 206 offline tests against installed Linux source. Tests cover dangling and valid symbolic links, hard links, link replacement between inspection and open, a no-NOFOLLOW capability fallback, short writes, ordinary sentinel mode preservation, cron and Kanban guards, and I/O failures. A separate isolated multi-process smoke used installed code and a real temporary process; no production model request was created and no production incident is asserted.

## Scoped and fresh reassignment status (v0.6.30)

Twenty-six related files passed 431 offline tests against installed Linux source; four Windows-specific cases were skipped. Regressions cover fleet isolation, context-local custom roles, stale and malformed snapshots, timestamp boundaries, unreadable or disappearing files, and blocked quota-failure behavior. A separate native registry/SQLite smoke used only temporary boards; no production card was reassigned or model request made.

## Scoped session links (v0.6.31)

Ten related files passed 239 offline tests against the installed Linux source; three Windows-specific cases were skipped. Temporary SQLite fleets covered direct links, profile mismatch, identical IDs, tombstones and live-context exclusion. A separate installed-source smoke used synthetic data only; it emitted an isolated update-bootstrap warning and did not validate a production session or measure model usage.

## Session link identity (v0.6.32)

Ten related files passed 245 offline tests against installed Linux source; three Windows-specific cases were skipped. Temporary SQLite fleets covered profile-switch round trips with colliding IDs, default and named profiles, discovery, browsing, aliases and reserved names. A separate installed-source smoke used synthetic data only; it emitted an isolated update-bootstrap warning and did not validate a production session or measure model usage.

## Session-scoped recovery (v0.6.33)

Twenty related files passed 318 offline tests against installed Linux source; three Windows-specific cases were skipped. Synthetic SQLite sessions covered middle-of-history tool output, colliding profiles, unrelated hits, visibility, bounded excerpts, Boolean queries, Thai, concurrency and interruption cleanup. A separate installed-source smoke used synthetic data and emitted an isolated update-bootstrap warning; production recall and real usage savings were not verified.

## Recoverable tool results after compaction (v0.6.34)

Thirty related test files passed 457 offline tests against installed Linux source. Isolated SQLite tests covered in-place and rotation publication, row-ID and unique call-ID resolution, ambiguous and missing originals, prior rewinds, concurrent appends, rollback, scoped search and removal of private markers. A native compressor with a deterministic local summary also recovered a demoted result. These fixtures do not establish production occurrence or quantify real usage savings.

## Bounded session recall (v0.6.35)

Twenty-five related test files passed 283 offline tests against installed Linux source. Isolated database fixtures cover rewinds and hidden rows, concurrent changes to title and search results, profile collisions, Unicode and structured pages, legacy readers, and recovery of compacted tool output. One synthetic scroll of eleven large messages returned 178,005 bytes before and 18,611 bytes after; this is not a measurement of production usage or model tokens. No model calls were made.

## Structured session recall (v0.6.36)

Twenty-nine related test files passed 361 offline tests on the installed Linux source. Isolated SQLite fixtures cover multilingual text, image payload exclusion, JSON-escaped tool arguments, byte offsets, unpaired surrogates, read-only and concurrent queries, deadlines, rewinds, and existing prompt-cache and profile boundaries. In three synthetic runs using 12 MB plain bodies, median scoped-search time changed from 19.36 to 28.27 ms; for a tool-argument hit with an unrelated 12 MB body it changed from 60.35 to 42.43 ms and peak RSS increase from 58,396 to 23,000 KiB. A separate 10 MB multimodal fixture was found after the change but not before. These are synthetic measurements, not live model usage or token savings. No model calls were made.

## Search log privacy (v0.6.37)

Eight related test files passed 138 offline tests on the installed Linux source. Synthetic successful, empty, and failed searches confirmed that slow-search logs retain diagnostic metadata without the search text. The gateway was reloaded using its native idle-only control. No model calls were made.

## Search expression fallbacks (v0.6.38)

A Linux offline regression suite checked exact phrases, mixed CJK text, boolean operators, punctuation, and Latin prefixes with native CJK and trigram indexes. Fifteen targeted cases passed on the installed source, with ten existing CJK-index cases. A separate ten-file search suite passed 186 tests on the candidate. The gateway reloaded through its idle-only control. No model calls were made. These tests do not establish production latency or usage savings.

## Bounded full-text search snippets (v0.6.39)

A Linux offline regression suite exercised long CJK and Latin tokens, long highlights, literal marker-like text, multiple hits, and the session search tool. Seven targeted cases and 15 earlier phrase-fallback cases passed against installed source. A separate 15-file search suite passed 220 tests on the candidate; these suites overlap. In one synthetic three-hit run with roughly 8 MiB per message, the tool response shrank from 25,170,683 bytes to 5,293 bytes and sampled peak RSS increase fell from 114,344 KiB to 41,156 KiB. One-hit peak RSS remained high because SQLite may materialize a large field. These figures are not production usage or latency measurements. The gateway reloaded through idle-only control; no model calls were made.

## Read-only cross-profile CJK search (v0.6.40)

Offline synthetic tests covered cross-profile search, tokenizer and index absence, stale indexes, a caller-owned transaction, a concurrent writer, and percent-sign fallbacks. Sixteen focused tests, 199 wider search tests, nine state tests and 80 read/write safety tests passed; seven platform-specific cases were skipped. These suites overlap. After installation, a three-file suite passed 91 tests on installed source. In a synthetic 40-run profile-open test, the query returned two matching rows instead of one, with median open times of 1.494 ms versus 1.421 ms before the change. This is not a production usage or speed measurement. The gateway reloaded through idle-only control; no model calls were made.

## Structured global recall (v0.6.41)

A 22-file offline suite passed 456 tests on both the candidate and installed source. Tests
cover nested escapes, word boundaries, Boolean/prefix queries, image-only and hidden-row
rejection, read-only CJK snapshots, bounded excerpts, timeout reporting, caller
transactions and progress handlers. Two timeout-injection tests were updated to target an
execution path that remains active after lazy evaluation; the retained assertions still
require a timeout. A synthetic 460,000-row mixed fixture with 30% large argument fields
passed all 15 trials: three trials each for two Latin terms, CJK, no-hit and frequent-word
queries. The frequent-word case returned all 20 expected results in 1.17–1.18 seconds,
compared with a three-second timeout in the earlier candidate. The slower Latin case took
2.78–2.82 seconds, so its deadline margin remains small. A private, bounded real-history
subset was searched in transient RAM storage with source identity and bounded-page checks;
it was not a search across a live production database. These results do not establish
natural-workload latency, usage savings, or compatibility with every SQLite build. The
gateway adopted the installed files through native idle-only reload. No model calls were
made.

## Bounded history byte readers (v0.6.42)

On the verified Python 3.14.7 / SQLite 3.53.1 runtime, 20,000 closed native Blob reads retained about 1.77 MB while their connection object remained alive. Closing and releasing that object returned the bookkeeping. This behavior agrees with the [CPython connection implementation](https://github.com/python/cpython/blob/v3.14.0/Modules/_sqlite/connection.c#L585-L590). The Hermes raw-search regression failed before the repair and passed afterward with a live-connection allocation budget below 256 KiB.

A 24-file offline suite passed 468 tests on both candidate and installed source, including concurrent-writer snapshots, caller transactions/handlers, invalid bytes, two-megabyte fields and bounded page reads. The synthetic 460,000-row fixture passed all 15 trials. Peak process RSS was about 63.8 MiB instead of 134.3 MiB in the preceding fixture run; this is not a production memory measurement. CJK searches took 1.54–1.57 seconds versus about 1.03 seconds before this repair, a deliberate tradeoff for bounded retained memory. Frequent-word queries stayed near 1.17 seconds; the slower Latin case stayed near 2.78–2.79 seconds and has little margin under the unchanged three-second deadline.

The gateway adopted installed source through native idle-only control. A permitted real-history subset was checked privately in transient RAM storage; this did not search an entire live profile or establish natural-workload usage savings. No extra model calls, provider probes or dependency changes were made.

## Deployment acceptance checklist (v0.6.43)

This documentation-only release separates exact installation, process adoption, interactive behavior and measured workload outcomes in an operator checklist. The v0.6.36 feature entry now identifies its global-search limitation as historical and links to the v0.6.41 correction. It does not change the cumulative native patch, model routing, quotas, provider settings or runtime defaults.

The exact release inventory and local documentation links are verified. Existing native regression and workload evidence above remain historical; no native suite or model task is repeated for unchanged source. Offline CI and public file/history/archive privacy checks validate the new artifact separately. The checklist does not certify that any particular deployment has completed every row.

## Answer cards in narrow chat tiles (v0.6.44)

An actual installed-package journey reproduced clipped card images beside an open HTML artifact. The native Playwright regression failed before repair and passed afterward. Seven related UI files passed 52 tests; two native Electron E2E tests passed, including older-session restoration. The runs overlap in behavior and are not summed. Renderer and E2E TypeScript checks passed. A preexisting restoration-test bridge type was narrowed so it no longer relies on an undeclared Window member.

After local source and package installation, six isolated native interaction checks passed for tables, supplied cards/images/links, Mermaid open/close, an interactive HTML artifact, malformed-source recovery and narrow chat layout. The artifact's local button updated and parent-document access was denied by its existing opaque sandbox. The 560-pixel test viewport lowers the minimum size only in the fixture; it is not a new production mobile-support claim. Model requests and external-application opens were zero. Offline font loading was denied; deliberately invalid card data exercised the existing error boundary and source-highlighting fallback, with their expected console messages. No uncaught renderer exception occurred.

Runtime lint retained the same 13 existing errors and three warnings; the new E2E file is clean. This is not a whole-repository lint claim. A two-GiB diagnostic TypeScript heap was insufficient; the renderer check passed with a four-GiB heap in the maintenance process. Service memory limits and dependency selection were unchanged. Owner Desktop remained closed, Gateway was not restarted and no model/provider probe was used. Production-window interaction and workload savings remain separate acceptance.

## Mac installation/update and backend startup (v0.6.45)

A native Apple Silicon experiment applied public v0.6.43 and v0.6.44 archives to separate exact-base checkouts. Base verification, normal Git apply and installed hashes passed for 569 and 570 paths respectively. Each version launched the existing Python 3.13 CLI. Across separate processes selecting the newer source with the same isolated home, one synthetic SessionDB row and its native search result remained available. The CLI version string still identifies upstream Hermes, not the Legion kit. No production source, application, credential store or real conversation was copied or replaced.

The public setup/doctor recipe also passed on macOS. Doctor reported `offline_ready: true` and `runtime_ready: unknown`; no native credentials or live profile configuration were generated. The companion suite initially failed on both system Python 3.9 and native Python 3.13 because the test fixture used the system's `/var` alias. Only the fixture root was canonicalized; the runtime exporter and explicit linked-destination refusal stayed unchanged. All 75 companion cases then passed on each interpreter and on Linux. These are overlapping cases, not 225 distinct tests.

Using admitted copies of existing native dependencies and packager suppliers, the patched native renderer/main/preload built and an arm64 package was produced with external networking denied. No dependencies or models were downloaded. An obsolete signing CLI flag was rejected before packaging; removing that harness flag allowed packaging. Certificate discovery was disabled, so the initial package did not pass strict signature verification. A separate local-only package copy was ad-hoc sealed with existing native entitlement files using the installed signing library, with no Apple credentials, timestamp, automatic entitlement rewrite or embedded provisioning profile. Deep strict signature verification passed. This is not notarization or a distributable Developer ID build. The host lacked the optional newer icon compiler and used the existing `.icns` fallback.

Actual Electron startup then exposed `NameError: name 'Path' is not defined` while importing the onboarding module on Python 3.13. A fresh-module annotation regression also failed before the repair on Linux Python 3.14, where deferred annotation evaluation had hidden the immediate import failure. The runtime repair adds the missing `pathlib.Path` import. The regression and two related native RPC/onboarding files passed 12 cases on Linux; the same import/annotation regression and a full native server import passed on the Mac. The exact two source/test files were installed locally with a scoped backup, original permissions and native update-lock custody while the owner Desktop was closed and no workers were active. Gateway identity, configuration and the Linux stop policy were preserved; no restart was required for this Python source repair.

After repair, two native Mac Electron tests passed: narrow answer-card layout beside an open HTML artifact, and cold restoration of a synthetic older session omitted from the first history page in the newly packaged app. The first uses source Electron; the second uses the local packaged executable and the explicitly selected patched backend. Mock-provider prompt counts were zero. A prior sandbox attempt denied local singleton IPC and was corrected to permit loopback and Unix sockets while keeping external networking blocked; no owner lock was deleted or process terminated. Original failures remain private evidence. The 12 native and two UI results cover different checks but are not a full upstream suite, full Mac feature audit, actual-provider acceptance or production-app adoption. No new usage, cache-saving, response-time or RSS improvement is claimed.

The cumulative patch now contains 572 paths. Existing patch hunks remain byte-identical; only the onboarding module and its import regression are added. Seven broken relative links in the installation page were repaired. Current public files, reachable Git history, release contents and notes are scanned for credentials and known private identifiers before publication. Machine identities, private paths, test homes, logs, screenshots, source clones and the Mac application package are excluded from the public payload.

## Scoped model catalogs (v0.6.46)

Six failing scope/concurrency/retention regressions and three controls first reproduced
incorrect catalog reuse and duplicate reads. A separate pricing reproduction showed
that capability arrays/objects could discard a catalog, and a boolean could become a
price. The final seven-file native suite passed 213 cases with zero retries, including
17 focused scope, disk-reuse, refresh, concurrency, retention and pricing cases.
Scoped Ruff found zero findings. The native health ratchet had zero unwaived blocking
findings; two documented broad exception catches preserve the inherited optional
provider-probe fallback rather than changing its failure behavior during this move.

A synthetic 1,000-model catalog fixture with eight simultaneous callers ran three
trials per version. Requests were [8, 8, 8] before and [1, 1, 1] after; all returned
the same catalog digest. Median elapsed time was 0.301 s versus 0.135 s; median peak
traced Python allocation was 3,615,725 versus 611,555 bytes. This equal-result fixture
uses baseline-compatible pricing data. The capability-shape failure was retained
separately and verified by correctness tests. These are synthetic transport results,
not service RSS, production latency, token usage or billing savings.

The exact three files were installed on Linux under native update custody with scoped
rollback bytes and original permissions. Native idle-only Gateway restart admission
was accepted; the replacement process postdated installation with zero active agents
and the existing emergency stop retained. No model call was made. Desktop remained
closed; no renderer rebuild was needed for this Python-only change.

Two native Mac trial UI cases passed in isolated homes with external networking denied:
narrow answer cards and cold restoration of an older saved session. Final runtime
ASTs matched those tested bytes after comment-only cleanup. The trial source hashes
were read back; the original Mac application and configuration were not changed.
These UI cases establish backend startup and those interactions, not full production
bot behavior. Natural-workload cache/usage acceptance remains incomplete because the
current read-only sample is dominated by test or unknown provenance and sparse task
bindings; no model requests were added to manufacture a favorable measurement.

## Credential-bound context windows (v0.6.47)

Native red cases demonstrated credential A's confirmed 131,072-token window being
reused by credential B whose catalog reports 65,536; unqualified legacy reuse;
credential/home-blind local memos; malformed provider-specific prices; callable
bookkeeping; unbounded scoped storage; and a lost parallel window write.
The final 14-file offline suite passed 302 cases with zero retries. The installed
Linux source separately passed the 19 focused cases (a subset, not 321 distinct
cases). Scoped Ruff found zero findings; the native health ratchet had zero
unwaived blockers, with two documented inherited best-effort exception policies.

Old fixture assumptions were updated explicitly: account-specific live windows now
use their scoped key while preserving unrelated and anonymous entries; reconciliation
spies include the credential argument; the negative-TTL test advances its clock rather
than depending on a private memo-key shape. Test isolation was corrected by placing the
checkout outside managed state and discarding owned stale compiled test caches after
that move. An early callable test mistakenly called its sentinel in the test itself;
it was corrected, then verified red on the exact baseline and green on the repair.
No test guard, runtime dependency or provider policy was weakened.

An isolated Mac native-Python smoke passed credential-bound overflow persistence,
separate-credential catalog resolution, explicit pin precedence, malformed prices
and non-minting bookkeeping. Two existing native UI journeys passed again with
external networking denied. This is trial-source evidence, not installation of the
custom desktop into the owner's original Mac application. No extra model calls,
provider allowance checks, changed quotas or paid fallback were used.

The exact eight files were installed on Linux under native custody and target-only
rollback, followed by focused acceptance and native idle-only Gateway adoption.
No renderer rebuild was needed; the owner Desktop remained closed. Production
before/after token, latency, quality and whole-service RAM savings are not established
by these tests. Official upstream version migration is a separate acceptance task;
this release preserves its pinned upstream base and does not claim that migration done.

## Stable transport repair (v0.6.48)

The separate seven-path unit was extracted against clean upstream v0.22.5, commit
`bf0203a794a07aac3ff764972ab9087baa4e4f4e`. The original cumulative patch and manifest
remain unchanged. The two new offline files first reproduced ten failures and one
passing origin-isolation control on that public base. After applying only the public
patch, eleven native files passed **88 tests**, zero failures and zero retries in
19.9 seconds. This is one scoped run, not a full upstream suite or an extra 88 tests
on top of overlapping installed-source results. Apply, exact before/after hash
verification, reverse-apply and reapply all passed in the separate checkout.

Native Linux installation had already preserved target ownership and modes under
update-lock custody. The Gateway adopted the files only after native idle admission;
existing profiles, auth stores, quotas, emergency stop and disabled Dashboard stayed
unchanged. A bounded real-provider synthetic developer loop then completed planning,
action, separate review and native terminal handoffs in about 50 seconds. Repeating
creation of the same pinned action returned the same task, and logs showed no further
model call after each terminal tool. The fixture used the same existing account via
native `key_cmd`, without copying OAuth refresh grants or writing bearer credentials
into the fixture. The isolated provider alias is an acceptance boundary, not proof of
production Captain adoption or every role and family. Raw logs, account metadata,
private paths and operational identifiers are not part of this release.

An initial loop exposed the worker wire-mode bug and failed at the planner. A later
loop produced and verified the artifact but hit its private four-turn ceiling before
review handoff. Increasing that fixture-only ceiling to six allowed the final loop;
production quota and bot turn settings were not changed. Failed attempts were retained
privately rather than reported as successful. No new paid fallback was used.

The release verifier now validates the digest and inventory membership of each
additional patch unit. Two new negative cases reproduced its previous omission;
all fifteen focused release-tool cases passed after repair. Separate companion tests,
privacy review, archive verification and GitHub CI are required before publication.
There is no new whole-service RAM, usage, cache-hit, throughput or macOS adoption claim.

## Ambient confirmations and stable upgrade (v0.6.49)

The installed Linux package reproduced a compact-window defect: after Save and
immediate reopen, the success toast covered the dialog's Save button. A loose
in-viewport assertion had passed; an actual center hit test failed because the
toast received the pointer. Ambient confirmations now use the layer below the
modal backdrop, while warnings, errors and actionable notices retain the existing
over-modal layer.

Seventeen notification component/store cases passed, including primary and
secondary recovery callbacks and bounded-stack dismissal. Full Desktop TypeScript
checks passed. The native health ratchet reported no new blockers or measurement
errors for the two paths. A test-only locator option rejected by TypeScript was
corrected; it was not a runtime defect. Existing packager/native dependencies were
consumed with external networking denied; no dependency install was performed.

The candidate and the installed packaged application both passed the real native
settings journey: open Bots, edit role/model/effort, save, reopen and verify retained
values; shrink from 1440×1000 to 1000×760, scroll, verify the full Save rectangle and
its pointer target, and operate Cancel. The fixed installed package returned Save
as the hit target at the same point where the original package returned the toast.
The backend ran in an isolated home using the unmanaged source with the relevant
installed settings/workflow paths matched. Original chats, projects and accounts
were not used. External networking was denied; the only observed resource error
was a blocked optional Google Fonts stylesheet. No model inference was requested.
This is installed-package acceptance in isolation, not the owner's original-window
session adoption, a complete UI audit or Mac deployment proof.

Exact two-source publication and an atomic Desktop image swap used native custody
while the owner application was closed. Gateway identity, profile/auth/config
hashes, modes and ownership were preserved; no Gateway restart occurred. The
rollback image shares 1,170 unchanged files with the active image and keeps the
changed bytes separately, avoiding another complete binary copy.

The nine-path public unit contains the unchanged seven-path v0.6.48 transport
repair plus these two frontend paths. Its native notification cases passed again
on the clean pinned public base using existing matching workspace dependencies.
An initial isolated run lacked the workspace-specific dependency link and failed
before tests; no dependency was installed to correct that fixture. Clean full
apply/reverse/reapply, exact seven-to-nine-path upgrade, and incremental rollback
that retains the transport changes all passed. The inherited 88 transport tests
were not rerun or added to the 17 UI cases as a new combined suite. Earlier full
THINK/ACTION developer acceptance remains limited to its documented scope.

The public release verifier also checks incremental-patch digests and inventory
membership. Two negative upgrade cases first failed; the repaired verifier passes
the scoped cases. No production token/RAM/cache/latency savings, full-fleet
THINK/ACTION adoption or new Mac parity is claimed by this release.

## Native role workflow integration (v0.6.50)

See [stable role workflows](stable-role-workflows.md#verification-boundary) for the clean-base Python/UI scope, one real Captain/developer loop, retained failures and explicit provider/Mac/usage limits. These results do not replace the historical cumulative-kit verification above.

## ARM64 installation and evidence boundaries (v0.6.51)

The [Mac guide](macos-install-update.md#choose-the-patch-base-first) now separates
the cumulative v0.22.2 walkthrough from the alternative v0.22.5 role unit, avoiding
an incompatible full-patch stack or an assumed interpreter upgrade. Patch bytes,
native runtime behavior and dependency locks are unchanged by this documentation
release.

In a separate custom native ARM64 installation, matching PM preparation, Desktop
typecheck/build/packaging, normal CLI source/runtime readback and strict ad-hoc
signature verification passed. The installed application then passed the
role/model/effort, reciprocal-pair, compact-button and navigation journeys using
isolated user data with zero inference requests. See the
[deployment checkpoint](macos-install-update.md#later-arm64-deployment-checkpoint)
for the scope and retained original-session/provider limits. The custom host's
private configuration, account material, logs, screenshots, backups and source
manifest are not published here. This release does not ship a Mac binary or
claim a new production usage, cache, latency or RAM saving.

## Cache miss evidence (v0.6.52)

The optional [four-path cache unit](cache-miss-evidence.md) corrects an unsupported causal inference: a 300-second idle gap was labelled confirmed expiry for all routes. It now records an unexplained provider-reported miss; known Hermes changes and historical metric vocabulary remain intact. Requests, prompt/cache policy, effort, account routes and telemetry consent are unchanged.

The two route regressions and the relay-storage integration failed before repair. Four native files passed 172 tests with zero retries, and the same scoped suite passed on the pinned clean public base. These overlapping checks are not summed. Native production-interpreter readback passed on Linux and ARM64 macOS, with only the idle Linux Gateway reloaded. No original Mac session/Gateway was started, no provider was called, and no usage or cache-hit improvement is claimed. Public apply/reverse/reapply and inventory, history, archive and privacy verification are separate release checks. Older cumulative/runtime/role patch bytes are unchanged.

## Historical privacy maintenance (v0.6.53)

Private operational references were removed from two legacy comments throughout reachable history. A private compact Git bundle preserves reversible recovery outside the publication. All original branches/tags and neutral authorship/tagger metadata were retained; corrected objects and release digests differ. Native Git application reconstructed and checked historical source hashes, and Python ASTs matched before/after the comment-only changes. Per-tree release inventories and tagged archive contents were verified independently before publication. See [privacy maintenance](privacy-maintenance.md) for consumer migration and the limits of repository/cache erasure claims. No Hermes runtime, model request, account, quota or existing worker changed for this maintenance. Native behavior test results remain historical and are not relabelled newly rerun.
