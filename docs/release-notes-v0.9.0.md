# Hermes Legion v0.9.0 — bounded Desktop SSH checks

## What you will notice

Desktop profiles using the same SSH target and authentication settings share a
transport instead of opening a master for every profile. A burst of startup or
reconnect checks queues rather than launching every heavy Python helper at once.
One-shot helpers start on demand and exit after their command; no idle helper
pool is introduced. Failure cooldown grows from one second to a 30-second cap,
resetting after a usable backend is published.

On one Mac, four concurrent real `hermes serve --help` requests through local
session-pipe mocks used a peak summed RSS of **340.5 → 100.7 MiB (70.4% lower)**.
The same outputs completed in **1.192 → 3.031 seconds**: queueing traded startup
latency for lower peak memory. Before: four native helpers. After: one native helper plus one lightweight
lifetime guard. Helpers and probes share a one-command queue; the remote kernel
slot remains held until cleanup completes. Both runs
ended with zero test runtime processes. These are sampled results for one paired
check burst, not gateway-idle, production Linux, MCP or whole-app measurements.

When a mux disappears, check requests fail instead of making an independent SSH
connection. Closing a connection cancels its queued and active checks. POSIX
session input acts as a lease; EOF, signals and command timeouts stop and reap
the owned helper process group. Remote kernel slots remain held until cleanup
finishes, including when the local client has already closed.

See [implementation and validation](desktop-ssh-resources.md) for the exact
ownership, queue, platform and process-count boundaries. This is a source kit;
it does not ship or install a rebuilt Hermes.app. The broader config/Bots/Chat
walkthrough, MCP/gateway idle-memory work and Windows remote-helper lifetime
acceptance remain open. No owner configuration or other-machine runtime was
changed for this release.

## Consolidated changes from v0.8.46 through v0.8.73

The following summarizes earlier releases in four user-facing groups. Historical
component measurements are labelled as historical; they were not rerun or added
to the new Desktop SSH benchmark.

### Safer disk use and backups

When a report cannot be archived safely, Hermes keeps its original and can move
on to another eligible report. Reports that become active while an archive is
being published are retained. Snapshot compaction refuses changed or linked
backup paths instead of following them to another location; changing a home
alias partway through a command cannot redirect that command into a different
home. These changes protect work when cleanup encounters an unusual filesystem
or activity change. They do not turn on stopped retention timers.

Web extraction can still return its current result when there is too little
observed space to save optional full text or its index. Prior cache files are
retained when a write is refused. If full text could not be saved for paging,
the response says so instead of presenting a usable saved path. Archive writes
also recheck space as encoded data is written, including archive overhead.

These are best-effort reserve checks, not a disk quota. Other applications can
consume space after a check. No production cleanup or reclaimed-byte total is
claimed. A refused optional write can mean another fetch later.

Included versions: v0.8.49, .52, .62, .63, .68, .70, .71 and .72.
Evidence: [storage and backups](storage-and-backups.md).

### Less temporary work when finding an older conversation

Finding a session by ID, selecting a conversation to resume, checking a
compression parent and checking a Gateway continuation no longer load large
prompt or tool fields that those checks do not use. Loading the transcript
still reads the context it needs. The TUI also retains at most 128 directory
labels while keeping its existing five-second label freshness.

Preparing a vision cache key reads the prepared image as a stream, avoiding a
second whole-file copy. Existing cache keys remain the same.

Native Mac component fixtures measured lower Python allocation and shorter
lookup times on deliberately large synthetic sessions. For example, exact-ID
lookup's median traced peak changed from 3,824,400 to 9,944 bytes. This is a
single read path's historical result, not a whole-app RAM or response-time
measurement. No model-token or billing reduction is claimed.

Included versions: v0.8.53, .54, .55, .58, .64, .67 and .73.
Evidence: [session reads](session-metadata-reads.md),
[TUI labels](chat-rendering-surfaces.md) and
[vision keys](vision-cache-routes.md).

### More reliable recall, cache discovery and goal waits

On a case-insensitive Mac filesystem, a recalled link keeps its original named
profile even after you switch profiles. That prevents a colliding session ID
from opening the other profile's conversation. A session with an unusable start
time can still be found or paged where its content and existing date rules allow.

Malformed cache timestamps are treated as ordinary cache misses rather than
blocking an otherwise healthy web search. A bad MCP expiry value cannot prevent
later healthy lazy servers from registering. Mixed-name filters use the same
name conversion for registration and cache identity.

Goal-judge memo keys retain timestamps that are part of the work evidence, so a
changed timestamp cannot accidentally reuse a stale verdict. Changing only the
generated clock can still reuse an otherwise identical verdict. Oversized or
boolean wait targets no longer select an invalid PID/time or interrupt valid
fallback parsing. These repairs do not establish a live Captain `done` verdict.

Compressed-resume acceptance now reaches its retained-history and receipt
assertions using a repaired native test fixture. That version is verification
coverage, not an additional end-user feature or proof of semantic memory.

Included versions: v0.8.50, .51, .56, .57, .59, .60, .61, .66 and .69.
Evidence: [recall](session-recall.md),
[search cache](search-cache-memory.md),
[MCP discovery](mcp-schema-publication.md),
[judge memo](goal-judge-memo.md),
[goal waits](goal-result-waits.md) and
[resume acceptance](session-metadata-reads.md).

### Clearer setup and doctor checks

Doctor accepts an explicit patch manifest, so a stable v0.22.5 checkout can be
checked against the stable kit rather than the historical v0.22.2 default.
Wrong revisions and changed files still fail; an offline-ready result does not
mean a running app has adopted the patch.

The Mac install/update guide resolves the dependency interpreter selected by
native Hermes PM instead of assuming an in-tree virtual environment. Synthetic
old-to-new-to-old readback preserved the same settings, profile and search state.
The release verifier avoids executing a configured Git filesystem-monitor hook
during its status check. The planner reports an invalid oversized timestamp
through its normal generic refusal rather than a traceback.

Included versions: v0.8.46, .47, .48 and .65.
Evidence: [offline setup and doctor](offline-setup-tools.md),
[Mac install/update](macos-install-update.md) and
[verification](verification.md).

Versions v0.8.74–.76 are recorded separately in the existing verification and
cache documentation. Source application, a rebuilt running app and existing
session adoption remain distinct acceptance steps.
