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

## Remaining capability set

Add the provider through the existing computer-use registry and backend contract,
with native snapshot refs and verified act loops. Keep secret typing on stdin,
preserve ownership/approval gates, and keep private snapshots/screenshots out of
public logs/uploads. Validate on supported platforms and the isolated native
Hermes UI before one meaningful feature release. Discovery/status alone is not
the complete backend, a native UI fix or permission to connect to another host.
