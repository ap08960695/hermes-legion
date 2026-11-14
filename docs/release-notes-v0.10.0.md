# Hermes Legion v0.10.0 — on-demand MCP startup for a profile

## What you will notice

A profile can leave unused stdio MCP servers stopped after their tool schemas
have been cached. Tools remain available; the first call starts the server.
Enable this in that profile's `config.yaml` before its next discovery/startup:

```yaml
mcp:
  memory_saving: true
```

The default is `false`. Explicit per-server `lazy` settings win, including
`false`. HTTP and event-enabled servers keep their existing behavior. Portable
stdio definitions loaded into the profile receive the same policy; direct
session-owned/programmatic definitions are unaffected. Already-connected servers
are not stopped when you edit the switch.

First discovery still connects to learn schemas. A missing, changed or expired
cache also connects normally. Simultaneous first calls now wait for the shared
connection attempt, with one initiating caller owning its failure/cooldown state.
They do not start another server or report a transient "not connected" merely
because another call is opening it.

The switch adds **no idle timeout**. Stateful servers can retain browser or
session state after returning a tool result. Their existing
`idle_timeout_seconds` remains a separate opt-in; `0` disables teardown,
including under `lifecycle:`. Only set an idle timeout when restarting that
server's state is acceptable. Active RPCs keep their existing lifecycle fence.

A compatibility repair also prevents SDK model defaults from masquerading as
peer cache hints. An omitted legacy TTL keeps the existing no-TTL cache behavior;
an explicit zero TTL remains uncached and positive TTLs retain their expiry.
Scope hints are collected independently; caches remain private to each profile.
No cache fingerprint, credentials or cross-profile connection identity changes.

## One measured Mac component case

The same native Hermes MCP client discovered two local stdlib mock servers,
shut them down, then repeated discovery using their schema cache. The same
profile settings enabled the new switch in both the old and changed executors.
Only one of the two tools was subsequently used. No app, gateway, SSH, remote
endpoint, provider or model request was used by this measurement.

| Phase / elapsed operation | Original source | Changed source |
| --- | ---: | ---: |
| Repeated discovery, before any tool: summed RSS | 223.25 MiB | 154.61 MiB |
| Native client + server/supervisor processes at that phase | 4 | 1 |
| Repeated discovery time | 60.36 ms | 1.10 ms |
| First tool call | 3.97 ms | 43.44 ms |
| Subsequent warm call | 0.60 ms | 0.58 ms |
| Maximum process count including cold discovery | 4 | 4 |
| Whole-case sampled peak summed RSS | 223.78 MiB | 223.11 MiB |

The unused phase used **30.7% less summed RSS**. The first call paid connection
latency. Cold discovery still needed both servers, so this is **not a whole-case
peak-memory reduction**. After using one server, that server and its shared
supervisor stayed alive; the unused server remained deferred. Counter state and
schemas were preserved when no idle timeout was configured.

This is one paired case with 20 ms sampling, including shared RSS pages. It is
not a statistical benchmark, whole-app/gateway idle result, production-server
measurement, Linux/Windows acceptance or model-token saving. Native PM Python
3.14.9 and its installed MCP SDK ran against isolated homes on the Mac. A task
Python audit adapter denied network/bind operations and outside-trial writes;
it is not a complete OS sandbox.

## Verification and adoption

Native standard-library regression tests cover actual config loading, explicit
server overrides, HTTP/events policy, portable entries, profile/cache isolation,
wire-hint presence and TTL controls, real cache-first registration, concurrent
first use and one-failure bookkeeping. Native SDK/stdio acceptance additionally
checked active-call survival, explicitly configured idle teardown, zero idle
server/supervisor processes, stable dormant schemas and concurrent revival.

The canonical native pytest suite and pinned Ruff checks were not run: their
interpreters/tools were unavailable locally, and no dependencies were fetched.
The native shell runner also precompiles with CPU-count workers, outside
the task's process limit. This is scoped acceptance, not a full native-suite pass.
See [verification](verification.md) for companion, export and release gates.

This source kit does not ship a rebuilt Hermes.app or modify an installed profile.
P0 Desktop SSH bounds from [v0.9.0](release-notes-v0.9.0.md) remain included.
Automatic teardown of arbitrary stateful servers, memory-aware helper admission,
other update helpers and whole-gateway memory reduction remain separate work.
