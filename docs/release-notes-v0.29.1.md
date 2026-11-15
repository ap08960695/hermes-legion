# Hermes Legion v0.29.1 — Keep bot edits after a failed save

## What you will notice

If **Bots → Edit profile → Save** cannot save a description, appearance or
advanced section, the editor stays open with your draft. The existing error
remains visible and Save becomes available again. A failed description update
no longer also reports that the profile was successfully updated.

Correct the draft or retry explicitly. Successfully written sections may
already be saved; this is not a transaction or rollback. Cancel still closes
the editor. The existing older-gateway appearance fallback remains supported.
No automatic retry, writer, connection, model call or dependency is added.

Apply the consolidated source kit to its pinned upstream base and rebuild
Desktop through its supported build path. This companion release does not
replace the owner's installed app or migrate stored profiles.

## Native Local acceptance

A synthetic bot was created through the native Mac interface with its optional
introduction switched off. On the previous renderer, the trial process guard
rejected a description write. The editor closed, displayed both an error and
success, and reopening showed that the revised description was lost although
the title had been saved.

With the corrected renderer and the same guard, the failed save kept both
edited fields visible and Save enabled. There was no success notification for
that failed attempt. Restoring the description to its saved value allowed a
title-only Save to close successfully; reopening confirmed the saved title.
The unchanged New group chat → Cancel flow also returned to Bots without
creating a group. Before/after images measured 3010 by 1776 pixels.

The guard deliberately prevented the description subprocess from running.
This verifies UI handling of a rejected write, not successful native description
execution. No introduction, prompt submission, inference or worker ran.
Both completed native cohorts passed 60-second gates with zero SSH attempts
or executions and at most four sampled Hermes processes. Owned processes
stopped, gateway ports closed, and the original trial bundle and task config
were restored. Owner data and other machines were untouched. Private images
and receipts remain outside the source release in the local work report.

## Regression and limits

Five rendered component cases cover rejected description writes and explicit
successful retry, appearance failure, two advanced failure responses, and the
older-gateway appearance fallback. Four failed on premature close before the
fix; all five pass after it. Renderer typecheck and build pass. Scoped lint
reports no findings in the two changed files. The two changed patch sections
apply, match their hashes and reverse to the pinned base; unrelated sections
are retained. The new regression joins the existing desktop test selection.

Successful native description writes, group creation and membership changes,
real worker lifecycle, owner-app adoption and Linux parity remain unverified.
Partial writes remain possible; no RAM or model-usage saving is claimed.
