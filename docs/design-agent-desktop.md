# Agent-desktop computer use

Status: unfinished, opt-in development, excluded from v0.34.0 runtime-readiness
claims. GOAL12 makes this the capability set after Bot Monitor. Monitor Local
acceptance is now recorded separately; the native mutation boundary below remains.

## First source slice: discovery and read-only status

`hermes computer-use status --backend agent-desktop` finds an existing binary
and reports its own version, platform and permission states. The command does
not select a runtime provider or establish that snapshots/actions work. Existing
default and plugin status behavior remains unchanged; `--backend cua` explicitly
uses the built-in status path.

Use `computer_use.agent_desktop.path` for a binary or extracted release directory.
An invalid explicit path fails closed. A directory must identify one executable
at its root or under bin; distinct matches are ambiguous. Otherwise search PATH,
local npm ancestors and the Hermes source root, configured npm prefixes, standard
Homebrew locations, then the npm global prefix. Discovery never installs,
downloads or activates a backend. A release helper stays beside its executable.

Reuse the existing bounded subprocess probe and credential-stripped environment.
Execute only `status`, once after resolution. Validate its command/envelope and
print only the binary, version, platform and known permission states. Malformed,
oversized, failed or timed-out results produce fixed diagnostics, never raw
stdout/stderr or exception text that could contain desktop content or secrets.
Accessibility and Screen Recording stay independent. A missing Accessibility
grant gets an informational command for the owner to run; Hermes does not execute
the guide or change permissions. Valid status is information, not operational
readiness. No extra dependency, daemon, pool, retry or paid/network service.

Approaches: registering an incomplete provider would falsely advertise actions;
a separate installer would duplicate distribution tooling. Extend the existing
status parser and add one shared discovery/status module. Standing delegation
selects this scope; advisor311 supports it. Tests cover resolver precedence,
failure boundaries, platform layouts, protocol/privacy and CLI compatibility.
One real workspace-installed status probe uses isolated HOME and OS boundaries.

The config key is recognized by the existing config command. Setting it preserves
an existing backend and unrelated settings. Exit 0 means a valid status response,
including denied permission states; 1 means no executable found; 2 means invalid
configuration, failed/timeout probe or invalid protocol. Permission grants and
operational readiness are separate. Windows npm shims resolve to the packaged
native executable; Windows/Linux path cases are fixtures, not live OS proof.

## AX capture provider

The provider registers `agent-desktop` through the existing loader. Selecting it
is explicit; cua remains the default. Its label says AX refs. Reuse discovery
and bounded credential-stripped probes; availability
checks may inspect paths/config but must not spawn npm or the driver. Full npm
discovery remains available at start and through the explicit status command.
When only the npm global probe locates a binary, set the discovered path explicitly
so the cheap availability check can find it too.

Capture supports `mode=ax` with an explicit application name and an optional
numeric native `window_id` within that app. Require complete protocol2.6 snapshot
data for that same app, or exact selected window with a valid canonical app label,
with bounded payload/tree depth/count, unique snapshot-owned refs and no raw
error disclosure. Map named AX nodes and native refs into existing CaptureResult/
UIElement shapes, using a private namespace per backend session. No image is
captured, saved or uploaded by this backend; snapshot data is returned to the
existing authorized tool caller. Existing tool artifact/approval/lease policy
still applies. Do not add public logging or store raw driver output on failures.

Unsupported input forms, focus, app/window listings, coordinate modes and bounded
permission mode fail explicitly; no fallback or fake successful empty result. The
provider currently runs on the gateway host only. It refuses terminal/sandbox or
unresolved placement at start and again before every capture, so a configured
sandbox can never silently become a host desktop read.
It is an opt-in development provider, not the full act/ref/verify backend.
Registering actions prematurely would advertise work not implemented; keeping
another standalone CLI path would bypass the actual provider/tool contracts.
Standing delegation selects this scope after the native Monitor baseline failed
before observer attachment. Advisor314 supports one read-only provider operation.
Test selected/default provider behavior, a scoped AX result through the real tool,
private refs/session isolation, unsupported operations and protocol/error bounds.

Example after explicitly selecting `computer_use.backend: agent-desktop`:

```json
{"action":"capture","mode":"ax","app":"Your application name"}
```

