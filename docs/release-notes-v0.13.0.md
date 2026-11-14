# Hermes Legion v0.13.0 — wait for memory before Desktop checks

## What you will notice

The Desktop source patch now delays POSIX SSH helper work when the execution
host reports less than **512 MiB available memory**, or memory cannot be observed.
Work starts once the observation recovers. Waiting uses the existing command
budget; expiry says the helper did not start because it was waiting for memory.
It does not label that outcome as a broken SSH connection or retry it silently.
The source patch must be applied and Desktop rebuilt before an installed app uses it.

The v0.9.0 fan-out protections remain: one programmatic command per host, one
remote-home kernel helper slot, compatible shared transports, reconnect backoff
and lease-driven cleanup. No new pool, setting, dependency or pre-started worker
is introduced. Closing a queued connection prevents a later helper launch.

## Measured on this Mac

One matched native `hermes serve --help` case ran through production executors
with local session-pipe mocks. A second, real native CLI-import fixture stayed
resident for 1.5 seconds. Only the OS observation was modeled: low while that
fixture existed, healthy after it exited. The old executor overlapped both; the
new executor waited. A separate run used the real Darwin observer successfully.
No SSH connection, app launch, model or other machine was used.

| Same modeled-pressure case | Before | After |
| --- | ---: | ---: |
| Peak summed descendant RSS | 160.3 MiB | 100.8 MiB |
| Request completion | 0.797 s | 2.233 s |
| Peak sampled process count | 3 | 3 |
| Native output | identical | identical |
| Surviving runtime | 0 | 0 |

Peak RSS fell **37.1%** in this single paired case. This measures avoided overlap
under modeled pressure, not actual low-memory stress, a general speedup, update
helper coverage or gateway idle memory. Samples target 15 ms and include shared
RSS pages; brief observer children can fall between samples. Test logic also
bounds the known fixture/guard/observer/helper process topology to four processes
and checks summed sampled RSS below 4 GiB. No physical disk-saving claim is made.

## Policy and limits

Linux uses explicit `MemAvailable` from `/proc/meminfo`; missing, malformed and
unknown observations wait. Darwin runs a bounded, reaped `vm_stat` probe and
estimates availability from the reported page size times free plus inactive
pages. This is an estimate, not Linux-equivalent availability or guaranteed
reclaimable memory. The 512 MiB threshold is an observation, **not a reservation**;
memory may change after observation. No pressure allocations were used.

Waiting intentionally holds the existing slot, so later checks wait behind it.
Each Darwin probe has at most 200 ms of execution budget, bounded further by the
remaining command deadline. EOF/cancellation and the deadline are checked after
the probe and before helper launch. The guard reaps observer children without
confusing their exits with the helper's completion. A first guard-owned status
header is stripped once; child output or exit 125 cannot impersonate admission
expiry. Existing helper stdin, output and lifetime handling remain intact.

This item completes POSIX Desktop command memory admission. Configurable
concurrency, broader update-helper admission, safe MCP scale-to-zero, minimal
idle gateway memory and owner-app adoption remain open. Windows remote memory
observation and Linux execution were not tested. See [resource policy](desktop-ssh-resources.md)
and [verification](verification.md) for the exact acceptance scope.
