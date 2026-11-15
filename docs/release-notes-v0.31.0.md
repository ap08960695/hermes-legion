# Hermes Legion v0.31.0 — Name and reopen Local group chats

## What you will notice

Create a Local group with two to six bots, cancel a draft without making a room,
and reopen a saved room through **Back → Manage team**. Those existing creation
steps now have a companion **Rename** control inside the room. Change its name
without replacing the room or its members. The header and open tab update after
confirmation, and the current unsent message stays in the composer.

This capability set combines the earlier creation/reopen walkthrough with the
new naming control. Apply the source kit and rebuild Desktop, including its SDK.
The installed daily app is not replaced by this source release.

## Behavior and compatibility

Rename is offered only when the owning gateway advertises `groups.rename`.
The request keeps the original connection, profile and canonical room ID. The
existing gateway performs its atomic name/event write; Desktop confirms the same
room and requested name through its existing state/log refresh before closing.
Blank names cannot be saved, pending controls prevent duplicate submits, and an
error keeps the name draft available. An unchanged explicit retry while the edit
remains open reuses its event ID; there is no automatic write retry. A different
readback is not reported as success. This is not a concurrent-edit lock.

The SDK updates only an existing workspace contribution's title, keeping its
render callback, data and close disposer. It neither opens a missing pane nor
moves focus. An older Desktop SDK keeps its previous caption behavior until the
room is reopened. An older gateway without rename remains usable without this
control. There is one capability read per mounted room, no new polling timer.

No backend code, schema, model route, prompt, cache context, quota or dependency
changes. Canonical room membership is still read-only in this view; legacy bot
group metadata is a separate feature. No message or model call is needed to rename.

## Verification

Two new missing-control cases fail on the original renderer. The first native
candidate confirmed the name and retained the unsent message, but exposed a stale
tab caption. Two further contract failures protect the caption path; final nearest
checks pass 63 tests across four files. They cover cancel/blank validation, lost
acknowledgment and same-intent retry, mismatched readback, original authority,
room switching, old capabilities, draft retention and caption updates without
replacing a workspace render callback or resurrecting a closed pane.

Scoped lint has no new diagnostics; two existing ref-cleanup warnings remain.
Types and renderer build pass, with the inherited dynamic-import warning. Seven
changed sections apply/hash/reverse on the pinned upstream base; five newly
carried paths bring the source kit to 1085 targets. Unchanged suites and the full
source inventory are not repeated. Full native suite, daily-app adoption, Linux
parity, sibling/legacy live monitoring and production efficiency remain open.

Native Local acceptance used a fresh isolated home and the real UI to create a
helper with introduction off, create a two-member canonical room, cancel a blank
rename and save a Thai/English name. The existing unsent message stayed intact.
Back → Manage team reopened the same room. After every process stopped and the
original trial bundle was restored, a final build reopened the SAME home; the
saved name and members remained. No database was seeded or copied between launches.

A second deliberate rename on the final build updated both header and main-tab
caption immediately and kept the current unsent message. Independent read-only
SQLite snapshots retained one room ID, authority and exact member targets. Cancel
changed nothing; the two different saved names added exactly two native rename
events. Both profile configs stayed identical during each rename. Sessions,
messages and driver tasks remained zero; populated chat history and model execution
were not exercised. Native transport/error and old-capability cases have unit proof.

The before reference is the earlier native group view with the unchanged original
workspace. Private images include r96-15-room-reopened.jpg,
r103-19-rename-saved.jpg (first candidate's stale tab),
r103-24-restart-room-retained.jpg and r103-27-caption-and-draft-updated.jpg.
Both launches passed actual 60-second Local gates with zero SSH attempts or
executions and at most four sampled Hermes processes. First/final runs collected
2490/1574 samples, with observer-inclusive RSS maxima of 940,228,608/884,637,696
bytes. These are samples, not continuous peaks, physical RAM or production savings.

All owned identities ended, ports closed, and the original 313-entry trial bundle,
strict signature and config baseline were restored. The second startup's normal
native multiplex flag was separately checked and backed up before UI use. The
second automatic rollback refused an already retained first diagnostic backup;
it completed after that verified backup was preserved under a distinct name.
No backup was overwritten. The owner's app/data, other hosts and stops stayed
untouched. The source kit still needs adoption through a Desktop rebuild.
