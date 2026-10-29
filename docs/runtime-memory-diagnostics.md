# On-demand Gateway memory diagnostics

Use this diagnostic when an idle Gateway retains more memory than expected. It
reports process memory and container counts without reading conversations,
formatting cached objects, opening session databases or calling a model. It does
not trim memory, evict agents, collect garbage, change quotas or select providers.
The normal status request remains unchanged.

## Read a small snapshot

After applying the complete patch and loading it through the documented
[idle update lifecycle](idle-updates.md), run this from the installed source using
its existing managed Python environment and the intended Gateway launch profile:

```python
import json
from gateway.control_socket import query_gateway_control
from hermes_constants import get_hermes_home

result = query_gateway_control(get_hermes_home(), "memory-stats", timeout=5)
if result is None:
    raise SystemExit("Gateway observation unavailable; do not restart or replay work")
print(json.dumps(result, indent=2))
```

This uses the existing private local control socket, not a network endpoint or a
new model tool. Inspect the answering PID against the serving Gateway before
attributing a result to a particular process. On unsupported hosts or while a
registry lock is busy, affected measurements remain null rather than becoming
zero. A missing observation does not establish an empty cache or an idle worker.

Available fields include RSS, anonymous RSS and thread count where supported;
agent, session-state and profile-config counts; tool/MCP container counts; and
native SessionDB registry generations and reference counts. Counts never include
profile names, session identifiers, schemas, prompt bodies or cached values.

Since v0.3.7, `bundled_locales` also reports `hits`, `misses`, `entries` and
`max_entries` from an already-loaded bundled-translation cache. If that cache has
not loaded, the field is null; observation does not initialize it. These are
static-file cache counters, not model prompt-cache hits or token savings. A miss
is a cache computation attempt and can include a failed read.

The cache keeps at most 32 verified source versions. File identity, size,
nanosecond modification/change timestamps and ownership/mode participate in its
key; changed or replaced bundles are re-read. Each caller receives an independent
dictionary while immutable strings can be reused. Profile overlays, plugin
modules and model context keep their existing isolation. Language/overlay resets
rebuild merged views without re-parsing an unchanged bundle. Read or validation
errors are not cached as successful parses.

Since v0.3.8, `plugin_code` reports the same four scalar fields for an already-loaded
compiled-source cache. Observation never initializes it or exposes paths, source
digests, code constants, globals or credentials. A miss is a compilation-cache
attempt, not a model request or a unit of token usage.

Eligible bundled directory imports can reuse immutable Python code objects while
executing each profile's module with its own globals. Native activation and
registration still run. The cache holds at most 128 source versions and excludes
source files larger than one MiB. Larger sources still load without shared
caching. Those are admission bounds, not a hard process
RAM limit. Source is read on every request: access failures remain failures, and
content changes produce a different cache key even when size/mtime are restored.
Previously loaded sibling modules keep their code until their own native reload.

The implementation uses Python's existing per-directory importer cache. Custom
root loaders and custom directory finders are preserved, and extension/sourceless
imports retain their native paths. Non-bundled profile plugins retain their native
import behavior and do not fill the shared code cache. No second disk cache or
new service is installed, and existing native bytecode files are left alone.

A first cold profile incurs source compilation work; the measured benefit is in
a persistent process serving many profiles. Do not assume a saving for every
short-lived single-profile process. Compare equal native configurations and
module/registration counts when measuring; lower RAM obtained by silently
omitting a plugin is not a successful optimization.

SQLite allocator measurements use symbols from Python's own loaded SQLite
extension. If symbols or tracking are unavailable, `sqlite.available` is false
and byte counts are null. The diagnostic never loads a different SQLite library
to manufacture a number and never resets the high-water mark. SQLite allocator
bytes exclude some process memory, so they cannot explain total RSS by themselves.

## Optional startup allocation tracing

Start with the small snapshot. For a deliberate deeper investigation, the
Gateway's native launch-profile configuration accepts:

```yaml
runtime:
  memory_profile_frames: 4
```

The default is `0` (disabled). Only integer values from 1 through 8 enable tracing
at Gateway initialization. Invalid values leave it disabled; an already-running
profiler is preserved. Use the native config writer to change only this field:

