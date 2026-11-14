# Desktop SSH resource limits (v0.9.0)

Desktop now shares compatible SSH transports across profiles and queues startup
checks. The [release notes](release-notes-v0.9.0.md) describe the memory/latency
tradeoff and consolidate v0.8.46–.73.

## Ownership and admission

A process-lifetime namespace binds each socket to the Electron main process that
owns its holder registry. Profiles in that process share the same master when
host, user, port, key path and effective SSH configuration agree. Separate app
processes retain separate close ownership. Profile-specific backend ownership,
managed-update gates, host-key checks and authentication settings remain intact.

Only explicit establishment may create a master. Mux payload and terminal clients
use `ControlMaster=no` and `ProxyCommand=false`; losing the socket cannot silently
open another connection. OpenSSH otherwise permits normal connection fallback
when a mux socket is unavailable. [OpenSSH configuration reference](https://man.openbsd.org/ssh_config).

One programmatic command per host may execute at a time, including platform
probes, mux verification and no-mux reachability checks. At most 256 more requests
wait in the host queue; excess requests receive a busy error. Closing a connection
cancels its queued/active work. Aborted establishment flights are replaced behind
the old teardown barrier. Failures share a one-to-30-second exponential cooldown;
a usable backend publication resets it. This adds no automatic retry loop.

POSIX execution also acquires a remote kernel lock **before starting Python**.
The inherited descriptor reserves the remote home's single helper slot through
actual cleanup, even after the local client has disappeared. Other application
processes/identities therefore cannot overlap the guarded command by reconnecting.
GNU `flock` or Darwin `lockf` descriptor mode is required; one empty lock file is
kept and reused, without PID leases or lockfile deletion races. See the
[GNU descriptor example](https://raw.githubusercontent.com/util-linux/util-linux/master/sys-utils/flock.1.adoc)
and [Darwin descriptor implementation](https://raw.githubusercontent.com/apple-oss-distributions/shell_cmds/main/lockf/lockf.c).

A stdlib-only Python guard forwards a length-framed stdin payload, then treats the
open session input as a lease. The child receives only its payload followed by
EOF. Session loss, signals and deadlines stop the owned group with TERM/KILL and
reap the direct child. The unreaped child anchors its PID/group until cleanup;
normal completion also removes same-group descendants retaining output pipes.
Signal handlers use plain flags instead of taking thread locks.

Managed detached serves retain their own ownership/idle lifecycle. Their launcher
now uses stdlib `setsid` plus HUP-ignore and exec, including on Darwin: `nohup`
alone would leave the serve inside the disposable helper group. The single-command
budget leaves room for the known marker judge/detacher/serve startup chain within
four Python roles. This is admission for Desktop's known entrypoints, **not an
OS-wide process quota** for arbitrary child programs, agent workers or MCP servers.
Windows no-mux admission/cancellation is retained; POSIX group-lifetime acceptance
does not establish equivalent Windows remote cleanup.

## Measured Mac check burst

Four real native `hermes serve --help` requests used the original and patched
production `SshConnection` executors over local session-pipe mocks. No SSH remote,
installed app, provider or model was used. The native interpreter was Hermes PM
Python 3.14.9; the lifetime guard used Apple's Python 3.9.6. Synthetic homes and a
Python audit adapter fenced writes/SQLite to the trial, denied external network
and child-process operations, and passed nine negative controls. That adapter is
not a complete OS sandbox.

| Same four requests | Original executor | Patched executor |
| --- | ---: | ---: |
| Peak summed helper RSS | 340.5 MiB | 100.7 MiB |
| Wall time | 1.192 s | 3.031 s |
| Peak sampled Python count | 4 | 2 |
| Output agreement | identical | identical |
| Surviving test runtime | 0 | 0 |

Peak summed RSS fell **70.4%** in this one paired check burst. Four native helpers
became one native helper plus one lightweight guard at a time. Queueing increases
completion time for concurrent checks. Sampling targeted 15 ms; RSS includes
shared pages, and finite samples are not a continuous hard memory quota. These
numbers do not measure actual SSH latency, gateway idle memory, Linux, Windows,
MCP usage, model tokens or a rebuilt running Hermes.app.

## Validation boundaries

Meaningful initial red: seven behavior failures with one stdin-preservation
control passing. Advisor review added four further failing cases before fixes:
aborted-flight replacement, process namespace, probe admission and marker-gated
detached-serve survival. The current focused cases additionally exercise shared
holder close, cooldown, queue cancellation, invalid/truncated frames, blocked
stdin, TERM-resistant helper/child cleanup, retained output pipes and remote
kernel admission across independent local sessions.

Real OpenSSH was also tested with a fresh config, missing private mux socket and
loopback listener: zero TCP connections and no configured-proxy sentinel. No
other-machine SSH or owner SSH configuration was used.

The broader native selection has a pre-existing Mac installer-wrapper ownership
failure reproduced against the exact upstream source/test. That production
predicate was not changed. Its case and a deep-HOME test requiring writes outside
the allowed task root were excluded from the passing scoped run; another skip is
platform-defined. This release does not claim a complete native suite pass.

The exported cumulative patch is checked through reverse/base/reapplication and
all 1,013 before/after target hashes. All unrelated prior target bytes and patch
sections remain exact. Strict whole-patch whitespace reports the same 13 inherited
diagnostics before/after; the ten-path P0 delta and repository diff are clean.
See [verification](verification.md) for final release gates.
