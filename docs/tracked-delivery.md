# Work tracking and reviewed delivery

Open **Work → Track work** on an enabled Kanban board to follow an objective, its success criteria, responsible profile, recorded step, next action, latest summary, result and delivery evidence. Long task instructions are folded initially. Results use the existing rich Markdown renderer; declared outputs reuse the native download action. The selected card and view are saved by connection and resolved board. Opening or restoring this view does not dispatch work.

On the board, use Tab to focus a card and Enter or Space to open it.
Press Shift+F10 or the Context Menu key for actions such as **Select**.
Escape closes the menu. Press it again on the board to clear selection.
After a partial bulk **Move**, focus stays on **Move to** so you can retry
the remaining cards. After a complete move, focus returns to **Filter cards**
if you stayed in the Move controls.
The bulk action buttons show a keyboard focus outline while you navigate.
In narrow panes, the Work views wrap below the board filters and **New task**.
The **Filters** menu reports selected profiles and tenants and checked toggles to assistive technology.
The **Board** menu marks the active board as selected.
The card’s **Status** menu marks the current status and explains system-managed choices.
**Filter cards** uses its own row in narrow panes, so typing keeps nearby controls in place.
**Clear search** restores the full board and returns focus to **Filter cards**.
Filtering **Current work** in a narrow pane brings the first matching lane into view.
In **Workflow**, the graph keeps the pane width and the selected card's details
stack below it. The graph controls wrap to stay reachable.
When card details close, keyboard focus returns to the button that opened them.
If that button disappeared from the same board, focus returns to **Filter cards**.
Tabbing to a link in a folded card description expands the description and
brings that link into view.
Tab into **Activity** or **Worker log** to scroll with the keyboard. Refreshes
keep your place while you read earlier entries and follow new ones at the end.
Long **Activity** details wrap below the event label and time.
The card's feed tabs wrap in narrow windows. Focus or hover over **Comment help**
to read how comments reach the worker.
Long card titles and status labels wrap to keep the full text readable and
the header controls within reach.
**Copy workspace path** copies the full path. It and the **Model** picker
show an outline when focused with the keyboard.
In **Runs**, focus a run with a long result and press Enter or Space to read
its full summary or error. Page Down scrolls the list.

In a narrow pane, **Track work** puts the card list above delivery details.
When cards in the current list share a title, Track work shows their
status, assignee and card ID so you can choose the right one.
In **Track work** and **History**, activating a focused **Show more** brings
the first newly visible card into focus. Press Enter to open the card.
Use **All work** to clear the selected card and return keyboard focus to its
picker entry, or to the picker if that entry is hidden.

If the first read fails, use **Retry** to load the same card. If a refresh
fails, Track work keeps the last loaded card and its open revision comparison
visible with a warning. **Retry** updates the card when the read succeeds.

A tracked delivery uses the existing version-1 `hermes-contract`, adding relative `required_artifacts`, named `acceptance_criteria` and `require_review: true`. The implementer submits an output and current check records to a different review profile. The reviewer inspects the output, reruns the checks, and either accepts, requests changes on the same card, or blocks for a concrete missing decision. The [goal execution skill](../skills/goal-driven-execution/SKILL.md) describes this flow without adding a scheduler, tool or permission.

Native acceptance binds the implementation handoff, current reviewer run, brief hash, output hashes and declared criteria. Each verification record identifies its own native run and contains check timestamps from that run. Required outputs survive managed scratch cleanup through the existing artifact retention path. Reopening or invalidating an accepted task retires its receipt; manually marking it done cannot revive that acceptance. Legacy completion remains visible as history with acceptance pending.

## Verification scope

The focused backend selection passed 146 tests across eight files; the Kanban renderer selection passed 105 tests across eighteen files. Renderer type checking and affected lint passed. Regression cases cover missing outputs, replayed checks, stale brief/receipt state, independent review, retained outputs, scoped selection and reads that never dispatch.

