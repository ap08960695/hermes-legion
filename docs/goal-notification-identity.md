# Count goal work at its actual notification destination

A Gateway goal is stored under a durable history session ID. Kanban tool
subscriptions instead use the current platform, chat destination, thread and
owning profile. These identifiers are not interchangeable: a Slack channel or
hosted local room can differ from its history ID. The old judge count therefore
missed followed work, while coincidentally equal chat/history IDs could include
another thread, platform or profile.

The Gateway now supplies its canonical notification destination to the native
read-only task counter. A pinned routing identity supplies the runtime owner
before the legacy source/profile fallback. Destination values remain bound SQL
parameters. Explicitly owned rows match only that profile; legacy unowned rows
remain eligible only at the exact destination. Incomplete destinations count as
zero rather than widening the query. This is an advisory count, not delivery or
completion authority, and it does not change notification routing.

The target is passed at evaluation time, never persisted as a second routing
registry or appended to a prompt log. Direct CLI/TUI GoalManager callers retain
their existing history-session count. Existing fleet discovery, worker/delegation
and explicit database pins, active statuses, WAL visibility, missing/legacy DB
handling and parked-goal quiescence remain intact. No conversation contents are
read to recover an identifier.

## Verification and limits

The real Gateway goal hook originally failed four route cases while the legacy
control passed. The final goal/board/notifier/multiplex selection passes 373 cases
in 35 files, with zero failures or file retries. Scoped code-health has no new
findings. Linux and macOS production interpreters each pass 12 installed-source
checks, including actual Gateway post-turn hooks for synthetic local and Slack
sources against real isolated SQLite. Only the judge decision and UI notice are
controlled; no Slack transport, external provider or real model is called. The
judge receives one own pending task, excludes neighboring routes and does not
run again while the goal remains parked.

Both hosts apply, reverse and reapply the 752-path public kit. Installed parity
has 751 exact files plus one pre-existing comment-only Python-AST-equivalent tool
difference on each host, zero missing files. Linux Gateway adopts source during
confirmed idle; the original macOS Gateway remains stopped. Existing workers,
profiles, models, quotas, effort ceilings, credentials, emergency stops and
fallback gates are preserved. No Desktop renderer rebuild was needed.

These checks establish identity/count plumbing and native parked-state behavior.
They do not establish original-session adoption, a continuous autonomous bot
graph, measured production usage savings or cross-bot cache causality. Earlier
broader auxiliary tests still have 20 inherited failures, documented separately;
this selection is not a globally green upstream suite. Overlapping historical
selections are not summed.
