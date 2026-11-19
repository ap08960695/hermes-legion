# Work tracking and reviewed delivery

Open **Work → Track work** on an enabled Kanban board to follow an objective, its success criteria, responsible profile, recorded step, next action, latest summary, result and delivery evidence. Long task instructions are folded initially. Results use the existing rich Markdown renderer; declared outputs reuse the native download action. The selected card and view are saved by connection and resolved board. Opening or restoring this view does not dispatch work.

A tracked delivery uses the existing version-1 `hermes-contract`, adding relative `required_artifacts`, named `acceptance_criteria` and `require_review: true`. The implementer submits an output and current check records to a different review profile. The reviewer inspects the output, reruns the checks, and either accepts, requests changes on the same card, or blocks for a concrete missing decision. The [goal execution skill](../skills/goal-driven-execution/SKILL.md) describes this flow without adding a scheduler, tool or permission.

Native acceptance binds the implementation handoff, current reviewer run, brief hash, output hashes and declared criteria. Each verification record identifies its own native run and contains check timestamps from that run. Required outputs survive managed scratch cleanup through the existing artifact retention path. Reopening or invalidating an accepted task retires its receipt; manually marking it done cannot revive that acceptance. Legacy completion remains visible as history with acceptance pending.

## Verification scope

The focused backend selection passed 146 tests across eight files; the Kanban renderer selection passed 105 tests across eighteen files. Renderer type checking and affected lint passed. Regression cases cover missing outputs, replayed checks, stale brief/receipt state, independent review, retained outputs, scoped selection and reads that never dispatch.

After installation, three fresh simple cards exercised successful arithmetic delivery, rejection followed by revision, and a missing-input blocker through native workers. These used seven worker runs and twenty physical model requests. A preliminary round used another twenty requests before the final evidence binding was added; it is not counted as acceptance of the final gate. No duplicate dispatch or read-triggered model request was observed. The fixture seeded the cards and explicitly admitted each native dispatch; this is evidence of the bounded worker/reviewer lifecycle, not an unrestricted autonomous Captain planning benchmark.

Linux and Mac packages were rebuilt and installed before publication. Native Work was checked at wide and narrow sizes, including restoring the selected completed card. The download check uses the real native download route with a controlled save-dialog destination and compares the returned bytes. Linux exposed no GPU devices and used an isolated, network-disabled UI fixture. The expected external font request failure is separate from JavaScript page errors. Mac used an isolated home and an offline provider; the UI fixture carries a copy of the accepted card with its output path mapped to that fixture.

Acceptance describes recorded evidence at handoff, not a new execution of checks whenever the page opens, nor universal output correctness. Existing running Gateways were not restarted; protected production settings and held work were preserved. New worker processes and rebuilt Desktop packages contain the update; an already-running process may retain previously loaded code until its normal restart.

## Compare a revision

In **Track work**, open **Compare with the round that asked for changes**.
The comparison pairs the handoff before the latest request with the handoff
after it, when available. It shows artifact changes from recorded hashes and
labels check evidence with its own run. The text diff reads only the selected
file. Both versions must be bounded text and match their recorded hashes.
Historical hashes can remain available after the original file bytes are gone.

[Revision comparison in a synthetic browser fixture](images/work-card-revision-fixture.webp)

## Usage for an accepted result

The accepted card loads recorded usage for THINK, ACTION, revisions, REVIEW
and goal judges when opened in **Track work**. Exact owner admission binds a
worker run to its profile session and compression continuation. Legacy runs
can contribute a bounded diagnostic sample when its key and run binding
match. Each row opens its native run evidence on demand.

Coverage is partial. A shared THINK run can appear on several cards.
Originating Captain sessions, ambiguous ownership and duplicate samples
are excluded. Input includes cached tokens. The cost column sums only
recorded actual USD amounts and leaves absent prices unavailable.

[Usage breakdown in a synthetic browser fixture](images/work-card-usage-fixture.webp)
