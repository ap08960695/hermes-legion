# Hermes Legion v0.27.0 — Host facts wait until needed

## What you will notice

Profiles with `agent.gateway_startup_warmup_timeout: 0` now leave the host
Python toolchain probe idle during gateway startup. Negative timeout values
also defer it. The first local prompt still receives the same cached host
facts through the existing bounded probe; the first turn may take longer.
This extends the [on-demand preset](on-demand-gateway.md) without another setting.

Positive timeouts retain asynchronous host probing, now after PID admission
and logging setup. Refused profile/host/duplicate/reservation/PID starts do not
launch this probe. Later startup failures can still occur after it starts.
`agent.environment_probe: false`, remote-terminal omission, the existing
single-worker cache and failure containment retain their behavior.

Apply the source kit and use the profile's next normal gateway launch to adopt
it. No running worker is stopped and no owner configuration is changed. There
is no new dependency, pre-started pool, model request or retry policy.

## Native Mac evidence and tradeoff

Four fresh whole-canonical-gateway cases ran before/after/after/before with
the same synthetic profile, local context, managed Python and restricted
version/pip commands. Gateway READY, authority, control server and API were
real. Each ran two native turns; only inference returned a synthetic response.

| Median of two cases per arm | Before | Deferred |
| --- | ---: | ---: |
| Toolchain subprocesses before first use | 5 | 0 |
| Cumulative toolchain subprocesses after two turns | 5 | 5 |
| Idle RSS before first use | 184.906 MiB | 184.852 MiB |
| Sampled whole-lifecycle peak RSS | 242.852 MiB | 255.281 MiB |
| Sampled maximum helper RSS | 24.492 MiB | 23.641 MiB |
| First-turn time through offline inference boundary | 861.61 ms | 1370.37 ms |
| Second-turn time through offline inference boundary | 10.84 ms | 11.07 ms |

**No RAM saving is established.** Idle RSS is essentially unchanged; deferring
probes moves their allocations into first-use work and this case's peak is
higher. The useful change is avoiding five unused startup commands. It is not
a whole-Hermes RAM cap, production latency improvement or minimum-idle proof.
Timing includes importing the agent class to install inference interception.

All four cases produced identical actual host-fact lines and static prompt
hashes; requests retained profile SOUL, workspace AGENTS and Thai text. The
second turn reused the completed probe. No provider or remote-host request
was made. Positive policy separately ran all five real checks and reused its
completed worker. Seven audit negatives and managed Python/pip stdout, status,
version and module-origin fidelity checks passed. These task-local audit guards
are not an OS security sandbox.

Sampling targeted 20 ms across the gateway and recursive children; no cohort
exceeded two workload processes, or three including the observer, and all owned
children stopped. RSS sums can count shared pages and miss brief transients.
This uses a synthetic profile without adapters/MCP; UI walkthrough, daily-app
adoption, real model calls, other platforms and other machines remain untested.

## Offline regression

Eight native unittest contracts cover disabled/positive/error policy, six
admission outcomes, startup ordering, deterministic nonempty first-turn facts,
cache/prefix preservation and remote/plugin-remote omission. The original
implementation fails ten assertions/subtests; the candidate passes. Eight
fresh-process bridge cases preserve default/positive/zero/negative/environment,
invalid/null fallback, explicit-disable and config precedence behavior.

The native fixture is packaged as
`tests/gateway/test_environment_probe_startup_unittest.py`. With the upstream
test environment, run:

```sh
scripts/run_tests.sh -j 1 tests/gateway/test_environment_probe_startup_unittest.py
```

Mac acceptance executed the same contracts with stdlib unittest in the existing
managed runtime. Pytest and pinned Ruff were absent; the canonical runner/full
native suite were not run. The kit's companion suite, tracked-only release
inventory, patch reversal/reapplication and installed hashes are separate checks.
