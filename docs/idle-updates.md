# Idle-only Gateway update admission

An idle chat does not imply that its scripts have finished. Native shutdown can
terminate registered tool subprocesses, so an automatic reload must check
background work immediately before it requests a restart.

With this patch loaded by the serving Gateway, the existing control client offers
an opt-in strict request:

```python
from gateway.control_socket import pause_gateway_for_update
from hermes_constants import get_hermes_home

ack = pause_gateway_for_update(get_hermes_home(), only_if_idle=True, timeout=8)
if ack is None:
    print("Deferred: unavailable, unsupported, or ambiguous reply; do not replay.")
elif ack.get("pausing"):
    print("Idle-only restart accepted; verify the replacement process separately.")
else:
    print("Deferred:", ack.get("reason", "already stopping"))
```

Run this only as the authorized update owner after checking native ownership and
backups. It requests a lifecycle change. It is not a model tool or an inference
request. Older servers do not implement `pause-if-idle`; the strict client returns
no accepted ACK and never substitutes legacy pause or process signals.

The request checks current agent, cron, API, deferred and native background work on
the Gateway event-loop thread immediately before restart admission. Active
processes, delegations, pending watchers or unreadable probes defer the request.
Failed background observations also keep automatic scale-to-zero awake. Expired
queued strict callbacks are disarmed. A missing reply can still be ambiguous if
a request was already accepted; inspect the existing process/lifecycle evidence
instead of sending another request to manufacture certainty.

Explicit `pause-for-update` keeps its existing bounded-drain behavior. Automatic
callers must opt into `only_if_idle=True`. A successful ACK is admission evidence,
not proof that a replacement loaded the intended source: verify fresh process
identity, canonical bootstrap source, tested file hashes and retained settings.
The lifecycle check covers native work tracked by this Gateway; independently
managed external work still needs its own ownership/resource checks.
