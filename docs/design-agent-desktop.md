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

## Second source slice: explicit read-only AX provider

The bounded read-only step registers `agent-desktop` through the existing provider
loader. Selecting it is explicit; cua remains the default. Its label says AX
read-only. Reuse discovery and bounded credential-stripped probes; availability
checks may inspect paths/config but must not spawn npm or the driver. Full npm
discovery remains available at start and through the explicit status command.
When only the npm global probe locates a binary, set the discovered path explicitly
so the cheap availability check can find it too.

Support only `capture` with `mode=ax` and an explicit exact application name.
Require complete protocol2.6 snapshot data for that same app and a valid window,
with bounded payload/tree depth/count, unique snapshot-owned refs and no raw
error disclosure. Map named AX nodes and native refs into existing CaptureResult/
UIElement shapes, using a private namespace per backend session. No image is
captured, saved or uploaded by this backend; snapshot data is returned to the
existing authorized tool caller. Existing tool artifact/approval/lease policy
still applies. Do not add public logging or store raw driver output on failures.

Input, focus, app/window listings, coordinate modes and bounded-permission mode
fail explicitly; no fallback, focus change or fake successful empty result. The
provider currently runs on the gateway host only. It refuses terminal/sandbox or
unresolved placement at start and again before every capture, so a configured
sandbox can never silently become a host desktop read.
It is an opt-in read-only development provider, not the full act/ref/verify backend.
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

## Remaining capability set

Extend the provider with verified act loops using native snapshot refs. Keep secret typing on stdin,
preserve ownership/approval gates, and keep private snapshots/screenshots out of
public logs/uploads. Validate on supported platforms and the isolated native
Hermes UI before one meaningful feature release. Discovery/status alone is not
the complete backend, a native UI fix or permission to connect to another host.
