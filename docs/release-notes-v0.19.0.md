# v0.19.0 — Gateway memory at the command line

## What you will notice

Run `hermes gateway memory` to read one JSON memory snapshot from the gateway's
existing private local control channel. You no longer need a Python snippet to
inspect its process, cache and SQLite counters. On macOS, current RSS now has an
on-demand fallback where the existing snapshot previously returned `null`.

The command adds no background monitor, model request, retry or lifecycle action.
Normal CLI bootstrap/recovery remains native. It does not trim memory or evict
work. This release supplies a measurement tool, **not a RAM-saving result**.

Use the serving gateway's launch profile. Targeting follows the existing
selected-home transport without searching other profiles. Check the returned
PID; a shared gateway's RSS covers the whole process, including every profile it
serves. Unknown measurements remain `null`, and current RSS is not peak RSS.
See [usage, exit codes and deeper diagnostics](runtime-memory-diagnostics.md).

## Native Mac evidence

One isolated native control-server pair used the same managed Python runtime,
configuration bytes, actual CLI entry point and private Unix socket. The baseline
server loaded the exact pre-change diagnostic module; both clients used the new
command so a valid unknown-RSS response also exercised exit 0.

| Observation | Previous diagnostic | Current diagnostic |
| --- | --- | --- |
| First reported current RSS | `null` | 35,328 KiB |
| Second reported current RSS | `null` | 35,344 KiB |
| Server RSS before any query | 32.4375 MiB | 32.265625 MiB |
| Server RSS after second query | 33.203125 MiB | 34.53125 MiB |
| First complete CLI invocation | 695.198 ms | 699.500 ms |
| Second complete CLI invocation | 678.870 ms | 689.429 ms |

Reported RSS agreed with the outside observer within the fixture's 2 MiB
tolerance. The answering PID matched the server, anonymous RSS remained unknown,
allocation tracing was absent, SQLite high-water counters were not reset, and
configuration bytes remained exact. psutil was absent before the first query
and loaded only by the new server's fallback. Importing it has a memory cost;
the end-to-end timings include ordinary CLI startup and do not isolate import
latency or establish a speed change.

The pair sampled at 20 ms from an outside observer, with at most two native
children plus that observer, 130.484375 MiB peak summed child RSS and zero
surviving children after shutdown. Summed RSS includes shared pages; brief peaks
can be missed. This is native CLI/control/diagnostic evidence, not a full gateway
startup, active adapter, installed-app, production workload or other-platform
acceptance test. No other machine or model endpoint was contacted.

## Compatibility and checks

The fallback runs only when the existing RSS value is unknown; existing values,
including zero, win. Expected missing-dependency, process-access and OS failures
leave RSS unknown. Memory pressure admission and trimming retain their existing
implementation. The CLI queries once with the existing five-second timeout:
valid snapshot exits 0, unavailable/malformed observation exits 1 with empty
stdout, and invalid arguments exit 2. "Unavailable" does not mean "stopped".

Ten native unittest cases cover parsing/dispatch, selected-home scope, one-query
behavior, malformed values, unknown/zero RSS, fresh current samples, fallback
failures and forbidden trim/GC/database effects. Before implementation, the
fallback assertion failed and the native parser rejected the new command.
Native CLI process exits 0/1/2 and actual socket shutdown were checked separately.
The canonical native pytest/Ruff environment was unavailable; no full native
suite or lint pass is claimed.

The cumulative kit now pins 1,038 targets. All 1,029 unrelated prior target
hashes and patch sections, including Desktop P0 fan-out protection, remain exact.
The source round-trip, companion suite, disposable release inventory and secret
scan results are recorded in [verification](verification.md). Existing daily
apps, profiles, models, owner data, ESTOPs, pauses and timers were not changed.
