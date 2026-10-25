# Bot activity

The Bots rail keeps a bot's canonical conversation preview and opening behavior.
A separate tools icon and short worker description show a recent observed worker
stamp. The full localized context is available in the existing tooltip; the row
avoids repeating "Worker activity" before every description. If a description is
missing, the worker title is used; with neither, a localized activity label remains.

The roster projection reuses its existing bounded session read. It includes only
the worker description (at most 120 characters) and terminal timestamp alongside
existing identity/title/activity fields. It adds no model request, timer, extra
query, account lookup or provider fallback. The usual roster refresh owns updates.

## Meaning and limits

- A worker with a terminal timestamp does not show current-worker detail or a
  worker-driven busy mood, even if its last activity is recent.
- Retained, missing-source and explicitly unreachable rows do not advertise a
  worker stamp as current. Their conversation preview remains available.
- Other workers retain the native 150-second recency policy. Recent activity is
  an observation, not proof of a still-running process, live tool, delivered
  result or successful task completion.
- The description is separate from the canonical chat preview. Clicking the bot
  still resolves the same native canonical conversation; it does not open the
  worker's transient session.
- Older backends may omit the new optional fields. Existing title/recency
  behavior remains; no new transport capability is required.

Compression-lineage projection also takes activity timestamp, description and
provenance from the displayed tip. Otherwise a row could display the tip's ID and
title beside the root's outdated activity. This repair applies to both compact
and full native session read paths without adding a query or schema migration.

## Verify locally

Use an isolated checkout and the pinned patch installation procedure. Run the
following through the checkout's native test runner and existing managed test
environment, with retries disabled:

```sh
HERMES_TEST_FILE_RETRIES=0 scripts/run_tests.sh -j 2 \
  tests/hermes_state/test_session_activity_projection.py \
  tests/tui_gateway/test_profiles_list_worker_session.py
```

These tests use temporary native SQLite state. They exercise terminal and active
workers, compact/full compression projection, payload boundaries and canonical
conversation preservation. They do not create a real task or call a provider.

Renderer checks live with `bot-row.test.tsx` and `row-helpers.test.ts` under the
native Desktop package. Follow upstream's dependency setup; the companion does
not install those dependencies. The rendered fixture used during development
also exercised active, terminal, unreachable and older-backend states with
synthetic data and the native diagram renderer.

Source installation, renderer compilation and activation are separate steps.
An existing Desktop or Gateway process must load changed modules through its
supported idle lifecycle. Do not hotpatch, signal a worker or force a restart to
make a status display current. This release does not replace the Desktop layout.
