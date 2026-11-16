# Agent-desktop computer use

Status: unreleased development. GOAL12 adds this after Bot Monitor. Native
Monitor terminal presentation remains an independent acceptance blocker.

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
Seventy focused source cases pass, including35new adapter cases. The real installed
binary is reached only for a private stopped-fixture missing-target error check;
successful capture/tool mapping uses synthetic protocol data. Native successful
adapter capture and Windows/Linux runtime acceptance remain open.

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
Other gestures, `type_text`, keyboard, focus, screenshots and bounded permission
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

## Remaining capability set

Extend the provider with verified act loops using native snapshot refs. Keep secret typing on stdin,
preserve ownership/approval gates, and keep private snapshots/screenshots out of
public logs/uploads. Validate on supported platforms and the isolated native
Hermes UI before one meaningful feature release. Discovery/status alone is not
the complete backend, a native UI fix or permission to connect to another host.
