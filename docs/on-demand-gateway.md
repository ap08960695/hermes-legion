# Optional on-demand gateway preset

This [native merge fragment](../examples/native/on-demand-gateway.fragment.json)
uses existing Hermes controls to defer unused startup work. It adds no runtime
mode or new default. Apply it only to an explicitly selected profile:

```yaml
agent:
  gateway_startup_warmup_timeout: 0
mcp:
  memory_saving: true
  discovery_concurrency: 1
```

The gateway skips its optional turn-machinery warmup at boot. Agent imports,
schema preparation and other first-use work then occur when needed. Cached
stdio MCP definitions use lazy startup, and discovery connects at most one
server tree at a time per discovery pass. Missing or stale MCP caches still
require live discovery. This is not an OS-wide process cap.

With the v0.27 source kit, a nonpositive warmup timeout also defers eager host
Python toolchain probing. The first local prompt retains its existing bounded
facts lookup and completed-result cache. Positive policy keeps asynchronous
probing after PID admission; later startup failures can still follow a probe.
[Whole-gateway comparison and first-use tradeoff](release-notes-v0.27.0.md):
five unused startup commands become zero, idle RSS is essentially unchanged,
and sampled peak RSS and first-turn time increase. No RAM saving is claimed.

The preset does not set an MCP idle timeout. Connected stateful servers keep
their existing lifecycle policy. Use the [separate idle opt-in](release-notes-v0.17.0.md)
only when their state may be discarded; per-server `idle_timeout_seconds: 0`
opts out. HTTP, events, explicit overrides, credentials and profile boundaries
retain their native behavior.

## Apply through native configuration commands

Choose the intended installed native launcher and one profile explicitly. Check
its config path before making changes. For a synthetic example profile:

```sh
: "${HERMES_BIN:?Select the supported native Hermes executable}"
"$HERMES_BIN" --profile legion-on-demand config path
"$HERMES_BIN" --profile legion-on-demand config get agent.gateway_startup_warmup_timeout --json
"$HERMES_BIN" --profile legion-on-demand config get mcp.memory_saving --json
"$HERMES_BIN" --profile legion-on-demand config get mcp.discovery_concurrency --json
```

Create that fresh profile through `hermes profile create` if appropriate, or
substitute the one existing profile you intend to change. Preserve one scoped,
recoverable backup of the selected config first. Record each key's prior value
and whether it was explicitly present; effective readback alone can show a
default. Do not publish a full config dump or replace a config with this fragment.

Then use the existing per-key writer:

```sh
"$HERMES_BIN" --profile legion-on-demand config set agent.gateway_startup_warmup_timeout 0
"$HERMES_BIN" --profile legion-on-demand config set mcp.memory_saving true
"$HERMES_BIN" --profile legion-on-demand config set mcp.discovery_concurrency 1
```

Repeat the three targeted `config get` commands to verify readback. If applying
the group fails, roll back only keys this attempt changed. Use `config set` with
each recorded previous value, or `config unset KEY` when it was originally absent.
Preserve unrelated concurrent edits; the backup is a recovery copy, not permission
to overwrite the whole current file.

Warmup is bridged at gateway process boot. These writes do not stop an active
warmup or unload an existing agent. Let the profile adopt the policy on its next
normal launch; do not interrupt active work or restart services for this recipe.
Other profiles are not modified. ESTOP, pauses, timers, routing, model selection,
credential pools, fallback policy and delegation limits are outside the preset.

## Native evidence

One Mac pair used the same initial synthetic config, context files and native
runtime. Existing parser commands changed only the three preset keys. A fresh
real `GatewayRunner` ran its actual start/await warmup methods on both sides.
An ambient warmup value of 777 was overridden by the native boot bridge: 20 in
the baseline fixture, 0 after applying the preset.

| Initialized runner case | Before | With preset |
| --- | ---: | ---: |
| RSS idle before first turn | 178.234 MiB | 144.000 MiB |
| Native runtime processes / children | 1 / 0 | 1 / 0 |
| First-turn time through an offline model boundary | 528.33 ms | 1165.85 ms |
| Sampled lifecycle peak RSS | 222.578 MiB | 220.516 MiB |

Idle RSS fell **19.2%** in this pair. The first turn paid the deferred cost.
That timing includes the class import needed to install inference interception
inside the first-use window; it does not isolate production latency from test overhead.
Peak is similar; this does not establish a repeatable peak reduction. The actual
gateway turn path constructed a real agent and assembled its request. Only the
inference methods returned a synthetic completion. Both requests contained the
profile SOUL, workspace AGENTS, Thai user text and the same canonical deferred
tool definitions. No provider request was made. This proves that fixture's first
assembly, not every provider, platform or failure path.

Scope is an initialized runner: full gateway startup, connected adapters and
the installed app were not exercised. Sampling targeted 20 ms across recursive
descendants and includes sampling allocations; summed RSS can count shared pages
and miss brief peaks. One outer orchestration process is excluded, with known
topology below four processes and 4 GiB. No test children survived shutdown.
Synthetic context and disabled environment probing limit generalization.

## Reproduce the offline contracts

Copy [the native unittest fixture](../verification/native_gateway_memory.py) into
a disposable patched Hermes checkout as `tests/gateway/test_legion_gateway_memory.py`,
and the fragment into `tests/gateway/fixtures/on-demand-gateway.json`. Use that
checkout's canonical runner:

```sh
scripts/run_tests.sh -j 1 tests/gateway/test_legion_gateway_memory.py
```

The five tests exercise native parser preservation, unselected-profile isolation,
MCP loader/discovery consumers, real warmup scheduling/deferral and actual first-turn
assembly with an offline inference boundary. Fixtures use temporary homes and no
service launch. Acceptance on this Mac used the same unittest fixture through
stdlib unittest in the existing PM runtime: pytest and pinned Ruff were absent;
the canonical runner would provision dependencies, so it was not run. No full
native-suite, installed-app, whole-gateway, model-usage or cross-platform claim.