```sh
hermes config set runtime.memory_profile_frames 4
```

Preserve any original value. Load the setting only when the Gateway and its
background work are genuinely idle, using the supported lifecycle. This native
option also works with launchers that isolate Python from environment flags;
keep that isolation in place.

Tracing adds CPU and memory overhead. During the idle maintenance window, request
one allocation snapshot by adding `params={"allocations": True}` and a suitable
bounded timeout to the Python query above. The response contains aggregate
bytes/counts and at most 30 core-relative code locations. External or unrecognized
locations become `<python-or-extension>`. It contains no object values, full
filesystem paths or traceback arrays. It cannot attribute every external
allocation to a specific dependency.

An allocation request does not start tracing. Without an active profiler it
returns `allocations.available: false`. A timeout can occur while a snapshot is
still computing; preserve that operation and inspect its state instead of
immediately requesting another snapshot. Use this deliberately, not as a polling
loop or a live-work benchmark.

Restore the previous setting through the native config writer. If the field was
originally absent, remove just that field:

```sh
hermes config unset runtime.memory_profile_frames
```

Use the idle lifecycle again to return to an untraced process, then verify that an
allocation request reports unavailable. Keep goals, pauses, models, accounts and
the rest of the profile configuration unchanged. Compare normal untraced samples
at matched lifecycle stages; removing profiler overhead is not a memory-saving
fix. This feature supplies evidence for later repairs, not a claimed production
RAM, latency or token reduction.

## Persistent profile locks

Gateway holds one native lock descriptor for each reserved profile. Its small UTF-8 owner record now uses a 4 KiB I/O buffer rather than a filesystem-derived default for the reservation lifetime. The record is still flushed and fsynced before reservation succeeds. Lock inode identity, exclusion, private modes, partial-claim rollback, maintenance purpose, and native release rules are unchanged. No new knob, cache, cleanup loop or profile limit is introduced.

Sixteen native reservations previously retained about 2.15 MB of traced Python allocations; the bounded implementation retains about 0.13 MB in the Linux production interpreter. This is an allocation measurement, not a promised reduction of whole-process RAM. Current synthetic startup PSS measurements remain allocator-sensitive; do not convert buffer bytes into an asserted production RSS/PSS saving. Traced runs also include profiler overhead.

## Fresh-store deferred schema phase

A genuinely empty store already commits its declared tables as an atomic phase. Its later deferred index/trigger phase now also commits as one separate transaction, after native column reconciliation. A failure rolls back that deferred phase; the earlier declared tables remain committed and normal later reconciliation can recover. Existing and settled stores keep their ordinary checks, without a new mandatory writer transaction. All per-profile ownership, durability, schema inspection, cache behavior and later FTS/migration phases remain native.

This targets first-time database setup. Use fresh and settled measurements separately; do not equate fewer setup commits with faster model generation, lower token usage, better provider caching or a whole-process RAM saving. No new configuration or background maintenance is introduced.

## Plugin ledger cleanup callbacks

Plugin registration handles now reuse one cleanup callback within their owning
manager. Managers remain separate, with late method lookup, per-handle release,
persistent registration ownership and exception/finally cleanup unchanged.
No mutable plugin module or manifest state is merged across profiles.

A production-interpreter component fixture with sixteen native managers and
8,192 registration handles reduced retained Python allocations from 3,775,936 to
1,617,472 bytes. Callback function objects fell from 8,192 to sixteen. This is the
registration fixture, not a whole-Gateway RAM reduction percentage.
Four separate native Gateway startups with 116 fresh synthetic profiles in ABBA
order observed mean PSS 336,038,912 versus 333,786,624 bytes, with zero swap. This
small controlled-series difference does not establish original-workload RAM or
startup latency savings. No token, cache-hit or inference-speed gain is claimed.

Existing immutable plugin code reuse remains bounded at its original capacity.
A separate sixteen-profile diagnostic observed 49 code-cache misses throughout,
525 hits and no duplicated source code objects; increasing the cache cap was not
justified. All native profile isolation, lifecycle, models, quotas and gates remain.
