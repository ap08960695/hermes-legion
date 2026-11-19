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

The current packaged Local fixture measured the blank overlay renderer
at 160.6 MiB RSS, 79% of the same renderer's RSS with five moving
pets. Five moving pets added 2.27 CPU points and 272.0 MiB RSS over
preview off. The shell already exceeds the full RSS target by itself.
Compare a leaner overlay entry at fixed geometry before investing in
further atlas transport changes.
[Current attribution](verification.md#attribute-the-current-mac-local-pet-overlay-cost).

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
The [Mac Local gateway](verification.md#authorize-a-mac-local-pdf-snapshot)
can authorize a single-use snapshot tied to the saved reply and file
revision. The [Mac Local popover](verification.md#preview-the-first-page-of-a-mac-local-pdf)
opts in through the current Monitor route and receives the rendered
first page after an explicit click. A [native memory watchdog](verification.md#guard-mac-pdf-raster-memory)
stops that child when its sampled peak physical footprint reaches 128 MiB.
[View first page](verification.md#open-a-rendered-pdf-first-page-in-hermes)
shows the loaded PNG in the existing viewer with zoom and a return
to Monitor.

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

## Keep the Monitor characters on the Mac desktop

After **Show bot characters** in Monitor, minimizing Hermes leaves the
characters in the existing borderless, non-activating desktop panel.
The workspace continues its existing five-second activity refresh while
that preview is active on Mac. Stopping the preview or leaving Monitor
ends the background refresh. A stale snapshot still expires, and a
lock or suspend pauses the panel.

The output popover still uses the current character and its expiring
output binding. [Mac Local verification](verification.md#keep-monitor-characters-moving-when-hermes-is-minimized).

## Show pets without window chrome

The shared, transparent panel covers the available display work areas.
It paints the installed sprites and has no status cards or Move
bar. Each character moves on its own. Drag a painted part of a sprite
anywhere in the display's work area. On release above the floor, the
pet accelerates downward, squashes on impact and takes two smaller
hops. Its shadow tightens at the landing spot and a brief dust puff
marks the first contact. The pet keeps its horizontal placement on
the chosen display when the preview reopens. Positions saved by
earlier builds also settle to the floor.
Left and Right move a focused pet along the floor. Reduce Motion
settles the pet immediately. When a Hermes text field is focused,
the overlay also settles immediately and keeps clear of the field.

While walking, pets crouch before each leg, bob through four steps,
and plant each step briefly. They slow to a stop before turning.
The artwork bends around its feet. Dragging still starts from the
pet's stable button position, and Reduce Motion keeps the pose still.
An assigned pack's motion weight sets its walking cadence, fall
duration, impact squash and rebound independently of sprite size.

A waiting character can show **Needs your answer** on hover or focus.
Click an actionable character to open its current output or worker
actions. Empty canvas pixels pass mouse input through. The overlay
still uses one panel for up to five pets. [Mac Local verification](verification.md#show-uncluttered-sprites-on-a-transparent-desktop-overlay).

## Pass a folder or report after pets land

When a worker starts, a folder travels from the delegating bot to the
worker. A saved completion sends a report back to its bot. If either
character is still arriving, the overlay waits until both are visible and
reads their positions then. Both pets pause walking while the folder or
report winds up, spins through an arc and bumps at the receiving pet.
The receiver briefly squashes at contact. Only the latest eligible cue
can wait within the existing 15-second window. Pause, Reduce Motion,
an interaction or a missing endpoint clears the waiting cue.
[Verification](verification.md#pass-task-and-report-cues-after-mac-desktop-pets-land).

## Show which pet needs an answer

A pending clarification in the focused canonical Bot Chat makes the
matching Mac desktop pet briefly show **Needs your answer** after it
lands. The stationary bubble lets clicks pass through and fits inside
the display. Reduce Motion uses a static hold. Hover or keyboard focus
shows the hint again, and clicking the pet retains the current output
and chat actions. The overlay remembers the last 64 actor/request pairs
so a roster refresh can keep the waiting pose without replaying its cue.
[Verification](verification.md#show-the-mac-desktop-pet-that-needs-an-answer).

## Flag a newly saved worker error

A saved worker error can show a short **Worker failed** bubble after the
pet lands. The report must be recorded during this preview and within
the last 15 seconds. Reopening a preview keeps the failed pose and the
saved report available. Click the pet, then **Open in Hermes**, to see
the report. Reduce Motion holds the cue still. [Verification](verification.md#flag-newly-saved-worker-errors-on-mac-desktop-pets).

## CPU cost of equivalent preview refreshes

Two network-isolated Mac fixture launches loaded the same production
overlay with five moving Characters. Each launch measured motion alone
and motion with one equivalent preview snapshot per second, in opposite
orders. Median Electron CPU above the main-only baseline rose from 4.92
to 13.24 percentage points. Within each launch the refresh added 8.89
and 7.74 points. Both phases drew roughly the same number of sprite
frames. Canvas setup calls rose from zero to 25 in each launch.

Two experimental receiver changes reused equal animation metadata across
snapshots, with the second also skipping equivalent mascot-state
notifications. Both removed all 25 canvas setups and preserved motion,
real atlas changes, and document reload. Neither produced a repeatable
CPU saving, so both stayed out of the runtime patch. The next comparison
should isolate publisher, IPC and React commit work while preserving
snapshot expiry and updates to status, output and display geometry.

The Round 351 fixture supplied raw sprite inputs on every refresh, so
its CPU comparison includes repeated image-header and base64 validation.
Monitor prepares immutable atlases once and reuses them. Use prepared
atlases when measuring equivalent Monitor updates.

The Character publisher now coalesces equivalent lease renewals before
IPC. It sends the latest observed expiry at a fixed trailing deadline,
normally every four seconds, with headroom before the visible lease
expires. Roster, status, cue, output identity, sprite identity and
shorter expiry changes publish immediately. Clearing, replacement and
disposal revoke pending renewal work.

## Cost of the panel, sprite cycling and desktop walking

The Mac fixture used the production overlay renderer and preload,
the native IPC handlers and five distinct prepared atlases with 96 × 104
pixel cells.
Each of four signed, network-isolated launches measured the main renderer
alone, then the empty transparent panel, then the same five Characters in
parked, stationary cycling and walking poses. Two launches reversed the
order of the three populated phases. Each pose had one publisher update.
The fixture excluded setup and pixel readback from the seven-second
sampling windows and asserted that no Character snapshots arrived during
those windows. A pixel and position check verified each Character in
each pose.

The table reports medians of four within-launch differences. CPU is in
percentage points of one core. Electron includes main and both renderers
when the overlay is open. WindowServer is measured system-wide.

| Phase change | Electron CPU | Overlay renderer CPU | WindowServer CPU | Electron RSS (MiB) | Electron footprint (MiB) |
| --- | ---: | ---: | ---: | ---: | ---: |
| Open the empty overlay | +0.01 | +0.01 | +0.14 | +176.45 | +92.62 |
| Show five parked Characters | +0.21 | +0.18 | -0.15 | +110.59 | +97.93 |
| Cycle five sprites in place | +3.06 | +1.53 | +4.14 | -21.91 | -22.52 |
| Enable desktop walking | +1.94 | +1.34 | +1.60 | +18.22 | +12.77 |
| Five walking Characters over main-only | +5.22 | +3.14 | +5.73 | +282.75 | +179.92 |

The blank panel accounted for about 62% of the walking RSS increase.
Parking stopped all timed sprite draws. Cycling in place added
2.71–3.43 Electron CPU points per launch. Walking added another
1.74–2.19 points with 261–267 draws versus 255–260 while cycling in place.
Walking RSS and footprint were higher when walking ran first among the
populated phases. Keep the launch order recorded when comparing memory.

The fixture used software graphics in the Electron main process and one
1710 × 1009 work area at 2× scale. The five-Character CPU and RSS budgets
remain open. Compare a Character-only renderer entry and preload at the
same panel geometry as part of removing the upstream mascot.

### Character-only renderer comparison

Five pairs of fresh signed Mac Electron launches alternated the original
renderer and a Character-only build. Each used the stock preload, native
IPC, fixed 1710 × 1009 work area at 2× scale, software graphics and five
prepared atlases. The candidate removed the legacy mascot UI and state
mirroring from the overlay. Both arms used the same Character renderer,
hit-test logic, publisher and work-area panel. The comparison sampled
main-only, blank and walking phases with equal seven-second windows.

| Cost above main-only | Original median | Character-only median | Median paired change |
| --- | ---: | ---: | ---: |
| Blank Electron RSS (MiB) | 176.19 | 175.79 | −0.40 |
| Blank Electron footprint (MiB) | 92.32 | 91.37 | −0.58 |
| Walking Electron RSS (MiB) | 295.86 | 294.88 | −0.03 |
| Walking Electron footprint (MiB) | 200.19 | 200.56 | +0.35 |
| Walking Electron CPU (points of one core) | 5.64 | 5.71 | −0.28 |
| Walking WindowServer CPU (points of one core) | 6.15 | 6.42 | −0.03 |

Each paired change subtracts the original launch's cost from the
candidate launch's cost before taking the median. In the walking phase
Electron CPU changes ranged from −1.47 to +0.53 points. Draw counts were
261–266 in both arms. All five characters painted and moved. Both builds
finished the same synthetic output request before and after panel reload.

The overlay entry chunk shrank by 5,458 minified bytes, but resident memory
and CPU missed the comparison's 20 MiB or 0.5-point improvement threshold.
Keep the current overlay for this performance change. The upstream mascot
removal still belongs with the Characters switch and settings migration.
The next resource test is an app-owned native panel fed by the existing
publisher. The standalone AppKit result justifies measuring it with the
same application-side baseline and checking interaction and teardown.

### Native panel through the owned publisher

Four signed, network-denied Mac fixture launches compared the production
Electron overlay with one AppKit helper in opposite orders. Both arms used
the owned Character publisher, stock preload, production IPC validation,
the same five atlases, 1710 × 1009 panel bounds at 2× and a 10 Hz movement
clock. The native arm took accepted snapshots over a private stdin pipe.
It used one nonactivating transparent panel, with no overlay renderer.

| Cost above publisher-only baseline | Electron | Native |
| --- | ---: | ---: |
| Blank process-tree RSS (MiB) | 176.10 | 41.22 |
| Walking process-tree RSS (MiB) | 297.56 | 124.85 |
| Walking process-tree physical footprint (MiB) | 201.87 | 88.88 |
| Walking process-tree CPU (points of one core) | 5.44 | 0.12 |
| Walking WindowServer CPU (points of one core) | 5.74 | 3.11 |
| Walking combined observed CPU (points of one core) | 11.18 | 3.23 |

The native process alone used about 60.65 MiB RSS while walking. The
publisher and Electron main process still grew by roughly 53.6 and 10.6
MiB respectively in the two native runs. The combined CPU observation
includes system-wide WindowServer activity. Both native runs exceeded
80 MiB incremental RSS and two combined CPU points.

All five native sprites changed cells and moved. Twenty owned layer
crops matched the selected atlas cells with at least 98.33% silhouette
overlap. The native panel paused when the main fixture window hid,
resumed when it returned, survived a replaced deadline, hid on local
lease expiry, cleared and reopened, and exited when the pipe closed.
The evidence covers the fixture's walking and parked states. Release
acceptance also needs per-pixel hit regions, keyboard, drag and output
actions, full pose parity, hardware graphics and Linux verification.

Two additional native runs deferred preparation of unused parked and
stationary variants until after walking was timed. Publisher RSS growth
fell to 40.55–40.78 MiB, while the helper still used 60.66 MiB. Whole-tree
walking RSS fell to 111.97–112.07 MiB. Combined CPU was 3.28 and 1.61 points
in the two runs. The memory budget still missed, and CPU fell within the
budget in one run. Compare publisher preparation and storage separately
from native compositor updates before adopting this presentation path.

### Bound the publisher's atlas decode allocation

Character atlas validation now writes the decoded base64 string directly
into one sized byte buffer. The PNG chunk walk, WebP screening, 4 MiB
decoded limit and frozen prepared atlas contract are unchanged.

Four fresh publisher launches alternated the original and updated
decoders in one signed, network-denied Mac fixture. They shared the
same five atlases, walking pose and native panel. Median walking
publisher RSS above the publisher-only baseline fell from 40.62 to
7.96 MiB. Whole-tree walking RSS fell from 109.09 to 80.17 MiB, and
physical footprint fell from 76.84 to 47.85 MiB. The two updated
launches added 79.34 and 81.00 MiB RSS. Preparing all five atlases took
79.7–90.0 ms before and 18.7–20.8 ms after.

Both decoders accepted and rejected the same PNG, WebP and malformed
base64 corpus. All four launches painted five moving Characters and
passed pause/resume, lease, clear and pipe teardown checks. The two
updated launches measured 2.30 and 2.87 observed CPU points including
WindowServer. The RSS and CPU budgets still need consistent passes.
Compare native presentation updates at the same visual cadence next.

### Attribute native animation cost to presentation

The network-denied Mac fixture measured five visible Characters in the
same full-size native panel at 2× with a 10 Hz timer. Each launch used
adjacent timed pairs in balanced orders. Still sprites kept the same
timer and layer writes while holding both positions and atlas cells
fixed. Atlas-only and translation-only changed one property each.
A second walking mode wrote a layer property only when its value
changed. The still/still control measured short-term variation in the
system-wide WindowServer counter.

| Comparison | Median WindowServer CPU difference | Four observed differences |
| --- | ---: | --- |
| Still versus still | −0.17 points | −0.49, −0.31, +0.02, −0.02 |
| Walking over still | +3.81 points | +3.30, +4.07, +3.58, +4.04 |
| Atlas only over same-launch still | +2.83 points | +2.99, +3.39, +1.71, +2.66 |
| Translation only over same-launch still | +2.73 points | +3.15, +3.55, +1.98, +2.30 |
| Changed-only writes versus normal walking | +0.07 points | −0.03, −0.63, +0.16, +1.06 |

Walking exceeded the still-control variation in both sample orders.
Either animation axis cost appreciably more than a still scene.
Skipping writes with unchanged values cut position writes by 40% and
atlas writes by 26%, with eight pixel-identical walking crop pairs.
WindowServer savings were inconsistent, so the candidate stays in the
fixture.

Normal walking added 65.70–79.82 MiB RSS across the process tree and
3.65–4.47 observed CPU points including WindowServer above the
publisher-only baseline. This fixture met the RSS ceiling in all four
walking samples and exceeded the CPU ceiling. Compare less frequent
presentation while preserving the motion path and elapsed timing.

### Test a lower native presentation cadence

Four network-denied Mac launches compared 10, 8, 6 and 5 Hz with five
Characters on the same 2× panel. Each presentation sampled the same
10 Hz logical walking path from monotonic elapsed time. A missed
sample advanced to the current pose without drawing catch-up frames.
Adjacent 10 Hz comparisons reversed order, and 10/10 pairs measured
short-term CPU drift. Publisher-only windows before and after the
panel bracketed CPU. RSS uses the initial publisher-only baseline.

| Presentation rate | Median added CPU | Added RSS range | Median added physical footprint | Longest submission gap |
| --- | ---: | ---: | ---: | ---: |
| 10 Hz | 3.19 points | 71.66–80.23 MiB | 36.72 MiB | 109.35 ms |
| 8 Hz | 3.25 points | 71.77–80.15 MiB | 36.58 MiB | 133.43 ms |
| 6 Hz | 2.10 points | 71.78–80.03 MiB | 40.36 MiB | 175.67 ms |
| 5 Hz | 2.08 points | 65.92–80.13 MiB | 36.77 MiB | 208.79 ms |

CPU combines the process tree and the system-wide WindowServer counter.
Against its adjacent 10 Hz reference, 6 Hz saved 0.79–2.41 points in all
four launches. The largest 10/10 control difference was 0.61 points.
At 6 Hz, added CPU ranged from 1.76 to 2.48 points. No lower cadence
met both budgets in every launch. The 5 Hz option also exceeded the
fixture's 180 ms submission-gap screen.

Twenty-four fixed-time crop pairs matched exactly across rates. This
establishes pose and path parity. Live motion at the lower rates has
longer holds, and its perceived smoothness remains open. Keep these
rates in the fixture. Compare a shared native surface with bounded
damage at the same cadence to isolate the cost of separate layers.

### Compare a shared native strip with individual layers

Four signed, network-denied Mac launches compared five sprite layers
with one 2× bitmap strip in the same native panel. Both displayed the
same five sprites, positions and atlas cells at matched 6 and 10 Hz.
The strip cleared only the union of each moving sprite's old and new
bounds, then repainted intersecting sprites in z-order. It submitted
a new image for the entire strip when pixels changed.

| Mode | Added CPU range | Added RSS range | Median added physical footprint |
| --- | ---: | ---: | ---: |
| Five layers, 6 Hz | 1.15–1.77 points | 73.26–97.25 MiB | 43.91 MiB |
| Shared strip, 6 Hz | 3.97–6.92 points | 88.56–102.89 MiB | 50.49 MiB |
| Five layers, 10 Hz | 2.35–4.36 points | 83.15–97.41 MiB | 42.56 MiB |
| Shared strip, 10 Hz | 8.11–11.70 points | 88.41–103.06 MiB | 48.30 MiB |

CPU combines the fixture tree and system-wide WindowServer. The
counterbalanced pairs put the shared strip 2.82–5.15 CPU points higher
at 6 Hz and 5.41–7.34 higher at 10 Hz. The helper accounted for most
of the increase. WindowServer changes varied in sign, and the largest
6/6 combined CPU control difference was 1.06 points. The strip cleared
15.6–18.7% of its area per submission on average across runs, so partial
painting alone left substantial work in this implementation.

All eight fixed-time crop pairs matched exactly, including transparent
pixels outside the sprites. Hide/resume, publisher clear and helper
teardown passed. Keep individual layers in the native fixture. At
6 Hz they met the CPU ceiling across these launches and exceeded
80 MiB RSS in three of four. The resource gate remains open. Next
isolate the remaining memory costs of the publisher and native helper
with the individual-layer path.

### Measure native panel and sprite memory separately

Four network-denied Mac launches compared the full work-area panel
with a 100-point-high bottom band. Both used the same five sprite
layers and walked at 6 Hz. The two adjacent pairs reversed launch
order. The panel height changed from 1,009 to 100 points while bottom
alignment, sprite positions and atlas cells matched. Four fixed-time
crop pairs matched pixel for pixel.

| Phase | Native helper RSS across both heights |
| --- | ---: |
| Started before panel creation | 34.89–34.91 MiB |
| Empty visible panel | 39.33–39.42 MiB |
| Five still sprites | 60.78–60.88 MiB |
| Five walking sprites | 60.77–60.86 MiB |

Showing the empty panel added about 4.5 MiB to the helper. The first
sprite frame added another 21.44–21.46 MiB, including layer and image
work. Walking left helper RSS near the still level. During walking,
the publisher renderer added 5.34–5.47 MiB and Electron main added
7.15–10.82 MiB over the publisher-only baseline.

The shorter panel saved 0.03 and 0.09 MiB of helper RSS. Fixture-tree
savings were 3.78 and 0.05 MiB, with the larger difference in Electron
main. System-wide WindowServer RSS moved by at most 0.03 MiB between
the matched overheads. Keep the full-height panel in the fixture.

Across both heights, walking added 73.38–77.16 MiB RSS and 2.49–2.81
combined CPU points over publisher-only. All four launches met the
80 MiB ceiling and exceeded the 2-point CPU ceiling. WindowServer
accounted for most added CPU. The next comparison should hold sprite
art and viewport constant while reducing position submissions from the
helper. This fixture covers one 2× display and a mouse-ignored panel.
