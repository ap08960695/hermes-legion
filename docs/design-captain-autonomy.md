# Captain autonomy

## Outcome

Give a Captain one authorized goal, let it decide and delegate within that scope,
show its plan and decisions, follow actual results, and finish or stop with evidence.
The owner can inspect and stop work. This capability is developed across rounds;
it is not released until its complete native acceptance passes.

## Existing authority

Native goals already persist a contract, continuation budget, pause/wait/done state,
tracked work and judge results. Profile flags `goals.allow_self_management` and
`goals.delegated_decisions` independently opt into self-setting and routine choices.
Both default false. `hermes goal ensure` preserves existing goals and pauses;
ordinary workers retain their assigned lifecycle. Existing goal/worker controls,
model/provider/account/quota, review and publication gates remain authoritative.
The UI does not become another scheduler or infer completion from activity.

## Approaches

- Extend native goals and profile settings: reuse current persistence, controls
  and ownership. Chosen; least new state and preserves other Hermes surfaces.
- Add an autonomy-level setting: simpler label, but duplicates two independent
  native permissions and creates conflicting authority. Rejected.
- Build a separate Captain runner/dashboard: larger parallel engine without a
  proven missing backend capability. Rejected.

These are maintainer implementation choices under the standing delegated goal.

## First complete step: profile controls

Add **Safety → Captain autonomy** using existing generic config rows and scoped
read/save/search routing. Expose only these existing permissions:

| Control | Native value | Boundary |
| --- | --- | --- |
| Let Captain set its own goal | `goals.allow_self_management` | Bound session only; preserves existing goals and pauses; does not start work |
| Delegate routine decisions | `goals.delegated_decisions` | In-scope choices only; approvals, external blockers and spending limits remain |

Keep `goals.max_turns` and every recorded goal budget unchanged. Do not add a
budget editor in this first step. Do not bundle or enable the switches, alter
defaults, select a model/provider,
raise a budget, or change a live conversation's cached prompt. Make the selected
profile visible through the existing scope control. Use translated field labels
and descriptions; settings search opens the same page. A backend exposing a permission in neither config nor schema must not gain a
fabricated opt-in merely because this page exists.

Scope: settings section/subpage mapping, field copy/locales, nearest route and
profile-save tests, changed patch sections and packaged documentation/inventory.
No new RPC, dependency, enum, store, worker or timer.

Acceptance for this step: real isolated Local screenshots before/after; explicit
UI edits read back through native config, survive reopening, affect only the
selected profile and preserve unrelated values. Back up fixture config first,
restore afterward, and close all owned processes. One worker/build at a time,
maximum four Hermes processes and less than 4 GiB extra RAM; no other host/ai.
Unit checks and existing release/secret gates complete the source-kit handoff.
This proves configuration, not autonomous execution or tool approval.

## Remaining capability acceptance

1. Show the current goal, plan, consequential decisions and actual delegated work
   through existing Goal/Catch up/Work/Monitor surfaces; add only proven gaps.
2. Run a bounded native `/goal` case: decide, delegate, follow results, verify and
   reach a terminal result without routine owner questions. Separate deterministic
   fixture plumbing from actual provider-backed behavioral evidence.
3. Exercise owner Stop/pause, external blocker and budget exhaustion, preserving
   recorded attempts and existing permission boundaries.
4. Release the complete visible batch with plain-language notes and screenshots.

Do not use owner state or enable an ESTOP/pause/timer. First ai connection and
owner-app adoption remain lead/owner-only. Agent-desktop input's separate native
lock-write exception stays ungranted; it is not needed for these CUA fixture checks.

## Next complete step: plan and delegated activity in Catch up

Reuse the current session's native todo plan and delegated-worker records in
Catch up, beside the existing goal and controls. Reuse StatusSection/StatusItemRow
and existing translated labels; retained tasks use the existing previous-task
label and historical rendering. Show worker native status and latest recorded
progress/result; open the worker's actual session with the Captain parent context.
Use the underlying subagent store because the composer aggregate intentionally
contains only running workers. No new RPC, poll, scheduler or inference.

Unknown/empty activity remains unreported, never borrowed from another session.
Native goal state alone determines completion. Activity finishing cannot rewrite
a goal or imply verification. Alternatives: linking only to worker runs leaves
the plan hidden; a new autonomy dashboard duplicates existing state.

Scope: focus control-panel adapter/tests, WorkPanel slot and LiveWorkPanel wiring;
changed source patch sections, docs and inventory. Session switching, late events,
retained snapshots, queued/failed/completed workers and worker navigation need
nearest integration coverage plus isolated Local before/after screenshots. This
step proves received activity visibility, not autonomous provider reasoning.

### Received terminal results across parent follow-up

Native acceptance reproduced a missing result: message.start prunes completed
workers for the live shelf, and Catch up then loses its failed worker. Preserve
that live lifecycle. In the existing subagent module, retain only the latest
pruned terminal batch, as the existing todo module retains its latest snapshot.
Catch up merges those received terminal records with current rows by worker ID,
with current rows winning. Existing session clear/Stop and gateway-switch wipe
remove both views, including a retained-only session. Live counters, retirement
tombstones and pending worker behavior remain unchanged.

This is one bounded in-memory snapshot per runtime session, not a durable history
engine. A renderer reload depends on the existing native reports; no new disk
store, RPC, poll, timer or goal authority. Tests exercise the actual parent-turn
prune, replacement rather than accumulating batches, reset/owner isolation and
child navigation; native acceptance must keep Failed visible after follow-up.
