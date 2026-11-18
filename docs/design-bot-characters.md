# Bot characters on screen

## Outcome and existing parts

Show active bots as original or user-owned characters, with short event-driven
status and interactions, latest-output preview and canonical chat/report opening.
Idle characters hide or sleep; animation never implies a task started or passed.
Reuse Bot Monitor/delegation state, native pet storage/atlas decoding, PetSprite,
PetBubble and the existing gateway-less overlay IPC/window. One shared renderer,
not one process/window per bot. Keep account/profile/session ownership and Stop
authority; no model calls for animation or invented progress.

## Approaches

Extend the current pet/overlay path: chosen maintainer approach, least duplicate
state/rendering. Independent windows per bot multiply baseline memory and violate
the one-renderer goal. A separate animation application duplicates lifecycle and
chat-opening authority. Keep the existing petdex/legacy renderer fallbacks.

## First completed slice: creator state preview

Existing `hermes pets show --cycle --once` omits run/wave/jump because the atlas
row names differ from canonical activity names. It also repeats a full sequence
as many times as there are states. The working patch cycles all seven canonical
PetState values and stops after one completed sequence; explicit-state precedence,
renderer alias/legacy fallback and cursor restoration are preserved. This fixes
existing author tooling without another command, dependency, process or setting.
Eight focused source tests and the real source CLI through an isolated native
PTY pass with a synthetic atlas. This is terminal preview, not the new desktop
overlay. [Evidence and limits](verification.md#pet-creator-preview--native-terminal-acceptance-unreleased).

## Local atlas validation: creator tooling

`hermes pets validate ./spritesheet.png` checks an existing local generated
atlas without installing it or changing pet settings. Reuse the generation
pipeline's `validate_atlas`; a separate pack parser or duplicate pixel validator
would create a second contract. The existing CLI table owns dispatch/help.
Accept static PNG/WebP, at most 16 MiB, with the native 1536x1872 geometry checked
before pixel decoding. Report populated rows, missing-state warnings and the
shared empty/collapse/outlier/transparent-RGB errors. Exit 0 permits warnings;
exit 1 reports an unreadable, unsupported or invalid atlas.

The real CLI parser/Pillow regression and isolated source CLI cover success,
failure and help. No installation, model request or network is needed. This
IMAGE path checks the current generated atlas only. Folder metadata and a
starter guide are covered below; animation budgets, archives, install/assign
and the complete creator capability remain open.

## Folder-pack creator lint: completed development slice

`pets validate DIRECTORY` now reads versioned native-atlas metadata (name, author,
licence and one confined static sheet) and reuses the image validator. Metadata
and opened files are bounded; invalid schemas, control text, symlinks, special
files and unsupported formats fail. The native idle row is required; absent
other rows remain visible warnings. IMAGE behavior stays compatible.

The [creator guide](character-pack.md) includes a blank manifest and a local
recipe for the original CC0 Lanternling example, with every native row filled.
Real parser/Pillow cases and actual source CLI generation/folder/image/help/
invalid-template/no-overwrite checks pass. No installer or profile change.

FPS, anchor and custom state mappings are deliberately absent until a runtime
consumes them; unknown fields fail rather than imply support. Lint does not
establish installability, playability, licence ownership or resource budgets.
ZIP, GIF/APNG/Lottie, bot assignment and extended event interactions remain
open. The native-atlas creator skill and terminal preview are covered below.

## Pre-install pack preview: completed terminal slice

`pets show --pack DIRECTORY` reuses the existing terminal renderer and state
loop with a private snapshot of exact validated bytes. It bypasses installed-pet
and pet-config resolution; conflicting slug+pack fails early.
The shared animation helper preserves installed preview and cursor restoration;
temporary snapshots clean up on success/error/CtrlC. Missing requested frames
fail before drawing. The validator report API stays unchanged while its loader
also exposes exact checked bytes to the preview. This is current native-atlas
terminal preview, not Desktop, installation or the full interaction contract.
Sixteen new parser/Pillow cases, six installed-preview cases and fifty validation
cases pass. Native PTYs confirm all seven aliases, finite once behavior and
Ctrl+C cleanup. The original example emits changing terminal frames; physical
screen/graphics appearance and Desktop resource acceptance are not established.

## Local pack import: completed Mac development slice

`pets import DIRECTORY SLUG` copies exact validated bytes into the existing
profile pet store and retains creator metadata/licence. Canonical `pet.json`
keeps list/show/select/remove compatibility; no new creator enum or automatic
selection. Strict canonical slugs and native no-replace publication preserve any
existing target, including an empty directory or symlink.

A private container/payload staging layout stays invisible to existing readers.
All files close before one publication operation; cleanup touches only that
owned container. Cleanup warnings cannot turn a committed import into failure
or hide the primary error. The source folder and prior entries/settings remain.
Atomic visibility does not promise crash durability or hostile store-parent
mutation safety; no unsafe rename fallback. Primary contracts:
[Linux renameat2](https://man7.org/linux/man-pages/man2/rename.2.html),
[Windows os.rename](https://docs.python.org/3.14/library/os.html#os.rename);
Darwin `renamex_np`/`RENAME_EXCL=4` was checked in the installed SDK.

Native Mac filesystem regressions and the actual isolated CLI lifecycle pass,
including races, I/O faults, original metadata, non-selection and restoration.
Linux/Windows code paths await native acceptance. Per-bot assignment, extended
formats/events and Desktop/resource proof remain open.

## Native-atlas creator skill: completed guidance slice

The self-contained [character-pack-creator skill](../skills/character-pack-creator/SKILL.md)
turns an authorized description/reference into a state plan, owned/original frames,
exact atlas assembly with the existing composer, lint and terminal preview.
It carries the current geometry/schema so an installed one-file copy works
without the Legion checkout. Image tools remain optional and within existing
rights/allowance. Provenance and actual permission terms stay explicit.

Creation does not imply import/selection. Requested import uses the existing
no-replace command and profile scope; selection stays a separate global action.
No new provider, generator, dependency, configuration or renderer. Native
skill discovery/read, the exact embedded assembly recipe (including existing
output/wrong-frame refusal) and actual isolated CLI workflow are verified.
This is deterministic fixture evidence; autonomous artistry, image-tool behavior,
Desktop characters and full interaction/format/resource acceptance are unproved.

## Active-character overlay preview: offline source step

The working source adds **Show bot characters** in Monitor. A loaded, enabled
pet is required. It previews at most five current source-qualified bot/worker
observations in the existing transparent overlay, using that pet's sheet and
PetSprite. Bounded name/source/latest signal and reported step remain plain
text. Current work uses the run pose; reported bot attention uses failed.
It does not infer reasoning, human waiting, completion or progress percentages.

The existing plugin pet door now exposes a scoped replaceable display publisher.
One preview owns the shared overlay; a superseded/disposed publisher cannot
revive or clear the newer snapshot. Identities include plugin, source and stable
bot/worker identity; no worker array-index fallback. Empty replacements cross
IPC. Monitor error/stale/retained/unqualified observations are excluded. The
15-second lease is anchored to the source snapshot time, with independent
receiver expiry. Unmount/unload clears the publisher; stopping restores the
previous mascot mode. No extra polling, model, gateway or per-actor OS window.

The read-only actor stage replaces the global mascot composer while previewing.
It uses short enter/exit transitions and a 15 fps sprite ceiling; reduced motion
uses static poses which still reflect semantic state changes. Native IPC gates
the stage on main-window hide/minimize and lock/suspend, preserves a known lock
through resume, and retires retained state/listeners when the overlay closes.
Normal mascot behavior has regression coverage. All nine Monitor locales have
the new control and its installed-pet/read-only scope hint.

Offline tests/types/lint and renderer/changed-IPC builds pass. Two earlier native
control renderers failed sandbox initialization before overlay loading. A fresh
fixture using the established Chromium sandbox and guarded native launch path
loaded the control renderer, then reached production overlay loading. Its
network guard refused a Google theme-font stylesheet before connection; the
trial closed and remains failed. This does not establish the cause of the two
earlier failures.

The shared theme painter now skips its font-link injection only for exact
`win=overlay`, covering cold boot and later theme paints. Palette, typography
and local font stacks remain; normal main/HUD/secondary windows still load and
deduplicate theme fonts. Suppressed fonts do not poison that cache. Four new
regression cases and 23 neighboring theme cases pass, as do scoped lint,
renderer types and the fixed renderer build. This guards the theme-font branch,
not every custom CSS or asset URL. A fresh contained native fixture subsequently
reached Local60 with the fixed production artifact, zero Desktop SSH and no
font/network refusal. CUA paired screenshots show only its control window's
normal-to-actors button transition. Overlay receiver telemetry stayed null;
actors, motion and mascot restoration are unproved. Observation admission
refused insufficient remaining reserve before the next action and closed the
trial permanently. Raw phase measurements cannot establish character CPU/RAM.
The fixture also lost console error text by using an obsolete callback shape;
a prepared offline repair preserves full event details but has not been run
natively in that round. A later diagnostic captured the missing fixture method
`onPreviewFileChanged`: production preload provides the passive event listener,
while the isolated host omitted it. Reusing that real subscription fixes the
fixture's bootstrap: a distinct host receives a run-bound overlay ACK and
reaches Local60 with unchanged renderer/native IPC artifacts. This identifies a
fixture defect; no product-source fix is inferred. Its app-filtered window
inventory lists control only, so overlay images, five actors, motion and resource
acceptance remain open. The later expanded visual attempt also ended at its
deadline. A subsequent relative-entry fixture reaches Local60 with a real native panel
identifier, but its exact app/window capture receives Screen Recording
`PERM_DENIED`. The trial closes without input or retries; no actor image, motion,
restoration or CPU/RAM acceptance follows. No permission settings are changed.
No completed character acceptance is claimed. [Evidence and limits](verification.md#bot-character-overlay-preview--offline-source-step-unreleased).

Persistent all-bot tracking, character interactions/open controls, per-bot packs,
display-only sleep handling and actual visibility/reduced-motion/resource
acceptance remain open. No version or release for this development step, and
no claim that the five-character CPU/RAM target is met.

## Pet picker source isolation: completed offline prerequisite

Before assigning imported packs to individual bots, the existing avatar Pet
picker must read the intended bot's library. It previously used the active
gateway and a slug-only thumbnail cache even when Edit Profile targeted another
source/profile or New Bot targeted another connection.

Both dialogs now supply a required captured source/request pair. Edit Profile
uses the existing owner-aware bot router (including backend profile aliases and
removed-owner refusal); New Bot pins the chosen/default backend descriptor when
supported. Legacy unscoped behavior remains available. Gallery query identity and
the shared120entry thumbnail LRU include source identity; thumbnails also include
slug/URL. A source change remounts the gallery, and older selection callbacks
cannot overwrite a newer pick, removal or another source's draft.

Mounted component/caller tests, renderer types/build and scoped lint comparison
verify this source fix offline. Native RPC functionality was observed in two
profiles, but isolation failed: an import-time updater probed a local repository
outside the fixture home. A separate strict successor stopped before Python
startup because its interpreter runtime was under the denied tree. Both native
attempts remain unaccepted; no third launch or boundary weakening. This is not
native UI, per-bot animated pack assignment, or character/resource acceptance.

The subsequent workspace-runtime preflight passes strict owner-read, child and
exec/protocol controls. Round219's metadata-audit failure remains failed. A fresh
Round220 actual pytest now passes profile-specific gallery/thumb and missing-
profile behavior under the same OS fences. A finite seven-command local Git
metadata allowance closes before RPC; eleven negative controls pass. Configs and
pack bytes stay unchanged, no global selection or unexpected activity occurs.
This completes contained native-handler acceptance only; Desktop routing,
per-bot assignment and character/resource acceptance remain open. [Boundary
evidence](native-checks-and-test-memory.md#profile-bound-pet-rpc--contained-mac-acceptance).

## Remaining capability work

The first overlay slice must map actual active bots/workers to bounded actors in
one window, with task/status and enter/exit/work/think/wait/error/done animation.
Add short, skippable handoff/result/review/retry/collaboration/escalation/group-done
interactions only from real events. Reuse canonical open/Stop/Pause, latest-output
preview and safe artifact/viewer/platform-open APIs; never execute artifacts.

Add on/off, edge/corner/multi-monitor placement, maximum actors, reduced motion,
DND and sounds off by default. Movement/idle loops remain active while visible;
static poses in reduced motion. Cap animation15–24fps, lower idle rate, pause fully
when screen locked/off or Hermes hidden/minimized. Measure before/after with five
actors on this Mac: target <=1–2% average CPU and <=60–80MB extra RSS. Report an
actual budget miss and trade-off before release; no budget claim from unit tests.

The draft native-atlas folder contract, metadata lint, original example recipe,
blank template and starter guide are now included. The full runtime format still
needs per-event animations and fallbacks, size/fps/anchor controls, and extended
formats. Native-atlas creator guidance, lint, terminal preview and Mac-tested
no-overwrite import are included. Reuse current stores and renderer
rather than introducing another atlas taxonomy. Only original/owned art; no
borrowed character designs or copied reference art.

Keep these items explicitly unimplemented until their source and native evidence
exist. Full capability release requires screenshots/short recording, real-event
acceptance and measured CPU/RAM. No source/runtime adoption into the owner app,
ai/otherhost access or permission changes; first adoption remains lead/owner-only.

## Per-bot installed characters — unreleased

Edit Profile gets a separate Character selector listing only that captured
profile's installed packs, plus Use default. Static avatar controls and legacy
local-only `pet` metadata keep their meaning. Save only a changed nullable
`character` slug through existing profile metadata/CAS; an untouched form never
reverts another window's assignment. New/unassigned bots inherit the existing
mascot. No download/install or global pet selection is part of assignment.

Use a scoped read-only `pet.sprite` RPC and the existing payload/PetSprite path.
Accept confined regular static PNG/WebP atlases, <=4MiB compressed and <=3million
pixels, native192x208 frames and up to9rows/9columns; reject path/symlink escape,
missing/oversized/animated packs. Enforce matching image-header dimensions,
geometry, frame counts and bounded base64 at the publisher before rendering.
This ceiling bounds input; actual five-character CPU/RAM remains a live gate.

Monitor resolves only its five current actors. Source/route/install/bot/slug key
all sprite identity; capture routes, request serially with an8s transport timeout,
retain at most5current identities and discard late evicted/reassigned replies.
Clear on stop/stale/unmount/source change; no automatic retry. An unassigned
actor uses the default atlas; assigned loading/error/missing actors stay hidden.
One source's bytes never substitute for another's identical slug. Overlay stays
gateway-less and uses existing preview expiry/IPC/shared renderer/reduced motion.

The separate installed dropdown reuses existing form and query behavior and
preserves the avatar Pet tab's static pictures and remote gallery semantics.
Tests cover persistence, source races, eviction, payload validation and overlay
rendering. The isolated Mac trial exercises real handlers and profile saves.
[Verification](verification.md#per-bot-characters--source-and-contained-mac-handlers-unreleased).

The canonical WebSocket processes these requests through its existing
interactive-ticket dispatch to shared handlers. The authority's profile fence
stays in place. Installed-only requests skip Petdex entirely. The full gallery
still fetches its public catalog when explicitly requested. Native screen
evidence, per-event interactions and five-character resource measurements
remain release conditions.

The [native overlay measurement](verification.md#five-character-packs--native-mac-overlay-measurement-unreleased)
now confirms five distinct moving atlases and mascot restoration in an isolated
Electron fixture. Preview adds 67.0 MiB over the existing mascot, but starting
the overlay adds too much versus the no-overlay baseline. Check the overlay's
renderer footprint before release. The full Edit Profile to Monitor walkthrough,
real bot events and production resource acceptance remain open.

Selecting the overlay route before importing the app bootstrap cuts its
reachable JavaScript from 9.22 to 3.68 MiB. The repeated Mac fixture kept
animation, mascot restoration and a fresh overlay open working. Five packs
still add 120.8 MiB in summed macOS physical footprint over no overlay, of
which the overlay renderer accounts for 96.2 MiB. The remaining release
budget needs work. [Current verification](verification.md#pet-overlay-boots-without-the-desktop-shell-unreleased).

Vite now groups the shared class-name helper with the renderer's UI
foundations. Opening the overlay avoids loading the Markdown vendor chunk.
The normal Markdown renderer still imports it.
[Import and Local smoke checks](verification.md#keep-the-markdown-vendor-chunk-off-the-overlay-boot-path).

The [five-mode Mac comparison](verification.md#where-the-pet-overlay-uses-memory-unreleased)
attributes 20.6 MiB to the blank overlay, 33.8 MiB to loading the production
overlay above blank and 58.1 MiB to the five-pack workload above the atlas-free
overlay. The largest measured step includes both sprite and presentation costs.
Use the fixed-geometry fixture to isolate decoded atlas and canvas residency.

[Matching five-pack runs](verification.md#keep-the-canvas-readback-hint-for-character-previews-unreleased)
showed that omitting the preview canvas readback hint added 152.4 MiB of
physical footprint with the same CPU use. Keep the hint under the current
Electron setup. Evaluate atlas residency separately before changing storage
or pixel fidelity.

A matched Mac run tested decoding just the active row of each character's
sprite sheet. Five moving characters used 32.8 MiB less physical footprint
than with full sheets, but used 0.23 percentage points more of one CPU core.
The candidate added 79.5 MiB and 2.96 CPU points over no overlay. Keep the
full-sheet path for now. The release budget still needs a change that reduces
rendering cost without losing movement or click-through.

A later Mac comparison fed pre-encoded running strips to the current
renderer. The strips saved 38.6 and 34.8 MiB in the two paired runs.
Full-size sheets with transparent unused rows had little effect by
comparison. The strips added 71.3 MiB and 2.43 CPU points
over no overlay. Treat these strips as a running-state fixture. A
product approach still needs state transitions and the CPU gate.
[Measurement method](verification.md#compare-resident-character-sprite-sheets).

A signed Local prototype drove five strip sprites from running to
waiting, failed and running again through owned overlay IPC. It
matched 120 canvas-frame hashes against full sheets. The mounted
canvas regression covers pending, superseded and failed image
loads. The strip prototype used 28.6 MiB less after the state
cycle. Product delivery still accepts full packs.
[Transition proof](verification.md#exercise-row-strip-transitions-in-the-character-overlay).

The signed Local producer prototype derived one-row PNGs at runtime
from the same five full sheets. Its overlay matched 120 drawn-frame
hashes. Across the app processes, strips used 4.3 MiB more after the
state cycle. The sampled capture peak dropped by 2.0 MiB. Producer
cropping took 20.5–33.1 ms per batch of five rows. The measured overhead
was 101.6 MiB and 3.98 CPU points. This is an unreleased
fixture measurement with synthetic PNG art.
[Runtime cropping proof](verification.md#measure-runtime-row-cropping-in-the-character-producer).

An isolated Mac import experiment encoded populated rows from the
validated bytes of three PNG and two lossless WebP sheets. It kept the
originals and capped their combined encoded size with the derivatives.
Five mixed-state characters matched 96 of 120 drawn frame hashes.
After the state cycle the strips used 35.7 MiB less than full sheets.
They added 76.7 MiB and 2.59 CPU points above no overlay.
In a follow-up, retaining PNG or lossless WebP per source matched
120 of 120 drawn frame hashes and added 84.3 MiB and
3.36 CPU points above no overlay. Product delivery still uses full sheets.
[Import experiment](verification.md#measure-import-time-character-rows).

A reversed-order Mac comparison held the art and painted canvas geometry
fixed. With five mixed-state strips, motion added 2.45–3.80 CPU points
over the same visible held poses. The separate trace counted 82
GPU swaps with motion and 0 with held poses in eight seconds.
The two moving samples used 91.33–92.18 MiB above no overlay.
[Mixed-state profile](verification.md#profile-animation-with-matched-mixed-state-strips).

A shared clock prototype aligned equal-period sprite steps after
staggered image changes. It matched 30 rendered frame hashes and had
43 GPU swaps in its eight-second traces, compared with 49–82
for independent clocks. The aligned trials added 2.51–2.58 CPU points and
88.5–89.1 MiB above no overlay. Desktop production still uses independent timing.
[Shared timing profile](verification.md#measure-shared-frame-timing-in-the-character-overlay).

A follow-up used naturally loaded full PNG and lossless WebP sheets
with mixed frame counts. It matched 27 rendered frame hashes. Traces
counted 88–95 aligned GPU swaps and 98 with independent
timing. Aligned overhead was 2.96–3.44 CPU points and 123.2–123.5 MiB above no
overlay. The change stayed in the isolated fixture.
[Full-sheet timing profile](verification.md#measure-shared-timing-with-naturally-loaded-full-sprite-sheets).

A follow-up Mac run measured 111.6 MiB and 2.81 CPU points of five-pack
overhead before tracing. About 1.51 CPU points came from the overlay
renderer and 1.29 from the main process, which hosted Chromium's GPU
thread in this fixture. The sprite loop already waits on a timer until
the next frame is due. In a separate eight-second Chromium trace, layer
updates used 41.5 ms of thread time, compared with 14.0 ms across renderer
timers and animation callbacks. The presentation surface was the next variable to isolate.

A four-run Mac comparison tried 224 logical pixels of native window height
instead of 325 at the same 632-pixel width and 2× scale. All five captions
fit, and sprite size, screen-space anchor and draw cadence matched. The
smaller window fell short of the required repeatable CPU or memory
savings. Keep the current height so the existing output popover has
room. The five-character resource budget remains open.

A matched Mac comparison tested CSS background positioning in place of
canvas drawing at the same size and cadence, using the full sprite sheets.
Captured frames showed five moving characters, the same caption positions
and a transparent backdrop. CSS used 177.7–185.9 MiB
more physical footprint than canvas. It added 295.6–296.6 MiB
and 3.01–3.28 CPU points over no overlay. Keep canvas and
test whether a shared paint region can reduce CPU with active-row residency.
The five-character resource budget remains open.

A matched Mac trial placed five full-sheet sprites on one tight canvas with
the same readback hint, draw cadence, captions and geometry. The shared canvas
added 109.9–112.6 MiB and 2.67–3.00 CPU points over no overlay.
The shared full-sheet renderer missed the resource gate. It also missed the CPU headroom needed for the earlier active-row decode cost. The product still uses separate canvases.
Keep the tested canvas path and target atlas residency and drawing cadence separately.

A Mac comparison kept the canvas sizes and full atlas residency fixed while
drawing only the visible region of each frame. The fixture drew 8,320 of
39,936 source pixels per frame and matched full-frame RGBA through 55
transitions in each tight run. This added 113.6–114.5 MiB and
2.57–2.61 CPU points over no overlay. The tighter-paint prototype exceeded the resource budget. Keep full-frame painting.

A matched Mac test compared 96 × 104 and 192 × 208 canvas backings at
unchanged logical size on a 2× display. The 1× backing added 115.3–117.0 MiB
and 2.05–2.26 CPU points over no overlay. Five sprites kept moving with the
same geometry and cadence. The 1× captures softened small sprite details
and missed the resource gate. Keep display-scaled canvas backings.
[Measurement method](verification.md#five-character-canvas-backing-resolution).

Hovering over a character caption reveals the full name, source and status
as text inside the overlay. The existing output button also reveals details
when focused. The detail box passes pointer input through. Passive captions
remain click-through, and a guarded Local Mac check confirmed moving from
an output button to a passive caption restores click-through. The matching
saved output still opens with one click on its caption.

The character overlay has one Move grip. Dragging it moves the group and
saves the final position through the existing overlay bounds route. Tapping
the grip leaves the composer closed. Arrow keys nudge the overlay when
the grip has focus. The guarded Local Mac drag confirmed native movement,
one final bounds message, passive click-through and output after the drop.
If Show bot characters opened the window, the preview stays opt-in at
the next launch. The saved desktop position is used the next time the
preview opens. A mascot that was already popped out still restores on
launch.

Right-click or Control-click an actionable caption to see Output actions.
Preview latest output displays the reply already read for that selection.
Open in Hermes appears when that reply authorizes it and requires a
separate click. Passive captions continue to pass secondary input through.
The isolated Mac fixture verified both gestures and the existing Open
command boundary.

The [cross-panel regression](verification.md#edit-profile-to-monitor-character-handoff-unreleased)
verifies that the saved character reaches Monitor after a roster reload, even
with the optimistic metadata cache cleared. The isolated Mac walkthrough
reached Edit Profile with the canonical Local gateway. Native input stopped
at the Character disclosure, before assignment and visual acceptance.

The [native Mac walkthrough](verification.md#saved-character-reaches-the-native-mac-monitor-overlay-unreleased)
then saved an installed pack through Edit Profile, read it back through a
separate authenticated Local request, and confirmed its art for the bot and
worker in the shared overlay. The preview was exercised with a synthetic
activity row. Real events and overlay resource acceptance remain open.

The [clarification walkthrough](verification.md#monitor-character-shows-the-focused-bots-pending-clarification-unreleased)
shows the waiting pose for the focused canonical Bot Chat until its pending
request settles. Monitor matches the existing runtime signal to one exact bot
row by connection, profile and canonical chat ID. The first native proof uses
synthetic prompt events through the Local gateway. Worker completion still
needs a reliable link between the worker session and its terminal outcome.

[Latest output](verification.md#read-a-bots-latest-saved-reply-from-its-character-unreleased)
starts with the underlined label of a current bot character. Only a click reads
its saved canonical Chat. The overlay receives one plain-text excerpt, up to
600 characters, through the existing window bridge. Opaque output addresses
expire with the current owner binding. The main process checks which window
sent the request and discards late replies after dismissal or loss of visibility.
A ready bot can show one completed or failed worker character for its
newest eligible saved report during the first minute after the outcome.
Working characters take priority within the five-character limit.
A saved Error uses the failed pose and previews the redacted error, with a
saved summary as the fallback. **Open in Hermes** opens the single matching
report from the authorized Monitor snapshot. Replacing the report, changing
its status, or changing its canonical Bot Chat invalidates the old action.
The popover adds no report fetch.

A stopped worker leaves the working overlay when its live observation ends.
Its saved interruption remains **Stopped** in Monitor and creates no
Completed or Error character of its own.

The isolated Mac Local lifecycle test held a loopback model reply while the
actual delegation worker read a fixture file, appeared as working, and
recorded a heartbeat. After completion the same delegation was delivered
to its Bot Chat. The working actor cleared, and its completed-worker
character opened the matching saved summary and Monitor report. The
worker, canonical parent and ledger identifiers matched through teardown.
Model replies, timing and usage were simulated.

The popover and label accept clicks. The animation and transparent margins pass
through on platforms that support it. [Open in Hermes](verification.md#open-the-full-bot-chat-from-its-character-unreleased)
uses one action scoped to the displayed output and rechecks the owning
profile's named chat before opening it. A replaced or missing chat requires a
fresh preview.

The Mac Local pointer test clicked a verified transparent margin and an
owned control beneath it received exactly one trusted click. The completed
worker label and **Open in Hermes** then received trusted system clicks and
opened the exact saved report. The underlay count stayed at one throughout.
The test used an isolated fixture with a stored report.

Opening a [web link](verification.md#open-web-links-from-a-bots-saved-reply-unreleased)
uses the existing default-browser opener. A complete plain-text reply can show
up to two distinct standalone HTTP or HTTPS destinations. Electron keeps the
validated destinations for the current popover and accepts one explicit link
click.

The [Delivered file row](verification.md#see-a-delivered-text-file-in-a-bots-preview-unreleased)
shows the exact path of a supported standalone file delivery from a complete
reply. The path appears as plain text and the transcript remains available
through **Open in Hermes**. **Copy path** copies the exact displayed path,
including for a path-only delivery outside the workspace. Electron accepts the
click only for the current popover and reports the clipboard result.

[PDF deliveries](verification.md#copy-a-delivered-pdf-path-from-a-character)
show the same selectable path and **Copy path** action, including for
mixed-case extensions. The PDF stays unopened.
In the [Local PDF fixture](verification.md#measure-pdf-rendering-in-an-isolated-local-window),
an empty iframe sandbox prevented the PDF page from painting. A separate
window with no preload rendered the blob with its own temporary session.
That fixture still needs an application-level integration and resource test
before the character can offer a PDF viewer.

The [static raster fixture](verification.md#measure-a-static-first-page-pdf-preview)
converted only page one to a bounded PNG. Its images passed the existing
gateway PNG validator. This approach leaves PDF links and viewer controls
out of the character preview. Mac builds now stage the executable and
its sandbox policy together. The [private Mac supervisor](verification.md#supervise-the-mac-pdf-raster-helper)
admits one render at a time and releases the slot when the helper closes.
Preview authorization and the renderer handoff still need integration.

[Preview file](verification.md#preview-a-delivered-text-file-in-a-bots-character-unreleased)
can read one small UTF-8 `.txt`, `.md` or `.csv` file directly inside the
current Bot Chat workspace on a Local POSIX backend. The gateway binds the offered revision to that chat,
its saved workspace generation and the exact current reply. It rechecks the
revision on click and reads through a directory descriptor without following
symlinks. The overlay shows the snapshot as literal text, including Markdown
markup and CSV formulas. The contents start at the first line. The **File path**
disclosure shows the filename and expands to the exact path. Before a preview
loads, the path appears directly in the popover. The five-character resource
budget remains open.

Static PNG previews reuse the workspace and reply checks. The gateway bounds
the file to 128 KiB and 1024 × 1024 pixels and rejects animation, compressed
metadata and international text metadata. The popover shows the snapshot
with the usual **File path** and **Copy path** controls. An outside-workspace
PNG offers the path without an image.

**Expand preview** grows the existing text or PNG view after loading.
The header remains reachable while the file preview scrolls. **Reduce
preview** restores the compact view. A new output starts compact.
[Local expansion proof](verification.md#expand-a-loaded-file-preview-in-a-bot-character).

**Copy text** copies the loaded text snapshot, including whitespace and
line breaks. The clipboard action uses the current preview and does not
read the file again. **Copy path** remains available for delivered files.
[Local clipboard proof](verification.md#copy-text-from-a-loaded-character-preview).

**View image** appears after a PNG decodes in the character popover.
It opens the same snapshot in Hermes' zoomable image viewer. Closing the
viewer returns to the current screen. The handoff uses the loaded bytes
and leaves the file and its path untouched.
[Local image viewer proof](verification.md#view-a-loaded-character-png-in-hermes).

**View text** opens a loaded nonempty text, Markdown or CSV snapshot
in Hermes' read-only source viewer. The viewer shows the filename and
keeps markup, spaces and tabs literal. It reads the current snapshot
without opening a file path or starting a file watch.
[Local text viewer proof](verification.md#view-a-loaded-character-text-file-in-hermes).

## Match a running character to its worker

The owning session’s `subagent.list` can include `child_session_id` for a
resident worker it can control. It matches the worker session ID in Monitor.
A client can supply it with `subagent_id` to `subagent.interrupt`. The gateway
checks both IDs under the same parent and interrupts that worker instance. A
stale or mismatched pair leaves the worker alone. Readable lineage entries
without a controllable worker omit the field. Existing callers can still
interrupt with only `subagent_id`.
The authenticated gateway contract documents the optional identity field.

Right-click a running Local worker caption to open **Worker actions**.
The menu checks the canonical parent once. **Stop worker** appears when
the gateway returns a unique running worker with that child session ID.
Clicking Stop consumes that menu's offer and sends the matched pair to
the owning gateway. Reopening the menu creates a fresh offer. The
menu distinguishes an accepted request from a refusal or a missing
acknowledgment. Monitor shows the worker's eventual status. Pause
remains open.
