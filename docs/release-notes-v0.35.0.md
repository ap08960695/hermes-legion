# Hermes Legion v0.35.0 — Desktop Characters

## What you will notice

- Turn **Characters** on in the Desktop title bar from any main screen. Pick
  **Small**, **Medium** or **Large** to resize the scene immediately. On macOS,
  the **Characters** menu bar item offers the same settings while Desktop is
  minimized. Each connection and profile remembers its choice.
- Active bots and workers appear on a transparent overlay. Characters wander at
  different speeds and pause on their own. Drag and release one to see it fall
  back to the floor. Task handoffs, completions, failures and requests for input
  can show a short cue. Reduce Motion quiets movement and transitions.
- Select an active character for recent output or **Open in Hermes** to return to
  its conversation. Supported Local deliveries can show text, Markdown or CSV
  source, images, and the first page of an eligible PDF. Preview controls stay
  reachable in short windows and can be used from the keyboard.
- The standalone Pets window and its old controls are retired. When Desktop
  first reads a profile's settings successfully, its old enabled flag and scale
  seed Characters settings if no choice is saved. Installed packs remain
  available under **Bots → Edit profile → Character**. Six original example packs
  and the [creator guide](character-pack.md) are included.
- A temporary sprite read error can be retried with **Refresh Characters** in
  the macOS menu bar or **Refresh** in Bots, including Monitor. Background
  refreshes continue to observe bot activity without retrying the failed atlas.
  Installed sprites use the same checked bytes for validation and display.

## Other changes in this batch

- Common chat and tab creation now have one entry in the navigation rail.
  Wide-layout switching also lives in the rail. Compact and standalone controls
  remain available. Bots centralizes bot and group creation and keeps **New
  section** in **Manage team**. [Bots before](images/ui-cleanup-bots-before.webp) ·
  [Bots after](images/ui-cleanup-bots-after.webp) · [Layout before](images/ui-cleanup-layout-before.webp) ·
  [Layout after](images/ui-cleanup-layout-after.webp).
- A rapid PDF switch keeps the latest eligible preview, rejected file previews
  release their file handles, and saved answer cards only load external images
  when requested for that card.
- Late Captain Goal results cannot override Stop or attach to a later run.
  Conflicting Goal readbacks are flagged for review while the draft stays
  available. Local gateway startup keeps its deadline when another launcher
  has the slot and reports whether the new root is ready or parked.

## Mac evidence

The screenshots use a synthetic Local Electron fixture. After an assigned
sprite read timed out, the minimized background refresh updated the roster and
left the sprite alone. Invoking the native **Refresh Characters** menu action
retried the read and restored the bot and its worker, which shared one atlas.
The screenshots show the fixture's published scene. [Before](images/characters-before-manual-refresh.webp) ·
[After](images/characters-after-manual-refresh.webp).

In an earlier controlled five-character Mac run, steady-state overhead was
**68.6–71 MiB of summed process RSS** and **1.47–1.73 CPU percentage points**
over the publisher-only baseline. The lead accepted this against the
steady-state target. The first walking sample was around **2.3 CPU points**,
mostly WindowServer. These measurements belong to that fixture and do not
include the entire Hermes service or remeasure the final candidate.
[Measurement method and limits](design-bot-characters.md#measure-first-presented-sprites-separately-from-walking-cpu).

Separate isolated Mac Local runs established a cold launch and restart with zero
Desktop SSH links. Local process and mock transport checks cover compatible
master reuse, helper admission and cleanup on transport loss, and reconnect
backoff. Authenticated SSH fan-out and the real ai backend still require separate
acceptance. [Desktop SSH evidence and limits](desktop-ssh-resources.md).

## Adopt the source kit

Apply the [consolidated stable source kit](stable-full-kit.md) to the pinned
upstream source and rebuild Desktop in a separate trial using the
[Mac install and update guide](macos-install-update.md). Use an isolated trial
home with Local as its only connection. [Rollback guide](installation-and-rollback.md).

Linux includes an X11/XWayland input-region adapter. Earlier GNOME and COSMIC
fixtures showed click-through and animation over XWayland. Those samples
exceeded the Mac resource target, and the final candidate still needs a Linux
compositor run. Native Wayland leaves Characters unavailable. Windows and other
platforms without the required directory descriptor APIs report installed
character sprites unavailable. [Linux setup and evidence](linux-desktop-pets.md).

This source packet is prepared for owner approval. Installed-app adoption,
production timeout and reconnect behavior, and ai operation remain unverified.
