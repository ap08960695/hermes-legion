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
