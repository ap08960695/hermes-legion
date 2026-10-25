---
name: goal-driven-execution
description: Use for an authorized multi-step objective, delegated decisions, or resuming unfinished work in the current session.
---

# Goal-driven execution

1. Read the latest owner objective, project contract and native task state. Record deliverables, verification, authorized scope and material stop conditions. Reuse existing cards, operations and owner answers.
2. Inspect the current session once with `hermes goal status`. If a goal exists, work within it. Preserve active goals and owner pauses. For a new authorized objective, use `hermes goal ensure` only when the owner enabled profile self-management; include explicit `outcome:` and `verification:` fields. It writes the existing native goal store without starting another model turn. If disabled, continue the authorized task using its existing contract, or let the owner set `/goal` in the session.
3. Select and read the applicable installed skills through native skill discovery. Use the narrowest relevant workflow and load further references only when needed. A skill supplies a method, not additional authority.
4. Decide reversible implementation details, sequencing, offline checks and remedies within the delegated scope. Prefer the option best supported by acceptance criteria, reuse and measured cost. Record consequential choices briefly with the reason and evidence; continue without routine permission questions.
5. Start eligible independent work once, with disjoint write scopes, native claims and current capacity checks. Before waiting, check other ready work. Retain script/worker identities and use native completion delivery or bounded non-model waits. Resume the original operation after interruption using its checkpoint.
6. Check each deliverable against actual acceptance evidence. Continue correcting authorized failures within existing limits. Completion requires verified outputs and no required work remaining; a green unit test alone does not establish deployment, visual quality or production savings.

Ask only when the next required action changes material scope, incurs unapproved cost, needs unavailable access, risks irreversible effects, conflicts with acceptance criteria or crosses a rights/review/publication gate. Continue independent authorized work while that decision waits. Time passing does not grant permission. Notify on completion, failure or a material question; keep unchanged waits quiet.

Keep existing turn caps, quotas, models, accounts and provider routes. Dispatched workers complete their assigned native task; they cannot extend it with a self-goal. Preserve user pauses and existing goal content. No paid fallback, quota probes, duplicate dispatch, unrelated worker interruption or extra inference solely for status/proof. A goal schedules normal work within native limits; it cannot guarantee completion when a real external dependency remains.
