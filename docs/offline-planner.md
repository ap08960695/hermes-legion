# Offline configuration and routing dry-run

`scripts/legion_plan.py` uses Python's standard library only. It reads only the explicit JSON files supplied to it. It does not import Hermes, inspect real auth files, open a socket, run a subprocess, mutate a snapshot, persist reservations or call a model. It outputs `executed: false` even when a recommendation is `selected`.

## Check a configuration

```sh
python3 scripts/legion_plan.py --team examples/team.full.json
```

This validates references and policy without selecting work. Unknown keys (including credential fields), duplicate identities/JSON keys, mismatched account/provider references, split account budgets and paid fallback are refused. Errors omit input values.

## Demonstrate the parallel workflow

```sh
python3 scripts/legion_plan.py --team examples/team.full.json   --snapshot examples/snapshots/synthetic-ready.json   --tasks examples/scenarios/parallel-production.json --now 1
```

The completed research is skipped; implementation, documents, analysis and media preparation are recommended in parallel within the simulated shared budgets. Review waits for its producer; an existing running operator is retained. Model IDs/readiness are placeholders and synthetic evidence, not verified live providers.

## Demonstrate shared budgets and privacy

```sh
python3 scripts/legion_plan.py --team examples/team.full.json   --snapshot examples/snapshots/synthetic-ready.json   --tasks examples/scenarios/shared-account-capacity.json --now 1
python3 scripts/legion_plan.py --team examples/team.full.json   --snapshot examples/snapshots/synthetic-ready.json   --tasks examples/scenarios/private-coding.json --now 1
```

Profiles using the same account debit one group. The private task cannot select a public-only Web lane. Other ready eligible accounts can serve **new** sessions without increasing a cap.

## Demonstrate session affinity and cooldown

```sh
python3 scripts/legion_plan.py --team examples/team.full.json   --snapshot examples/snapshots/synthetic-codex-cooldown.json   --tasks examples/scenarios/sticky-session.json   --pins examples/session-pins.synthetic.json --now 1
```

The pinned route is cooling down, so the recommendation is HOLD; it does not jump to another account or reset anything. Without a pins file, an eligible new session can be planned separately.

## Fail closed without current evidence

```sh
python3 scripts/legion_plan.py --team examples/team.full.json   --tasks examples/scenarios/parallel-production.json --now 1
```

Ready work is held when the snapshot is absent. An expired snapshot, absent budget counter, unknown account/profile readiness or unverified required capability also holds. Running sessions and sessions already selected in the same plan are busy: no second task is selected for them. Non-finite times and nonstandard JSON `NaN`/`Infinity` are refused rather than treated as permanently current evidence. `--now 1` is for deterministic fabricated examples only. Never use a fake observation time to make real expired data usable.

## Boundaries

This is a reference planner, **not a live router or quota service**. A recommendation does not pin a credential in Hermes, change an existing session, guarantee cache reuse, establish account eligibility or reserve a native slot. Runtime application remains an operator/native-workflow step with fresh gates and actual provider selection. Do not point it at native `auth.json`, `.env` or a personal profile; those are deliberately not its input formats.

## Explain why a route was selected or held

```sh
python3 scripts/legion_plan.py --team examples/team.full.json --snapshot examples/snapshots/synthetic-codex-cooldown.json --tasks examples/scenarios/sticky-session.json --pins examples/session-pins.synthetic.json --now 1 --explain
```

`--explain` adds an `explanation` object to each decision, without changing decisions, pins, reservations or input files. A busy session, unfinished dependency, stale/missing snapshot or existing worker is explained as a `gate` with no candidate search. An unavailable pinned reference remains pinned; alternatives are not considered.

For tasks reaching route selection, `candidates` reports each allowed profile/account alias and its rejection codes. Codes distinguish role/privacy mismatches, undeclared or unverified capabilities, profile/account readiness, missing/invalid quota evidence, cooldown, parallel capacity, and hour/day budgets. A candidate can have several reasons. Eligible alternatives are labeled `lower-priority` (including native account-list order); the selected route is labeled `selected`. Candidate evidence is evaluated before that task's simulated reservation, so the selected candidate does not appear to exhaust its own slot.

Explanations use only the supplied offline metadata. They do not probe accounts, reveal credential values, discover actual native credential selection or authorize a retry. Without the flag, the original output structure is preserved. See [offline doctor and setup](offline-setup-tools.md) for configuration preparation.
