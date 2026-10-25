# Goals, skills and delegated Captain decisions

Give the Captain an outcome and decision boundary so it can finish authorized work while you are away. Native `/goal` tracks continuation; skills provide the method; the project contract supplies acceptance criteria and authority. These complement the existing Kanban workflow rather than creating another task engine.

## Set an owner goal

In the intended Hermes session, inspect `/goal status` first. If no goal exists, set a concrete objective with `/goal <text>`, for example:

```text
/goal Deliver the approved documentation update.
outcome: All requested sections and examples are complete.
verification: Review the rendered documents and run the existing offline checks.
constraints: Keep current quotas, models and provider routes; no paid fallback.
boundaries: The assigned documentation directory; no production changes or publication.
stop_when: Required access is unavailable or the requested acceptance criteria conflict.
```

Keep the current native turn cap. `/goal` work and its normal native completion judge may use your existing model allowance; this is not unlimited or free execution. A blocked external dependency remains blocked. Inspect a paused goal before choosing `/goal resume` in that session; do not clear, replace or repeatedly resume it merely to keep activity going.

## Let a Captain establish its own goal

The patched command `hermes goal status|show|ensure` is bound to the calling session and profile. `status` reads compact metadata; `show` also displays the goal/contract, so keep its output private. Neither starts a chat. To permit self-setting, the owner explicitly enables `goals.allow_self_management: true` in that Captain profile using the native config workflow. The default is false; turn budgets remain unchanged.

For an existing profile named `legion-legatus`, after applying and verifying the complete patch:

```sh
hermes -p legion-legatus config set goals.allow_self_management true
```

Replace the profile name with your intended Captain profile. This changes only the self-setting permission; keep your current goal/turn settings. Do not replace the whole profile configuration with an example.

From a tool running inside that session, after confirming a new objective is authorized:

```sh
hermes goal ensure <<'GOAL'
Deliver the approved documentation update
outcome: All requested sections and examples are complete
verification: Review the documents and run existing offline checks
constraints: Preserve current quotas, models and provider routes
boundaries: The assigned documentation directory
GOAL
```

The command requires an existing open session and explicit outcome/verification. It preserves active, paused and cleared goals. An identical completed objective stays complete; a different authorized objective after completion can use the profile's existing cap. Concurrent owner changes win over stale writes. No session-selection, resume, clear or budget-override command is exposed. Dispatched/delegated workers retain their native task lifecycle.

This command only stores native goal metadata. It does not dispatch a worker, invoke a judge, send a kickoff, install a timer or call a model. The existing post-turn hooks see it when normal authorized work completes a turn. With the CLI, a fresh metadata read also respects a pause made through another surface. Do not run `ensure` as a polling loop or claim that metadata creation proves autonomous execution.

## Check every intended Captain

Self-management permission and skill installation belong to a profile. Enabling one Captain does not configure a second Captain. The profile selected in Desktop also does not select the profile of a terminal command. On an existing working installation, check the configuration path and permission for each intended profile first:

```sh
hermes config path
hermes config get goals.allow_self_management
hermes -p legion-legatus config path
hermes -p legion-legatus config get goals.allow_self_management
```

Use the first pair for the terminal's current launch home and the second pair for the named example profile. After confirming the intended main Captain home, the owner can explicitly opt it in with `hermes config set goals.allow_self_management true`. Keep the existing goal, turn cap, models, accounts and quotas. Ordinary dispatched workers still retain their task lifecycle and cannot extend it with a self-goal.

Install the published `goal-driven-execution` skill in each intended Captain's native skill scope, then confirm that native skill discovery and viewing can resolve that same content. A file installed for another profile is insufficient. A short pointer in that Captain's SOUL can keep the method on demand:

```text
For an explicitly authorized multi-step objective or continuation, load the installed goal-driven-execution skill through native skill discovery. It governs current-session goals, parallel work, verification and routine delegated decisions within the existing owner scope, quotas and gates.
```

These checks establish configuration and discoverability. They do not establish that a cached Captain has read the pointer, used a skill or completed autonomous work. Retain existing conversation prefixes and verify that behavior through the next normal authorized task rather than sending an extra model request solely for proof.

## Supply the skill and decision policy

Review [goal-driven-execution](../skills/goal-driven-execution/SKILL.md) and install its directory into the intended profile's native skills directory using your normal skill workflow. Have the Captain discover/read it for multi-step objectives; select specialist skills according to the actual task. Keep skill bodies on demand rather than rebuilding a live conversation's system prefix.

| Captain can decide within authorization | Ask only if the action requires it |
|---|---|
| Reversible implementation details and sequencing | Material scope or conflicting acceptance criteria |
| Offline verification and bounded correction of failures | Unapproved expenditure or unavailable access |
| Eligible parallel work under current claims/capacity | Irreversible changes or rights/review/publication approval |
| Reusing an owner answer, checkpoint or existing operation | A missing owner-only decision with no authorized default |

Record consequential choices and evidence with the existing task. Notify the owner only on completion, failure or a material decision. Do other authorized independent work while waiting. User pauses, quotas, account bindings and project gates continue to apply. Enabling this policy does not authorize a provider change or paid fallback.

For an already-running conversation, load the skill through native skill discovery on the next authorized turn. Changing a SOUL file does not prove that a cached agent has loaded it. New agents read the updated profile normally; use the documented idle lifecycle for process changes and retain the current goal and session.
