# Hermes Legion v0.14.0 — share repeated Desktop update checks

## What you will notice

When several Desktop surfaces ask for the same source-installation update status
at once, they now share one running check. They avoid launching a separate Python
interpreter and repeating launcher/bootstrap work for every request. Once the
check finishes, its result is discarded; a later request starts another check.
The native check's existing disk-cache policy is unchanged.

Distinct checks wait in order, with one source-check process active per Electron
process and at most 256 more distinct operations pending. Identical adjacent
ordinary requests join without consuming another pending slot. **Force checks
and channel changes always run independently**, in their FIFO turn. A read does
not join an earlier check across an intervening force, channel or different
request. This preserves explicit freshness and channel-selection ordering.

Each caller parses its own status object, including nested data, so updates to
one caller's presentation cannot change another caller's result. Execution and
JSON errors remain visible, release the slot and do not trigger an automatic
retry. An overloaded queue reports a busy error. No new setting, dependency,
worker, timer, process pool or saved-result cache is introduced.

This is a source patch. Apply it and rebuild Desktop before an installed app uses
it. The owner's daily Hermes.app was neither rebuilt nor launched for acceptance.

## Measured on this Mac

Two identical concurrent requests used the actual generated Hermes launcher and
native `hermes_cli.source_check` through the production Desktop executor. Both
sides used valid cached synthetic profiles, the same isolated source/runtime,
unchanged generated bootstrap/recovery program and existing PM Python 3.14.9.
A private audit prefix and isolated dependency path fenced acceptance; no API
request, SSH connection, app launch or other machine was involved.

| Same two-request cached case | Before | After |
| --- | ---: | ---: |
| Python interpreter launches | 2 | 1 |
| Peak summed descendant RSS | 134.875 MiB | 67.234 MiB |
| Peak sampled process count, including Git | 4 | 2 |
| Completion time | 1.241 s | 0.642 s |
| Caller status | identical | identical |
| Surviving test runtime | 0 | 0 |

Peak summed RSS fell **50.2%** in this one paired case. Profile config and cache
bytes were preserved. Sampling targeted 15 ms and includes shared RSS pages;
brief children can fall between samples. A single-request topology preflight and runtime PID/RSS checks bounded the
known native/Git case to four
processes and below 4 GiB. These are component measurements, not statistical,
whole-update, network/download/apply, gateway-idle or model-usage results.

## Scope and tradeoffs

The FIFO covers source checks across all installations in one Electron process;
install aliases cannot bypass it. Exact command, arguments, working directory
and environment snapshots determine whether adjacent ordinary requests can join.
Managed PM launchers and the older explicit-interpreter path retain their
existing resolution, validation, timeout and error behavior. Python still owns
channel config, cache identity and update decisions. Launcher recovery,
preservation, dependency selection, actual update/apply and P0 SSH limits stay
unchanged.

A slow active check delays other installations too. The existing six-minute
process timeout starts when that check executes; no queue-wait timeout or new
cancellation API is added. This is not an OS-wide helper quota: other Electron
processes and other helper entrypoints are outside this queue. Configurable
helper admission, wider update-helper coverage, MCP scale-to-zero, minimal idle
gateway RAM and installed-app adoption remain open. No Windows execution,
physical memory-pressure or general token-saving claim is made.
