# Live Captain cards on 2026-11-09

These are isolated private Hermes homes. Each run has a counted model relay, a 1 GiB
memory cgroup, no Linux GPU, and production Gateways closed on Linux and Mac. The
owner's ceiling of 32 model requests is now fully used.

| Card | Source | Requests | What was proven from native records | Why it stopped |
| --- | --- | --- | --- | --- |
| t_a12e6e49 | v0.8.33 kit | 5 | Native skill discovery, exact installed skill read, card read, `hermes goal status` | The model invented `--outcome`/`--verification` flags; the skill was fixed in v0.8.34 |
| t_58048ed9 | v0.8.34 skill | 5 | The Captain created its own native session goal with `hermes goal ensure` | Ran `python3`, which the test policy forbids |
| t_4380d341 | v0.8.40 kit (989 paths) | 4 | Owner `/goal` set through the native TUI command path (no model call). The Captain chose between the two allowed wordings on its own, commented "เลือก รวมได้ 5 เพราะสั้นและชัด", and completed the card with result `รวมได้ 5`. The card reads back as done. | Its fifth request (the final reply) hit the 32-request ceiling, so the post-turn goal judge never ran |

## After the owner raised the ceiling to 48

| Card | Source | Requests | Result |
| --- | --- | --- | --- |
| t_280a5933 | v0.8.40 kit | 3 | Stopped when the Captain checked `2+3` with `python3`, which the fixture policy forbade at the time. The fixture now allows read-only goal checks and pure arithmetic checks. |
| t_8ff2d400 | v0.8.40 kit | 8 | The card was done, and the **first live goal-judge verdict** ran: `continue`, because "the response claims completion but provides no concrete tool-result evidence". The loop then spent another turn. |
| t_c93184b4 | v0.8.42 candidate | 5 | With the kick fix, the first turn saw its contract. The Captain read the card back and replied with evidence (`status: "done"`, `result: "รวมได้ 5"`, the comment). The judge call would have been request 49, so it was refused at the 48 ceiling. |

The t_8ff2d400 judge was right to reject the reply. Hermes caused the extra round:
`/goal` started the first turn with only the headline, so the turn never saw the
Verification criterion or the rule to show evidence. Only the continuation prompt
carried that rule. v0.8.42 gives the first turn the same contract and evidence rule.

## After the owner raised the ceiling to 56

| Card | Source | Requests | Result |
| --- | --- | --- | --- |
| t_d1f9e350 | v0.8.43 kit | 8 | Card done, with evidence in the reply. The live judge answered `continue` because the reply showed a readback, while the goal text said "do not reread the card, call no other tools". The contract's Verification line required that readback. The judge applied the explicit constraint correctly. The test input contradicted itself; Hermes did not misbehave. The second judge call was refused at the 56 ceiling. |

Lesson for goal authors: keep the goal text and the Verification line consistent. A
judge treats an explicit prohibition as binding even when the contract asks for the
opposite.

## What remains unproven

- A live `done` verdict and terminal goal state. Two live judge verdicts (t_8ff2d400, t_d1f9e350) were `continue`, each for a reason the judge stated correctly. A consistent test prompt is ready for the next quota.
- Live reuse of the v0.8.37 judge memo. The two recorded judge verdicts do not
  establish that an identical-input repeat returned a stored verdict without
  another judge call.
- Behaviour in a production Gateway or a running Desktop, which stay closed by owner
  instruction.

The Captain re-read the card after completing it. That verification step cost one
request and was reasonable under the goal-driven skill. A tighter prompt can skip it
when the completion result is already authoritative.
