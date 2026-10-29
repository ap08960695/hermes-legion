# Managed workers use the owning source tree

A routed profile intentionally receives a sanitized subprocess environment. That
scrub can remove the Hermes checkout from PYTHONPATH. A managed worker launched
with python -m agent.managed_worker could then bind an older editable/runtime
agent package while other imports came from the current owner checkout. The
observed failure was ModuleNotFoundError for agent.reasoning_limits before any
provider request. The native admission remained unknown; it was not replayed or
reclassified as a successful task.

The managed launcher now uses the existing native source/dependency pinning helper,
after the profile scrub and before process startup, as cron and Kanban already do.
It preserves the owning profile's sanitized secrets, inherited client paths and
module entrypoint. It does not copy source into an environment, install packages,
change profiles or providers, bypass approval, or increase concurrency or quotas.
Single-profile workers retain their inherited environment plus this import pin.

## Verification

- The regression starts a real Python child with safe-path mode and a stale agent
  package. Both routed and inherited-environment cases failed before the repair.
- The full managed-worker selection passed 124 tests in 40 files, no retry or
  failure. This includes profile secret boundaries, stop/drain, ownership and
  tool/client environment behavior. Focused runs overlap and are not added.
- Installed native checks on Linux and macOS launch through the real managed
  spawn path and load agent, gateway policy and effort limits from the same
  checkout. Own-profile environment is retained and launch credentials absent.
  These checks use synthetic credentials, no network or model requests.
- Exact two-file installation preserves original permissions and configuration.
  The original macOS Gateway is not started merely for acceptance.

Provider-backed parallel-bot acceptance is a separate bounded case. See release
verification for its final result; import checks alone do not prove coordination,
original-session adoption, all provider families, faster work or lower billing.

## Bounded real-provider follow-up

After the import repair, a new synthetic ledger case reached the existing Codex
account through native memory-only credential access and created a real paired
THINK task. Its coordinator consumed the fixture's seven-iteration cap before
its own terminal completion. The native result was gave_up after eight physical
requests, not a successful parallel loop. The completed provider requests prove
the worker now starts, but do not prove bot overlap or end-to-end coordination.
The failed coordinator and ready child remain evidence and were not replayed.
The original fleet stop state, configuration and models remained unchanged; no
paid fallback, quota change or original user workload was used.
