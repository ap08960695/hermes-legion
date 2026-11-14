# Hermes Legion v0.18.0 — opt in to lighter gateway startup

## What you will notice

The optional [on-demand gateway preset](on-demand-gateway.md) leaves turn machinery
cold until first use, starts cached stdio MCP servers only when needed, and limits
discovery to one server tree at a time. Existing Hermes controls do the work;
there is no new runtime mode or automatic change to your profiles.

Apply three reviewed keys with the native config commands, after backing up one
explicitly selected profile. Warmup adopts the setting on the next normal gateway
launch. Existing work is not interrupted. Unrelated model, routing, credentials,
fallback, delegation and lifecycle controls are preserved. No global MCP idle
timeout is included, so the preset does not opt stateful servers into retirement.

## Measured tradeoff

One native Mac initialized-runner pair used **178.234 → 144.000 MiB** idle before
the first turn: **19.2% less RSS**. Both had one native process and zero children.
First-turn initialization through an offline inference boundary took
**528.33 → 1165.85 ms**. Sampled lifecycle peak was **222.578 → 220.516 MiB**,
similar rather than evidence of a general peak saving.
First-use timing includes the class import needed for test inference interception;
it does not isolate production latency from harness overhead.

The real gateway turn path constructed its agent and assembled SOUL, workspace
context, Thai user text and identical canonical deferred tool definitions before
the synthetic model completion. Actual boot configuration overrode an ambient
warmup value; no warmup/resolver/agent-construction stub was used. Only inference
methods were replaced, so no provider/model request was needed. Config bytes
remained unchanged during the measured case, and no test children survived.

This is an initialized-runner component result, not full startup, a connected
gateway or installed-app adoption. One pair, 20 ms sampling, shared RSS pages,
sampling allocations, synthetic context and disabled environment probing limit
generalization. The first call pays deferred initialization. No runtime modules
are unloaded after use, and existing per-server policy still governs MCP lifetime.

## Verification and compatibility

Five executable native contracts cover application/readback and unrelated settings,
unselected profiles, MCP consumers, actual warmup behavior and first-turn assembly.
The pre-preset control fails the no-preload condition because normal warmup is
scheduled; this is existing behavior, not an old-code bug. The feature packages
existing controls with a tested application recipe.

The 1,030-target native patch and manifest remain byte-for-byte unchanged,
including P0 SSH protection. The companion adds a fragment, recipe and native
verification fixture; no runtime dependency or default changes. Full native
pytest/Ruff, Linux/Windows runtime, whole-gateway idle RAM and daily-app use remain
unverified. The owner's app, homes, data, ESTOP, pauses and timers were untouched;
acceptance never connected to another machine or ai.
