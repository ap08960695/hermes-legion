# Role-specific THINK / ACTION handoffs

This extension pairs **bots by their actual job**. Developer THINK plans for Developer ACTION; Research THINK plans for Research ACTION. There is no mandatory global planner or executor, and the pairing does not determine the model. Each bot keeps its own native model/provider/reasoning configuration.

This document describes the extension implementation. Local profile migration, provider-backed bot acceptance and production activation must be recorded separately. An offline lifecycle test is not proof that an account or model is available.

## Pair existing bots

Use the Bots editor's THINK / ACTION settings, or the authenticated `profiles.workflow.get` / `profiles.workflow.configure` operations. Writes require the expected configuration revision and the appropriate native profile/host capability. Saving these fields does not switch an active session or change its model.

### Choose the model for each bot

The same editor can save a bot's role, provider, model and effort in one revision-fenced operation. A rejected model, invalid effort, stale revision or declined selection warning writes neither half. Catalog validation uses the selected bot's credential scope; it does not start inference. A change to effort alone keeps the saved route and needs no provider probe.

Effort is stored as a native override for the selected model, preserving the bot's global policy and other model overrides. “Keep existing effort policy” leaves those settings intact. The editor shows the effective configured effort; provider-specific wire clamping and availability remain separate runtime facts. Quotas, fallback routes, credentials and counterpart configurations are unchanged.

These are defaults for future runs. Existing chats and active workers retain their current model and context. The native cost/data-policy confirmation applies before committing a changed model. Reopening the editor reads the saved values; a role label never selects a model automatically.

For a Developer THINK bot:

```yaml
bot_workflow:
  role: developer
  mode: think
  family: gpt
  counterpart: developer-action
```

For its Developer ACTION bot:

```yaml
bot_workflow:
  role: developer
  mode: action
  family: gpt
  counterpart: developer-think
```

Both links must be reciprocal, with matching roles and opposite modes. Supported family labels are `gpt`, `claude`, `agy`, `nim` and `web`. A label or a linked pair is configuration information; it does not prove subscription eligibility, remaining quota, tool access, confidentiality clearance or provider readiness. Preserve the existing account pool and its shared concurrency/rate limits. Do not create paid fallback routes.

Create new counterpart bots when needed. Before converting an existing bot, inspect its assigned unfinished work and active sessions. Do not repurpose a live worker to satisfy a rollout checklist. Keep planning bots' tools limited to their planning duties; a role label is not an execution sandbox.

## Captain → THINK

Captain selects an eligible role pair using existing project, confidentiality, tool, quota and approval gates. Send THINK a bounded planning task with clear acceptance criteria. THINK plans only and completes its native task with a structured `metadata.role_plan`:

```json
{
  "role_plan": {
    "version": 1,
    "role": "developer",
    "constraints": ["Keep existing quota and approval gates; no paid fallback"],
    "steps": [
      {
        "id": "implement",
        "instructions": "Implement the agreed change and run its offline regression test.",
        "acceptance": ["The regression test passes", "Existing behavior remains covered"],
        "write_scope": ["src/example.py", "tests/test_example.py"]
      },
      {
        "id": "document",
        "instructions": "Document the resulting behavior.",
        "acceptance": ["The example matches the implementation"],
        "write_scope": ["docs/example.md"]
      }
    ]
  }
}
```

The native handoff requires a current THINK run, validates the plan, and stores its SHA256 plus the bounded plan on that same run. The plan survives managed scratch-workspace cleanup. It is not an instruction to retain the complete THINK conversation.

Limits: version 1; at most 16 steps; at most 16 constraints and acceptance items per step; at most 500 characters per item; 2,000 characters per step instruction; 16 KiB total canonical JSON. Step IDs must be unique lowercase identifiers. An empty `write_scope` declares no writes. Declared paths are relative literal paths; they do not grant filesystem permission.

## THINK → ACTION

After THINK is genuinely done, Captain uses the existing `kanban_create` tool:

```json
{
  "title": "Implement the planned change",
  "assignee": "developer-action",
  "plan_task": "<completed-think-task-id>",
  "plan_step": "implement"
}
```

The task gets an exact parent/run/plan-hash/step binding and native dependency edges. Its deterministic idempotency key is generated automatically; do not supply another key. Repeating an identical request returns the original task, including after native review or archival, without starting another attempt. Changed scope requires a new THINK plan. Existing model/provider/effort, runtime and goal fields remain governed by native validation.

Only the selected step and shared constraints enter ACTION's additional context. The complete plan is recoverable from the named THINK task/run. Native dispatch, direct claims, worker context and terminal handoffs all revalidate the binding. Missing, stale or incompatible plans cannot start an ACTION run. The dispatcher parks that condition through its existing capability block without spending a worker retry.

Steps with independent write scopes can be ready together, within existing profile/account/resource limits. Add `"after": ["implement"]` to a later step when it depends on an earlier step. Create prerequisites first; the dependent task stays in `todo` until its native parents finish. Overlapping declared write scopes require an explicit dependency. Cross-project/resource locks remain authoritative.

## Review and failures

Use the native review/request-changes flow. Review changes return to the original ACTION implementer; this does not require re-planning routine corrections. An independent reviewer may own a review run without being mistaken for the original ACTION bot.

When the plan itself is unusable, ACTION blocks once with the concrete reason. Captain can create a new task for the same role THINK bot:

```json
{
  "title": "Revise the unusable plan",
  "assignee": "developer-think",
  "replan_of": "<blocked-action-task-id>"
}
```

This requires an actual blocked ACTION run and its recorded reason. It creates an idempotent new planning task linked to the previous completed THINK parent. It never reopens, retries or replays the blocked ACTION. A successful new plan has a new run/hash and produces separately bound ACTION work.

Wait for existing native completion/block notifications. Do not poll the model, repeat create calls to test progress, or call `kanban_show` after a successful `kanban_complete`. Stop the worker after its successful terminal handoff. Ask the owner only when the remaining decision exceeds the existing authorization or requires unavailable input.

A completed step, a passing offline test or a role-plan hash never waives independent review, rights, publication, privacy or project holds. Provider-backed acceptance, before/after usage measurements and production installation are separate evidence.

## Keep project data on its approved lane

A profile can declare `kanban.blocked_task_markers`, a list of up to 32 literal strings
(1–160 characters each). Matching is case-insensitive across the task title, body,
tenant and workspace path. A match refuses a direct claim and blocks automatic
dispatch before a worker attempt or model call. Invalid policy fails closed. The
assignee's own configuration applies, independently of the hosting Captain profile.

```yaml
kanban:
  blocked_task_markers:
    - confidential-project-example
```

Use the same markers as the owner's existing routing policy on every restricted
THINK and ACTION counterpart. Markers enforce that declared boundary; an unmatched
task is not proof of confidentiality clearance. Existing account, quota and approval
checks still apply. Do not reroute a refused task to another paid provider automatically.

Generic task decomposition offers planning bots and legacy roles. Linked ACTION bots
are excluded because they require a completed, pinned plan. If a decomposition result
chooses ACTION, the native router selects its reciprocal THINK counterpart. An ACTION
root is refused before the auxiliary model call. Its existing task is left intact.
Both halves must be admitted by the owning fleet dispatcher's existing profile
allowlist. A routed Captain's private configuration cannot widen that list. If a
chosen pair is unavailable, decomposition refuses it instead of silently assigning
the work to another bot or account.