For a particular window, supply both selectors:

```json
{"action":"capture","mode":"ax","app":"Your application name","window_id":42}
```

The provider generates `--app APP --window-id w-42` and requires exactly that
returned ID. Accept only positive JSON-safe integers; missing/invalid app scopes
and PID selection are refused before spawning. Use the numeric component of the native
`w-N` ID, not an Electron window index or CUA element index. Obtain it from a
fresh trusted window selection; IDs may become stale or be reused. Selector
agreement alone does not prove enduring process identity. The combined route uses
the app as a native inventory filter and returns its canonical label; this label
may differ. Named-app-only capture still requires exact returned label equality.
There is no prefix/alias heuristic or automatic retry fallback. Complete snapshots
marked `identity_unproven`, including malformed flag values, are refused.
The common-tool window path and refusal/privacy/stale-ref controls pass alongside
existing semantic-action cases: 118 focused source tests, one worker.

### App scope and earlier window-only evidence

Pinned 1.3.1 [core selection](https://github.com/vercel-labs/agent-desktop/blob/b0b7277bea09b770ef9d1fb45aad667bc432cd57/crates/core/src/snapshot/surface_target.rs)
passes the app filter into [native inventory](https://github.com/vercel-labs/agent-desktop/blob/b0b7277bea09b770ef9d1fb45aad667bc432cd57/crates/macos/src/system/window/window_inventory.rs).
Without it, the driver uses global window/AX inventory, including frontmost AX
and accessibility probes for eligible app PIDs. Selecting one returned window
did not confine these internal reads. The earlier window-only isolation claim
is withdrawn; its selected-content/PID/refmap evidence retains that narrow scope.
The unreleased window-only API is now refused. Add `app` to migrate; do not retry
without it. No further unscoped live trial is used to re-prove the failure.

An explicit app filter scopes AX/CG window probes to matching owner PIDs. Native
app-owner discovery still enumerates OS app metadata. Use a unique intended app
identifier; valid canonical text alone is not ownership proof. Native scoped
filtering and exact-window ownership checks are part of the trusted driver
contract; no syscall audit or universal metadata-isolation guarantee is claimed.

Only protocol2.6 is accepted in this slice. Named AX nodes use the existing
element/label response; native refs stay attached to their snapshot. Geometry is
unknown, not a usable coordinate. Output is limited to1MiB UTF-8,2048nodes and
64levels; incomplete/malformed/foreign-target responses fail with a fixed error.
The limit is applied after the house probe captures output, not an OS output-memory
quota. A successful transport does not prove that a visible UI painted correctly.
Seventy focused source cases pass, including35new adapter cases. The initial real-binary
check targeted only a private stopped-fixture missing-target error;
successful capture/tool mapping initially used synthetic protocol data. A later
isolated macOS native capture passes through the actual provider and common tool;
see the native runtime boundary below. Windows/Linux runtime acceptance stays open.

## Single-use semantic ref input

Add semantic `click(element)` and `set_value(value, element)` through the existing
tool's approvals, hardblocks and lease. Only a native ref from the latest complete
capture may advertise Click or SetValue. Bind it to that backend's private session
and explicit target and lease epoch. Serialize capture/input state, invalidate old authority before
replacement captures, and consume every ref before a permitted input is spawned.
Success, timeout, failure and cancellation all require a fresh capture afterward;
there is no retry, physical/foreground path or coordinate fallback.
Human takeover invalidates the earlier capture even after control is handed back.

Element indices must not rebind an approved stale request after a new capture or
backend restart. Use process-wide non-reused positive indices within JSON's exact
integer range; native qualified refs stay private to their snapshot/session. Keep
the existing unknown geometry and explicit capture target requirement.

`set_value` uses native `set-value --stdin`, never a value argument. Preserve UTF-8
bytes, empty strings and line endings; reject NUL and more than128KiB before spawn.
Extend the existing bounded probe with additive bytes stdin so Windows text-mode
newline translation cannot alter a value. Existing text/no-input callers keep
their behavior. Bound native action time/output; drop raw results/errors that may
echo the value. A narrow additive common-tool verdict recognizes recapture-required
results without recommending physical escalation or asserting delivery.

Treat a valid action envelope as command completion only, not verified UI intent.
Input, capture and host-placement authority are rechecked under the same lock.
Other gestures, keyboard, focus, screenshots and bounded permission
mode remain unsupported. No schema, default-provider, approval or lease change.
Advisor315 supports this two-operation slice and atomic consumption. Standing
delegation selects inline TDD; no native Monitor/owner-app action is needed.
Transport fixtures prove success mapping; a real isolated unknown-ref refusal
proves only the native failure boundary, not successful input or application effect.

The installed1.3.1 help and [versioned ref contract](https://github.com/vercel-labs/agent-desktop/blob/v1.3.1/README.md#quick-start)
define qualified refs and stdin. The [action result contract](https://agent-browser.dev/desktop/json-output)
separates delivery from application effect; the [interaction reference](https://agent-browser.dev/desktop/commands/interaction)
describes semantic activation and value replacement. No source claims mouse
mechanics or automatic semantic verification from a successful command.

## Explicit-ref typing

Extend the existing `type` action with its existing `element` field; no schema
change. For agent-desktop, require a fresh snapshot ref advertising `TypeText`.
Use the same atomic single-use/lease/host checks as click and set_value. Send
exact UTF-8 bytes through `type REF --stdin`, including empty input and line ends;
reject NUL, invalid UTF-8 and more than 10,000 bytes before native execution. Refuse
foreground/bring-to-front forms without physical or focus fallback. Type inserts
at the target's insertion point; it does not replace the entire field or prove
caret placement/application commitment. Fresh capture must verify the intended
effect before another input. Use set_value for full value replacement.

The base method adds optional element. Generic dispatch forwards only a supplied
element, rejects malformed supplied indices before approvals, and snapshots
request arguments before approval so the original caller cannot swap the text or
index while approval waits. Targeted approval summaries omit text. Existing
untargeted calls retain their signature and preview. Cua explicitly refuses
targeted type before any input, with no physical escalation advice; it retains
existing untargeted behavior. Third-party providers need to support the optional
argument to accept targeted type; old untargeted signatures still work.

Standing delegation chooses this source slice after171 native capture failed.
Advisor318 supports the smallest existing-contract extension. Meaningful tests
cover dispatch/approval/privacy, bytes boundaries, capabilities and consumed refs.
Native unknown-ref refusal is refusal evidence only; real application insertion,
caret placement and Monitor acceptance remain independent live gates.

## Ref scroll areas

Add scroll through the existing scroll action and shared single-use ref execution.
Require an explicit latest captured element whose native canonical role is
`scrollarea`; an arbitrary element advertising ScrollTo is not a scroll area.
The [scroll contract](https://agent-browser.dev/desktop/commands/scroll) assigns
refs to scrollarea nodes. That role authorizes an attempt, not successful delivery
on every platform; native headless policy may refuse without physical fallback.
Only up/down/left/right and exact integer amounts 1–50 are accepted, using the
existing cua action bound. Omitted amount defaults to3. Reject bool/string/float/
null, nonpositive/oversized counts, geometry, modifiers and foreground/focus.

Common dispatch preserves the supplied amount for provider validation. Move its
old int conversion into cua, preserving that backend's existing coercion/clamp.
Schema-valid integer calls to other providers stay unchanged; those providers now
receive the original value for malformed requests instead of a coerced integer.
Reusing _act retains atomic consumption, lease/host binding, timeout/privacy and
mandatory fresh capture after every attempt. Native completion cannot establish
that a desired row is visible. Read fresh state before any further input.

Standing delegation selects this next source slice; advisor319 supports bounded
role semantics and existing guards. Use focused regression and native unknown-ref
refusal only while the prior native capture/Monitor blocker remains unresolved.

## Native capture and mutation runtime boundary

The actual macOS provider and common `computer_use` tool now capture the full
production Local Hermes Monitor window: one complete native snapshot, 50 refs,
78 mapped elements, and an exact owned app/process/window/session witness.
CUA AX and pixels before/after corroborate the device nonce, default profile,
Connected state and Monitor view. The table is present in AX below the visible
fold; this is not separate pixel acceptance of every table cell. The fixture is
foregrounded after an exposed Raise; background operation remains unverified.

Capture runs in the existing gateway thread, with one native snapshot child.
A fresh guardian sample must show three product processes and memory headroom
before the fourth child is admitted. Exact binary hash, argv, environment,
single-use admission, profile lease, placement and nonce/PID-birth/executable/
window/refmap checks remain enforced. The validated baseline ACK starts one
120-second capture phase directly, followed by the bound final comparison ACK.
A redundant second manual phase ACK was removed after it raced the gateway;
it conveyed no input permission. The original 335-second acceptance deadline,
360-second total, cleanup reserve and per-call identity/freshness fences remain.

The successful isolated trial passes the 60-second Local gate and final ACK,
then closes every owned process. Sampled peak is four product processes and
914,702,336 bytes including the guardian; external CUA/advisors/build/controllers
are excluded. This is capture acceptance, not a whole-service RAM or savings
claim. No model prompt, native input, provider screenshot or owner-app adoption
is part of this trial. Private before/after evidence is retained under
`../evidence/agent-desktop-native-capture-20261117`.

Earlier failed trials stay failed: a phase-handoff race stopped before provider
execution; another complete snapshot returned a 31-character prefix of the
36-character fixture app name and failed exact-app validation. The successful
case uses a short unique app name. Native AX exposes the nonce as a separate
static text node where CUA joins it with “Device”; the fixture checks the exact
nonce in both representations. A later fresh long-name fixture passes through
explicit window selection: its returned canonical app label differs, while the
exact native window ID, owned process lifetime, nonce and refmap agree. No named
app comparison is relaxed. This trial again maps 50 refs/78 elements, matches CUA
AX/pixels, passes 60 seconds Local and the final bound ACK, and closes all owned
processes after 105.83 seconds. Sampled peak is four product processes/seven
including OS utilities, 916,946,944 bytes including guardian, with the same
external-observer exclusions. Native input/model calls/provider images remain
absent. Private before/after: `../evidence/agent-desktop-window-capture-20261117`.
This historical window-only result proves selected output, not isolated inventory;
the app-required contract above supersedes it.
Never accept a prefix merely to make an identity check pass. The earlier tiny
synthetic-renderer capture and unknown click outcome retain their narrow scope.

### Foreground app + window recapture

A fresh full-production Local Monitor passes three sequential actual provider/
common-tool snapshots with both selectors. Each maps 50 refs/78 elements; one
backend session, distinct snapshot IDs and disjoint element indices. Exact owned
PID/birth/executable, original window generation, native window, nonce and refmap
agree each time. Fourth-slot reservations prevent overlapping native children
and require fresh three-process/headroom samples. Paired CUA AX/pixels and final
bound ACK pass; the table remains below-fold AX evidence. The original deadlines,
Local/write/lease/cleanup guards remain. No native input/model call/provider image.

The foreground trial closes in 132.78 s with zero survivors, sampled peak four
product processes/seven including OS utilities and 921,600,000 bytes including
guardian. External CUA/advisors/build/controllers are excluded; no whole-task RAM
or savings claim. Private before/after: `../evidence/agent-desktop-app-scoped-capture-20261117`.
The separate cold inactive app-scoped trial fails `WINDOW_NOT_FOUND` after 60 s
Local. Native scoped inventory drops windows not classified visible/minimized;
visibility/Space association is a hypothesis, not established root cause.
Foreground success does not establish cold inactive or background pixel support.

### Minimized native AX recapture

A separate isolated production Local Monitor passes three app + window scoped
provider/common-tool snapshots while its original window is minimized. Each maps
47 native refs/75 elements; one backend session, three snapshot IDs and disjoint
indices. Fresh own-Electron state, events and 100 ms samples bind the same
PID/window generation/native ID. Thirteen witness rows span 1,215 ms, bracket all
three reads and report minimized/unfocused throughout, with maximum gap 102 ms.
This supports no target-window focus observed in that interval, not absence of
every transient focus or an independent OS visibility/current-Space audit.

CUA baseline AX/pixels precede minimization. The final CUA observer runs only after
native work finishes, restores the window and matches Monitor/nonce/default/
Connected before the bound final ACK. These are restored pixels, not minimized
CUA AX or minimized pixels. The first case remains failed: restoration occurred
during its follow-up CUA AX observation and the fresh minimized ACK refused it,
before any native capture. Another case stops on a ScreenCaptureKit parameter
error before minimization. A shared fixture bundle ID was found; the successful
case uses a distinct ID, but that does not establish the error's cause.

The successful case passes 60 seconds Local and all existing scope/ref/resource/
lease/deadline guards, then closes in 107.92 s with zero survivors. Sampled peak:
four product processes/six including OS utilities, 946,978,816 B including guardian;
external CUA/advisors/build/controllers are excluded. No product code change,
native input, model call, provider image, whole-task RAM or savings claim. Cold
inactive/other-OS/input acceptance remains open. Private baseline/restored proof:
`../evidence/agent-desktop-minimized-capture-20261117`.

### Background capture diagnosis

Two fresh isolated production Local trials remain failed. The first uses a
fixture-only `showInactive` reveal; during CUA app selection, Electron reports
activation and the guard stops before native capture. The second avoids
CUA and passes 60 seconds Local with no target focus/activation observed across
581 Electron witness rows (maximum gap 207 ms). Its first exact-window native
snapshot returns `ACTION_NOT_SUPPORTED` / `window_without_accessibility_element`.
No complete snapshot or recapture loop is accepted. These are not pixel evidence,
an independent continuous macOS activation witness, or unchanged startup proof.

The provider now maps only that supported protocol2.6 snapshot failure to fixed
guidance about the target app's accessibility support. Native error titles,
window IDs and suggestions are never copied into the error; other/malformed
failures keep generic guidance. Failure still invalidates previous refs and does
not focus, retry or fall back. Three regressions fail before the change; the
backend/action source files then pass 110 tests. Replaying the retained native
failure through the actual common tool confirms the new message without another
native operation. That is offline replay, not a successful after-fix UI trial.

Both trials close all owned processes; eight configs and two geometry absences
are restored. Private diagnosis: `../evidence/agent-desktop-background-diagnostics-20261117`.
The app already has a renderer-accessibility helper; the cause of cold inactive
window exposure remains unresolved. Investigate it before adding another enable
switch. Background CUA/pixel and native act/verify acceptance remain open.

### Snapshot and input write authorization

The pinned 1.3.1 [snapshot command](https://github.com/vercel-labs/agent-desktop/blob/b0b7277bea09b770ef9d1fb45aad667bc432cd57/crates/core/src/commands/snapshot.rs)
uses `snapshot::run_with_context`, then `RefStore::for_session` and
`save_new_snapshot`. Its session refstore lock, latest-snapshot marker and refmap
live beneath the configured `AGENT_DESKTOP_HOME`. The successful capture uses an
owned workspace state root under the existing write fence. Hermes retains its
own `HERMES_HOME/bot-desktop` lease checks; no lease is disabled for capture.

Native input's existing `InteractionLease` instead creates/manages the canonical
`/tmp/agent-desktop-<effective-uid>` directory and `interaction.lock` artifact
(macOS resolves `/tmp` through `/private/tmp`). A no-UI source-function probe
previously reproduced the workspace write refusal there. This is a necessary
fixture blocker, not proof of the earlier click's exact failure provenance.
At those earlier trials, no narrow write exception had been established for
that canonical mechanism. Workspace refstore access and a permission status did
not prove input readiness; those failed trials remain failed.

Later GOAL lead notes report Mac Screen Recording granted and ask to continue
input-lease work on an isolated test app. The capture-permission blocker is
cleared by that report; native lease acquisition/act/verify is still untested.
Bind future input to the test app and the applicable write scope, retaining the
canonical lease instead of relocating/bypassing it or changing system permission
settings. Ordinary installations are not subject to the earlier fixture's write
rule. Workspace runtime preparation and a later contained pet-RPC trial perform
no permission audit or native input. [Pet-handler proof](native-checks-and-test-memory.md#profile-bound-pet-rpc--contained-mac-acceptance)
does not establish capture, canonical input lease or act/verify readiness.

## Remaining capability set

Extend the provider with verified act loops using native snapshot refs. Keep secret typing on stdin,
preserve ownership/approval gates, and keep private snapshots/screenshots out of
public logs/uploads. Validate on supported platforms and the isolated native
Hermes UI before one meaningful feature release. Discovery/status alone is not
the complete backend, a native UI fix or permission to connect to another host.
