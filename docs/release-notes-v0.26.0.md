# Hermes Legion v0.26.0 — Local startup leaves saved remotes on demand

## What you will notice

Starting Desktop with the local gateway selected no longer initializes unused
saved SSH, remote URL or cloud connections merely to build the agent roster or
run Bot Relay. Saved connections, cached agent rows and credential-free SSH
seed routes remain available.

Selecting a remote gateway, pressing **Test**, updating it or delivering an
actual queued cross-gateway message can still connect it. Local and remote
backends remain supported. Already opened remote work keeps its existing
connection lifecycle; changing the foreground route does not kill that work.

No setting, dependency, pre-started pool or model request is added. Apply the
source kit and rebuild Desktop to adopt it. The daily Mac app was not changed
or launched, and no other machine was contacted.

## Behavior and limits

Passive enumeration borrows only an already-settled, still-owned backend
descriptor with the correct registry identity. SSH inventory uses its existing
transport without opening or closing it. A result that outlives its source,
owned promise or borrowed SSH session is discarded before roster publication.

Remote plugin routes carry a `connectOnDemand` snapshot hint when no current
descriptor is ready. Bot Relay skips passive roster reads, outbox polls and
socket pins for those routes. Its complete route inventory remains available
for delivering actual claimed work, so one local sender can still address a
cold remote. Fresh route snapshots restore participation after explicit use.
Cold roster contributions are removed locally; a temporarily empty inventory
still preserves the existing last-good cache behavior.

This hint is not an atomic transport lease. An already-ready remote can close
after a snapshot, and its existing lifecycle may reconnect it. This release
does not promise that switching to Local disconnects all previously opened
remote work or impose a whole-app process/RAM cap.

## Verification

Seven canonical Electron files pass 155 cases; three official UI-project files
pass 104, including 50 relay lifecycle cases. Full Electron and UI type checks
and scoped ESLint pass. Six cold-route lifecycle cases fail with the original
relay and pass after the fix. An additional control caught and prevented a
transient-empty-inventory cache regression during implementation.

An isolated fixture executes the actual main-process IPC handlers through
typed boundary doubles: 43 cases cover passive cold/cached/pending/failed
sources, current registry/legacy ownership, source retarget/removal, promise
and borrowed-session replacement, and preserved explicit selection/Test.
The SSH publication race was reproduced before adding its post-await fence;
a failed install-id read still retains valid profile-list success. These
controls execute no SSH process or model request.

Final native cold-launch evidence is recorded in the
[verification report](verification.md). Resource readings describe that bounded
isolated case, not ordinary installed-app RAM or a before/after memory saving.
The earlier native failure stopped before its first SSH execution and is not
an equivalent-work RAM baseline.

The separate Config/Bots/Chat Computer Use walkthrough and before/after screen
captures remain unfinished: the native window service returned
`cgWindowNotFound` for the exact isolated app path. Loaded renderer and healthy
local backend observations do not certify visual usability. No actual remote
host, installed daily-app adoption or other-OS acceptance is claimed.

Ten native paths change: six existing upstream files join the 1,056-target kit,
and four prior targets change. All 1,046 unrelated prior rows, bytes and patch
sections remain exact, including the SSH transport/helper protections. Patch
roundtrip, installed hashes, companion tests, tracked-only release checks,
secret scans, final advisor review and preservation/cleanup gate driver handoff.
The lead owns Linux sync and push; this work grants no first-remote-connection
approval.
