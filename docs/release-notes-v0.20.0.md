# v0.20.0 — Load an unused local dashboard on demand

## What you will notice

An ordinary messaging gateway can now leave its unused local dashboard cold.
Set `gateway.dashboard_warmup` to `false`: the first HTTP/dashboard request
loads it through the existing lazy mount. You trade a slower first dashboard
request for less memory while it remains unused. The default stays `true`.

Back up the selected gateway launch profile and record the old value before:

```sh
hermes config set gateway.dashboard_warmup false
hermes config get gateway.dashboard_warmup --json
```

Apply the complete source patch and adopt the configuration through the
supported [idle update lifecycle](idle-updates.md). Setting the key does not
restart the gateway. Use `hermes -p NAME ...` for a named launch profile; a shared
gateway uses its launch configuration, not each served profile's turn context.
Restore the old value with `config set`; if originally absent, remove only this
key with `hermes config unset gateway.dashboard_warmup`.

Missing or invalid values preserve warmup. The established parser recognizes
boolean tokens, including `false`, `off` and `0`. Native key-presence precedence
is retained: a legacy top-level spelling wins over the nested spelling.
Models, providers, credential pools, fallbacks and unrelated settings retain
their values. No new environment variable, mode, dependency or monitor is added.

Authentication is unchanged. A listener that needs dashboard auth providers
still preloads them; an already-loaded dashboard stays loaded. The flag only
skips optional background scheduling. It does not unload the dashboard after
use or change native session WebSocket routing. Client-owned idle-exit gateways
already skip this warmup. The existing three-key on-demand preset is unchanged;
this setting is a separate opt-in.

## Native Mac evidence

Four fresh lifetimes in ABBA order ran the actual canonical `start_gateway`
bootstrap: profile ownership, session authority, control socket, local API,
runner, cron/housekeeping, READY, and native shutdown. No startup component was
mocked. Each process used the same managed Python and synthetic no-adapter
profile; native CLI configuration ran in a separate completed process before
boot. Initial backups were identical, with only this effective boolean changed.
Turn warmup was disabled and no MCP servers were configured on both sides.

The idle point was three seconds after READY, with default dashboard warmup
explicitly awaited first. The opt-out arm kept `hermes_cli.web_server` unloaded
until its first real local request; neither arm loaded the legacy TUI server.

| Observation | Default warmup | On demand |
| --- | --- | --- |
| Idle RSS, run 1 | 213.578125 MiB | 183.859375 MiB |
| Idle RSS, run 2 | 213.890625 MiB | 183.703125 MiB |
| Median idle RSS | 213.734375 MiB | 183.781250 MiB |
| Median first dashboard health request | 16.753 ms | 473.287 ms |
| Median second request | 2.203 ms | 1.117 ms |
| Median sampled lifetime peak | 226.695313 MiB | 226.679688 MiB |

Median idle RSS fell **29.953125 MiB (14.014%)**, passing the predeclared
5% **and** 10 MiB gate. Peak memory was essentially unchanged once the dashboard
loaded. First-use import cost is deferred; this small series does not establish
a second-request speed improvement or a general production saving.

Both real `/api/health` requests returned 200 with identical health data. Route
signatures matched across all four processes; a protected route returned 401
without credentials every time. The mounted app retained its native authority,
runner binding and withheld session token. Configuration bytes stayed exact
during each lifetime; all processes and their listeners stopped.

An outside observer sampled recursive RSS every 20 ms, including all native
descendants and excluding itself from reported totals. It observed one native
process throughout each case; total extra memory remained below 4 GiB. Shared
pages, allocator state and missed brief peaks limit interpretation. This proves
one synthetic canonical local startup/dashboard flow, not installed-app UX,
messaging adapters, live models, public-auth providers or other platforms.

## Checks and compatibility

Eight native unittest cases cover scheduling, conservative config parsing,
serialization, actual CLI-to-runtime loader preservation, first-request mount,
singleflight, auth-required preload selection and close-during-lifespan cleanup.
The auth selection test uses the real listener with a mocked mount; it is not a
public-auth-provider integration test. Before implementation, the explicit-false
scheduling regression failed while the default control passed. A separate
integration regression caught the initially omitted native config-loader bridge
and passes with that bridge included. Existing native tests were not rewritten.

The cumulative kit pins 1,042 targets. All 1,036 unrelated prior target hashes
and patch sections, including P0 Desktop fan-out protection, remain exact.
No new preset or defaults change is bundled beyond registering the opt-in key
with its backward-compatible `true` default. See [verification](verification.md)
for release checks and limits. The selected runtime lacks pytest/Ruff; no full
native suite or lint pass is claimed. Existing Uvicorn/websockets deprecation
warnings remain visible in the standalone native test output.
