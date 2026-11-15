# Hermes Legion v0.28.0 — Settings actions keep your place

## What you will notice

- A named **Actions** button groups **Export config**, **Import config** and
  **Reset to defaults**, in both wide and narrow Settings layouts.
- After cancelling reset, focus returns to Actions. Press Return to reopen
  its menu, or Escape to dismiss the menu and keep working.
- Your unsent Local draft stays in Chat when you open Settings for the first
  time after startup, close it, or cancel these Settings dialogs.

These related changes form one Settings capability set. Apply the consolidated
source kit to its pinned upstream base and rebuild Desktop through the supported
build path. This companion release does not replace the owner's installed app
or modify their configuration. No dependency, lockfile or new preference is needed.

## Native Mac acceptance

The corrected renderer ran in the existing native Mac trial app with a fresh
Local-only home and app-data directory. A Thai/English draft was entered before
the first Settings visit, then checked on return and after the cancellation
flows. Its accessibility value, including its trailing newline, remained exact.
Actual screenshots agreed with the accessibility state.

Named actions, Export save Cancel, Import chooser Cancel, and Reset Cancel were
checked. Settled focus returned to Actions; Return reopened the menu at both
window widths. Native screenshots measured 3010 and 1714 pixels wide. Config
bytes stayed exact. No Send, completed export/import or destructive reset ran.

The launch passed a 60-second gate with zero SSH attempts/executions. All owned
processes stopped; the gateway closed, DesktopSSH was zero, and the original
trial bundle was restored and its strict signature verified. Other machines
and the owner's daily Hermes data were untouched. Private before/after images
and receipts are referenced by the local work report, outside this release.

## Regression and scope

A first-visit route regression reproduced the loss when legacy Local mode was
published after the composer mounted. The mode signal now invalidates the
owner hook, whose external registry lookup is exempt from compiler memoization.
The existing canonical Local fallback and explicit/runtime/known-owner ladder
remain; request tags and persistence boundaries keep their behavior.

Three route contracts and the nearest six-file selection pass: 58 cases total,
including seven Settings Actions/confirmation cases and remote-owner isolation.
Scoped lint, renderer types and the renderer build pass. The nine affected
patch sections apply, match their manifest hashes and reverse to the pinned
base. Unchanged source targets were not rechecked.

To repeat the native check: type an unsent draft before opening Settings;
open and close Settings; cancel Export, Import and Reset; confirm the draft
and configuration remain; repeat Cancel and Return at a narrow window width.
Use isolated data and Local-only connection guards for this check.

Older drafts already saved under a different owner key are not migrated.
Daily-app adoption, remote-host behavior, completed import/destructive reset,
Linux UI parity and the full native suite remain untested. No production RAM,
latency, cache-hit or model-usage saving is claimed by this Settings release.
