# Hermes Legion v0.17.0 — release idle MCP processes

## What you will notice

A profile can now give its restart-safe stdio MCP servers one default idle
timeout. Pair it with cached lazy startup to keep unused servers stopped and
release their processes after use:

```yaml
mcp:
  memory_saving: true
  idle_timeout_seconds: 5
```

The new idle default is **off (`0.0`)**. Existing profiles keep their behavior.
`memory_saving` alone still only defers startup. The idle setting also works
independently, after the next discovery/startup; it does not rewrite server
definitions on disk. New or expired schema caches still need live discovery.

Set per-server `idle_timeout_seconds: 0` for stateful servers that must keep
browser or session state. Any explicit idle key at the top level or inside
`lifecycle:` prevents inheritance, including zero, null and invalid values.
Their existing native interpretation remains: top-level null can still fall
through to a nested timeout. HTTP and event-enabled servers receive no inherited
timeout. Portable stdio entries use the same profile policy.

Global opt-in cannot determine whether restarting a server is safe. Retirement
discards server memory and adds connection latency to the next call. Active
RPCs retain the existing lifecycle lock; tools remain registered while dormant.

## Measured on this Mac

The same native Hermes loader, registry and MCP SDK use a local stdio echo peer,
with identical initial configuration bytes and matching seeded schema caches.
The baseline uses the previous loader, which ignores the new global idle key;
the patched loader supplies the five-second default. No model request, network
connection or application launch is part of this case.

| Same native MCP component case | Before | After |
| --- | ---: | ---: |
| Summed RSS after 5.5 seconds idle | 184.813 MiB | 139.219 MiB |
| Child processes at that checkpoint, including supervisor | 2 | 0 |
| Whole-case sampled peak summed RSS | 184.875 MiB | 185.094 MiB |
| Maximum sampled runtime processes | 3 | 3 |
| Next echo latency | 2.62 ms | 109.13 ms |
| Six-second RPC completes past five-second idle limit | yes | yes |
| Surviving test children after shutdown | 0 | 0 |

Idle summed RSS fell **24.7%** in this one pair. The parent keeps the loaded SDK;
whole-case peak is essentially unchanged. Patched peer and supervisor were both
gone 70 ms after the observed five-second deadline. The next echo came from a
fresh peer, with its counter reset; a subsequent six-second RPC completed on
that peer before retirement resumed. Schemas and configuration bytes were
preserved. The counter reset demonstrates the state-loss tradeoff.

Recursive ancestry samples target 20 ms and include the native parent, peer
and death supervisor. One outer orchestration process is excluded; the known
overall topology stays within four processes and well below 4 GiB. Sampling
allocations affect parent RSS, summed RSS counts shared pages, and brief peaks
may be missed. This is one component pair, not a statistical benchmark or a
whole-gateway idle result. Private Python audit checks deny network operations,
unapproved subprocesses and owner-path access; five negative controls pass.
They are not complete OS containment.

## Validation and adoption

Seven new unittest methods cover inheritance, finite parsing, malformed values
and overflow, explicit override presence, HTTP/events, portable definitions and
profile isolation. Twelve old-code failing subcases prove the missing behavior.
The existing loader fixture checks that config bytes stay unchanged; the native
pair also checks byte preservation. All **25 native MCP tests** pass after export.
The existing config parser set/get path also proves default and configured
readback while preserving unrelated synthetic model, provider, credential-pool,
fallback and server settings.

The companion suite passes **131 tests with two Linux-only skips**. The 1,030
target patch passes actual reverse/base/reapply hash checks and strict installed
compatibility; all 1,025 unrelated target rows and patch sections stay exact,
including P0 SSH protection. Canonical native pytest and pinned Ruff are
unavailable in the selected runtime; neither was downloaded. Full native suite,
Linux/Windows execution, physical memory pressure, whole-gateway RAM and daily
app adoption remain unverified. Apply the source patch to adopt this feature;
the owner's installed app, profiles and controls were untouched.
