# Offline examples

These are **Legion planning documents**, not native Hermes config files. All account aliases, principal references, labels, readiness and remaining budgets are synthetic. The numbers are not recommended quotas, not the author's actual limits, and never configure a real service.

- `team.small.json`: five profiles illustrating role twins and one Web specialist.
- `team.full.json`: Captain/planner, thirteen worker-role families with native-provider twins, and six named Web specialists (34 profiles in total).
- `snapshots/`: disposable simulated state; no token store or live usage is read.
- `scenarios/`: synthetic task lists. Already running tasks are retained; dependent reviews wait.
- `session-pins.synthetic.json`: an existing profile/account recommendation retained across a simulated session.

For a deterministic demonstration, use `--now 1` with the synthetic snapshots. Without a current snapshot, ready work is held. Never extend a stale real snapshot to make work eligible. Use aliases without names, emails, account IDs or tokens. Native config fragments are separately identified under `profiles/native/`.

## Explicit native fragments

`native/prompt-cache-auto.fragment.json` is an optional native config **merge fragment**, unlike the planning documents above. It contains one setting and must not replace an existing config. Follow [the scoped native recipe](../docs/prompt-cache-policy.md); defaults, routes, accounts, quotas and fallback settings are not modified by opening or exporting this file.
