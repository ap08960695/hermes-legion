# Reuse the goal-judge verdict for an identical input (v0.8.37)

After every non-empty turn of a session with an active goal, Hermes asks the
auxiliary judge whether the goal is done. When a turn ends with the same response
as an earlier turn, and the goal, contract, subgoals, background-process and
delegation blocks are also unchanged, the judge input differs only in its clock
line. Hermes used to pay for a second judge call anyway.

`hermes_cli/goals_judge_memo.py` now stores `done`, `blocked` and `continue`
verdicts keyed by a SHA-256 of the system prompt and judge prompt with the current
time removed. A matching input returns the stored verdict without a model call.

- `wait` verdicts are never stored, because they depend on elapsed time.
- Unusable (non-JSON) replies and transport failures are never stored.
- The memo is per process and holds at most 256 entries, oldest evicted first.
- Any change to the response, goal, contract or background state is a new key.

## Evidence and limits

`tests/hermes_cli/test_goal_judge_memo.py` has three cases. The identical-input case
fails on v0.8.36 (two calls) and passes now (one call). Across all 35 test files that
use the judge or goal manager, 494 cases pass on Linux. The 12 native check groups
pass except `profile-archives`, which flags untracked desktop packager archives
already in the dev checkout and unrelated to this change. On ARM64 macOS, 57 cases
in 5 goal files pass in a temporary pytest environment, which was removed afterwards.

The four changed files are installed in the live Linux and Mac checkouts with
matching SHA-256 values. The patch applies to a clean v0.22.5 worktree and passes
`verify_checkout.py --phase installed` for 983 targets. No model request was made.
How often real sessions repeat a final response is not measured, so this saves an
unknown number of calls: zero when responses never repeat. Production Gateways remain
closed and still run their previously imported code.

## Preserve timestamp evidence (v0.8.50)

The original key removed every occurrence of the generated timestamp from the
rendered prompt. When response evidence contained that exact timestamp, removing
it could leave the same key and incorrectly reuse a previous `done` verdict.
The inverse also occurred: unchanged evidence containing an earlier clock value
could miss the memo when only the generated clock advanced.

The judge now captures its template and fields once. It renders the outgoing
prompt normally and a separate canonical memo prompt with only the generated
`current_time` field empty. The memo hashes that canonical text without rewriting
it. Goal, response, criteria, contract and background timestamps remain evidence,
including text that resembles a `Current time:` line. All three template forms
retain their outgoing bytes; contract priority and extra criteria are preserved.

Two parametrized regressions add 18 cases. On the preceding implementation,
15 changed-evidence cases reuse stale `done` and three clock-only cases miss valid
reuse. All 21 cases in the existing regression file pass after repair. Actual
candidate selfchecks also preserve wait/parse/transport non-admission and the
256-entry bound. These checks use a controlled judge, with no model request.

The seven-file native selection first reports **85 passed, 4 failed**: four
PID-wait cases cannot prove process ancestry for guarded child cleanup in this
Mac environment. They remain unverified, not inherited failures or passing tests.
With exactly those four node IDs explicitly excluded, the same selection passes
85 cases; counts overlap. The [verification record](verification.md) names them.
No native live-system guard or assertion is weakened, and all recorded synthetic
30-second child PIDs are subsequently absent.

The trial uses the pinned source and native Python 3.14 dependencies with separate
locked pytest tools, synthetic homes, one worker and no file retries. Task-local
Python guards reject network, owner-state reads and writes outside the trial,
except the exact verified null-device sink. Runner scratch stays inside the trial
and optional precompilation uses one CPU. These are scoped application-level
checks, not OS-wide isolation or a whole-native-suite result. Existing processes
need normal idle adoption; no owner installation or running service is changed.
Live judge `done`/terminal-goal proof, PID behavior, usage savings and cache-hit
improvements remain unproven.
