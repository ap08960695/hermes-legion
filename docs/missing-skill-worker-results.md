# Missing-skill worker results

A Kanban worker whose requested skills could not be loaded used to raise before
its first model turn. The managed owner then reported an unknown execution,
leaving a known setup failure without an actionable result on the card.

The worker now returns a structured failed result with the unresolved skill
names and a request to install or enable them in the assigned profile before
retrying. The owner settles the admission as terminal/failed, and the existing
worker exit and dispatcher failure policy handle the card. No model request is
needed to diagnose the missing preload.

The existing partial-loading policy is preserved: if at least one requested
skill loads, the normal turn still receives the skill prompt and missing-skill
notice. Skill discovery, owner authority, retry limits and unexpected-crash
handling are unchanged. This is not a new automatic skill installer.

## Verification for v0.8.20

- A regression failed on the previous source; the new missing-skill and three
  normal/partial-loading cases pass with real temporary skill and board stores.
- 90 related cases pass across eight files, including the native loopback
  dispatcher lifecycle. A macOS-only case in an adjacent selection is skipped
  on Linux; it is not counted as passed.
- Four native offline cases pass on each installed host, including the managed
  result projection and durable worker receipt. All 958 source targets match
  the release manifest on Linux and macOS.
- A fresh simple review card with its required review skill deliberately absent
  makes zero model requests. Its admission settles terminal/failed, its worker
  log names the missing skill, and a no-spawn dispatcher sweep applies the
  fixture's no-retry policy and blocks the card. The existing run classification
  remains `crashed` for exit code 1; the typed admission reason is
  `kanban_skills_unavailable`.
- The earlier failed fixture and its unknown admission are retained; neither it
  nor any production card was replayed. Production queue activation and GPU use
  remain disabled. This Python change does not rebuild or revalidate Desktop UI.

Separately, the previous release's revision handoff was verified with a fresh
simple review card: three successful model requests, no request after
`kanban_request_changes`, and correct return to the original implementer without
starting the implementation follow-up. This is one bounded reviewer run, not
acceptance of a complete autonomous development cycle.
