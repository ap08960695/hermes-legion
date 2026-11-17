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

Capture supports `mode=ax` with an explicit exact application name.
Require complete protocol2.6 snapshot data for that same app and a valid window,
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
the existing unknown geometry and explicit app capture requirement.

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

A production main/preload build with a tiny synthetic renderer now passes an
actual macOS provider capture: five native refs, independently checked process
identity, nonce content and window/session binding. CUA verifies the initial
screen after an explicit Raise. This proves foregrounded fixture capture only;
Bot Monitor, background operation and input effects remain unverified.

On macOS, agent-desktop 1.3.1's default interaction lease uses
`/tmp/agent-desktop-<uid>/interaction.lock`, independently of HOME, TMPDIR and
AGENT_DESKTOP_HOME. The [versioned implementation](https://github.com/vercel-labs/agent-desktop/blob/b0b7277bea09b770ef9d1fb45aad667bc432cd57/crates/core/src/session/interaction_lease.rs)
creates a private runtime directory; [ref execution](https://github.com/vercel-labs/agent-desktop/blob/b0b7277bea09b770ef9d1fb45aad667bc432cd57/crates/core/src/ref_action/ref_action_wait.rs)
acquires this lease before dispatch. A workspace-only write sandbox conflicts
with that requirement even when snapshots succeed. A no-UI source-function
probe reproduces INTERNAL/EPERM there; an owned workspace control succeeds.
This is a fixture boundary diagnosis, not an Accessibility diagnosis or a runtime
fix. The earlier live click's delivery/effect remain unknown.

Do not infer action readiness from status or capture. Do not bypass the canonical
lease, substitute a per-profile lock, weaken the sandbox or change permissions
to make this fixture pass. Continue Monitor acceptance with the supported CUA
path; native mutation acceptance needs compatible canonical coordination first.

### Snapshot and input write authorization

The pinned 1.3.1 [snapshot command](https://github.com/vercel-labs/agent-desktop/blob/b0b7277bea09b770ef9d1fb45aad667bc432cd57/crates/core/src/commands/snapshot.rs)
uses `snapshot::run_with_context`, then `RefStore::for_session` and
`save_new_snapshot`. Its session refstore lock, latest-snapshot marker and refmap
live beneath the configured `AGENT_DESKTOP_HOME`. This is separate from the
canonical native interaction lease. An explicit owned workspace state root makes
this capture path eligible for the existing workspace write fence; it does not
relocate or authorize the native input lock. Hermes also retains its own
`HERMES_HOME/bot-desktop` lease checks. No lease is disabled for capture.

Native input remains blocked in this fixture until the owner grants a narrow
exception for the existing canonical mechanism to create/manage its required
`/tmp/agent-desktop-<effective-uid>` directory and `interaction.lock` artifact
(macOS resolves `/tmp` through `/private/tmp`). Workspace refstore permission,
Accessibility permission and the desired feature do not grant that exception.
Never try an input operation merely to test whether the forbidden write works.
This is the trial's authorization boundary, not a claim that ordinary installations
cannot use native input.

Full-production capture acceptance is still open. The first preparation trial
exits before gateway readiness: placing the fixture directory before source makes
its `gateway.py` shadow the production package. No Electron app or native driver
starts. A future-only bootstrap puts source before fixture helpers and validates
the resolved gateway package and exact capture/admission helper paths before
startup. Under the same OS/audit fences, actual imports pass; fixture-first gateway
shadowing and a foreign capture helper both fail before startup. The original
failed trial is retained, with no live retry or capture-success claim.

Next fresh trial: one default profile, unchanged production renderer/main/preload,
one common-tool AX capture in the existing gateway process, and one exact
snapshot subprocess admission. Compare nonce content, PID/birth/executable,
window generation and native refs with CUA AX/pixels. Keep the four-process,
3.5 GiB, Local-only network/write/SSH and cleanup fences; no model prompts or
native input. Import preparation does not establish runtime readiness or earn a
feature release.

## Remaining capability set

Extend the provider with verified act loops using native snapshot refs. Keep secret typing on stdin,
preserve ownership/approval gates, and keep private snapshots/screenshots out of
public logs/uploads. Validate on supported platforms and the isolated native
Hermes UI before one meaningful feature release. Discovery/status alone is not
the complete backend, a native UI fix or permission to connect to another host.