After installation, three fresh simple cards exercised successful arithmetic delivery, rejection followed by revision, and a missing-input blocker through native workers. These used seven worker runs and twenty physical model requests. A preliminary round used another twenty requests before the final evidence binding was added; it is not counted as acceptance of the final gate. No duplicate dispatch or read-triggered model request was observed. The fixture seeded the cards and explicitly admitted each native dispatch; this is evidence of the bounded worker/reviewer lifecycle, not an unrestricted autonomous Captain planning benchmark.

Linux and Mac packages were rebuilt and installed before publication. Native Work was checked at wide and narrow sizes, including restoring the selected completed card. The download check uses the real native download route with a controlled save-dialog destination and compares the returned bytes. Linux exposed no GPU devices and used an isolated, network-disabled UI fixture. The expected external font request failure is separate from JavaScript page errors. Mac used an isolated home and an offline provider; the UI fixture carries a copy of the accepted card with its output path mapped to that fixture.

Acceptance describes recorded evidence at handoff, not a new execution of checks whenever the page opens, nor universal output correctness. Existing running Gateways were not restarted; protected production settings and held work were preserved. New worker processes and rebuilt Desktop packages contain the update; an already-running process may retain previously loaded code until its normal restart.

In the Work card drawer, a comment that fails to send stays in the editor.
Text you type while another comment is sending stays available as a draft.

**Edit description** focuses the editor. If saving fails, the description
draft stays open so you can retry. **Cancel edit** discards the draft.

Long attachment names wrap so the full name stays readable. A pending
download stays in the tab order and ignores repeat activation.

**Blocked by** and **Blocks** show full card titles and a visible keyboard
focus outline. Activate a title to open its card.

## Compare a revision

In **Track work**, open **Compare with the round that asked for changes**.
Track Work opens the latest request for changes. Use **Revision round** to
compare an earlier request on the same card. The five most recent requests
are shown. The comparison disclosure and round picker show a focus outline
when you reach them with Tab and stay inside a narrow card. Each comparison
pairs the handoff before that request with the last handoff before the next
request. The latest round
shows a waiting state until a revised handoff is available.

The comparison shows recorded artifact changes and labels check evidence by
run. Earlier rounds use recorded check IDs if the card brief has since changed.
A text diff reads only the selected file. Both versions must be bounded text
and match their recorded hashes. Historical hashes can remain available after
the file bytes are gone. If the comparison is stale, **Refresh card** loads
the latest revision list in place. Select a file to load its updated diff.
You can switch files without waiting. Focus stays on
the file button when the diff loads. Tab to the diff named for the selected
file, use the arrow keys or Page Down to scroll, then Tab to leave.

[Revision comparison in a synthetic browser fixture](images/work-card-revision-fixture.webp)

## Usage for an accepted result

The accepted card loads recorded usage for THINK, ACTION, revisions, REVIEW
and goal judges when opened in **Track work**. Exact owner admission binds a
worker run to its profile session and compression continuation. Legacy runs
can contribute a bounded diagnostic sample when its key and run binding
match. Each row opens its native run evidence on demand. If it fails to
load, use **Retry run** in the open row. The totals and other open run
details stay visible.
If a refresh fails, the last loaded totals and open run evidence stay
visible with a warning. **Retry usage** rechecks the same card and review.
On a narrow pane, press Tab to focus **Usage by phase** and use the
Left and Right arrows to scroll through the columns. Press Tab again
to reach the run evidence. The run and retry buttons show a focus outline.

Coverage is partial. When THINK usage is linked, the table explains that
adding card totals can count the same run twice. Use the run evidence to
identify planning usage shared by several results.
Originating Captain sessions, ambiguous ownership and duplicate samples
are excluded. Input includes cached tokens. The cost column sums only
recorded actual USD amounts and leaves absent prices unavailable.

[Usage breakdown in a synthetic browser fixture](images/work-card-usage-fixture.webp)
