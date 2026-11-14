# Hermes Legion v0.15.0 — on-demand Desktop ticket helpers

## What you will notice

Desktop now starts at most one Python ticket helper at a time by default and
closes an unused helper after five seconds. Switching among several profiles
queues new helper admissions instead of keeping a process for every profile.
Nothing is pre-started. Every request still obtains its own fresh native ticket.

To adjust the tradeoff, edit the launch profile's `config.yaml` and restart
Desktop. Use a top-level `desktop:` block with exactly two-space indentation:

```yaml
desktop:
  gateway_ticket_helper_limit: 1       # integer 1–2; default 1
  gateway_ticket_helper_idle_ms: 5000  # integer 100–30000; default 5000
```

Missing, malformed and out-of-range settings use the defaults. These are
launch-only settings, without a new Settings control or Python config probe.
This source patch must be applied and Desktop rebuilt before an installed app
uses it. The owner's daily Hermes.app was not rebuilt or launched for acceptance.

## Measured on this Mac

The same three concurrent profile requests used production Desktop ticket code
and the actual native Python 3.14.9 ticket client against private synthetic
AF_UNIX control sockets. The controller ran in the measuring Node process; no
real gateway, worker, model, SSH connection or other machine was involved.
Both sides executed the identical native helper program. The primary paired
case used the default policy.

| Same three-profile case | Before | After |
| --- | ---: | ---: |
| Peak summed RSS sampled during requests, including Node caller | 134.328 MiB | 72.156 MiB |
| Maximum sampled processes, including Node caller | 4 | 2 |
| Helper processes after 5.5 seconds idle | 3 | 0 |
| Total RSS at that idle checkpoint, including Node caller | 138.969 MiB | 47.531 MiB |
| Three-request completion time | 67.64 ms | 163.94 ms |
| Initial ticket results | three fresh profile-bound grants | identical |
| Surviving test runtime after cleanup | 0 | 0 |

The sampled request-window peak fell **46.3%** in this one pair. Serialization
made the requests slower. A separate real case applied the parser's limit of two
and 100 ms idle timeout: two helpers could serve requests together, a third
waited for a slot, and no helper remained after 250 ms idle. Reviving a retired
helper still obtained a fresh grant. Original native owner, profile, protocol,
purpose, control-home and working-directory isolation cases pass.

Samples targeted 20 ms and sum RSS pages that can be shared; brief processes and
peaks may be missed. Each native run stayed within four runtime processes and
4 GiB. A private Python audit adapter fenced the measured helper's reads,
writes, subprocesses and sockets; six negative controls pass. This is not full
OS containment. The additional existing native integration tests use isolated
homes and the selected PM interpreter, with only their socket temp base relocated.

These are component measurements with synthetic control responses. They do not
measure an installed app, a full gateway's idle RAM, physical memory pressure,
Linux/Windows execution, MCP servers or model/token use. The measuring Node
caller remains alive at the idle checkpoint; only ticket helpers scale to zero.

## Admission and compatibility

Helper capacity is global within one Electron process. Starting and retiring
children count until actual process close, so killing a helper does not release
a slot early. Busy helpers are never evicted. Up to 256 admission requests wait
in FIFO order. Existing eligible bridges may multiplex their own profile's
requests while other admissions wait; sustained activity can make another
profile's admission expire. Each mint request has one monotonic ten-second
budget covering queue wait, retirement, spawn and ticket exchange. Overdue
responses are refused even if an overdue timer callback has not run yet.
Queue-full, admission expiry and runtime reset have separate errors; native
owner or credential rejection keeps the existing path. Reset cancels queued
work and prevents stale callbacks from starting helpers.

Exact interpreter, working directory, full environment and profile keys retain
isolation. No grants or completed results are cached or shared. The native
helper program and client, runtime lookup, detached gateway lifecycle and P0 SSH
policies remain unchanged. A fresh helper also has an idle timer before its first
request, so a deadline crossed during startup cannot leave it running unused.

The 256 limit covers waiting admissions, not requests or stdin buffering already
assigned to a live helper. The separate runtime-command lookup has its existing
30-second timeout and is outside this helper cap and mint budget. Other helper
entrypoints and Electron processes are outside this policy. Lower limits and
shorter idle periods can cause more cold starts and slower profile switching.
Memory-aware admission for this path, wider update-helper coverage, MCP idle
retirement and minimal whole-gateway RAM remain open.
