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
