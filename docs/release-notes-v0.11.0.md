# Hermes Legion v0.11.0 — lighter cached MCP startup

## What you will notice

Hermes now leaves the MCP SDK unloaded while registering tools from a valid
lazy-server schema cache. Tools and their parameters remain available. The SDK
loads when a connection is actually needed, including the first tool call,
uncached discovery and an enabled-server probe. Empty registration and an empty
probe also avoid the import.

Use the existing [profile memory-saving setting](release-notes-v0.10.0.md), or
an explicit per-server `lazy: true`, to use cached startup. There is no new
setting or dependency. Profiles that connect immediately retain that behavior;
missing, changed or expired caches still connect to obtain current schemas.
The missing-package and safe-worker gates, filters, trust, profile isolation,
cache policy and explicit idle settings retain their existing paths.

The first call pays the deferred import cost. Once loaded, the SDK remains in
the client process; this does not unload modules or discard stateful servers.

## One measured fresh Mac client

An isolated native Hermes client first populated its schema cache through the
installed MCP SDK and a local stdlib stdio peer, then stopped. Two fresh clients
ran the same configured discovery and concurrent first-call case, before and
after the change. Their fixture, audit bootstrap, case code and tool schema
matched. The peer's counter returned 1 and 2 from one server instance, then 3
on a warm call. All child processes stopped at case completion.

| Phase / operation | Previous source | Changed source |
| --- | ---: | ---: |
| Cached discovery, before tool use: summed RSS | 151.22 MiB | 116.70 MiB |
| Processes at that phase | 1 | 1 |
| MCP SDK loaded at that phase | Yes | No |
| Cached discovery time | 255.04 ms | 5.20 ms |
| Two concurrent first calls, batch elapsed | 55.83 ms | 325.74 ms |
| Subsequent warm call | 0.53 ms | 0.58 ms |
| Whole-case sampled peak summed RSS | 199.75 MiB | 199.72 MiB |
| Maximum process count | 3 | 3 |

Before tool use, the fresh client used **34.52 MiB less RSS (22.8%)**. Whole-case
peak memory did not meaningfully decrease. The first-call batch moved SDK import
work from startup to use. These percentages must not be added to v0.10.0's
different, already-warmed two-server case.

This is one paired native component case, with 20 ms samples and shared RSS
pages included. Python 3.14.9 and MCP 2.3.0 ran on the Mac with isolated homes;
no Hermes.app, gateway, SSH, other machine, external endpoint or model was used.
A task Python audit adapter denied network and outside-trial writes; it is not
a complete OS sandbox. These are not whole-app idle, production-server,
Linux/Windows, model-token or billing measurements.

## Verification and adoption

Four metadata regression cases failed with the previous discovery gates; two
refusal controls passed. The real cold-seeded cache also exposed the eager SDK
import through both registration entry points. The changed source passes six
new cases plus the prior eighteen native MCP memory-policy cases. Cached tool
parameters and utility schemas remain available without invoking the SDK loader.
Actual native stdio acceptance covers cache-miss fallback, shared concurrent
first use and a live local probe. HTTP preparation loads the installed SDK and
transport feature flags; no HTTP request was made.

The canonical native pytest suite and pinned Ruff were unavailable in the local
interpreter; no dependencies were fetched. Native acceptance is scoped standard-
library testing plus actual SDK/stdio execution. See [verification](verification.md)
for companion, export and release checks.

This companion kit does not rebuild or modify the owner's Hermes.app or profile.
The [v0.9.0 Desktop SSH bounds](release-notes-v0.9.0.md) remain included unchanged.
Memory-aware helper admission, the separate config-loader footprint, update
helpers and whole-gateway idle memory remain open standing-goal items.
