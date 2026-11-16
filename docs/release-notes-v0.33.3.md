# Hermes Legion v0.33.3 — Scope Settings config actions

## What you will notice

Export and Reset now use the profile shown under **Applies to** in Settings.
Previously, displaying one profile while another was active could export the
other profile or reset its settings. Each action keeps the profile and connection
captured when it started, including while waiting for confirmation or a read.
Reset names the target profile before confirmation. Cancel makes no defaults
request or write, and a refused save reports failure.

Apply the source kit and rebuild Desktop. This source bug-fix release does not
install a rebuilt daily app. Reset retains native merge semantics: extra config
keys are preserved; this is not a complete factory wipe.

## Implementation and checks

The Actions component reuses the existing config-owner resolver and displayed
request scope. The defaults helper accepts an optional existing scope while
preserving no-argument behavior and read-origin binding. No backend, schema,
locale, dependency, new state or polling behavior is added.

Nine new cases include eight failures before the fix and an ambient-defaults
control. The initial selection has 9 passes and 8 failures; the final nearest
selection passes 60 tests. Coverage includes exported Blob contents, changes
during export/defaults reads and confirmation, named Cancel without I/O,
read-origin binding, and refused versus successful Reset acknowledgement.
Scoped lint, renderer types and build pass. A test-only type-import lint error
was corrected; the unrelated existing dynamic-import build warning remains.
Four changed source/test sections pass pinned-base apply/hash/reverse. One
existing upstream route-binding test joins the kit and explicit Desktop selection,
bringing the kit to 1086 targets; unrelated patch sections remain unchanged.

Native Mac proof uses fresh Local-only homes with two distinct configurations.
With ambient scope-b at 4222 and Settings displaying default at 3111, the original
renderer exports 4222/owner B; the rebuilt renderer exports 3111/owner A through
the same native Save dialog. A fresh rebuilt launch names default in the Reset
dialog and Cancel returns to Settings. Both config files remain byte exact and
both session stores are empty. No Send or inference occurs.

The export cohort reaches its watchdog deadline after the export proof and before
Reset. An inactive UI-state read relaunches the restored task trial; its two
processes are identified and stopped. A separate fresh cohort completes the named
Reset/Cancel journey and closes normally. The baseline and both rebuilt cohorts
pass actual 60-second SSH-zero gates and sample at most four Hermes processes.
Observer-inclusive RSS maxima are 937,672,704, 948,797,440 and 888,340,480 bytes;
these are bounded samples, not continuous peaks or memory-saving results. All
owned processes and gateway ports end; config bytes/modes and the original
313-entry trial bundle with strict signature are restored. Private evidence and
rollback copies remain outside the public kit.

Native Reset is never confirmed: the real defaults include timer policy, which
this journey must preserve. Actual Reset routing, races and refused writes have
offline coverage only. Daily-app adoption, remote/ai/Linux acceptance and the full
Settings walkthrough remain open. Owner data, ESTOP, pauses and timers are untouched.
