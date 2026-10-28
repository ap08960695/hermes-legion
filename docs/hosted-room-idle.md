# Hosted room standby scheduling

Canonical gateways previously started a hosted-room supervisor for every served
profile, including profiles with no Group Chats. Large idle fleets therefore
kept one polling thread per empty profile.

The ready gate now arms each runtime without creating a supervisor. Existing
producer wakeups (including direct runtime wakeups) start exactly one supervisor
immediately after readiness. A wake received during startup waits for the ready
gate. The existing Gateway watcher discovers persisted local, owned, non-disbanded
rooms at the native five-second fallback cadence, off the event loop. No new
poller, registry, model request or per-profile timer is added. The scan is single
flight even if its observer is cancelled; normal SQLite read latency can delay
fallback discovery, while normal producer wakeups do not wait for a scan.

A standby existence read never grants execution. Full native ownership, epoch,
member, admission, lease, receipt, unknown/no-replay and concurrency gates still
apply. Reads use the authority's existing handle with reopen disabled. Stop
disarms under the runtime lock, so late reads, producers and ready callbacks cannot
revive a stopped owner. Explicit start/restart for other consumers remains
supported. Supervisor and room threads inherit the owning ContextVars via the
existing context-thread helper. Prompts, cache prefixes and toolsets are untouched.

## Evidence and limits

The selected native regression suite passed 9 files / 102 cases with zero file
retries. It includes canonical private-socket routing, once-only finite admission,
startup recovery, foreign-owner fences, accepted-work stop behavior and concurrent
wake/cancelled-observer regressions. Installed Linux and macOS synthetic-home
acceptance each passed 6 controls, with network denied and zero inference. The
original macOS Gateway was not started for this acceptance. No original-user
conversation or task was submitted.

A matched isolated benchmark constructed 116 real canonical profile services and
ran the native ensure path at the existing one-second Gateway watcher cadence.
Empty-profile supervisors: 116 before / 0 after. PSS: about 235.25 / 162.34 MiB.
Across an approximately six-second idle observation, process CPU time was about
2.72 / 0.11 seconds. Preparation stayed about 23.5 / 23.7 seconds: this patch does
not make initial profile/store construction faster. These are component measurements,
not whole-Gateway RAM, provider usage, token/cache-hit or end-to-end task savings.
The updated Linux Gateway also showed zero hosted supervisor threads after a native
only-if-idle update. Existing quotas, models, effort ceilings and fallback policy
are unchanged. This release changes Python backend code; no Desktop bundle was
rebuilt.
