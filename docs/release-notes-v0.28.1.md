# Hermes Legion v0.28.1 — Readable status on bot cards

## What you will notice

The Bots screen keeps each card's status above its action buttons. Previously,
"No active work reported" could be squeezed into four short lines beside
Open Screen, Edit profile and Open chat, even in a wide window. The status now
has the card's full content width and the same buttons sit underneath.

Apply the consolidated source kit to its pinned upstream base and rebuild
Desktop through the supported path. No dependency, preference or data
migration is required. This companion kit does not install a rebuilt app.
This is a layout bug fix, so it uses a patch version.

## Native Mac acceptance

An isolated Local-only Mac app reproduced the four-line status at the normal
260-pixel minimum card width. The corrected renderer displayed the complete
status on one line at the same wide window size and at a narrow window size.
Before/after wide screenshots measured 3010 by 1776 pixels; the narrow check
measured 1714 by 2018 pixels. These raster sizes are not CSS viewport sizes.
An empty search showed its existing no-results message; clearing it restored
the card. The walkthrough also checked Manage team and New bot -> Cancel;
the entered name created no profile. No chat was opened or prompt submitted.

Both native cohorts passed their 60-second gates with zero SSH attempts or
executions and at most four sampled Hermes processes. Their processes stopped,
gateways closed, DesktopSSH was zero, and each original trial bundle was
restored with its strict signature verified. Local configuration bytes stayed
exact. Owner data and other machines were untouched. Private screenshots and
receipts remain outside the release, referenced by the local work report.

## Checks and limits

Only two CSS utilities change in the existing workspace component. Four existing
workspace UI tests, renderer types and the renderer build pass. The visual
regression is demonstrated on the native app; no DOM-class mirror test was
added for this CSS-only fix. Scoped lint has the exact same 32 errors and 15
warnings on the pre-fix file and the corrected file; none were introduced.
The changed patch section applies, matches its hash and reverses to the pinned
base; unrelated source sections and the existing test selection are retained.

Repeat the check in isolated Local mode: open Bots, inspect the inactive
card's status and all three actions, narrow the window, search for a missing
bot, then clear the search. Compare with the pre-fix renderer at the same size.

Live worker activity, worker lifecycle, provider use, daily-app adoption and
Linux parity were not tested. Bot monitoring and the wider Config/Bots/Chat
walkthrough remain incomplete. No RAM or model-usage saving is claimed.
