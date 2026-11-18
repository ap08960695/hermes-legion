# Walk and turn near the desktop corner

Mac desktop pets take short walks between their idle or working poses.
Each pet has a staggered cycle and varies its travel distance within its
slot. Directional atlas rows follow travel. A one-direction pack mirrors
the running row and preserves alpha hit testing. Focus, hover, output and
drag pause walking. Reduced motion keeps the static pose.

In the signed Mac Local fixture, all five Lanternling sprites drew the
left, right, and working atlas rows and traveled 34–43 points with
Hermes minimized. The same run passed four-corner drag, transparent
release, and latest-output popover checks.

| Preview | CPU, percent of one core | Mean physical footprint |
| --- | ---: | ---: |
| Off | 0.98% | 541.4 MiB |
| Five moving pets | 2.76% | 579.5 MiB |
| Increase | 1.79 percentage points | 38.2 MiB |

The warmed 20-second samples include Electron and the local gateway.
GPU and networking ran in-process. Local60 saw zero Desktop SSH links
and the fixture stopped cleanly. Default GPU and multi-display
performance still need verification.

# Drag Mac desktop pets to the screen edges

The Mac character panel covers the connected work areas. Each pet moves
independently using global pointer coordinates. A drag clamps the whole
sprite to the pointer's display, with a nearest-display fallback for
gaps. A display change rehomes stranded pets. Five characters start in
a smaller bottom-right group and keep their horizontal movement.

The signed packaged Mac Local fixture used one 1710 × 1009 work area
with Hermes minimized. Chromium pointer input placed one pet at all
four work-area corners, kept the other four in place, and restored
click-through after each release on transparent pixels. Re-grabbing the
pet after it overlapped a neighbor returned it to its starting spot.
The latest-output popover fit within the work area. A mock with two
offset displays covered the seam and disconnect behavior. This Mac had
one connected display.

| Preview | CPU, percent of one core | Mean physical footprint |
| --- | ---: | ---: |
| Off | 0.91% | 532.1 MiB |
| Five moving pets | 2.39% | 589.6 MiB |
| Increase | 1.48 percentage points | 57.6 MiB |

The warmed 20-second samples include Electron and the loopback gateway.
GPU and networking ran in-process for the fixture. Local60 reported
zero Desktop SSH links. Stopping preview released the overlay renderer
and all fixture processes exited. Physical pointer input, multiple
connected displays, Spaces and default GPU topology remain open.

# Pace desktop pet movement at 10 Hz

The desktop overlay caps horizontal wandering at 10 position changes per
second. The installed sprite canvases keep their existing animation.
Focus, hover, dragging, and an open popover park the selected character.
Reduced motion uses a static pose.

In a signed packaged Mac Local fixture, all five pets made 14 position
changes over roughly 1.4 seconds with the cap, compared with 84 each
with continuous interpolation of the same CSS path. Each canvas showed
at least three different sprite frames in the follow-up checks. The same
overlay renderer and 300 px band were used for all preview-on conditions.
The main window stayed minimized and the latest-output popover fit on screen.

| Condition | CPU, percent of one core | Mean physical footprint |
| --- | ---: | ---: |
| Preview off | 1.01% | 505.2 MiB |
| Five pets, paced | 3.18% | 559.3 MiB |
| Five pets, continuous CSS control | 3.34% | 557.7 MiB |
| Five pets, pace restored | 2.79% | 556.8 MiB |

Pacing saved 0.16–0.55 percentage points of one core against the continuous
CSS control. The preview-off comparison puts paced overhead at 1.78–2.17
CPU points and 51.6–54.1 MiB of physical footprint in this run. Memory varied
between runs. The release budget for the default GPU topology
still needs verification. The fixture ran GPU and networking in Electron
main. Both successful Local probes recorded zero Desktop SSH links and the
overlay renderer exited when preview stopped.

# Isolate desktop-pet rendering cost on Mac Local

A signed packaged Electron fixture kept the main window minimized. It used
the same overlay renderer and five sprites from the installed Lanternling
atlas for every preview-on sample. The 150 px band kept the width and bottom edge fixed.
Pausing horizontal movement and hiding content were probe-only overrides.
The sprite canvases kept advancing in both conditions.

| Condition | CPU, percent of one core | Mean physical footprint |
| --- | ---: | ---: |
| Preview off | 0.92% | 520.0 MiB |
| Five moving pets, 300 px | 6.38% | 577.2 MiB |
| Five moving pets, 150 px | 3.60% | 571.9 MiB |
| Horizontal movement paused, 300 px | 3.10% | 567.0 MiB |
| Content hidden, 300 px | 2.34% | 566.9 MiB |
| Horizontal movement paused, 150 px | 2.45% | 567.5 MiB |
| Five moving pets, 300 px restored | 4.32% | 568.1 MiB |

The restored condition used about two CPU percentage points less than the
initial 300 px condition. The narrower band and parked horizontal movement
both used less CPU than either 300 px moving sample. Footprint drift and
the still-mounted overlay limit the memory conclusions. The alternate
band was checked for sprite fit at rest. Drag range and popover fit require
separate evidence before shipping a narrower band.

# Measure five desktop pets in a packaged Mac Local build

An ad-hoc signed Electron 44.9.3 app loaded its packaged archive
and unpacked renderer. Main and overlay used distinct renderer
processes. With the main window minimized in both samples, the
loopback gateway and the app were measured for 20.5 seconds with
preview off and for 20.5 seconds with five moving Lanternling sprites.

| Preview | CPU, percent of one core | Mean physical footprint | Mean RSS |
| --- | ---: | ---: | ---: |
| Off | 0.85% | 469.3 MiB | 796.6 MiB |
| Five moving pets | 5.15% | 574.4 MiB | 902.1 MiB |
| Increase | 4.30 percentage points | 105.1 MiB | 105.5 MiB |

Both increases exceed the character preview targets of roughly
1–2 CPU percentage points and 60–80 MiB of memory. The overlay
renderer exited when preview stopped. Local60 reported zero Desktop
SSH links and the entire fixture stopped without survivors. These
are short fixture measurements. GPU and network ran inside Electron
main to hold the four-process limit.

# Recheck desktop-pet click-through when a drag ends

On release or cancellation over the pet control, the overlay checks
the current hit again after React commits the end of the drag. The
shared native panel can return clicks on empty pixels to the desktop
even if the pointer has stayed still. The check runs once per
completed gesture.

The renderer regression starts on a painted sprite, releases over
an empty point, and verifies that click-through updates without
another mouse move.

# Show uncluttered sprites on a transparent desktop overlay

The Mac overlay reapplies its clear native backing when the window is
revealed. A controlled WindowServer capture reproduced an opaque
#121212 backdrop even with transparent CSS. After the fix, the same
empty pixel followed two different backgrounds behind the panel.
Five sprites from the installed Lanternling example remained visible
while Hermes was minimized. The capture included only windows from
the isolated test app.

The character controls use the painted sprite for pointer hit-testing.
Scoped regressions cover empty pixels, individual drag, cancelled
drag, keyboard nudging, and current-output selection. The five-actor
and 15 fps sprite limits still apply.

# Keep Monitor characters moving when Hermes is minimized

A signed Mac Local build showed five characters in one floating panel.
Minimizing the main window left the panel visible and inactive. Sprite
canvas pixels changed while the main window stayed minimized. A fresh
worker status reached the panel through the existing Monitor query,
and a character opened its current output popover. The run exceeded
the preview's 15-second lifetime and kept all five characters present.
A simulated lock removed the actors and unlock brought them back.

In this shared-renderer fixture, the Electron main and renderer
averaged 0.40% of one core with the main window minimized and
preview off, and 1.21% with five animated actors. Mean combined
RSS rose by 24.0 MiB over short samples. Local60 recorded zero
Desktop SSH. The app and gateway stopped with no survivors. OS
display sleep, actual Space changes and packaged renderer overhead
still need separate evidence.

# Check Close button contrast in the Hermes image viewer

The existing Close button uses a white icon on an opaque dark circle
in the image viewer. The control has a white keyboard outline with a
dark outer ring. The styling stays inside the image-viewer dialog.

In the isolated Mac workflow, the button remained visible over a white
PDF page and a dark PNG. The same Close control handled pointer and
keyboard dismissal, and Escape returned to Monitor.

# Open a rendered PDF first page in Hermes

After **Preview file** renders a PDF on Mac Local, **View first page**
opens the same image in Hermes' zoomable viewer. The control appears
after the popover has decoded its image. Closing the viewer returns
to Monitor. The original delivery path stays available in the popover.

Electron holds one bounded PNG with the current preview action and
hands it over only for the matching click. Opening, zooming and closing
use the in-memory first page. A stale or replaced action cannot hand
over its image.

# Verify PDF preview through Mac Local Monitor

A signed isolated Desktop build opened **Bots → Monitor → Show bot
characters** against one loopback gateway. The character's **Preview
file** action redeemed the current workspace ticket once, read the
file once, and started one sandboxed raster helper. The 413 × 640
first-page PNG matched the reference byte for byte. **Expand preview**
increased the displayed height from 68 to 192 px.

Replacing the file after the offer produced **File preview unavailable**
before disk read or rasterization. An outside-workspace PDF offered
**Copy path**. The intercepted clipboard received the exact path,
including spaces and Unicode.

The fixture used Chromium's process-per-site switch. Both windows
shared one renderer, and the raster start accounted for four product
processes. The Local60 gate passed before input with zero Desktop
SSH. The app and gateway stopped with no survivors.

# Guard Mac PDF raster memory

The Mac raster helper checks its kernel-reported peak physical
footprint before parsing, every 10 ms while working, and before
publishing a successful result. It exits at 128 MiB or on a failed
measurement. The watchdog runs as a thread in the existing helper.
The parent keeps its timeout and discards output from nonzero exits.

A signed Apple Silicon regression inserted a bounded 160 MiB
allocation during parsing. The previous build returned its page.
The guarded build stopped while the allocation was active and
returned zero PNG bytes. Three normal documents still matched
their reference PNGs exactly. Peak footprint is sampled, so a
fast allocation can briefly exceed the threshold.

# Preview the first page of a Mac Local PDF

A PDF delivered in the current Bot Chat workspace can show **Preview
file** in the character popover on Mac Local. On click the existing
Monitor route redeems the ticket, and Electron sends a bounded snapshot
to the sandboxed raster helper. The overlay receives a PNG of page one.
The popover keeps **Copy path** and offers **Expand preview**. Outside
deliveries and unsupported connections show the path. An older Local
gateway that rejects the opt-in can still offer text and PNG previews.

Electron claims each click once and discards the raster if the current
popover is replaced, hidden, closed, or navigating. Invalid or failed
renders show **File preview unavailable**. The built-in document viewer
and system-open actions remain separate work.

# Authorize a Mac Local PDF snapshot

Native Mac Local callers with session control can set `pdf_preview` to
true when requesting the latest Bot Chat output and again when redeeming
its file ticket. The workspace rules still require one direct-child
delivery in the current reply. The offer checks file metadata. The
single-use read rechecks the exact reply and file revision, verifies
the opened descriptor before and after reading, and returns at most
512 KiB of PDF bytes. Expired, replayed, replaced, linked, oversized,
and invalid-header offers return no snapshot.

An isolated Mac authority read a two-page fixture. The first-page PNG
from the signed sandboxed helper matched the saved image byte for byte.
The fixture passed the snapshot to the helper outside Electron. Character
PDFs still offer **Copy path**. App integration remains open.

# Supervise the Mac PDF raster helper

The private Mac supervisor accepts a PDF byte snapshot and starts the
packaged helper with its sandbox policy on demand. It caps stdin at
512 KiB and stdout at 128 KiB. The PNG must have a complete header and
end marker, with each edge in 1–640 px. A timeout, cancellation, stream
failure, or overflow terminates the child and discards its output. A
second request is refused while the first child owns the slot, through
its close event.

A standalone Apple Silicon probe used the shipped unpacked layout and
policy. It reproduced three saved first-page PNGs, rejected malformed
and oversized inputs, and reaped the child after timeout and cancellation.
Only one render ran at a time. macOS refused nested profiles, so the
successful probe applied the shipped sandbox directly to the child.
Gateway authorization, Desktop IPC, the viewer, and a runtime RSS
limit remain open. Character PDFs still offer **Copy path**.

# Stage the macOS PDF raster helper

Mac native preparation builds the PDF raster executable with arm64
and x86_64 slices. Prepared inputs bind the build script, C source
and sandbox policy to the native receipt. A Mac tree missing either
output requires restaging. The existing native copy step places both
files in `dist/native`. Packaged assets use the existing unpacked ASAR
layout.

An ad hoc signed Local Electron fixture invoked the unpacked helper
through its bundled policy. The helper accepted bounded bytes on
stdin, rendered page one, and rejected invalid headers, malformed PDF,
oversized input, and path arguments. Character PDF deliveries still
offer **Copy path**. Live viewer wiring and release signing remain open.

# Measure a static first-page PDF preview

An on-demand CoreGraphics and ImageIO helper accepted PDF bytes on stdin
and returned a PNG for page one. It capped input at 512 KiB, checked page
geometry, allocated a bitmap with a 640 px longest edge, and capped output
at 128 KiB. Fifteen Mac Local runs covered a two-page report, rotation
with a nonzero page origin, and a large sheet. The existing gateway PNG
validator accepted each output. Oversized input, excessive geometry, and
malformed content returned no image.

A supervisory test killed and reaped its child on timeout and RSS
controls. Paired controls verified that the working sandbox blocked a
protected fixture read, a write, child execution, and a loopback connection.
A global file-read allowlist aborted before the helper entered main. The
working profile denies reads under protected roots while permitting other
system reads. Integration, packaging, and application-level measurements
remain open. Character PDF deliveries still offer **Copy path**.

# Measure PDF rendering in an isolated Local window

A signed standalone Mac fixture used Electron 44.9.3 and the same
one-page blue document in two successive windows. Both windows used
Chromium's renderer sandbox, context isolation, no preload, and
temporary sessions. The ordinary blob iframe painted 45,796 blue
pixels in the page. The iframe with an empty `sandbox` attribute
painted zero. Both captured 2,464 pixels of the orange HTML control.
An independent macOS image conversion also rendered the source page.

Fixture controls exercised a denied localhost fetch, top navigation,
popup, download, and geolocation permission. The inspected host and
PDF frames exposed no Hermes bridge, Node bindings, or opener.
The separate-window experiment used no running Hermes app or gateway.
The character continues to offer **Copy path** for PDFs. Production
viewer authority, PDF actions, and process and memory overhead in Hermes
remain release gates.

# Copy a delivered PDF path from a character

A complete reply with one standalone PDF delivery shows the exact path in
the character's latest output. Select **Copy path** to copy it, including
spaces and original spelling. **Path copied** confirms success.

This works for an existing workspace PDF and for a delivery path outside
the workspace. The path stays selectable plain text. The action leaves
the PDF unopened and sends no file preview request.

# View a loaded character text file in Hermes

Open a character's latest output and choose **Preview file** on a
delivered text file. Once it loads, choose **View text**. The Hermes
source viewer shows the filename and scrollable literal source.
Closing it returns to the current screen.

Text, Markdown and CSV use the same read-only source view. The file
preview must contain text before the action appears. The handoff
uses the existing snapshot and does not read or watch the file.

# View a loaded character PNG in Hermes

Open a character's latest output and choose **Preview file** on its
delivered PNG. Once the image appears, choose **View image**. Hermes
opens its existing image viewer with zoom controls and a close button.
Closing the viewer returns to the current screen. Text and failed
image previews omit the action.

Renderer and Electron tests cover the decoded image button, exact
snapshot handoff, stale request, wrong sender, extra payload and a
closed output. The handoff uses the loaded PNG bytes.

# Copy text from a loaded character preview

In a character's latest output, choose **Preview file** on a delivered
text file and then **Copy text**. A successful clipboard write shows
**Text copied**. Empty, unavailable and PNG previews omit the action.

An isolated signed Mac Local fixture intercepted the clipboard write and
received all 1,590 UTF-8 bytes from the loaded snapshot, including its
spaces, tabs and line breaks. Copying caused no additional file reads or
file RPCs. The PNG fixture only offered **Copy path** after loading.
Local60 found zero Desktop SSH. All fixture processes stopped.

# Expand a loaded file preview in a bot character

The file preview header offers **Expand preview** and **Reduce preview**
for an already loaded text or PNG snapshot. The toggle works in the
existing popover and sends no IPC. New output starts compact. On image
decode failure the larger view closes and the unavailable state appears.

An isolated signed Mac Local fixture exercised PNG and literal text
through Bots and Monitor with the loopback gateway. The image grew from
68 to 192 px high. Complete visible text lines grew from 2
to 4, with the same header position while the preview
scrolled. There were two file reads for the two files and no toggle IPC.
The Local60 check found zero Desktop SSH. All owned processes stopped.
Tests cover preserving the loaded content, retaining the toggle's focus
target, resetting for a new output and clearing a failed image.

# Measure shared timing with naturally loaded full sprite sheets

Five signed Mac Local fixtures used one build and the same full PNG
and lossless WebP sheets. Two independent/aligned comparisons ran in
opposite orders around a no-overlay control. Natural browser image
loads spanned 0.0–0.1 ms. The visible states used 6, 6, 6, 4 and
5 frames. A renderer test covered unequal periods and immediate row
repaint on a state change.

The two variants matched 27 drawn-frame hashes and preserved canvas
and caption geometry. Independent timing drew 28–41 frames per actor
in eight seconds and aligned timing drew 29–43. Each actor's populated
frames appeared. Separate traces recorded 98 independent
GPU buffer swaps and 88–95 aligned swaps. The three equal-period
sprites shared 41 display frames with independent timing and
43 with aligned timing.
All five sprites restarted together twice during the first independent
draw probe, after the resource sample. The trigger remains unknown.
The other three animation probes stayed in sequence.

CPU differences (independent minus aligned) were -0.21 and +1.53 points. Aligned overhead was 2.96–3.44 CPU points and
123.2–123.5 MiB above no overlay. It exceeded
the 2-point CPU ceiling and exceeded the
80 MiB memory ceiling. The samples include fixture GPU work and exclude
WindowServer. Product delivery and timing use their current paths.
All five runs recorded zero Desktop SSH after 60 seconds and no survivors.

# Measure shared frame timing in the character overlay

Five signed Mac Local fixtures used one build and equal sprite strips.
Two independent/aligned comparisons ran in opposite orders around a
no-overlay control. Fixture-delayed image loads spanned 1026–1028 ms. The experimental timing path draws the first ready
pose and aligns later deadlines. A renderer test covered staggered
image readiness, an overdue frame, and cancellation on hide.

The two variants matched 30 drawn-frame hashes and preserved canvas
and caption geometry. Independent timing drew 40–42 frames per actor
in eight seconds and aligned timing drew 44. All six frames
appeared in order. Separate traces recorded 49–82 independent
GPU buffer swaps and 43 aligned swaps. Draws from all five sprites shared a timestamp 0–42 times with
independent timing and 38–44 times when aligned. Independent frames
were already grouped in the second draw probe.

Shared timing saved 0.84–1.58 CPU points across the two pairs. Aligned overhead was 2.51–2.58 CPU points and
88.5–89.1 MiB above no overlay. Both trials exceeded the 2-point CPU and 80 MiB memory ceilings. The samples include fixture GPU work and exclude
WindowServer. Product delivery and timing use their current paths.
All five runs recorded zero Desktop SSH after 60 seconds and no survivors.

# Profile animation with matched mixed-state strips

Five fresh signed Mac Local fixtures used equal PNG/WebP row strips,
state warm-up and canvas geometry. Two overlay pairs ran in opposite
orders with a no-overlay control between them. The static control used
the renderer's reduced-motion path. Five painted canvases remained
visible without drawing during the pose probes. Every moving canvas
changed during its corresponding probe.

Untraced samples measured 0.16–0.19 CPU points above no overlay for
held poses and 2.61–3.99 for moving. Motion added 2.45–3.80 points in
paired trials. Physical footprint above no overlay was 87.97–88.13 MiB
for held poses and 91.33–92.18 MiB for moving. Separate eight-second
traces recorded 0 GPU buffer swaps for held poses and 82
for moving. The layer update counts were 0 and 82.
Median moving swap gaps were 83.7–99.4 ms. Neither trace recorded a gap of 35 ms or less.
CPU includes fixture GPU work and excludes WindowServer.

Moving exceeded both the 2-point CPU ceiling and the 80 MiB memory ceiling.
The test changed no product animation. All five accepted runs recorded
zero Desktop SSH after 60 seconds and left no survivors.

# Measure import-time character rows

The real pack validator and atomic importer ran in a disposable Mac
profile. The experiment encoded populated rows from the exact validated
PNG or lossless WebP bytes after confirming the installed source matched.
Four offline controls checked partial alpha, a combined source-and-row
4 MiB cap, fallback for gamma metadata and replacement between validation
and import. Across five synthetic packs, four rows per pack added
44.6 KiB of encoded data.

Three fresh signed Mac Local fixtures compared no overlay, full sheets
and import-time strips with one renderer. Five characters rotated
through mixed running, waiting and failed states. 96 of 120
drawn frame hashes matched. Canvas identity, geometry and cadence passed.
After the cycle, strips used 35.7 MiB less than full sheets across the
app processes. They added 76.7 MiB and 2.59 CPU points above no
overlay. The candidate met the 80 MiB memory ceiling and
exceeded the 2-point CPU ceiling in this pair. Each run recorded zero
Desktop SSH after 60 seconds and no survivors. Production delivery
continues to use full sheets.

All 24 mismatches in the benchmark came from one of the two WebP
packs. A fourth signed Local fixture compared 36 test crops from
both WebP sources in Chromium. Full PNG transcodes matched 18/36
against full WebP and PNG strips matched 18/36. Full PNG and
PNG strips matched 36/36. Lossless WebP strips matched
36/36 against full WebP. The PNG strips differed by up to three RGB levels per channel.
Alpha matched in all 36 frames.
The codec control recorded zero Desktop SSH and no survivors.
The mismatch reproduced without slicing the atlas. Keeping WebP in
the derived row preserved the drawn pixels for these two source packs.

A fifth signed Local trial kept PNG rows in PNG and WebP rows in
lossless WebP. It used the original full-sheet and no-overlay runs as
controls with the same renderer build and state sequence. This time
120 of 120 drawn frame hashes matched. After the cycle the
same-format strips used 28.1 MiB less than full sheets. They added 84.3 MiB
and 3.36 CPU points above no overlay. CPU was +1.06 points
relative to full sheets. The run exceeded both resource ceilings. It recorded zero
Desktop SSH after 60 seconds and left no survivors.

# Measure runtime row cropping in the character producer

Three signed isolated Mac Local runs compared no overlay, full PNG
atlases and crops derived from those same atlases in the producer
renderer. Five characters went from running to waiting, failed
and running again. All 120 drawn-frame hashes matched. Canvas
identity, geometry and cadence passed. Offline controls covered
discarding superseded work, caching the current row and falling
back to the full atlas for failed or missing crops.

After the cycle, strips used 4.3 MiB more across the app processes.
The overlay renderer changed by -27.8 MiB, the producer
by +10.9 MiB, and the main process including GPU by
+21.5 MiB. The sampled capture peak dropped by 2.0 MiB. Strips added
101.6 MiB and 3.98 CPU points above no overlay. This trial
exceeded the 2-point CPU target. Memory was above the 80 MiB ceiling. The capture peak includes diagnostics.
The experiment leaves product delivery on full sheets. It used synthetic
PNG art. WebP and owner art remain unverified.
Each trial recorded zero Desktop SSH after 60 seconds and no survivors.

# Exercise row-strip transitions in the character overlay

A signed, isolated Mac fixture sent five characters through running,
waiting, failed and running again with one production renderer.
Full-sheet and strip snapshots matched 120 drawn frame hashes,
canvas identities within each run, viewport geometry and cadence.
The offline image-load regression checks one mounted canvas.
Pending and failed decodes leave its pixels in place. An earlier
load arriving after the newest image draws schedules no new frame.

In one 20-second sample after the transitions, strips used 28.6 MiB
less than the full sheets. Their overhead was 70.5 MiB and 2.53 CPU
points above no overlay. The test used fixture-supplied sprites at
the owned IPC receiver. Gateway delivery of one-row sprites and
the broader release budget remain open. Three runs recorded zero
Desktop SSH after 60 seconds and no survivors.

# Compare resident character sprite sheets

Seven fresh isolated Electron runs used the same production renderer.
Two opposite-order passes compared five full sheets, five equally sized
sheets with transparent unused rows, and five one-row running strips.
The running pixels, canvas dimensions, 2× viewport, and frame cadence
matched. Each run sampled 20 seconds after an 18-second warmup. The
figures below compare each variant's two-run midpoint with the
no-overlay baseline.

| Source | Added physical footprint | Added CPU points of one core |
|---|---:|---:|
| Full sheets | 108.0 MiB | 2.41 |
| Transparent unused rows | 108.2 MiB | 2.93 |
| Running strips | 71.3 MiB | 2.43 |

The renderer produced matching SHA-256 hashes for all six frames of
each of the five canvases. The lower footprint with strips measures
the end-to-end effect of smaller source images. The trial leaves
allocation-level attribution and state-transition behavior open.
Every run recorded zero Desktop SSH at 60 seconds and no surviving
processes.

# Keep the Markdown vendor chunk off the overlay boot path

The built overlay entry reached the entire Markdown vendor chunk through
ordinary buttons' class-name helper. Moving that helper to the shared UI
foundations reduced statically reachable overlay JavaScript from
3,871,493 bytes in 48 files to 3,522,873 bytes in 47 files. The built
manifest still links Markdown from the normal Chat renderer. The same
check rejected dropping the helper from all groups because the resulting
overlay reached the syntax-highlighting bundle.

The isolated Mac fixture loaded five moving sprites before and after.
The old renderer requested the Markdown chunk. The new renderer left it
off the request list. Both kept matching geometry and animation cadence.
A single matched comparison measured physical footprint and CPU. The
five-character resource target remains open.

# Five-character canvas backing resolution

Six isolated Mac Electron runs used one bundle with five synthetic full
sprite sheets. Two opposite-order 2×/1× pairs were bracketed by no-overlay
baselines. At 2× display scale, each character kept its 96 × 104 logical
size and changed only its backing from 192 × 208 to 96 × 104. The
measurement sampled 20 seconds after 18 seconds of warmup. CPU is the
percentage of one core, including fixture GPU work and excluding
WindowServer. Memory is the median summed physical footprint.

| Canvas backing | Added memory over no overlay | Added CPU points |
|---|---:|---:|
| 2× | 113.5–116.7 MiB | 2.58–2.62 |
| 1× | 115.3–117.0 MiB | 2.05–2.26 |

All five packs moved in both modes with matching rectangles and cadence.
The 1× backing softened sprite details and exceeded the memory budget
with the full sprite sheets still resident. The desktop keeps its
display-scaled backing. Each trial recorded zero Desktop SSH after 60
seconds and zero surviving processes. Real bot activity and pointer
interactions were outside the benchmark.

# Preview a delivered PNG in a bot’s character (unreleased)

The latest-output popover can preview a single static PNG from the
current Bot Chat’s Local workspace. Clicking **Preview file** rechecks
the same reply and reads through the same no-follow file path as text.
The gateway limits the snapshot to 128 KiB and 1024 pixels per side and
declines animated PNGs, compressed metadata and international text metadata.
The image uses its file name as a label. A refused or undecodable snapshot
reports **File preview unavailable**. An outside-workspace PNG shows its
path and **Copy path**.

# Preview a delivered text file in a bot’s character (unreleased)

**Preview file** appears when the complete saved reply delivers one
absolute `.txt`, `.md` or `.csv` path directly inside the current Bot Chat
workspace on a Local POSIX backend. Suffixes are case-insensitive.
A click rechecks the saved reply and workspace, then
reads up to 8 KiB of UTF-8 text through no-follow file and directory
descriptors. The snapshot appears as plain text in the popover, with
Markdown markup and CSV formulas shown literally. Once the preview loads,
the file starts at the first line. Expand **File path** to select the full
path. Expanding it uses the path already shown by the reply.

The isolated Mac Local run made zero file reads when the popover opened
and one when the user selected **Preview file**. It preserved the two
spaces in the filename and displayed HTML-like bytes literally. A later
reply pointing outside the workspace showed its path and made zero file
reads. The fixture passed 60 seconds with zero Desktop SSH and exited.
Regressions cover stale replies and cross-owner requests, symlinks, hard
links, special files and overflow after the initial size check.

# See a delivered text file in a bot’s preview (unreleased)

A character’s latest-output popover labels the full path when a complete
saved reply contains one standalone `MEDIA:` delivery of an absolute
`.txt`, `.md` or `.csv` path. Quoted filename spaces are preserved. The label is plain
text and **Open in Hermes** still opens the owning Bot Chat. Ambiguous
or incomplete replies keep the ordinary text preview. Select **Copy path**
to copy the exact displayed path without reading the file. The popover shows
**Path copied** once Electron confirms the write. Copying is available before
or after a preview and for deliveries whose path is shown without a preview.

An isolated Mac Local run displayed the exact path, including two spaces
in the filename, from the canonical Bot Chat despite a newer side chat.
The path was outside the fixture chat’s workspace. The popover made one
authenticated output read and requested zero probes or launches of that
file. The Desktop passed 60 seconds with zero SSH and all fixture
processes exited. This walkthrough covered the path display.

# Open web links from a bot’s saved reply (unreleased)

The character popover shows up to two distinct standalone HTTP or HTTPS
destinations from a complete saved reply. Select the full URL to send it to
the default browser. Long destinations wrap. Truncated replies, Markdown
links, file paths and malformed URLs appear as plain text. A preview accepts
one link click, and **Open in Hermes** remains available afterward.

The isolated Mac Local run used a reply with two destinations and a duplicate.
The popover displayed two choices and made one authenticated output read.
Selecting the second destination handed its exact URL, including the query
and fragment, to Electron’s browser opener once. The fixture intercepted that
handoff without launching a browser. The app passed the 60-second zero-SSH
check and all fixture processes exited. Renderer and IPC regressions cover
stale or replayed clicks, forged payloads and incomplete or unsafe links.

# Open the full Bot Chat from its character (unreleased)

**Open in Hermes** appears after the overlay loads the bot's saved output.
An active popover supplies one action. The main renderer resolves the exact
Bot Chat again on its owning connection and profile, checks the named chat
is still the one previewed, and opens its current compression tip. A missing
or replaced chat leaves the existing conversation alone. Regressions cover
expired and replaced previews, mismatched windows, duplicate clicks, and
closing the popover while the lookup is in flight.

An isolated Mac Local run started in Monitor and opened the full fixture Bot
Chat using the overlay button. The gateway log recorded one output read, one
named lookup and one resume for that chat. The displayed reply and session ID
agreed with the fixture even though a newer visible side chat existed.
The Local gateway and app passed 60 seconds with zero SSH and exited.

# Read a bot’s latest saved reply from its character (unreleased)

With the character overlay enabled in Monitor, select an underlined bot label
to open its latest saved reply. The overlay requests one bounded, plain-text
result from that bot’s exact canonical Chat. The regressions cover a newer user
message, hidden messages, empty and file-only replies, the text limit, and
identical chat IDs on different profiles. Renderer and IPC tests also cover
stale bindings, forged IDs, late replies and closing during a read.

An isolated Mac Desktop with a canonical Local gateway showed the seeded
assistant reply in the overlay. The click produced exactly one authenticated
read. Moving across the transparent area restored click-through. Closing the
popover left the character overlay active without another read. The fixture
used persisted messages and synthetic worker activity with no model request.
A second Local run opened a long reply, scrolled its body while the header
and close control stayed visible, then dismissed it without a second read.
Both trials passed 60 seconds with zero Desktop SSH, used at most four product
processes and exited. Attachment actions and worker results remain open.

# Monitor character shows the focused bot’s pending clarification (unreleased)

Monitor uses the existing waiting pose while the focused canonical Bot Chat
has a pending clarification for one matching connection and profile. It clears
the pose when the request settles. The renderer regressions cover lost runtime
bindings, missing or ambiguous owners, retained rows, and error precedence.

The isolated Mac Desktop used its canonical Local gateway. A synthetic
clarification appeared in Chat. After opening Monitor and enabling the preview,
the owned overlay showed the amber waiting pose next to cyan activity. The
settle event cleared amber while cyan remained. Both captures were checked
in sRGB. The first run switched profiles after the prompt arrived and captured
no waiting pose. The successful retry selected the mascot’s profile before
opening Chat and kept that profile through both captures.

Each run passed at least 60 seconds with zero Desktop SSH. The peak was four
product processes and 1.09 GiB of sampled RSS including the observer. All test
processes exited. Model-generated clarifications, worker completion, output
preview and the five-pack resource target remain open.

# Saved character reaches the native Mac Monitor overlay (unreleased)

An isolated Electron control first opened a plain Character disclosure and
selected an installed option with Computer Use. Trusted DOM events, the
accessibility state and a painted marker agreed for both steps. The control
showed that the same action could work in a fresh, isolated window.

The production Desktop build then connected to the canonical Local gateway
through an authenticated loopback session. After the 60-second zero-SSH
check, Computer Use opened the fixture bot's **Edit Profile → Character**,
selected its installed Ruby pack, and saved. The editor reported success.
A separate authenticated roster request read `ruby-character` from the
same profile. The request for the installed gallery was Local-only.

With an enabled cyan mascot in the active Local profile, Computer Use opened
Monitor and selected **Show bot characters**. The bot and its synthetic
worker both displayed ruby sprites in the shared overlay. Independent pixel
checks found the ruby art and no cyan mascot pixels. That closes the native
save-to-preview walkthrough for the isolated fixture. The earlier input and
capture divergence did not recur. Its cause remains unknown.

The control and full app each passed their own 60-second zero-SSH check.
The full Desktop and gateway used at most four product processes, reached
about 1.10 GiB peak summed RSS with the observer, and exited. The activity
row was synthetic. Real bot events and the five-character resource budget
remain release gates.

# Edit Profile to Monitor character handoff (unreleased)

The packaged Mac Desktop renderer, Electron main and preload connected to the
actual Local gateway. An authenticated loopback connection returned the
fixture roster. Computer Use reached Bots and Edit Profile for the named
fixture after 60.10 seconds with zero Desktop SSH. The Character disclosure
and its label returned no clickable frame. Coordinate input found no window,
keyboard focus failed to advance in the editor and captured pixels lagged the
accessibility tree. The trial stopped before any gallery read, assignment,
profile save or Monitor preview. The input and capture cause remains open.

The renderer regression uses the existing Edit Profile and Monitor views
with a simulated profile transport. It selects an installed pack, checks the
revision-checked write preserves unrelated profile metadata, clears the
optimistic cache, reloads the saved value and verifies Monitor publishes the
exact assigned sprite from the same Local route. Both focused suites pass
18 tests. This proves the renderer handoff through the test transport. The
first Mac attempt stopped before the save and visual preview.

The native run used a synthetic worker observation and no model generation.
Peak sampled RSS including the observer was about 893 MiB, with at most four
product processes. The test app and gateway both closed.

# Keep the canvas readback hint for character previews (unreleased)

Two fresh Mac Local fixture runs drew the same five atlases in the same
632 × 325 panel at 2× scale. The trial omitted the canvas readback hint only
for read-only preview sprites. The paired run retained it. The renderer's
animation, capture dimensions and atlas fingerprints matched. All five
sprites moved through six observed frame positions in both runs.

| Preview context | Median summed RSS | Median summed macOS physical footprint | CPU, one core = 100% |
| --- | ---: | ---: | ---: |
| Readback hint retained | 492.8 MiB | 181.4 MiB | 5.03% |
| Readback hint omitted | 542.7 MiB | 333.8 MiB | 5.01% |

Omitting the hint added 152.4 MiB of physical footprint with essentially the
same CPU use. Most of the increase appeared in the main process, which also
accounts for graphics in this fixture. These measurements do not identify
individual graphics allocations. The experiment was reverted. The retained
regression test checks opaque and transparent mascot hits and verifies that
pointer movement over previews requests no canvas context for alpha sampling.

Both launches checked zero Desktop SSH after 60 seconds before capturing
their owned overlay. Each used at most three product processes and left
none running. Each measurement used a steady 20-second window before any
capture. The result applies to this synthetic Mac fixture. The five-pack
resource budget and the real Edit Profile to Monitor walkthrough remain open.

# Where the pet overlay uses memory (unreleased)

Five fresh, local-only Electron runs used the same Desktop renderer build and
overlay preload. They spent about 20 seconds in a steady phase before capture.
The four overlay modes used a fixed 632 × 325 logical-pixel panel at 2× display
scale. The blank mode mounted only a transparent document. The atlas-free mode
loaded the production overlay with an empty atlas. The last two modes drew the
mascot and five distinct character packs through the existing native IPC.

| Mode | Median summed RSS | Median summed macOS physical footprint | CPU, one core = 100% | Overlay renderer footprint |
| --- | ---: | ---: | ---: | ---: |
| Main window without overlay | 261.4 MiB | 69.3 MiB | 0.85% | — |
| Blank overlay | 349.9 MiB | 89.9 MiB | 1.69% | 17.1 MiB |
| Production overlay without an atlas | 424.7 MiB | 123.7 MiB | 2.62% | 48.0 MiB |
| Existing mascot | 440.1 MiB | 132.5 MiB | 3.51% | 56.5 MiB |
| Five distinct character packs | 500.2 MiB | 181.9 MiB | 4.50% | 96.7 MiB |

The blank window added 20.6 MiB. Loading the production overlay added 33.8 MiB
above blank. The mascot added another 8.8 MiB, and replacing it with five packs
added 49.4 MiB. Five packs used 58.1 MiB above the atlas-free production mode.
That difference includes decoded art, canvas, labels, animation and preview
traffic. Measure those costs separately before choosing an atlas or canvas
change. The full five-pack overhead was 112.6 MiB of physical footprint and
3.66 CPU percentage points, above the release budget.

Both empty modes captured fully transparent pixels. The mascot matched its
own atlas, and all five distinct packs moved across eight captures. Each mode
had a zero Desktop SSH check after 60 seconds, used at most three product
processes and left none running. Graphics accounting is included in the main
process for this fixture. These are single-run, process-level measurements from
a synthetic Local fixture. The full Edit Profile to Monitor walkthrough and
real bot events remain open.

# Pet overlay boots without the Desktop shell (unreleased)

The renderer selects `?win=overlay` before loading the Desktop shell,
app-only stores, providers and clipboard setup. The overlay keeps the
same URL, shared styles, transparent first paint and native window/IPC
lifecycle. Normal Desktop, HUD, secondary, browser, quick and wake
routes retain their existing bootstraps. Seven route tests cover the
dispatch boundary. The overlay isolation case fails before this split.
Seven additional theme and character preview cases pass.

The Vite manifests show the static JavaScript reachable from the entry
and selected overlay branch falling from 147 files (9.22 MiB) to 48
(3.68 MiB). The app bootstrap stays outside the overlay load graph.
The local Electron fixture matched the earlier work: five distinct
moving packs, mascot restoration, then a new overlay window receiving
and drawing the mascot. Capture and reopen were outside measurement.

| Steady phase, about 20 s each | Mean summed RSS | Mean summed macOS physical footprint | CPU, one core = 100% |
| --- | ---: | ---: | ---: |
| Main window without overlay | 259.5 MiB | 68.9 MiB | 0.74% |
| Existing mascot | 434.0 MiB | 125.0 MiB | 3.12% |
| Five distinct character packs | 510.1 MiB | 189.7 MiB | 4.38% |

Five-pack RSS overhead was 250.6 MiB, compared with 307.9 MiB in the
previous fixture run. The current full overhead still misses the target:
120.8 MiB of summed physical footprint and 3.64 CPU percentage points.
The overlay renderer itself accounts for 96.2 MiB of the five-pack
footprint. No prior physical-footprint measurement exists for comparison,
and the single sample pair establishes no CPU saving. The final fixture
ran 60.079 seconds with zero Desktop SSH before capture, used at most
three product processes and left none running. Full Desktop settings
and Edit Profile to Monitor have not been walked through natively.

# Five character packs — native Mac overlay measurement (unreleased)

The current Desktop renderer and native overlay IPC ran in a fresh, local-only
Electron fixture with no gateway, saved connections or inference. After 60.063
seconds in overlay mode with zero Desktop SSH processes, the exact overlay
renderer captured the mascot, five simultaneous distinct packs and the restored
mascot. Eight source frames contained all five assigned colors in order. Each
sprite moved through six observed positions. The local GIF retains seven
encoded frames. Image checks normalize each embedded display profile to sRGB.
The independent app-scoped agent-desktop capture returned `WINDOW_NOT_FOUND`;
the image evidence comes from the owned Electron window's `capturePage`.

| Steady phase, about 20 s each | Mean summed RSS | CPU, one core = 100% | Product processes |
| --- | ---: | ---: | ---: |
| Main window without overlay | 273.2 MiB | 1.45% | 2 |
| Existing mascot | 514.1 MiB | 3.61% | 3 |
| Five distinct character packs | 581.1 MiB | 3.88% | 3 |

Five packs added 67.0 MiB and 0.27 percentage points over the mascot. The full
overlay added 307.9 MiB and 2.43 points over the no-overlay main window, missing
the approximately 60–80 MB and 1–2% budgets in this fixture. RSS can count shared
pages more than once. This is one comparison with synthetic sprites, without
full Desktop startup, Edit Profile and Monitor interaction, real bot events or
a production memory claim. Screenshots and the GIF were taken outside the
sampled phases. The run closed all three product processes, with 695.6 MiB peak
sampled RSS including the observer.

The first trial stopped after a premature mode change and a changing baseline
process set. The second reached Local60 but stopped at a raw RGB check. The saved
frame reproduced the check failure and passed embedded-profile conversion.
Both failures remain recorded separately. A fresh final trial used identical
production bundles with the corrected private observer. No product source,
dependency, release or version changed.

# Installed characters stay offline — Local Desktop dispatch (unreleased)

The existing Desktop WebSocket admits these RPCs through its shared handlers
after the authority's profile check. An installed-only request used to start a
Petdex prefetch. The Mac regression recorded three prefetch calls across three
installed-only reads before the fix and zero afterward. The full gallery still
merges its explicitly requested catalog with installed packs.

Four route cases use real issued tickets and the production WebSocket request
dispatcher with synthetic transport frames. They verify independent gallery
and atlas bytes for a shared slug, denial for unserved or out-of-scope profiles
and a worker grant, and Local roster metadata, save, stale-write refusal and
clear through the existing profile writer. The focused run passed 20 tests
including the sprite and generated-contract suites. Network and SSH execution
were blocked for this invocation. No Electron window was launched.

# Per-bot characters — source and contained Mac handlers (unreleased)

Six focused Desktop files pass 50 cases. They cover the installed-only picker,
unchanged and cleared metadata, stale or evicted sprite responses, malformed
atlases, and per-actor rendering. The renderer type check, build and scoped
lint pass. The canonical Python test runner passes 14 sprite-handler and two
generated-contract cases, including invalid file references and corrupt images.
Changed patch sections apply and reverse against the pinned base. All unrelated
sections retain their original bytes.

One contained native pytest exercises real gallery, thumbnail and sprite
handlers against two profiles with the same slug and different art. Real
`profiles.configure` saves and clears the assignment, rejects a stale save and
preserves unrelated metadata. The trial restores fixture configs and verifies
pack and avatar bytes. Four returned PNG/WebP payloads pass the production
TypeScript validator. The handler measurement samples 267 MiB peak summed RSS
including the observer, with at most three controlled processes and zero
survivors. It measures the fixture, not the Desktop overlay.

This earlier trial covers the shared RPC handlers and client source. The later
Local Desktop dispatch trial above covers the canonical WebSocket's shared
handler path. Native Desktop pixels, event animations and five-character
CPU/RAM acceptance remain open.

# Profile-bound pet RPC — contained Mac handler acceptance

One fresh real pytest passes actual gallery/thumb requests for two isolated
profiles with the same slug and different original sprite bytes. Gallery names
and decoded thumbnails stay profile-specific; a missing profile fails. Root and
profile configs and installed packs remain byte-identical, with no global pet
selection. This is in-process native handler proof, not app startup, UI routing,
per-bot animated assignment, real remote catalogs or five-character CPU/RAM.

A separate preflight passes the strict owner-read/child/exec/protocol boundary.
The private fixture then proves seven exact local metadata reads and eleven
pre-exec refusals, including changed cwd/argv/environment, remote/SSH and a
closed-phase read. Git executable/config/refs/source hashes are pinned; configs,
protocols, hooks, fsmonitor, lazy-fetch and replacements are restricted. Only
metadata import can use the finite allowance; it closes before RPC. Actual
pytest suppression plus an explicit warm empty catalog prevents prefetch.
951Python origins stay in the workspace;410libraries contain no owner Hermes
runtime. No unexpected event, retry or guard relaxation occurs.

Trial1.598s/238911488B sampled including guardian/max3controlled processes,
0recorded survivors. These are fixture costs; external controllers/advisor are
excluded. One consultation, supplied facts only. Earlier218/219failures remain
failed. [Procedure and limits](native-checks-and-test-memory.md#profile-bound-pet-rpc--contained-mac-acceptance).

Source/patch/selection/default/version/release unchanged;7matching source hashes
reuse38UI/type/build evidence. Required companion/tracked-copy/secret gates
remain separate. No owner app, ai/onex2/other host, permission audit/input,
Hermes inference, ESTOP/pause/timer or adoption action. Capture/input lease and
full character acceptance remain open.

# Workspace runtime boundary — controls complete, native handler proof incomplete

A reusable workspace copy of the public interpreter/runtime/test packages now
boots inside the unchanged strict owner-Hermes-home read fence. Source tools and
owner state are not modified. Fresh venv/path handling keeps copied executable
`.pth` hooks inactive and resolves all symlinks within the bundle. The complete
repaired preflight passes:413module origins/405libraries avoid owner runtime,
parent/child read-deny controls pass, the resolved transport-helper executable is
denied, and Git file transport is refused. Exact guard/interpreter hashes bind
this to the later trial. [Scope and procedure](native-checks-and-test-memory.md#workspace-runtime-under-a-strict-hermes-home-read-fence).

Original preflight remains failed at `copy2` system-flag metadata preparation.
Before another operation, a public/private plan amendment permits one distinct
byte-only exec-control, one complete preflight and then one actual pytest only
if all controls pass. The repaired preflight passes; no guard weakening.

That one actual pytest fails before pet RPC assertions. Normal package import
requests workspace-local Git version metadata; its unexpected-subprocess audit
blocks the attempt before execution. No RPC/startup/UI acceptance, retry or
subprocess exception is claimed. Runtime/controls are the completed milestone;
full native source-isolation acceptance is still open. Round218 failures remain
failed. One fresh actual handler trial, two consultations, no review chain.

No product source, patch section, test selection, dependency lock, defaults,
version/tag/release or owner-app adoption changes. The7matching source hashes
reuse38UI/type/build evidence rather than rerun it. Current required companion,
tracked-copy verifier and secret gates remain mandatory. No owner app, ai/other
host, permission retry, input, Hermes inference, ESTOP, pause or timer action.

New GOAL lead notes report Monitorv0.34.0 released/tagged/pushed and Mac Screen
Recording granted. These close the stale release/capture-grant statuses; they
do not prove app adoption or native input/act/verify. This round performs neither
permission audit nor input. Canonical lease behavior stays untested.

# Pet picker source isolation — offline source fix, unreleased

PetTab formerly queried the active gateway and cached thumbnails by slug even
when its bot/creation target belonged to another source or profile. Required
captured source/request pairs now flow from both dialogs through AvatarPicker.
Owner-aware edit reads preserve aliases and fail closed for a removed owner.
Creation reads pin the intended backend/profile where scoped RPC is available;
legacy unscoped behavior remains. Source-keyed gallery lifetime/query identity
and source+slug+URL thumbnail identity keep the shared120entry LRU bounded.
A click generation invalidates stale results on newer picks, removal or unmount.
No persistent assignment field, global pet selection, extra provider or setting.

Four mounted regressions fail on the original picker. The fixed picker passes
all8cases (four new/four existing), including same slug/different source icons,
routed gallery/thumb calls, URL changes and late-source/older-click/removal guards.
Both parent bindings execute captured request callbacks; alias rewriting, removed
owner refusal and selected creation target are checked. Final3files/38tests pass,
one worker, no retries. A first command used the wrong installed Vitest path and
never reached tests; its failure remains. The first caller suite has37pass/1fail
because a new exact label matcher missed the existing current-source suffix;
using the established accessible-name matcher gives18creation cases, then the
final38case suite passes. No product workaround for that fixture issue.

Renderer types and a production renderer build pass. Scoped lint has0new
messages; the same7pre-existing create-dialog diagnostics remain, verified
against its backed-up original. Six other changed files are clean. The final
post-test edit only adds the lint-required blank line; the current source is
built. Existing dynamic-import build warning remains. No unchanged full source,
Desktop or mock suite is rerun or summed into these counts.

Native attempt1 calls real pet.gallery(localOnly) and pet.thumb handlers against
two isolated profile directories with the same slug and distinct original fixture
sprites. It verifies different galleries/thumbnails, missing-profile refusal and
exact config/installed bytes. An explicitly warm empty catalog avoids catalog
prefetch; no service or app is launched. Functional assertions pass, but process
receipts expose gateway-import update prefetch invoking Git against a local
repository outside the fixture home. The guard omitted owner-read denial.
That attempt is INVALID for isolation; raw functional proof/receipt is retained
unchanged with a separate rejection. No owner write or remote/SSH connection is
observed; this does not establish that the owner repository was untouched.

A second separately prepared actual-pytest fixture uses the upstream supported
background-prefetch test mode, plugin/conftest/cache suppression, all outbound,
owner-read and Git protocol/exec fences, plus owned parent/child/exec controls.
It exits1before pytest, controls or RPC because the interpreter's base runtime
is inside the denied owner tree (encodings import fails). Controls are prepared,
not proved. No permission change, fence weakening, third native launch or third
advisor call. Neither attempt establishes isolated native UI/backend acceptance.
Both recorded process trees close with0survivors; raw failures remain failed.

The completed milestone is the offline source/consumer fix. Native startup/UI,
per-bot animated assignment and five-character CPU/RAM acceptance stay open;
no version/tag/release/adoption. Two advisor consultations used supplied facts,
not independent inspection. No owner app, backend switch, Hermes model inference,
ESTOP/pause/timer or remote-host control. Only changed patch sections are exported.

# Character-pack creator skill — native tooling slice, unreleased

The self-contained `skills/character-pack-creator/SKILL.md` guides a brief or
permitted reference through state planning, original/owned frames, exact native
atlas assembly, lint, terminal preview and requested import. It uses the existing
composer/CLI/store; no provider, generator, dependency, runtime configuration or
stable patch change. It preserves actual art permission/provenance and separates
creation/import from global selection. Extended formats/events and per-bot
assignment are explicitly outside the current contract.

Frontmatter validation passes. A one-file copy in a new isolated profile is
found/read by native `find_all_skills`/`skill_view`; the returned bytes match the
shipped skill. Home, config, skills/search roots and pets destination are checked
inside owned directories before use. The exact embedded recipe is executed from
an unrelated cwd using original CC0 Lanternling example frames: all nine atlas
rows lint without warnings. It refuses an existing output without changing its
bytes and rejects wrong-sized input before creating output. The manifest example
is parsed and filled with the fixture's actual author/licence.

Twelve native operations have expected observed exits: skill/read/assembly,
three command helps, folder lint, invalid manifest, non-TTY preview refusal,
actual pack PTY preview, import, list, duplicate refusal and removal. Preview
emits39encodedframes/20distinct with one cursor restoration; this is terminal
output, not physical appearance. Only the test import is removed; source pack,
prior entry and config remain byteexact. No automatic selection, leftover staging
or recorded survivors. Seven relevant source hashes match unchanged patched files or the pinned
upstream base; prior source suites are not rerun or added to this count.

Private harness attempt1 failed generated-entry escaping before source imports.
The repaired attempt passes discovery/assembly/help/lint/error behavior, then
stops because its expected no-TTY message differs from the real diagnostic;
exit1 and the source identity are correct. Both failed receipts stay failed.
After checking the actual diagnostic offline, only the five unexecuted commands
run in a bounded continuation in that owned profile. No product fix, full-sequence
retry, extra advisor review chain or acceptance of a failed scenario.
Repaired run9.648s and continuation16.024s; sampled peak164151296B including
guardian, at most3product processes. These costs do not prove Desktop or saving
budgets. Original syntax failure adds0.072s/31784960B sampled separately.

This verifies deterministic tooling/discovery and embedded recipe behavior only.
No independent artist-agent/image-tool evaluation or new art-generation request;
creative quality, instruction-following, physical/Desktop visual evidence and
five-character CPU/RAM acceptance remain open. Only Mac native runtime checked.
No owner app/data, backend switch, connection, model inference, permission retry,
ESTOP, pause or timer action. The full characters feature remains unreleased.

# No-overwrite creator pack import — Mac CLI step, unreleased

`pets import DIRECTORY SLUG` uses the existing bounded snapshot loader and pet
store classes. It accepts only a canonical1–64character slug before store access.
The checked image bytes, creator manifest and standard pet.json are written into
a private container/payload layout below the store. Existing enumeration ignores
that unfinished container. One native no-replace directory operation publishes
all closed files; no existing target is removed or replaced. No automatic
selection, force flag, new createdBy enum, renderer, model call or dependency.

Darwin uses SDK-verified renamex_np/RENAME_EXCL; Linux uses renameat2/NOREPLACE;
Windows uses os.rename's documented existing-target refusal. Missing native
support or an unsupported filesystem fails closed. Only the Mac native path is
executed here; no OS faking or other machine use. Atomic visibility is separate
from crash durability and assumes a trusted/stable store parent. Cleanup errors
are logged without changing the committed result or masking a prior failure.

The old CLI first rejects the absent import command (intended RED). Thirty new
import cases plus9existing engine and37folder validation cases pass (76total),
one canonical worker/no retry. Real Mac filesystem cases cover existing file,
empty/full directory, live/dangling symlink, a target created at publication,
two threads/one winner, hidden staging, retained creator metadata, exact immutable
bytes despite source replacement, WebP/store/renderer compatibility, each write
fault, publication/native-capability refusal, cleanup faults before/after commit,
canonical slug checks, warnings, invalid images and no selection/config changes.
Scoped Ruff passes. Linux/Windows marker arms are not native acceptance here.

Actual source CLI from a backed-up isolated profile passes nine sequential
cases: import0/list0/duplicate1/empty-target1/bad-slug1/installed-show0/select0/
select-original0/remove0. Each binds importer/loader/CLI hashes. Import/list/
show/collisions leave config byte-identical; only explicit selections change the
fixture, and its original config is restored afterward. Original entry and source
pack stay byte-identical; creator metadata and image survive import. The imported
directory is owner-private on this Mac. The installed preview emits39actual
encoded terminal frames/19distinct chunks, restores the cursor once and exits.
No staging or recorded process survives. Native21.464s/peak172703744B inclguardian,
max3product processes (4including guardian); external controllers excluded.
This is terminal/filesystem proof, not Desktop pixels or five-character CPU/RAM.

Four changed source/test sections apply/hash/reverse/hash against pinnedbf0203a;
unrelated sections stay exact and two Python regressions append. Required
companion/tracked-copy/directory+history gates are recorded privately. No Hermes.
app/CUA/permission retry, owner app/data, otherhost/ai, ESTOP/pause/timer/settings
change. No version/tag/release/adoption; full formats/events/per-bot assignment,
creator skill and native character/resource acceptance remain open.

# Pre-install creator pack preview — native terminal step, unreleased

`hermes pets show --pack DIRECTORY --cycle --once` previews the existing seven
canonical activities without installing/selecting a pet. The shared loader
returns the exact bounded bytes it validated; `validate_pack` keeps its previous
report-only API. A trusted private temporary snapshot feeds the existing renderer
and animation loop. Pack mode branches before pet-config/installed resolution.
Slug+pack, malformed input, missing requested frames and unavailable TTY report
errors. Snapshot cleanup and cursor restoration cover normal exit and Ctrl+C;
handled I/O/value errors report failure, unexpected errors still propagate after
cleanup. Existing installed-show loop/precedence/error behavior is preserved.

Three intended RED journeys first reject the absent `--pack` option. The first
new-suite attempt instead hits a test-fixture TTY seam: pytest replaces its
capture stream after setup. Patching the current stream at call time fixes that
fixture; no renderer fix is inferred. Sixteen real parser/Pillow cases now pass,
including exact seven-state colours/once count, explicit-state precedence,
default idle, immutable source-to-snapshot bytes even after source replacement,
WebP, bad packs, conflicts, no TTY, snapshot-write/init/animation error cleanup,
Ctrl+C and missing frames. Six installed-preview plus50validation cases also
pass (72total), one canonical worker/no retry. Only external stream capability
and sleeps are controlled; real renderer/pixel encoding runs. Scoped Ruff passes.

Three sequential bounded native PTYs run the actual source CLI from owned homes,
with no renderer/time/TTY stubs. A coloured native atlas emits the seven canonical
states in order,42frames, one cycle and exit0 (11.719s). Original CC0 Lanternling
emits39frames/20distinct encoded chunks, with4distinct idle chunks (10.231s).
Its infinite idle preview receives SIGINT only after a real rendered frame and
returns0 with cursor restored (1.499s). Every case restores the cursor once,
keeps source-pack/config bytes unchanged, creates no installed pet store and
leaves zero snapshots or recorded survivors. Source hashes bind both modules.
The highest native sampled RSS including guardian is190595072bytes, at most
3product processes; the external shell/controller is excluded. These are
terminal-output/cleanup checks, not physical font/graphics appearance, Desktop
movement, full-task memory savings or five-character CPU/RAM acceptance.

Three changed source/test sections apply/hash/reverse/hash against pinned
`bf0203a`; unrelated sections stay exact. One Python selection appends. Required
companion/tracked-copy/directory+history gates are recorded privately. No native
Hermes.app/CUA/permission retry or owner app/config/data change, no otherhost/ai,
ESTOP/pause/timer action. No version/tag/release/adoption. Pack install/assign,
extended format/events and full native character acceptance remain open.

# Character creator folder lint — unreleased development step

`hermes pets validate DIRECTORY` reads a draft schema-1 `hermes-native-atlas`
manifest: name, author, licence and one static native atlas. Name/author/licence
are bounded inert printable text; unsupported fields/schema and duplicate keys
fail. JSON is capped at64KiB and the sheet at16MiB. Files are regular and local,
with no symlink components or asset subpaths; bounded reads compare opened file
identity and use nonblocking/no-follow flags where supported. A replaced FIFO
fails without blocking. This is stable-folder read-only lint, not an installer
or a guarantee against hostile concurrent directory replacement.

Image checks are factored from the existing CLI handler and still call the real
generation validator. Raw IMAGE behavior, including user-selected image symlinks
and missing-row warnings, is retained. Packs additionally require a populated
idle row. No metadata setting affects a renderer or profile; unsupported fps,
anchor or event mappings fail rather than imply working runtime controls.

Thirty-seven new real parser/Pillow cases plus13existing IMAGE cases pass with
one canonical worker/no retry: valid PNG, WebP with printable Thai/BOM metadata,
no folder writes, schema/field/control-text errors, duplicate/deep/malformed/
oversized JSON, traversal/absolute/URL/nested assets, directory/file symlinks,
missing idle, animated content, oversized assets, special files and replacement
file/FIFO identity refusal. Scoped Ruff covers both source files, the new tests
and example recipe. No unchanged full source/desktop suite is claimed.

Actual source CLI from owned scratch generates the original CC0 Lanternling
example, validates folder and image, shows help, rejects the blank template,
and refuses to overwrite the existing output folder. Case exits0/0/0/0/1/1;
example bytes/config stay unchanged and previous config state is restored.
The first harness run stopped after an overly strict help assertion ignored
argparse line wrapping; that failure is retained. A distinct run normalizes only
observer whitespace and completes all cases with unchanged product source.
The atlas was visually inspected as a native-sheet example, not a Desktop frame.
No model, asset download, Hermes.app/CUA or permission action occurs this round.

Three changed source/test sections apply/hash/reverse/hash against pinned
`bf0203a`; unrelated sections stay exact. The new Python regression appends to
the existing selection. Required companion/tracked-copy/directory+history gates
are in the private round evidence. Full pack format, install/assign, preview,
character interactions and five-actor visual/CPU/RAM acceptance remain open.
No version/tag/release/adoption or ai/otherhost access.

# Local sprite atlas validation — creator step, unreleased

`hermes pets validate <spritesheet>` is wired through the real pets parser and
existing command table. It checks a regular PNG/WebP file (at most 16 MiB), native
1536x1872 header geometry before pixel decoding, and a static image. The existing
generation validator supplies occupancy, size/collapse/outlier and transparent
RGB diagnostics. Populated rows and absent-state warnings are printed; warnings
alone return 0 and errors return 1. No second pixel validator or dependency.

The old CLI fails the new missing-state-warning journey because `validate` is
not a command. With the new handler, 13 parser/Pillow cases pass: native PNG/WebP,
unchanged fixture files, visible missing-state warnings, empty/residue errors,
geometry rejection before load, animated PNG/WebP rejection, missing/corrupt/
oversized/directory/GIF input. Six neighboring preview cases pass. Scoped Ruff
passes. The canonical runner uses one worker/no retry; its scratch root and
serial targeted precompile stay inside the isolated task. No broad source suite
or full unchanged selection is claimed.

The actual source `hermes_cli.main` runs from an owned directory outside the
source tree with an isolated backed-up home. Valid, missing-file and help cases
return 0/1/0 with expected output. Atlas and fixture config stay byte-identical;
prior config state is restored. These are native CLI checks using synthetic
geometric artwork, not desktop images or a complete character pack.

Two source/test sections are exported against pinned `bf0203a`; changed-section
apply/hash/reverse/hash checks pass. The new test appends to the Python selection;
unrelated patch sections and selection order remain. Companion tests, tracked
copy release verification and directory/history secret scans are recorded in
the private round evidence. No version bump or character feature release.

The UI attempt in this round remains failed: the first launch never reaches
bootstrap; the distinct relative-entry fixture reaches Local60 (60.048 seconds),
zero Desktop SSH and a native panel media identifier. Exact app/window capture
then reports `PERM_DENIED: Screen Recording permission not granted`. Both trials
close with zero recorded survivors; no third launch, permission change or input.
No five-actor image/motion/restoration or CPU/RAM result is accepted. Raw private
trial receipts, CLI stdout/stderr, source bindings and config backups remain in
`../uitest-v090-c2q4iijp/characters-r213` and `characters-r213-fixed`.

# Bot character overlay preview — offline source step, unreleased

The working source adds an explicit Monitor character preview through the
existing plugin pet door, overlay IPC and PetSprite. No new model request,
roster polling, gateway or per-character process/window is added. A loaded,
enabled pet is required; its sheet is shared as display input. The first slice
is read-only and cannot use the global mascot composer to submit a prompt.

Source tests cover the real plugin publisher and overlay mirror, source/stable
identities and deterministic five-actor limit, replacement/empty updates,
superseded/disposed ownership, bounded safe text and old/future snapshot lease
bounds. The lease expires 15 seconds after the source observation; clicking
preview cannot refresh old work. Monitor tests exclude retained/unavailable,
unknown/unqualified and idle historical-error rows, ended/stale/identity-less
workers, and clear on read error, unmount and explicit Stop. No request or chat
open is caused by those snapshots. Nine locale bundles have the new copy.

The actual receiver is tested with safe text, explicit poses, a bounded list,
paused/stale frames, reduced-motion static poses and normal-mascot restoration.
Canvas scheduler tests prove static semantic-state repaint without animation
timers and a 15 fps sprite ceiling. Native IPC tests cover hide/minimize,
lock/suspend/resume lock preservation, return to mascot mode and disposal on
overlay closure without a final state push. These are source/unit contracts;
mocked native events and canvas contexts are not macOS visual acceptance.

Meaningful RED cases precede the missing plugin door, source observation expiry,
sprite cadence/static rendering, Monitor opt-in, receiver behavior, lock latch
and native overlay-close cleanup. Focused UI run: 58 cases pass; after affected
code changes, 24 impacted cases pass again. The final native IPC suite passes
two cases. Renderer and Electron types pass. Scoped lint has no errors; one
unchanged pre-existing `document` warning remains in the sprite test. Production
renderer and the changed native IPC bundle build; the existing Vite
ineffective-dynamic-import warning remains. No full unchanged engine/Desktop
or mock sweep is claimed.

Two distinct fresh native hosts attempted the actual production overlay
artifact with an owned geometric atlas and synthetic observations. Each main
control renderer crashed before control HTML/overlay-window creation, reporting
`Failed to initialize sandbox.` The IPC module was imported, but the production
overlay renderer never loaded. Trial one closed two processes after 2.65s,
sampled peak 181,157,888 bytes including guardian. Trial two verified owned
Cocoa home/temp/appData/log/crash paths, then failed identically and closed two
processes after 2.62s, peak 191,823,872 bytes. Neither reached Local60, CUA,
screenshots, five characters, or performance measurement. These startup peaks
are not overlay RAM measurements. No further native trial in round209.

The narrow sandboxd query had no matching records. Static comparison found that
the earlier working harness leaves Electron to Chromium's sandbox under Node
guards, whereas these trials also applied an outer Seatbelt profile. That is a
diagnostic lead, not a demonstrated cause. Existing crash/startup evidence must
be attributed before another launch; no sandbox or permission bypass was used.
Raw failures, ownership/closure receipts, scripts and source checks remain at
`../uitest-v090-c2q4iijp/characters-r209`. No owner app/data, other host or ai
connection, credential, permission, ESTOP, pause or timer change.

Only 16 changed source/test sections are exported against pinned
`bf0203a794a07aac3ff764972ab9087baa4e4f4e`, with apply/after-hash/reverse/before-hash
checks and unrelated sections retained. Desktop selection appends the affected
tests; Python selection stays unchanged. This completes an offline development
step only. Full native rendering, persistent tracking, interactions/output
preview, packs, display-only sleep and five-character CPU/RAM acceptance remain
open. No version, tag, adoption or release.

# Pet overlay theme-font fix — source acceptance, unreleased

One fresh round210 fixture reused the earlier working Chromium-sandbox launch
path with Node I/O/network guards, independently contained child processes,
blackhole proxy and per-session canonical-file/network/navigation/IPC gates.
This is not equivalent to an outer OS sandbox against a compromised privileged
Electron process. Chromium sandboxing remains enabled; no permission or system
setting changed. Pure guard self-checks pass (19 checks).

The owned control renderer loaded, then production overlay loading attempted a
Google Fonts Courier Prime stylesheet. The native URL gate rejected it before
network connection. The trial failed and closed all three processes after
25.91 seconds, sampled peak 548,421,632 bytes including guardian, zero survivors.
This proves a startup blocker was reached, not native character acceptance or
the cause of round209's earlier sandbox failures. No second trial was run.

`applyTheme` injects the font link both at module boot and provider paint. Its
shared font-link branch now skips exact `win=overlay`; palette/typography and
local font stacks remain. Main, HUD and secondary window font loading stays
unchanged, and suppressed links never enter the deduplication cache. Other
custom CSS or asset URLs are outside this fix.

The cold-import regression intercepts real head publication before importing
the module and never attaches the external resource. It fails before the fix;
three main/HUD/secondary controls already pass. After the fix all four new
cases plus 23 neighboring theme cases pass (27 total). They cover provider
paint, theme/mode changes and a later normal paint reusing the same module to
check the skipped font was not cached. Scoped lint has zero errors/warnings;
renderer types and a separate fixed production renderer build pass. Failed
native artifact hashes are kept separately from the fixed artifact hashes.
At completion of round210 no native run after the fix, Local60, CUA,
screenshot, actual Monitor/bot flow, five-character CPU/RAM or whole-task saving
was claimed. The following attempt records the later, limited startup evidence. Failed raw state and
receipts remain at `../uitest-v090-c2q4iijp/characters-r210`.

Two source/test sections are exported against the same pinned upstream base,
with apply/after-hash/reverse/before-hash checks and all earlier sections kept.
The kit now has 1151 paths. Desktop selection appends this test (179 total);
Python selection remains 1536, with prior ordering/other keys unchanged. No
version, tag, adoption or release. Next is a fresh contained Local-only native
trial of the fixed overlay; full characters capability remains incomplete.

# Character preview native attempt — startup progress, UI proof blocked

Round211 reused 18 still-matching feature/theme source hashes from committed
`a4c3a2d`; no product source, patch section, target or test-selection change.
Fresh renderer and native IPC builds pass under the bounded runner. The launched
fixture binds its actual source/build/guard hashes and exact loaded overlay URL;
27 theme cases and earlier feature unit results are reused, not rerun or summed.
The Chromium sandbox, guarded Node I/O/network, OS-contained child processes,
per-session URL/navigation/IPC fences and isolated Cocoa/home/app-data paths
remain. They do not establish equivalent outer OS protection for privileged
Electron. Nineteen URL/IPC controls and one positive/19 negative observer
controls pass offline; no permission or owner-data changes.

One fresh native trial loaded the control and production overlay document.
Local60 passed after 60.060 seconds in overlay mode: DesktopSSH0, no gateway,
model or external request/refusal. The round210 Google font refusal did not
recur. Original PID/birth/nonce, main+overlay IDs/URLs, native visibility/unlocked
state and artifact identity are checked before/after CUA observations. Screen
was unlocked before launch; no input to owner apps or other machines.

CUA paired AX/images show only the control window: Mode normal, then Mode actors
after its real Preview button. They are not pictures of a mascot or five actors.
The overlay preload receiver's telemetry remained null. No actual overlay-state
receipt, five-character frame, motion or mascot restoration is established.
The next stop-preview request was refused because the acceptance reserve was
below 20 seconds; no stop-preview input occurred. Permanent INVALID/STOP then
closed all three native product processes, 217.870 seconds, sampled peak
594,821,120 bytes including guardian, zero survivors. This is an observation-
budget refusal, not proof the 240-second total deadline expired. No second trial
or changed live criteria. CUA completion summary was sent once.

Raw phase metrics were generated for windows named no-overlay/main, mascot and
actors. Those labels do not prove the rendered states. Receiver acknowledgement
and visual actor/motion evidence are absent, so the measurements are explicitly
unaccepted for 13c CPU/RAM comparison. `measurements_completed` in the original
closure means the sampler collected a phase, not that characters rendered.
Original measurement/closure files remain unchanged beside a separate
`acceptance-qualification.json`; no budget or saving claim follows from them.

Read-only attribution found a fixture evidence-loss defect: installed Electron44
`electron.d.ts` gives event details as the first console-message argument and a
deprecated numeric level as the second. The fixture read the second as details,
logging only `3`; its error-severity check could not fire. The missing message
cannot be recovered, and the renderer's cause remains unknown. A separate
next-attempt adapter now projects first-argument message/source/line/severity
and explicitly rejects numeric/malformed events. Ten synthetic contract cases
and syntax checks pass; this adapter was not part of the failed native trial
and proves no native error recovery or product fix.

Private paired observations and limits:
`../evidence/bot-characters-native-attempt-20261117-r211`. Raw states, signed
fixture metadata, launched scripts/build hashes, receiver/console records,
closure and offline preparation: `../uitest-v090-c2q4iijp/characters-r211`.
Next: use readable console attribution and mount/state-ack fail-fast gates,
predeclare an owned-overlay capture path and shorter sequence, then one fresh
contained Local-only attempt. Full characters acceptance remains incomplete.
No COMMIT-MSG for this unfinished item; no version, release or adoption.

# Overlay bootstrap diagnosis — fixture repair proven, visual acceptance open

Round212 completes startup attribution and a fixture-only fidelity repair.
Product source remains committed `a4c3a2d`; 18 feature/theme hashes, production
renderer and native IPC artifact hashes stay unchanged. No patch or selection
change, version or release. Earlier failed attempts remain failed.

One fresh 120-second diagnostic uses the corrected Electron console listener,
early overlay opening and run-bound receiver ACK gate. It stops after 6.013
seconds with the actual error: `onPreviewFileChanged is not a function` in the
production SDK chunk. Peak 506,970,112 bytes including guardian, three native
product processes, zero survivors. No Local60 or UI action occurred. Source
trace: plugin initialization calls runtime-loader's required preview-file
subscription; production `electron/preload.ts` provides it, but the private
minimal fixture preload did not. This identifies a fixture contract omission,
not a Hermes product defect.

A meaningful VM/EventEmitter regression fails on the old preload's missing
function. The repaired fixture reuses production's actual passive channel and
callback/unsubscribe behavior. Tests prove payload delivery, independent
unsubscription and zero outbound IPC; no fake/noop native capability or product
edit. Scope was explicitly amended before one distinct repaired fixture: two
round212 native trials total, no failed-generation revival or third launch.

The repaired host reuses the same current production renderer/native IPC and
all prior containment. Its real overlay receiver acknowledges the fixture
nonce and normal state; Local60 passes at 60.061 seconds without the earlier
console or font refusal. Chromium sandbox, Node I/O/network guards, OS-contained
children, own Cocoa paths and session URL/IPC fences stay. This is not equivalent
to outer OS containment of compromised privileged Electron. Resource bounds
stay at four native product processes and under 3.5 GiB.

The installed agent-desktop read-only `list-windows --app UNIQUE_NAME` returns
only the control window. Its PID/process instance matches the owned app; the
transparent panel is absent from that inventory. No guessed window ID,
unscoped/screen capture, permission change or mutation follows. The driver
closes cleanly; combined native/driver/observers sampled peak 602,357,760 bytes.
No overlay image or screenshot command was obtained. This does not prove the
driver cannot capture a panel by another properly bound native target.

No actor input, five-actor phase, motion, restoration or metrics acceptance.
The expanded visual trial remained incomplete and its guardian ultimately
fired the native total deadline; final closure is 240.872 seconds, sampled peak
565,313,536 bytes including guardian, three product processes, zero survivors.
This is not a strict 240-second total pass. The runner had waited until the total
limit instead of ending acceptance at 215 seconds to preserve cleanup reserve.
A separate next-attempt runner corrects that stop boundary; it is not yet
native-verified. No further native launch this round. CUA functions were prepared
outside the native clock; no CUA app binding/input/AX/image operation ran, and
one completion summary closed that preparation.

Installed Electron declarations document `getMediaSourceId()` as a native
window identifier whose macOS component is CGWindowID. A next-attempt telemetry
copy and strict parser prepare a run-bound own-panel target for an explicit
app+window screenshot. Two positive/eight negative synthetic parser cases pass.
No live media ID or panel capture is claimed; this is a diagnostic lead, not
permission to guess IDs or remove app scope. Resolve the capture path and
prepare every step before a fresh trial starts.

Completed handoff is diagnosis/fixture-bootstrap evidence only, suitable for a
documentation commit. Full visual/interaction/resource acceptance is open.
Raw original and repaired records:
`../uitest-v090-c2q4iijp/characters-r212` and `characters-r212-fixed`.

# Pet creator preview — native terminal acceptance, unreleased

The character creator tooling now previews every canonical pet activity through
the existing `hermes pets show --cycle --once` command. Literal atlas row names
previously excluded wave, run and jump, and the outer loop repeated the selected
sequence once per selected state. The fix uses the canonical state sequence and
exits after one full sequence; the renderer resolves its existing aliases and
legacy fallbacks. Explicit state selection still wins over `--cycle`.

Six new source cases assert the explicit seven-state order and frame count,
single waiting/default idle, explicit-state precedence and cursor restoration on
both interruption and render error. The all-state case fails on the original
source; all six plus two existing pet-toggle cases pass through the canonical
runner with one worker. An earlier runner setup failed before collection because
its scratch path escaped the isolated write boundary; that is not a product
regression. Directing scratch files into the owned test root resolved it.

Before and after native PTY trials run the actual CLI parser, pet store, atlas
decoder and renderer with identical isolated input:
`hermes pets show preview-fixture --cycle --once --mode unicode --scale 0.1`.
Executable, imported module path/hash and process lifetimes are recorded. Before:
idle/failed/waiting/review repeated four times, 16 state visits, 19.61 seconds.
After: idle/wave/run/failed/review/jump/waiting exactly once, seven visits,
9.41 seconds. Each hides and restores the cursor once, leaves configuration
unchanged and closes every owned process. No model, download or network is used.

The small synthetic color atlas establishes dispatch, loop count, CLI wiring and
cleanup, not real character-pack compatibility, artwork quality, desktop overlay
behavior or a RAM/CPU saving. Sampled peaks including the observer were
156,450,816 bytes before and 159,301,632 after, with at most three product
processes; these are not whole-service measurements. Private ANSI recordings,
receipts and test output: `../uitest-v090-c2q4iijp/characters-r208`.

Only `hermes_cli/pets.py` and the new test target are exported against pinned
`bf0203a794a07aac3ff764972ab9087baa4e4f4e`; changed sections apply, match after
hashes, reverse and match before hashes. Unrelated patch sections are retained.
Python test selection appends the new file. Desktop overlay, interactions,
latest-output popover, pack format/creator skill and five-character resource
budgets remain unimplemented. No version or release for this development slice.

# Captain provider acceptance — readiness only, unreleased

The real-provider acceptance contract now specifies one consistent read-only
choice/delegation/parent-readback case, current allowance/account/route gates,
shared counting for every upstream attempt, and actual judge-owned Done/native
UI evidence. It reuses the normal native `/goal` parser and first-turn contract;
there is no new runner, model route, request budget, configuration or runtime code.

The historical real-card allowance was raised to56 and fully used. No newer
verified allowance is established this round; actual-provider acceptance remains
owner-blocked. Selected read-only local model configuration metadata does not
prove account binding, available project allowance or provider quota. No credential
values are copied or published, and no Hermes provider inference is attempted.
The separately requested advisor consultation is not a new Hermes test allowance.

A fresh isolated offline check parses the documented goal with the actual native
parser and verifies all five contract fields reach its first-turn kickoff. It
also checks the two public fixture alternatives both evaluate to5. This proves
syntax and contract propagation only, not that a provider chose, delegated,
verified or reached Done. Existing scripted native acceptance below retains its
scope. No native UI/source/runtime/patch/default/selection/version/tag/release
change, owner-app adoption, other-host/ai connection or paid fallback.

# Captain direct Stop — native Local acceptance, unreleased

Completed native development step: a fresh source-bound Local Hermes at 480×620
shows direct composer Stop while the parent is idle and its worker runs. One
normal AX button click interrupts the owned worker and pauses the owning goal
at turn 1/20. The normal parent interrupted-result response appears; the direct
Stop button disappears after work stops. Before/after screenshots and matching
full AX are retained in `../evidence/captain-background-stop-20261117`.
The BEFORE is an older source baseline from a separate failed203 generation;
the new active/stopped/terminal frames are one original206 generation.

The real native helper proves child ended, interrupted delegation ledger and
accounted delivery/normal parent result BEFORE releasing the held server reply.
Then goal, child metadata, ledger and admissions stay exact for three seconds;
no goal continuation/new judge is admitted. Independent paused work and profile
configs stay unchanged. Original-chat UI_READY, UI_STOPPED and UI_VERIFIED ACKs
pass, followed by `goal-acceptance.json` accepted=true. Seven scripted loopback
requests (cap16 across parent/worker/judge/retry attempts) exercise real /goal,
plan, delegation, read_file and session Stop. They establish orchestration, not
provider reasoning, paid usage, real savings or arrival at a cancelled client's
callback; server-handler completion is the narrower late-reply evidence.

The fresh renderer binds to the three composer source hashes in committed112b6c2
and current Stop runtime/helper sources. Main/preload reused byte-exact. Prior203
five-file/88-case source tests, types and scoped lint are reused with exact hash
match; renderer build passes fresh. No runtime, patch, default, dependency,
permission, test-selection, version, tag or release change this acceptance round.
Existing ownership/persistence/Done/Pause regressions retain their prior scope.

One fresh trial only: Local60/zeroSSH before CUA; original PID/birth/window/URL/
generation with fresh single-use5s admissions, minimum20s observation reserve,
335s acceptance/360s total/25s cleanup, max4 product processes/<3.5GiB retained.
Invocation-local app selection avoids the prior cross-cell binding failure.
Normal History navigation settles this time; no additional input replay, menu,
keyboard, coordinate, DOM/store or control-API injection. The prepared one-shot
unmet-predicate AX/pixel diagnostic and independent guardian5s watchdog are never
invoked. Six diagnostic failure controls and existing1positive10phase refusals
pass offline; capture-hang enforcement is not livevalidated. Normal5s flights
remain; diagnostic-only minimum25s admission would be stricter than normal20s.
This pass does not explain the earlier AX/native URL disagreement.

Native elapsed186.20s, peak4 product/8 all children,1,185,759,232B sampled RSS
including guardian; external CUA/advisors/controllers excluded. These are fixture
bounds, not whole-task RAM/savings. All recorded generations and API/model ports
close, seven fixture config/env files restore byte-exact, geometry absence
restores, DesktopSSH0. App exits before gateway/model teardown. Raw:
`../uitest-v090-c2q4iijp/captain-r206-stopbutton-capture/evidence`.

Earlier201–205 failures stay failed with original evidence. Native button before/
after, interruption/paused goal and bounded held-server-reply/terminal ACK are
accepted here. Provider-backed autonomous decisions, owner adoption and first ai
connection remain separate open/owner-only work. Complete Captain capability is
still unreleased.

# Direct Stop for background workers — source step, unreleased

Historical round203 handoff below; fresh native206 acceptance is recorded above.

Native baseline AX/pixels show a waiting Captain with a running worker and no
composer Stop after its parent turn settles. The working composer now subscribes
to the existing `sessionBackgroundResume(runtimeSessionId)` live count and adds a
secondary typed Stop button while the parent is idle. It calls existing `haltRun`:
park the owning queue and invoke existing session cancellation. It does not
submit a draft or queue it. Existing Send/voice/busy-parent paths are unchanged;
no RPC, timer, dependency, permission, model call or new state store is added.

Controls regression first fails on the missing button (3 failures/20 passes).
After implementation, five focused files pass 88 tests: controls, runtime-owner
live counts, queue parking, background queue preservation and slash session
commands. Cases cover an empty minimal composer with canSubmit=false, a draft
alongside Send, one busy-parent Stop, absent live work and the disabled boundary.
TypeScript, scoped ESLint and a fresh production renderer pass. Only the three
changed patch sections are applied, hash-checked, reversed and checked against
the pinned base; unrelated patch sections and test selection are retained.

Two prior native diagnostic probes remain failed: a newly added focus requirement
refused before History; a separate scoped AX probe reached the correct waiting
chat while unfocused, then setValue did not expose the required slash menu. This
establishes neither an AX editor product defect nor Stop delivery. Baseline:
`../uitest-v090-c2q4iijp/captain-r203-stopax-capture/evidence/01-goal-active.jpg`.

A distinct fresh fixture binds the new renderer to the three source hashes and
reuses byte-exact existing native main/preload. Initial owned AX binding and
normal AX Raise complete. The guarded History step then returns -10005/
ScreenCaptureKit -3812 invalid parameters; native readiness records #/history,
but no post-action History frame/receipt exists. The helper invalidates/stops;
no Local60, actual Stop, UI_READY/UI_STOPPED/UI_VERIFIED or goal acceptance exists.
A later root error label mistakenly described initial binding failure and
replaced the helper's STOP/INVALID text; the retained per-call/lifecycle receipts
correct that label privately. The trial remains failed with no retry. This is an
unresolved observation failure, not a demonstrated product defect. Do not infer
a passing after screenshot or reuse any failed trial as acceptance.

All three trials close their recorded generations and model/API ports and restore
21 fixture config/env files plus three geometry absences; Desktop SSH is zero.
Their sampled peaks are four product processes each, respectively 1,004,978,176 B,
1,154,760,704 B and 1,021,591,552 B including guardian. External CUA, advisors and
controllers are excluded; these are not whole-task RAM or savings measurements.
New fixture: `../uitest-v090-c2q4iijp/captain-r203-stopbutton-capture/evidence`.

At the round203 handoff, the source improvement has offline coverage; native
button/interruption/paused-goal/held-server-reply/terminal ACK remain open then.
Fresh206 acceptance above closes that bounded scenario. Existing Stop gateway evidence below retains its stated scope.
Provider reasoning, cancelled-client callback arrival, ai and owner adoption are
unproven. No version, tag or release is created for this development step.

# Captain session Stop — fix and qualified desktop observations, unreleased

Historical round201 observations below remain qualified/failed as stated. Fresh
206 direct-button acceptance above does not relabel those trials.

Completed source fix: native session Stop previously cancelled a waiting worker
but left its goal active. A real gateway regression fails on that exact state
before the fix. Shared authority Stop now pauses only the owning active goal,
using its physical compression tip and profile, verifies the persisted pause,
and publishes the existing control snapshot. Absent/paused/completed goals stay
unchanged. Saving/readback failure still runs cancellation and reaches the caller.
No frontend, dependency, default, quota or permission change.

Five canonical isolated files pass 11 tests in 23.6 seconds: actual native Stop,
ownership/compression/status/refusal and failed-persistence controls, plus existing
pre-adoption/adopted/late Stop handling. Done and Pause controls pass separately
in 38.3 seconds. The full Stop regression ends the child and accounts its
interrupted delegation/normal parent follow-up before releasing the held model
reply; child metadata, delegation ledger, goal and admissions remain exact for
three more seconds. Independent paused work and config remain intact. All model,
worker and judge request attempts share a cap of 16; this is scripted localhost
orchestration, not provider reasoning. Server-handler completion does not prove
arrival at the cancelled client's completion callback.

Two separate desktop attempts remain FAILED, with no full native acceptance.
The first observer incorrectly required a document URL in the owned macOS Window
menu and stopped before the 60-second Local gate. After closure/restoration, a
fresh fixture used a menu-specific identity check, retaining native URL/window/
generation checks before and after it. One positive and three refusal controls
pass; the normal document guard is unchanged.

The second fixture passes 60 seconds Local. Original 480×620 AX/image observations
show a running worker and goal waiting, actual Desktop `/stop`, then interrupted
work and Goal paused 1/20. Native readback proves ended child, interrupted ledger,
accounted delivery and parent interrupted-result response BEFORE held reply
release. UI_READY is acknowledged. A later observer admission refuses insufficient
remaining phase budget before UI_STOPPED acknowledgment. No UI_STOPPED,
UI_VERIFIED, goal-acceptance or accepted late-reply desktop result exists. Do not
relabel either trial or restart it. Captures are qualified observations only:
`../evidence/captain-goal-stop-20261117`; raw trials and STOPs are retained.

Both trials close every owned generation and model/API port. Seven config/env
files and one geometry absence are restored per trial; Desktop SSH is zero.
The second trial lasts 227.31 seconds, peaks at four product processes and
1,196,507,136 B sampled RSS including guardian; external controllers are excluded.
The first closes in 54.65 seconds at four product processes/971,767,808 B. These
are fixture bounds, not whole-task memory or savings evidence. The initial
screen-state parser error was corrected to read the root IOConsoleLocked=false
before any CUA binding; no locked-screen input occurred.

The source fix has regression and on-screen interruption/pause observations;
full desktop late-reply and provider behavior remain open. No version, tag,
release, owner-app adoption, owner state/control change, or other-host/ai use.
The earlier acceptance sections below retain their original scope.

# Captain Pause and goal limits — native Local acceptance, unreleased

Four native regression files pass through the canonical single-worker runner:
Done control, owner Pause, external blocker and turn-budget exhaustion. Each
uses the existing real gateway/session authority, goal manager, SQLite, tools
and native judging path with scripted localhost model/judge replies. The fixture
never writes tested-goal metadata or patches the judge, manager or provider
cache. One existing helper file plus three thin case files preserve the project's
required per-file process isolation. Four changed patch sections pass apply/hash/
reverse checks; 1,130 targets, unrelated sections unchanged.

Pause is applied while the child reply is held and the kickoff admission has
settled. After the actual child result, parent verification and ordinary async
delivery settle, the paused goal remains identical at one turn. Only the original
kickoff and async-result admissions exist; no new judge/goal continuation appears
during a further three-second observation. A scripted external blocker remains
paused with zero delegated auto-continues despite delegated choices being enabled.
A configured two-turn cap reaches two actual judged turns and pauses on Continue,
with no third admission. Independent paused work and fixture config stay intact.
This proves native verdict handling and real turn-budget enforcement, not an
external credential policy or provider decisions. Each case has a shared cap of
16 parent/worker/judge request attempts.

The four isolated files pass in 78.0 seconds; sampled source RSS with observer is
457,621,504 B. A fresh production Local desktop window reuses the unchanged,
hash-bound renderer/preload. Original 480×620 AX/pixel captures show Waiting with
a running worker, actual **Goal actions → Pause goal**, then completed plan/worker
evidence while Goal paused remains at 1/20. Nine loopback exchanges include only
one pre-Pause judge. Native goal metadata equals its pre-release paused snapshot.
Both profile configs remain unchanged during the case. Private captures:
`../evidence/captain-goal-limits-20261117`.

Native trial: 166.59 seconds, 60 seconds Local, peak four product processes and
1,182,466,048 B sampled RSS including guardian, zero owned survivors. App/helper
exit precedes gateway/model teardown; seven config/env files and one geometry
absence restored; Desktop SSH zero. External controllers are excluded, so these
are fixture bounds, not whole-task RAM or savings evidence. Terminal capture
retains left-edge clipping; no general layout acceptance is claimed.

Earlier parametrized attempts remain failed: a paired run's main client retained
the prior temporary endpoint while its auxiliary judge used the new endpoint.
Pause alone passed, and failure occurred before Pause action. Changing process
HOME between gateway restarts does not establish a runtime product bug. Follow
canonical per-file isolation instead of resetting caches or changing product
routing. An edit-script error also started a stale probe; it was stopped and
its recorded generations were confirmed closed after the initial survivor
receipt. No retry relabels those attempts as accepted.

No runtime/default change, owner state/ESTOP/pause/timer/settings/permission
change, other-host/ai connection or owner-app adoption. Goal Pause allows already
running work and its ordinary result follow-up to finish and use model calls.
Full worker Stop/cancellation and provider reasoning remain open. No version,
tag or release; the Captain capability is still in development.

# Captain native goal workflow — scripted Local acceptance, unreleased

This section records round 199; the newer boundary acceptance is described above.

A new native regression creates a goal through `slash.exec`, submits its real
kickoff directive, writes the task plan through `todo_list`, delegates a native
file read, receives completion and verifies its evidence in the parent through
`read_file`. Native goal judging parks on the active delegation and reaches Done
after two turns. The fixture never writes the tested goal's metadata directly or
patches the judge/runner. Judge approval requires recorded child evidence and a
verified parent tool result. All parent/worker/judge/retry requests share a cap
of 16; the accepted case uses ten scripted localhost exchanges. The independent
goal is paused through native slash commands and remains unchanged.

The canonical per-file test runner passes the one new regression in 17.3 seconds.
Task-local launcher adaptation keeps scratch inside the authorized workspace,
uses a socket-safe short path and syntax-checks only this new file instead of
the unchanged full precompile. A Python audit guard denies shell startup
snapshots, matching the native fixture. No product runtime change is needed.
One new patch section passes apply/hash/reverse; unrelated sections stay exact.
The stable kit now contains 1,127 targets; Desktop selection remains unchanged.

The current production renderer is reused with matching source hashes and
unmodified preload. A fresh isolated Local native run has original-window
480×620 AX/pixel acknowledgments for waiting/running and terminal states.
Catch up shows the tool-written plan, running worker and Goal waiting at 1/20,
then tasks 2/2, worker evidence and Goal done after two turns. Goal waiting clears
on actual delegation completion; no extra owner prompt is sent. Both profile
configs remain unchanged during the case. Private captures and receipts:
`../evidence/captain-goal-workflow-20261117`.

The accepted native run lasts 122.57 seconds, passes 60 seconds Local, peaks at
four product processes and 1,196,621,824 B RSS including guardian, and closes with
zero owned survivors. App/helper exit precedes gateway/model shutdown. Seven
fixture config/env files and one geometry absence are restored; Desktop SSH zero.
External observers/controllers are excluded; no whole-task RAM or savings claim.

Preparatory failures remain failed: forbidden `/var/tmp` runner scratch, a long
socket path falling back to forbidden `/tmp`, and shell environment snapshots
exceeding the stricter source-check process guard. The latter's initial closure
receipt reports a survivor; an explicit PID/birth wait confirms it closed.
Subsequent source check stays within its guard; no native trial fails this round.
Terminal capture has some left-edge clipping, so no general layout acceptance is
claimed. Full provider reasoning, owner Stop/block/budget cases, agent-desktop
input, other-host/ai connection and owner-app adoption remain unproven/ungranted.
No owner data/settings, ESTOP/pause/timer/permissions change, version or release.

# Captain plan and worker results — native Local step accepted, unreleased

Catch up shows the bound chat's received plan, native worker progress and latest
finished results. Native testing reproduced a lost result: the parent's follow-up
pruned finished live workers, removing the failed worker from Catch up. The store
now retains only its latest pruned terminal batch for review; current rows win
on matching IDs. Session clear/Stop and gateway switches remove both views.
Live counters/retirement, native goals, budgets and model settings stay unchanged.
No new RPC, polling, scheduler, dependency or durable history store.

A regression fails before the retention fix. The seven nearest source files then
pass 60 tests: actual parent-turn pruning, latest-batch replacement, no late
resurrection, live counts, owner/session isolation, retained-only/global clears,
gateway-switch wipe and child/parent navigation. Production renderer/native-main
build and renderer typecheck pass. The six changed adapter/store source and test
files pass ESLint. Older navigation act warnings remain; no full-source lint or
unchanged full native suite claim.

Separate native production Local baseline and corrected candidate runs pass
bound AX/pixel acknowledgments for running and terminal phases at 480×620. The
baseline lacks plan/worker rows. Candidate shows Previous tasks 2/2, Running,
then Failed with the received rejection after automatic parent follow-up. Stored
synthetic plan and five scripted loopback exchanges exercise real delegation/file
reading, not autonomous provider reasoning. Paused goal and fixture config remain
byte exact. Child navigation is offline-tested, not clicked in these native trials.
Private captures: `../evidence/captain-work-visibility-20261117`.

Both accepted runs pass 60 seconds Local, stay within four product processes and
finish with zero owned survivors. Baseline/candidate sampled RSS including guardian
is 1,228,095,488 / 1,129,119,744 B; external CUA/advisor/controllers are excluded.
These are fixture peaks, not whole-task RAM or savings evidence. App/helper exit
is observed before gateway/model teardown. Across five trials, 35 fixture config/
env files and five geometry absences are restored; Desktop SSH remains zero.

Failed trials and STOPs remain failed. The first trial breached the process guard
at five during teardown. Ordered app-exit/gateway teardown corrects that fixture
ordering; subsequent accepted trials peak at four. Another failed trial exposed
the product's disappearing terminal result before this fix. Window-menu activation
resolved earlier AX/pixel visibility mismatch without a product focus change.
No owner app/data/settings, other host/ai, ESTOP/pause/timer or permissions change;
agent-desktop native input remains ungranted. Complete autonomous goal execution,
Stop/block/budget cases and capability release remain open. No version/tag bump.

# Captain plan and worker activity — round 197 historical incomplete trials

The unreleased working patch puts the bound session's received tasks and native
worker progress/results in Catch up. It reuses existing stores, task rows,
translations, historical rendering and child-session navigation. No new RPC,
poll, scheduler, model setting or goal/budget change. Completed activity does not
complete a goal. Five changed native sections retain the existing 1,122 targets.

Two adapter cases fail before implementation. The three nearest files then pass
19 cases, including a shell-to-Catch-up integration. Coverage includes live and
retained tasks, completed/failed/queued worker status, result text, session switch
and late foreign updates, absent/prototype-key sessions, actual child/parent
navigation arguments, and unchanged goal state after completed activity. Renderer
production build and typecheck pass. Adapter source/test lint is clean; a
baseline comparison finds no introduced diagnostics in the other touched files.
Existing React act warnings in two earlier navigation tests remain.

Four isolated Local baseline trials remain failed, with their STOPs retained.
The first exposed a private scripted-model classifier error; two more exposed
fixture scaffold links mistakenly copied as file contents. The fourth reaches
a real native chat, persisted synthetic plan and native delegated file read,
with a paused goal and bounded loopback model endpoint. CUA observes the chat
AX/pixels. Catch-up navigation does not open in the observed AX state; coordinate
input reports noWindowsAvailable. The observation budget then expires. This does
not establish a product navigation bug, a locked screen or accepted UI comparison.
No candidate native launch or before/after screenshot pair is claimed.

All owned processes and model/API servers are closed, 28 fixture config/env files
and four geometry absences restored, Desktop SSH count zero. The fourth trial
passes 60 seconds Local; its sampled peak is four product processes and
1,139,458,048 B including guardian. External CUA/advisor/build/controller memory
is excluded; no whole-task RAM or savings claim. No other host, ai or owner-app
connection, native agent-desktop input or owner data/settings change.

Native acceptance remains open, so no COMMIT-MSG, version, tag or release is
created for this step. Scripted loopback activity and stored synthetic tasks do
not prove provider-backed autonomous goal completion, Stop/block/budget behavior.

# Captain autonomy profile controls — accepted step, unreleased

Desktop now exposes the native `goals.allow_self_management` and
`goals.delegated_decisions` permissions in **Safety → Captain autonomy**, using
existing scoped config rows, saves and search routing. They remain independent
and default off. No new runner, RPC, store, budget editor or prompt mutation.
Page and field copy is supplied for all nine bundled locales; native visual
acceptance below uses English. Backend authority remains unchanged.

The regression is red before implementation: the new switch is missing, while
the old-backend/no-fabricated-permission control passes. The three nearest
Settings/helper/subpage files then pass 79 tests. Assertions cover independent
flags, only the changed key in the selected profile save, unchanged limits and
unrelated settings, and absence of invented old-backend defaults. Renderer
typecheck and scoped lint pass; two initial test-format warnings are corrected.
Twelve changed source sections apply, match after hashes and reverse against the
pinned upstream. Ten existing targets plus two newly patched upstream files yield
1,122 targets; unrelated sections and the existing test selection are retained.

A real isolated Local baseline shows the earlier Safety navigation without this
page. A fresh candidate shows both switches off. Its active profile is `captain-b`;
the visible Settings target is `default`. Actual CUA clicks first enable routine
decisions alone, then self-management. Switching to `captain-b` still shows both
off. Returning to `default`, closing/reopening Settings and selecting the field
through Settings search shows both saved permissions on. Native YAML readback
confirms exactly those two effective config changes; the other profile is byte
identical. Seeded active/paused goal JSON and recorded caps 13/7 are unchanged,
as are configured goal limits 20/17 and other model/approval settings. These are
configuration/preservation controls, not a running autonomous goal-loop proof.

The successful case uses AX after actions and separate documented CUA AX/image
calls for the two required screenshots; both image observations succeed without
retry. Final bound ACK and 60-second Local gate pass. Closure 202.67 s, zero
survivors, gateway/model server stopped; peak four product/seven including OS
utilities, 988,250,112 B including guardian. External CUA/advisor/build/controllers
are excluded; no whole-task RAM or savings claim. No model calls, native
agent-desktop input, other host/ai connection or owner-app adoption.

Earlier candidate trials remain failed: one observation lease refusal before
input (fractional/integer clock mismatch plausible, exact client age unavailable),
one invalid native profile-menu element before selection, and one ScreenCaptureKit
parameter error after the first switch click. No failed STOP is reset. A private
integer timestamp fix retains the strict 0–5,000 ms lease; actual-consumer boundary
controls accept 0/5,000 and reject fractional-future/-1/5,001 ms. These fixture
changes are not product fixes. Before/after and configuration receipts remain
private: `../evidence/captain-autonomy-controls-20261117`.

The full Captain capability remains open: plan/decision/delegation follow-through,
native terminal completion and owner Stop/block/budget acceptance. This step does
not establish provider-backed autonomy or authorize wider rights.

# Minimized native Monitor AX recapture — accepted, unreleased

One distinct isolated production Local fixture from kit `de783fc` passes three
actual app + window scoped agent-desktop provider/common-tool snapshots while the
original Monitor window is minimized. Each maps 47 refs/75 elements, with one
backend session, three snapshot IDs, disjoint indices and the same owned process/
window generation/native ID/nonce/refmap. Fresh fourth-slot/headroom admissions
and the existing Local/write/lease/deadline guards remain.

Own-Electron events and 100 ms state samples confirm minimized/unfocused across
all three reads: 13 rows, 1,215 ms, maximum gap 102 ms, including a sample after
native completion. No focus is observed within that interval; every transient
focus and OS visibility/current Space are not independently proven. CUA baseline
AX/pixels precede minimization; only after native work finishes does the final
CUA observer restore the window and capture matching Monitor/nonce/default/
Connected AX/pixels. Final bound ACK passes. No minimized CUA AX/pixel claim;
the narrow table remains below-fold AX evidence.

The first case remains failed: follow-up CUA AX observation coincides with restore
584 ms after minimize, so fresh minimized acknowledgment refuses before native
capture. A second case fails ScreenCaptureKit parameter validation before
minimization. Its fixture shares a bundle ID with the first; the accepted case
uses a distinct ID. This correlation is not a proven cause. Failed STOPs remain.

Accepted closure: 107.92 s, zero survivors, gateway/model-server stopped, 60-second
Local gate passed. Sampled peak four product/six including OS utilities,
946,978,816 B including guardian; external CUA/advisor/build/controllers excluded.
No whole-task bound/savings, native input/model call/provider image, cold inactive,
other-OS or owner-app adoption claim. Twelve fixture configs and three geometry
absences restored; eleven UI/two provider source hashes preserved. Desktop SSH 0,
new ai SSH 0; unrelated preexisting sessions left untouched.

Product code, native patch/manifest and test selection are unchanged. Private guard
controls reject stale/foreign/state-transition/gap/deadline/trigger failures;
these controls do not prove runtime coverage on other platforms. Baseline/restored
evidence: `../evidence/agent-desktop-minimized-capture-20261117`.

# v0.34.0 — Bot Monitor source-release review

The capability batch is accepted for the scoped source-kit handoff described in
[release notes](release-notes-v0.34.0.md), using separate matching native runs:
round179 recovery/source authority, round180 progress/Completed, round181 Error,
round185 narrow Stop/worker controls/keyboard reach, and round187 existing nonempty
canonical reopening. Round186 is
corroborating recorded-issue observation only; its INVALID/STOP/noACK is unchanged.
No all-capabilities-in-one-run, paid-provider, ai, adoption or agent-desktop runtime
readiness claim. Runtime-untested paths remain listed in the release notes.

This review changes documentation and release inventory only. The 1120-target source
manifest, patch and test selection remain unchanged; their per-slice regression/
patch evidence is reused. Companion unit, tracked-copy release and both secret
gates are the fresh handoff checks. No new UI launch or owner config access.
Historical records below retain their original acceptance/failure boundaries.

# Native existing canonical Bot Chat reopening — accepted, unreleased

**Named-profile Monitor Open reopens the existing nonempty Bot Chat.** This
focused native scenario passes its bound UI acknowledgment and independent
read-only postcheck. It does not change round186's failed scenario result.

One fresh isolated Local 480×620 instance uses the production renderer and
source-built main/preload development bundle from kit `b5a8ca5`. Eleven relevant
source hashes and the production preload stay unchanged. The existing guarded
Local/zero-SSH hold passes for 60 seconds before UI input.

Actual public RPC creates a default canonical chat, a separate side chat and a
named-profile canonical Bot Chat. Two loopback fixture replies populate the side
and named transcripts, with distinct IDs and markers. Before any Open, read-only
snapshots freeze canonical ID/title, profile, session inventories, messages and
recorded API/token counters. The target is nonempty and preexisting **before
navigation**; persistence across an app relaunch is not tested.

Native CUA AX/pixels first show a distinct New session route, then Bots → Monitor.
The exact named-profile Open action alone changes the URL to the saved canonical
session ID. The Bot Chat visibly shows the saved INDEPENDENT_PROFILE user and
assistant content and the matching profile; it does not show the independent
side-chat marker. No direct URL navigation, RPC activation, new prompt or input
retry causes this transition. Matching text alone is not the identity proof:
the URL and profile bind that content to the pre-Open named DB row, separately
from default canonical and side-chat controls.

After the observed result, the generation/target/profile-bound acknowledgment
passes with a 12.993-second-old capture; its postcheck has 99.409 seconds left in
the dedicated 120-second canonical phase. Native before/after checks and a second
independent read-only DB inspection agree: session ID sets, messages and selected
API/token counters remain unchanged in both DBs. Only the two initial fixture
reply kinds occur. Opening the chat creates no session or model call.

Original PID/birth/executable/window UUID/URL/lifecycle, single-use five-second
admission receipts, CUA20/ACK1, freshness30, 335/360 acceptance/overall deadlines,
25-second cleanup reserve and process/network guards remain. The scoped scenario
omits worker delegation and filter/report walkthroughs already covered elsewhere;
no product behavior, host adapter, DOM observer, preload capability or SQL/query
seeding is added. Responses/timing/usage are fixtures, not production billing.

Guardian exit0 records no failure/survivors and confirms gateway/model-server
shutdown. Native elapsed 113.302 seconds; sampled peak four product non-OS/seven
total children and 1,124,253,696 bytes including guardian. External CUA/advisor/
build setup are excluded; no whole-task memory bound or savings claim. All31
remembered PID generations close, owned paths/HOME and Desktop SSH are zero.
Five configs and window-state absence restore; eleven source hashes stay exact.
Cleanup journals 352,393,483 logical scratch bytes before deletion; physical
reclaim is unmeasured.

Private before/after images: `../evidence/bot-monitor-canonical-reopen-20261117`.
Raw evidence: `../uitest-v090-c2q4iijp/bots-r187{,-canonical}/evidence`.
This closes the existing nonempty canonical-reopen gate. Next is the feature-batch
release review, retaining qualified round186 Error-control observations and its
failed full-scenario boundary. No version/tag/release, remote connection or daily-
app adoption is included; earlier failures stay failed.

# Native recorded-issue search observations — phase admission refused, unreleased

**Recorded-issue filtering/search is visibly observed and independently
corroborated; the full round186 scenario remains INVALID/STOP.** No terminal ACK,
acceptance file, report click or canonical reopen is claimed.

One fresh isolated Local 480×620 production renderer/source-built main/preload
bundle from kit `c225aaa` reuses the existing guarded lifecycle. Eleven source
hashes and production preload remain unchanged. After the 60-second Local/zero-
SSH gate, public RPC creates canonical, independent side-chat and named-profile
controls, then delegates an actual fixture-file read. Releasing the held loopback
response returns HTTP 400. Native child ending, Error ledger, accounted delivery,
canonical report and independent transcripts pass. Seven unique model reply kinds
are fixtures; replies/timing/usage are simulated, not paid/live-provider evidence.

Guarded native AX/pixels show these completed observations:

- Recorded issues is explicitly selected. Its AX result contains only the default
  bot's native Error and excludes the independent profile/current worker.
- Searching `MONITOR_NATIVE_REJECTION` retains that same Error row. The visible
  query and selected Recorded issues control agree with the full captured tree.
- Focusing the token-sort header and pressing Tab reveals the report column.
  Pixels show Last recorded issue: Error, recorded time/task, the exact HTTP 400
  error excerpt and Recent reports (1); AX agrees on the default/source identity.
- Clear search, All and name sort reset the controls. AX restores both source-
  qualified rows; pixels show empty search, selected All and the name-sort arrow.

This tests Recorded issues membership plus search of the selected visible error
excerpt. It does **not** select an Error-only report-dialog outcome filter, test a
live Recorded stalled outcome or inspect every historical report body.

The next report-click admission fails before any CUA click or capture. The last
successful postcheck has 23.596 seconds left in the 120-second UI_TERMINAL phase
and 133.761 seconds left in overall acceptance. The next admission refuses the
20-second observation minimum; no exact refusal-time remaining-budget claim is
made. No report observation, UI_TERMINAL or native-acceptance file follows. The
original INVALID/STOP and guardian's insufficient-observation-budget failure are
retained. No retry, replacement receipt or longer phase is used. Earlier guarded
observations remain bounded evidence, not a passing full scenario.

The named-profile canonical ID, title, transcript and usage were independently
snapshotted read-only before any Open. It is a genuinely preexisting nonempty Bot
Chat, distinct from default parent, side chat and child. It is never opened in
this trial, so native reopening remains an acceptance gate. The accepted wide
Error report from round181 and complete narrow Stop from185 remain prior coverage;
this trial does not alter their results or supply its own report acceptance.

Original PID/birth/executable/window UUID/URL/lifecycle, single-use five-second
admission receipts, CUA20/ACK1, freshness30, 120-second active reserve, 335/360
acceptance/overall deadlines, 25-second cleanup reserve and Local/network guards
stay unchanged. No new observer process, DOM observer, host adapter, preload
capability, query/SQL seeding, manual Refresh or UI lifecycle write.

Guardian exits 1 because of the admission failure, with gateway/model-server
shutdown confirmed and zero survivors. Native elapsed 208.989 seconds; sampled
peak four product non-OS/seven total children and 1,003,831,296 bytes including
guardian. External CUA/advisor/build setup are excluded; no whole-task RAM bound,
billing or savings claim. All 29 remembered PID generations are closed; owned
paths/HOME and Desktop SSH are zero. Five configs restore byte-exact, window-state
absence restores, and eleven source hashes remain unchanged. Cleanup journals
352,393,439 logical scratch bytes before deletion; physical reclaim is unmeasured.

Private labelled same-generation images:
`../evidence/bot-monitor-recorded-issue-search-20261117`. Raw evidence:
`../uitest-v090-c2q4iijp/bots-r186{,-error}/evidence`. This docs-only item records
completed observations and their limits; no product/patch, version/tag/release,
owner-app adoption or remote connection change. Next prefer a focused canonical
reopen trial; retain this failed scenario explicitly during feature-batch review.

# Native narrow Stop acceptance and nonempty worker controls — unreleased

**The fresh narrow Stop scenario passes, including its final native ACK.**
The prior round184 INVALID/STOP remains unchanged. This closes that scenario's
acceptance gap; Bot Monitor is still an unreleased feature batch.

One new isolated Local instance uses the production renderer and source-built
main/preload development bundle from kit `8080af9`. Supported persisted 480×620
geometry matches native content bounds. Eleven relevant source hashes remain
unchanged; the production preload stays byte-exact. Original PID/birth/executable,
window UUID, URL and lifecycle checks bind each action/capture. Existing guardian
admission supplies single-use five-second receipts inside each CUA call; no extra
observer process, DOM observer, host adapter, query injection or SQL seeding.

Before launch, the private non-observing ACK writer adopts the existing one-second
minimum proposal. UI observation admission still requires 20 seconds. Identity,
freshness (30 seconds), monotonic phase/335-second acceptance/360-second overall
deadlines, 25-second cleanup reserve and 120-second active reserve stay unchanged.
Offline controls distinguish CUA20 refusal at eight seconds from ACK1 admission,
with expired/insufficient ACKs refused. The live terminal ACK uses this path with
ample budget: its report is 10.330 seconds old and the capture's postcheck has
89.470 seconds left. This is not a live one-second-boundary timing experiment.

After the 60-second Local/zero-SSH gate, public RPC creates canonical, independent
side-chat and sibling-profile controls and delegates an actual fixture-file read.
CUA AX/pixels show these native interactions:

- Searching `Subagent` leaves only the real Working worker, task and step 1/250;
  vertical scrolling reveals that result at the narrow size.
- Clearing search restores the rows. Working excludes the idle sibling profile.
  Elapsed sorting moves the real worker before its parent; name sorting restores
  parent/worker/sibling order. AX establishes full order; pixels show the first
  sorted task/elapsed value and the selected column's arrow.
- Two Tab presses from the elapsed-sort header focus the worker's Open chat and
  visibly reveal the rightmost column. This proves native keyboard horizontal
  reach. It does not prove wheel/trackpad panning or open a chat.
- Search/filter/sort are explicitly reset. Vertical scrolling reveals the actual
  worker, Working and step 1/250 before the active ACK. Authenticated interrupt
  ends that child before releasing the held server reply.
- Automatic roster reads remove the worker/old step and show the canonical
  interruption preview. The exact default/source-qualified Recent reports action
  opens Stopped, matching task/time and a nonempty 74.3-second interruption summary.
  The final generation/parent/worker/delegation/summary-bound ACK is accepted.

Read-only DB, durable ledger, accounted delivery and independent transcripts
agree with the visual observations. Seven unique loopback model reply kinds are
fixtures; timing/usage are simulated. No external model service or paid fallback.
Held server-handler completion still does not prove canceled-client handler
arrival. No manual Refresh or UI lifecycle/SQL writes drive the transition.

Recorded issues returns an empty result for this Stopped-only history, as the
existing shared selector deliberately includes only Error/Recorded stalled.
That exclusion is a negative control, not a defect or nonempty issue acceptance.
Nonempty Error/Stalled filtering/search, and native reopening of an existing
nonempty canonical chat, remain distinct gates before final feature-batch review.

Native closure takes 195.056 seconds, sampling four product non-OS/eight total
children and 1,009,860,608 bytes including guardian. It records no failure or
survivors and confirms gateway/model-server shutdown. External CUA/advisor/build
setup are outside that sample; no whole-task memory bound, billing or savings
claim. All 25 remembered PID generations are closed, owned paths/HOME and Desktop
SSH are zero. Five configs are restored byte-exact and window-state absence is
restored. Eleven source hashes remain unchanged. Scratch removal journals
352,393,457 logical bytes before deletion; physical reclaim is unmeasured.

Private before/after and control images:
`../evidence/bot-monitor-narrow-acceptance-20261117`. The before-fix image belongs
to the separately owned failed round181, not the new generation. Raw evidence:
`../uitest-v090-c2q4iijp/bots-r185{,-stopped}/evidence`. Earlier failed trials remain
failed. This records a completed native acceptance slice, with no product/patch,
version/tag/release, owner-app adoption or remote connection change.

# Guarded native narrow Stop observations — final ACK refused, unreleased

**Visual observations and DB readback match; the scenario remains INVALID/STOP.**
This record completes only the guarded observation slice. It is not full native
scenario acceptance, a release or owner-app adoption.

A fresh production renderer plus source-built main/preload development bundle
from kit `d0d5fbc` includes the narrow table's one-class correction. Supported
persisted 480×620 geometry matches actual native bounds/content size. Eleven
relevant source hashes remain exact; the production preload is unchanged.
Original PID/birth/executable, window UUID generation, URL and lifecycle receipts
bind each CUA action/capture. The existing guardian performs read-only admission
inside each CUA call, consuming a fresh single-use five-second receipt before
the API; no extra Python process is started. Operations receive explicit app and
receipt arguments, callbacks use those arguments, and failures latch STOP.
One full paired AX/pixel baseline passes after the 60-second Local/zero-SSH gate.

Actual public RPC delegation reads the fixture file. Vertical scrolling reveals
the real worker in the native narrow table, with Working, task and step 1/250
matching AX and pixels. Only then is the generation/parent/worker-bound active
acknowledgment written. The scenario uses authenticated subagent.interrupt,
checks ended child state before releasing the held reply, and verifies interrupted
result, durable ledger and accounted delivery. Seven unique loopback reply kinds
are used, rejecting duplicates; replies/timing/usage are fixtures, not production
billing. Held server-handler completion does not prove canceled-client handler
arrival, which remains unproven.

After automatic roster reads, AX/pixels show zero workers, no old step, and the
canonical parent's MONITOR_PARENT_INTERRUPTED preview. A right-scroll request
does not visibly expose the report button; its cause is unconfirmed. Activating
the exact semantic Recent reports button for default/UI Local184Stopped opens
a visible Stopped dialog at the same 480×620 size, with the exact goal, recorded
time and nonempty Operation interrupted summary. No manual Refresh, DOM observer,
appended preload capability, host adapter, query/SQL seeding or UI lifecycle write
is used. Independent read-only DB checks confirm matching canonical parent,
child end/API count, delegation/result/summary/delivery and separate nonempty
side-chat and sibling-profile controls. Four paired capture generations match.

The final terminal ACK fails a private observer budget check. Its writer calls
the same read_check default of 20 seconds used before a new observation, although
this step performs no CUA operation. The report postcheck records 26.095 seconds
left. The refusal follows 18.027 seconds later, at approximately 8.096 seconds
remaining, using the retained launch wall/monotonic mapping rather than an original
monotonic sample at refusal. Other ACK checks are not re-executed after that first
failure. Separate image metadata and DB readback establish the observed result;
they do not create a successful ACK. No UI_TERMINAL or native-acceptance file is
written. The original INVALID/STOP remains, with no retry or receipt rewrite.

Future-only ack-next.py changes the non-observing ACK minimum to one second.
Offline controls show the old 20-second policy refuses eight seconds; one second
admits eight only with the existing identity/liveness checks satisfied. Dead,
closed, foreign, insufficient and expired cases refuse. Deadline/freshness/reserve
checks and the CUA admission minimum remain unchanged. This proposal is not run
against the retained failed trial or validated through another live scenario.

An immutable 360-second launch limit reserves 25 seconds for cleanup; acceptance
ends by 335 seconds. Readiness/active phase caps reserve terminal time before
work is released; the active ACK requires 120 seconds left for interruption and
terminal verification. The controlled native runtime closes without survivors
after 230.192 seconds, sampling four product non-OS/eight total children and
975,077,376 bytes including guardian. External CUA/advisors/setup are outside
that sample; it is not a whole-task memory bound or a savings result. Exit zero
establishes cleanup, not scenario acceptance.

Private before/active/removal/Stopped frames are under
`../evidence/bot-monitor-narrow-stopped-20261117`; the labelled before-fix frame is
from the separately owned failed round181 fixture, not this generation. Raw
receipts remain in `../uitest-v090-c2q4iijp/bots-r184{,-stopped}/evidence`.
This docs-only item records guarded native observations and their exact limits.
The failed final ACK, unproven native panning and nonempty-control checks remain
open before the feature-batch release. Earlier failed attempts stay failed.

# Native narrow readiness timeout and release-gate audit — unreleased

A fresh production renderer and source-built main/preload development bundle
from `2706aab`, including the narrow-table correction, use an owned Local-only
profile and supported persisted 480×620 geometry. This is not shipped-package
or installed-app adoption proof. Eleven
relevant source hashes match through build; the production preload is byte-exact
to the prior unmodified preload. The existing Node/OS/Chromium fences and
remembered-generation guardian remain unchanged. The native content bounds match
480×620 and the 60-second Local/zero-SSH gate passes.

The first exact-owned CUA selection and paired baseline pixels show the actual
Hermes chat and Local/profile labels. Its paired AX result is a diff-only
unchanged message, not a persisted full baseline. The fixture's 90-second
UI_READY deadline expires before an acknowledgment is written. The gateway log
names that exact timeout; both profile databases contain zero sessions and zero
messages. No worker, delegation, authenticated Stop or task report is created,
and no model work runs. The original guardian fails after 92.789s and closes its
owned generations, with a gateway/model-server shutdown receipt.

A later full AX read shows the owned bundle's default Electron welcome page.
Four replacement main/helper generations start after the guarded run has ended;
all are closed by exact owned executable/PID-birth checks. That AX file is retained
under an explicit unexpected-default-app label, separate from the original
baseline image. Their RAM, network and write coverage is unmeasured; the earlier
guardian sample does not cover them. The timing and changed content establish an
observer/lifecycle failure, not a Monitor defect or proof of who initiated the
replacement. There is no native retry or further CUA action after that observation.

The original controlled sample reaches four non-OS/eight total children and
937,541,632 bytes including guardian. It is not a bound for the complete CUA path
or a whole-task RAM/savings result. The initial read-only identity probe used a
Python without psutil and failed before mutation; the existing explicit test
interpreter completed the preflight. That setup correction is not a native retry.

Future observation uses one paired full AX/pixels result and an immediate
original PID/birth/executable/window plus monotonic phase/overall-budget check
before every CUA call. A private guard passes two positive and fifteen negative
offline controls for generation/window changes, dead instances, expiry, short
budget and invalid clocks. It is not integrated or proven against live CUA and
cannot eliminate exit-between-check-and-call races. A future 180-second UI_READY
budget within the same 360-second overall limit is a proposal, not a change to
this retained failed fixture. No cancellation instrumentation or client-handler
arrival claim is added.

Independent offline work completes a compact [release gate audit](design-bot-monitor.md#release-gate-audit--2026-11-17)
in the existing design. Eight referenced source/test surfaces match their
packaged after-hashes; round181's unchanged 40 source cases, lint/types and
browser red/green evidence are reused. The audit separates source/component,
native wide, browser geometry and missing native narrow/Stopped evidence. It
also preserves the gap in nonempty native control coverage and the bounds on
roster observations, costs, model labels, report search and canonical opening.
README now reflects actual native progress and limits its old stale-reply wording
to the stopped-state assertion that was tested. No source, patch, test selection,
version/tag/release or adoption change is made in this round.

Private raw baseline/timing/closure evidence remains under
`../uitest-v090-c2q4iijp/bots-r182{,-stopped}/evidence`; the labelled baseline image
and unexpected AX are under `../evidence/bot-monitor-readiness-20261117`.
Native narrow/Stopped acceptance remains open. Previous failed attempts stay
failed; this completed item is the release-gate audit, not native acceptance.

# Native Monitor Error report and narrow-layout fix — unreleased

Two fresh sequential isolated Local native fixtures use the same production
renderer/main/preload bytes. Each passes the 60-second Local/zero-SSH gate and
live instance identity checks before CUA interaction. Only the first fixture
passes its outcome acceptance. Loopback model replies, timing and usage are
simulated; no external model service, lifecycle/SQL seeding, host adapter, manual
Refresh, DOM observer or appended preload capability is used.

The first actually delegates and reads a fixture file. CUA AX and pixels show
Working/step 1/250, then zero workers/no old step after the model HTTP 400.
The exact source-qualified Recent reports dialog shows Error, its task/time,
nonempty failure summary and HTTP 400: MONITOR_NATIVE_REJECTION. Native ended
child, error ledger, accounted delivery and canonical report agree; independent
nonempty side-chat and sibling-profile transcripts remain separate. Seven unique
model call kinds complete, rejecting duplicate/extra calls. UI acknowledgments
bind generation/parent/worker/report IDs and do not write lifecycle or SQL.

The second uses supported persisted 480x620 geometry; native bounds and content
size agree. AX contains the real active worker, but pixels show only instructions
and filters. A planned vertical scroll moves the heading; a further scroll
cannot reveal the table. No active acknowledgment or authenticated Stop occurs.
The scenario subsequently times out awaiting that acknowledgment; its guardian
records failure and closes the fixture. Stopped/report presentation and late
canceled-client completion-handler arrival are unproven. No native retry occurs.

A focused browser regression renders the actual BotMonitor and production CSS
with synthetic rows, a wrapping Workspace-style toolbar and reserved shell space.
It reproduces a zero-height table wrapper, with 355px of rows trapped inside it.
Adding `shrink-0` to that wrapper is the only product change. The exact UTF8
fixture fails on the old source and passes after repair: wrapper height 355px,
outer Monitor scrollHeight 673px versus clientHeight 291px, final row revealed
inside the viewport, zero inner vertical scroll/overflow, and horizontal panning
reveals the final column. Renderer errors are zero. The check asserts geometry,
not class names or DOM presence. It uses headless single-process Chromium with
the Chromium sandbox retained, plus the existing workspace/network/SSH fence.
This establishes browser layout behavior, not final native-shell acceptance.

Run with existing source dependencies and an installed Playwright browser:
`node apps/desktop/scripts/check-bot-monitor-layout.mjs /path/to/patched-source /path/to/private-output`.
Select a private HOME/TMPDIR and local-only OS/network fence as for other isolated
verification. The script binds its static fixture server only to 127.0.0.1,
closes the browser/server and removes its generated build in finally; the caller
retains screenshots and geometry. No dependency is installed by the check.

Nearest Monitor/open/workspace checks pass 40 tests across three files; scoped
source lint has zero warnings and renderer types pass. The Monitor and new
layout-check patch sections are exported/apply/hash/reverse checked against
pinned bf0203a794a07aac3ff764972ab9087baa4e4f4e. The target count is now 1,120;
the existing source-test selection remains unchanged, with unrelated patch
sections retained byte-exact.
The reusable browser regression is packaged with the upstream desktop scripts.

The native Error run lasts 149.828s, sampling four non-OS/six total children and
945,045,504 bytes including guardian. The failed narrow run lasts 148.814s,
sampling four non-OS/eight total children and 1,066,500,096 bytes. Source checks
peak at 2,606,465,024 bytes including observer. Build, external CUA/advisor and
short-lived setup controllers are separate; none is a whole-task benchmark or
production RAM/usage saving. Five fixture configs and absent geometry restore
for each fixture; nine relevant native source hashes match before the CSS fix.

Private Error/failed-narrow/browser images are under
`../evidence/bot-monitor-error-narrow-20261117`; raw receipts remain in
`../uitest-v090-c2q4iijp/bots-r181{,-error,-stopped}/evidence`. Error acceptance
predates the one-line CSS fix; the native narrow/Stopped gate and final batch
acceptance remain open. Earlier failed observations stay failed. No release,
version/tag, owner app/data, other host, permission, ESTOP/pause/timer or adoption
change is included.

# Native Monitor worker completion and nonempty report pass — unreleased

A fresh full production renderer/main/preload/SDK/query displays a real native
child through active work, advancing elapsed time, completion and its canonical
report. The private Local scenario reuses the committed native lifecycle model,
RPC and read helpers. Only loopback model replies, timing and usage are simulated;
seven unique fixture calls complete, with duplicate/extra calls rejected. No
external model service or paid fallback is used.

Public RPC creates the canonical parent plus independent nonempty side-chat and
sibling-profile controls. Actual delegation reads the fixture file. CUA AX and
pixels agree on one Working worker, step 1/250, elapsed 17s then 32s, recorded
worker model and fixture token amounts. The canonical parent's preview and the
independent profile remain separate. Current-tool data is absent and stays absent.
Fresh generation/parent/worker acknowledgments follow those observations; they
do not write lifecycle or SQL. The scenario owns heartbeat/reply release and
completion. Durable child end, completed ledger, accounted delivery and matching
canonical report assertions all pass, including the independent transcripts.

After successful automatic roster reads, native AX and pixels agree on zero
current workers, no stale step, parent completion preview and one Recent report.
Opening that exact default/source-qualified report shows its task, Completed
status, completion time and nonempty MONITOR_WORKER_DONE excerpt. The sibling
profile still has zero reports. The terminal acknowledgment binds the same
parent, worker, delegation ID and summary, and only follows matching pixels.
Read-only retained-database checks independently confirm the ledger/delivery and
transcript separation. This closes the completed-worker native paint/report gate;
earlier failed terminal observations remain failed.

The 60-second Local/zero-SSH gate precedes CUA interaction. No DOM observer,
appended preload capability, host adapter, query injection or manual Refresh is
used. Guardian exit is clean after 204.135 seconds; sampled peaks are four non-OS
children, seven total children and 978,321,408 bytes including the guardian.
Build/setup and external CUA/advisor are outside that figure; it proves neither
full-task RAM nor production billing/savings. Five fixture configs restore and
eight relevant source hashes remain unchanged.

Private active/advancing/terminal/report captures are under
`../evidence/bot-monitor-worker-completion-20261117`; raw receipts remain under
`../uitest-v090-c2q4iijp/bots-r180/evidence`. Native Error/Stopped presentation,
narrow layout and final feature acceptance/release audit remain separate. This
round changes documentation/inventory only; no product/patch/API or release.

# Native Monitor stale recovery and canonical navigation pass — unreleased

A fresh production renderer/main/preload built from the committed query-cache
correction passes the isolated Local walkthrough. The real gateway exposes two
empty profiles. CUA accessibility and screenshots agree at baseline, degraded
refresh, recovery and final Bot Chat navigation. No DOM observer or appended
preload capability is used. The 60-second Local/zero-SSH gate passes first.

A labelled inventory IPC fault actually rejects route reads. The guard stops
before aggregate inventory, so that second configured fault is not exercised.
After explicit Refresh and settled retries, both source labels remain, the
stored-snapshot warning appears, rows say Retained snapshot and both Open buttons
are disabled. Removing the fault and explicitly refreshing clears the warning
and restores current status/Open. Successful native route/aggregate returns and
real backend profile-reader receipts independently confirm recovery. The fault
is simulated; this is not a real gateway-outage test.

One Open click on the named profile reaches a Bot Chat tab. The first observation
is intermediate; the later read-only observation shows the session URL and empty
chat. That ID matches the sole persisted Bot Chat row in the named profile's
state.db, with profile_name naming that profile. The default database remains
empty. Both databases contain zero messages; the new row records zero model API
calls and input/output tokens. No prompt is sent. This proves creation/navigation
of an empty canonical chat, not reopening a pre-existing nonempty transcript.

The native guardian closes without failure or survivors after 172.762 seconds.
Sampled peaks: four non-OS children, eight total children and 942,440,448 bytes
including the guardian. Build/check setup and external CUA/advisor are outside
this measurement; no full-task RAM or savings claim. Five fixture configs restore,
six relevant source hashes remain unchanged, and Desktop SSH stays zero.

Private before/after captures are under
`../evidence/bot-monitor-query-authority-20261117`; raw receipts remain under
`../uitest-v090-c2q4iijp/bots-r179/evidence`. Earlier failed runs remain failed.
This completes degraded-refresh/recovery and empty canonical navigation gates.
Nonempty task reports and terminal worker progress still need native acceptance.
No product/patch/API change, unchanged source-suite sweep or release is included.

# Monitor route-inventory failure preserves scoped snapshots — unreleased

A fresh isolated Local full production renderer/main/preload and real canonical
gateway pass CUA AX/pixel baseline, Bots and Monitor navigation. Both actual
empty profiles show their Local source and configured model. The fixture uses
no DOM executeJavaScript observer or appended preload capability. Metadata-only
loopback catalog responses are synthetic; no model generation or worker runs.

A labelled native IPC fault rejects route and aggregate inventory reads. After
Refresh and subsequent query polling, AX and pixels agree on two retained rows
with lost source labels, Status unknown and enabled Open, without a stale notice.
This reproduces a product fallback bug under a simulated transport failure;
it does not prove a real gateway outage. No Open/recovery is attempted. CUA ends,
the guardian stops cleanly after its 60-second Local/zeroSSH gate, and every
owned native PID generation closes. Prior observation failures stay failed.

The shared fetch swallowed the route error and read ambient profiles, then
returned a successful partially unscoped snapshot after aggregate failure. It
now rejects before that compatibility read when its exact query cache holds a
nonghost, nonremote scoped row belonging to this active connection. Existing query-error
handling preserves the old source/canonical snapshot, marks work unavailable,
hides active workers and disables Open. Successful authoritative refresh clears
the stale state. Initially unscoped legacy hosts remain usable; healthy route
inventory plus aggregate failure still retains unavailable foreign rows while
current active-source facts remain fresh. No SDK, schema or new state is added.

The real-SDK/preload integration reproduces the missing stale notice on old
source, including an ambient reply that would overwrite canonical facts. After
the fix it proves the unchanged cached snapshot, source labels/canonical preview,
hidden worker, disabled Open, no ambient/activation/navigation request and fresh
recovery. A second case proves absent legacy capabilities still work. The first
green run reaches recovery but finds duplicate source labels on bot/worker rows;
scoping its assertion to the canonical bot row corrects only that test selector.
The next fresh native run contains that first guard, yet repeats the settled
fault: standalone Monitor has a populated query cache and an empty sidebar-owned
global roster. The earlier regression mounted an extra publisher. Native input
stops; recovery, canonical Open and another UI attempt are not performed.

The shared fetch now receives the previous snapshot from its exact query
context client/key, captured before IPC, in both useRoster and primeRoster.
Two added real-SDK/preload regressions fail on the old source: standalone loses
the stale notice; primeRoster incorrectly reports success. After correction,
standalone retains the identical cache/source/canonical preview, hides workers,
disables Open and recovers through an authoritative Refresh; primeRoster retains
its cache in error without ambient reads or activation/navigation. Four relevant
source files pass 31 cases; scoped lint has zero warnings and renderer TypeScript
passes. No unchanged Monitor mock sweep, post-correction renderer rebuild or live
retry is run.

Two source sections apply, match after hashes and reverse against the pinned
upstream. All unrelated cumulative patch bytes stay unchanged; 1,120 targets,
existing test selection retained. Native images prove the initial global-roster
guard failure only; they do not prove the query-cache correction.
Native after-fix degraded paint, canonical navigation, nonempty reports and live
terminal progress still gate the Bot Monitor batch release. No version/release,
owner app/data, remote host/ai, ESTOP, pause, timer or permission change.

# Require app scope for native window capture — unreleased

Window-only requests are now refused before native probe. Every capture requires
an explicit valid app; numeric selection passes both `--app APP --window-id w-N`.
Exact returned window ID, canonical-label validation, lease/ref invalidation and
privacy/error bounds remain. Named-app-only equality stays exact; combined scope
uses the app as the native filter and may return its canonical label. No PID,
fuzzy matching, autoactivation or unscoped fallback is added. Existing caller/
schema already forwards both selectors, so no default/config/dependency change.

Primary pinned source establishes the gap: [core selection](https://github.com/vercel-labs/agent-desktop/blob/b0b7277bea09b770ef9d1fb45aad667bc432cd57/crates/core/src/snapshot/surface_target.rs)
uses [global native inventory](https://github.com/vercel-labs/agent-desktop/blob/b0b7277bea09b770ef9d1fb45aad667bc432cd57/crates/macos/src/system/window/window_inventory_global.rs)
when app is omitted. That inventory reads frontmost AX and probes eligible owner
PIDs. Earlier window-only output/PID/refmap witnesses did not isolate internal
inventory; that isolation claim is withdrawn. Retained selected snapshots bind
fixture output, not absence of unrelated internal metadata reads. App-scoped
inventory still discovers OS app-owner metadata; choose a unique intended scope.
No syscall audit or hostwide metadata-isolation claim. No unscoped live retry.

Updated regression is red 36 fail/50 pass before implementation, then backend/
actions pass 118 tests with one worker. Both selectors reach the common tool and
exact native argv; missing/malformed app scopes and window-only calls never probe.
Canonical-label differences, named-only identity checks, wrong windows, private
errors and stale refs remain covered. Two changed patch sections apply/hash/
reverse; unrelated sections, 1,120 targets and test selection remain unchanged.

Fresh foreground production Local Monitor passes three actual app+window scoped
snapshots in one backend session, each 50 refs/78 elements. Distinct snapshot IDs,
disjoint indices, same original owned PID/birth/executable/window generation/
native window/nonce/refmap; reserved fourth slot and fresh headroom each time.
Paired CUA AX/pixels, bound final ACK and 60-second Local gate pass. The narrow
table remains below-fold AX evidence. Closure 132.78 s, zero survivors, gateway/
model-server stopped; sampled peak four product/seven including OS utilities,
921,600,000 B including guardian. External CUA/advisor/build/controllers excluded;
no whole-task bound/savings claim or native input/model call/provider image.
Private before/after: `../evidence/agent-desktop-app-scoped-capture-20261117`.

Separate cold inactive app-scoped trial remains failed: after 60 s Local, first
snapshot returns `WINDOW_NOT_FOUND`; zero accepted captures. Closure 62.59 s/
zero survivors, peak four product/948,256,768 B including guardian. Visibility/
Space association is a hypothesis from native filtering, not proven cause.
Earlier failures remain failed; no cold inactive/background pixel acceptance.
Eight configs/two geometry absences restored, eleven UI hashes unchanged each,
two intentional source hashes verified; both runtime trees closed, Desktop SSH 0.

# Inaccessible native window guidance — unreleased

Two isolated production Local background trials fail and remain failed. The
fixture changes only reveal to `showInactive`; real renderer/main/preload remain.
First, Electron reports activation during CUA selection; the trial stops before
native capture and closes in 23.77 s. Second, no CUA observer is used: after 60 seconds
Local, the first native exact-window snapshot reports `ACTION_NOT_SUPPORTED` /
`window_without_accessibility_element`. It closes in 63.14 s. No successful AX
capture, three-read loop or background pixel acceptance is claimed.

The second trial records 581 Electron witness rows with no target focus/activation
observed and maximum gap 207 ms. Original PID/birth/executable/window generation,
native window, nonce and admission guards remain; no continuous native activation
witness exists. A fourth-slot reservation blocks new fixture helper spawns and
requires a fresh three-process/headroom guardian sample before the native child.
Offline controls: focus 1 positive/18 negative, native-only phase 1/13, reserved
slot 1/6 and two helper-provenance substitutions refused. These controls do not
prove successful capture or witness completeness. CUA/pixel acceptance is not
replaced by native-only evidence.

The observed user-facing defect is lost failure guidance. The provider now emits
a fixed accessibility-exposure explanation only for that exact supported error;
malformed/foreign failures retain generic guidance. No private native message,
window ID, title or suggestion is echoed. Previous refs expire; no automatic
focus/retry is added. Actual regression: 3 fail/75 pass before implementation,
then backend/actions pass 110 tests with one worker. Retained native-error replay
through the actual common tool returns the new message in one probe, without a
native spawn. No post-fix live success is implied. The underlying exposure cause
is unresolved; an existing renderer-accessibility helper already enables the API.

Both runtime trees close with zero survivors and gateway/model-server stopped.
Sampled peaks four product processes, 908,394,496 B / 939,622,400 B including
guardian; CUA/advisor/build/controllers excluded. No whole-task bound or savings
claim. Eight fixture configs/two geometry absences restored; eleven UI source
hashes unchanged each, two intentional source changes match the patch. Native
input/model calls/provider images remain absent; no owner app or ai connection.
Private diagnosis: `../evidence/agent-desktop-background-diagnostics-20261117`.
Two changed patch sections apply/hash/reverse against the pinned upstream;
unrelated sections, 1,120 targets and test selection remain unchanged.

# Earlier window-only capture — superseded

This historical slice proved selected output. Its inventory-isolation claim is
withdrawn above; current capture requires app scope. It did not establish absence
of unrelated native inventory reads.

The experimental agent-desktop provider accepted the common tool's existing
numeric `window_id` without `app`: snapshot `--window-id w-N`, with exact returned
window ID and a valid canonical app label. Exact named-app matching is unchanged;
no prefix/alias fallback or PID selector is added. Incomplete, unproven or malformed
native identity is refused. Invalid numeric/mixed selectors never spawn; wrong
window responses disclose no private payload and invalidate earlier ref authority.

The regression is red before implementation (21 failures/47 passes), then two
focused source files pass 100 cases with one worker. Two changed patch sections
apply against the pinned upstream, match after hashes and reverse to before
hashes; unrelated sections and the 1,120-target/test-selection set are unchanged.

A fresh long-name isolated production Local Monitor passes the actual common
tool/provider with native 1.3.1: one complete snapshot, 50 refs, 78 mapped elements.
Its canonical native label differs from the requested fixture's friendly name.
Trusted native ID comes directly from that owned Electron window's media-source
ID; exact response ID plus PID/birth/executable, original window generation,
session/refmap and nonce witnesses agree. A numeric ID alone is not enduring app
identity: callers need a fresh trusted selection because IDs can be reused.

Paired CUA AX/pixels and the final bound ACK corroborate nonce/default/Connected/
Monitor before and after. The table remains below-fold AX evidence. Foregrounded
fixture, no native input/provider image/model call or owner-app adoption. The
60-second Local gate passes; all owned processes close in 105.83 seconds with no
survivors and gateway/model-server stopped. Sampled peak four product processes,
seven including OS utilities, 916,946,944 bytes including guardian; external CUA,
advisor/build/controllers excluded. No whole-task RAM bound or savings claim.
Private before/after: `../evidence/agent-desktop-window-capture-20261117`.
Input's canonical-lock exception, background/other-OS acceptance and the full
capability release remain open. Earlier failed trials remain failed.

# Full-production agent-desktop AX capture — unreleased

A fresh isolated production Local Hermes Monitor now passes the actual selected
provider/common tool capture: one complete 1.3.1 snapshot, 50 native refs and 78
mapped elements. The witness binds exact app, owned PID/birth/executable, native
window/session/refmap and the original Electron window generation. CUA AX/pixels
before/after corroborate the nonce/default/Connected/Monitor view; the final
bound comparison ACK passes. The table is below the visible fold, so its full
AX contents are not claimed as independently painted cell-by-cell evidence.

Capture runs in the existing gateway thread. A fresh guardian sample admits the
single native child only with three product processes and 512 MiB headroom.
Native hash/argv/env/single-use, profile lease and all original Local/write/SSH/
identity/335-acceptance/360-total/cleanup guards remain. A validated baseline ACK
now creates the same 120-second capture phase directly; the redundant manual
phase ACK caused the first failed trial's race and conveyed no input authority.
Offline controls refuse wrong identity/window/ACK, STOP, expired budget and phase
reset. The original failed case and its STOP are retained.

A second failed case returns a complete 50-ref snapshot under a truncated app
label (31 of 36 fixture-name characters); exact-app validation refuses it. A
short uniquely named fresh fixture then passes without relaxing that comparison.
Native and CUA differ in whether “Device” is joined with the nonce; both retain
the exact nonce. The later explicit-window proof above adds a separate safe route;
it does not retroactively accept this failed named-app case.

Successful trial closure: 135.31 seconds, zero survivors, gateway/model-server
stopped, sampled peak four product processes/eight including OS utilities,
914,702,336 bytes including guardian. CUA/advisors/build/controllers are excluded;
no whole-task bound or RAM savings claim. No model prompt/native input/provider
image/owner app or other host/ai is involved. The 60-second Local gate passes.
Private before/after: `../evidence/agent-desktop-native-capture-20261117`.
Capture acceptance is complete; input's canonical-lock write exception remains
ungranted, background/other-OS acceptance and the capability release stay open.
The earlier failed/preparation records below retain their historical scope.

# Native provider capture and interaction-directory diagnosis — unreleased

The later full-production capture preparation traces the pinned 1.3.1 snapshot
path to its configured session refstore, separate from the canonical input lease.
Workspace refstore writes are eligible; native input's `/tmp` directory/lock
writes still need an explicit owner exception. No permission or sandbox change
is made, and no input operation is attempted to probe that boundary.

The single production trial fails before gateway readiness because fixture-first
imports resolve the runner's `gateway.py` as the production package. The guardian
closes its one process after 0.71 seconds, sampled peak 131,203,072 bytes including
the guardian; Electron and agent-desktop never start. No full-target snapshot or
new UI evidence exists. A future-only bootstrap fixes source/helper ordering and
checks module provenance before startup. Actual imports under the existing
OS/audit guards pass, while the original shadowing order and a substituted capture
helper are refused. Eight existing Python guard cases and the single-use native
command admission controls also pass. These are preparation checks, not a native
capture pass. Original failure receipt and STOP remain unchanged; no live retry.

Four fixture configs and initial window-state absence are restored, eleven source
hashes unchanged and no owned process survives. Disposable build/runtime/temp
artifacts are removed after recording their logical sizes; no physical disk saving
or whole-task RAM claim. Full-production common-tool capture is the next live gate;
native input and the agent-desktop feature release remain open.

The earlier tiny-renderer capture evidence below retains its original scope.

A subsequent fresh full-production trial passes the import boundary and starts
the real Local gateway/main/renderer. CUA app selection returns the original
window's AX text with app/connection nonce, default profile and Connected state.
That tool-returned observation is not a saved AX/pixel pair or native provider
capture. The next controller call raises a missing-app-binding error during
argument evaluation, before Raise or capture dispatch. INVALID/STOP terminates
the trial without retry. No 60-second gate, screenshot, model prompt or native
driver operation occurs. Earlier failed trials remain failed.

Guardian cleanup exits normally after 42.48 seconds with zero survivors and a
gateway/model-server stop receipt; this is closure evidence, not acceptance.
Sampled peak is four product processes, six including OS utilities, 919,797,760
bytes including the guardian. A transient gateway-ensure Python occupies the
fourth slot; this does not prove a free driver slot at capture time. External
CUA/advisors/build/controllers are outside that runtime sample.

Future-only controller templates declare the app binding outside the block and
wrap the entire call. Offline JavaScript controls reproduce the old argument
error escaping the operation helper, then prove INVALID/STOP before any UI API
for a missing binding and on admission, operation and capture failures. A
synthetic selection checks the declaration shape; actual CUA binding persistence
and full-production provider capture remain unverified. Four configs/geometry
absence restored, eleven source hashes unchanged, owned processes closed and
sized disposable artifacts removed. No product/default/patch behavior changes.

The actual common tool and selected provider parse a complete macOS native
snapshot with five refs from an isolated production main/preload and synthetic
renderer. Private checks bind live PID/birth/exe, nonce content, window and
session/snapshot refs. CUA AX+pixels confirms initial state after an exposed
Raise; this is foregrounded fixture capture, not Monitor or background proof.

The subsequent native click returns INTERNAL/EPERM with unknown delivery/retry.
The provider consumes authority and requests fresh state. No post-click capture,
value input or live retry occurs; effect remains unknown.

Version 1.3.1 source traces the macOS default interaction lease to a canonical
`/tmp` directory outside the fixture's permitted write scope. An assert-based
probe compiles the exact published directory/path/validation/error functions
with minimal type shims, excluding UI dispatch and lock acquisition. Under the
same sandbox it reproduces the native error; the same source creates a 0700
owned-workspace control directory. The canonical directory stays absent.
Installed binary matches its npm-packaged digest and source diagnostic markers;
a reproducible binary-to-source build is not established. This identifies a
necessary fixture blocker without assigning the prior click's exact provenance.

Completed scope is native capture and offline boundary diagnosis. No product
code, lease relocation, permission, sandbox or provider behavior changes. Native
input effects, Monitor terminal visuals and the feature release remain open.

# Agent-desktop ref scroll areas — unreleased

The existing scroll action now accepts a latest captured native scrollarea ref.
Only canonical scrollarea role authorizes the native attempt; arbitrary ScrollTo
or Scroll on another role cannot authorize it. Role is not a platform delivery
guarantee. The official scroll contract and installed1.3.1 help define qualified
area refs and direction/amount arguments; Linux headless refusal remains native
without enabling headed or physical fallback.

Agent-desktop accepts four exact directions and integer amounts1–50, default3,
using the house cua bound. Rejects bool/string/float/null, nonpositive/oversized
counts, missing/foreign refs, coordinates, modifiers and foreground/focus. Shared
_act atomically consumes authority and checks lease/host; no new transport, retry
or raw result exposure. Native completion never establishes desired row visibility;
a fresh capture must verify it. Capture note teaches the area requirement without
changing the byte-frozen schema or default provider.

Common dispatch now preserves raw amount. Its former int conversion lives at
the cua boundary, preserving legacy coercion/clamp. Schema-valid integer calls
are unchanged; third-party providers now receive original malformed values and
remain responsible for validating them. No provider-name branch or new option.

49 new source cases plus122nearest ref/type/adapter/approval/fence/delivery cases
pass (171total, seven files, one worker). Fifteen initial behavioral reds; no
setup-error red claim. Tests cover all directions/bounds/default, type rejection,
role separation, consumed refs, stale index, lease/placement, cancellation/private
error, generic raw forwarding, approval denial and legacy cua coercion/clamping.
Synthetic successes are source/protocol acceptance, not native UI proof.

A private hybrid uses synthetic area capture and empty private native namespace.
The actual installed1.3.1 binary receives scroll/ref/down/3 and refuses with
SNAPSHOT_NOT_FOUND; source refuses reuse. Exact command audit and OS network/write/
SSH fences retained. No live app target, successful native scroll/visibility,
model generation, UI/app/gateway launch or native171retry is claimed. Prior
WINDOW_NOT_FOUND and incomplete detached accounting remain unresolved.

Four changed source sections apply/hash/reverse on pinned
bf0203a794a07aac3ff764972ab9087baa4e4f4e;1118targets, unrelated patch bytes retained.
New test selection appended without reordering. No schema/default/dependency/
version/tag/release/adoption change or full upstream/unchanged source sweep.

# Agent-desktop explicit-ref type — unreleased

The existing generic type action now forwards an explicitly supplied element to
the provider; it never silently drops that target. Malformed supplied indices
refuse before approval. Original text/index arguments are snapshotted at entry
so the caller cannot swap them while approval waits. Targeted approval summaries
omit typed content; old untargeted preview/signature behavior remains unchanged.
The byte-frozen schema is unchanged. The base optional argument is additive; cua
refuses targeted type before input/focus and gives no physical escalation advice.

Agent-desktop accepts only a latest captured TypeText-qualified ref. Native type
uses exact UTF-8 stdin, including empty input and line ends, with a 10,000-byte cap
and NUL/encoding validation. Reuses locked single-use, lease and placement checks.
Foreground/bring-to-front refuse; no click/focus/coordinate/physical path or retry.
Insertion is at the element's insertion point, not replacement. Native command
completion does not establish intended insertion/caret/application commitment.
The existing type_text response action is retained for backend compatibility.

35 new cases plus 32 existing action, 35 adapter and 20 approval/fence/delivery cases
pass: 122 total across six source files, one worker. Sixteen initial behavioral
reds expose missing dispatch/native support, private preview and invalid target
handling; an initial runner flag error is separate setup evidence. Existing
adapter assertion caught a response-action compatibility mismatch; corrected
implementation retains type_text, without weakening that prior regression.
Cases cover UTF8byte boundary/empty/newlines/invalid text, capability separation,
stale/missing/invalid refs, lease/placement, cancel/error, approval argument swaps,
hardblocks/denial, legacy untargeted dispatch and cua no-input refusal.

Private hybrid: synthetic capture -> actual installed 1.3.1 type CLI, fresh empty
private namespace and stdin. Native SNAPSHOT_NOT_FOUND and source reuse refusal
confirm only refusal; no application was targeted or input delivered. First
setup used a test interpreter missing ruamel.yaml; it failed before native spawn,
config was restored, and the existing full runtime completed the check read-only.
Python audit exact-argv guards and OS network/write/SSH fences remain in force.
No dependency install, native app/gateway/model launch or GUI retry this round.

Five changed source sections apply/hash/reverse against pinned
bf0203a794a07aac3ff764972ab9087baa4e4f4e; 1,117 targets, unrelated patch bytes retained.
The new test path is appended without reordering existing selection. Native round171
WINDOW_NOT_FOUND/resource-accounting failure remains failed; no corrected native
resource gate, real caret/input effect, Windows/Linux runtime or Monitor visual
acceptance is claimed. Full capability/feature release stays open.

# Agent-desktop semantic ref input — unreleased

The existing selected provider now supports semantic click(element) and
set_value(value, element). Only the latest complete app-scoped capture's qualified
refs and advertised Click/SetValue actions authorize input. Capture/input/stop
state is locked; every input attempt consumes authority before native dispatch.
Failed recapture, restart, lease epoch or placement changes invalidate old refs.
Indices never rebind to later snapshots/instances and stay exact JSON integers.
No coordinates, physical/foreground fallback, retry or implicit focus is added.

Native set-value receives exact UTF-8 bytes through stdin, including empty values
and line endings; NUL/invalid encoding/over128KiB refuses before spawn. The house
bounded probe adds bytes stdin and still returns text. A real Python child roundtrip
proves byte preservation; existing text/default/timeout behavior stays covered.
Native responses that may echo values are discarded except for validated command/
disposition structure. Fixed results never expose raw stdout/stderr or values.
An additive recapture-required verdict asks for fresh evidence without asserting
delivery or recommending physical escalation. No verified application-intent claim.

Six source test files pass97cases:32new ref-input cases,35prior adapter cases,
10probe cases including2new stdin cases, and20existing approval/fence/delivery
cases. Reds expose unsupported ref actions and the helper's prior bytes rejection;
one later guidance-wording mismatch is corrected. Tests include concurrent input,
cancellation, pending approval versus replacement capture, human handoff, denied
approval, app mismatch, native uncertainty and secret-result/argument isolation.
These are synthetic protocol successes and deterministic boundary regressions.

The private hybrid check uses a labelled synthetic capture with a fresh private
native namespace. The actual installed binary receives click and set-value stdin
but has no such snapshot, so both return SNAPSHOT_NOT_FOUND. The provider consumes
refs and refuses reuse. No live application is targeted, no successful native
input/application effect is claimed, and no owner app, permissions, model call,
network service or remote machine is used. Native Monitor observation is not
retried; its earlier failed terminal acceptance stays failed.

Changed source sections are packaged/roundtripped separately, preserving unrelated
patch bytes. No schema, default provider, common approval/lease or dependency
change. Full backend/native input success, screenshots and Monitor UI remain open.

# Agent-desktop AX read-only provider — unreleased

The actual provider loader can now select `agent-desktop` explicitly while cua
remains default. One supported operation is app-scoped `capture`, `mode=ax`;
input, focus, listings, screenshots, coordinate scopes and bounded permissions
refuse explicitly. Host reads are also refused for terminal/sandbox or unresolved
placement, including after an already-started backend's placement changes.

Thirty-five new cases plus30status and5provider compatibility cases pass through
the existing source per-file runner. The provider-selection regression fails
before registration. Later boundary reds expose UTF-8 byte limits, failed-start
state retention and placement boundaries; corrections pass. Existing provider
list/error expectations include the new option. Success uses synthetic native
protocol2.6 data through CaptureResult and the real common computer_use handler.
Tests cover scoped identity, complete/unique refs, bounded trees, fixed private
errors, session separation, cheap no-spawn availability and unsupported operations.

The real installed binary is invoked through the selected source provider/common
tool under isolated HOME/config, sanitized environment and OS network/write/SSH
fences, targeting only the stopped private fixture. Its missing-target failure
becomes a fixed common-tool error without raw snapshot/stdout/stderr disclosure.
Initial private live assertion omitted the common `capture failed:` prefix; that
expectation was corrected and its failed receipt retained. This is real error-path
proof, not a successful native snapshot or full backend acceptance. No model call.

Before this source slice, one fresh full-native static Monitor baseline runs with
the read-only observer gate disabled throughout. Native AX reaches Bots while
pixels remain Connecting; exact app-scoped agent-desktop returns WINDOW_NOT_FOUND.
Baseline fails before observer attachment; no observer-cause conclusion or product
fix is inferred. Monitor diagnostics stop and lifecycle is not retried. Guardian
81.52s,60sLocal/zeroSSH gate,4Hermes/8sampled processes,942686208B including guardian
and sampled children/controllers; no savings or full UI acceptance claim.

Six changed source sections apply/hash/reverse against the pinned upstream; prior
unrelated patch sections remain byte-identical. New regression is selected. Source
checks remain sequential and below existing process/RAM ceilings; no dependency,
schema/common-tool/approval/lease change, owner app/data or permission change.
The full act/ref/verify backend and native Monitor terminal UI remain unfinished.

# Native Monitor observation preflight — unreleased

A static full native Local fixture reproduces observation divergence without a
worker or model generation. CUA Chat-to-Monitor images visibly advance; an initial
app-scoped agent-desktop1.3.1 AX snapshot succeeds for that isolated window.
Later, read-only native diagnostics record document visibility=hidden while
BrowserWindow remains visible/not minimized. DOM and CUA AX show an empty filter
result, but the CUA image still shows All/two rows. The later same-app AX snapshot
returns WINDOW_NOT_FOUND while the same main/renderer PID generations continue.
No product, lock, permission or window-destruction root cause is established.

The private assertion audit validates these authority/timing boundaries and
rejects four controls: wrong app, wrong PID generation, absent hidden transition
and absent matching AX result. It explicitly records full observation preflight
and terminal UI acceptance as false. Pixel content is reviewed separately; a
changed image hash or advancing callback clock cannot certify correct paint.
Five native source inputs stay unchanged. No product patch is justified here.

The guardian exits cleanly after174.61s, passing its60sLocal/zeroSSH gate; sampled
peak4Hermes/8including OS probes,937787392B including guardian and sampled native
children. External short-lived diagnostic controllers are outside that RSS
sample, so it is not an all-process benchmark or memory-savings result. Final
PID-generation/task-path closure finds no owned survivors; DesktopSSH0. Fixture
configs are restored and generated runtime/bundles removed. No owner data,
permission change, other host, lifecycle retry, version/release or adoption.

Completed scope is observation diagnosis. Native terminal/report presentation
and the remaining feature gates remain open; next preflight needs scoped baseline
observations before attaching diagnostics. Prior failed lifecycle remains failed.

# Agent-desktop discovery and status — unreleased

The explicit CLI status flag discovers an installed agent-desktop and reads its
status without registering/selecting a runnable provider. Config path takes
precedence and invalid/ambiguous paths fail closed. PATH, local npm ancestry and
source installs, configured/global npm prefixes, Homebrew and extracted release
paths are covered. Windows npm shims resolve to native architecture executables.
The existing default/plugin status route and explicit cua contract checks remain.

Thirty new cases plus two adjacent CLI cases pass. The initial CLI regression
fails before implementation on the unrecognized flag. Windows shim and config
exception cases fail before their corrections. A config roundtrip first showed
that custom keys already save; strengthening it exposed the misleading unknown-
key notice, fixed by registering the optional default path. Tests also cover
ambiguous directories, independent permission states, bounded/scrubbed probes,
invalid/oversized/wrong-command output and no raw output/exception leakage.

The actual Hermes CLI runs config-set then status against the installed workspace
binary with isolated HOME/config and OS network/write/SSH fences. It reports
binary version1.3.1, Accessibility granted, Screen Recording denied and Automation
unknown. Backend cua and an unrelated memory value survive. No guide, snapshot,
app target, permission change, model/provider request or remote operation occurs.
Sampled checks stay below171MiB including their observer; not a product benchmark.

Four changed source sections apply/hash/reverse against pinned bf0203a; all
unrelated patch sections are retained byte-for-byte. The new regression is
selected. No unchanged source sweep, GUI build or lifecycle retry. Companion,
tracked-copy and secret gates are separate receipts. No version/tag/release or
owner-app adoption. The runtime provider, act/ref loop, native target observation
and Monitor terminal UI acceptance remain unfinished.

# Native Monitor delegated-worker activity — unreleased

The full production renderer/main/preload/SDK/query now displays a worker created
by real native delegation, not a seeded roster or host adapter. A private Local
scenario reuses the committed native lifecycle model, RPC and read helpers;
scenario orchestration and bounded observation waits are private test code.
Native RPC creates a named Bot Chat, an independent nonempty side chat and a
distinct nonempty sibling-profile Bot Chat. The parent delegates one real local
file read. Only loopback model responses, timing and usage are simulated.

Matched native CUA pixels and AX show the owning default bot and its Working
worker, step 1/250, elapsed 11s, recorded worker model and fixture token values.
The independent sibling stays separate; the side-chat preview cannot replace
the canonical parent's preview. The completed sub-item is this real active-worker
bridge. It does not establish advancing elapsed pixels or another completed UI
interaction. A private assertion audit rejects wrong source/step and idle input.

The native scenario subsequently records an advancing heartbeat, ended child,
completed terminal ledger, accounted delivery and matching canonical Completed
report. Independent side/profile transcript and report checks remain intact.
Read-only inspection of the retained real database agrees with these receipts.
These are recorded backend assertions, not a passing full native UI scenario.
The terminal UI observation times out: later pixels stay on an older worker and
partial AX changes cannot establish current presentation. The scenario exits 1;
no UI_TERMINAL acknowledgment or full acceptance receipt is manufactured. A
Working-filter attempt likewise does not establish matched visual acceptance.

The trial passes its 60-second Local gate and closes its gateway and known owned
processes. Sampled peaks: 4 Hermes workload processes, 8 including OS probes,
1,059,045,376 bytes (about 1010 MiB) including observed children and the observer.
This is fixture size, not a product memory improvement. Guarded terminal startup
probes are refused; the admitted native file read still completes. A later
fallback trial aborts on a renderer psutil.AccessDenied; accounting is not relaxed
and that trial is not accepted. All owned runtime instances are finally closed.

GOAL12's workspace-only agent-desktop fallback is installed with isolated state.
Status reports Accessibility granted and Screen Recording denied; no permission
or system setting is changed. Scoped name/bundle snapshots return WINDOW_NOT_FOUND.
Installation does not prove UI operation. The private runtime, generated bundles
and installer cache are removed after evidence; the reusable workspace tool stays.

Native terminal/report paint, elapsed advancement, canonical navigation, degraded
refresh, narrow layout and the feature release remain open. No product code,
patch, version, tag, release or owner-app adoption changes. No remote/ai access,
owner state changes, paid model call or unchanged mock-suite rerun.

# Full native Monitor static walkthrough — unreleased

A fresh full production renderer and entry/main/preload run against a real
canonical Local gateway in a private runtime copy. The connection registry holds
only Local; HOME, app-data and both profile configs belong to the trial and have
backups. Unlike the preceding diagnostic-renderer and SDK contract slices, this
uses the actual application, SDK, gateway transport, query and Workspace/Monitor
together. Default and a named profile are real empty definitions; no test code
seeds sessions, workers, reports, roster or query cache. A bounded loopback catalog
serves model/context metadata only and rejects generation, rather than answering
model prompts. The production preload is byte-identical to its fresh build.

CUA opens Monitor in the native application. Matched native pixels and AX show
two source-labelled rows, configured models, unavailable usage/report fields and
zero current worker observations. Name search keeps only the named profile.
Recorded issues produces an empty result for these empty histories; clearing
search and restoring All returns both rows. An explicit Refresh action contains
fresh production route/roster handler returns and real gateway profile reads
inside its recorded interval; all identities remain Local. Existing interval
polling also runs, so total read counts are not attributed to the manual action.
Source checks bind the observed inputs to the renderer build. Receipt assertions
reject missing profiles and wrong source labels. Screenshots establish this
captured wide layout only, not narrow-window behavior or nonempty task filtering.

The final native trial passes its 60-second Local observation, then stops its
gateway and all known owned processes. Sampled peaks: 4 Hermes workload processes,
7 including known OS probes; 942,309,376 bytes (about 898.7 MiB) including every
observed child and the observer. This is fixture size, not before/after memory
savings. Normal Chromium sandbox/proxy, main Node guards and OS gateway/helper
boundaries remain. There are no task SSH attempts, generation attempts or Node
network/filesystem refusals. Both gateway-adjusted configs match their boot
backups. Runtime and generated artifacts are removed after evidence collection.

Earlier setup/capture attempts are separate from this accepted trial. One
metadata-only POST was initially misclassified and refused; its trial stopped.
An earlier trial's exit receipt was unavailable, so its roots were independently
confirmed absent before the final launch. A stale Monitor capture did not recur
and is not treated as a product bug. Native Open chat input later returned
elementHasNoFrame, then noWindowsAvailable: no canonical navigation claim.

Live worker/progress/settlement, nonempty issue/report content, degraded-refresh
paint, narrow layout, packaging and owner-app adoption still gate the feature
batch. No product source, patch, version, tag or release changed. The prior SDK
mock suites are not repeated; fresh companion/release-copy/secret gates remain
separate. The feature is still unreleased.

# Native Desktop profile inventory IPC — unreleased

A fresh bundle from the production Electron entry/main/preload runs in a private
runtime copy with isolated HOME, app-data and a Local-only connection registry.
A real canonical gateway serves two actual fixture profile definitions: default
and monitor-ipc-164. There are no seeded sessions, workers, reports or model
responses. A minimal diagnostic renderer invokes the existing getProfileRoutes
and getAgentRoster methods. The production preload bytes are unchanged before an
append-only diagnostic receipt export; main handler observers return the original
results. The real gateway profile reader is observed without replacing its result.

Both native handler returns match the renderer's deserialized replies. Two real
gateway profile reads occur inside the handler intervals and return exactly the
two names; routes and agents keep Local ownership. The route handler also sees
non-string/duplicate fallback inputs without publishing extra identities. All
sources are Local and the only source is reachable. The runtime remains alive
for the required 60 seconds, with no SSH attempts or Node network/filesystem
refusal records, then
stops its gateway and all recorded owned processes. Core source input hashes and
both fixture configs remain unchanged after the trial.

Final trial sampled peaks: 4 Hermes processes; 6 total including exact known
OS read probes; sampled RSS including every observed child and the observer is
622,247,936 bytes (about 593.4 MiB). The classifier checks executable, parent and
arguments for the startup shell/license probes; pure negative controls keep
actual Electron/Python processes counted. This is workload size, not a measured
product memory improvement. Main uses Node network/process/filesystem guards;
Chromium keeps its normal sandbox and verified loopback-only proxy. The gateway
and Node-spawned helpers retain the OS network/write/SSH boundary.
An auxiliary startup ps read is refused by that OS boundary; both accepted
inventory calls still correlate with the actual gateway reader. Wider startup
health is outside this acceptance.

Setup failures are retained separately: the test-only interpreter lacked anyio;
dev metadata copies lost their relative dependency tree; a stricter outer OS
sandbox prevented Chromium sandbox initialization; the first process counter
included OS probes. The final run uses the existing full interpreter read-only,
real-path source metadata dependencies and the documented split guard layout.
Only the private runtime copy was signed locally; the cached runtime and owner's
app were unchanged. A failed attempt's immediate helper-survivor sample is kept;
a bounded follow-up confirms zero survivors before another launch.

This closes native transport/inventory for these two reads only. It does not
exercise the full Monitor query/work lifecycle, SDK canonical navigation, native
paint/layout, shipped packaging, installed-app adoption or provider billing. No
product code, patch, version, tag or release changes; the Bot Monitor batch stays
unreleased. Existing SDK/preload/query checks are prior results, not repeated
here. Required companion/release-copy and secret-scan gates are separate receipts.

# Monitor Desktop SDK/preload contract — unreleased

Two new rendered integration cases use actual SDK host methods, native preload,
profile refresh, profile request dispatch, real connection/profile atoms,
useRoster, the roster publisher hook and BotsWorkspace/Monitor. Only Electron IPC
responses and gateway I/O supply synthetic facts. Avatars use a placeholder;
activation/navigation actions are refusal traps. No direct query cache or shared-
roster population. The local source owns a named canonical parent and current worker;
a saved, dormant SSH source exposes a distinct same-name bot. Explicit Refresh
preserves the local canonical/worker facts and keeps foreign Open disabled, with
no remote route request, source activation, ambient fallback or chat open. Native
inventory IPC rejection retains the previously published foreign row as
Unavailable while local facts remain usable.

The earlier query regression substituted three SDK host methods. This closes
their renderer-to-preload glue seam, including actual profile-name IPC arguments
and actual descriptor dispatch. It does not execute Electron main handlers,
native IPC serialization, the real gateway pool, a real backend or navigation.
No new product behavior, dependency, capability, setting, storage or version.

A wrong agent-roster preload channel fails on the missing visible foreign row;
the preload is restored byte-for-byte afterward. The final new cases pass, and
five nearest automatic-query/retention/canonical-open cases pass (seven cases
in total). Scoped lint and renderer types pass. A direct typed preload import
initially pulled Electron's separately configured sources into renderer checking;
runtime test import preserves that compilation boundary. An initial retention
fixture omitted the publisher; mounting its real hook corrects the setup without
seeding state. No product fix was inferred from either fixture error.

One new patch section applies, matches its after hash and reverses against the
pinned upstream base. All 1,101 prior patch sections remain byte-for-byte;
the manifest now lists 1,102 targets and selection includes the new test. No
unchanged source sweep or renderer rebuild. Bounded checks used one Node process
plus their observer, sampled below 2.44 GiB, with no surviving owned children.
Companion tests, tracked-only release-copy verification and both secret scans
are recorded separately in the round receipts.

Fresh Computer Use inventory reports unavailable browser access host. Native
Chrome selection then fails SCStreamError -3811 before AX/input; its CUA part
ends immediately with a completion summary. No lock/permission diagnosis, retry,
trial/owner Hermes launch or screenshot acceptance. Native paint, Electron main,
real transport/inventory and actual canonical navigation still gate the Bot
Monitor batch release. No owner data, remote host/ai, ESTOP, pause or timer change.

# Native failure reaches preselected issue controls — component acceptance

One fresh native Local failure now verifies the145issue context and146dashboard
filter/search together. Actual BotsWorkspace/useRoster/provider/query client first
shows the same active child across a natural five-second interval, elapsed7s->12s.
Its canonical reports are still empty. Select Recorded issues and enter the known
local rejection marker: Monitor remains mounted, query success and cached parent/
active child remain intact, while the filtered view correctly has no matches.
These local controls add no request and never claim the native worker stopped.

Only then acknowledge the existing diagnostic barrier. The observer has released
its WebSocket receive lock; acknowledgment changes wrapper return timing only.
The unchanged original native test owns fixture-model reply release, rejection,
terminal ledger/delivery and parent settlement. The next natural query keeps the
selected filter/search and reveals exactly that canonical bot and inline recorded
Error task/error/time. Worker/step and independent profile are absent from the
filtered table; source-qualified raw identities stay separate in the query cache.

The native report's unused summary actually contains the negative-search marker,
while its selected error does not. Searching that marker has no matches; restoring
the error query restores the same bot. Recent reports then opens exactly one full
captured Error report with raw multiline summary/error matching native receipts.
The inline issue uses the stored report timestamp. No manual refetch, cache
injection, prop replacement, second socket or observer lifecycle/SQL write.

Original native real file read, ledger/result, parent response/admissions/delivery,
unchanged isolated config and nonempty independent side/profile/refusal assertions
pass. Seven loopback model replies/usage are fixtures, including the400rejection;
SDK local state/inventory and avatar presentation remain simulated. This short
negative case makes no heartbeat-advance, production billing or RAM-saving claim.

One native attempt passes1case/2deselected; one JSDOM consumer passes10.237s
(17.40sNode runner). Native main18.045s, bounded per-file runner23.72s. Three
successful component roster reads/five captured main-roster reads; helper-scoped
control reads are additional. Peak sampled summedRSS1,410,383,872B including
observer/excluding outer controller, max4sampled processes including observer.
Existing3child+observer/<3.5GiB/180s/loopback/SSH/shell/write fences stay unchanged.
These are guard samples, not continuous peaks or production memory measurements.

Changed-consumer saved-native replay passes plus six HTTP refusal controls. First
replay assertion incorrectly matched the Unavailable filter button as an error
screen; it now checks the Monitor heading plus query success and cached identity.
No native launch preceded the passing replay. Saved fields/retimed active stamps
remain explicitly replay data and are excluded from native proof. Five core source
hashes and frozen private fixture bytes match before/after the sole fresh run.
Product/patch/selection stay unchanged; only acceptance docs/inventory change.

No GUI inventory/input/app retry this round; the prior146browser-host/input
blocker was not refreshed and is not claimed as a new observation. No owner
Hermes/data, ai/other host or ESTOP/pause/timer action. Native-to-production-query-
to-JSDOM acceptance does not prove browser paint/layout, Electron host transport/
inventory or canonical desktop navigation. Those still gate the Monitor batch
release; no version/tag/release/adoption.

# Find recorded issues across bots — unreleased

Monitor adds a Recorded issues dashboard filter and includes each bot's displayed
recorded issue task/excerpt in its existing text search. This finds the bot across
the team before opening a report dialog. Error/Stalled history remains distinct
from current Needs attention or Working; stopped/unknown/completed-only history
and missing reports do not become recorded issues. Worker rows never inherit the
parent's issue. Retained/offline reports remain eligible with their original
source/Open restrictions. No extra request, query policy, store, wire field,
dependency or navigation action; one label covers all nine existing catalogs.

Monitor and Reports share the existing bounded canonical selection/normalization
through botRecordedIssue. Select the first error/stalled record within the first
20before matching; preserve order and trimmed-error-before-summary precedence.
The same normalized120character task and160character excerpt feed both JSX and
search. Hidden older reports, unused summary, record21, side-chat reports and
text beyond those bounds cannot create a search match. Local search and this
filter compose; current filters/sort and captured report dialog keep their rules.

Test-first against prior source:29existing Monitor cases pass,3new cases fail on
missing filter/unsearchable issue text. After the change, Monitor32plus actual
query2and canonical Open integration3pass,37total25.35sVitest/25.76srunner. Cases
cover same-name owners, canonical error/stalled selection, nonissue/missing/
record21 exclusion, worker noninheritance, local historical versus current filters,
normalized/case-insensitive search, clipped/hidden-field exclusion, clearing search,
retained/query-error report reading, disabled Open and filter/query persistence
through fresh data and issue removal. Roster input stays unchanged; no explicit
search/filter action requests a refetch or chat open. SDK/roster boundaries in
these rendered tests remain simulated; no native runtime or paint is implied.

Scoped lint0errors; four new padding warnings fixed in test formatting, leaving
only the same two pre-existing padding warnings from145. Renderer types/build
pass; existing ineffective-dynamic-import warning remains. Final export reflects
only those harmless padding changes after the semantic checks. Four changed
sections apply/hash/reverse against the pinned base; all1097unrelated sections,
1101targets and Desktop170file selection stay unchanged. Required companion,
tracked-copy and secret-scan gates are recorded in the round receipts. No release,
version, tag or per-step CHANGELOG entry; Bot Monitor stays a development batch.

CUA inventory still reports unavailable browser host. Its inventory-only part
ended with a completion summary; no blind native input/app/Guest retry after145's
noWindowsAvailable result, no task server/gateway/model or owner Hermes launch.
No screen-lock inference, screenshot/layout, browser actual-query/degraded-refresh,
Electron host transport/inventory or canonical desktop navigation acceptance.
Those release gates remain open. No owner app/data, ai/other machine or ESTOP/
pause/timer action.

# Monitor recorded issue context — unreleased

The existing Last recorded issue block now shows the selected recorded task,
its stored timestamp and a short error excerpt directly in the dashboard's
report cell. It still selects only the first Error or Recorded stalled task in
the canonical Bot Chat's existing20report window; a later success does not erase
that recorded issue. It never fills worker rows, promotes history into current
attention/Working or borrows another source/side chat. No new request, poller,
store, dependency, wire field, locale key or navigation action.

Task text is whitespace-normalized and bounded to120characters; detail uses a
trimmed nonblank error or summary fallback, normalizes whitespace and stays
within160characters. Both render as escaped plain text with two-line clamps.
Existing nine-catalog labels identify the recorded issue/error/report excerpt.
The stored timestamp is shown under its issue without a completion/success label
for stalled tasks; missing/invalid time and task remain Not reported. Empty detail
adds no fabricated error. Recent reports still opens its full bounded captured
snapshot, independent of later inline data updates.

Test-first:25existing cases pass and4affected assertions fail on original source
because inline task context is absent. Minimal report-component change adds the
context. Monitor29cases pass, including canonical owner/order, error/stalled
history versus current attention, worker exclusion, summary fallback for blank
error, invalid/absent time, clipping/escaped guest text and synchronized inline
refresh while an open dialog preserves its captured task/time/body. Nearby actual
query2and canonical Open integration3cases pass with the same product source.
An initial new filter selector used Attention rather than the existing Needs
attention label; corrected only that test. Renderer typecheck caught an undefined
fixture timestamp outside the number|null wire contract; changed it to null and
reran the affected fixture, scoped lint and renderer typecheck successfully.
Renderer build passes; existing ineffective dynamic-import warnings remain.

Exactly two changed source/test sections apply, match after hashes, reverse and
match pinned before hashes. Other1099sections,1101targets and Desktop170file
selection stay unchanged. Required companion/inventory/secret gates follow in the
round receipts. This remains a development source slice, with no version/tag or
release note until the Bot Monitor capability batch is ready.

CUA browser host is unavailable. Native Chrome AX and screenshot read worked,
but a profile AX click changed nothing; one bounded coordinate fallback returned
server-10005noWindowsAvailable. CUA ended immediately; no Guest/server/native
gateway was started, no owner image saved as acceptance, no lock state inferred.
No paint/layout, browser actual-query/degraded-refresh, Electron transport or
canonical desktop navigation claim. Those release gates remain open; no owner
Hermes/data, ai/other-host or ESTOP/pause/timer action.

# Native Error and Stopped reports through production query — component acceptance

Two more native outcomes now pass through the real roster query and Monitor:
provider rejection after the file read, and authenticated per-child Stop while a
model reply is held. Each runs separately with the unchanged parameterized native
lifecycle test, one existing authenticated socket and its serialized read-only
adapter. Actual BotsWorkspace/useRoster/TanStack interval supplies component data;
SDK local state/inventory, avatar presentation and model replies/usage are fixtures.

The observer waits for same-child active DOM assertions across one natural
five-second interval before returning the test's first active roster read. The
receive lock is released during that diagnostic acknowledgment. The test then
owns rejection/Stop and settlement; the observer never writes lifecycle or SQL.
Each case moves from Working/step1/250 to removed current worker/step and exactly
one canonical report: Error with the recorded rejection text, or Stopped with the
recorded interruption text. Raw multiline summary/error text matches the selected
run exactly. Parent/child/delegation/report/helper identities cross-check against
native receipts; side-chat and independent profile cannot supply the report.
No cache injection, prop replacement, manual refetch, ambient RPC or chat action.

Native assertions retain real file read, terminal ledger/delivery, parent terminal
admissions and nonempty side/profile readbacks. The Stop case independently proves
ended child state before releasing the held reply; delayed success cannot replace
its terminal state, result or assistant transcript. Negative scenarios do not wait
for a heartbeat and make no heartbeat-advance claim; completed-path evidence stays
in the prior acceptance. No new native production behavior is implied.

One native attempt per outcome: Error1pass/2deselected and Stopped1pass/
2deselected; two matching JSDOM consumer cases pass. Each sees elapsed
7s->12s / 7s->12s across the real interval, then three
successful component roster reads/five captured main-roster reads. Max4sampled
processes including observer; largest sampled summed RSS
1,451,474,944B including observer/excluding outer controller. Existing
3child+observer/<3.5GiB/180s/loopback/SSH/shell/write guards remain unchanged.
These samples are resource fences, not continuous peak or production RAM savings.

Both changed-consumer preflights pass against explicitly labelled saved native
fields plus retimed active timestamps; six HTTP refusal controls pass per case.
The first Error replay exposed a test matcher normalizing newlines, while DOM
held the exact raw summary. Exact raw-text assertions fixed the consumer before
any native launch; first evidence is kept. Replay data is excluded from native
proof. Four relevant source hashes stay exact; source/patch/selection unchanged.
This is acceptance documentation/inventory only; no new release/version/tag.

CUA browser host remains unavailable. No input/app/Guest retry, owner app/data or
ai/other-host connection. These tests prove native-to-query-to-component outcome
reconciliation, not paint/layout, actual Electron transport/inventory, desktop
navigation, managed-worker processes or provider billing. Browser actual-query/
degraded-refresh visuals, Electron and canonical navigation still gate the single
Bot Monitor batch release.

# Retained native snapshot through adapter fault — component acceptance

The unchanged completed native lifecycle scenario and actual-query JSDOM consumer
now exercise141retained-refresh behavior together. After initial native active
DOM acknowledgment, the private read-only HTTP adapter refuses exactly three
requests in one natural fetch/retry cycle:503/503/503, with the unchanged5s
interval and1s/2s retry delays. Each refusal returns before native RPC; native
WebSocket, model worker and lifecycle stay running. Focus/reconnect refetches
are disabled. This is simulated adapter failure, not a real gateway/socket drop.

Actual query reaches error after retry exhaustion. Same cache object/content and
child identity stay intact; no ended_at or fabricated completion is added. Monitor
retained notice replaces current work, old worker/step disappear, chat Open is
disabled, and local reports open the honest empty stored snapshot. Empty reports
prove only that captured result, not nonempty native history retrieval/no failures.
Read-only SQLite probes confined to this test's home find ended_at null and
api_call_count1 at both error and pending-recovery acknowledgments. Original native
heartbeat later advances, so UI unavailability never stands in for cancellation.

Existing Refresh starts one pending read. An adapter release barrier (15s deadline)
waits for component assertions; stale notice/cache/Open restriction persist for
1004ms and server read waits1.007s. No automatic successful read can bypass that
barrier. Successful fresh native read restores same worker/Open, elapsed7s->16s.
Original native file read,60s heartbeat, true terminal ledger/delivery/report,
parent admissions and nonempty side/helper/profile refusal checks all pass.
Only model replies/usage, SDK state/inventory and adapter fault/timing are fixtures.
No lifecycle mutation, extra native socket, manual completion or retry-policy change.

Sole native attempt1pass/2deselected68.1s; component1pass54.67s (61.84s Node runner),
native main62.830s. Eleven successful component roster reads/thirteen captured
main-roster reads, plus three refused HTTP attempts that send zero native RPC.
Report/parent/child/delegation/helper/cache/source and raw payload readbacks match.
One Node thread-pool PID retains unchanged3child+observer/<3.5GiB/180s fences.
Max4sampled processes inclobserver, summed peak1,446,084,608B inclobserver/excluding
outer controller. These are guard samples, not production RAM/billing evidence.

Labelled saved-native replay preflight plus six HTTP refusal controls pass. Initial
barrier-only check was strengthened with one full second of pending assertions;
final changed preflight1case19.283s. Replay active timestamps are retimed and no
live DB probe occurs there; it is excluded from native proof. Raw versions kept.
Four relevant source hashes remain exact; product/patch/manifest/test selection
stay unchanged. Only acceptance docs/inventory change. No unchanged mock/type/
build/native-negative sweep. Source141behavior remains unreleased.

Current CUA browser host remains unavailable; no input/app/Guest retry or owner
Hermes launch. JSDOM proof does not establish paint/layout, real Electron SDK
transport/inventory, native gateway failure/reconnect, desktop navigation, managed
workers or provider usage. Native Error/Stopped query report cases are deferred;
browser/degraded-refresh visuals and Electron/navigation still gate batch release.

# Native gateway through production query — component acceptance

One unchanged test_native_worker_settlement_becomes_its_bot_chat_report[completed]
now runs with a private observer and a real-query component consumer. Canonical
per-file Python runner starts the isolated pytest process/public start_gateway;
no CLI daemon/subprocess isolation is claimed. Native agents/delegation/read_file,
60s heartbeat, true successful outcome, ledger/delivery, parent admissions and
nonempty side/profile controls remain real. Seven loopback model replies and
usage are fixtures. No observer SQL or lifecycle writes.

Observer reuses the test's one private-ticket-authenticated WebSocket and one
RPC receive owner, serializing all reads with its lock. It releases that lock
before waiting for the initial active/terminal DOM acknowledgment (up to40s each).
This changes assertion timing, not lifecycle authority. After file-read helper
exit it launches Node directly: Vitest threads/maxWorkers1 avoids another worker
PID. Existing3children+observer/<3.5GiB/180s/loopback/SSH/shell/write fences remain.
No budget increase, competing reader, native restart or second native attempt.

Actual BotsWorkspace selects Monitor; actual useRoster/provider/client merges
unchanged native profiles.list payloads via strict explicit-local SDK boundaries.
SDK inventory/state and avatar presentation are simulated. Focus/reconnect refetch
is disabled; existing five-second interval supplies12component reads, with14
captured main-roster reads including the native test's own. No manual refetch,
cache prefill/prop update, ambient request, activation, navigation or draft call.
Same parent/child/source/cache and helper control identities match native receipts.
Working/step1/250 and elapsed7s ->12s appear, then ended child/step disappear and
exact goal/Completed/MONITOR_WORKER_DONE report opens under the same named parent.
Report/delegation/heartbeat/side/helper identities are independently cross-checked.
Raw input stays unchanged; adapter's loopback port closes after the run.

Native1pass/2deselected in69.1s; component1pass55.52s (62.14s Node runner); native
main scenario63.024s. At most4sampled processes including observer, peak summed
RSS1,444,986,880B including observer/excluding outer controller. These are sampled
guard values, not continuous peak/shared-page accounting or production RAM savings.
Both component acknowledgments and all known PID/birth identities close normally.

Labelled preflight first replays saved137native data with active timestamps retimed;
its1case passes10.157s, six invalid HTTP path/Host/Origin/type/body controls pass.
Initial replay-envelope KeyError was corrected before any native launch. Preflight
is not native evidence. Raw receipts, fixture/guard identities and exact relevant
source hashes are retained privately. No product/patch/manifest/test-selection
change; unchanged mock/native negatives/types/build/source sweeps are not rerun.

This is JSDOM component acceptance through a private adapter. It proves neither
browser paint/layout nor actual Electron SDK inventory/transport, installed app
launch, canonical desktop navigation, provider billing or managed-worker processes.
CUA still reports unavailable browser host; no input/app/Guest retry, owner Hermes
or ai connection. Browser actual-query paint and Electron/navigation gates remain
open; Monitor is unreleased.

# Monitor retained refresh failure — unreleased

Workspace uses the existing cached roster on refresh error, passing optional
stale state to Monitor. With no cached data, the existing ErrorState remains.
A successful empty roster counts as data. Monitor displays a localized polite
status notice and retained-snapshot status, hides unconfirmed current workers/
step/elapsed/Working, classifies rows unavailable for local filters and disables
chat Open. Stored canonical reports, recorded usage/model and captured timestamp
remain readable; no worker is ended or given an invented completion/report.
Existing query interval, retry policy, cache and source identity remain unchanged.
The notice/restrictions persist through pending Refresh and clear only on success.
Raw query errors never enter the notice. All nine existing catalogs cover it.

TDD against original source:25existing pass/3new fail because Monitor/dialog is
removed and stale notice absent. Rendered regressions cover preserved open report
and trigger focus after dismissal, hidden current progress, disabled explicit
Open, Working/Unavailable filters, unchanged input, recovery and absent/empty data.
Actual BotsWorkspace/useRoster case waits for the existing two retries to exhaust
a failed natural poll (four requests including initial success), then reads the
prior Error report without inventing Completed or mutating cached child ended_at.
A held explicit Refresh keeps stale restrictions; successful release restores
current work/Open. It passes8.154s; unchanged interval-success case stays green.

Final31cases across three affected files pass25.88s; scoped six-file ESLint exits0
without warnings, full renderer types0 and bounded Vite build0. Build retains the
existing advancedChunks deprecation/ineffective profile-ops dynamic-import warnings.
Typecheck exposed the prior unchanged Open-chat test's notify mock returning
undefined for a string SDK result; stable synthetic id corrects that test only.
Last lint cleanup changes blank lines only, verified against the typed/tested
bytes; tests/types/build were not repeated for whitespace.

Six changed sections apply/after-hash/reverse/before-hash against pinned upstream;
1,101targets retain unrelated sections byte-for-byte. Existing Desktop selection
170 stays byte-identical. No new gateway API/dependency/storage/poller/version/tag.
This is an unreleased UI source slice, not native/browser visual proof. CUA host
still unavailable; no owner Hermes/Guest/server/gateway/model or launch retry.
Report access uses All/Unavailable; a filter removing an opener keeps the existing
row lifetime boundary. Live actual-query/Electron/navigation gate stays open.

# Monitor automatic workspace polling — unreleased

monitor-query.test.tsx renders actual BotsWorkspace once, selects Monitor through
its button and lets actual useRoster/TanStack scheduling issue the second roster
read on the unchanged 5000ms interval. No manual refetch, invalidation, setQueryData
or prop update. SDK atoms/routes/agents/requestProfile and avatar presentation
are synthetic; workspace/data/routing/mood/Monitor/report modules remain real.
Focus/reconnect refetches are disabled. Only the exact local default route and
profiles.list with empty params are admitted; two request timestamps must be
at least4900ms apart. The condition wait is bounded to8000ms.

The initial current child shows Working, step2/8 and30s elapsed. The next snapshot
ends that same child and supplies the named parent's Completed report: worker and
step disappear, parent reports no active work and exact source/goal/result open.
Same-name unavailable foreign bot remains separate and disabled, lacks canonical
report data and never gains its own query cache. Unrelated side preview is absent;
input stays unchanged. Ambient RPC, activation, chat open and draft calls stay zero.
One connected case passes in5.144s (12.49s runner), scoped ESLint exits0. Initial
failures were incorrect expected idle-label literals, corrected to existing
"No active work reported"; no product behavior was changed to satisfy the test.

Only the new section is apply/after-hash/reverse/absence checked against pinned
bf0203a upstream;1,101targets retain all prior1,100sections. Desktop selection
appends this file only (170files); other selection fields stay exact. No product
API/dependency/locale/version/tag/release change or unchanged source/mock sweep.
This proves offline connected automatic reconciliation, not native gateway/UI,
Electron, real SDK navigation, provider billing or production resource savings.
CUA inventory still reports unavailable browser host; no input/app launch retry,
task browser/server/gateway/model or owner Hermes launch. Live gates remain open.

# Monitor Open chat contract — unreleased

New monitor-open.test.tsx renders actual Monitor with the workspace's onOpen
wrapper and runs real openRosterBot, prepareBotSource, canonical lookup and
requestForBot routing. No action/canonical/data/routing modules are mocked; SDK
RPC/navigation/workspace boundaries are synthetic. Fresh locale/atoms and restored
host spies isolate cases. Same-name local/foreign rows, an unavailable foreign
source, worker, latest side chat and stale canonical tip have distinct identities.

Bot and worker actions each make one exact local title/hidden registry lookup
and open its fresh returned tip with the captured route/workspace owner. No
boundary call occurs before gesture; disabled foreign action is inert. Ambient
RPC, activation and draft spies refuse calls; exact one session.list excludes
create/prompt. Registry rejection settles with an explicit error notification,
no desktop open/draft/claim and no fallback to a worker or side conversation.
Three new cases and nearby Monitor/row-action/registry suites pass; scoped ESLint
passes. This is an offline rendered integration contract, not actual SDK desktop
open, browser visuals, live gateway or Electron navigation proof.

One new patch section applies/hashes/reverses against pinned upstream;1,100targets
and all prior sections remain. Test selection appends this file only. No product
source/API/dependency/locale/version change. CUA inventory still reports browser
host unavailable; no native/Chrome input retry, task window, model/gateway/server
or owner Hermes launch. Existing live useRoster/Electron/navigation gates remain.

# Monitor roster-query settlement — unreleased

One added case in existing data.roster.test.tsx runs actual useRoster and a real
TanStack QueryClient/provider against host-boundary responses, without mocking
the hook. It waits for successful active data, then performs real refetch and
checks the same named parent, ended child, exact report, local route/source health
and source-qualified cache key. One merged row, untouched input and no ambient
request guard source attribution. Boundary responses are synthetic: this is no
native or live browser claim. The file's backed-up input equals pinned upstream
bf0203a794a07aac3ff764972ab9087baa4e4f4e. Its changed section applies/hashes/reverses.
That existing test file is newly included in selected Desktop tests; all previous
selections and patch sections remain. Source inventory becomes1,099targets.

Query20 and Monitor24 checks pass,44total, with scoped test ESLint. An initial
assertion was tightened to wait for query success before checking the active
worker; final44checks pass13.77s. No product source/API/dependency/locale change.

A task-private fixture replaces the earlier adapter poller with actual useRoster,
shared queryClient/provider and dataUpdatedAt, plus explicit stable local/profile
atoms and a narrow local host adapter. Only exact local profiles.list is routed
to the pre-existing native test socket; simulated source inventory is labelled.
Raw result stays unchanged, production hook owns merge/annotation/reconciliation.
No fixture timer/cache prefill; unsupported ambient/chat actions are refused.
The fixture builds, using the existing installed TanStack module after correcting
its out-of-tree import resolution. Failed build output is retained separately.
Build success does not establish runtime adapter/provider/cache behavior.

Execution is unrun; integration remains unproven. Chrome AX/menu actions left UI
unchanged, a bounded coordinate fallback returned Computer Use server-10005
noWindowsAvailable, and listBrowsers reported access host unavailable. CUA part
ended with completion summary; no Guest window, static service or native gateway
was started. No screenshot/worker/refresh acceptance is claimed this round, and
no alternative non-CUA automation or blind Hermes launch was used. Native selector,
live useRoster and canonical navigation remain open before the feature release.
Unchanged native lifecycle, full renderer/types and prior UI matrices were not
rerun. Source/fixture/errors/build hashes are retained privately; no owner Hermes,
ai/other host or ESTOP/pause/timer action. This is a completed offline regression
step, not completed live acceptance or a release.

# Monitor native-to-browser settlement — unreleased

Actual Monitor, Reports, production CSS and production mood/source helpers ran
in Chrome Guest at1140×620 against fresh profiles.list responses from the real
local native gateway scenario. A task-private pytest observer serializes reads
on that test's one authenticated WebSocket; no second socket, lifecycle SQL,
product API or product poller. Its static/roster server binds127.0.0.1 only.
Model replies/timing/usage remain simulated; native agent/delegation/read_file,
heartbeat, terminal ledger/delivery and canonical reports remain real.

CUA shows the same scoped child Working at step1/250; real reads advance elapsed
9s ->39s. Working filter hides the independent helper, All restores it. After
normal native settlement, current workers become0 with no stale Working/step,
canonical parent preview becomes its completed acknowledgement, and that child's
Completed report opens with MONITOR_WORKER_DONE. Raw child/parent identities
match native roster, browser DOM-checked receipts and native DB assertions.
Current-tool facts are absent after the read and remain missing. Helper source
status stays Unknown: this adapter supplies no Electron source metadata.

Images under ../evidence/local-ui-20261116/: r137-browser-active.jpg,
r137-browser-progress.jpg, r137-browser-settled.jpg and
r137-browser-completed-report.jpg. Unaltered CUA bytes/hashes/call/time identities,
19 raw roster reads, DOM-checked active/terminal receipts and native output stay
private. The native test source is byte-identical. Completed case passes with
its real heartbeat, terminal/delivery/report and both nonempty independent
side-chat/profile controls. Its85.618s includes deliberate UI receipt waits;
92.1s per-file runtime is not a production latency measure. Seven model requests
are fixtures. Initial pytest -p argument collided with Hermes profile parsing;
that setup failure is retained. Standard PYTEST_PLUGINS loading resolves it
without product/test/guard changes or automatic retries.

Three added rendered cases cover active -> Completed/Error/Stopped report,
removing ended workers' stale step/tool/Working state. Monitor24+31 nearby checks
pass,55total; scoped test ESLint and the actual-component fixture build pass.
Unchanged full renderer/types/backend negatives are not rerun. Eight exact
Host/Origin/path/POST/CSP controls pass; only same-origin roster and view-receipt
requests are allowed, no credential leaves the test observer. Guest closes to
its original owner new-tab window; native test closes the owned server/socket.
Sampled native peak425132032B inclobserver, max4processes inclobserver, unchanged
180s/<3.5GiB/3child fence. Not continuous OS peaks or browser RSS accounting.

This is browser fixture adapter acceptance, not Electron launch, useRoster,
real chat navigation, production billing/model quality or RAM savings. Those
native integration gates still block the Monitor batch release. One changed
patch section applies/hashes/reverses;1,098targets and selected tests retained.

# Monitor report focus — unreleased

Original `BotMonitorReports` conditionally mounted a Dialog without a Trigger.
Escape and Close removed the dialog but left keyboard focus on BODY. The existing
SDK DialogTrigger now wraps the snapshot-capturing button inside a persistent
controlled Dialog root. Radix restores its trigger ref; no manual focus callback,
timer, global primitive, request, dependency or routing change is involved.

Two added rendered tests fail on the original component at the exact focus
assertion, then pass after. Each dismissal checks the precise source-qualified
opener for two bots both named Writer, dialog removal and no chat/refetch calls.
Monitor21 plus31 nearby tests pass, 52 total; scoped ESLint, renderer TypeScript
and full renderer production build pass. Existing snapshot/filter tests remain.

A private Chrome Guest preview uses actual Monitor/Reports, SDK primitives and
production CSS, saved synthetic native134 snapshots plus labelled layout props.
Before build substitutes the backed-up original report module at Vite transform;
after build consumes final source. No product source swap while processes run.
At 1140×620, original Escape leaves BODY focused. Fixed Escape returns focus to
native-completed's report button; Close returns it to native-interrupted's button.
Fresh AX focus and the fixture's read-only DOM focus receipt agree. Matched
unaltered screenshots under `../evidence/local-ui-20261116/` are
`r136-browser-escape-before.jpg` / `r136-browser-escape-after.jpg`;
`r136-browser-close-after.jpg` records the second opener. Stored Stopped report
pixels match AX in `r136-browser-stopped-report.jpg`, replacing the prior round's
unaccepted stale capture with new browser evidence. Raw image/source identities,
red/green output and closure receipts are private round evidence.

Browser fixture has no Electron bridge/backend and refuses network requests via
CSP and explicit client guards; its static server binds only 127.0.0.1. Guest
closed to the original profile picker, owned server stopped. No owner profile or
Hermes app opened. Missing opener after actual row removal remains a natural
limit. Native selection/progress/settlement still gate the Monitor feature batch.
Only two changed patch sections were apply/hash/reverse checked; selection and
1,098 targets retained. Unchanged backend/native/mock suites were not rerun.

# Monitor browser layout — unreleased

Actual `BotMonitor`/`BotMonitorReports`, SDK primitives, i18n and production CSS
were built into a loopback-only offline preview and operated through CUA in
Chrome Guest. The iframe viewports were 1140×620 and 480×620 CSS pixels, including
report portals. Saved synthetic native134 outcome rows and separately labelled
layout fixtures supply props. The explicit locale client supplies English only
and refuses saves; no Electron bridge or backend behavior is invented.

The model-column defect reproduced after correcting the fixture's Tailwind source
scan: actual cell widths were 60.89px and normal model labels broke into fragments.
Adding only `min-w-48` to the model cell preserves a 12rem minimum, its existing
long-token wrapping and local horizontal scrolling. The browser geometry assertion
(`width >= 160`) fails before and passes after: all seven model cells measure
192px at both viewports. Matched images and the horizontally revealed narrow
model view confirm readable text; this is not a CSS-class mirror assertion.

Private unaltered CUA images under `../evidence/local-ui-20261116/`:
`r135-browser-wide-red.jpg` / `r135-browser-wide-green.jpg`,
`r135-browser-narrow-red.jpg` / `r135-browser-narrow-green.jpg`, and
`r135-browser-narrow-readable-models.jpg`. Image hashes, tool-result identities,
fixture source/row hashes and geometry/action receipts are retained with the
round evidence. The earlier `invalid-css-fixture` image is excluded from the
product reproduction: it lacked generated utilities and was a harness defect.

Observed controls include empty search, Working filter and token-sort action.
The narrow long report wraps Thai and unbroken text within its dialog; the
Completed outcome filter gives the expected empty snapshot. Escape dismisses it.
Focus was then observed on the HTML document rather than the opener; follow-up
remains. Later AX showed the saved native Stopped report while screenshots still
showed an older dialog, even after fresh screenshot/Raise. Those stale pixels do
not count as report visual acceptance. No broad focus/layout/accessibility pass.

Existing Monitor19 plus31 adjacent rendered tests pass, 50 total. Scoped ESLint,
renderer TypeScript and full production renderer build pass. Only one source
class changes; no new dependency, locale, field, request, routing or worker policy.
One changed patch section applies/hashes/reverses; selection and 1,098-target
inventory remain unchanged. Native/backend regressions are unchanged and were
not rerun. No live worker, real chat navigation, auto-refresh, billing or native
Electron proof follows from this offline fixture. The task Guest tab and owned
asset server are closed; no owner profile or Hermes app was opened. Feature
release remains pending native Monitor progress/settlement acceptance.

# Native Monitor lifecycle integration — unreleased

`tests/gateway/test_bot_monitor_native_lifecycle.py` follows three actual native
delegations through the public gateway lifecycle and authenticated private-control
ticket/WebSocket API. Each creates the named Bot Chat, submits its parent turn,
identifies one real subagent and checks persisted `read_file` output while its
next model reply waits. Completion, provider rejection and explicit Stop all
reach native terminal records, async ledger delivery, parent acknowledgement,
and the same canonical report consumed by Monitor. No main-task SQL seed,
status/heartbeat write, terminal repair or ledger fabrication supplies evidence.

- Success retains the normal durable heartbeat and completed task/report.
- A scoped HTTP400 `invalid_request_error` after the active read produces a native
  failed task with error exit reason and the rejection text in the Error report.
- Authenticated `subagent.list` identifies the target delegation; owned
  `subagent.interrupt` returns found. The child ends before its held reply is
  released. After the reply handler finishes, ended-at/API count are unchanged
  and no successful worker result is persisted. Task/report remain interrupted
  (Stopped), distinct from Error. Both negative single-child units record batch
  error; the per-task result, not that unit label, determines the report.

Nonempty side-chat and sibling Bot Chat controls persist through the same API.
Their identities/transcripts/report scopes remain independent before and after
settlement. Canonical token fields match the stored parent row; no worker sums.
An unknown profile stays refused. Each 180-second deadline starts at its main
submission and covers outcome, parent delivery and report; negative cases omit
the unchanged 60-second heartbeat wait.

All three parameters pass serially together in one canonical per-file process,
with repository fixtures/guards, one worker, zero automatic file retries and
scoped scratch/output retention. Final result: 3 passed and 5 existing WebSocket
and uvicorn deprecation warnings in 75.33 seconds. Submission-to-receipt times:
61.896s success, 2.513s rejection, 2.470s interrupted; 21 loopback model requests.
Sampled maximum: 3 processes including observer and 473,399,296 bytes RSS, under
the unchanged limit of 3 children plus observer, less than 3.5GiB, and a 180s
outer deadline. These are sampled test resources, not continuous OS peaks,
production memory savings or provider usage. No full shell-wrapper/CI-parity
claim. The gateway shares the pytest interpreter, imports, environment and event loop. Model
content/timing/usage are loopback fixtures, not billing or model-quality proof.
Task-only OS fences deny auxiliary login-shell execution; the real regular-file
fast path still reads its marker. This is not shell-tool, CLI daemon boot/signals,
subprocess-boundary, native layout or on-screen progress acceptance.

Development checks retained: individual success/rejection passes; one stopped
startup refused by the unchanged process limit before cancellation; one combined
run exposed conftest's fixed DB-path pin. Existing multiplex-test dynamic-path
setup corrects the fixture without changing product code or weakening guards.
The final complete-file run establishes cohabitation; isolated passes alone do
not. No runtime/API/renderer/dependency change. Scoped Ruff and code health pass.
One changed section applies/hashes/reverses against the pinned base; 1,098 targets,
selection and unrelated sections retained. Native target selection and Monitor
visual/progress/settlement acceptance remain open; no feature release.

# Recorded task reports in Bot Monitor — unreleased

Recent reports opens a source-qualified local snapshot of recorded async task
outcomes, bounded report/error excerpts and completion times, with outcome
filters. The main bot row names the last recorded issue in its bounded snapshot.
Completed, Error, Recorded stalled, Stopped and Unknown stay distinct. A mixed
completed batch may contain failed tasks; missing task status/index cannot borrow
unit success or another task's identity. Historical outcomes never establish
current work/blockage or change worker/attention eligibility. Canonical chat
opening stays on the existing named bot action.

The shared read-only helper uses exact preferred compression-chain ids from the
existing walker (replacing the tip-only walk, not changing its policy). Both
canonical readers use their existing scoped store/cache. Ordinary latest-session
summaries keep their prior shape. At most20terminal ledger rows and20tasks per
canonical chat; SQL bounds task JSON at16384characters and result JSON at65536
before decoding. Existing forced redaction precedes goal256/summary2048/error512
character cuts; no raw-JSON fallback. Only id/index, normalized status, timestamp
and those text excerpts are projected. Malformed/oversized records can retain
known unit failure but never imply successful batch tasks. Missing/legacy/read-
error data omits reports without losing canonical usage/identity. Empty/partial
snapshots are not proof of no failures. Redactor imports remain on demand.
Nonempty report projection binds only the store's home ContextVar and restores
it in finally; no new secret hydration or process-environment mutation. Two
separate profile vault registries are tested under a different launch scope,
without applying launch-profile values to the sibling's output.

Ten new Python cases first produced9missing-field failures/1passing absence case,
then all10passed. A later sparse/missing batch status/index probe correctly
reproduced false unit-success/name borrowing and went red→green. A separate
registered-vault-value probe reproduced scrubbing under the wrong launch home;
red→green binds the store's home and restores the ambient caller context.
Final12new+8canonical-usage+10worker-reader+6canonical-read cases =36pass. Real temporary
SessionDB and read-only attachments cover preferred compression, branch/reset/
delegate/tool/sidechat decoys, distinct homes, subject privacy, mixed batches,
row/task bounds, malformed/oversized payloads, old wire data, failed reads,
forced redaction before cuts, nonsecret text budgets and whitelisted output.
The unchanged canonical per-file engine uses task-local scratch, repository
conftest/guards,1worker/no retry and reused pytest/Ruff tooling. Not an unqualified
shell-wrapper/CI-parity or full source/control-suite claim.

Five new rendered report scenarios first failed as expected; the responsive
shared-Select filter also reproduced its missing combobox before implementation.
Final19Monitor+31nearby UI =50pass in5files. Explicit open/close, local filters,
neutral stopped/unknown, absent versus empty, escaped guest text without links,
same-name source isolation, retained data and captured snapshots across refresh
are covered without refetch/chat navigation. All9catalogs cover new chrome.
Scoped ESLint0warnings, renderer types/build, generated check and code health
0blocking/0advisory pass. Build retains the unrelated ineffective-dynamic-import
warning in profile-ops. Twelve changed sections apply/afterhash/reverse/beforehash
against the pinned base;1097targets, unrelated sections exact. Only the new
Python test appends; previous selection order/metadata retained.

No native app/CUA trial: the prior noWindowsAvailable control/capture condition
has not changed. No new native visual/layout, before/after pair, live worker,
billing,60-second launch or RAM-saving proof. Owner app/data,otherhosts,ai,ESTOP,
pauses and timers remain untouched. Full Monitor stays partial/unreleased until
native layout/progress/settlement acceptance; no feature release or adoption.
[Design](design-bot-monitor.md#recorded-task-reports-slice).

# Canonical Bot Monitor usage — unreleased

Bot rows now display tokens, recorded estimates/provider-reported amounts and
model from the resolved named Bot Chat row. They keep configured model separate.
One selected usage source drives display and token sorting; workers never borrow
missing fields from the canonical row. No side-chat fallback, root/tip addition
or worker rollup. Stored usage does not establish current work or lifetime totals;
elapsed/tool/step remain worker-only. Ordinary latest-session summaries retain
their prior shape; a canonical alias may share its own enriched summary.

The five existing usage fields share one projection. Both canonical readers use
already-selected rows, with optional Python/TypeScript/generated OpenRPC contracts.
No added query, provider, polling, timer, dependency or storage/schema migration.
Eight new Python cases had seven expected missing-field failures and one passing
absence case before implementation. All eight then pass with 34 shared usage/
worker checks; six nearby canonical read cases pass separately: 48 total. Real
temporary SessionDB stores and read-only attachments cover compressed/uncompressed
chats, separate homes, recency/worker decoys, ordinary summaries, absent/zero,
legacy/unified parity, older contracts and subject privacy without config leakage.

The unchanged canonical per-file engine uses task-local scratch redirection,
repository conftest/guards, one worker and no retry, reusing the preceding round's
tool-only pytest environment and Ruff. This is actual pytest with that runner
adaptation, not shell-wrapper/CI parity or a full source suite. One wider run was
stopped by the conservative process guard when a mixed read/control file spawned
an extra descendant; all owned children ended. Its partial successes are not a
passing full run. Final four usage files pass 42 cases, and the six read cases
pass separately without relaxing the guard. No full mixed control-file claim.

Three new rendered scenarios failed before implementation; final 14 Monitor
plus 31 nearby UI cases pass in five files. They cover source selection, token
sorting, missing versus zero, model labels, unchanged opening and no invented
work/elapsed. Scoped ESLint, renderer types, bounded build, generator check and
code health (zero findings) pass. Eleven changed sections apply/hash/reverse
against the pinned base; unrelated sections stay exact. The kit has 1094 targets
and appends only the new Python test, preserving prior selection order/metadata.

No native app or Computer Use trial was started: the previous noWindowsAvailable
control/capture failure has no changed condition. Prior evidence and rollback
remain. No new native visual/layout/lifecycle, 60-second launch, billing or RAM
savings proof is claimed. Owner app/data, other hosts, ESTOP, pauses and timers
were untouched. Full Monitor stays partial/unreleased, with error/stuck/report
and native acceptance next. [Design](design-bot-monitor.md#canonical-bot-usage-slice).

# Recorded Bot Monitor usage — unreleased

Monitor worker rows now display recorded USD estimates and recorded provider-
reported amounts separately, with a persistent partial-coverage/not-invoice hint.
They are never added together. The existing SessionDB row projection sends
positive finite recorded amounts even after unknown/included latest pricing;
storage-default zero stays null unless the matching pricing status supports a
recorded zero. Missing, negative and nonfinite values stay unavailable. Tiny
positive amounts do not round to zero; signed zero displays as zero.

Recorded worker model and configured bot model carry distinct labels; a missing
worker model never borrows the bot route. This is stored metadata, not a live
binding or an invoice reconciliation. Optional Python/TypeScript contracts and
generated TypeScript/OpenRPC agree, including the already-declared parallel
observations. Both unified and legacy readers reuse the existing bounded row
read/cache; no added query, pricing lookup, provider call, timer, dependency or
storage/schema migration.

Twenty-four new Python cases first failed on missing fields, then passed with
26 nearby activity/roster checks: 50 tests in five files. They use real temporary
SessionDB stores, read-only attachments, legacy/unified parity, separate homes,
old optional contracts, invalid/default/known-zero/partial costs and bounded
model metadata without config canaries. The canonical shell wrapper could not
run here: pytest was absent, then its fixed /var/tmp scratch violated owner write
scope. Tool-only pytest/asyncio and pinned Ruff were installed under the isolated
work folder. The unchanged canonical per-file engine ran with task-local scratch
redirection, repository conftest/guards, one worker and no retry. This is real
pytest proof with that runner adaptation, not an unqualified shell/CI-parity or
full Hermes suite claim. Owner runtime environment was borrowed read-only.

Two new rendered scenarios first failed on missing cost/model UI. Final 11
Monitor tests plus 31 nearby tests pass; signed zero was separately reproduced
before normalization. Scoped ESLint, renderer types, code health (zero findings)
and bounded build pass. Twelve changed patch sections apply/hash/reverse against
the pinned base; unrelated sections remain. The kit has 1093 targets and appends
two Python test files while retaining prior selection order and metadata.

One final-artifact native Local trial tested the previously unobserved foreground
boundary with passive focus telemetry and baseline GPU flags. CUA read AX and an
inactive New session screenshot, but the single observed-titlebar coordinate
click returned noWindowsAvailable. Action completion and foreground focus were
not established; no Bots/Monitor navigation followed. The bounded probe stopped
without further activation, Reload or restart. No native dashboard visual,
before/after layout, actual worker lifecycle or production paint fix is claimed.
The capture/presentation/control boundary remains unresolved.

The actual Local SSH-zero gate lasted 60.042 seconds; across 824 samples at most
four Hermes processes were observed, with observer-inclusive RSS maximum
885,653,504 bytes. These are bounded samples, not a continuous peak/physical RAM
or savings measurement. Synthetic worker costs/models and one canonical fixture
message are not actual usage, billing, tool execution or worker activity. All
owned processes, ports and Computer Use ended; the original 313-entry trial
bundle/strict signature restored and three fixture config byte/mode baselines
were preserved. Owner daily app/data, other hosts, ESTOP, pauses and timers stayed
untouched. Existing unrelated external SSH sessions were left intact; SSH-zero
is scoped to Hermes Desktop.

This completes the recorded-usage source slice, still unreleased. Error/stuck/
report authorities, native layout/live lifecycle acceptance and full Monitor
remain open. [Design](design-bot-monitor.md#recorded-worker-usage-slice).

# Bot Monitor first dashboard slice — unreleased

Bots → Monitor now gathers visible bots and current worker observations into one
searchable table, with status filters and Name/Elapsed/Tokens sorts. Worker rows
show reported task/signal, tool, step, elapsed and token facts; explicit Open chat
uses the captured parent bot's existing source-qualified canonical action. Cost
is not reported, the model is explicitly configured, and missing/invalid counters
remain distinct from reported zero. Cards and Manage team remain accessible.
Successful roster refresh timestamps re-evaluate age even when data is identical;
no extra request, timer, dependency, storage key or backend authority is added.

Nine rendered Monitor regressions pass, alongside 31 nearby workspace, worker
and row-helper checks: 40 tests in five files. The initial eight failed before the
control existed; a ninth reproduced stale work after an identical refresh before
the timestamp dependency was added. Final scoped lint, renderer types, code health
and bounded renderer build pass. Seven changed patch sections apply, match their
after hashes, reverse and match the pinned base; unrelated sections are retained.
The kit has 1091 targets and appends the Monitor test to its existing selection.

Two isolated native Mac Local attempts used the earlier dashboard artifact before
the refresh-age follow-up. The first captured Connecting while AX reached Bots.
Adding disable-gpu in the second changed the initial captured surface to the
connected New session page, but later Bots navigation and native Raise still left
that old surface in the screenshot while AX showed Bots and two synthetic worker
observations. No native Monitor visual acceptance, before/after dashboard pair,
real worker lifecycle, production paint fix or final-artifact live proof is claimed.
Load milestones without observed fail/crash events do not establish painting;
capture versus presentation remains unresolved. No Reload or restart retry chain.

Both actual 60-second gates reported zero app SSH attempts/executions, with at most
four Hermes processes. Sampled observer-inclusive RSS maxima were 884,506,624 and
1,075,200,000 bytes; these are bounded samples, not continuous peak/physical RAM or
savings measurements. Synthetic SessionDB observations ran inside the existing
gateway process, without inference or worker processes. All owned processes,
ports and Computer Use ended; the original 313-entry trial bundle/signature and
fixture config baselines were preserved/restored. Owner app/data, other hosts,
ESTOP, pauses and timers were untouched. Existing unrelated external SSH sessions
were left intact; the zero-link claim is scoped to Hermes Desktop.

This completed source slice stays unreleased under the batched release policy.
Cost/error/stuck authority, report navigation, native layout/live lifecycle proof,
daily-app adoption, Linux/ai and the full feature remain open.
[Design and next steps](design-bot-monitor.md).

# Native Mac Projects preference persistence — v0.33.8 follow-up

In **Settings → Workspace → Projects & discovery**, default's Working Directory
changed to a synthetic trial folder, discovery was switched off, roots changed
to two bounded folders and the exclusion list changed to a child path. The native
off flag was confirmed before either list edit. The final focused exclusion edit
went directly to Shell environment without Enter or a separate blur; returning
retained all four values. The new-chat profile stayed scope-c during this flow.

Settings switches read scope-b and scope-c's distinct original paths and on/off
values, then default's edits. Parsed native comparison found only `terminal.cwd`,
`desktop.repo_scan_enabled`, `desktop.repo_scan_roots` and
`desktop.repo_scan_exclude_paths` changed. All unrelated default values and both
other profile files were preserved. Every first app/gateway/helper and guardian
ended before fresh processes reopened the same home, app data and exact signed
diagnostic bundle. All three profiles showed their previous values without another
edit; all three saved config hashes and modes matched. Session, message,
delegation and hosted-room counts stayed zero.

Actual Local SSH-zero gates lasted 60.068 and 60.082 seconds. Across 1291 and 841
samples, at most four Hermes processes were observed; observer-inclusive RSS
maxima were 929,218,560 and 865,173,504 bytes. These are bounded samples, without
continuous-peak or savings claims. All owned processes/ports and Computer Use ended
before original config baselines and the 313-entry trial bundle/signature restored.
Owner app/data, other hosts, ESTOP, pauses and timers were untouched.

This is named preference acceptance on v0.33.8, without a source/build change or
new release. No Send, inference or terminal/file tool ran. Actual discovery
results, empty-root home scanning, cwd effects, invalid paths, pending-save races,
crash durability, all Settings pages, daily-app adoption and Linux/ai remain open.
Earlier startup paint symptoms remain unresolved. [Scope and limits](settings-autosave.md#native-mac-projects-preference-persistence-v0338-follow-up).

# Native Mac attachment cap Escape persistence — v0.33.8

In **Settings → Chat → Attachments**, a focused 1 MB draft followed by Escape
reopened as 16 MB on the before build, with no saved cap file. The final build
writes the device-wide 1 MB cap before closing; reopening and a Settings profile
switch show 1 MB. Fresh app/gateway processes reopen the same home, app data and
exact signed diagnostic bundle and read 1 MB without another edit. Saved cap
bytes/mode and all three unchanged native profile configs match.

The real rendered overlay regression fails four cases on backed production bytes
with 29 controls passing; the fix passes all 33. Nearest selection totals 76
passing cases, with no new act-warning headers. Scoped lint, renderer types,
bounded renderer build, health and changed-section base/apply/hash/reverse checks
pass. Prior test selection and unrelated patch sections are retained.

All three actual Local SSH-zero gates pass. The first final observer was
interrupted before final statistics; its raw 60-second gate remains, and recovery
verified recorded process/guardian/port closure before fresh launch. Completed
before/reopened observers record at most four Hermes processes. Session, message,
delegation and hosted-room counts stay zero. All owned processes/ports and Computer
Use end before original cap absence and the 313-entry trial bundle/signature
restore. No owner data, ai/other host, ESTOP, pause or timer change.

This proves saving/reading the named cap, with no actual attachment-limit, upload,
native IME, crash-durability, memory-savings or whole-Settings acceptance claim.
The daily app is not rebuilt. [Implementation and limits](release-notes-v0.33.8.md).

# Native Mac Workspace preference persistence — v0.33.7 follow-up

In **Settings → Workspace**, default's Persistent Shell was switched off, and
File Read Limit changed from 100000 to 120001. The focused number edit was followed
directly by navigation to Shell environment, without Enter or a separate blur.
Returning to Files & execution retained 120001. Settings profile switches read
scope-b on/100000 and default off/120001 without another edit. The new-chat profile
remained scope-c during this first flow.

Native comparison found only default's `terminal.persistent_shell` and
`file_read_max_chars` changed; all unrelated values and both other profile files
were preserved. All first writers and the guardian ended before fresh app/gateway
processes reopened the same home, app data and exact signed bundle. Both profiles
showed their saved values, and all three config hashes and modes matched the
checkpoint. Session, message, delegation and hosted-room counts stayed zero.

Actual Local SSH-zero gates lasted 60.053 and 60.124 seconds. Across 1029 and 902
samples, at most four Hermes processes were observed; observer-inclusive RSS
maxima were 922,025,984 and 893,829,120 bytes. These are bounded samples, without
continuous-peak or savings claims. All owned processes/ports and Computer Use ended
before original config baselines and the 313-entry trial bundle/signature restored.
Owner app/data, other hosts, ESTOP, pauses and timers were untouched.

This records existing v0.33.7 preference persistence, with no source/build change
or new runtime release. No terminal, SSH backend, file-read tool or model ran.
Their behavior, numeric boundaries, crash durability, persistence before 550 ms,
Projects controls, all Settings, daily-app adoption and Linux/ai remain unverified.
Earlier startup paint symptoms remain unresolved. [Scope and limits](settings-autosave.md#native-mac-workspace-preference-persistence-v0337-follow-up).

# Native Mac Chat behavior persistence — v0.33.7 follow-up

The existing Reasoning Blocks switch in **Settings → Chat → Behavior** saved off
for default while scope-c was selected for new chats. Direct navigation to
Attachments and back retained off. Native comparison found only the intended
`display.show_reasoning` and `display.platforms.cli.show_reasoning` changes; every
other default value and both other profiles were preserved. Settings read scope-b
as on and default as off without another edit.

All first writers and the guardian ended before fresh app/gateway processes opened
the same home, app data and exact signed bundle. The same off/on values appeared;
all three config hashes and modes matched the saved checkpoint. Native session,
message, delegation and hosted-room counts stayed zero. No Send or model request.

The two actual SSH-zero gates lasted 60.129 and 60.075 seconds. Across 1090 and
733 samples, at most four Hermes processes were observed; observer-inclusive RSS
maxima were 898,301,952 and 880,181,248 bytes. These are bounded samples, without
continuous-peak or savings claims. All owned processes/ports and Computer Use ended
before the original three config baselines and 313-entry trial bundle/signature
were restored. Owner app/data, other hosts, ESTOP, pauses and timers were untouched.

This is acceptance evidence for existing v0.33.7 behavior, with no source/build
change or new runtime release. Startup paint remains unresolved; successful
launches here do not establish reliability. Reasoning output, every Settings page,
crash durability, daily-app adoption, cross-device and Linux/ai remain unverified.
[Scope and limits](settings-autosave.md#native-mac-chat-behavior-persistence-v0337-follow-up).

# v0.33.7 — Confirm per-Bot membership saves

Unchanged native before: Create & join checks a membership and clears the name
while profile.yaml stays absent in a write-denied target folder. No failure warning.
Final native build: the same denial retains the name, shows the local-only warning
and Retry. Restoring folder write access alone does not create metadata; explicit
Retry saves it. A second denied removal preserves native bytes and the bot's other
group; Retry confirms the intended removal. Remove-all clears only that bot.

All first writers/guardian stop before new app/gateway identities reopen the same
home, app data and exact signed artifact. Retained memberships remain checked;
removed memberships remain unchecked. Native metadata/config bytes and modes
match for all three profiles. Sessions/messages/delegations/hosted rooms stay empty;
no Send, model fixture, inference or dispatch. This is the existing per-Bot legacy
metadata path, not canonical-room roster editing or cross-device acceptance.

Initial rendered red4/2 controls; explicit Retry/sticky-failure red2/5 controls;
final nearest34 pass, including pending, fallback, removal, later draft and Japanese
feedback. Types/build and scoped health0/0 pass. Lint adds zero diagnostics to six
errors/one warning reproduced against backed baseline bytes. Vite's existing
deprecation/dynamic-import warnings remain. Five pinned-base sections apply/hash/
reverse correctly;1088 targets and one selected Desktop test addition. No unchanged
broad source/mock sweep. [Adoption and limits](release-notes-v0.33.7.md).

Actual SSH-zero gates:60.056/60.058/60.123 seconds for before/final/reopened cohorts.
1148/1644/1119 bounded samples stay at most four Hermes processes; observer-inclusive
RSS maxima895795200/913227776/886013952 bytes, without continuous-peak/saving claims.
All owned processes/ports/CUA end; original profile/config baselines, denied folder
modes and313-entry bundle/strict signature restore. Owner app/data, other hosts,
ESTOP/pauses/timers unchanged. These final launches need no Reload; previous startup
paint cause remains unresolved. Canonical/standalone room member editing, actual
sync/dispatch, providers, daily-app/Linux/ai, spoken a11y and narrow windows remain
unverified. Required companion, tracked-copy release and exact secret gates apply.

# Native Local startup diagnostic — v0.33.6 follow-up

A fresh isolated Local launch's first Computer Use observation reported Not
connected; its saved JPEG showed CONNECTING. During subsequent window activation
and observation, the same process/build showed This device / scope-b / Connected
without Reload, Send or a new WebSocket. The first saved full AX tree was already
Connected; the initial AX result is an observed tool result, not a retained raw AX
file. This is a diagnostic observation, not a startup fix or reliability claim.

Sparse native main/ASGI traces show the renderer published its Local/scope-b
route about four seconds after app process birth. Its sole WebSocket was accepted,
and the first 36 RPCs received successful responses before eight seconds. The
same socket continued heartbeats and answered all 52 observed numbered RPCs;
no second handshake or authentication recovery occurred. These are instrumented
main/backend intervals, not a user-visible paint deadline. Window hide/show events
also occurred; renderer atom consumption and the actual foreground paint were not
traced. Visibility, paint scheduling and stale UI state remain hypotheses. The
previous Reload-dependent observations are not explained by this cohort.

Task-only observers exclude tokens and request/result bodies. IPC controls
preserve receiver, arguments, return/Promise identity, synchronous throws and
unrelated handlers; ASGI controls preserve message/result/exception identity.
Observation can change timing. No product code, renderer build, dependency, test
selection, patch or runtime version changed; unchanged broad suites were skipped.

The actual 60.146-second SSH-zero gate passes. Across 967 bounded samples, Hermes
count stays at most four and observer-inclusive RSS reaches 886,996,992 bytes,
without a continuous-peak or saving claim. All owned identities/ports end; original
config bytes/modes and the 313-entry trial bundle/signature restore. Both session
stores stay empty. No owner app/data, other host, ESTOP, pause or timer changed.
Required companion, tracked-copy release and secret gates apply. Cold startup
acceptance remains open; the next useful observation is renderer state and paint
across window visibility, rather than another speculative connection retry.

# v0.33.6 — Announce compact bot work correctly

The retained unchanged native before build names a compact bot Ready while its
real child runs. Final rebuilt native Local UI names it Working, retains Working
across the normal heartbeat and Refresh, then returns Ready after native child
completion and parent delivery. One Send/one child/four controlled loopback model
calls; no seeded activity. Independent DB snapshots and 26 actual default-to-sibling
reads correlate child and canonical parent IDs. Clicking the row reopens that
same parent; its preview remains separate from worker activity.

BotRow reuses its existing mood and translated Working label for an available
source; unavailable wins and other source labels remain. The shared accessible
name/name tooltip changes, without a new query, poll, state, API or lifecycle rule.
Real rendered regressions fail 2 with 12 controls before the fix; final nearest 46
across 4 files pass, including all-ended/stale, another eligible worker, exact-source
group activity, unavailable and canonical preview/open controls. Scoped official
health comparison: 0 blocking/0 advisory; lint/types/build pass. Inherited act and dynamic-
import warnings remain. Two scoped pinned-base sections apply/hash/reverse;
1086 targets and test selection retained. No unchanged broad source/mock sweep.

Final trial required one native Reload to recover Not connected before any Send
or session/model call. Cause unresolved; cold startup is not accepted. After that,
the same final process/build passes the status journey. Actual 60.083-second SSH-zero gate passes;
1,923 bounded samples stay within four Hermes processes and observer-inclusive
RSS reaches 1,217,249,280 bytes. Intermediate trial also
closed normally; its proof is kept distinct. All owned identities/ports/model
threads end and original config bytes/modes and the 313-entry bundle/signature restore. No owner
app/data, other host, ESTOP/pause/timer changes. Native AX names/screenshots checked;
spoken VoiceOver, independent tooltip interaction, providers, legacy/managed
subprocess, daily-app, remote/ai and Linux remain open. Required companion,
tracked-copy release and exact secret gates apply. [Release notes](release-notes-v0.33.6.md).

# Native compact Bots acceptance — v0.33.5 follow-up

Actual Local **Bots → Open chat** creates scope-b's native canonical Bot Chat.
One UI Send invokes native delegation and holds one child on a controlled
loopback model response. Select default, then **Bots → Manage team**: the compact
row shows the child task separately from the parent's message preview. After
the normal 60-second heartbeat and Refresh, the same child's activity reports
model waiting. Clicking the row reopens the original canonical parent ID, never
the child. Returning to Bots retains compact mode and the waiting observation.

Release the reply: the native child result, terminal timestamp, completed/delivered
delegation and parent result persist. Refresh keeps both rows and the new parent
preview, with no worker activity. Independent SessionDB snapshots prove one child,
lineage/profile, heartbeat and terminal state. Thirty-one default-to-sibling trace
reads match both worker and canonical parent IDs; default's session/message/
delegation tables remain empty. Exactly four controlled loopback model calls;
no lifecycle rows seeded. Fixture tokens are not provider usage or savings.

The actual 60.048-second SSH-zero gate passes. Across 1,697 bounded samples,
Hermes count stays at most four and observer-inclusive RSS reaches 1,204,846,592
bytes, without a continuous-peak or physical-memory claim. All owned processes,
model thread and loopback ports end; original config bytes/modes and the 313-entry
trial bundle with strict signature restore. No owner app/data, other host, ESTOP,
pause or timer changes. Existing v0.33.5 source, renderer, dependencies and test
selection are reused; no runtime release. One child only: parallel counts,
large-list/keyboard/narrow layouts, legacy backends, managed subprocesses,
providers, daily-app, remote/ai and Linux remain unverified. Required companion,
tracked-copy release and secret gates apply. [Journey](bot-activity.md#native-compact-rows-v0335-follow-up).

# Native Mac title-bar close recovery — v0.33.5 follow-up

With minimize-to-tray explicitly disabled, actual Local Settings changes default's
Memory Budget 3111→3456 while the isolated home refuses writes; scope-b remains
the new-chat selection. After autosave fails, clicking the native window close
button adds a new config permission failure (1→2) and flush failure (0→1).
The same native app/window retains draft 3456 and write-access guidance; the
primary file stays at 3111 and the other profile stays byte exact. Passive native
events record the close and its prevented state after dispatch, with no CLOSED
or application Quit event. The observer never changes the event.

Restore only the owned folder mode, then click close again without editing.
Native CLOSED and complete saved mapping 3456 are proved before guardian cleanup,
while the Mac app remains alive. This distinguishes destroyed-window acceptance
from hiding to tray or application Quit. All first-cohort writers and the guardian
end before fresh app/gateway identities reopen the same home, app data and build.
Settings reads 3456; config bytes match the post-close file, without a zero-write
claim. Unrelated mapping and the other profile are preserved. Both native session
stores stay empty; no Send/model/tool runs.

Both actual SSH-zero gates pass (60.141 / 60.084 seconds); 2,175 / 811 bounded
samples stay within four Hermes processes. Observer-inclusive RSS maxima are
898,891,776 / 883,294,208 bytes, without continuous-peak or saving claims. All
owned identities/ports end before original config bytes/modes, folder mode and
the 313-entry trial bundle with strict signature are restored. No owner app/data,
other host, ESTOP, pause or timer changes. No runtime, build, dependency, selection
or version change. Crash, disk-full, network failure, persistence before 550 ms,
daily-app, remote/ai and Linux acceptance remain open. Required companion,
tracked-copy release and secret gates apply. [Journey](settings-autosave.md#native-mac-title-bar-close-recovery-v0335-follow-up).

# Native Mac Settings Quit recovery — v0.33.5 follow-up

Actual Local Settings, applying to default with ambient scope-b, changes Memory
Budget 3111→3456 while the isolated home refuses writes. Native autosave fails;
CmdQ adds a new config permission failure (1→2) and a quit-flush failure (0→1).
The same app/window remains open with draft 3456 and write-access guidance, while
the primary file remains at 3111 and the other profile stays byte exact.

Restoring only the folder's write access and issuing another CmdQ, without a new
edit, saves 3456 and exits with native quit code 0. The process exit and native
quit event are recorded before guardian cleanup. Its identity-bound exit marker
can be armed only after the blocked-quit proof; a small admission self-check
passes one positive and eight negative controls. The diagnostic hook observes
events without preventing or changing them. Existing product queue/gates remain.

After every first-cohort writer/helper and guardian ends, fresh app/gateway
identities reopen the same home, app data and diagnostic build. Settings reads
3456 with config bytes matching the post-Quit file. Complete mapping comparisons
preserve unrelated values and the other profile. Both native session stores stay
empty; no Send, model request or terminal tool runs. Byte equality does not prove
zero writes. The second cohort ends through the guardian, separately from the
first cohort's accepted native Quit.

Both actual SSH-zero gates pass (60.029 / 60.127 seconds); 1,296 / 768 bounded
samples stay within four Hermes processes. Observer-inclusive RSS maxima are
915,914,752 / 877,035,520 bytes, without continuous-peak or saving claims. All
owned identities/ports end before original config bytes/modes, folder mode and
the 313-entry trial bundle with strict signature are restored. Finder capture
initially returned cgWindowNotFound; the console was verified unlocked and the
owned trial window worked. No owner app/data, other host, ESTOP, pause or timer
changed. No source patch, renderer build, test selection, dependency or version
change. Title-bar close, crash, disk-full, network failure, persistence before
550 ms, daily-app, remote/ai and Linux acceptance remain open. Required companion,
tracked-copy release and secret gates apply. [Journey](settings-autosave.md#native-mac-failed-quit-and-recovery-v0335-follow-up).

# Native Local sibling Bots acceptance — v0.33.5 follow-up

Actual UI Send in scope-b invokes native delegation and holds one child through
its normal heartbeat. After selecting default, Bots shows default Ready and
scope-b Working with the task and separate parent preview. Task-only passthrough
roster tracing records the actual default authority, readable scope-b sibling,
and shared `_sibling_sessions` returning the same child ID found independently
in scope-b's SessionDB. Twenty-two default-to-sibling reads match that ID; the
profile label alone is not routing evidence.

The child heartbeat advances from absent to a native timestamp. Refresh shows
its waiting description. Releasing the controlled reply produces the native
child result and terminal timestamp, durable completed/delivered delegation,
and parent result. Refresh then shows Ready / Working 0 with no active-worker
detail. Default's session/message/delegation tables remain empty throughout.
Exactly four loopback model replies control content/timing only. Fixture token
numbers are not provider usage. No lifecycle/activity rows were seeded.

The admitted cohort passes the actual 60.137-second SSH-zero gate and 1,608
bounded samples, with at most four Hermes processes and observer-inclusive RSS
1,183,531,008 bytes. An earlier task observer confused LocalBot with its authority;
it was closed before UI Send or the 60-second gate, corrected and tested before a
fresh cohort. Its 381 samples and 905,297,920-byte observer-inclusive RSS remain
failed-cohort evidence, not acceptance. UI evidence-helper binding corrections
preceded the single Send; no mutation or request was blindly repeated.

Both cohorts end all owned identities, model threads and loopback ports; original
config bytes/modes and the 313-entry trial bundle with strict signature restore.
No owner app/data, other host, ESTOP, pause or timer changed. The narrow observer
preserves original read return/exception identity and context cleanup; it adds no
query or authorization/lifecycle mutation. No source patch, renderer build, test
selection, dependency or version change. This proves native gateway-thread child
monitoring through canonical Local sibling reads; managed subprocesses, providers,
legacy, daily-app, remote/ai and Linux remain unverified. Resource values are
samples, not continuous peaks or savings. Required companion, tracked-copy
release and secret gates apply. [Journey](bot-activity.md#native-local-sibling-acceptance-v0335-follow-up).

# Native Local startup diagnostic — v0.33.5 follow-up

One earlier cold launch stayed on Connecting until native Reload. One fresh,
isolated Local launch with the same v0.33.5 renderer reached This device / scope-b /
Connected without Reload; the earlier stall did not reproduce. Sparse buffered
main-process markers showed the first descriptor claim ready in 1,801 ms and
WebSocket mint completion 18 ms later. These are main-process intervals, not
renderer receipt, publication or user-visible startup latency. No sanitized
renderer warning/error or renderer-gone marker was captured in this repeat.

Only the task diagnostic hook and compiled main had observation markers. IPC
observer controls preserve receiver, arguments, return/Promise identity,
synchronous throws and unrelated handlers; no Promise settlement observer was
added. Instrumentation can alter timing and suppress a race. The previous stall's
cause remains undetermined; this is neither a runtime fix nor a reliability claim.
No runtime, patch, test selection, dependency, renderer build or version change.

The actual 60.040-second SSH-zero gate passed. Across 759 bounded process samples,
Hermes count stayed at most four and observer-inclusive RSS reached 891,846,656
bytes, without a continuous-peak or saving claim. Both configs stayed byte exact,
both native session stores stayed empty, and no Send/model/tool ran. All owned
identities and the gateway port ended; original config bytes/modes and the
313-entry trial bundle with strict signature were verified restored. No owner
app/data, other host, ESTOP, pause or timer changed. Daily-app, remote/ai/Linux,
crash and repeated cold-start acceptance remain open. Required companion,
tracked-copy release and secret gates apply to this documentation follow-up.

# v0.33.5 — Keep list edits when closing Settings

Native Mac Local before/after: a focused comma-separated Environment Passthrough
draft adds a second entry and trailing comma. Before, Escape closes Settings but
disk and reopened UI retain only the original entry. After, the same flow saves
both entries and reopening reads them without another file change. All other
primary config values and the other profile's bytes are preserved. Both native
session stores remain empty; no Send, model request or terminal tool runs.

Regression uses the actual OverlayView and focused list control: Escape itself
must cause one parsed callback before teardown, without manually firing blur.
Genuine red: three failures/27 passes. Final nearest: 73 passes across six files,
including Enter, ordinary blur, raw drafts, unrelated unmounts and IME controls.
Scoped lint/types/build pass; inherited dynamic-import warning remains. Two
scoped pinned-base sections apply/hash/reverse correctly; 1086 targets and test
selection remain. No unchanged source/mock/transport sweep.

Both normal closures pass actual 60-second SSH-zero gates, sample at most four
Hermes processes and restore original config bytes/modes plus the 313-entry trial
bundle and strict signature. Observer-inclusive sampled RSS maxima are
958,857,216 / 1,006,927,872 bytes, without a saving or continuous-peak claim.
The after cohort needed one native Reload to leave Connecting before the list
flow. Its cause is unestablished; cold startup is not accepted. A capture failure
recovered with a fresh read and no repeated mutation. Native IME, crash, all-page,
daily-app and remote/ai/Linux acceptance remain open.
[Release notes and limits](release-notes-v0.33.5.md).

# Native Settings search and leaving the page — v0.33.4 follow-up

Actual Mac Local Settings search matched `compression.threshold`; Down/Enter
opened Context & compression and focused the highlighted threshold row. Tab
entered the input. ArrowUp saved 0.50→0.51 across navigation to Persistent memory
and back. Shift-Tab focused Auto-Compression; Space switched it off and Escape
closed Settings. Native disk comparisons show only those two primary values
changed, with all other values preserved and the other profile byte exact.
Settings reopen reads 0.51/off without another file change. Session stores stay
empty; no Send, inference or compression execution occurs.

One normal cohort passed the actual 60.022-second SSH-zero gate, sampled at most
four Hermes processes, and reached observer-inclusive RSS 969,981,952 bytes.
These are bounded samples, without a continuous-peak or memory-saving claim.
All owned identities and ports ended before original synthetic config bytes and
modes were restored. The original 313-entry trial bundle and strict signature
restored; no owner app/data, other host, ESTOP, pause or timer changed.

Native event-to-disk timing was not measured: this proves eventual durability
after leaving, not persistence before
the 550 ms deadline. Crash, all-page, daily-app and remote acceptance remain open.
No runtime, patch, test selection, dependency or build change; no version bump.
Required companion, tracked-copy release and secret gates apply to this follow-up.
[Journey and limits](settings-autosave.md#native-keyboard-and-leave-page-acceptance-v0334-follow-up).

# v0.33.4 — Nudge compression ratios precisely

Native Local before/after confirms one ArrowUp on Threshold 0.5 and Target 0.2
saves 1.5/1.2 before and 0.51/0.21 after. Protected Recent Messages still steps
20→21→20. Complete native config comparisons preserve other values and the other
profile's bytes; Settings reopen reads 0.51/0.21 without another write. Session
stores remain empty; no Send, model request or compression execution occurs.

Genuine red: 8 failures and 14 passes, after correcting a controlled-prop test
assertion. Final nearest selection: 65 passes; scoped lint/types/build pass, with
the inherited dynamic-import build warning. Real input stepUp/Down plus the change
callback cover ratios, zero, whole/absent values, integer/timeout and legacy
controls. Two scoped pinned-base apply/hash/reverse sections; 1086 targets and
the existing test selection remain. No unchanged source/mock/transport sweep.

Both normal native closures pass actual 60-second SSH-zero gates and sample at
most four Hermes processes. Observer-inclusive RSS maxima are 905,887,744 and
898,891,776 bytes, without a memory-saving claim. All owned identities/ports end;
config bytes/modes and the 313-entry bundle with strict signature restore.
No daily-app, remote/ai/Linux, compression-effectiveness or new range-validation
claim. [Release notes and limits](release-notes-v0.33.4.md).

# Native Local profile Settings persistence — v0.33.3 follow-up

Actual Mac UI edits save default Memory Budget from 3111 to 3333 while ambient
scope-b remains 4222, then save scope-b from 4222 to 4333 while default stays 3333.
Native file assertions compare complete config mappings against the originals
plus only the requested budget. The untouched profile stays byte exact after the
first edit. Profile switch and Settings close/reopen retain 3333.

All first-cohort processes and the gateway port end before new app/gateway
identities reuse the same home/profile paths and exact diagnostic build. The
second UI reads A=3333 and B=4333 without edits; both config hashes match the
pre-restart snapshots. Both native session stores remain empty. No Send, model
request or direct config seeding after launch supplies these results.

Both cohorts close normally and pass actual 60-second SSH-zero gates. Sampled
maxima: four Hermes each; observer-inclusive RSS 907,018,240 / 874,299,392 bytes.
These are bounded samples, without a continuous-peak, physical RAM or saving
claim. Original config bytes/modes and the original 313-entry trial bundle with
strict signature restore after every writer/watchdog ends. Retained private
evidence includes input-selection corrections and a rejected restart preparation;
neither is represented as a product regression or a clean first attempt.

Runtime, patch, test selection and build remain unchanged. Required companion,
release inventory and secret gates apply to this documentation follow-up.
See [journey and limits](settings-autosave.md#local-profile-persistence-acceptance-v0333-follow-up).

# v0.33.3 — Scope Settings config actions

Native Local before/after: ambient scope-b has budget4222, displayed default has
3111. Actual native Save exports4222/B before and3111/A after. A fresh rebuilt
launch shows default in the Reset dialog; Cancel returns to Settings. Configs
remain byte exact; session stores stay empty; no Send/model request occurs.

Nine added cases yield genuine red8/9passes, then nearest60pass. Exported contents,
confirmation/read scope changes, Cancel/noI/O, defaults read-origin and refused
Reset acknowledgement are covered. Lint/types/build pass; inherited dynamic-import
warning remains. Four-section pinned-base apply/hash/reverse passes,1086targets;
one existing upstream route-binding test joins the kit/explicit selection.

Baseline and rebuilt export/Reset cohorts pass actual60sSSH0/max4Hermes samples;
observer-inclusive RSS937672704/948797440/888340480B, no savings claim. Export cohort
watchdog expiry and inactive-read task-trial relaunch are retained as failed
closure diagnostics; exact relaunch identities are stopped. Fresh Reset cohort
closes normally. All owned identities/ports end and configs/modes/original313bundle/
strict signature restore. Native Reset write is intentionally skipped because
native defaults include timer policy. No daily-app/remote/ai/Linux or full Settings
acceptance claim. [Release notes and limits](release-notes-v0.33.3.md).

# v0.33.2 — Keep untouched settings visible after import

Native Local before/after uses two actual imports of the same memory-only file.
Before, omitted switches show off and Profile Budget stays empty after repeating
the import. After, those values stay on/1375 without reopening while Memory
Budget becomes 2901. Disk stores only the requested override and preserves all
original file keys. A following User Profile edit writes its intended additional
value; Settings reopen reads correct values. No Send/model request occurs.

Seven new cases fail before; final nearest selection passes 75 tests. Coverage
includes held/rejected saves, empty/null-mapping imports, explicit values, next
sparse edit and delayed read versus edit/unmount. Lint/types/build pass with
existing act/dynamic-import warnings. Two-section pinned-base apply/hash/reverse
passes; 1085 targets and test selection remain. No unchanged source/mock sweep.

Both actual 60-second gates show SSH0/max4 sampled Hermes; observer-inclusive
sampled RSS maxima 940,507,136/936,787,968 bytes, no savings claim. Both process
sets/ports end and config, modes, original 313-entry bundle and signature restore.
Native delayed-read/failure injection, full Settings, daily-app and ai/Linux
acceptance are not claimed. [Release notes and limits](release-notes-v0.33.2.md).

# v0.33.1 — Confirm config imports after saving

Native Local Import previously showed success while removal confirmation was
still cancellable. The rebuilt renderer waits for its existing native save
acknowledgement. Cancellation and a real test-home permission refusal show no
success; the latter displays actionable Autosave failed guidance and preserves
disk bytes. Restored access permits retry, saving both imported fields while
retaining unrelated keys. Settings reopen reads Memory Budget 2901 and original
unrelated values. The short success toast was captured on a repeated import.

Eight new cases fail before; the final nearest selection passes 68 tests.
Scoped lint, types and build pass with existing act/dynamic-import warnings.
Two changed sections pass pinned-base apply/hash/reverse; 1085 targets and test
selection remain. No unchanged source/mock sweep was repeated.

Final native run passed an actual 60-second SSH-zero gate, <=4 sampled Hermes
processes and 928,481,280 bytes observer-inclusive sampled RSS; no savings claim.
No Send/model request occurred. Processes, port, config/modes and original trial
bundle were closed/restored. Baseline guardian was absent on resume; independent
recorded-identity/port/config checks preceded its restoration. Native ai/Linux,
daily-app adoption and partial-import draft display remain open.
[Release notes and detailed limits](release-notes-v0.33.1.md).

# v0.33.0 — See parallel bot work

Fresh native Local before/after UI Send created two real delegated children in
one profile. Before, Bots showed one and briefly became Ready after stopping
newest A while B ran, recovering on B's heartbeat. After, both titles/count 2
appeared; Stop A left B/count 1/Working immediately after Refresh. Native 60s B
heartbeat retained B's title beside its waiting activity. Releasing B persisted
its reply/terminal state and the native batch delivery; final Refresh showed
Ready/Working 0/no worker detail and the parent's new preview. Late A reply did
not overwrite its terminal state. Five controlled loopback model requests per
run; no lifecycle records seeded. Model content/timing only were controlled.

Backend red7/20controls ->27 native assertion bodies pass using task-local
fixture adapters and real SessionDB, not canonical pytest/conftest (unavailable
in the managed environment). Initial duplicate-title bounds fixtures corrected
before valid red. UI red4/38controls ->42 nearest pass. Lint/types/build pass;
inherited row-test act and dynamic-import warnings remain. Twelve scoped
sections pass pinned-base apply/hash/reverse;1085targets/selection retained.
Optional <=20-worker metadata shares existing reads/cache and safe projections;
no new query/poll/write/dependency/schema migration or model request.

Both actual60s gates SSH0/max4sampledHermes/<4GiB.2272/1753samples,
observer-inclusive RSSmax1226244096/1228685312B, not continuous peaks or savings.
Both cohorts closed, gateway/model ports and threads ended, original313bundle/
hash/strict signature/config restored. No owner data/otherhost/stop mutation.
Native canonical full cards only; compact/legacy/sibling offline coverage,
large-list keyboard scroll/narrow/managed-process monitoring/adoption unproved.
[Release notes and detailed limits](release-notes-v0.33.0.md).

# v0.32.0 — Read and enlarge chat charts

Native Local before/after actual Send displayed the same controlled reply with
Markdown table, dense nine-category/two-series bar chart and Mermaid. The final
renderer exposes chart full view, Zoom in/Reset/Close/Escape and a Details table
with all full labels, duplicates, zero, negatives and unrounded parsed decimals.
Collapse removes the rows. Mermaid still opens/closes. Native Reload, New chat,
History and same-report reopen retained formats and values; stored messages
stayed exact after the native terminal-newline trim. One model request per
accepted run; no seeded lifecycle rows, no production model/usage-quality claim.
Native shell focus after Close/Escape is the composer; opener restoration is a
shared-component unit contract, not whole-app acceptance.

Original chart red5/7controls and shared focus red2/17controls preceded the fixes;
final19nearest pass across three files. Lint/types/build pass; inherited dynamic-
import warning remains. Four scoped sections pass apply/hash/reverse on the
pinned base;1085targets and existing test selection retained. No full source,
unchanged mock or broad native sweep repeated. Table DOM exists only while open;
no new fetch/poll/model request/backend/schema/prompt/context/dependency change.

Accepted before/final gates actual60sSSH0/max4sampledHermes/<4GiB.1183/1917samples,
observer-inclusiveRSSmax1186381824/1365884928B, not production savings. Preparatory
startup stopped before CUA/Send because two app-owned OS probe shells were counted
as workers. Exact executable/argv/stable-parent controls classify those utilities,
retain their RSS/descendants and still reject five actual Hermes; no bound raised.
All three cohorts closed, ports/modelthreads ended, original313bundle/hash/strict
signature/configs restored. Raw rejected run retained. No owner/otherhost/stop
mutation. Native wide bar workflow only; line/pie unit proof, other formats and
adoption limits in [release notes](release-notes-v0.32.0.md).

# v0.31.1 — Separate same-goal delegation cards

Fresh native Local homes ran two real delegated calls with the exact same goal
and distinct producer child IDs. Before the fix, stopping A made both cards show
Response stopped while B was still running; they stayed wrong after B completed.
The fixed renderer showed A Stopped / B Running, then A Stopped / B Done with B's
own output. Both runs refused A's late held reply and delivered both native
completion notifications. Only model content/timing were controlled on loopback;
no lifecycle rows or dispatch receipts were seeded. Each run used seven controlled
model requests and the same two-tool-call parent fixture cap, not a production
model or whole-autonomy check. Dispatch history without live state stays unknown.

Eleven regressions fail on the original matcher with 17 controls passing; the
fixed 28 nearest tests pass. Scoped lint, types and renderer build pass, with the
inherited dynamic-import warning. Three changed sections pass pinned-base
apply/hash/reverse; 1085 targets and the existing test selection remain. No new
backend API, schema, model request, polling timer or prompt/context change.

Both actual 60-second Local gates had SSH0 and at most four sampled Hermes processes.
Before/after observers collected 2742/2227 samples with RSS maxima of
1,224,884,224/1,295,679,488 bytes including the observer.
All owned identities ended, gateway/model ports closed and the 313-entry original
trial bundle, strict signature and exact baseline configs were restored. These
are sampled resource bounds, not continuous peaks or a production RAM comparison.
Distinct before/after terminal-card images and native DB snapshots stay private.
No unchanged native/mock suite or full source sweep was repeated. Daily-app
adoption, Linux/ai, legacy matching ambiguity and broader monitoring remain open.
[Release notes](release-notes-v0.31.1.md).

# v0.31.0 — Name and reopen Local groups

The native Local UI created a helper without introduction, then a two-member
canonical room. Blank names could not be saved; cancelling left the native room
and log unchanged. Saving a Thai/English name retained the current unsent message.
Back/Manage team reopened the same room. All first-run processes stopped and its
bundle/config were restored before a final build opened the SAME native home:
name, room ID, authority and member targets survived that process restart.

The first candidate exposed an old main-tab caption after Rename. A small SDK
caption update now preserves the existing workspace render callback and disposer,
without focus movement or reopening a closed pane. The final native UI changed
header and tab together and retained the unsent message. SQLite readback found
one room and exactly two rename events for two explicit different names, with
zero sessions/messages/driver tasks. This proves the controlled naming workflow,
not populated history, inference, membership edits or sibling/legacy monitoring.

Original missing-control red2 and caption-path red2 precede implementation. Final
63 nearest tests pass across workspace, reopen, capability and SDK contracts.
Types/build pass. Scoped lint adds no diagnostics; two pre-existing ref-cleanup
warnings and the build's inherited dynamic-import warning remain. Seven changed
sections pass pinned-base apply/hash/reverse, adding five upstream targets for
1085 total. The workspace regression joins the existing Desktop selection.

Both actual 60-second Local gates had SSH0 and <=4 sampled Hermes processes, under4GiB.
First/final2490/1574samples peaked at940228608/884637696B RSS including observer.
No owner app/home/data/other host/ESTOP/pause/timer was touched. Owned identities
ended, ports closed and313original bundle entries/signature/configs restored.
A second-run diagnostic-backup name collision was recovered without overwriting
its first verified backup. Raw state, images, failures and rollback stay private.
No full source sweep or unchanged native/mock suite was repeated.

# v0.30.2 — Live background reports without Reload

A fresh empty Local home created a real native parent and two delegated children
through UI Send. Composer Stop ended A before its held reply; B completed and
native parent delivery produced the streamed reply. The saved completion summary
appeared without any manual Reload or Refresh. Opening it showed A Interrupted,
B Completed, partial output and the report. A later native Reload/reopen retained
exactly one summary. No copied owner receipt or lifecycle/activity row was seeded;
only five loopback model requests and their timing were controlled. Stored model
content matched delivery and there was no profile_mismatch. The before reference
is the earlier native run with the same unmodified event handler.

Two new tests fail on the original handler. A further Stop regression fails on
the first candidate and passes after clearing adoption at interrupted settlement.
All 25 nearest tests pass across three files. They cover delegated/process reports
after streamed parent output, exactly one hydrate invocation, later refresh without
duplication, ordinary nonproducer turns adding zero reads, Stop, prior adoption
and stale execution fences. Scoped lint/types/build pass; the inherited dynamic-
import warning remains. Four scoped sections apply/hash/reverse against the pinned
base; unchanged source/mock suites were not repeated. This adds no model request.

A preparatory cohort was stopped before app CUA work for the Stop-latch fix and
final rebuild; it submitted no model request. Both cohorts passed their actual
60-second Local/SSH-zero gates within four sampled Hermes processes and 4 GiB.
The accepted cohort's 1283 samples peaked at 1,396,719,616 bytes RSS including the
observer. All owned identities ended, both ports closed, the original 313-entry
bundle/signature and exact baseline configs were restored. Values are sampled,
not physical-RAM or production-saving measurements.

Existing error/empty-final/Stop gates can still defer hydration; refresh follows
the parent reply's end. Process report behavior has focused unit proof, not a new
native shell-process acceptance. Original dispatch rows remain parked after
restoration. Daily-app adoption, Linux parity, whole native suite and production
efficiency remain open. See [release notes](release-notes-v0.30.2.md).

# v0.30.1 — Clean saved background reports

The v0.30.0 native two-child completion was copied through SQLite backup into a
fresh task-owned Local home. Its original content and outcome metadata matched
before launch. On the rebuilt native app, Chat history opened that saved report:
A/B outcome/name pairs, partial output and the successful child/parent result
remained visible; the terminal trace path and gateway notice disappeared. The
source database hash and copied row content/metadata stayed exact after viewing.
Message count and stored API accounting were unchanged; no new Send/model work
was submitted. The copied home's live resume was refused with profile_mismatch,
so this proves saved-history display, not cross-home resume or fresh delegation.

Three new regressions fail on the original parser; all ten nearest tests pass.
The cases cover batch/single/process framing, preserved outcomes/input records,
unwrapped legacy output, embedded notices, near matches and extra suffix text.
Existing upstream display whitespace normalization is retained. Scoped lint,
renderer types and build pass; the inherited dynamic-import warning remains.
Two changed patch sections apply/hash/reverse; unchanged source/mock checks were
not repeated. This is a renderer bug fix with no dependency/schema/backend change.

The actual 60-second Local gate had zero SSH attempts/executions. The cohort's
1120 samples saw at most four Hermes processes and 989,478,912 bytes RSS including
the observer. Owned identities ended, the gateway port closed, 313 original bundle
entries and strict signature were restored, and baseline config stayed exact.
Sampled resource values are not continuous peaks or production savings.
Daily-app adoption, Linux, the whole native suite and live pre-Reload summary
visibility remain open. See [release notes](release-notes-v0.30.1.md).

# v0.30.0 — Retained delegated task outcome details

Actual native Local UI Send started two delegated children. Composer Stop ended
A before its held response; B stayed live, emitted its native 60-second heartbeat
and completed independently. A late reply could not change its terminal result.
The parent received the native interrupted/completed batch. SQLite retained the
producer's paired outcome/name lines in existing display metadata, while the
model received the exact separate notification content. Native View → Reload,
open, collapse and reopen showed both pairs and the existing report. No lifecycle
or activity rows were seeded; only five loopback model replies and timing were
controlled. The earlier v0.29.5 restored-history screenshot is the before reference.

Three new UI/hydration cases fail before the change; all 14 nearest tests pass.
Two new native backend cases and updated existing assertions fail on the original
code; all three native test bodies pass via stdlib fixture adapters (not canonical
pytest/conftest). Coverage includes unsorted task indices, stored restoration,
unchanged model content, forced redaction before shortening, the 2000-character
card limit, literal task text, empty report and remount. Scoped lint, renderer
types and build pass; the unrelated dynamic-import warning remains. Seven changed
patch sections apply/hash/reverse; unchanged source and mock suites were not swept.

The fresh cohort passed its actual 60-second Local/SSH-zero gate, sampled at most
four Hermes processes and 1,355,825,152 bytes RSS including the observer. All owned
identities ended, both ports closed, 313 original bundle entries and strict
signature were restored, and exact baseline config was restored. Sampled RSS is
not a physical RAM or production-saving measurement. Daily-app adoption, Linux,
whole native suite, live pre-Reload summary visibility and legacy report trace
cleanup remain open. See [release notes](release-notes-v0.30.0.md).

# v0.29.5 — Stopped delegation cards

Native Local before/after evidence covers real UI Send, two native child agents,
composer Stop for A, B's continuing heartbeat, rejection of A's late response,
B's independent completion and native parent delivery. The repaired renderer
shows a visible and accessible Response stopped label with a neutral icon;
the earlier renderer labelled that interruption Error. Five controlled loopback
model calls per admitted cohort; no product lifecycle/activity rows were seeded.

Seven new cases include live/explicit settled results, empty/partial output,
late progress, and real failure/completion controls. With the corrected native
start→terminal fixture, five cases fail on the original code; the repaired two
files pass 17 tests. Scoped lint, renderer types and build pass. Four changed
patch sections apply/hash/reverse against the pinned base; unchanged source and
mock suites were not reswept. See [v0.29.5 notes](release-notes-v0.29.5.md) for the
initial cap-triggered diagnostic, build warning and precise history boundary.

# Native child file-read monitoring acceptance

On the v0.29.4 runtime, actual Local UI Send started a native delegated
child, which called `read_file` once on an isolated synthetic UTF-8 file. Its
native tool result, child lineage, step count, heartbeat and terminal timestamps
were read back from SQLite. Bots displayed Working / step 1/250 after the read,
then a native model-wait heartbeat and finally Ready / Working 0 with no active
worker detail. The parent received the native completion delivery. No lifecycle
or activity row was inserted by the diagnostic fixture.

Only model replies and timing were simulated on loopback, with five successful
responses. A preceding cohort was stopped after its preparation omitted the
model-port registration from the audit guard; the corrected fresh cohort reused
the previously proven guard. Native shell environment probes remained refused;
the native file-read path succeeded. This is not shell-tool acceptance. Both
cohorts closed and restored the task app/config; the accepted cohort passed its
actual 60-second Local/SSH-zero gate within the four-Hermes-process and 4 GiB
sampled resource limits. Raw screenshots and receipts remain outside the kit.

The brief running-file-read state, cancellation, sibling/legacy live behavior,
daily-app adoption and production model/efficiency results remain unverified.
No runtime patch, dependency or release version changed for this acceptance.

# v0.28.0 — Settings actions keep your place

The corrected renderer passed native Mac acceptance with isolated Local data:
a Thai/English draft seeded before the first Settings visit remained exact on
return, and after Export/Import chooser cancellation and Reset Cancel. Named
Actions and settled Cancel focus worked in wide and narrow windows; Return
reopened the menu and Escape dismissed it. Configuration bytes stayed exact.
Both this corrected cohort and its preceding diagnostic cohort passed a 60s
Local launch gate with zero SSH attempts/executions. Owned processes stopped,
gateway ports closed, DesktopSSH was zero, and the original trial bundle was
restored. Raw screenshots and receipts remain outside the release inventory.

The exact late-Local-mode route regression failed before correction and passed
afterward, with an explicit remote-owner isolation control. The fresh nearest
selection passed 58 tests across six files, including seven real Settings
Actions/confirmation integration cases. Scoped lint, renderer types and a
bounded renderer build passed. Nine changed patch sections apply/hash/reverse
against the pinned base; unchanged source targets and old mock suites were not
reswept. Companion tests and the release/secret gates are recorded separately.

This proves the scoped Settings flow on a real native app with synthetic data.
It does not prove daily-app adoption, a full native suite, completed import or
destructive reset, remote-host behavior, or production RAM/model savings.
See [v0.28.0 notes](release-notes-v0.28.0.md) for adoption and manual checks.

# v0.27.0 — Host toolchain probes follow on-demand startup

[Behavior and limits](release-notes-v0.27.0.md). Eight native unittest contracts
pass. Original code fails ten assertions/subtests across nonpositive/error policy,
six pre-admission exits and startup ordering. Positive and explicit-disable policy,
deterministic nonempty native first-turn facts, cache/prefix preservation and
remote/plugin omission controls pass. Eight fresh-process config bridge cases
pass; a separate positive policy executes five real checks once and reuses its
completed worker.

Four isolated Mac whole-canonical-gateway cases ran before/after/after/before.
READY, authority, control server and API were initialized by the real bootstrap,
with two real GatewayRunner turns per case and offline inference responses.
Startup checks change from five to zero; both arms total five after first use
and retain identical facts, config and static-prefix hashes, SOUL/AGENTS/Thai
context and second-turn cache reuse. Median idle RSS, 184.906 to 184.852 MiB,
is essentially unchanged; lifecycle peak, 242.852 to 255.281 MiB, is higher.
First-turn time is 861.61 to 1370.37 ms; second-turn time is 10.84 to 11.07 ms.
These timings include import/setup of inference interception. No RAM, speed or
model-usage saving is claimed. Median per-arm maximum sampled helper RSS is
24.492 to 23.641 MiB. Observer-inclusive peaks are 272.063 to 284.492 MiB;
maximum topology is two workload processes, three including the observer, with
20 ms target samples and zero surviving owned children. Shared-page accounting
and missed brief transients limit RSS evidence.

Seven audit negative controls and Python 3.14.9/pip stdout, status and module-origin
fidelity pass. Synthetic local profiles have no adapters or MCP; no inference
request, owner app/home/data/control change or other-host connection occurred.
This is task-local audit containment, not an OS sandbox. Canonical pytest, pinned
Ruff, the full native suite, UI Config/Bots/Chat, daily-app adoption and other
platforms remain unverified. Native contracts ran via stdlib unittest in the
managed runtime.

The kit companion suite runs 133 tests: 131 pass and two Linux-only cases skip.
A tracked-only disposable copy passes 245 release files/246 intended paths and
is removed with its private index. Actual reverse/base/reapply and strict
installed compatibility pass all 1,058 targets; 1,055 unrelated prior rows,
source bytes and patch sections, including P0, remain exact. The 13 inherited
whitespace diagnostics are unchanged and the new delta is clean. Exact directory
and all-history Gitleaks scans report no leaks; 225 commits were scanned. No
direct commit, push, publication or remote access occurred.

# v0.26.0 — Cold Local startup keeps saved remotes on demand

[Behavior and adoption limits](release-notes-v0.26.0.md). The accepted item is
passive cold-start transport initialization. Config/Bots/Chat Computer Use
walkthrough and screenshots remain unfinished; native window capture returned
`cgWindowNotFound` for the exact isolated app path. This is not screen acceptance,
daily-app adoption, a whole-goal completion or permission to connect another host.

Before the relay fix, an actual isolated source-built Mac app selected Local but
attempted SSH config resolution for a saved source. The execution guard refused
that attempt before SSH ran and stopped the owned tree. Passive Electron roster
paths also dialed saved SSH/URL/cloud sources in the actual-handler fixture.
After the shared readiness lookup and relay filters, a fresh final production
artifact ran **60.031 seconds** with the identical Local selection and three
reserved synthetic saved SSH/URL/cloud inputs: **zero SSH attempts and executions**,
no unexpected Node nonlocal-network attempts and zero surviving owned processes.
No actual remote host was used.

Passive SSH inventory borrows an existing, correctly owned session and never
opens/closes it. Current source, promise and borrowed-session ownership are
checked after awaits. A review found the post-profiles/install-id-await SSH
publication race; actual-handler red demonstrated stale profiles, then the
post-await fence passed all five interleavings for each roster/plugin consumer.
An identity-read failure still preserves a valid profile-list success.

Six meaningful relay cold-route failures precede the fix; a fresh original
relay run has those six failures and 44 passing controls. Final official UI
project: three files, 104 passing cases, including 50 relay lifecycle cases.
Seven scoped canonical Electron files pass 155 cases. Full UI/Electron types
and scoped ESLint pass. An isolated actual-main IPC fixture passes 43 cases;
these boundary-double controls do not execute SSH or inference. They cover
cached/seed routes, ready registry/legacy ownership, pending/rejected lookups,
retarget/removal/generation/session races, cold-target delivery and explicit
selection/Test. Older unmarked relay behavior remains covered. A transient-empty
inventory control caught our initial cache-sweep regression; cold-only early
cleanup preserves the previous normal sweep timing and last-good cache behavior.

The final app uses its actual dirty local source stamp and production product
identity. Its identity initializer was executed with runtime fallback refused;
retained native module layout, ASAR integrity and strict signature checks pass.
Only fresh renderer assets remain in the final task-owned stage. Task-local
Node TCP/DNS/UDP refusal, OS-contained CLI children, a dead loopback Chromium
proxy and a guarded native local gateway bound the test. Chromium's built-in
sandbox stays enabled. Configured HOME isolation is not a whole-app access
sandbox, and loaded renderer/healthy REST do not establish visual usability.

One accepted final cohort has **782.640625 MiB sampled workload peak RSS** and
**806.703125 MiB including the observer**. Maximum sampled Hermes count is four;
maximum observed workload OS count plus observer is five. Utilities and observer
remain included in RSS/count reporting. The requested sample period is 100 ms;
473 samples have a median gap of 132.848 ms and maximum gap of 138.853 ms. Shared
pages, missed short transients, resource-limiting launch flags and one isolated
case prevent normal-app/global RAM or speed conclusions. The failed before arm
ended early, so it is not an equal-work memory comparison; no RAM saving is claimed.

Rejected cohorts stay excluded: an earlier nested-sandbox renderer restart hit
five actual Hermes processes and was stopped. A later five-count sample was four
Hermes processes plus macOS `locale LC_CTYPE`; the revised utility exception
requires exact executable, argv and stable PID/birth, with conservative negative
self-checks. That sample remains rejected, and a fresh run supplied acceptance.
A successful pre-publication-fence cohort was also superseded after main changed.
The synthetic gateway configuration and restored registry match their saved
inputs; original trial configuration and three protected app hashes also match.
Recorded process identities are absent.

Ten native paths change: four prior targets and six existing upstream files
joining the 1,056-target kit. All 1,046 unrelated rows, bytes and patch sections
remain exact, including SSH transport/helper protections. Actual reverse/base/
reapply and all target hashes pass; strict installed verification passes. The
13 inherited cumulative whitespace diagnostics remain unchanged; incremental
changes are clean. A final user-guide wording edit leaves all runtime/program/
artifact hashes exact and needs only doc export/roundtrip verification.

Companion tests, intended-tracked-only release inventory, directory/history
secret scans, final advisor review and cleanup/preservation gate driver handoff.
No direct commit, push or publication is performed here.

# v0.25.0 — Bounded fresh backend probes

[Behavior, controlled native measurements and limits](release-notes-v0.25.0.md).
Old canonical red2children!=1 then correctedgreen. Four canonical files113pass,
ElectronTSC/scopedESLint pass. Existing import/version/installation callers share
one owner; fresh post-install checks execute independently of older pending work.
No resultcache/coalescing/pool/newprogram/newcoldretry. Admission and execution
budgets separate; actual close owns slots and one timeout retry. Unknown memory
expires; upstream catches still report unavailable runtime. Arbitrary wrapper
children/otherhelpers/bypasses/globalRAM remain outside direct-child cap.

Before product edits: real native program and six audit negatives pass, then
accepted external-observer two-import baseline (max4includingobserver/<4GiB/zero).
Prior observer summary referenced obsolete ticket grant field AFTERsuccessful
metrics/cleanup; retained/excluded terminal-failure result, corrected before
accepted baseline. One test-runner wrong Vitest path failed beforetests; corrected
before creditedred. Typecheck runner disabledincremental on composite config and
failed before sourcechecking; corrected to normal noEmit with ownedbuildinfo.
Lint type-import/spacing corrected, final canonical/types/lint pass. No productbug
or additional regression credit for these fixture/configuration corrections.

Fresh old/current/current/old: two real native import checks succeed each with
identical250ms postimportholds/config/nativeprogram/case/adapters. Direct helper
max2->1, two launches/zero survivors both. Median simultaneous combined Node+helper
peak194.078125->139.875MiB(-54.203125MiB/-27.9285%); fixed>=5%AND10MiB gatepasses.
Helper-only106.84375->53.375MiB; wholeharness includingobserver222.359375->
168.1640625MiB. Completionincludingholds782.4538955->1208.4737915ms slower~426ms.
Externalpsutil20ms requested/median37.3–45.5/max48.0msABBAgaps; sharedpages/transient
misses/allocator/fourcases/modeledhold limit attribution. Configured2 nativecontrol
keeps two-way overlap/two successes; actualhealthy memory allcandidatecases.
No app, real pressure, otherhost, inference, normalstartup/globalRAM/otherOSclaim.

A targeted close-ownership review found repeated async error events could throw
after the first. New regression redcleanup-refused->green with retained listener,
first error preserved. Final native paired preflights/ABBA/config2 rerun tied to
final module hashes; earlier successful cohort retained/excluded from figures.

Final1050targets/fivepaths(3prior2new)/1045unrelatedpriorrows-bytes-patchsections
exact; main onlyimport+launchconfigcall and relatedSSHcode unchanged. Required
roundtrip/strictinstalled/companion/release/scans/advisor/protectedstate/process
cleanup gate handoff. No owner controls or state are changed.

# v0.24.0 — Busy ticket helpers share bounded admission

[Behavior and measured native Mac evidence](release-notes-v0.24.0.md).
Two guards keep busy cached reuse in the existing shared 256-job queue and leave
its head deadline/timer intact while that helper is busy. One unanswered frame
per helper at fixed configuration; live two-to-one retirement remains unchanged.
Old canonical red: two frames != one; same regression green. Three canonical
Vitest files pass 64 cases, Electron types and scoped ESLint pass. No full app or
canonical Mac hard-coded-/tmp helper fixture acceptance is claimed.

Corrected native fresh old/current/current/old: 64 equal fresh grants each,
submitted unanswered64 ->1 with63queued, one native RPC in progress both arms,
one helper/zero survivors. Whole-Node-lifetime median combined peak120.46875 ->
120.8203125MiB, mint duration including >=100ms hold175.935 ->178.750ms.
No RAM saving or speed claim. External psutil samples requested20ms/median35.5–
36.1ms/max40.5ms, simultaneous Node/helper sums exclude observer, include startup
and idle retirement. Three known processes including observer/<4GiB sampled.
Shared RSS, transient misses, four cases and synthetic grants limit attribution.
Prior synchronous Node/ps sampler contaminated timing/RSS and caused an overload
deadline failure; that cohort is retained privately and excluded from numbers.
A corrected preflight first used strip-only Node against a parameter property;
it exited before any helper. Node22 transform mode matches prior runtime. No
product bug or additional regression credit for these fixture corrections.

Separate native300overload: old300fresh/current257fresh+43queue-full; subsequent
fresh recovery grant both arms. Not equal-work/RAM comparison. All cases preserve
config/program hashes and close helpers/socket. Actual healthy memory observations,
owned Unix only, six audit negatives/not OS containment. No app/owner mutation,
other host/SSH/inference/physical pressure/other-OS/production acceptance.
Three prior targets change;1048total/1045unrelatedrows-bytes-sections/P0 exact.
Required roundtrip, strict-installed, companion, release, scans, advisor and
preservation/process cleanup gate driver handoff.

# v0.23.0 — Source-check Python waits for available memory

[User-visible behavior and controlled native evidence](release-notes-v0.23.0.md).
Old canonical regression launched one child below the floor instead of zero;
updated queue tests pass 27 cases. Canonical queue/source-channel/legacy selection
runs 31 cases: 30 pass, one native Windows-only skip. Electron types and scoped
ESLint pass. A first private-runner configuration blocked the fixture's LOCAL Git
origin; permitting only the file Git protocol fixed that fixture run, while its
publication HTTP remained redirected to loopback. No product repair or extra
regression credit is attributed to this harness issue.

One outstanding polling timer belongs only to the active admission; its delay is
100 ms or the remaining budget, whichever is shorter. The monotonic
360000 ms budget begins after its predecessor settles, covering observation,
memory waiting and execution. Safe integer >=512 MiB admits; unknown/invalid/
missing/throwing observations wait. Before/after observer checks reject expiry;
remaining timeout is floored and must be >=1 ms before synchronous execute.
Existing queue identity, force/channel barriers, errors, parsing and count release
remain. Pending operations own no poller; success and expiry leave no timer.

Native preflights include actual healthy availability and both overlap arms.
Final fresh old/current/current/old uses the exact generated installation launcher,
actual CLI import and cached native source check/Git. Only availability is modeled
low while a native CLI process lives. A shared audit phase gate blocks Git Popen
until Node confirms background close, preventing a fifth known process. Initial
config/cache bytes, final bytes, output and native program/adapter hashes match.
Source-check overlap yes -> no; median combined peak229.6015625 ->175.2109375MiB
(-54.390625MiB/-23.6891%), preselected >=5% AND >=10MiB threshold passes.
Completion including the gate1712.235562 ->1975.051979ms; process count including
Node3 ->3, zero survivors. No production latency or real pressure claim.

Recursive20ms samples, shared pages, loader/allocator noise, four cases, transient
children, modeled observation and phase gate limit these results. Two Python+
Node OR source-check Python+Git+Node plus one excluded ps observer <=4 measured
known processes; outer orchestration excluded, total sampled RSS including it
<4GiB. Native8 audit negatives/SQLite positive/base audit AST/generated program
exact pass, not OS containment. No app launch, owner state/control mutation,
other machine, inference, actual update/apply or other-OS acceptance.
Three prior kit targets change plus two upstream tests;1048targets/1043unrelated
prior rows/bytes/patchsections/P0 remain exact. Mandatory companion, release,
roundtrip, scans, advisor, preservation and process cleanup gate handoff.

# v0.22.0 — Runtime lookups share Desktop helper admission

[User-visible behavior and controlled native Mac measurements](release-notes-v0.22.0.md).
An old-code reset regression spawned two lookup children before the old child
closed; the updated module waits. Eighteen actual-TypeScript assert contracts,
46 canonical Vitest cases, full Electron type checking and scoped ESLint pass.
Native metadata and native ticket-client functions execute under task-local audit
checks; six ticket-guard and eight metadata-guard negatives pass, not OS containment.

Four fresh Node cases old/current/current/old reproduce a slow lookup with a
finite file gate after native CLI import. The same native ticket program reaches
an owned Unix socket returning a synthetic fresh grant. Healthy host memory is
observed directly. Lookup overlap is 2 → 1; peak runtime processes including Node
3 → 2. Median combined peak is 170.296875 → 131.640625 MiB (22.7% lower), request
completion 841.325 → 911.354 ms. The preselected >=5% and >=10 MiB gate passes.
All cases reject the stale request, mint one fresh ticket, preserve config bytes
and leave zero helpers. Recursive 20 ms RSS sampling includes Node/children and
excludes one ps observer; at most four known processes and <4 GiB extra RSS.
File gates, synthetic grant, shared RSS, loader/allocator noise, sampling gaps and
four cases limit the result; no general app or normal-launch saving is claimed.

Default capacity one/configurable two and 256 waiting jobs now cover runtime
lookups and ticket helpers together. Lookup queue waiting consumes its existing
30-second budget; ticket requests retain ten seconds. Active failures settle
without freeing a slot before close. Generation travels through delayed backend
selection, and memory observers are followed by queue/generation/deadline/capacity
rechecks. Existing ticket program/argv, interpreter validation and profile scope
are preserved. Backend installation/selection and other entrypoints remain outside
the bound. No app, real gateway owner, other OS or provider acceptance is claimed.
Five existing native files change: three prior targets and two upstream tests
newly included in the 1,046-path kit. All 1,041 unrelated prior targets and P0 are exact.
Companion, inventory, patch roundtrip, scans, preservation and advisor review gate
handoff; owner controls remain untouched and no other machine was contacted.

# v0.21.0 — One native idle-cleanup job per runner

[User-visible behavior and controlled Mac measurements](release-notes-v0.21.0.md).
The meaningful old regression saw zero agents cached instead of three while
one callback was blocked. Eleven standalone native unittest cases pass after
implementation, including real shutdown finalization, native executor quiesce,
DB-close refusal while a writer lives, and SQLite close/reopen history readback.
An explicit two-second test drain budget distinguishes the blocked writer from
idle pool threads; a preliminary zero-budget probe counted both and was corrected.

The four fresh old/current/current/old component cases use real native methods
and four synthetic persisted sessions with fixed 200 ms provider callbacks.
Concurrent idle-sweep commits are **4 → 1**, peak sampled threads including main
**5 → 2**. Median cleanup **213.076 → 846.627 ms**; peak RSS **117.726563 /
117.593750 MiB**, idle **117.164063 / 117.140625 MiB**. No RSS saving or speed
claim. Initial configs and native SQLite history readback match; configs remain
byte-exact, all native processes stop. External recursive sampling is 20 ms,
one native child plus one excluded observer, under 4 GiB extra RSS. Synthetic
callbacks, sampling gaps, allocator noise and four cases limit the result.

The worker claims one current eligible entry under the cache lock; waiting agents
remain cached for native shutdown or later use. A token fences repeated sweeps,
queued cancellation, immediate completion, partial submission failure and stale
callbacks. Lock-order inspection finds executor acquisition beneath cache locking;
executor shutdown releases its lock before stopping/joining workers. Existing
provider commit/soft-release/error policy and per-owner profile scope remain.
No new setting, pool, timer, trim or model call is added. The shared pool retains
idle threads until normal shutdown. Other eviction paths are not globally capped.

Two existing pytest test seams await completion and drain their executor; they
are not claimed run with pytest. The selected runtime lacks pytest/Ruff; no
provisioning, canonical native suite/lint, installed app, full gateway workload,
real provider, other-host or other-OS acceptance is claimed. Mandatory companion,
release, native export/roundtrip, preservation, advisor and scans gate handoff.

# v0.20.0 — Optional dashboard warmup in the canonical gateway

[User-visible behavior, configuration and measured tradeoff](release-notes-v0.20.0.md).
The new `gateway.dashboard_warmup` key defaults to true. Its canonical config
field, serialization and native loader bridge feed only the existing background
warmup scheduling seam. Missing/invalid values keep warmup enabled; literal
opt-out preserves the existing lazy first-request mount. Auth-required or
already-loaded dashboard preload, session transport and lifecycle are unchanged.

Before implementation, the explicit-false scheduling test failed because a
warmup task was created; the default control passed. Actual canonical boot then
caught an omitted config-loader bridge, reproduced by the native CLI-to-loader
test and fixed in the shared bridge. Post-export **eight native unittest cases
pass**, 0.456 seconds. They cover default/disabled scheduling, invalid values,
serialization, raw unrelated settings, actual native CLI/load path, lazy HTTP
mount/singleflight, auth-required preload selection and close-during-lifespan
cleanup. The auth selection test uses a real listener with mocked mount, not a
public-auth provider. Existing Uvicorn/websockets deprecation warnings remain
visible. No existing native pytest test was altered; pytest/Ruff are unavailable,
so no canonical native suite/lint pass is claimed.

Four fresh canonical `start_gateway` lifetimes ran in ABBA order, including real
ownership, authority/control/API, runner, cron/housekeeping, READY and awaited
native shutdown. Both arms disabled turn warmup and configured no MCP servers or
messaging adapters. A separate completed native CLI process applied the single
key before each backend started. Initial config backups matched; only the
effective boolean differed and all config bytes stayed exact during each run.
Idle was fixed at three seconds after READY, explicitly awaiting default warmup.
Opt-out kept the dashboard module unloaded until first request. No legacy TUI
server was loaded.

Default idle RSS **213.578125 / 213.890625 MiB**, opt-out **183.859375 /
183.703125 MiB**; medians **213.734375 → 183.781250 MiB**, lower by
**29.953125 MiB / 14.014%**, passing the frozen 5% and 10 MiB gate. Median first
real dashboard health request **16.753 → 473.287 ms**; second **2.203 → 1.117 ms**.
The series does not establish a second-request speed gain. Median lifetime peak
**226.695313 / 226.679688 MiB** is essentially unchanged. Import cost moves later.
Health responses returned 200 with equal payloads; route signatures matched,
protected requests returned 401 in every case, native runner/authority bindings
and withheld-token policy remained. All lifetimes stopped with zero descendants.

Outside recursive 20 ms samples observed one native process per lifetime, plus
one excluded observer; total extra RAM stayed below 4 GiB. RSS includes shared
pages and can miss brief peaks. This is synthetic canonical local startup and
dashboard API evidence, not app UX, messaging/model/public-auth/other-platform
acceptance or a general production saving. Preliminary config-in-process and
missing-bridge runs are retained privately, superseded rather than repeats.

The kit has **1,042 targets**: two prior targets change and four join it. All
1,036 unrelated prior rows/source bytes/patch sections, including P0 Desktop
fan-out protection, remain exact. Actual reverse/base/reapply/all-after-hashes,
strict installed compatibility, companion suite, release inventory and secret
scan results gate the driver handoff. The existing preset remains unchanged;
application and proof limits are documented in the release notes.

Companion **133 run, 131 pass, two Linux-only skips**, 4.425 seconds. The
tracked-only disposable release copy passes **238 files / 239 intended paths**;
its copy and private index are removed, the real index unchanged. Exact
Gitleaks directory/history scans both exit 0 with no leaks, 218 history commits.
Eight audit negative controls pass; protected app/config backups and all source
hashes match, ten recorded PID/birth identities are absent and the owned-runtime
scan is empty. Final report/preservation scans gate the driver signal.

# v0.19.0 — Native gateway memory command and Mac current RSS

[Usage, matched measurements and limitations](release-notes-v0.19.0.md).
The native parser and command map invoke one existing private `memory-stats`
query. A platform-owned lazy psutil fallback fills unknown current RSS only;
existing readings, anonymous-RSS semantics and trim/admission behavior remain.
No runtime monitor, model tool, dependency, allocation request or lifecycle
change is introduced.

Before implementation, a native fallback assertion failed (`None` versus 123
KiB), while the existing parser rejected `gateway memory` with code 2. The
existing-RSS control passed. Post-export **10 native unittest cases pass** in
0.010 seconds, covering selected-home ContextVar dispatch, one-query behavior,
unknown/zero RSS, malformed response refusal, current rather than cached/peak
readings, expected failures and forbidden trim/GC/database effects. Seven audit
negative controls pass; actual AF_UNIX traffic supplies the positive control.
This is a Python audit harness, not OS containment. Selected native runtime has
psutil but no pytest/Ruff; canonical native suite/lint were not provisioned.

One final native control-server pair used identical initial config bytes and the
same actual native CLI entry point against the exact old/current diagnostic
module. RSS changed from unknown to **35,328 / 35,344 KiB** on its two queries;
PID matched the server and an outside observer agreed within 2 MiB. The new
server loaded psutil only on demand. Before-query RSS was 32.4375 / 32.265625
MiB old/current; after the second query 33.203125 / 34.53125 MiB. These are
observation/import costs, not RAM savings. Complete CLI timings were
695.198/678.870 ms old and 699.500/689.429 ms current, including shared startup.
No speed conclusion follows from one pair. A preliminary unequal-client probe
is superseded, not counted as an independent repeat.

Actual CLI exits **0/1/2** pass, including valid unknown RSS, missing server and
invalid arguments. The socket is removed on shutdown; config bytes stay exact,
SQLite high-water is not reset, allocations absent, and no children survive.
Twenty-millisecond recursive sampling observed at most two native children plus
one outside observer, peak summed child RSS 130.484375 MiB, under 4 GiB total.
RSS includes shared pages; brief peaks can be missed. No full gateway, connected
adapter, installed-app, production workload or other-platform proof is claimed.
No model endpoint, other machine or owner control/state was touched.

The cumulative patch pins **1,038 targets**: one prior diagnostic target changes
and eight targets join it. All 1,029 unrelated prior rows/source bytes/patch
sections, including Desktop P0 protection, remain exact. Actual reverse/base
hashes/reapply/all-after-hashes and strict installed compatibility pass. The same
13 inherited whitespace diagnostics remain; the new delta/root are clean.
Companion suite: **133 run, 131 pass, two Linux-only skips**, 4.402 seconds.
The tracked-only disposable release copy passes **237 files / 238 intended
paths**, with private index/copy removed and the real index unchanged. Exact
Gitleaks directory/history scans both exit 0, no leaks, 217 history commits;
final report/preservation rescans gate the driver handoff.

# v0.18.0 — Optional on-demand gateway preset

[Application, native consumer contracts and measured tradeoff](on-demand-gateway.md).
The companion packages three existing native settings; it introduces no runtime
code, mode or default. The native patch/manifest are byte-exact to v0.17.0 and all
1,030 source hashes, including P0 SSH protection, remain unchanged. Actual native
reverse/base/reapply hashes and strict installed compatibility pass.

The pre-preset no-preload control fails because existing default warmup schedules
work. This is a before-preset behavior control, not an old-code bug or new runtime
fix. The executable native fixture passes **five tests**, 2.965 seconds: per-key
parser/readback and unrelated settings, unselected profile isolation, actual MCP
loader/discovery consumers, real warmup start/await and actual first-turn assembly.
The fixture re-enters the native boot bridge between temporary homes because
unittest reuses the module import; matched measurements use fresh processes and
the actual module-boot bridge. Native queued logging cleanup follows its existing
test pattern before removing a home. No logging-error or ResourceWarning in the
accepted fixture run. Existing MCP selection: **25 passed**, 3.040 seconds.

One fresh paired initialized-runner case starts from identical synthetic config
backups, then uses canonical parser writes for only the three preset keys. An
ambient warmup777 is overridden at actual boot to baseline20/preset0. Both sides
construct real GatewayRunner instances and invoke actual warmup start/await;
the preset leaves run_agent/model_tools unloaded at the idle checkpoint. RSS
**178.234375 → 144.000 MiB**, 19.2075% lower; one native process/zero children both.
First turn **528.332 → 1165.846 ms**, including test-interception class import
inside that timed first-use window. Lifecycle peak **222.578125 → 220.515625 MiB**;
similar, not a general peak-saving result. The actual gateway turn path constructs
the agent and assembles SOUL, AGENTS, Thai input and byte-equivalent canonical
wire tool definitions; only inference methods return a synthetic completion.
One boundary call on each side, no provider request, config bytes unchanged during
measurement, canonical shutdown with no children. Initial probes and fixture
corrections are recorded privately, not credited as product bugs or repeat evidence.

Twenty-millisecond recursive samples include the native runner and its sampling
allocations, exclude one outer orchestrator and observe at most one native process
in the pair. Known topology stays within four processes/<4 GiB. Shared pages,
brief peaks, one pair, synthetic context and disabled environment probing limit
generalization. Private audit guards deny network, unapproved subprocesses and
owner-path access; they are not OS containment. Full startup/adapters/gateway idle,
app adoption, other platforms and model usage remain unverified. Canonical native
pytest and pinned Ruff are absent; no dependency provisioning was attempted.

Companion: **133 run, 131 passed, two Linux-only skips**, 4.402 seconds. Release
inventory/disposable-copy verification, exact directory/history secret scans,
advisor review, source/app/config preservation and zero-SSH checks gate handoff.

# v0.17.0 — Profile MCP idle defaults

[Plain-language behavior and native Mac component evidence](release-notes-v0.17.0.md).
Two production targets, the existing unittest and two native guides change.
`mcp.idle_timeout_seconds` defaults to disabled; positive finite seconds supply
the existing native timeout only to stdio/no-events entries missing both top
and nested lifecycle idle keys, after portable merge. Boolean/nonfinite/invalid/
overflow/disabled values leave healthy entries intact. Existing lazy behavior,
explicit overrides, security and profile boundaries stay intact. No new module,
dependency, tool, observer process, lifecycle or reconnect implementation.

Seven new test methods produce twelve clean old-code failing subcases, then
**25 native unittest cases pass**. Existing cache and concurrent-first-use cases
remain in that selection. Actual canonical config parser set/get readback
proves the default and positive inheritance while unrelated raw synthetic model,
provider, credential-pool, fallback and server settings remain exact. Private
audit negatives: five pass. Selected runtime lacks canonical pytest and pinned
Ruff; no download or full-native-suite pass is claimed.

Fresh native preflight used the actual loader, SDK, registry, supervisor and
stdio echo peer: three processes, 180.844 MiB summed RSS, no shutdown survivors.
Final matched pair uses the previous versus patched loader with identical initial
config bytes and matching caches seeded separately. At 5.5 seconds idle, summed
RSS **184.8125 → 139.21875 MiB**, 24.7% lower; recursive children **2 → 0**, including
supervisor. Whole-case peak **184.875 → 185.09375 MiB**, essentially unchanged;
maximum three sampled native processes on both sides. Next echo **2.624 →
109.128 ms**. Patched children disappear 70.44 ms after the observed deadline.
Fresh peer counter resets, schema stays registered, a subsequent six-second RPC
finishes on that same peer beyond the five-second limit, and retirement resumes.
Both runs preserve config bytes and end with zero children. Initial paired probe
included restart inside the delayed RPC; replaced by the final separated-latency
pair above, not counted as an independent repeated benchmark.

Twenty-millisecond recursive samples include native parent/peer/supervisor and
exclude one outer orchestration process. Known overall topology <=4, <4 GiB.
Shared RSS pages, observer allocations and sampling limits apply. Python audit
checks are not OS containment. No app/other-machine/SSH/model/network acceptance,
physical-pressure, Linux/Windows execution or whole-gateway saving is claimed.

Companion: **133 run, 131 passed, two Linux-only skips**. Export remains **1,030
targets**; all 1,025 unrelated manifest rows/source bytes/patch sections exact,
including P0. Actual reverse/base/reapply and strict installed compatibility
pass. Thirteen inherited cumulative whitespace diagnostics remain unchanged;
new native delta is clean. Release-copy, inventory and exact directory/history
scans are required before the driver signal. Daily app and owner state untouched.

# v0.16.0 — Ticket-helper memory admission

[Plain-language behavior and native Mac controlled-overlap evidence](release-notes-v0.16.0.md).
One existing production scheduler, its existing admission test and native Desktop
guide change. New bridges with capacity require a safe integer memory snapshot
at least 512 MiB; low/unknown, missing API, invalid value or exception waits within
the original ten-second mint budget. One 100 ms scheduler poll runs only while
memory blocks an eligible head. Existing bridges remain reusable; FIFO admissions,
256 waiting requests, real-close reservations, idle and reset remain intact.
Head identity, generation and deadline are rechecked after observation.

Thirteen clean old-code failures prove pressure/invalid/missing/error waiting,
reset and replacement safety, clock expiry and memory-to-capacity transition.
Fourteen new memory cases reuse the existing process fixture; the old cap/idle
cases use a deterministic healthy observation. Post-export selection: **43 passed,
one Windows-only skip**, seven files, 1.31 seconds, exit 0. Existing real client
cases retain profile/owner/protocol/purpose/control-home/cwd-shadow, bundled and
runtime lookup coverage. The private AF_UNIX temp base is relocated into an owned
short root; product behavior is not changed for test permissions.

One native preflight before implementation used one helper, two fresh grants,
actual healthy observation and two runtime processes at 71.984375 MiB total RSS.
Final recursive-ancestry paired case runs the same real native CLI import and
native ticket program; only memory observation is modeled. Peak summed RSS
including Node controller: **157.15625 → 126.28125 MiB**, 19.6% lower. Python
workload-only peak: 90.359375 → 59.6875 MiB. Runtime processes 3 → 2; overlap true →
false. Ticket latency 136.219 → 1649.366 ms; whole-case completion 1.846 → 2.039 seconds. Helpers
retire to zero on both sides. Separate actual healthy Node observation admits
normally, retains overlap and returns the same native grant. Full descendant
sampling includes the controller; one ps observer is excluded from RSS/counts,
with known maximum four processes including it, below 4 GiB. Same config bytes and
native program; runtime stopped after every run. Six audit negative controls and
real AF_UNIX positive pass, not full OS containment.

One pair, 20 ms target samples, shared RSS pages, finite samples and controller sampling
allocation overhead; no physical-pressure or general workload saving claim.
Initial known-PID-only pair was replaced by recursive-ancestry acceptance, not
counted as independent repeated measurements. Old measurements remain private.
The actual Electron app was not launched; package versions/typings alone are
not Electron-runtime proof. No other-machine/ai connection, real gateway/worker,
provider/model call or owner state/control mutation was used for acceptance.
Assigned buffers/runtime metadata lookup and broader gateway/MCP idle work stay open.

Initial implementation had an invalid optional variable declaration; it was
corrected before behavior acceptance. One progress-report command used the test
cwd instead of the kit root and failed read-only; absolute roots corrected it.
Neither is credited as an extra product fix or a meaningful old-code red.
Whole-Electron TypeScript no-emit, two-file ESLint and all three development
bundles pass, without launching or packaging an app. Cumulative target count stays
**1,030**: three existing targets change. All 1,027 unrelated prior rows/source
bytes/patch sections stay exact, including P0 SSH. Actual reverse/base/reapply,
every target hash and strict installed compatibility pass. Incremental/root
whitespace clean; the same 13 inherited cumulative diagnostics remain.

Companion verification: **133 run, 131 passed, two Linux-only skips**, 4.577
seconds, exit 0, with task TMPDIR and bytecode disabled. Release inventory
verification passes **231 files / 232 intended tracked paths** on a disposable
copy; private index and copy are removed and real index stays unchanged. Final
advisor, exact secret scans, protected hashes, cleanup and zero-SSH gate handoff.

Final advisor finds no concrete blocker using supplied code/evidence. Original
app/config and all 1,030 source hashes match; 20 recorded PID/birthtime identities
have no survivor. Cleanup removes nine exact owned dependency/build/cache/export/
short-fixture paths (1,231,024,079 logical bytes, no physical-space saving claim).
Existing source/app/runtime/borrowed objects, backups, matched inputs and receipts
remain. Exact first directory/history secret scans exit 0 with no leaks across
214 commits. Final report/scans/preservation/zero-SSH still precede driver signal.

# v0.15.0 — On-demand Desktop ticket helpers

[Plain-language settings, native Mac measurements and limits](release-notes-v0.15.0.md).
Three runtime paths, one new behavior test and the native Desktop guide change.
Existing launch-config parsing/main wiring feeds one module-owned admission
queue and lifecycle. Default helper cap 1, configurable 1–2; idle 5000 ms, configurable 100–30000 ms.
Starting and retiring helpers consume slots until actual close. Busy helpers
are never evicted; queued admissions are FIFO, bounded to 256 requests, while existing bridges
may multiplex. One monotonic ten-second mint budget includes queue/retirement/
spawn/exchange. Reset cancels waiting work and prevents stale startup. Native
helper program/client and exact command/cwd/full-env/profile identity remain intact.

Three meaningful old-source reds prove uncapped helpers, wrong idle lifetime and
missing admission ordering. Final native selection: **29 passed, one Windows-only
skip**, seven files, 1.27 seconds, exit 0. New cases cover actual-close/error barriers,
busy/no-eviction, same-key fresh grants, parser-to-policy propagation, safe defaults,
queue overflow/expiry, generation/reset, synchronous-spawn rollback, reentrant
reservation, input snapshots and oversized frames. Review found two new deadline
gaps: deterministic three-case red/green proof now covers an unused fresh child
when expiry crosses either startup boundary, and an overdue reply arriving before
its timer callback. Constructor idle retirement and per-waiter absolute deadline
checks close those gaps. A process mock observes the actual production scheduler;
there are no test-only production APIs.

Existing real native tests pass profile/owner/protocol/purpose/control-home and
cwd-shadow checks plus bundled/runtime lookup contracts. An initial driver used
Vitest --root from the wrong process cwd: its bundled fixture linked the wrong
source and failed. Old source reproduces the failure under that same bad cwd;
corrected-cwd baseline **14 passed, one Windows-only skip** and patched selection pass.
Resolved native module __file__ paths point inside the trial source. Only the
AF_UNIX fixture temp base is relocated into an owned short root; product sources
are not changed to accommodate the fixture. Initial whole-matrix red also had
cleanup rejections and missing new setter; only the clean focused three reds
are credited as original-feature regressions. A config-import startup, type-import,
composite TypeScript flag and one documentation read-cwd error were harness
corrections. No additional product fix is credited for them.

Native one-helper preflight returns two fresh grants before implementation.
Final same-case three-profile pair runs unchanged native Python 3.14.9 ticket code
against private synthetic AF_UNIX controls in the Node caller process. Sampled
request-window summed RSS including caller: **134.328125 → 72.15625 MiB**, 46.3% lower;
maximum sampled processes 4 → 2; request 67.635 → 163.943 ms. At 5.5 seconds idle: helpers 3 → 0,
total RSS 138.96875 → 47.53125 MiB. Exact initial grants and program hash match; no
survivors. Separate parser 2/100 ms native case admits two helpers, queues third,
and reaches zero after 250 ms idle; fresh revival and native identity refusals pass.
Six audit negative controls pass for the measured helper adapter, not complete
OS containment. Additional existing native tests use the selected PM interpreter
and isolated homes without claiming that adapter fences every subprocess.

One pair, 20 ms target samples, shared RSS pages; brief peaks/children may be missed.
Request-window peak and later idle checkpoints are distinct measurements. Each
native run is bounded to four runtime processes and below 4 GiB; no app, remote connection,
real gateway/worker/model, whole-gateway idle or physical-pressure result. A
smaller cap deliberately slows profile switching and can increase cold starts.
The queue limit excludes assigned requests/stdin buffering, and runtime-command
lookup retains its own 30-second timeout outside mint admission. Other helper entrypoints
and processes, MCP retirement and broader memory admission remain open.

Companion verification: **133 run, 131 passed, two Linux-only skips**, 4.518
seconds, exit 0, with task TMPDIR and bytecode disabled.

Whole-Electron no-emit TypeScript, three-file ESLint and all three development
bundles pass; no app is launched or packaged. Cumulative export adds four targets:
**1,030 versus 1,026**, same pinned upstream. Only the existing main target and four
added paths change; unrelated prior rows/bytes/patch sections stay exact. Actual
reverse/base/reapplication, every target hash, strict installed compatibility,
companion tests, release inventory and exact directory/history scans gate handoff.
Full standing GOAL remains unfinished; owner-app adoption is not claimed.

Release verification passes **230 inventory files / 231 intended tracked paths**
on a disposable copy; private index and copy are removed, real index unchanged.
Exact directory/history scan logs report no leaks across 213 history commits.
Final advisor finds no concrete blocker on supplied code and evidence. Original
app/config and all 1,030 source hashes match; 14 observed PID/birthtime identities
have no survivor. Owned dependencies, build/cache/export and short-fixture scratch
are removed (1,231,230,232 logical bytes; no physical-space saving claimed).
Source/app/runtime/borrowed objects, backups and receipts remain. Final report
closure, rescans, preservation and zero Desktop SSH precede the driver-owned commit.

# v0.14.0 — Share Desktop source-update checks

[Plain-language behavior and native Mac measurements](release-notes-v0.14.0.md).
One existing production file now owns a global FIFO around actual source-check
execution. Adjacent identical ordinary checks share raw output; each caller
parses independently. Exact command/args/cwd/environment snapshots separate
execution identities. Force and channel changes are independent barriers, and
later reads do not join across distinct work. One active plus 256 pending distinct
operations is bounded; identical joins use no extra slot. Failures release the
slot without retrying, and completed results are not retained. No new setting,
module, timer, pool or launcher/recovery/update-apply behavior is introduced.

Six meaningful old-source failures prove duplicate process launches, concurrent
nonidentical work, missing ordering/barriers and unbounded admission. The final
new cases additionally verify independent nested result objects, fresh later
checks, two separate forced checks, raw/JSON failure recovery, every execution
input and environment snapshot, full-queue identical joining, overflow recovery,
managed launcher routing and legacy null status. The process boundary is mocked
in those unit cases; the system under test is the real source-check bridge.

Post-export native selection: **35 passed, one Windows-only skip**, seven files,
18.90 seconds, exit 0. Existing native tests exercise real legacy/managed source
checks and source-channel/handoff behavior with local Git and loopback transport.
Whole-Electron TypeScript no-emit and two-file ESLint pass with no errors or lint
warnings. All three Electron development bundles compile; no app is launched or
packaged. Companion: **133 run, 131 passed, two Linux-only skips**, 4.590 seconds,
exit 0, task TMPDIR and bytecode disabled. No full native-suite pass is claimed.

Single-request generated-launcher preflight peaks at 67.34 MiB with two sampled
processes. Matched two-request native cached case: **134.875 to 67.234375 MiB**
peak summed RSS, **50.2% lower**, two interpreter launches to one, four maximum
sampled descendants to two including Git, 1240.90 to 641.82 ms. Both callers get
identical status and separate objects; config/cache bytes remain exact; no test
runtime survives. The actual generated bootstrap/recovery program matches a
fresh native regeneration. A private isolated dependency/audit prefix supplies
the existing PM Python 3.14.9 runtime; no application, SSH, network or model is used.
Eight negative audit controls and a SQLite positive pass; base audit function ASTs
match the exercised adapter. These Python checks are not complete OS containment.

One pair with 15 ms target samples and shared RSS pages; brief children may be
missed. Known native/Git topology and PID/RSS supervision keep the case within
four processes and 4 GiB. This is not a whole-update/download/apply, gateway-idle,
physical-pressure, app-adoption, Windows or model/token result. Global source-check
serialization also delays other installs behind a slow check. Existing six-minute
execution timeout excludes queue waiting. Configurable global helper admission
and other helper entrypoints remain separate work.

Fixture-only corrections: embedded audit prefix originally assumed __file__ under
python -c; its trial root is now literal. A typed synthetic commit shape and the
mock's import type were corrected. These are not product fixes or extra credited
reds. No outside-root test fixture was run this round. The source fixture launcher
and private baseline sibling were removed after measurement.

Cumulative export adds two targets (the previously unpatched source bridge plus
its new test): **1,026 versus 1,024**, same pinned upstream. Actual reverse/base/
reapplication, all hashes and strict installed-checkout compatibility pass.
Every prior target byte and patch section stays exact, including P0 SSH paths.
Incremental/root whitespace is clean; the same 13 inherited cumulative warnings
remain. Release inventory and exact directory/all-history secret scans gate the
source handoff. Full standing GOAL, owner-app adoption and broader Add4/5 remain open.

Release verification passes 229 inventory files / 230 intended tracked paths on
a disposable copy; its private index and copy are removed, real index unchanged.
The first exact directory/all-history Gitleaks scans exit 0 with no leaks across
212 history commits. Final advisor accepts the supplied source/results with no
concrete blocker. Protected app/config hashes match; nine recorded PID/birthtime
identities have no survivor. Owned COW dependencies, compiler outputs, caches,
preflight home and export objects are removed: 1,231,282,524 logical bytes, with
no physical-space saving claimed. Final matched profiles, inputs and evidence
remain. Final report scans and zero-SSH check gate the driver-owned commit.

# v0.13.0 — POSIX Desktop memory admission

[Plain-language notes and modeled-pressure Mac measurements](release-notes-v0.13.0.md).
Two production paths and three colocated test files change. The existing guard
observes execution-host memory after framing and before heavy spawn, retaining
the one-slot P0 limit. Linux explicit `MemAvailable` and Darwin bounded `vm_stat`
free-plus-inactive estimates admit at 512 MiB; low/unknown waits within the
existing deadline. EOF/cancellation prevents late work. Expiry has a distinct
guard-owned first stdout status plus exit125; the consumer strips admitted
status once. Child output/exit125 cannot impersonate expiry. No new setting,
dependency, pool, transport retry or wider concurrency policy is added.

Three new production-path tests fail on old source: premature heavy launch,
missing admission expiry and absent observation. New-source lifetime tests then
pass. Parser fixtures include zero, units, malformed/missing/duplicate fields,
page size and non-double-counting. Further actual local-session cases cover
recovery/exact Thai-NUL stdin exactly once, expiry without retry or connection
poisoning, cancellation, hung-observer reaping and cross-session slot exclusion.
Observer SIGCHLD is isolated from heavy-helper completion; existing TERM-resistant
child, retained pipes, detached serve, shared transport and cooldown cases remain.

Final post-export native selection: **228 passed, three documented skips**, six
files, 24.60 seconds, exit0. Skips retain the known upstream Mac installer-wrapper
ownership failure, deep-HOME case requiring outside-root writes, and platform
skip. An initial unrestricted selection inadvertently ran that deep-HOME fixture
and reproduced the known ownership failure; it is not acceptance. Its transient
socket was closed by fixture cleanup; the shared short directory was not deleted.
A mock missing the new owned status was updated. TypeScript whole-Electron
no-emit check passes; scoped five-file ESLint has zero errors/warnings. All three
Electron development bundles compile; no application was launched or packaged.
Companion: **133 run, 131 passed, two Linux-only skips**, 4.554 seconds, exit0,
task TMPDIR and bytecode disabled. Full native-suite acceptance is not claimed.

Same native `serve --help` case with a held native CLI-import fixture and modeled
OS pressure: peak summed RSS160.3125 ->100.8125MiB (**37.1% lower**), request
797.27 ->2232.56ms. Baseline overlaps; patched execution waits until the fixture
exits. Exact output matches. Separate real Darwin observation passes. At most
three processes sampled/<4GiB and no runtime survivors; known fixture topology
is bounded to four. One pair/15ms samples/shared pages, not actual low-memory
stress, a reservation, update-helper/gateway/app/remote/Linux/Windows/model proof.
Availability can change after observation; slot head-of-line waiting is intentional.

Full cumulative export remains1,024targets on unchanged pinned upstream. Actual
reverse/base/reapply, all hashes and strict installed-checkout compatibility pass;
unrelated prior bytes and patch sections stay exact. Incremental/root whitespace
clean;13 inherited cumulative diagnostics unchanged. Minor release inventory and
exact directory/all-history Gitleaks scans gate handoff. Private evidence lives
under the isolated admission trial; owner app/home/control state stays protected.
Configurable concurrency and broader Add4/Add5/UI acceptance remain open.

Intended-tracked-only release verification passes228inventory files/229paths;
the disposable copy and private index are removed, real index unchanged. Both
exact Gitleaks directory/all-history commands exit0/no leaks,211history commits;
neutral history identities verified. Nine audit negative controls pass, and the
native-case audit functions match the exercised adapter AST; not OS containment.
Final advisor review accepts the supplied source/results with no concrete blocker.
Own COW dependencies, compiler outputs, caches, pilot homes and export objects
are removed (1,231,474,573 logical bytes, no physical-space claim). Original app
three protected hashes, trial config/backup and1,024source hashes match. Fifteen
recorded benchmark PID/birthtime identities have no survivor. Reports and final
zero-SSH/rescan receipts gate the driver-owned commit; no owner app adoption.

# v0.12.0 — Keep saved-message metadata independent of the turn engine

[Plain-language notes and matched Mac measurements](release-notes-v0.12.0.md).
The unchanged API-content extractor moves into existing `agent.message_metadata`;
gateway transcript, gateway branch and CLI branch imports follow it. Its old
internal definition is removed, with no re-export, wrapper, option or dependency.
An unused typing import is removed with it. Five runtime paths and one behavior
regression file change. Helper source and AST match the previous definition.

The final fresh-process regression fails against the old five-file source at
`gateway.session_transcript` requesting `agent.turn_context`. The changed source
imports real `SessionStore` and builds identical transcript arguments while
refusing turn/compression/auxiliary imports and external work. Other scoped tests
cover empty/Thai/JSON/non-string sidecars, gateway branch rows and actual SQLite
append/reopen/rewrite across two homes with colliding IDs and frozen prompts.
Actual CLI branch-handler acceptance uses real SQLite with display output stubbed;
parent/child sidecars and lineage survive. This is not full CLI UI acceptance.

Initial fixture corrections preserve the existing distinction between raw empty
sidecars and conversation projections that omit them, and close SessionStore's
additional cached handles. An initial private assertion that SQLite would never
load the turn engine was invalid: its separate compressor dependency still does.
These are fixture corrections, not extra product fixes. The final matched pair
uses separate clean homes and native cold-seeded caches on both sides.

Cached readiness RSS116.9375 ->101.46875 MiB (13.2% less), one process both.
After first SQLite/save/replay136.125/135.9375 MiB and whole-case peaks214.90625/
214.671875 MiB show no meaningful later-memory or peak reduction. Configuration
loading570.18 ->397.36ms; first history operation383.66 ->555.87ms: cost shifts,
not a demonstrated workload speedup. Same config/case/bootstrap/peer/schema/raw
sidecars; later append and actual concurrent first/warm calls retain behavior.
Max3 processes/<4GiB,20ms sampling/shared pages. No app/gateway/remote/model/
production-server proof or percentage addition to previous cases.

Full cumulative export1024targets (four added targets), same pinned upstream;
actual reverse/base/reapply hashes pass, prior unrelated bytes/sections exact.
Native incremental whitespace clean; same13 inherited cumulative diagnostics.
Canonical native pytest/pinned Ruff and installed-app/cross-platform acceptance
remain unverified. Five Python audit negative controls pass; adapter containment
is not an OS sandbox. Scoped test and closing release receipts follow.

Post-export native stdlib: 27 passed, 4.080 s, exit 0, no ResourceWarnings;
includes three new metadata/storage cases and prior 24 MCP cases. Companion:
133 run, 131 passed, two Linux-only skips, 4.518 s, exit 0, task TMPDIR and
bytecode disabled. Intended-tracked-only release copy passes 227 inventory files
(228 paths); private copy/index removed, real index unchanged. Exact directory
and all-history Gitleaks scans exit 0, no leaks, 210 history commits. Final report
closure rescans gate the driver signal. Original app protected hashes/trial config
backup and all 1,024 source hashes match. Own export scratch and obsolete pilot
homes are removed; final matched homes, CLI proof and evidence remain. No physical
disk-saving claim. Desktop SSH count and final process closure are recorded privately.

# v0.11.0 — Defer MCP SDK until an actual connection

[Plain-language notes and Mac measurements](release-notes-v0.11.0.md).
Three discovery gates use the existing cheap package-availability flag. The
existing connection preparation path still loads the SDK before transport/type
feature flags are needed. No new policy, dependency, pool or lifecycle change.

Final six-case regression runs against the previous gates produced four
metadata-import failures and two passing missing-package/safe-worker controls.
Real SDK/stdio cold-seeded cache cases also failed the no-import assertion through
both public registration entry points. Initial fixture corrections covered a
too-strict loader-call assertion, native tool-name spelling, explicit lazy-state
cleanup and an unsupported repeated-registration return assumption. Those setup
failures are not product regressions or credited additional reds.

Post-export native standard-library run: 24 passed, 3.317 s, exit 0. Actual
installed SDK/stdio cases pass fresh cached discovery, direct registration,
one-server concurrent first calls, warm counter/schema preservation, cold-cache
connection fallback and a live local probe. HTTP preparation imports SDK and
transport flags with preflight disabled; no HTTP network request is claimed.
Five Python audit negative controls pass; this is not a complete OS sandbox.

Final paired fresh-client case: 151.21875 -> 116.703125 MiB before use (22.8%
less), one process on both; discovery255.04 ->5.20 ms, concurrent first-call
batch55.83 ->325.74 ms, warm0.53 ->0.58 ms. Whole-case peaks199.75/199.72 MiB
do not demonstrate peak-memory reduction. Same final case/bootstrap/peer/schema;
20 ms sampling includes shared pages. At most three processes, below 4 GiB;
every native case ends with no child/server/supervisor survivors.

Full cumulative export has 1,020 targets, pinned to the unchanged upstream
revision. Actual reverse/base/reapply hashes pass; all prior unrelated target
bytes and patch sections remain exact. Incremental native whitespace is clean;
the same thirteen inherited cumulative diagnostics remain. Canonical native
pytest and pinned Ruff are unavailable locally, freshly checked; neither full
native-suite nor installed-app/gateway/Linux/Windows acceptance is claimed.

Companion acceptance with task TMPDIR: 133 run, 131 passed, two Linux-only
skips, 4.111 s, exit 0. Intended-tracked-only release copy passes 226 inventory
files (227 paths including the manifest); private copy/index removed and real
index unchanged. Exact directory/history Gitleaks scans both exit 0, no leaks,
209 history commits. Final report-only rescans gate the driver signal. Original
app protected hashes and the retained trial config backup match; no app launch
or other-machine access. Required Desktop SSH count is zero.

# v0.10.0 — On-demand MCP startup for a profile

[Plain-language notes, configuration and Mac measurements](release-notes-v0.10.0.md).
This is an opt-in profile policy, not automatic teardown of arbitrary stateful
servers. The shared loader preserves explicit values and HTTP/event behavior.
Existing idle recycling is exercised only with explicit per-server configuration.

Test-first config regressions produced 12 failing subcases against the old loader.
Actual SDK absence tests produced one missing-hints failure and three independent
field-presence failures; explicit zero/positive TTL and profile privacy controls
pass. A native no-spawn case with a verified valid schema cache failed with the
pre-policy loader, then passed. An initial case without that cache precondition
was invalid and is not credited as the feature red. A separate deterministic
native first-use join case failed before its coordination change. Advisor review
added two failing empty-first-page cases; hints now remain from page zero even
when it has no tools, retaining explicit no-cache/private policy.

Native stdlib unittest and actual SDK/stdio acceptance run with isolated homes,
no external network, no app/SSH/model/provider operations. Broader native pytest,
pinned Ruff and installed-app adoption are not claimed. Cold discovery still
peaks at four processes; repeated discovery before first use measured
223.25 -> 154.61 MiB summed RSS (30.7% lower), four -> one processes,
60.36 -> 1.10 ms; first call 3.97 -> 43.44 ms. Same config and fixture/bootstrap;
20 ms samples include shared pages. Whole-case peaks223.78/223.11 MiB do not
establish a peak-memory reduction. All test runtime is stopped after each case.

Final post-export native stdlib run: 18 passed, 2.888 s, exit 0. Companion:
133 run, 131 passed, two Linux-only skips, 4.608 s, exit 0. Actual native
SDK/stdio lifecycle acceptance passes, including concurrent first use/revival,
active-call protection and explicit idle cleanup; maximum three processes there.
The paired measurement's cold phase uses at most four processes and under 4 GB.

Export reverse/base/reapply checks pass all 1,019 before/after target hashes;
installed-phase compatibility passes with no unrelated source changes. One old
task-only P0 baseline runner config was moved to private evidence after the
strict checkout checker correctly refused it. Prior unrelated target bytes and
patch sections remain exact. Native incremental/root diffs are whitespace-clean;
strict cumulative patch checking retains the same 13 inherited diagnostics.

Intended-tracked-only disposable release copy passes 225 inventory files
(226 paths including the manifest). Only the new release notes are added through
a private intent-to-add index; copy/index removed and real index unchanged.
Both exact Gitleaks working-directory/all-history scans exit 0 with no leaks;
208 history commits scanned. Public relative file links, Python AST and exact
final benchmark code hashes pass. This is source/native-component acceptance;
canonical native pytest, pinned Ruff and installed-app adoption remain unverified.

# v0.9.0 — Bound Desktop SSH helper fan-out

[Plain-language release notes](release-notes-v0.9.0.md) consolidate v0.8.46–.73.
[Implementation and validation](desktop-ssh-resources.md) define process-owned
master sharing, host/remote admission, helper lifetime and platform boundaries.
The P0 change is a ten-path native source/test delta: nine additional targets
join the existing 1,004-path full kit, now 1,013, without dependency/lock changes.
All unrelated prior hashes and patch sections remain exact.

Initial regression: seven failures and one passing preservation control; four additional advisor-found cases
failed before their fixes. The scoped native six-file run passes 220 cases,
with three explicit exclusions/skips: restricted external-tmp binding, a proven
pre-existing upstream Mac installer-wrapper ownership failure, and a platform
skip. This is not a complete native-suite pass. Actual marker-gated detachment
survives the guard cleanup without the setsid utility; no production ownership
predicate or stale backend record policy was relaxed.

Whole Electron TypeScript and the three Electron main/preload bundles compile;
the application was not launched or installed. Only a fresh-config OpenSSH
missing-mux test uses the real SSH executable, with literal loopback target,
zero TCP connections and no configured-proxy sentinel. No other host was used.

A paired four-request real native `serve --help` check burst over session-pipe
mocks measured 340.5 → 100.7 MiB peak summed RSS (70.4% lower), 1.192 → 3.031 s wall time,
identical outputs, four → two peak sampled Python processes and zero survivors.
Native PM Python 3.14.9 and Apple guard Python 3.9.6; nine audit negative controls
pass. Samples target 15 ms, include shared RSS pages, and are not a hard memory
quota, statistical benchmark, gateway idle, model-usage or real SSH measurement.
The earlier two-command pilot is not the released admission policy or benchmark.

Full export installed hashes, reverse/base checks, reapplication and all 1,013
before/after hashes pass. The P0 incremental/native and repository diffs have no
whitespace errors. Strict cumulative checking retains exactly the same 13 legacy
whitespace diagnostics as the previous patch; no unrelated cleanup was folded in.

Final companion checks: 133 run, 131 passed, two Linux-only skips, 4.418 s,
exit 0. Post-export native scoped run: 220 passed, three documented skips,
19.00 s. Intended tracked-only release copy passes all 224 inventory files
(225 paths including the manifest); private-index intent-to-add includes only
the two new public docs. Disposable copy removed; real index unchanged.
Both exact Gitleaks directory/all-history scans exit 0 with no leaks; 207 history
commits scanned. Owner app/home/controls and stopped timers remain untouched.
This source release does not establish installed-app adoption, other-machine
runtime validation, gateway idle reduction or completion of the standing goal.

# v0.8.76 — Recover overflowing web-cache TTL configuration

The shared TTL float-conversion handler now includes `OverflowError` in its
existing exception tuple. Signed unrepresentable integers use the established
20-minute default; representable extremes/string/nonfinite clamp behavior stays.
No config rewrite, sign clamp, new numeric limit, provider fallback or retry.
[Native real-config and cache/registry proof](search-cache-memory.md#overflowing-ttl-configuration-v0876).

Baseline102 passes/five files. Two invariant tests add24 cases before product edit:
meaningful red six failures/38 passes, no setup/import failures. Both signed values
reach the native TTL reader through actual config loading; fresh-memo registered
search fails before its selected provider on the original. Fourteen other config
controls, four disabled-cache controls and all20 prior cases pass. Source config
bytes remain exact; ordinary synthetic LKG backup creation stays in private homes.
Controlled wall/monotonic clocks and derived mtimes cover memory/disk/extraction
hits before/exactly at expiry, retaining seeded cache bytes. Actual registry calls
preserve success/error/repeat counts, selected backend/provider, healthy queries
and disabled caching; original managed policy stays, rescue is disabled/trapped.

Actual exported reverse/base/reapplication:126 passes/five complete files, zero
failures/skips/retries/exclusions,6.9s. Result43/sharing44/metadata18/eviction11/batch10.
Post-reapplication native probe reads both signed configs, returns1200 seconds,
preserves input bytes, and verifies imported path/hash against export. No actual
provider/model/network call. No performance, usage or workload saving measurement.

Borrowed PM-selected3.14.9/deps read-only, separate PM-locked pytest9.1.1/asyncio
1.3.0, private HOME/HERMES_HOME/TMPDIR and unchanged scoped Python owner-read/write/
SQLite/network/process/null/leading-flag/per-PID negatives/exit7; one compile/test worker.
No full native suite/pinned whole-source lint/health/OS containment, live API/UI/
service/fleet/original-session/terminal-goal proof. Owner source/data/apps/config/
control/quota/ESTOP/pauses/stopped timers remain untouched.

Same1004 targets/basebf0203a(v0.22.5)/all before/unrelated after hashes/sections and
selection. Only existing result-cache runtime/disk-sharing test after hashes and
sections change. Temp-index full-index binary-U1 installed/reverse/check/base/
reapply pass; native/raw-root whitespace clean. Read-only owner972/1004 match,32
pending normal lead adoption/Linux validation. No new public file/dependency/lock.
Required companion:133 run,131 pass/two Linux skips,4.415s,exit0. Tracked-only222
inventory/current hashes/exact7paths/empty real index/unchanged selection/neutral
history pass; copy removed. Both exact directory/history secret scans pass
(206 commits,no leaks). Advisors84/85 accept bounded design/handoff using supplied
evidence only; actual mandated CLI/session/outcome recorded privately.

All own native/probe/export/companion/release/scan/advisor handles are terminal.
Separate-argv Git common/object-path checks establish owned clone paths and
independent borrowed owner stores before exact cleanup. Owned trial/source/test-
tools/fixtures/home/log/cache/synthetic LKG/temp-index/probe/export tree, pointer
and setup removed; absence and borrowed resources/protected hashes verified.
Pre-cleanup729388KiB is not attributed saving; no owner backup created or purged.
Final records/hashes/inventory/scope/index/preservation/selection/whitespace/exact
scans precede subject-only driver handoff. Broad standing goal remains active.


# v0.8.75 — Prepare request-cache admission once before locking

Three changed production lines compute the existing vision request-cache admission
once before the shared lock, then reuse its decision for publication and logging.
Preparation stays inside the original exception/cleanup scope; no new await or
policy is added. [Cross-thread progress and native evidence](vision-cache-routes.md#request-cache-completion-admission-v0875).
Pending ownership, publication/TTL, capacity/LRU, follower settlement, cancellation,
native pixels, routes and the separate inner payload budget remain.

Original native probe:one owner, two validations [lock-held,lock-free]. Candidate:
one lock-free validation, with identical returned/cached values and empty pending
state. Baseline80 passes/five files. Two invariant tests add five cases before
product edit: meaningful red five failures/sixteen prior passes. A gated target
owner allows another consumer's nonblocking lock probe, actual unrelated cached
hit and new-key completion before gate release; followers settle with either the
owner value or native admission error, and cleanup remains. Actual registry calls
use real PNG/preparation/key/extraction and fixed external-provider boundaries;
ASCII/Unicode success and provider-error repeats each validate once per owner,
with no admission/provider work on a hit. Source PNG/output/reservations preserved.

Actual exported reverse/base/reapplication:85 passes/five complete files, zero
failures/skips/retries/exclusions,8.7s. Request21/content19/route14/native20/history11.
Existing cancellation/size/TTL/route/inner-byte/native/history cases retain every
assertion. Actual imported path/hash matches export. Seven alternating untraced
64-owner batches on the same200,033-byte result yield median0.167342->0.084298ms
owner completion. Separate count phases show128->64 validations, but64 producer
calls/retained keys on both implementations, equal outputs and no pending work.
These are component timings/validation counts, not whole-tool latency, memory,
model-call, cache-hit-rate or billing savings. Validation still synchronously
occupies its active event loop; cross-thread progress does not establish service
throughput or continuous Captain concurrency.

Borrowed PM-selected3.14.9/deps read-only, separate PM-locked pytest9.1.1/asyncio
1.3.0, private HOME/HERMES_HOME/TMPDIR and unchanged scoped Python owner-read/write/
SQLite/network/process/null/leading-flag/per-PID negatives/exit7; one CPU/worker.
No full native suite/pinned whole-source lint/health/OS containment, live provider/
model/API/UI/service/fleet/original-session/terminal-goal proof. Owner source/data/
apps/config/control/quota/ESTOP/pauses/stopped timers remain untouched.

Same1004 targets/basebf0203a(v0.22.5)/all before/unrelated after hashes/sections and
selection. Only existing request-cache runtime/test after hashes/sections change.
Temp-index full-index binary-U1 installed/reverse/check/base/reapply pass; native/
raw-root whitespace clean. Read-only owner972/1004 match,32 pending normal lead
adoption/Linux validation. No new public file/dependency/lock/config/cache layer.
Required companion:133 run,131 pass/two Linux skips,4.479s,exit0. Tracked-only222
inventory/current hashes/exact7paths/empty real index/unchanged selection/neutral
history pass; disposable copy removed. Both exact directory/history secret scans
pass (205 commits,no leaks). Advisors82/83 accept bounded design/handoff using
supplied evidence only; actual mandated CLI/session/outcome recorded privately.

All own native/probe/benchmark/export/companion/release/scan/advisor handles are
terminal. Actual separate-argv Git common/object-path checks establish owned clone
paths and separate borrowed owner objects before exact cleanup. Owned trial/source/
test-tools/fixtures/home/log/cache/temp-index/probe/benchmark/export tree, pointer
and setup are removed; absence and borrowed resources/protected hashes verified.
Pre-cleanup714092KiB is not attributed saving; no owner backup created or purged.
Final records/hashes/inventory/scope/index/preservation/selection/whitespace/exact
scans precede subject-only driver handoff. Broad standing goal remains active.


# v0.8.74 — Bound retained auxiliary vision analysis payload

The existing content cache now adds a 32 MiB charged key/entry payload limit to its
256-entry/one-hour TTL/LRU behavior. Native string/tuple size accounting runs under
the existing lock; oversized replacement removes only the same key, and admitted
puts evict oldest entries until both limits hold. Fresh results return unchanged.
[Native regression, limits and measurements](vision-cache-routes.md#retained-analysis-byte-budget-v0874).
No new config, dependency, fallback, result truncation or cache layer is added.

The original native 256-entry probe charges 64,081,298 bytes, despite outer-cache
result admission. Baseline: 68 passes/five files. Two invariant tests add twelve
cases before product edit: meaningful red twelve failures/seven prior passes.
ASCII/Thai/non-BMP, scale notes, exact equality/one-byte denial, byte/count LRU,
replacement, TTL and concurrent puts are covered. Direct and actual registry
paths return full fresh large results, preserve useful small hits and source
images, retain provider errors and release reservations. Exported reverse/base/
reapplication: 80 passes/five complete files, zero fail/skip/retry/exclusion, 8.2 s.
Counts: content19, route14, request16, native20, history11. Existing native-pixel
bypass and saved/runtime/concurrent route cases remain in that complete selection.

Same bounded 256-analysis fixture, original AST put with unchanged globals/lock
versus imported candidate: three separate GC/tracemalloc phases yield median
charged bytes64,081,298->33,542,612, traced retained64,069,122->33,541,294 and peak
64,319,428->34,042,341 bytes; retained entries256->134, surviving values identical.
Seven separate alternating256-put time batches at256 resident small entries show
median0.000141->0.104933ms per put. Actual imported path/hash matches export.
Container/lock overhead, transient provider results and in-flight work are outside
the budget. Fewer retained hits can require later provider calls. No whole-Hermes
RSS, workload cache-hit-rate, response-latency or billing improvement is claimed.

Borrowed PM-selected native3.14.9/deps read-only, separate PM-locked pytest9.1.1/
asyncio1.3.0, private HOME/HERMES_HOME/TMPDIR and unchanged self-tested scopedPython
owner-read/write/SQLite/network/process/null/leading-flag/per-PID negatives/exit7;
one CPU/worker. No full native suite, pinned whole-source lint/health, OS containment,
provider/model/API/UI/service/fleet/original-session/terminal-goal runtime proof.
Owner data/source/apps/config/control/quota/ESTOP/pauses/stopped timers remain.

Same1004 targets/basebf0203a(v0.22.5), all before/unrelated after hashes/sections and
selection unchanged. Exactly existing vision runtime/content-cache test after
hashes/sections change. Temporary-index full-index binary-U1 export and installed/
reverse/check/base/reapply pass; native/raw-root whitespace clean. Read-only owner
974/1004 match,30 pending normal lead adoption/Linux validation. Driver commits;
lead handles adoption and publication. Required companion:133 run,131 pass/two
Linux skips,4.457s,exit0. Tracked-only222 inventory/current hashes/exact7paths/empty
real index/unchanged selection/neutral history pass; disposable copy removed.
Both exact directory/history secret scans pass (204 commits,no leaks). Advisors
80/81 accept the bounded design/handoff, supplied evidence only; actual mandated
CLI/session/outcome are recorded privately.

All own native/probe/benchmark/export/companion/release/scan/advisor handles are
terminal. Actual separate-argv Git common/object-path checks establish owned clone
paths and a separate owner object store before deletion. Exact owned trial/source/
test-tools/fixtures/home/log/cache/temp-index/probe/benchmark/export tree, pointer
and setup are removed; absence and borrowed resources/protected hashes verified.
Pre-cleanup714144KiB is not attributed saving; no owner backup is created or purged.
Final records/hashes/inventory/scope/index/preservation/whitespace/exact scans
precede the subject-only driver handoff. Broad standing goal remains active.


# v0.8.73 — Avoid context hydration in Gateway tip checks

One native production line switches the transcript rerouter's liveness check to
`get_session_metadata(tip)` on the same parent-owner handle. It uses only row
existence and `ended_at is None`. Transitive resolution, owner isolation, epoch-zero
closure, token flush, shared errors, queued order and actual history stay intact.
Full readers and lineage configuration classification are unchanged. [Regression
and component measurement](session-metadata-reads.md#gateway-compression-tip-liveness-v0873).

Baseline59 passes. The first fixture setup used unsupported create keywords;
corrected to existing native update methods before product edit. Meaningful red:
six SQL hydration failures/60 passes. Two new invariant tests add seven cases,
covering normal/read-only/live/closed/epoch-zero SQL denial with full-reader
controls and byte preservation, native parent-owner reroute with unpublished child
and conflicting ambient IDs, token drainage, missing/same/no tip/DB and shared
errors. Existing multi-hop/closed-tip/backlog assertions remain. Exported actual
reverse/base/reapplication: five complete files136 pass, zero failures/skips/
retries/exclusions,13.4s. File counts: session66,profile24,lineage43,history2,resume1.

Same native synthetic flushed database and real resolver, original AST method with
original globals/binding versus imported candidate: seven alternating40-call time
batches median1.111593->0.219958ms; three separate traced40-call batches median
peak4,028,144->17,848bytes. Prompt1,835,008bytes plus1MiB config value. Equal outputs,
empty token queues and identical DB/WAL hashes. These are component measurements,
not whole-Hermes RSS/workload/response/billing savings. Actual imported runtime
path/hash matches exported manifest.

Borrowed PM-selected3.14.9/deps read-only, separate PM-locked pytest9.1.1/asyncio
1.3.0, private HOME/HERMES_HOME/TMPDIR, unchanged self-tested scoped Python audit/
null/process/leading-flag/per-PID negatives/exit7, one CPU/worker. No native full
suite/pinned whole-source lint/health/OS containment, live provider/model/API/UI/
service/fleet/original-session/terminal-goal proof. Older PID ancestry and UI
containment gaps remain; no guard weakening, process retries or extra model call.
Owner source/config/data/apps/control/quota/ESTOP/pauses/stopped timers untouched.

Pinned basebf0203a(v0.22.5). Two existing upstream targets with nonnull before
hashes join the kit: Gateway transcript runtime and its existing session tests,
giving1004. All prior1002 rows/sections exact. Three existing Gateway test files
join selection; no new public file/dependency/lock/schema/config. Temp-index full-
index binary-U1 export and installed/reverse/check/base/reapply pass. Read-only
owner974/1004 match,30 pending normal lead adoption/Linux validation. Driver commits;
lead handles adoption and publication. Required companion133run131pass/two Linux
skips,4.417s,exit0. Tracked-only222inventory/currenthashes/exact8paths/emptyrealindex/
neutralhistoryidentity pass; copyremoved. Native rawwhitespaceclean. Rawrootexit2
has exactlytwo necessary blank U1patchcontext lines; otherroot whitespaceclean.
Both exactdirectory/history secret scans pass (203commits,no leaks). Advisor78/79
accept boundedhandoff, suppliedevidenceonly. Actual exactmandatedCLI and exit0 are
recorded privately; no independent advisor execution is claimed.

All own native/benchmark/export/companion/release/scan/advisor handles terminal.
Actual separate-argv Git common/objectspath checks establish ownedclonepaths and
separate ownerobjectstore before cleanup. Exactowned trial/source/testtools/
fixtures/home/log/cache/tempindex/benchmark/export tree,pointer/setup removed;
absence and borrowed resources/protectedhashes verified. Pre-cleanup717380KiB
is not attributed saving; no ownerbackup created or purged. Finalrecord/hash/
inventory/scope/index/preservation/whitespace/exactscan refresh precedes driver
subject-only handoff. Broader standinggoal stays active.


# v0.8.72 — Admit optional web index publication before allocation

Six lines in the native extraction-index writer add a destination-volume check
after existing trimming and before the unchanged atomic JSON writer. Escaped-JSON
ASCII length bounds native UTF-8 and lone-surrogate fallback bytes. Free space
minus that bound must remain >=1GiB; equality succeeds. Low/unknown capacity keeps
the prior index through existing optional handling. [Behavior and tradeoffs](storage-and-backups.md#web-index-write-admission-v0872).

Original isolated native full/unknown probes observe zero volume checks, create
one atomic temp and replace prior bytes/inode. Reapplied probes observe once,
create no temp and retain exact prior bytes/inode. No actual disk pressure/loss
claim. Baseline124 passes/eight files. Sixteen cases added before product edit:
original pressure selection11 meaningful failures/26 passes, no setup failures.
All previous21 cases retained with separate payload/metadata capacity fixtures.
Final eight files140 pass, zero failures/skips/retries/exclusions,8.9s after true
exported reverse/base/reapplication. Actual imported module path/hash matches
export. Exact ASCII/Thai/surrogate serialized bytes and readback, bound equality,
post-trim counting, prior inode/mode, no pre-admission temp, atomic failure cleanup,
mixed batches and repeated actual registry dispatch/fresh result/footer are covered.

Existing atomic writer/locks/500-entry limit/payload checks, keys/TTL/routes/profile/
provider/safety/fallback policy remain. Unicode can be refused conservatively near
the margin; extra serialization/check cost unmeasured. A payload admitted before an
index refusal can remain unindexed/under old metadata. No two-file transaction,
quota/whole-cache bound/prune/global disk guarantee or production saving claim.

Borrowed PM-selected native Python3.14.9/deps read-only, separate PM-locked pytest
9.1.1/asyncio1.3.0, private HOME/HERMES_HOME/TMPDIR and unchanged self-tested scoped
Python audit/null/process/leading-flag/per-PID negatives/exit7; one CPU/worker.
No native full suite/pinned Ruff/whole-source health, OS/native containment,
live provider/model/API/UI/service/fleet, terminal-goal/original-session/workload proof.
Current read-only ancestry probe: own parent-ID succeeds, but own parents()/recursive
children raise PermissionError errno1 with no audit denial; /bin/ps remains EPERM.
No sleeper or signal; prior PID4 gap remains. Do not weaken guards to close it.
Owner source/control/data/quotas/ESTOP/pauses/timers untouched. Read-only public
source comparison974/1002 match;28 paths await normal lead adoption/Linux validation.

Same1002 targets/basebf0203a(v0.22.5), every before/unrelated after hash/selection
unchanged. Exactly existing cache runtime/pressure-test after hashes and sections
change. Temporary-index full-index binary-U1 export and installed/reverse/base/
reapply pass. Generic writer and v0.8.71 payload-helper bytes unchanged. No public
file/dependency/lock/selection added. Native/root raw whitespace clean. Required
companion: 133 run, 131 pass/two Linux skips, 4.516 s, exit 0. Tracked-only 222-file
inventory/current hashes and both exact secret scans pass (202 commits, no leaks).
Advisor77 accepts bounded handoff. Exact owned trial/source/test-tools/fixtures/
log/home/cache/temp-index/probe tree, pointer/setup removed; absence verified.
Owner runtime/source/dependencies/object store retained. Pre-cleanup 722672 KiB
is not attributed saving. Final records/hash/inventory/scans refresh before
subject-only driver signal. Broad goal stays active.

# v0.8.71 — Admit optional web full-text writes before overwrite

One web-specific helper now checks the destination volume against the final UTF-8
payload size plus 1 GiB before extraction-cache or paging-text overwrite. Low or
unknown space retains prior files; existing optional error handling returns the
fresh provider result and an accurate storage-failure footer. Each copy checks
independently. [Preservation, boundaries and limits](storage-and-backups.md#web-full-text-write-admission-v0871).

Actual original native probes for modeled full/unavailable space observe zero
volume checks, replace both prior copies/index and claim a saved paging path.
No actual disk pressure/loss is claimed. Baseline: 70 native cases across four
files. Thirteen new storage-pressure cases give eight meaningful original failures
and thirteen passes, with no fixture/import failures. Final eight-file selection:
124 pass, no failures/skips/retries/exclusions, 8.8 s after export/reapplication.
Real files, UTF-8 equality/next-byte boundaries, cap suffix, mixed-batch metadata,
prior/unrelated/index bytes, repeated actual registry dispatch and fresh text/
truthful footer are covered. Fixed selected-provider and policy/safety boundaries
use existing fixture seams; no external request or paid fallback is performed.

Borrowed PM-selected native Python 3.14.9/dependencies and separate PM-locked
pytest 9.1.1/asyncio 1.3.0 tools; private HOME/HERMES_HOME/TMPDIR, unchanged self-tested
Python audit/owner-read/write/socket/process/null/leading-flag/per-PID guards,
exit-7 propagation, one CPU compile/worker. No native full-suite, OS/native-extension
containment, UI/service/model/fleet, HTTP2/PID4, live terminal-goal or workload claim.
Owner installation/control/quota/ESTOP/pauses/timers untouched. Lead handles adoption
and Linux; current read-only public-source comparison: 974/1002 match, 28 pending.

Same 1002-target v0.22.5 base bf0203a and every before/unrelated after hash/selection.
Exactly three existing patch sections/after hashes change. Temporary index export
and installed/reverse/base/reapply checks pass. No new public file/dependency/lock/
selection. Native source whitespace clean. Raw companion diff check returns 2 for
one literal-space empty unified-patch context record at line 84245; no source
whitespace error, all nonpatch whitespace clean. Patch format remains valid.

This bounds full-text admission only: existing JSON-index persistence, generic
spill behavior, derived cache and TTL/eviction remain. No quota/total-cache bound/
automatic pruning; encoding/observation cost unmeasured. Required companion: 133
run, 131 pass/two Linux skips, 4.456 s, exit 0. Tracked-only 222-file inventory and
current hashes pass; both exact directory/all-history scans exit 0 with no leaks
(201 commits). Advisor75 accepts this explicitly partial payload-admission step.
Exact owned trial/source/test-tools/fixtures/log/home/cache/temp-index/probe tree,
pointer and setup removed; absence verified. Borrowed runtime/source/dependencies/
objects retained. Pre-cleanup 714016 KiB is not attributed saving. Final records,
hashes, inventory and exact scans refresh before driver signal. Broad goal stays
active; source installation and loaded-owner adoption remain separate.

# v0.8.70 — Admit encoded archive writes against the reserve

The companion retention packer checks each encoded gzip/tar write against observed
free space minus the write length, preserving the existing 1 GiB margin. It flushes
pending output before observation. Initial source-size admission, verification,
source/activity checks, exclusive publication, sync and removal gates remain.
[Behavioral proof and limits](storage-and-backups.md#encoded-archive-reserve-v0870).

Original actual one-byte source creates a 231-byte archive after modeled reserve+1
admission with just one observation. The new original-code regression has three
source-preservation failures on each Python 3.12.10 and native PM-selected 3.14.9:
encoded overhead, unknown space and trailer pressure. No real disk pressure claim.
Fixed retention: 30 run, 28 pass/two Linux skips on each, 0.207/0.183 s. Actual raw
file writes beneath buffering prove flush ordering, source retention, temporary
cleanup and later-report progress; ample space remains lossless. Direct sink checks
cover exact boundary, next byte and flush/observation/write error propagation.
Required full companion: 133 run, 131 pass/two Linux skips, 4.221 s, exit 0.

Native interpreter runs stdlib companion tests only from a temporary cwd with
private HOME/HERMES_HOME/TMPDIR and -I/-B/-S. No source/dependency clone, native full
suite, model/API/service/UI/owner-state work or observer/containment bypass. No new
HTTP2/PID4, original-session, terminal-goal, workload or Linux parity proof. Encoded
admission is not a quota: allocation and external writers can change free space
between observation and write. Additional packing overhead is unmeasured.

All upstream patch/manifest/selection and verification bytes remain unchanged,
including the 1002-target kit. Companion-only source, tests, README, storage and
verification documentation and release inventory change; no new public file or
dependency. Final tracked-only 222-file inventory, hashes, raw whitespace and exact
whole-directory/all-history secret scans pass (200 commits, no leaks). Advisor73
accepts the bounded handoff. Exact owned small trial/source-copy/fixtures/log/home/
tmp tree and pointer removed; absence verified, borrowed native runtime/source/
dependencies retained. Pre-cleanup 88 KiB is not attributed saving. Final gate
refresh precedes the driver signal. Driver commits; lead handles adoption, Linux
parity and publication. Broad goal remains active.

# v0.8.69 — Keep overflowing web-cache timestamps inside the miss boundary

A signed `10**400` timestamp in disposable disk search-cache metadata raises
OverflowError during float subtraction. Native disk/fresh-memo reads raise, and
registered search returns an error before reaching its provider. Add only
OverflowError to the existing disk lookup exception tuple. Miss bytes stay exact;
the normal selected-provider/store path can recover a requested query. Keys, TTL,
numeric policy, migration, deletion, retries and fallback policy remain unchanged.

Actual Mac Python 3.14.9 baseline: 47 native cases across two files. The original
disk-sharing selection has six intentional failures and 14 passes. Sixteen cases
are added: two signed direct failures, four registered success/error failures,
and ten controls. Fresh, exact TTL boundary, expired, future, missing/null/malformed
and nonfinite metadata retain behavior. An exploratory probe initially targets an
absent old memo seam; reading the actual current-kit late import corrects it before
successful registered reproduction, without product or guard changes.

Final native selection: 89 pass across six files, no failures/skips/retries, 5.7 s,
including actual final exported reapplication. Tests retain real private JSON/cache
paths and fresh memos, exact poisoned/unrelated bytes, four-process sharing,
profile/caller-copy/flight/busy/store-contention/storage-pressure controls. Registered
success invokes the selected fixed provider once with bucket 10, returns three
results, stores all ten with a finite time, and serves five through a fresh memo
without another invocation. Rescue-disabled fixture configuration preserves provider
errors and bad cache bytes, with no keyless request or managed paid fallback.
[Detailed scope and limits](search-cache-memory.md#oversized-disk-timestamps-v0869).

Borrowed PM-selected Python 3.14.9/dependencies, isolated PM-locked pytest 9.1.1/
asyncio 1.3.0, private HOME/HERMES_HOME/TMPDIR and unchanged self-tested Python audit/
null/scratch/leading-flag/per-PID guards/exit7. One CPU compile/worker, no retries.
No full native suite, live provider/model/MCP/fleet/service/UI, OS/native-extension
containment, new HTTP2/PID4, workload hit-rate/RSS/latency/billed saving or owner
adoption claim. Required companion: 131 run, 129 pass/two Linux skips, 4.525 s, exit 0.

Same 1002 targets and pinned base bf0203a (v0.22.5), all before/unrelated after hashes
and selection unchanged. Exactly two existing sections/after hashes change. Filtered
bytes, temporary index/full-index binary-U1/installed-reverse-base-reapply pass.
Imported runtime path/hash matches exported manifest; final package reruns 89.
Final test import ordering preserves the module docstring before package regeneration.
No new public file/dependency/lock/selection. Read-only owner comparison: 977/1002
match, 25 paths await normal adoption. Native/raw root whitespace clean. Tracked-only
222-file inventory/current hashes and exact directory/all-history Gitleaks scans
pass, no leaks, 199 commits. Advisor 71 accepts bounded handoff. Exact owned trial/
source/tools/fixtures/log/home/cache tree, pointer and setup removed; absence
verified, borrowed source/runtime/dependencies/objects retained. Pre-cleanup
705680 KiB is not attributed saving. Final hash/inventory/whitespace/secret refresh
precedes driver signal.

# v0.8.68 — Recheck report activity after archive publication

The shared companion packer reuses its optional activity callback after exclusive
archive publication/directory fsync and before the final source stamp/removal.
Busy/unknown activity retains source and verified archive through existing failure
report/exit 1; later eligible reports still proceed. Source mutation during the new
observation also reaches the final stamp before deletion. No observer, retention,
archive, reserve, selection or owner-control policy changes; callback-free behavior
remains. [Preservation evidence and race limit](storage-and-backups.md#report-activity-after-publication-v0868).

Actual original Mac probe opens a synthetic source FD at successful postpublication
directory fsync. Original removes pathname, FD link count zero, bytes still readable and
verified archive retained. Baseline retention26 run24 pass/two Linux skips. Two new
test methods exercise held/unknown subcases and mutation-during-second-observer;
original 28-test runs show three source-preservation failures on both required
Python 3.12.10 and PM-selected Hermes 3.14.9. No fixture/import error. One harness
log-counter initially double-counts source/trace lines; corrected parsing verifies
saved required-red output, then native red independently confirms the same failures.
Fixed retention: 28 run, 26 pass/two Linux skips on each interpreter, 0.178 s/0.158 s.
These counts overlap full companion: 131 run, 129 pass/two Linux skips, 4.459 s, exit 0.

Positive inode/device/linkcount/bytes, verified earlier archive and changed source,
post-sync observation, final-stamp ordering, main failure/exit 1, later report success,
unrelated-byte preservation and temp cleanup asserted. Observer boundary injects
fixture-only held/unknown results; real source descriptors are used. This is not
OS-wide observer/production purge/whole-disk or atomic race-freedom evidence.

Native interpreter runs stdlib companion tests only, from a temp cwd with private
HOME/HERMES_HOME/TMPDIR and -I/-B/-S parent. No source/dependency clone, Hermes native
suite, application/model/MCP/fleet/UI/service launch or observer bypass. All native
patches/manifests/selection and verification scripts remain byte-identical to HEAD;
unchanged 1002-target kit is not re-exported or re-applied. No new adoption target.
Six existing public files only; raw whitespace clean for this round. Prior v0.8.67
patch-context disposition belongs to the committed artifact. Tracked-only 222-file
release inventory/current hashes and exact directory/all-history Gitleaks scans
pass, no leaks, 198 commits. Advisor 69 accepts bounded handoff. Owned small trial/
probe/source-copy/log/home tree and pointer removed, absence verified; borrowed
interpreter/source retained. Pre-cleanup 76 KiB is not attributed saving. Final
hash/inventory/whitespace/secret refresh precedes driver signal. No owner data/
control/quota/ESTOP/pause/timer action; residual check-to-delete activity race remains.

# v0.8.67 — Avoid unused context in declared cache-scope identity

The shared identity lookup selects source, parent ID and model configuration,
retaining the existing marker helper and source handling order. Direct token
flush-before-read and missing-row behavior remain. Receipt snapshots keep the
same connection/transaction, no flush, and the original missing-row TypeError.
No fallback query, full-reader retry, auth/receipt/schema/provider-key change.
Only this method and its explanatory docstring change; source stays at2000 lines.

Baseline87 native pass. Actual original direct/snapshot/raw helper parity covers
84 configuration/source/parent states per adapter; final candidate repeats them.
Initial authorizer red3 fail/4 controls. First seven-file candidate148 pass/one
existing full-reader-call spy fails; corrected SQL trace tests the same one-row
contract and passes on original. Separate native missing-snapshot probe exposes
and preserves its error instead of a false verdict. Corrected original two-file
red3 fail/59 pass. Final/reapplied seven-file149 pass,0 fail/skip/retry,12.7s.
Seventeen explicit marker/source cases per writer/read-only handle preserve exact
scope outputs and DB/WAL bytes; receipt savepoint/visibility/queue/no-write/error
checks and direct flush-before-read/error controls pass. Existing worker ownership
and foreign-target refusal remain. [Detailed proof and measurement](session-metadata-reads.md#declared-cache-scope-identity-v0867).

Native3.14.9 borrowed PM runtime/deps, isolated PM-locked pytest9.1.1/asyncio1.3.0,
unchanged scoped Python audit/null/scratch/leading-flag/per-PID self-checks and exit7,
one CPU compile/one worker/no retries. No full native suite, live service/model/
MCP/fleet/UI, OS/native-extension containment or new HTTP2/PID4 proof.

Same read-only payload-heavy identity fixture, exact original AST versus actual
final method: seven alternating40-call timing batches, three separate traced
batches after GC, five warmups each. Equal outputs and DB/WAL hashes/empty queues.
Median batch-average1.255107->0.560297ms; traced peak4,000,638->2,107,076bytes.
Identity component only; scope memoization means no every-request saving claim.
No workload RSS/latency/cache-hit/billed-usage result.

Export1002 on pinnedv0.22.5: two existing upstream test files newly patched with
nonnull before hashes; only one prior runtime after hash changes. All previous
1000 before/other-after hashes, selection and exact unrelated patch sections stay.
Filtered bytes, installed/reverse/base/reapply pass; no public file/dependency/lock
added. Read-only owner979/1002 match,23 pending normal adoption paths.
Native source/nonpatch whitespace pass. Raw root git diff --check reports exactly
two single-space empty unified-diff context records in the patch; documented
format exception, not a passing raw whitespace gate. Canonical full-index binary
-U1 format and apply/hash checks remain; no checker/attributes changes.
Required full companion:129 run,127 pass/two Linux-only skips,4.699s,exit0.
Tracked-only222-file inventory/current hashes and exact directory/all-history
Gitleaks scans pass, no leaks,197 commits. Advisor67 accepts the bounded handoff,
concrete adapter predicate and exact raw-whitespace disposition. Owned trial/source/
tools/fixtures/logs, pointer and setup removed; absence verified, borrowed source/
runtime/dependencies/objects retained. Pre-cleanup713496KiB is not attributed disk
saving. Final hash/inventory/format/secret-scan refresh precedes driver signal.

# v0.8.66 — Normalize MCP filter names before cache fingerprint sorting

Registration already stringifies include/exclude entries. Fingerprinting sorted
raw values and raised TypeError for mixed names such as lookup/7, interrupting
lazy discovery before a healthy later cached server. Two shared expressions now
stringify before sorting. String keys, duplicates, legacy bare-string behavior,
fields/JSON/hash, filters, trust and discovery policy remain. Old numeric-only
keys may become ordinary misses; no migration or automatic recovery claim.

Native baseline cache/TTL: 29 pass/one Linux skip. New fingerprint and actual
loader/cache/ToolRegistry cases give 14 targeted failures/15 controls/one skip.
Initial repaired run passes behavior but one transport assertion includes a
loader-setup urllib3 IPv6 capability probe. Stack/phase tracing identifies it;
whole-process audit denial remains. Advisor 63 accepts measuring registration
after actual loader/cache setup, with both servers still unregistered. Corrected
fixture on exact original source repeats all 14 failures before reapplying fix.
No registration prewarming, bind allowance, platform change or audit relaxation.

Final native cache/TTL/publication selection passes 53/one Linux skip, including
actual two-process writes and after patch reapplication. Six literal old string
fingerprints, mixed permutations/ties and two old numeric-key misses are checked.
Actual include/exclude discovery registers both servers with correct names and
required parameters; include wins, config/cache bytes stay exact, registration
spawn/connect/bind counters stay zero. [Compatibility and measured scope](mcp-schema-publication.md#mixed-name-filter-fingerprints-v0866).

Borrowed PM-selected Mac Python 3.14.9/dependencies, isolated PM-locked test tools,
private HOME/HERMES_HOME/TMPDIR, unchanged self-tested Python audit/null/scratch/
leading-flag guards, one-worker canonical runs and zero file retries. Setup may
attempt a denied SDK capability probe; no whole-startup zero-attempt, OS/native-
extension containment, running MCP/model/fleet/UI or full native-suite claim.
Live stdio/HTTP shared-identity tests were screened out before execution; prior
HTTP2/PID4, live/UI/Linux/original-session/workload gaps remain unverified.

Export grows 999 to 1000 targets on the same v0.22.5 base: one existing runtime
after hash and one existing upstream regression file newly patched with pinned
nonnull before hash. Previous 999 before/other-after hashes and test selection
are unchanged. Filtered checkout hashes/exact changed patch sections and installed/
reverse/base/reapply checks pass. No new public file/dependency/lock. Read-only
owner comparison: 979/1000 match, 21 pending normal source/test adoption.
Native and raw root whitespace pass. Required companion: 129 run, 127 pass/two
Linux-only skips, 4.443 s. Tracked-only 222-file release inventory and exact
Gitleaks directory/all-history scans pass, no leaks, 196 commits. Advisor64 accepts
bounded handoff on supplied evidence. Owned trial/source/tools/fixtures/logs,
pointer and setup removed; absence verified, borrowed runtime/dependencies/object
store retained. Pre-cleanup705688KiB is not attributed disk saving. Final current
hash/inventory/whitespace/secret-scan refresh precedes the driver signal.

# v0.8.65 — Keep planner numeric overflow inside the CLI refusal boundary

A valid JSON snapshot with an oversized integer in captured_at/expires_at raises
OverflowError from the existing finite-number check. The CLI previously emitted
a traceback instead of its value-free REFUSED message. Add only OverflowError to
the existing main exception tuple. Validation/API rejection, timestamp policy,
pins, quotas, choices, explanation mode and side-effect-free planning remain.
The doctor already handles this exception; setup has no snapshot numeric path.

Original planner baseline: 27 pass. Eight added field/sign/ordinary-explain
subcases fail at the intended exact-stderr assertion before repair on both
Python 3.12.10 and committed Hermes Python 3.14.9. Each uses an actual 401-digit
JSON integer and a valid other timestamp, avoiding parser digit limits. API and
doctor refusals and input preservation pass before the CLI assertion. Fixed
planner selection: 29 pass on each interpreter, overlapping counts. Four finite
CLI controls assert selected/eligible-role-route and hold/snapshot-expired results
in ordinary/explain modes, exact unchanged inputs and no execution.

Native interpreter is resolved read-only through PM committed selection. Stdlib
companion tests run from a private temporary working directory with isolated
HOME/HERMES_HOME/TMPDIR and -I/-B/-S parent. No source/dependency clone, test-tool
install, Hermes service/model/fleet/UI launch or process-observer override.
No OS/native-extension containment or native Hermes full-suite claim.

All upstream patches/manifests/native verification/selection stay byte-identical;
unchanged 999-target kit is not re-exported or rerun here. Six existing public
files change: helper/test, README, offline guide, verification and release
inventory. No new public file/dependency/lock/adoption target. Raw whitespace
passes for this change; v0.8.64 patch-context disposition remains historical.
Required full companion: 129 run, 127 pass/two Linux-only skips, 4.500 s.
Tracked-only 222-file inventory and exact directory/all-history Gitleaks scans
pass, no leaks, 195 commits. Advisor 61 accepts bounded handoff. Owned 16 KiB
fixture/log/home tree and pointer removed; absence verified, borrowed runtime
retained. No attributed disk saving. Final hash/inventory/scan refresh precedes
driver signal. No owner configuration/data/control changes or new live-service,
workload or adoption evidence. [Operator/API boundary](offline-setup-tools.md#oversized-planner-timestamps-v0865).

# v0.8.64 — Avoid unused context reads in compression parent checks

The shared compression-child gate selects the existing metadata reader when
callable. Receipt snapshots without that API retain their existing full reader
and transaction. Child marker rules, parent decisions, direct token flushing and
exception propagation remain. Callable None/error results never retry full context.

Original baseline: 17 pass. Writer/read-only SQLite authorizers then expose ten
unused-context failures with 28 controls passing. The first candidate passes 38
focused cases but breaks two worker tests because CompressionSnapshot aliases the
helper without a metadata API. Actual adapter regressions reproduce both absent/
noncallable failures before compatible dispatch. Final focused selection: 43 pass,
including callable success/None/error, exact exception identity, direct token
flushing, original full-reader access, main/WAL/data-version preservation and
snapshot receipt connection/savepoint/no-write/no-flush checks.

Seven files pass 68 unique native cases, also after actual patch reapplication;
no failed integration case is excluded. Repeated gates overlap. Commands under
the isolated native test environment:

```sh
bash scripts/run_tests.sh -j 1 \
  tests/hermes_state/test_compression_lineage_guard.py \
  tests/hermes_state/test_session_md_export.py \
  tests/hermes_state/test_runtime_worker_history.py \
  tests/hermes_state/test_runtime_worker_compaction.py \
  tests/hermes_state/test_display_projection_parity.py \
  tests/gateway/test_session_history_canonical.py
bash scripts/run_tests.sh -j 1 tests/gateway/test_failure_writer_ownership.py \
  -k test_failure_owner_follows_only_live_lineage_markers
```

Other ownership-file cases are outside this selection. Prior two HTTP/four PID
cases remain unverified. Native Mac Python 3.14.9 uses borrowed committed runtime
and dependencies, isolated PM-locked pytest 9.1.1/asyncio 1.3.0, private HOME/
HERMES_HOME/TMPDIR and unchanged self-tested Python owner-read/write/SQLite/socket/
process/null guards. Each canonical run uses one worker and zero file retries.
No Hermes service/model/fleet/UI launch or OS/native-extension containment claim.

The equal-parent helper fixture reports median 0.786236 to 0.009057 ms and traced
peak 3,823,988 to 10,142 bytes, with equal decisions and preserved DB/WAL hashes.
These are direct-helper measurements, not receipt-snapshot, full resume, service
RSS or representative-workload gains. See [method and limits](session-metadata-reads.md#compression-parent-checks-v0864).

The pinned v0.22.5 export has 999 targets: one existing runtime after hash changes
and one existing upstream test becomes a patch target. All previous 998 before
hashes and other after hashes remain; native test-selection bytes are unchanged.
Installed/reverse/base/reapply checks pass. An initial exporter refused a mistaken
existing-target assumption before writes; its following candidate rerun is not
export proof. Corrected roundtrip and separately named reapplied runs supply it.

Native changed-source and root nonpatch whitespace checks pass. Raw root
`git diff --check` exits 2 for exactly one literal-space empty-context record at
`patches/stable-full/0001-stable-full.patch:66148`; no other warning. Advisor 59
accepts this format exception; patch format and whitespace checker remain unchanged.
Required companion: 127 run, 125 pass/two Linux-only skips, 3.924 s. Tracked-only
222-file inventory and exact Gitleaks directory/all-history scans pass, no leaks,
194 commits. Owned trial/pointer/setup removed and absence verified; borrowed
runtime/objects retained. Pre-cleanup 709752 KiB is not attributed disk saving.
Final hash/inventory/scan refresh precedes driver handoff. Read-only owner source
comparison records 979/999 matches, 20 pending normal source/test adoption.
No owner installation, data, service, control, quota, ESTOP, pause or timer change.

# v0.8.63 — Bind snapshot CLI selection to one physical home

The CLI resolves its selected home once inside controlled error handling, then
reuses it for all preflight and per-file plan/apply calls. A supported home alias
can no longer redirect the invocation to another home after inspection. Existing
helper gates and APIs remain; this is a companion-only change.

Baseline storage16 passes. Actual isolated Mac probe retargets a home alias after
preflight; old code compacts the other home's two snapshots and reports success,
leaving inspected originals untouched. Verified archives survive; this is wrong
selection, not demonstrated irrecoverable loss. Four regression subcases fail
before repair on required Python3.12.10 and committed Hermes Python3.14.9: plan/
apply after preflight and between files. Fixed storage18 passes on each, overlapping
counts, including exact initial-home bytes/archives/metadata, untouched other-home/
live/unrelated data, temp cleanup and missing/dangling-home refusal. Native runs
use stdlib tests and private HOME/HERMES_HOME/TMPDIR, with no Hermes service/model
startup or process-observation override. No source/dependency clone is required.

Physical namespace races remain; selected home/ancestors/backups must stay stable.
No batch atomicity or production cleanup is claimed. See [operator scope](storage-and-backups.md#bind-cli-selection-to-one-physical-home-v0863).

All upstream patches/manifests/native selection remain byte-identical. Six existing
public files change; no public file/dependency/lock is added. Required companion
suite: 127 run, 125 pass/two Linux-only skips, 3.669 s. Storage18 also passes under
committed Hermes Python3.14.9, including from a temporary working directory.
Whitespace, unchanged-patch and tracked-only222-file inventory checks pass.
Exact Gitleaks directory/all-history scans exit0/no leaks, history193 commits.
Owned empty fixture directories/pointer removed and absence verified; borrowed
runtime/source retained. Final refresh precedes driver signal. No owner backup,
production maintenance or attributed disk saving.

# v0.8.62 — Recheck backup paths at compaction mutation boundaries

The companion snapshot helper shares its unresolved-path `lstat` symlink check
between admission, metadata creation, exclusive publication and original removal.
Pre-resolve backup-root refusal and supported physical home aliases remain. This
preserves the original when a parent changes to a link after initial inspection.
No SQL, automatic selection, model, timer or owner-state action is added.

A real Mac fixture moves HOME/backups outside HOME after archive publication and
inserts a link to the relocated directory. Original code reports compacted and
removes the relocated source; verified gzip remains. Fifteen existing tests pass
baseline. Six added root/inner-parent subcases fail before repair on required
Python 3.12.10 and committed Hermes Python 3.14.9. They inject at compression,
metadata writing and after publication. Fixed storage selection passes 16 tests
on each interpreter, overlapping counts. Exact original/live/unrelated bytes,
expected final-output presence, gzip readback/metadata hashes and owned-temp cleanup
are asserted. Native execution uses stdlib companion tests under private HOME/
HERMES_HOME/TMPDIR, not a Hermes service or a bypass of process-observation guards.

The repeated guard detects tested windows; it cannot make check-to-use operations
atomic. Keep backup namespace stable. See [operator limits](storage-and-backups.md#revalidate-snapshot-paths-during-compaction-v0862).

All upstream patches/manifests/native selection stay byte-identical. Only existing
companion helper/test, README, storage guide, verification and release inventory
change; no new public file/dependency/lock. Required companion suite: 125 run,
123 pass, two Linux-only skips, 3.794 s. Storage cases also pass under committed
Hermes Python 3.14.9. Raw whitespace and unchanged-patch checks pass; tracked-only
inventory passes for 222 release files. Exact Gitleaks directory/history scans
exit zero with no leaks; history covers 192 commits. Final refresh follows owned
cleanup. No production backup purge,
owner config/service/control/quota/stop/timer change or disk-saving claim.

# v0.8.61 — Preserve named-profile links through native case aliases

The shared recall link helper replaces one validated candidate's resolved-string
comparison with `samefile(home)`. Native case-insensitive directory aliases can
have different resolved spellings despite identical filesystem identity. Before
repair a work-profile read emitted a bare link, which reopened review content
after switching profiles with a colliding ID. Actual Mac Python 3.14.9 reproduces
this with native SQLite stores and no model request.

Original link-file baseline: 24 pass/one known FileExistsError before assertion.
A conditional fixture uses the existing native case alias, or creates the original
symlink when absent, and asserts same-file identity. Fixture-only red now reaches
the canonical-link assertion. Extended red: six intended failures/25 controls.
The helper plus five registered-handler modes require canonical work qualification
and original content after switching to review. Main/WAL byte preservation and
specifically injected runtime-identity OSError fallback pass. Validation, existence,
default-root, explicit profile precedence and the existing quiet failure boundary
remain. No broader normalization, schema/query/provider/config/control change.

Seven selected native files pass 221, zero failures/skips/deselections/retries,
38.8 s, one worker. The prior case-alias exclusion is gone:

```sh
bash scripts/run_tests.sh -j 1 \
  tests/tools/test_session_search_title_bounds.py \
  tests/tools/test_session_search_scoped_query.py \
  tests/tools/test_session_search_link_scope.py \
  tests/tools/test_session_search_readonly.py \
  tests/tools/test_session_search.py \
  tests/tools/test_session_search_safe_window.py \
  tests/tools/test_session_search_fleet_scope.py
```

Reapplied link-file checks pass 31 again, overlapping the 221. Actual Mac filesystem
case alias is exercised; the retained symlink branch needs a case-sensitive host
for fresh execution. This is not a full native-suite or fresh Linux result. Prior
two HTTP/four PID cases are not selected or newly validated. No UI/model/fleet/
service/process-wait or owner state/control/quota/stop/timer changes.

Committed runtime/dependencies borrowed read-only, separate native PM locked
pytest 9.1.1/pytest-asyncio 1.3.0, same scoped audit guard/null/scratch/wrapper checks,
fresh negative/exit-status-7 selfchecks, one CPU/worker, no retries. OS/native-
extension containment remains unproven; no runtime harness correction needed.

Export retains all 998 paths, pinned v0.22.5 base/before hashes and native selection
bytes. Only existing search runtime/link-test after hashes change. Installed,
reverse-to-base and reapply checks pass all 998. Companion suite: 124 run,
122 pass, two Linux-only skips, 3.886 s. Native changed-source and raw root
whitespace pass. The tracked-only 222-file release inventory passes. Exact
Gitleaks directory/history scans exit zero with no leaks; history covers 191
commits. Final refresh follows owned cleanup. See [behavior and limits](session-recall.md#case-alias-profile-links-v0861).

# v0.8.60 — Keep recall usable with nonfinite start timestamps

The existing `_coerce_started_ts` helper returns None for numeric conversion
ValueError/OverflowError and for overflowing numeric text. It preserves exact
integers, finite floats, numeric strings, ISO parsing and boolean/empty handling.
Title, scoped-query and message-page metadata checks keep their existing policy
for unknown start times. No database rewrite/schema, query/rank/profile/visibility, provider,
retry, control or timer change. See [behavior and preservation limits](session-recall.md#nonfinite-session-start-times-v0860).

Actual native Mac Python 3.14.9 persists REAL infinity and reproduces all three
failures with no date bound. Four-file baseline: 54 pass/one unrelated fixture
setup failure. New tests initially assert a nonexistent `_read_only` attribute;
that test-only typo is corrected to `read_only` before source edit. Corrected red: 31 conversion
failures/33 passes; fixed and reapplied focused file: 64 passes each, overlapping.
Twenty direct cases and 36 registered-handler cases cover persisted signed
infinity/finite controls, writer/read-only handles and unbounded/matching-bound
behavior. Bounds require explicit exclusion or the exact scope error; unbounded
responses require actual title/message IDs and content. Numeric NaN is direct-only.
Main/WAL byte and data_version checks pass; real read-only UPDATE fails with SQLITE_READONLY (8),
readers close, seed writer remains open until fixture teardown. No owner data/model.

Seven admitted native files pass 214, zero failures/skips/retries, 35.8 s, one worker:

```sh
bash scripts/run_tests.sh -j 1 \
  tests/tools/test_session_search_title_bounds.py \
  tests/tools/test_session_search_scoped_query.py \
  tests/tools/test_session_search_link_scope.py \
  tests/tools/test_session_search_readonly.py \
  tests/tools/test_session_search.py \
  tests/tools/test_session_search_safe_window.py \
  tests/tools/test_session_search_fleet_scope.py \
  -k 'not test_context_profile_symlink_uses_a_canonical_link_name'
```

The single deselected case attempts a distinct WoRk symlink beside existing work
on this case-insensitive filesystem and raises FileExistsError before its behavior
assertion. Original 54/1 baseline is retained. Fixture and related runtime stay
unchanged; canonical-profile symlink behavior remains unverified here. Prior two
HTTP/four PID cases are not selected or newly validated. No full-suite-green claim.

Committed runtime/dependencies are borrowed read-only. Separate native PM tools
use locked pytest 9.1.1 and pytest-asyncio 1.3.0. The existing scoped Python audit
guard, verified null sink, private scratch and wrapper flag/probe handling remain.
Fresh negative checks and exit status 7 propagation pass; one CPU/worker, no retries.
OS/native-extension containment remains unproven. No UI/service/model/fleet work,
owner state/control/quota/stop/timer change or new workload-saving claim.

Export retains v0.22.5 base, all 998 paths/before hashes and native selection bytes;
only existing search runtime/title-regression after hashes change. Installed,
reverse-to-base and reapply checks pass for all 998 targets; reapplied focused
checks pass 64 cases. Companion suite: 124 run, 122 pass, two Linux-only skips,
3.767 s. Native changed-source and raw root whitespace checks pass. The tracked-
only 222-file release inventory passes. Exact Gitleaks directory/history scans
exit zero with no leaks; history covers 190 commits. Final refresh follows owned
cleanup before driver handoff.

# v0.8.59 — Reject boolean goal-judge wait targets

The shared integer-alias helper now skips booleans before conversion. Previously,
JSON true in any PID/time alias selected target 1 and could override a later valid
PID/time. The two-line fix retains session/PID/time priority, normal no-target
continuation, overflow handling, integer 1, numeric strings, finite-number coercion
and legacy done:true. No memo, timeout, provider, scheduler or wait-execution change.

A guarded actual native Mac Python 3.14.9 probe reproduces six true-to-1 results
and boolean override of a later valid PID. All 27 existing focused cases pass
baseline. Twelve new raw-JSON true/false cases and fourteen judge API cases then
give twelve expected assertion failures and 41 passes. The fixed focused selection
passes 53; seven admitted files pass 146, zero failures/skips/retries. These cover
goals, memo, judge delegations, timeout, auxiliary accounting, delegated decisions
and board counts. The 53 focused cases overlap the 146. See
[behavior and compatibility](goal-result-waits.md#boolean-judge-wait-targets-v0859).

The native command uses the guarded interpreter and locked tools described below:

```sh
bash scripts/run_tests.sh -j 1 \
  tests/hermes_cli/test_goals.py \
  tests/hermes_cli/test_goal_judge_memo.py \
  tests/hermes_cli/test_goal_judge_delegations.py \
  tests/hermes_cli/test_goal_judge_timeout_config.py \
  tests/hermes_cli/test_goal_aux_accounting.py \
  tests/hermes_cli/test_goal_delegated_decisions.py \
  tests/hermes_cli/test_goal_kanban_board_counts.py \
  -k 'not test_parked_on_live_pid_does_not_continue_or_judge and not test_stop_waiting_clears_barrier and not test_barrier_on_a_live_process_does_not_expire and not test_judge_wait_pid_parks_loop'
```

The four excluded cases are:

- `test_parked_on_live_pid_does_not_continue_or_judge`
- `test_stop_waiting_clears_barrier`
- `test_barrier_on_a_live_process_does_not_expire`
- `test_judge_wait_pid_parks_loop`

These remain unverified under the prior process-ancestry boundary. No guard is
bypassed or actual wait/signalling added to the new regressions. Committed native
runtime/dependencies are borrowed read-only; separate locked pytest 9.1.1 and
pytest-asyncio 1.3.0 tools, scoped Python audit guards, verified null sink,
trial-local scratch, one CPU/worker, zero file retries and fresh exit-7/negative
selfchecks retain prior admission. OS/native-extension containment is unproven.
No owner home/config/profile/database/app/service or stop/quota/timer change.

The source export retains base v0.22.5, all 998 paths/before hashes and native
selection bytes. Only existing goals runtime/regression after hashes change.
Installed/reverse/base/reapply checks pass all 998; reapplied focused cases pass
53 again. Companion suite: 124 run, 122 pass/two Linux-only skips, 3.859 s.
Native changed-source and raw root whitespace checks pass. The tracked-only
222-file release inventory passes. Exact Gitleaks directory and all-history scans
exit zero with no leaks; history covers 189 commits. Final refresh follows cleanup.

The attempted fresh isolated UI lane stops before app/backend launch or dependency
copy: required sandbox-exec containment fails even for true with sandbox_apply
EPERM. A fresh loopback bind succeeds but does not establish UI readiness. Existing
v0.8.7 vision-routing proof already covers the historical catalog-fixture failure;
it is not a new fix or an unresolved resolver bug in this round. Live terminal
goals, owner-process adoption, representative workload gains and Linux parity
remain separate.

# v0.8.58 — Stream prepared-image cache-key hashing

`_analysis_cache_key` reuses `hashlib.file_digest` on a context-managed binary file
instead of allocating full image bytes for SHA-256. Metadata evaluation order and
final key identity remain. No new helper/dependency/minimum Python, cache setting,
route, prompt/history, image-preparation or provider behavior.

All 32 original content/route/request cases pass baseline. Five new cases expose
two original stream-path failures with five controls in the focused file, then
all seven pass after edit. They cover stable keys without whole-file read, same-size
valid PNG changes with preserved mtime, real handle closure on success/digest error
and missing/open-error fallback. Whole three-file selection passes 37; native
saved/runtime/direct/registered/concurrent boundaries remain. Reapplied focused
file passes seven again; counts overlap. No full native-suite claim.

Actual Mac Python 3.14.9 uses original function AST and imported candidate against
one real native-prepared valid PNG, 12,589,062 bytes, 2048×2048 RGB. Seven alternating
10-call time batches give median batch-average 4.738133 to 4.601042 ms. Three separate
traced batches give peak 12,665,605 to 470,798 bytes, identical across each variant's
three batches. All keys match; prepared SHA unchanged. Setup/import/preparation/
warmup excluded. See [method, ranges and limits](vision-cache-routes.md#streaming-content-keys-v0858).
No whole-service/vision-workload RSS, usage, cache-hit or live-owner gain claim.

Borrowed committed runtime/dependencies read-only; isolated locked test tools,
self-tested scoped audit/null/scratch/exit guard, prior duplicate-flag/per-process
probe fidelity, one CPU/worker and zero retries. No new harness correction needed.
OS/native-extension containment remains unproven. No owner source/config/profile/
database/apps/services, stop/quota/timer change; blocked HTTP/PID cases not rerun.

Export retains all 998 paths, base/before hashes and native test-selection bytes.
Only vision runtime and existing content-regression after hashes change. Installed/
reverse/base/reapply checks pass; native and raw root whitespace pass without a
format exception this round. Companion suite: 124 run, 122 pass/two Linux-only skips, 3.849 s. Tracked-only inventory
verifies 222 rows and patch hashes; both exact secret scans pass without leaks,
188 history commits. Advisor accepts scoped key-path gains. Owned trial/pointer
removed, borrowed dependencies retained. Final hash/scan refresh precedes driver
signal; owner adoption and Linux/live/workload proof remain separate.

# v0.8.57 — Tolerate overflowing MCP cache expiry metadata

Native `get_cached_entry` catches only OverflowError around its existing TTL
finite-validation/deadline operations and returns the ordinary miss sentinel.
One persisted bad hint no longer aborts the shared lazy-discovery loop before
healthy entries register. No discovery, writer, lock, schema, numeric policy,
provider, retry or cache-deletion change. See [native regressions and boundaries](mcp-schema-publication.md#overflow-safe-expiry-metadata-v0857).

Five original TTL cases pass. New actual disk-cache signed-field and real mixed
lazy-discovery tests give six targeted overflow failures/fourteen controls before
production edit. All twenty pass after repair and after export/reapply. Healthy
required schema parameters, bad-server eager set, unchanged file bytes, zero
transport calls, malformed/nonfinite misses, exact expiry and defensive copy hold.

Adjacent SDK/publication files give 33 unique native passes/one Linux-only skip
across three files. Initial publication attempt fails because a temporary Python
wrapper misreads duplicate -B as filename; second reaches native writer but startup
checks race a shared positive probe path. Tracker bookkeeping errors/timeouts are
recorded for that second attempt, not attributed to production cache code. Narrow
temporary corrections handle only redundant leading -B/-S/-I (unknowns rejected)
and use per-process positive probe names. Negative/admission/null checks remain.

Three concurrent guarded wrappers each exit7 and are reaped; probe files disappear.
An owned native spawn failure child exits7 and is joined/reaped. Corrected actual
two-writer test requires both child exitcodes zero and finally joins; all four
publication cases pass; corrected runner reports no tracker diagnostics. No OS/native-extension containment
claim. No previously blocked HTTP/PID cases or live service/model work attempted.

Export998 targets: only cache runtime after hash changes among prior997; add existing
pinned TTL regression before/after row. All previous before/other after hashes stay.
Export script initially assumes the test needs adding to selection; it is already
selected, so that assertion refuses after writing patch/manifest. Explicit final
checks prove selection bytes unchanged and export coherent. Installed/reverse/base/
reapply998 checks pass; focused reapplied twenty pass. No incomplete artifact claim.

Native changed-source and nonpatch-text whitespace pass. Raw root diff --check
returns2 solely for one literal-space empty inner patch context record; canonical
Git full-index/binary/U1 format is retained. This format disposition is separate
from successful patch roundtrip/hash checks; no checker or attribute weakening.
Companion suite: 124 run, 122 pass/two Linux-only skips, 3.963 s. Tracked-only inventory
verifies 222 rows and patch hashes; both exact secret scans pass without leaks,
187 history commits. Advisor explicitly accepts the one canonical context record
while preserving raw-check exit2. Owned trial/pointer removed; original dependencies
remain. Final hash/scan refresh precedes driver signal.

# v0.8.56 — Restore native compressed-resume acceptance

`tests/hermes_cli/test_resume_compressed_gateway_id.py` replaces its stale
zero-argument config-loader stub with synthetic YAML and the real native loader.
The fixture binds the Gateway's import-time launch home to its isolated home.
One new test uses distinct launch/profile low/high reasoning settings and checks
low/high/low results from default/explicit/default reads. No production code changes.

Fresh baseline reproduces three setup TypeErrors; after adding the profile control,
that control passes while all three original cases still error. Fixture repair
then passes four: classic preload/late history restore addresses the logical receipt
owner, direct physical tip still fails with `storage_unavailable`, and profile
loader separation holds. Native Mac Python 3.14.9 uses actual SessionAuthority,
SQLite receipts/compression and in-process GatewaySessionStore dispatch. Reapplied
export passes all four again. See [actual coverage](session-metadata-reads.md#compressed-resume-receipts-v0856).

Adjacent warm/cold compression/ownership and policy/posture cases give 50 unique
passes across four native files. The initial optional breadth run has 50 passes
and two failures: actual HTTP model fixtures stop at the existing socket-bind
network audit guard. These were selected before their socket needs were screened;
no guard change or blocked-case retry follows. The admitted rerun uses exactly:

```text
-k 'not test_launch_policy_reaches_real_turn_runner and not test_ordinary_daemon_cli_launch_policy'
```

Only those two cases are deselected: policy file 21 instead of 23, other files
unchanged at 6, 19 and 4. They remain network-unadmitted/unverified; no passing
full-suite or live-service claim. Prior four process-observation PID cases and
original-session/live goal/UI requirements remain open.

Committed native dependencies are borrowed read-only. Locked isolated test tools,
self-tested scoped owner-read/write/socket/process/null guards, trial scratch,
exit 7 propagation, one CPU/worker and zero retries remain. Native-extension/OS-wide
containment is not established. No owner source/config/profile/database/app/service,
quota, ESTOP/pause or timer change; source/runtime adoption and Linux parity separate.

The export adds one existing pinned upstream test target/selection, giving 997.
Every prior 996 before/after row is unchanged; no production hash change. Exact
installed/reverse/base/reapply checks and native/raw root whitespace pass. Required
companion suite passes: 124 run, 122 pass/two Linux-only skips, 3.882 s. Tracked-only
inventory verifies 222 rows and patch hashes. Both exact secret scans pass without
leaks; history scans 186 commits. Final advisor accepts scoped handoff. Owned source/tools/fixtures/caches/log tree
and pointer are removed; borrowed dependencies remain. Final hash/scan refresh
precedes driver handoff.

# v0.8.55 — Avoid context reads during classic resume selection

The native classic title-or-ID selector reuses `get_session_metadata` for its
initial ID check. One call changes; title/local-prefix priority, compression-tip
and fork/delegate handling, fallbacks and full-reader API remain unchanged.

New `tests/hermes_cli/test_resume_metadata_reads.py` runs actual read-only SQLite
selection in fresh child processes. Its seven cases cover exact ID/title/prefix
continuation, ambiguity/missing/read failure/absent store, actual constructor mode,
connection closure and complete initialized-profile file/directory preservation.
The corrected unchanged-source run gives three targeted positive-ID failures and
four controls; candidate and reapplied export both pass seven.

Three earlier six-fail/one-pass attempts exposed fixture assumptions, before the
production edit: readonly SQLite creates empty WAL/derived SHM; native config
initialization creates SOUL.md and standard directories; fresh CLI import creates
agent.log/errors.log. The native write trace runs through SessionDB readonly open,
pragmas, load_config_readonly, ensure_hermes_home and initialize_home. The config
API name describes shared-cache semantics, not filesystem immutability. Explicit
native profile initialization and ordinary import now precede seed/snapshot; no
selector prewarming. Fresh lookup preserves every existing byte and directory,
including logs, with only validated empty-WAL/derived-SHM additions. No bare-home
or existing nonempty-WAL preservation claim. See [scope and measurement](session-metadata-reads.md#classic-resume-identity-v0855).

Four adjacent files pass 33 cases with one Linux-only skip; together five files
pass 40 unique cases/one skip, also after reapply. Optional
`test_resume_compressed_gateway_id.py` has three setup TypeErrors in both candidate
and byte-identical original: its zero-argument config-loader stub receives the
native explicit path. Its behavior assertions never run; fixture remains unchanged.
This is a recorded coverage gap, not a passing full native suite. Prior four PID
cases remain unverified; no process-guard bypass or fresh live model/service run.

Actual native Mac Python 3.14.9 measures real selector open/read/tip/close on one
payload-heavy synthetic read-only database. Seven alternating 40-call batches give
median batch-average 2.191502 to 1.355344 ms; three separate tracing batches give
median peak 3,903,339 to 256,853 bytes. All IDs match and database bytes remain.
Import/setup/warmup are outside measurement. No whole-service or live usage claim.

Same committed native dependencies and isolated locked test tools, self-tested
scoped Python audit/null/scratch/exit adaptations, one worker/CPU and zero file
retries. Native-extension/OS-wide containment is not established. Owner source,
config/profile/database/app/service, quota, ESTOP/pauses and timers are untouched.
Read-only owner-source comparison records ten pending source/test targets.

The v0.22.5 export has 996 targets: existing main after hash changes and one new
regression target/selection. All previous before hashes and other after hashes
remain. Installed/reverse/base/reapply checks pass; native and raw root whitespace
checks pass. Companion suite: 124 run, 122 pass/two Linux-only skips, 3.866 s.
Tracked-only inventory verifies 222 rows and patch hashes. Both documented exact
secret scans pass without leaks; history scans 185 commits. Advisor accepts the
scoped fixture boundary, documented optional Gateway coverage gap and final
handoff. Owned trial source/tools/fixtures/cache/log tree and pointer are removed;
borrowed original dependencies remain. Final inventory/scan refresh precedes the
driver commit signal.

# v0.8.54 — Avoid full-context reads for exact session IDs

The exact branch of native `resolve_session_id` calls `get_session_metadata`
instead of `get_session`. This one-line change reuses the same token-count flush,
returns the same ID and avoids unused prompt/tool/config materialization. Prefix
SQL, ambiguity, wildcard escaping, full-reader API and caller signatures remain.
No new projection, schema, cache, provider work or permission rule is introduced.

Six existing metadata/search tests pass before edits. New writable/read-only
authorizer cases fail specifically on forbidden unused context reads; prefix and
pending-token persistence controls already pass. The scoped red run has two
failures/eight passes, then all ten pass after repair. An initial test attempt
shared model-config denial with FTS cases, blocking their legitimate lineage
configuration reads; that extra denial is now local to ID resolution. The original
search authorizer and production search behavior are unchanged.

Twenty-eight related profile/foreign-session/accounting cases and two selected
existing full-reader/prefix cases pass, giving 40 scoped native cases across five
files. This includes a selected subset of the large state test file, not the full
file or native suite. The four previous PID cases remain unverified; a fresh OS
process-inspection probe is refused, with no guard bypass or child spawned.

Actual native Mac Python 3.14.9 compares the original and candidate resolver methods
on the same synthetic read-only database. Seven alternating 40-call timing batches
give median batch averages of 0.825658 versus 0.008156 ms per exact lookup. Three
separate allocation batches give median traced peaks of 3,824,400 versus 9,944
bytes. All IDs match. Setup/warmup are outside measurement; version order alternates,
timing and tracing stay separate. Ranges, payload and limits are recorded in the
[read-path guide](session-metadata-reads.md#exact-session-id-lookups-v0854). No whole-service
RSS, startup, live workload or billed saving is established.

Tests retain the prior isolated source/home, read-only native dependencies, locked
temporary test tools, self-tested scoped audit/null/scratch/exit adaptations, one
worker and zero file retries. No owner source/config/profile/database/app/service,
pause/ESTOP, quota or timer change. Native-extension/OS-wide containment remains
unproven. Owner adoption and Linux runtime proof are separate.

The export retains all 995 targets, before hashes, pinned v0.22.5 base and test
selection; exactly two existing after hashes change. Installed, reverse/base and
reapply/installed checks pass, and the reapplied focused file passes ten again.
Those counts overlap. Companion suite: 124 run, 122 pass/two Linux-only skips.
Tracked-only release inventory verifies 222 rows and patch hashes. Raw diff and
changed native-source whitespace checks pass without a format exception this
round. Read-only owner-source comparison records eight targets pending adoption.

# v0.8.53 — Bound retained terminal Git-label memory

The native status-bar Git-label cache now retains at most 128 cwd entries in
insertion order. Hits retain their fast path and five-second TTL; refreshing an
expired key does not change its eviction position. Oldest-entry eviction recomputes
labels normally on revisit. The helper still uses direct local reads, with no new
dependency, configuration, process, provider request or background cleanup.

The existing two-case native file passes before edits. Five added cases give three
expected cache-bound failures and four passing controls before the production
change. All seven then pass, including positive/empty labels over 512 directories,
exact TTL expiry, no fresh-hit Git probe, FIFO refresh/revisit and BOM/detached/
worktree behavior. Fifty adjacent native status/layout cases pass separately.

Native ARM64 Mac Python 3.14.9 runs an equal 512-directory workload in separate
old/new processes. Every returned label matches. Against idle tracing snapshots,
net retained Python allocation is 147,730 versus 49,625 bytes, with 512 versus 128
cache entries. Paths, clock and tracing boundaries match; fixture bookkeeping is
prepared before tracing. This single component fixture proves neither whole-Hermes
RSS nor latency/usage savings. See [measurement and limits](chat-rendering-surfaces.md#bounded-git-label-cache-v0853).

Testing uses an isolated source/home, read-only existing native dependencies,
locked temporary test tools and the existing self-tested scoped audit/runner
adaptations: protected owner-state reads, outside Python writes, socket bind/connect
and unadmitted processes denied; exact null sink admitted; one worker and zero file
retries. Native-extension/OS-wide containment and full native-suite coverage are
not claimed. Owner installations, services, stop controls and timers are preserved.

The kit adds two existing upstream paths to the pinned v0.22.5 export: 995 targets,
with all previous 993 rows unchanged. Native test selection explicitly includes the
existing Git-label test file. Source installation, owner adoption, Linux parity and
public delivery remain distinct gates. Capacity 128 is a bounded policy choice,
not an optimum; workloads exceeding it can incur extra filesystem reads.

Exported installed, reverse/base and reapply/installed checks pass all 995 targets;
the reapplied native file passes seven cases again. Counts overlap with the 57
native cases above. Companion suite: 124 run, 122 pass, two Linux-only skips.
Tracked-only release inventory verifies 222 rows and patch hashes. Raw generic
`git diff --check` reports one whitespace warning for a single-space empty context
record in the generated patch; this is an explicit format exception. Native changed
source and other public text pass whitespace checks. Patch formatting/checkers are
not weakened. Owner adoption remains pending for six source/test targets.

# v0.8.52 — Refuse linked snapshot backup roots

The companion snapshot helper checks the unresolved `HOME/backups` entry before
resolving it. This repairs the boundary once in `_candidate`, shared by API calls
and CLI preflight/apply. Linked roots pointing outside or inside the selected home
and dangling roots are refused. Explicit home aliases and physical nested backup
compaction retain their existing behavior. No native source patch changes.

All eleven existing storage cases pass before edits. Four new tests add linked-root
API/CLI refusal and compatibility controls. Against the old helper, the fifteen-test
file reports six failing subcases from accepted linked roots and two expected
file-not-found errors for dangling links. With the narrow repair, all fifteen pass.
Refusal checks preserve source bytes, links and directory inventory; a later linked
descendant also leaves the earlier valid CLI selection untouched.

On ARM64 Mac, the actual PM-selected Python 3.14.9 and installed native `SessionDB`
create a synthetic session/message database. Its source module matches the stable
manifest. Linked-root CLI apply refuses without mutation; physical-root apply then
compresses it, decompression matches every original byte, and a fresh native process
reads the retained multilingual message. An initial harness-only assertion assumed
the snapshot had no native lock siblings; replacing it with the actual before/after
inventory comparison resolves that failure. Production helper code is unchanged
after its focused green run.

Native children use a clean environment, isolated home, `-I -B -S` and self-tested
Python audit guards against owner-state reads, out-of-trial writes, network and
process starts. These guards do not contain every native-extension operation or
prove OS-wide isolation. Trial files are removed; borrowed source/dependencies and
owner configuration, profiles, databases, services, pauses/ESTOP and timers remain.

The full companion suite runs 124 tests: 122 pass and two Linux-only cases skip.
The tracked-only disposable package verifies all 222 inventory rows and patch
hashes. Native patch/manifests remain byte-identical to v0.8.51, with no source
apply/reverse rerun claimed. Both exact directory/history secret scans pass with
no leaks found; the advisor accepts this scoped handoff using supplied evidence.
This is snapshot safety and native fixture readback, not live model acceptance,
original-session adoption, a whole-disk guarantee or race-safe filesystem access.

# v0.8.51 — Handle overflowing judge wait targets

The shared native wait-target parser now catches `OverflowError` alongside its
existing invalid-type/value exceptions. This one-line repair handles signed
numeric overflow across all six aliases without changing wait priority, fallback,
no-target continuation, flags or the v0.8.50 memo repair. Out-of-range conversion
no longer escapes the judge's normal return contract.

The actual installed parser reproduces the failure with numeric `1e999` in all
aliases in an isolated synthetic-home probe. In the pinned candidate, six existing
focused cases pass; 21 new cases then yield 18 expected overflow failures and three
passing priority/filter controls. After repair all 27 focused cases pass, with
real parser/judge imports and controlled auxiliary replies. This is offline proof,
not a live model verdict or original-goal terminal result.

The native seven-file selection passes 106 admitted cases and explicitly excludes the same four PID cases
listed in the v0.8.50 section below; their unsupported process-ancestry cleanup is
not retried or declared validated. Test and native guard code are not bypassed.
Scoped Python guards, exact verified null sink, trial-local scratch, one CPU/worker
and zero file retries retain the prior admission boundaries. No owner state,
service, pause/ESTOP, timer or provider setting changes.

The consolidated patch retains upstream v0.22.5 and 993 targets; only the existing
runtime and regression file change. Existing native test selection already covers
that file. See [wait-target handling](goal-result-waits.md#overflowing-judge-wait-targets-v0851).

The exported patch passes installed verification, reverse-to-base verification
and reapply/installed readback for all 993 targets. Its reapplied focused native
selection passes 27 cases again. Companion tests run 120 cases: 118 pass and two
Linux-only cases skip. The tracked-only disposable 222-file package passes release
verification. Counts overlap and are not a full native-suite or live-acceptance
claim. Owner adoption and Desktop/terminal-goal evidence remain pending.

# v0.8.50 — Preserve goal-judge timestamp evidence

The goal-judge memo no longer strips timestamps from rendered evidence. Its sole
caller renders an unchanged outgoing prompt and a canonical memo prompt with only
the generated clock empty. The hash helper preserves that canonical text. Source
changes are limited to two existing runtime files and their existing regression;
the consolidated kit keeps its v0.22.5 base and 993 targets.

The native three-case baseline passes. New red regressions show 15 stale `done`
reuses after evidence changes and three missed reuses when only the clock changes.
All 21 cases then pass, including exact outgoing/canonical rendering for plain,
subgoal and contract templates and preservation of spoofed clock lines. Separate
actual-candidate controls cover wait, parse/transport failures and memo admission.
No actual model judges these fixtures or finishes an original goal.

The wider seven-file run reports 85 pass and four failures. The native live-system
guard refuses cleanup signals when this environment cannot establish ancestry of
the synthetic child processes. Those capability-blocked cases are:

- `TestWaitBarrier::test_parked_on_live_pid_does_not_continue_or_judge`
- `TestWaitBarrier::test_stop_waiting_clears_barrier`
- `TestWaitBarrier::test_barrier_on_a_live_process_does_not_expire`
- `TestJudgeDrivenWait::test_judge_wait_pid_parks_loop`

All are in `tests/hermes_cli/test_goals.py`. Their recorded child PIDs are later
absent. No guard is bypassed. Explicitly excluding only these four nodes yields
85 pass, zero failures across the same seven files. This is an admitted selection,
not an inherited-failure claim or a globally green native suite; counts overlap.

Testing uses isolated source/state and locked temporary pytest tools alongside
existing native dependencies. Task-local guards self-test owner-state, write,
network and process restrictions. Runner scratch is redirected into the trial,
the verified null sink is admitted, return codes propagate, precompilation is
single-CPU, and file retries are off. Two earlier zero-test harness failures are
not passes. This does not establish OS-wide isolation, production adoption or
measured token/cache savings. Desktop loopback and live goal acceptance remain
blocked/unproven. See [memo boundaries](goal-judge-memo.md#preserve-timestamp-evidence-v0850).

The companion suite runs 120 tests: 118 pass and two Linux-only cases skip. The
tracked-only disposable 222-file package passes release verification. The exported
patch passes installed verification, reverse-to-base verification and reapply/
installed readback for all 993 targets; its reapplied native memo regression
passes 21 cases again. Existing test selection already includes the changed file.
Historical patch artifacts and the native base pin remain unchanged.

# v0.8.49 — Isolate report retention failures

Known report-validation errors escaped the retention apply loop, aborting later
work. A real synthetic linked-report reproduction preserved its source but left
the following valid report unpacked. The per-entry handler now records these
failures and continues, retaining exit status 1 and all archive/process guards.

Two new regressions exercise CLI parsing/main, real filesystem archives and the
actual verifier. Initial runs expose five unhandled cases; an appended corrupt
gzip member separately exposes raw `zlib.error`. All six cases now preserve the
rejected report, leave no temporary/destination archive for it, and complete a
later valid archive with exact payload equality. The linked target stays intact.
Existing mutation, visibility, ownership, protection and preview checks remain.

The full companion suite passes 120 tests with two Linux process-observation
skips, and the tracked-only 222-file release inventory passes. An unmodified CLI
process launched from a temporary directory retains the synthetic report when
this Mac sandbox cannot observe processes; no guard override is used in that
check. It proves conservative refusal, not successful production cleanup.

This is companion-only offline acceptance with controlled process observations,
not a native Hermes runtime test, production purge or measured disk saving. No
owner home, timer, pause/ESTOP, installed source or dependency environment changed.
Native patch artifacts and the 993-target source selection are unchanged. See
[storage safeguards](storage-and-backups.md#report-validation-failures-v0849).

# v0.8.48 — Explicit patch manifests in the offline doctor

The doctor previously accepted only the historical cumulative-kit manifest. Its
new optional `--manifest` and API argument reuse the existing strict checkout
verifier, preserving the historical default. Base/installed CLI regressions first
failed on the missing option; they now pass. Wrong revisions/hashes, malformed or
missing manifests, and a manifest without a checkout remain failures without
echoing rejected paths or content.

On this Mac, the correctly applied 993-target v0.22.5 source is refused under the
historical pin and passes with the explicit stable-full pin. Its Git status is
unchanged; `executed` remains false and runtime readiness remains unknown. Native
patch artifacts and test selection are unchanged.

An installed-Desktop journey stopped at loopback preflight (`listen EPERM`) before
any app/backend launch. No binding workaround, owner-state change, provider work,
pause/ESTOP or timer change was attempted. No new Desktop or runtime acceptance is
claimed. See [manifest selection](offline-setup-tools.md#select-the-matching-patch-manifest-v0848).

# v0.8.47 — PM-managed Mac install/update compatibility

The old Mac recipe's in-tree venv is absent on this real PM-managed installation.
Native PM metadata resolves its committed dependency interpreter read-only. Two
fresh v0.22.5 trial checkouts accept the v0.8.37 and current kit patches with 983
and 993 exact installed hashes. The reusable native assertion fixture seeds under
the older source, reads under the newer source, then reopens under the old source
without rewinding the database. Synthetic settings, profile and older multilingual
search content remain intact; watched bytes match. Invalid committed selection,
missing-session reads, seed replay and bare-store-Python guards are exercised.

The OS sandbox preflight was refused. Self-tested Python audit guards denied
processes, sockets and forbidden Python file operations before trusted dependency
and native imports. Denied optional metadata/capability probes degraded version
text; source hashes are the identity evidence. This is guarded synthetic native
compatibility, not complete OS/network isolation, installed Desktop activation,
provider/goal judging, Linux runtime adoption or a performance gain. All native
patch artifacts and dependencies are unchanged. See the
[exact Mac scope and limitations](macos-install-update.md#managed-runtime-acceptance-v0847).

The companion suite passes 115 tests with two Linux-only skips. Two new admission
tests reject missing/invalid markers and mismatched homes before native imports,
preserving synthetic owner-like state. A tracked-only export of the intended
public tree passes all 222 inventory rows. An independent temporary index includes
the two reviewed new fixtures before driver staging; the real index stays untouched.
Both documented Gitleaks 8.30.1 scans pass with no leaks reported, including the
existing 177-commit history. No full native pytest suite or production test is claimed.

# v0.8.46 — Release history fsmonitor fence and accurate judge evidence

A real marker-writing Git fsmonitor hook runs during the old release history
check. The regression fails on v0.8.44 and passes after disabling fsmonitor
for the status invocation. All 22 release-tool cases pass, including clean CLI
acceptance, dirty-tree refusal with matching inventory hashes, and non-neutral
history on another branch. The complete companion suite runs 113 tests with two
Linux-only skips and no failures on macOS.

The live-card record previously said no judge call ran, despite its two recorded
`continue` verdicts. Its open item now states the actual evidence gap: those
verdicts do not establish an identical-input repeat returning a stored verdict
without another judge call. No new live run, verdict, request allowance or
terminal state is claimed. Live `done`, terminal goal state, memo reuse and
production adoption remain unproven. See [the open items](live-captain-cards-20261109.md#what-remains-unproven).

The exact release inventory passes for all 220 public files in a disposable copy
of tracked working-tree bytes. The original directory still refuses local ignored
files and operational notes. Package-copy verification does not establish original
directory cleanliness or history safety. The documented Gitleaks 8.30.1 directory
and all-history scans pass with no leaks reported (176 commits scanned).
Native source patches/manifests and test selection are unchanged. No native Hermes
suite, provider, service or live Captain test was used. See
[history-check scope](privacy-review.md#read-only-history-check-v0846).

These changes form one v0.8.46 delivery. v0.8.45 was an unpublished preparation
step, not a separate release. No push or publication was performed in this round.

# v0.8.44 — Second live judge verdict

On card t_d1f9e350 the live goal judge rejected a finished card for violating the
goal's own "do not reread" rule, which contradicted its Verification line. The
cumulative count is 56/56 requests. No code change. See
[the live cards](live-captain-cards-20261109.md#after-the-owner-raised-the-ceiling-to-56).

# v0.8.43 — v0.8.42 installed on the Mac

The four v0.8.42 files are installed in the Mac checkout, and their SHA-256 values
match Linux. On ARM64 macOS the new kick-contract case and 52 other goal cases pass
in a temporary pytest environment, which was removed afterwards. Two
`test_surface_goal_state_matches_cli[...-gateway]` cases fail in that run. Run alone
on the unchanged base, the same test fails all 60 of its cases. The cause is that
this checkout sits inside the real `~/.hermes`, so importing `cli` trips the
`home_io_guard` test fixture; the v0.8.42 change does not cause it. The
tui_gateway setup errors also occur on the base in that environment. No code change.

# v0.8.42 — First /goal turn sees its contract and evidence rule

The new case fails on v0.8.41. 99 goal-dispatch, kick and TUI goal cases pass, and
498 cases pass across 40 goal-related files. The 7 remaining failures are the 2
gateway kickoff timing cases, which also fail on the base commit, and 5 assertions
that compared the kick prompt to the bare headline (updated). The patch is
installed in the live Linux checkout. The Mac is held, by host agreement with
another session. On the live card the reply carried the requested evidence, but the
judge call did not fit inside the 48-request ceiling.

# v0.8.41 — Live Captain card evidence

The owner `/goal` path, a delegated wording choice, the card comment and the card
completion are now proven on isolated live cards. The goal judge verdict is not
proven, because the 32-request ceiling is fully used. See
[the three live cards](live-captain-cards-20261109.md).

# v0.8.40 — Documentation correction

The TUI in a git-checkout install rebuilds from source on launch. Only the web
dashboard bundle needs a manual build. No code change.

# v0.8.39 — TUI agents panel shows tool and step

1,882 TUI cases pass. The new case fails on v0.8.38. The patch verifies 989 targets
on clean v0.22.5. The source files match on Linux and Mac. The TUI rebuilds itself
from the newer source on its next launch. Correction in v0.8.40: an earlier note said
it needed a manual build.

# v0.8.38 — Tables on the web dashboard, honest TUI rendering hint

Three new cases fail on v0.8.37 and pass now. 452 web cases and 97 prompt and
hint cases pass on Linux. The patch verifies 986 targets on clean v0.22.5. Source
is installed on Linux and Mac with matching hashes. The installed web bundle has
not been rebuilt yet. See [chat rendering surfaces](chat-rendering-surfaces.md).

# v0.8.37 — Reuse the goal-judge verdict for an identical input

One new case fails on v0.8.36 and passes now. 494 cases in 35 goal and judge test
files pass on Linux, and 57 cases in 5 files pass on ARM64 macOS. The patch applies
to clean v0.22.5 and verifies 983 targets. The installed Linux and Mac files match.
See [the memo's scope and limits](goal-judge-memo.md).

# v0.8.36 — Retention parity on macOS

A new lsof-path test fails on v0.8.35 and passes now; all 24 retention tests pass on
Linux, and on ARM64 macOS with two Linux-only skips. Linux and Mac hold helpers with
the same SHA-256. A 50-second Linux sample found `ping` as the only transient closed
process besides the listed session daemons.

# v0.8.35 — Retention runs on hosts with SSH and user systemd

Four new retention tests fail on v0.8.34 and pass now: a real non-dumpable child
named `gpg-agent` no longer disables observation, while an unknown closed process
still does; a stuck entry no longer abandons the plan; another user's tree is kept;
inner links are removed without touching their targets. All 23 retention tests pass.
On the Linux host, the preview went from `remove=0 keep=298` to a working plan. The
installed purge dry-run exits 0. Hermes home dropped from 43 GB to 34 GB.

# v0.8.34 — Exact goal ensure usage in the Captain skill

An isolated Captain card (private home, counted relay, 1 GiB cgroup, no Linux GPU,
production closed) proved native skill discovery, exact installed skill read,
card read and `hermes goal status`, then stopped when the model called
`hermes goal ensure --outcome ... --verification ...`. Those flags do not exist,
so the skill now gives the literal heredoc form. Five physical requests were used
(23 of the owner's 32). Goal creation, card completion and the goal judge remain
unproven live. Native source and patch bytes are unchanged.

# v0.8.33 — Native checks and bounded test imports

All twelve native blocking check groups pass on Linux, resolving 41 Ruff and nine
ownership/platform findings without new checker suppressions. A shared live UID
fact retains numeric ownership checks. The Desktop control fixture keeps normal
module caching; its full 33 cases pass at 286.6 MiB, while an isolated old-fixture
control crosses the unchanged 768 MiB guard.

Linux passes 497 native cases across separate complete-file runs; ARM64 macOS
passes 496 with two host skips in one 33-file run. The reviewed fifteen runtime
and eighteen test files are installed on both hosts, with 980 pinned source paths.
The Mac resumed segment preserves original access metadata, records OS-added
provenance, and uses a fault-tested pending journal; the first segment's protected
end-hash comparison is explicitly unavailable. One real-Gateway fixture remains
not run. No new real card/model request or production activation occurred. See
[the complete evidence and limits](native-checks-and-test-memory.md).

# v0.8.32 — Read UTF-8 state with optional BOMs

Seven readers accept valid UTF-8 state with an optional BOM, including quota
snapshots, attention policy, update capsules and owned daemon PIDs. Native quota
refresh preserves unrelated adapter observations. Five complete affected files
pass 29 cases and five updater regression files pass 43 cases on Linux and
ARM64 macOS. The Mac updater check required a narrow test-policy exception for
the native read-only process observer; the original failed run is retained.

The reviewed five runtime and five test files are installed on both hosts. The
complete kit now pins 978 paths, including two new regression files. Native code
health has zero new findings; full native static checks retain 41 existing Ruff
and nine ownership/platform findings. No new real card/model request or service
activation occurred. See [the exact tests, resource limits and remaining
acceptance scope](utf8-state-files.md).

# v0.8.31 — Isolate the auxiliary refresh fixture

The existing OAuth refresh fixture now uses its own Claude Code configuration
directory before cache-key calculation, retaining real locking and every
refresh/write/cache assertion. Its original failure reproduces on Linux and
ARM64 macOS with protected real homes. Three complete native files pass 245
tests on each host after repair, in matching isolated checkouts with separate
test environments and no networking, model requests or Linux GPU devices.
The reviewed test is installed on both hosts; the 976-path kit changes only
that test's after hash. Runtime authentication code and Desktop builds are
unchanged. The clone walkthrough now pins this release.

The changed fixture passes pinned Ruff and code health. Full native checks
retain 41 existing Ruff findings and 16 Windows-footgun findings; this release
does not claim global native-suite or static-check success. See [the fixture
scope, resource observations and remaining checks](auxiliary-refresh-test-isolation.md).

# v0.8.30 — Clarify native verification scope

The compact-worker guide distinguishes the matching isolated Linux checkout
from the installed macOS source; both native compatibility runs used separately
managed test environments. It also separates temporary configuration-test
profiles from the existing Captain profiles, whose configuration was not changed.
The v0.8.29 native test, live-card and installation results remain historical;
they are not relabelled as rerun. Runtime patches, skill assets, the fragment and
the native verifier are unchanged. All 104 companion tests pass for this wording
update, and the exact release inventory and secret scans are checked again.

# v0.8.29 — Optional compact card-worker schemas

An on-demand skill reference and explicit native configuration fragment keep
eight lifecycle/recall tools direct and defer six additional Kanban schemas
for a fresh dedicated worker. Native profile/config/tool assembly and wire
serialization checks pass two cases each on Linux and ARM64 macOS, without
network access, Gateway startup or model requests. The 976-path native kit is
unchanged.

The complete four-file skill is installed and passes the copy doctor and native
resolution checks for the existing main and named Captain on each host. File
metadata, unrelated profile state and existing permissions are preserved; the
optional fragment is not applied to a live profile. Installation and offline
guidance checks do not establish use by a cached Captain.

One completed simple-card pair used two physical requests per card. Total input,
including cached input, fell from 21,242 to 16,734 tokens (21.22%); wire schema
bytes fell 35.65%. Both returned the same result. Four authorized extra card
slots are consumed: two earlier controls stopped before a model request and
were retained without replay. The cumulative count is 17 physical requests
against the original 32-request ceiling. All production and test Gateways are
closed and no Linux GPU was exposed.

This single pair does not establish general quality, better cache use, lower
RAM, lower latency or live Captain adoption. See [the complete measured scope,
native recipe and limitations](compact-worker-schemas.md).

# v0.8.28 — Official Codex alias usage

Official Codex routes configured through a custom alias now use the existing
subscription-included pricing path without optional model-catalog reads. The
five accepted-route regressions failed before repair; nine connected native
files pass 109 tests. Linux and Mac installed interpreters each pass 13 direct
routing controls with zero catalog attempts. The complete 976-path kit passes
exact reverse/base/forward/installed checks and installed compatibility on both
hosts. The production Gateways remain closed, with account/configuration/saved
state retained.

The bounded live batch created eight cards: six completed and two earlier
failures were retained without replay. All 13 physical model requests, including
the one in a failed card, count against the 32-request cap. The successful runs
reconcile full body consumption, native task/run/session usage and observed
client exit. No Linux GPU was exposed. The matched layout comparison reported
46.92% cache read for both layouts; neither cache improvement nor general
latency causality is established. See [the measured scope and failures](codex-alias-usage.md).

# v0.8.27 — Check complete Captain skill copies

The offline doctor compares an explicit installed skill directory with every
published supporting file. Four regressions and all 104 companion tests pass.
Linux/ARM64 Mac native discovery, per-profile goal flags, saved goals and the
two-file skill are verified for the intended main and named Captain. Both
Gateways stay closed; no model, GPU or card dispatch is used. Runtime source
and Desktop builds are unchanged. See [scope and installation checks](captain-skill-installation.md).

# v0.8.19 — Stop after scheduled and revision handoffs

Four regressions failed before repair; 473 related Python cases pass afterward.
A fresh native scheduled-card pair used three requests instead of four and stayed
parked on the next dispatch check. Linux/Mac source matches all 957 paths; eight
offline native Mac checks cover successful and foreign handoff proof. See
[scope and token measurements](scheduled-review-handoffs.md).

# v0.8.18 — Avoid discarded recall payloads

One regression failed before repair; 214 related Python tests pass afterward.
Native Linux/Mac comparisons retain byte-identical answers while loading 19
payload rows instead of 51 in the adaptive fixture. A fresh simple Linux card
recovered all three saved codes in three model requests with 19 payload rows.
All 956 source paths match on both hosts. See [scope and measurements](adaptive-recall-hydration.md).

# v0.8.17 — Stop after a verified blocked handoff

Two regressions failed before repair; 383 related Python tests pass afterward.
A fresh native two-stage card used four model requests instead of five and
recovered its saved checkpoint correctly. All 955 source paths match on Linux
and ARM64 Mac; 12 offline native Mac checks pass. No GPU or production queue was
used. See [the acceptance scope and limits](blocked-worker-handoff.md).

# v0.8.16 — Preserve config type-change order

Eight new regressions failed before repair; 38 related tests pass after repair.
Fourteen actual-queue/native-storage comparisons pass on Linux and ARM64 Mac.
Unsafe type transitions retain two ordered config requests, while compatible
controls still coalesce into one. Both native packages were rebuilt and installed,
with 954-path source parity and package/source fingerprint checks. No model or GPU
work was used for the behavior checks. See [scope and limits](settings-null-sections.md#ordered-type-changes-v0816).

# v0.8.15 — Preserve edits followed by null sections

Two new regressions failed before repair; 30 related UI/Electron tests pass after
repair. The actual queue's coalesced patches now match sequential writes through
native config storage on Linux and ARM64 Mac. Both packages were rebuilt and
installed, with 953-path source parity and package/source fingerprint checks.
These offline behavior checks made no model requests and used no GPU. See
[the null-section contract and limits](settings-null-sections.md).

# v0.8.14 — Scoped recall tool preparation

An optional native config fragment makes the search schema eager for a selected
recall profile. One isolated pair of simple cards both recovered the correct saved
answer: four requests with default discovery, three with eager search. Total input
fell 21.1%, but uncached input only 1.7%; no general latency or billing saving is
claimed. Offline native setter, readback, scope and rollback checks make no model
requests. See [the recipe and evidence boundaries](recall-tool-policy.md).
The 952-path runtime kit is unchanged.

# v0.8.13 — Actionable settings write failures

Known permission, read-only filesystem and storage/quota failures return safe
recovery guidance. A post-replacement failure does not claim that the file stayed
unchanged. The native Python selection passes 226 tests; installed Linux failure
injection confirms the new message, retained edit, held close and successful retry.
The 952-path kit includes the backend change and regression tests. See
[scope and limits](settings-write-errors.md).

# v0.8.12 — Preserve settings edits across navigation and close

The native main process owns pending shared-config edits and ordered saves.
Seventy-two UI/Electron tests and installed Linux Escape/reload/close/quit checks
pass. The 950-path source kit and native Linux/ARM64 Mac packages were installed
before publication. See [settings autosave](settings-autosave.md).

# v0.8.11 — Accessible shared settings controls

Shared settings inputs and pickers now use their existing localized field titles
as accessible names. The six-file selection passes 33 tests, with renderer types,
scoped lint and source health clean. Native Linux and ARM64 Mac packages were
installed before publication. Linux Desktop named-field editing and saved-value
reload pass in an isolated home without GPU devices or model calls. Immediate
reload before the existing autosave debounce can still discard pending edits.
See [scope and the remaining save limitation](settings-accessibility.md).

Fresh-process token-memo measurements also confirm lower retained RSS for the
controlled workload; they do not establish production Gateway savings. See
[the RAM measurement](token-memo-memory.md#fresh-process-rss-follow-up).

# v0.8.10 — Native Desktop and saved recall acceptance

Evidence-only release: installed Linux Desktop navigation and stored rich output
passed at 1280/640 pixels without GPU devices or model calls. A separate simple
native recall card recovered an answer absent from its prompt and completed in
16 seconds using four cloud requests, with 68.7% observed cache-read input. One
earlier fixture failed and used four additional requests. Same-result offline
query replay read 20 payload rows from the 256-message archive. No whole-system
savings claim is made. See [the complete scope and limits](native-desktop-recall-acceptance.md).

# v0.8.9 — Forward unified worker progress

Both unified roster paths now carry step, elapsed-time inputs, usage and stored
terminal state. Two regressions failed before repair; 36 related tests pass after
repair. Native checks and 919-path source parity pass on Linux and ARM64 Mac.
Three isolated simple cards completed using four physical cloud requests, with
GPU devices unavailable to the test processes. Actual rich-output and monitor
components render the observed data at three widths. Full Desktop navigation and
running production-Gateway adoption remain unverified. See [scope and evidence](unified-worker-progress.md).

# v0.8.8 — Bound retained token-estimate memo memory

The token memo now caps retained key/value objects at 32 MiB and keeps the existing
4,096-entry ceiling. Two tests reproduce the preceding retention problem; 143 tests
across eight related files pass after repair. Nine overlapping tests pass against
installed Linux source. Native production-Python checks preserve estimates, warm
reuse and lifecycle release on both AI and ARM64 Mac without a model call.
The 918-path kit matches both hosts; source health, companion checks and patch
apply/reverse/reapply pass. Existing Gateway processes are preserved. See [measurements and limits](token-memo-memory.md).

# v0.8.7 — Make offline vision routing checks deterministic

The v0.8.6 adjacent failure was an unseeded catalog assumption: the test expected
known text-only metadata in a clean offline home where capability was unknown.
The replacement supplies synthetic raw catalog entries and verifies rejection of
known text-only models plus acceptance of vision and unknown models. Runtime policy
is unchanged. Both permissive and restrictive gate mutations are caught.

The combined vision/cache selection passes 147 tests across thirteen files. A
separate capability selection passes 65 overlapping tests; the installed Linux
routing file passes eleven. Installed production Python on Linux and ARM64 Mac
each passes three offline catalog/route checks. Source health, scoped lint and
companion tests pass; the 916-path kit matches both hosts. No real inference or
worker execution ran. See [the verification boundary](vision-routing-verification.md).

# v0.8.6 — Keep vision cache reuse within the selected connection

The repaired direct and registered auxiliary-image paths retain separate successful
results after endpoint/API/authentication mode changes. Thirteen new regressions
fail on the original code; the final focused selection passes 32 tests, including
concurrent contexts. The adjacent selection passes 112 tests with one reproduced
pre-existing vision-routing failure, named in [the detailed record](vision-cache-routes.md).
Scoped lint and source health pass; no full-suite success is claimed.

Installed production Python on Linux and ARM64 Mac each passes twelve offline native
checks, and the 915-path source kit matches both hosts. Existing UI packages, Gateway
identity and owner stops are preserved. No GPU, real model, worker launch, dispatch,
session resume or service restart is used. Runtime adoption and live card acceptance
remain open.

# v0.8.5 — Keep worker progress readable

The prior component fails the tooltip regression and clips progress facts in an
offline browser fixture at three row widths. The repaired selection passes 62 UI
tests, renderer TypeScript, scoped lint and source health. The actual component and
installed CSS keep step, elapsed and token facts inside the row at all three sizes.
See [worker monitor readability](worker-monitor-readability.md) for the exact scope.

Linux and ARM64 Mac source match the 914-path kit. Both Desktop packages are rebuilt
and installed, including the Mac Finder copy; packaged frontend assets match their
compiled output. No app was launched and no worker ran. A small test card remains
blocked without an assignee, session or run, and owner stops remain intact.
Original-session adoption and live-worker behavior are not yet verified.

# v0.8.4 — Bound retained search memo memory

Five regressions fail on the prior source. The repaired search/cache selection passes
75 tests; a separate web/provider/storage selection passes 332 tests. Scoped lint and
source-health checks pass. Actual installed Linux and macOS source and production
Python each pass four offline native checks, including registry dispatch to an evicted
result's real disk copy without a provider call. Configuration, owner stops, and Gateway
process state remain unchanged. No GPU, inference, dispatch, or service restart is used.

An isolated 512-query fixture retains 72,212,954 traced Python bytes before the fix and
33,623,906 afterwards (about 53% less). After expiry and a lookup of an unseen query,
retention changes from 512 entries to zero; the repaired trace is 46,032 bytes. These
are fixture allocations, not deployed process RSS or a promise of request/latency savings.
See [search cache memory](search-cache-memory.md) for conditions and tradeoffs.

# v0.8.3 — Attribute post-turn goal judge usage

The current pre-repair source fails five ownership regressions. The focused accounting
selection passes 10 tests after the repair; a separate adjacent selection passes 142 tests.
Scoped lint and source health pass. Actual installed Linux and macOS source and production
Python each pass four offline native checks with real stores and fixed SDK response fixtures.
These checks deny network access and GPU access; they do not start production worker jobs.

The 912-path kit is installed with matching payloads on both hosts. Configuration and owner
pauses are preserved, and existing Gateway processes are not restarted. A small native smoke
card is parked without a worker/run; live provider acceptance and original-process adoption
remain unverified. No new performance or usage savings are claimed. See [the accounting
record](goal-usage-accounting.md) for scope, fixture counts and limitations.

# v0.8.2 — Retain in-use data and verify report archives

The companion retention helper repairs protected-descendant handling, stale planning
observations, incomplete process visibility, and report archive verification. New
regressions failed before their corresponding repairs. The full companion suite passes
100 tests on Linux. Native macOS retention tests pass 18 tests and skip one Linux-only
process-observation case. These are CPU-only temporary-directory tests; no GPU or model
inference is involved.

Matching helper bytes were installed on both hosts before publication. The Linux
scheduled wrapper's read-only preview exits with an explicit incomplete-process-visibility
result before any cleanup. No production data was removed, and no disk, latency, RAM or
model-usage savings are claimed for this release. A small native test card was created
and read back in blocked state with no worker/run; its execution is not yet verified.
The owner's emergency stop was preserved. Earlier live UX and dispatch gaps below
remain open. The upstream source kit and Desktop builds are unchanged by this release.

# v0.8.1 — Usability fixes from a live walkthrough

The packaged Desktop was driven with Playwright under a virtual display against the
owner's real Hermes home (no settings saved, no cards created). The walkthrough found the
problems listed in the [kit notes](stable-full-kit.md#usability-update-from-a-user-walkthrough-v081);
each fix was reviewed independently. The full Desktop Vitest suite passes (1,784 files,
15,471 tests), the TypeScript checks pass, and the focused Python checks pass. The kit now
covers 909 paths and was applied to the idle Linux and macOS installations, with the
Gateway restarted and both Desktop packages rebuilt.

Not verified live: rich chart/mermaid answers, the live bot progress line and THINK/ACTION
dispatch. The owner's fleet was deliberately paused during this release, so no model turn
or Kanban dispatch ran; those features rely on their offline tests. Kanban run durations
were confirmed on real historical runs.

# v0.8.0 — Efficiency, monitoring and delegated goals

This release regenerates the consolidated stable kit (now 877 paths) for upstream
v0.22.5. It was built in a separate development checkout, tested there, applied to the
owner's idle Linux installation, and the Gateway and packaged Desktop were rebuilt and
restarted only after the board showed no running or claimed work.

Offline evidence:

- Python: the recorded selection plus the new tests (1469 files) ran with 10 workers:
  13,660 passed. Every remaining failure also fails on an untouched copy of the previous
  baseline or passes when re-run alone. The baseline-only failures come from the test
  host (a live-home I/O guard and a checkout-local `.hermes/bin` path), not from product
  code. Two gateway files that spawn live processes failed only while another suite was
  running; both pass alone.
- Five previously failing baseline checks now pass: two prompt-assembly tests were updated
  to read the context tier where Legion places the platform hint; the committed prompt
  snapshot was regenerated in a temporary home; and two conversation-loop tests exposed a
  real defect, where a failed price lookup re-sent a delivered response. Price lookup
  failures now record an unknown cost.
- Desktop: the full Vitest suite passes (1,780 files, 15,454 tests). Eight files that failed on the baseline now pass. Two were product bugs
  (a stale remembered route survived the settled disk scan; two buttons used native
  `title=`); the rest were tests whose storage spies never took effect under jsdom or
  that predated intentional scoped session opening and plugin i18n. TypeScript checks and
  the native build pass.
- The Kanban SIGKILL end-to-end scenario no longer needs its two known-gap allowances
  (#121255, #119618) after the per-attempt start marker.

Operational evidence on the owner's host (not a performance claim for other fleets):
retention of aged scratch, superseded backups/runtimes and packed reports reduced the
Hermes home from about 83 GB to 48.5 GB. Per-workload token or latency savings from the
caches and compact views are not yet measured and are not claimed here.

# v0.7.43 — Preserve auxiliary cache usage and account for Claude calls

Native Codex and Anthropic auxiliary adapters projected provider usage onto Chat Completions but dropped cache-read, cache-write and reasoning details. Anthropic prompt totals also omitted its separately reported cache buckets. The ambient auxiliary accountant then interpreted that already-converted result as native Anthropic usage, losing ordinary counters or dropping a fully cached call.

Both adapters now share the existing canonical usage normalizer and emit the Chat Completions detail fields their existing hooks consume. Session accounting reads that chat-shaped result independently of the billing-provider label; billing routes remain unchanged. Reported reasoning stays a subset of output, not an additional total. Fully cached calls still count once. Excluded MoA tasks remain excluded to avoid double accounting.

Six regressions fail before the repair. The main offline selection passes four files and 50 cases; the separate adapter/effort/pricing integration selection passes three files and 309 cases, without failures or retries. Source health has no new findings. Scoped Ruff is clean outside the large existing auxiliary-client file, whose single unrelated unused-noqa finding is identical before and after and is not suppressed.

Actual installed production Python on Linux and macOS each passes six native checks with the real installed OpenAI ResponseUsage and Anthropic Usage types, native adapters, hooks and a temporary SessionDB. The provider-response boundary supplies fixed offline responses; remote pricing lookup returns unknown. No provider inference or pricing request is made. Answer content, completion gates, source payloads, billing-provider labels and one-attempt behavior remain intact.

For a hand-checked Codex fixture, 100 prompt tokens comprise 30 uncached, 60 cache-read and 10 cache-write tokens; 20 output tokens include seven reasoning tokens. A Claude fixture retains 100 uncached, 80 cache-read and 40 cache-write tokens, so its prompt total is 220 rather than 100. A completely cached 100-token call is retained with one call count. These are accounting examples, not newly measured provider cache hits or usage savings.

A read-only audit of an already completed private graph finds 39 physical requests and 34 recorded session calls. This repair does not prove the cause of those five missing historical records and cannot reconstruct discarded provider cache details. Old zeros are not evidence of cache misses. Displayed usage can rise as previously omitted reported buckets are counted; that does not itself mean more requests. No past usage row is backfilled or repriced.

Five reviewed source/test paths were installed on both hosts before publication, with exact file metadata restoration and target-only rollback. The full 843-path source kit passes native apply/reverse/reapply and installed-parity checks on both hosts, except for one pre-existing private Python comment with an equivalent parsed syntax tree. The accepted native Desktop images are unchanged because no renderer runtime changes. Original Gateways and workers are not restarted; cached original-process adoption remains separate.

No prompt, tool/schema, model, reasoning setting, quota, dependency, account, cache policy or paid fallback is changed. All new checks use zero model calls. The English source artifact excludes private conversations, live boards, screenshots, credentials and private Git history.

---

# v0.7.42 — Bound import-free plugin source reads

Entry-point and directory plugin classification looked at only the first 8,192 characters but read and decoded the entire Python file before taking that slice. Both paths now use the existing source reader with a bounded text read. No source code is imported or executed during classification.

Plugin kind, explicit overrides, the detection-window boundary, UTF-8 BOM handling, invalid-byte replacement, universal newlines, cached-source resolution, missing-file behavior and existing slicing semantics are preserved. No manifest cache, tool/schema, prompt prefix, model, quota, dependency, database or paid fallback is changed.

Two real-file resource regressions fail before the repair. The main offline selection passes four files and 95 cases; the separate discovery/registration/launcher integration selection passes four files and 105 cases, with zero failures or retries. Scoped Ruff and source health pass. Native acceptance against the actual installed source and production Python passes six checks on each of Linux and macOS. Four actual bundled manifest projections also match before and after, with their source files unchanged. These are scoped checks, not a universal suite result.

A matched, warmed native classification benchmark uses a 4,194,370-byte synthetic source and five samples per path. Directory classification median traced Python allocation peak falls from 8,524,553 to 152,573 bytes; median operation time changes from 2.644 to 0.209 milliseconds. Entry-point classification changes from 8,524,058 to 151,039 bytes and 2.431 to 0.114 milliseconds. The inspected source window remains 8,192 characters and the classification is unchanged. This measures the fixed large-file fixture, not process RSS, overall production startup, model usage or typical small-plugin speed.

Two reviewed source/test paths were installed locally on both hosts before publication, with target-only rollback and exact file metadata restoration. The full 839-path kit passes native apply/reverse/reapply and installed-parity checks on both hosts; the sole non-byte-identical path is an existing private Python comment with the same parsed syntax tree. The accepted native Desktop images remain unchanged because this repair changes Python metadata reads only. Original Gateway processes and workers are not restarted, and cached original-process adoption is not inferred.

All new tests and measurements make zero model calls. Existing stop, profile, project, provider and quota gates remain unchanged. This source release contains English guides and neutral templates, with no private conversations, live boards, credentials, screenshots or private Git history.

---

# v0.7.41 — Clear compact-window navigation

Fix a real CSS cascade defect that made short navigation words break inside the word at a 320-pixel window width. The normal spacing rule now comes before the existing narrow-window override. No new state, request, dependency or navigation route is added.

The native regression failed before the repair and passes after it. The related Desktop selection passes eight files and 36 tests; the separate native E2E selection passes one test. Scoped lint and all three TypeScript projects pass. These are separate selections, not a universal test total.

The actual installed Linux app and both installed macOS launch locations each pass nine native interaction checks at widths of 900, 580 and 320 pixels: short labels, Settings through All features, retained-chat history and scoped roster synchronization. Both native package builds pass; the Mac image passes strict local signature verification. Mac signing is local ad-hoc signing, not notarization. All new UI tests use private synthetic homes and make zero provider inference requests.

The full 838-path source kit passes native apply/reverse/reapply checks on both hosts. Source parity is exact except for one pre-existing private Python comment whose parsed syntax tree matches. No original Gateway or worker is restarted, no screen is unlocked, and original emergency-stop, project, provider and quota gates remain unchanged. No paid fallback or model call is added. Original-user adoption and causal production RAM, usage, cache or latency gains are not claimed.

This release contains source patches, English guides and neutral templates, not private accounts, chat histories, live boards, screenshots or prebuilt application images.

---

# v0.7.40 — Read only the visible Kanban history window

`kanban_show` compact and summary views previously fetched every comment, event and run from SQLite, decoded the entire run metadata history, and only then discarded older entries. Long-lived cards paid this memory and latency cost even for a short status reply.

The read path now fetches only the existing visible history window through the existing task indexes. Counts and recent rows share a read snapshot that also works on a read-only board and preserves an outer transaction. Comment clipping, ordering (including equal timestamps), latest-event window, heartbeat filtering, total counts, evidence metadata and explicit `full=true` behavior are unchanged. No database migration, new index, tool/schema, prompt, model, quota, cache policy, dependency or paid fallback is introduced.

## Verification and measurements

Two registry/SQLite resource regressions failed before the repair. The final related selection passed 12 files and 117 tests with zero failures or retries, covering compact/summary/full output, read-only nested transactions, descendant scope, redaction, output budgets, unknown fields, parent completion fences and unchanged request diagnostics. Scoped lint and source health pass. The same five native acceptance checks pass against actual installed source on Linux and macOS using their existing production Python.

A matched native registry benchmark used 2,000 synthetic entries in each history table and five samples per mode. Compact reads materialized 65 history rows instead of 6,001. Median traced Python allocation peak fell from 52,658,868 to 229,767 bytes; median instrumented operation time fell from 70.628 to 1.818 milliseconds. Summary reads likewise retain their original output and total counts. These measurements describe that fixed fixture and Python allocations, not process RSS, a production daily workload, model token savings or universal UI latency.

All eight before/after payload comparisons match, including compact and summary reads of three genuinely completed prior private workflow cards. Those small real cards showed no meaningful speed gain and slightly more fixed bookkeeping; the repair targets scaling with long history. Existing board contents remained unchanged, and no model call was made by the new tests or measurements.

A separate analysis of an already completed provider-backed private graph found 34 main diagnostic records across five roles in one installation namespace, with all 19 worker records bound to their task/run. Main-call usage reported 552,925 input and 471,552 cached tokens (85.28%). Compatible analyst/ACTION requests match route, key, common-prefix, options and tools fingerprints in all 30 cross-role pairs. Declared-account evidence is unknown, and matching request fields plus cached tokens do not establish authenticated account identity or the server's cross-bot cache origin. Auxiliary usage is incomplete; this short synthetic window is not a matched 24-hour before/after comparison or causal usage-saving claim. Raw identifiers, request content and private records are not published.

Three reviewed source/test paths were installed locally on both hosts before publication, preserving existing private comments, file metadata and compact target-only rollback. Fresh installed-process acceptance is verified. Original Gateway processes and workers were not restarted; adoption inside an already cached original Gateway is not inferred. Existing Desktop packages remain the separately accepted v0.7.39 renderer, since this repair changes Python reads only. Existing stop/project/provider gates, quota settings and protected services remain unchanged.

---

# v0.7.39 — Durable drafts, bounded history and native bot controls

Accepted send settlement now preserves newer editor input. An earlier rejected or unconfirmed message remains separately recoverable in the existing bounded, owner-isolated store. Recovery is explicit, requires an empty matching editor and never sends. An unchanged manual retry retains its original submission identity; ambiguous delivery is never automatically replayed. Text survives reload; attachments remain memory-only and must be reattached after reload.

Input-history browsing retires inactive cursors instead of keeping every visited session. Shortened history cannot return undefined text. Losing history restores the original draft. A transient runtime replacement retains browsing only for the same explicit owner and durable conversation; changing owner or conversation retires the cursor.

Expanded rich-content viewers now expose an accessible name using the existing trigger label. Routed relay roster, outbox and reply controls consume their already-validated profile selector before strict payload checks. Cross-profile tickets, capability checks, retired-owner fences and unknown-field refusal remain intact. Generated workflow clients describe the requested effort and effective limit already emitted by the runtime; no model or limit is changed.

## Verification

The draft/history selection passed 39 files and 621 cases. The separate rich-content selection passed 22 files and 190 cases, and the native-control/generated-contract selection passed six files and 28 cases, all without failures or retries. These are separate scoped selections, not a combined universal test count.

The installed Linux app passed twelve draft/history interaction steps, including replay-gap reattachment, keyboard traversal, original-draft recovery, rejected-send conflict handling, reload and an explicit original-ID retry. The current installed Linux app and both current macOS launch locations then each passed a separate 17-step native selection: stored Markdown/table/code/math/Mermaid rendering, named diagram zoom and Escape, bot creation cancellation without an introduction, read-only effort metadata, actual dependency ancestry, Settings navigation/close/Escape and compact-window history. Scoped relay roster synchronization produced zero RPC refusals. The current Mac package passed all five native preparation/typecheck/stamp/build/package steps and local code-signature verification before installation. This is local ad-hoc signing, not notarization.

Both hosts received the full 835-path source cohort before publication. Native parity checks found 834 byte-identical paths and one pre-existing comment-only Python difference with an equivalent parsed syntax tree. Full native apply/reverse/reapply acceptance passed on both hosts. The 180-file companion inventory and 81 offline companion tests pass.

A five-sample native-Node microbenchmark of 1,000 synthetic session visits reduced retained inactive cursors from 1,000 to zero, serialized state from 46,891 to two bytes and median store-operation time from 106.526 to 0.971 milliseconds. This measures the store fixture, not process RSS, production latency or token savings.

A separate read-only native check retrieved an existing real maintenance conversation more than three weeks old through both session READ and exact-title DISCOVERY. Its two original messages and metadata remained unchanged. This proves stored retrieval, not autonomous long-interval Captain recall.

All new native UI checks used private synthetic homes with zero provider inference. The existing Mac memory floor was met without lowering it or stopping other applications. The screen was not unlocked; original Gateway processes and workers were not restarted. Original-user adoption, causal production usage/RAM/cache/latency gains and cross-bot cache sharing remain unproven. No account, provider, model, quota, dependency or paid fallback is added. Raw histories, private host/project identifiers, credentials and screenshots are excluded from the public artifact.

---

# v0.7.38: owner-safe history windows and composer drafts

Opening another profile's same-ID history could leave the first runtime bound
while changing its displayed owner. Separate windows also shared draft keys.
Explicit history owners are now checked before route or read-marker changes.
Conflicting owners open through the existing native window bridge; repeated
same-owner links focus the existing window. Original histories remain bound.

Draft text and retry identity use connection, profile, target profile and
session ownership. Debounce, teardown, reload, undo, prepared-image recovery,
SDK fallback and deferred send results retain the editor's captured owner.
Lineage/profile moves retain the source if destination storage fails. Storage
events and updates touch one key; retention scans occur when adding a saved
scope and never prune another owner's drafts. Unassigned legacy drafts stay
separate and require explicit recovery into an empty editor. No automatic
submission or model request is added. Attachments remain memory-only.

The final related UI selection passed **30 files /496 tests**, zero failures
and zero retries, with frozen source hashes checked before and after. The
native window-registry selection separately passed **one file /24 tests**.
Native TypeScript/build checks passed; scoped health has no findings. Lint
has zero errors and seven previously existing warnings. These selections
are separate evidence and are not a summed universal test count.

Both Linux and macOS received the exact 55-path combined history/draft
cohort before publication (47 paths in the latest draft change). Rebuilt,
installed native applications passed ten isolated interaction checkpoints on
each platform, including same-ID owner windows, draft isolation, reload,
reopen and duplicate-window prevention. Both Mac launch locations have the
same locally signed package; this is ad-hoc signing, not notarization. The
existing memory admission threshold was met without lowering it. The screen
was not unlocked and the original Mac Gateway was not started.

All fixtures use private synthetic homes with zero provider inference. No
original human session, real worker adoption, causal production usage, cache,
RAM or latency saving is inferred. No dependency, tool, RPC, quota, model,
provider or paid-fallback change is included. Raw histories, screenshots,
host details and credentials remain private.

---

# v0.7.37: session links keep their profile and source

A named-profile history link could resolve the correct title but open a
same-ID conversation from the default profile. Two navigation seams dropped
the owner: the reference click discarded its profile, then the shared tab
opener forwarded explicit routes only for Bot workspaces. Links now capture
the existing source resolver before asynchronous loading and pass their
profile through the existing tab-opening path. A legacy source keeps its
profile-only routing; no connection is invented. Unqualified links retain
their existing behavior. Tab metadata now matches the explicit owner before
reusing a cached row, so same-ID titles from another profile or connection
cannot suppress the existing bounded metadata lookup. No new RPC, tool, dependency, quota or fallback.

The installed native Linux application reproduces the wrong-profile result
before the repair using two separately owned, same-ID CLI histories in an
isolated home. Four real-store owner-routing regressions fail before the fix;
one ordinary-link control already passes. A further same-ID title case also
fails before the metadata repair; its five existing slice controls pass. The final related selection passes
twelve files / one hundred twenty-five tests without retries. Lint and native typechecking
pass. The replacement Linux image must pass the same native title-and-click
acceptance before installation and again after installation, with no model
inference and no original session/profile data used. These are private native
acceptance histories, not proof of original-user-window adoption.

Seven exact source paths are installed on Linux and macOS before publication,
with target-only rollback and original file metadata preserved. The Linux
renderer is rebuilt from native prepared inputs without external networking.
The macOS renderer remains pending under the already recorded resource hold;
this release does not repeat the refused build, lower its headroom gate,
unlock the screen or start the original Mac Gateway. Source parity and
renderer adoption remain separate claims. No production token, cache-hit,
RAM or latency reduction is inferred from this correctness fix. Raw histories,
host details, credentials, screenshots and personal data are not published.

---

# v0.7.36: usable session links inside quoted answers

An actual native recall reply returned a session reference as a JSON string.
The installed Desktop swallowed the closing quote into the session identifier,
so the link could not resolve its title or open the intended conversation.
The bare-reference matcher now stops at quote delimiters. Explicitly quoted
values with spaces, inline/fenced code, punctuation, profile boundaries and
normal session links retain their existing behavior. No new tool, prompt,
dependency, account, quota, model call or fallback is added by this fix.

Four quote regressions fail before the repair; nineteen controls already pass.
The related native UI selection passes six files / fifty-nine tests with no
retry, and the native Linux typecheck and offline prepared build pass. The
actual prior reply and new packaged UI are checked in an isolated home with
external network denied. A copied local-session receipt remains bound to its
original owner: it is not authorization to resume that session under a new
profile. The click-through control uses a new same-owner native CLI transcript
replaying the prior verification answer and a separate derived reply that links
to that control. Importing foreign local authority is not claimed as accepted. No owner
gate is weakened, and this is not original-user-window adoption.

Exact two-file source installation on Linux and macOS precedes publication,
with scoped rollback and original permissions preserved. The installed Linux image passes nine rendered checkpoints: actual JSON
reference resolution, same-owner click-through, native profile rename, overlay
dismissal, compact delete/cancel, target-only deletion and reload persistence.
The image was validated before installation; no model request was made by the UI
acceptance. Expected font/plugin-list fetches fail because external network is
deliberately denied; no application exception is observed. The existing macOS image is intentionally kept:
its build was refused before starting because available RAM was below the
existing six-GiB build headroom gate. No process was stopped to force a build,
and the locked Mac screen was not unlocked. macOS renderer adoption remains
pending; source parity is a separate verified claim.

A separate native provider-backed recall check used one fresh user prompt and
four physical requests, under a hard five-request cap. It recovered five exact
facts and the source reference from thirty-four messages of a genuinely
completed private test workflow, using two complementary history searches in
13.46 seconds. Observed main-call input was 20,747 tokens, including 11,648
reported cached tokens. These are one-case observations, not a causal production
before/after reduction, cross-bot cache-sharing proof or months-long retention.
The raw transcript, session identifiers, profile data, screenshots and private
host details are excluded from this repository.

---

# v0.7.35: faster ASCII history verification with unchanged matching

A large ASCII argument miss still called the Python character classifier once per
character even after the earlier positive-match optimization. Two native SQLite
resource regressions reproduce this unnecessary work through decoded and raw field
checks. The verifier now consumes bounded ASCII word/gap runs with a compiled
standard-library regex, preserving the exact existing ASCII letters/digits rule.
Non-ASCII chunks retain the native Unicode61 codepoint classifier and CJK boundary
handling. No extra index, database connection, dependency or model call is added.

Prefix matching, phrases across long punctuation/chunk boundaries, words split
between chunks, Unicode folding, complete character/UTF-8 byte metadata, binary
flags, suffix validation and loud deadlines remain checked. Token buffers retain
their original query-sized bounds; huge word runs are sliced only to that bound.
No full field hydration or matching-policy change is introduced.

The final related selection passes 241 files / 2316 tests,
zero failures, 16 existing skips and zero file retries with four
workers. Scoped source health and test Ruff pass; the existing runtime FURB167
alias warning is unchanged. Overlapping selections are not summed. Native production
Python on Linux and macOS each passes fifteen installed controls, including real
registry discovery, decoded/raw negative work bounds, exact cross-chunk offsets,
prefix/late/malformed/deadline behavior and full Unicode/binary metadata.
Both hosts install the exact two paths with scoped rollback and metadata restored
before publication. Full-kit apply/reverse/reapply and installed parity are verified
on both hosts. Linux activation is native and idle-only; original Mac Gateway stays
off. No renderer, quota, model, account, tool schema or prompt-prefix change is made.

Four sequential uninstrumented ABBA component samples preserve boolean results:

| Synthetic case | Before, ms | After, ms |
|---|---|---|
| 500k-character ASCII word miss | 112.24 / 111.05 | 41.56 / 41.44 |
| 500k-character single ASCII word miss | 64.50 / 65.23 | 2.07 / 2.14 |
| 200k-character Unicode control miss | 78.70 / 68.56 | 74.53 / 70.12 |
| Early positive with 500k-character suffix | 2.09 / 1.97 | 2.01 / 1.99 |

These are small-sample component observations, not original-workload latency, RAM,
model-token or provider-cache evidence. The Unicode/positive controls establish no
general performance ranking. The earlier original Captain baseline timeout remains
a separate preserved condition; it has not been replayed, and candidate success
on that original query is not claimed. The broader Hermes objective stays active.

---

# v0.7.34: avoid redundant work after verified argument matches

Boolean tool-argument checks previously kept tokenizing or case-folding unrelated
suffixes after all requested terms were already found. A synthetic valid SQLite
tool-call fixture reproduces two excessive-work failures, one for Unicode61 tokens
and one for Thai substring matching. Candidate review also caught a raw-field path
that continued through the rest of its read chunk; matching now stops at the first
conclusive token boundary in that chunk as well.

The remaining decoded stream is still consumed and validated. Full character and
UTF-8 byte lengths and binary/surrogate flags remain correct for excerpts and
paging. An early positive match cannot hide invalid UTF-8 or malformed JSON later.
Missing terms, late matches, prefixes, phrases, multiple query terms, native CJK
semantics, caller transactions and deadline failures retain their contracts.
The same matching logic covers decoded argument fields and legacy native fields;
no full JSON hydration, higher deadline or extra model call is introduced.

Final related tests: 240 files / 2308 passed, zero failures,
16 existing skips, zero file retries and four workers. Scoped code
health and test Ruff pass. The runtime module retains its pre-existing FURB167
alias warning; no new lint finding is introduced. Overlapping suites are not summed.
Linux and macOS production Python each pass twelve installed native controls,
including actual registry discovery, negative/prefix/late results, invalid suffixes,
full Unicode metadata and expired deadlines. Both hosts install the exact two
paths with scoped rollback and restored permissions before publication. The full
consolidated patch is checked for apply/reverse/reapply and installed parity on
both hosts. Original models, quotas, resource gates and prompt/tool schemas stay.
Linux activation remains native and idle-only; original Mac Gateway stays off.

In one synthetic 500,000-character unrelated suffix fixture, instrumented ABBA
samples classify 500,056 characters before versus thirty after, returning the same
boolean result. Observations were 98.19/99.33 ms before and 2.36/2.17 ms after,
including instrumentation. This is a component result, not an original-workload
latency, RAM, model-token or provider-cache claim. The earlier original Captain
baseline timeout remains a separate preserved result; it has not been replayed
and candidate success on that original query is not claimed. The broader Hermes
improvement objective remains active.

---

# v0.7.33: reliable and bounded session discovery

Discovery previously capped raw matching messages at 300 before excluding current
context, inspected lineages or duplicate sessions. One busy session could hide
older conversations, an in-place compacted message, or an interactive conversation
behind scheduled-task chatter. Six native SQLite scenarios reproduce the failure
on the parent, through the actual tool registry. A separate review caught and
fixed two candidate-only regressions: a refill must not broaden an AND query when
an exact hit already exists, including an exact scheduled-task hit.

The repair applies lineage and live-context eligibility in every native search
route before row pagination. It refills by excluding selected lineage roots, asks
for at most the remaining output slots per query, and prioritizes interactive
sessions before scheduled ones at each matching tier. Exact, substring and relaxed
matching tiers are exhausted globally in that order, preserving fallback precision.
The requested output cap remains ten. Recursive lineage membership terminates on
cycles. Hidden/rewound rows, active delegation context, profile ownership, temporal
bounds and bounded excerpt hydration retain their guards. Older adapters retain
their bounded compatibility path. No tool schema or prompt-prefix change is made.

The final related selection passes 239 files / 2297 tests,
zero failures and 16 existing skips, with zero file retries and four
workers. Scoped code health and Ruff pass. Overlapping runs are not summed.
Linux and macOS production Python each pass eighteen installed native controls:
six saturation conditions in Latin, Thai and CJK, using readonly fixture databases.
No model/provider requests are made. The full consolidated patch is checked for
apply, reverse and reapply on both hosts, with scoped rollback and exact modes.
Linux activation is native and idle-only; the original Mac Gateway remains off.
No renderer rebuild, dependency, model, quota or resource-gate change is needed.

An additional synthetic 301-message fixture returns the same top-one message
before and after. Four ABBA samples reduce candidate rows crossing into Python
from 300 to one per query. Traced peak allocations were 458,145 and 334,362 bytes
before, versus 45,938 and 45,642 after; elapsed observations were 14.36/10.29 ms
before and 3.30/2.95 ms after. These component observations were taken alongside
offline tests, not a controlled original-workload latency or whole-process RAM
benchmark. They establish no model-token savings, provider cache hits or original
session adoption. The broader improvement objective remains active.

---

# v0.7.32: leaner plugin cleanup and accurate review-block metadata

Every registration previously allocated a fresh cleanup closure that captured its
manager. The same cleanup operation is now cached once per manager with the native
cached_property mechanism. Managers keep distinct callbacks and all registrations
retain their own release operation. Cleanup still late-binds the owner's method,
always runs after a release failure, and remains idempotent.

The new callback-memory test failed before the repair; two lifecycle controls
passed. The broader run also exposed an older workflow mismatch: the existing
backend accepts review-to-block moves but its workflow metadata denied them. The
metadata now agrees with that existing verb without changing kernel gates or
mutating any live card. Three multiplex-status fixtures now use an isolated
launcher directory, keeping the original-home I/O protection active. Those four
failures were reproduced on the parent code; no assertion or guard was relaxed. The final related selection passes 344 files / 3528
tests, zero failures, 8 existing skips and zero file retries.
Scoped source health and Ruff pass. Overlapping selections are not added together.

Linux and macOS production Python each pass seven installed native controls:
callback allocation bound, cross-owner ledger isolation, repeated disposal,
complete cleanup, persistent late dispatch, failed-release cleanup, and native
review-to-block behavior matching the published workflow. No model
or provider request is made. Exact scoped rollback and permissions are preserved;
Linux activation is native and idle-only, while original Mac Gateway stays off.
The full consolidated patch is applied/reversed/reapplied and installed parity is
checked on both hosts. No renderer rebuild or dependency/config change is needed.

The sixteen-manager / 8,192-handle component fixture retains 2,158,464 fewer Python
bytes. Four sequential native 116-profile fresh startup measurements (ABBA) show
mean PSS 336,038,912 before versus 333,786,624 after, zero swap. That controlled
series is not an original-user workload benchmark or a general latency/RAM claim.
No model-usage, provider-cache or inference-speed improvement is inferred.
Original models, quotas, effort ceilings, fallback and resource gates remain.
The broader improvement objective stays active.

---

# v0.7.31: make auxiliary and compaction test fixtures faithful

Twenty inherited failures were caused by dynamically fabricated MagicMock
attributes, rather than demonstrated production failures. Ordinary auxiliary
clients now explicitly declare that they do not own the main-context compression
recovery boundary. Three single-model conversation fixtures explicitly declare
that they have no MoA aggregator slot. All assertions and behavioral expectations
are unchanged. Only six test files change; runtime, credentials, retry/fallback
policy, models, quotas and resource gates are unchanged.

The same six-file baseline had 286 passes and 20 failures; corrected fixtures
pass all 306 cases. The final related selection passes 125 files / 1,290 tests,
zero failures, zero skips and zero file retries. Selections overlap and must not
be added together. Structural comparison verifies that the only AST changes are
the explicit mock-constructor fields. Scoped code health and Ruff pass.

Both installed hosts have the exact six test files and pass two additional
production-Python checks against actual synchronous and asynchronous SDK client
constructors. The real clients have neither fabricated ownership nor aggregator
attributes. No HTTP request or model inference is attempted. These are SDK-contract
checks, not a new full-loop model benchmark. The complete consolidated patch is
applied, reversed and reapplied on both hosts, with full installed-source parity.

No Gateway or Desktop restart is required for this test-only maintenance. Original
process identities, settings and protected files are preserved. No RAM, cache-hit,
token-cost or latency reduction is claimed by this release. The earlier twenty
failures remain recorded in historical reports below; this release resolves that
specific inherited set. The broader improvement objective remains active.

---

# v0.7.30: batch the fresh deferred index/trigger phase

Fresh store initialization previously committed each deferred index and trigger
separately. A failure could leave an earlier trigger committed even though the
phase failed. Initialization now identifies a genuinely empty declared schema and
runs its later deferred phase in one BEGIN IMMEDIATE transaction with rollback on
BaseException. The declared-table phase remains a separate earlier transaction.
Existing stores keep ordinary behavior, so settled checks do not gain a mandatory
write lock. Later FTS/migrations, schema version, ownership and durability stay native.

Two new native tests failed before the change: fresh triggers were created outside
a transaction, and an injected second-trigger denial left the first committed.
The existing-store/data control passed. The final related selection passes
274 files / 2353 tests, zero failures and zero file retries,
with 16 existing skips. Scoped source health and Ruff pass.

Linux and macOS production Python each pass six installed-source controls: fresh
transaction/integrity, native history and FTS, settled/read-only reopen, injected
deferred rollback and ordinary recovery, existing owner data and transaction
behavior, and a settled opener behind another writer. Private synthetic databases
and denied networking are used; no original-user store or model is called.
Linux activation is idle-only and original Mac Gateway remains off. The complete
consolidated patch is applied/reversed/reapplied and installed parity is checked
on both hosts. Companion tests are a separate selection; no renderer rebuild.

Diagnostic ABBA trials on sixteen fresh native stores reduced the open phase by
about 36.6 percent. One untraced matched native Gateway startup pair with 116 fresh synthetic profiles took 24.44 seconds before and 19.43 seconds after (about 20.5 percent lower). This is a single controlled pair, not a production or already-settled-store latency result. PSS did not improve; no RAM saving is claimed.
No original-workload latency, RAM, usage or provider-cache gain is inferred from
that component result. Original quota, model, effort, fallback and resource gates
are preserved. Earlier twenty inherited broad auxiliary failures remain documented;
historical overlapping test selections below are not summed. Full goal stays active.

---

# v0.7.29: bound long-lived profile lock buffers

Native synthetic startup allocation attribution found that profile reservation
held a filesystem-sized text I/O buffer for every lock descriptor. The repair
bounds that existing buffer to 4096 bytes. It does not remove locks, change lock
records, reduce the served fleet, interrupt active work, or alter any model,
quota, effort, fallback, ownership, review or resource gate.

The regression failed before the repair at 2,152,541 retained bytes for sixteen
real reservations. The related native test selection passes 7 files / 46 tests,
zero failures and zero retries, with six existing other-OS skips. It covers native
exclusion, partial-reservation rollback, stale and foreign locks, inode lifetime,
bootstrap, shutdown and endpoint identity. Scoped source health and Ruff pass.

Linux and macOS production interpreters each pass six installed-source checks:
bounded retained allocation, externally visible durable records/private mode,
exclusion, rollback, same-inode reacquisition/late cleanup, and a record larger
than the buffer. These operate on synthetic private homes with networking denied.
No model call or original user database is used. Original Mac Gateway stays off.
The complete consolidated patch is applied, reversed and reapplied on both hosts;
installed parity is a separate check. No renderer rebuild is required.

The allocation reduction is directly measured. Whole-Gateway PSS did not show a
stable equally sized improvement in the initial raw startup pairs. Allocator and
measurement effects must remain visible; this release makes no quantified original
workload RAM, startup latency, usage, or provider-cache saving claim. Full Hermes
acceptance and representative workload measurement remain ongoing. Earlier twenty
inherited broad auxiliary failures remain documented. Historical overlapping test
selections below are not added together.

---

# v0.7.28: discover the role-plan contract before creating work

A retained failed automatic-dispatch case showed Captain prescribing an internal
step ID that contradicted the validator. THINK then asked the user to resolve
that technical conflict. The repair makes the existing native routing CLI expose
the plan contract once, only when its bounded admitted roster includes THINK.
Its example and pattern come from the native role-plan module. The same module
supplies ID-choice ownership and external-name guidance in the THINK worker brief.
No global tool schema, account, quota, provider, model, approval or validator
change is introduced. No existing conversation prefix or worker is reloaded.

Before the change, two new behavior checks failed. The final related native
selection passes 9 files / 68 tests, with zero failures and zero file retries.
A third control keeps legacy-only discovery free of the planning contract.
The CLI test consumes the advertised ID through a real SQLite THINK completion
and checks that profile configuration remains byte-identical. Existing empty,
unadmitted, corrupt-peer, bounded-roster and secret-output controls still pass.
The worker test keeps exact externally required file/API names intact.
Scoped source health and Ruff pass.

Linux and macOS production Python each pass eight installed-source checks with
zero network/model requests, including native CLI contract discovery and a
legacy-only omission, a durable native plan using its advertised ID, strict
invalid-ID refusal, completed-review readback and foreign-assignee rejection.
The complete 759-path patch is checked by apply/reverse/reapply on both hosts,
with installed parity checked separately. Linux activation is idle-only; the
original Mac Gateway stays off. No renderer rebuild is needed.

A fresh provider-backed private GPT role loop now completed end to end using the
same frozen source and its actual embedded dispatcher: three original cards,
four native runs, a validated THINK plan, independent Analyst reference, paired
ACTION, independent review on the same card, Captain verification and native
goal done. Only the initial user prompt was submitted; there were no manual
staged dispatch calls, retries, additional human prompts or paid fallback.

The case used 39 physical requests under an unchanged hard limit of 42 physical requests.
The private fixture allowed six goal turns and actually completed in five.
This does not change any original account quota or live profile limit. A preceding
fresh case used 40 requests, reached the same artifact/review work, then correctly
paused at its five-turn fixture cap when the judge requested more explicit
verification confirmation. It was retained and never replayed. Different inputs
and responses prevent attributing the later success or request count solely to
the fixture cap or this patch.

Actual THINK/Analyst model calls overlapped for about 5.06 seconds. Captain called
the native routing CLI once and received its planning contract. Captain and the
independent reviewer each have an actual successful verify.py tool receipt;
all seven artifact cases passed. Four original-card result admissions reached
terminal completed state. Every worker's last tool was its successful native
handoff, with zero observed subsequent model starts for that native session.
After goal done, a fifteen-second observation saw zero additional requests.
The private owner then exited through its genuine idle-only native stop path.

Among 34 returned main calls with known input usage, the provider reported 552,925
input tokens and 471,552 cached input tokens (about 85.3 percent). This is observed
synthetic-workload input caching, not a billed-cost saving, a production before/
after improvement, complete auxiliary-token accounting, or cross-bot cache
causality. All protected original files and supplied inputs remained unchanged;
no auth files were copied and no raw credential matches were found in the case.

This acceptance covers one isolated GPT coordinator/planner/analyst/action/reviewer
graph on frozen installed-equivalent code. It does not prove original Captain
adoption, all provider families, all workloads or completion of the broader
maintenance objective.

Provider-backed acceptance above is separate from the offline/native checks.
These offline/native checks alone do not prove model autonomy, original-session
adoption, all provider pairs, production usage savings or cross-bot cache causality.
Earlier twenty inherited broad auxiliary failures remain documented. Historical
selections below overlap and must not be summed.

---

# v0.7.27: keep completed independent review evidence readable

A later fresh automatic-dispatch case reached all original role handoffs:
THINK complete, independent Analyst complete, ACTION requesting review, and the
independent reviewer completing the same card. All seven artifact checks passed.
It used 37 physical requests, and real THINK/Analyst calls overlapped for about
2.91 seconds. Four local automation admissions actually reached terminal
completed state. Captain then could not inspect the completed original card:
validation still treated the reviewer as an unrelated ACTION assignee. The
native goal correctly paused. This failed case is retained without replay;
it does not establish successful whole-goal completion.

The validator now recognizes a completed independent review only when the latest
native run is completed, has an end timestamp, matches the current assignee and
has the native claimed-event provenance of a review run. It keeps the original
actor, parent/run/hash, step, dependencies and write scope intact. Foreign
terminal assignees remain refused. No alternate role registry, status rewrite,
model request, automatic retry or authority bypass is introduced.

The new real-world regression failed before the fix while two foreign-assignee
controls passed. The final combined related selection has 8 files / 58 passes,
zero failures and zero file retries. Linux and macOS production Python each
pass six installed-source checks with zero network/model requests, including
completed-review readback and foreign completed-assignee refusal. The same
release includes the strict step-ID brief/error clarification described below.
Full provider-backed reacceptance remains separate; original-session adoption,
all provider pairs, production usage savings and shared-cache causality are
not established. Historical overlapping suites must not be summed.

A subsequent fresh bounded case stopped before ACTION because Captain's brief
introduced an underscore-containing internal step ID as an explicit requirement.
THINK detected its conflict with the strict grammar and asked for clarification.
The private case drained after 21 physical requests and was not replayed. This
separate coordination/policy issue remains open: routine internal identifiers
should not require owner intervention, while externally meaningful identifiers
and material authority gates must remain protected. No approval rule or identifier
validator was weakened to make the case pass.

---

# v0.7.27: advertise strict THINK step IDs before handoff

A fresh bounded automatic-dispatch case completed the independent Analyst work,
but the THINK bot submitted an underscore-containing step ID. The unchanged
validator correctly refused it. Its former error said only “unique lowercase id,”
and the worker brief omitted the accepted grammar, so the bot unnecessarily
asked the user about a technical formatting rule. That failed case used 22
physical requests after its private workers drained; it is retained, never
replayed, and is not reported as a successful full loop.

The brief and error now state `[a-z][a-z0-9-]{0,63}` and explicitly exclude
underscores. The existing validator, exact plan hash, run binding, write scopes,
independent review, quotas, effort ceilings and approval policy are unchanged.
No tool, parser relaxation, retry or model call is added by the repair.

Two new tests failed on the unchanged parent. The final related selection has
8 files / 58 passes / zero failures and file retries. Scoped source health and
Ruff pass. Linux and macOS production Python each pass six installed-source
checks using native SQLite/configuration/handoff APIs, with no network or model
requests: brief grammar, atomic invalid-ID refusal, durable valid plan, and
legacy completion. These checks do not establish provider-backed autonomy.

A separate earlier case used 18 requests and stopped at an inline Python command
approval refusal. The policy remains deny. Existing jq passed the real native
Terminal path for read-only JSON aggregation while inline Python remained
blocked. Capability selection must preserve approval boundaries; it is not
permission to disable them or replay a failed task.

The complete 759-path public patch is verified by apply/reverse/reapply on both
hosts, and installed source parity is checked separately. Linux activation is
idle-only. The original macOS Gateway stays off. Fresh provider-backed full-loop
acceptance remains separate work. Original-session adoption, all provider pairs,
production usage savings and cross-bot cache causality are not established.
Earlier broad auxiliary testing retains twenty documented inherited failures;
this scoped passing selection is not a globally green upstream suite.
Historical selections below overlap and must not be summed.

---

# v0.7.26: lazy local adapter owner binding

Consolidated kit:759 source paths. Related native wake/local/notifier selection:
32 files /114 latest per-file passes, zero failures/retries; final changed fixture
four passes. Scoped health clear. Linux and macOS production Python each verify
four real authority/FIFO scenarios with model scheduling held and no model calls.
Full public apply/reverse/reapply and installed parity are checked on both hosts.

A real fourteen-request discovery case found the bug and achieved actual model
overlap, but failed its full loop. It is retained and never replayed. Provider
reacceptance of the corrected loop and original-session adoption remain unproven.
See [the owner-binding repair and evidence limits](local-result-wake.md).
Historical selections below overlap and must not be summed.

---

# v0.7.25: completed card-result goal waits

The consolidated kit has 756 source paths. Related goal, viewer and loop
selection: 30 files / 302 passes, zero failures and file retries. Scoped source
health has no new findings. Linux and macOS native installed acceptance each
verify nine scenarios with real isolated SQLite and controlled judge decisions;
no real model or external provider calls. Full public apply/reverse/reapply and
installed parity are checked on both hosts. Original-session adoption and a
continuous autonomous bot graph remain unproven.

See [the advisory wait repair and limits](goal-result-waits.md). Earlier evidence
below is historical, overlaps this selection and must not be summed.

---

# v0.7.24: Gateway goal notification identity

The consolidated kit pins 752 source paths. Goal/board/notification/multiplex:
35 files / 373 passes, zero failures and file retries; scoped code-health has no
new findings. Linux and macOS installed native acceptance each pass 12 checks,
including two real Gateway-hook/synthetic-route cases with controlled judges.
No real model or external provider calls for this release. Both hosts pass full
public-patch apply/reverse/reapply. Installed parity per host:751 exact plus one
pre-existing comment-only AST-equivalent tool difference, zero missing files.

See [the identity repair and evidence limits](goal-notification-identity.md).
Historical selections below overlap and are not summed. Their broader inherited
failures, original-session and continuous-graph limitations remain visible.

---

# v0.7.23: bounded retries and cross-board goal waiting

The consolidated kit now pins 750 source paths. The new goal/board/notification
selection passes 290 cases across 15 files, zero failures and file retries.
Code-health reports zero new findings for the three scoped source/test paths.
Native installed acceptance on Linux and macOS each passes ten SQLite/goal
checks; both hosts also pass the five real-SDK controlled-loopback retry checks.
No real model or external provider is called for this release.

The async repair has a separate three-file/24-pass focused selection. Its broader
125-file selection has 1,270 passes and 20 inherited failures, all reproduced on
the unchanged parent in the same six failed files; zero new failures. The exact
inherited names are in the test selection. Overlapping selections are not summed,
and this is not a globally green upstream suite.

Both native hosts apply, reverse and reapply the 750-path public patch using the
unchanged checkout verifier. Each original installed tree has 749 exact files and
one pre-existing comment-only, Python-AST-equivalent Kanban tool difference; zero
missing files. No source-wide restore or replacement was performed. Linux Gateway
loaded the scoped source during confirmed idle; the original macOS Gateway stayed
stopped. Existing stop state, profiles, models, quotas, credentials and work were
preserved. This does not prove an original session adopted the new behavior.

See [goal waiting](goal-kanban-awareness.md) and [auxiliary retry policy](async-auxiliary-retries.md).
These cases establish retry admission and native advisory-count/wait mechanics,
not workload billing/cache/RAM savings or a continuous autonomous bot graph.
The previously bounded real-provider graph below remains separate historical
proof; it was not replayed or charged again for this release.

---

# v0.7.22: bounded real native parallel evidence

Evidence-only update; the exact 748-path source patch payload is unchanged from
v0.7.21. A new synthetic Linux case completed six native cards / seven runs with
36 physical high-effort requests, zero retries/fallback and nine artifact checks.
Native run overlap was 18 seconds and main model request overlap 13.839283 seconds.
No tools or model requests followed terminal handoffs; final quiet observation was
15 seconds. Original model/configuration/quotas/holds remained unchanged.
See [the case, method and limits](parallel-native-acceptance.md). This is not
continuous production scheduling, all-family adoption, cross-bot cache causality
or measured workload savings. Source regression/native Linux/macOS acceptance
below remains historical evidence on the same bytes, not repeated test totals.

# v0.7.21: compact saved profile routing

748 pinned paths. Broader profile/workflow selection: 84 files / 738 pass / six
existing platform skips / zero failures and retries. Seven installed native CLI
checks each on Linux/macOS pass with network denied. See [routing snapshot](profile-routing-snapshot.md).
Final integrated selection: 88 files / 835 pass / eleven existing skips / zero failures and retries. Actual-owner tool-shell CLI checks pass on both hosts. The real coordinator correctly blocked on the pre-repair stale CLI after seven requests; no parallel completion or usage reduction is proven. No global-green
or original-user adoption claim.

# v0.7.20: managed-worker source pinning

742 pinned paths. Full managed-worker selection: 40 files / 124 pass / 0 fail,
zero retries. Installed native source/secret isolation checks pass on Linux and
macOS with zero model/network requests. See [source pinning](managed-worker-source-pinning.md).
The new real coordinator reached the provider and created THINK, then gave_up at the private iteration cap after eight requests. Parallel-bot completion is NOT_PROVEN; no global-green, original-user adoption or workload savings claim.

# v0.7.19: known native auxiliary reasoning floor

740 pinned paths. Four focused files / 24 pass; broad 74-file selection / 848 pass
and 15 inherited failures, zero retries and no new failures. Five native installed
smart-approval serialization controls each on Linux/macOS pass offline.
See [native floor and actual Captain acceptance](native-auxiliary-reasoning-floor.md)
for the result and its limits. No global-green or production savings claim.

# v0.7.18: auxiliary Codex effort fidelity

738 pinned paths. The final Responses request retains top-level chat effort,
including owner ceilings, lower efforts and explicit disablement. Focused 62
cases pass; the broad 73-file selection has 840 passes and 15 inherited failures,
reproduced unchanged on the prior source. Five native offline serialization
controls each on Linux/macOS pass without model calls. No new code-health
findings. No production usage savings or successful real Captain goal completion
is claimed. See [acceptance and known limitations](auxiliary-codex-effort.md).

# v0.7.17: preserve concurrent MCP schema entries

736 pinned paths. A profile-local native lock covers manifest read-modify-write;
no lock is held during server discovery or tool execution. Final scoped native
regression: 98 files / 911 passed / 0 failed / 1 existing skip, zero retries.
Five installed production-Python controls each on Linux/macOS retain both peer
entries and cold-register both required tool schemas with zero server starts,
network requests or model calls. Code-health reports no new findings.
See [concurrent MCP schema publication](mcp-schema-publication.md).
This is synthetic native acceptance, not original-workload usage or latency proof.
Historical/focused counts overlap and are not summed.

# v0.7.16: retire old profile config caches

735 pinned paths. Completed delete/rename and permitted Gateway retirement
release old config cache values and warning records. Parked live homes,
unfinished authorities and sibling profiles retain their recovery state.
Latest-per-file regression: 256 files / 1,855 passed / 0 failed / 7 existing skips,
zero retries. Five installed production-Python controls each on Linux/macOS;
eight packaged-renderer checkpoints with a separately instrumented private backend.
No inference or measured original-workload RSS/PSS savings claimed.
See [profile config cache retirement](profile-config-cache-retirement.md).
Historical counts and focused runs overlap and are not summed.

# v0.7.15: preserve the validated config generation

731 pinned paths. Both native readers now back up their parsed bytes and
descriptor metadata instead of reopening the source path after validation.
Native regression: 174 files / 1,234 passed / 0 failed /
4 existing platform skips, zero retries. Installed Linux/macOS:
eleven production-interpreter controls each, network denied. Code-health clear.
See [validated config snapshots](config-backup-snapshot.md). No original-user
conversation adoption or measured savings claimed. Historical counts overlap.

# v0.7.14: complete, ordered config backup publication

729 pinned paths. Rapid same-second saves no longer collide; readers do not
see partial copies; failed copies preserve the previous good backup; rotation
uses a fresh completed-file listing. Default retention five and unchanged-content
deduplication remain. Native regression: 173 files / 1,230
passed / 0 failed / 4 skips, zero retries. Installed Linux/macOS:
seven production-interpreter controls each, zero providers. Code-health clear.
See [config backup publication](config-backup-publication.md). No measured disk,
RAM, usage or cache saving claimed. Historical counts overlap.

# v0.7.13: preserve last-good config through metadata failures

727 pinned paths. Signature I/O failures now reuse native last-good raw config/
backup recovery; strict readers, missing-file semantics, worker snapshots and the
normal cache path remain unchanged. Native regression: 163 files /
1,110 passed / 0 failed / 4 skips, zero retries. Installed
Linux/macOS: thirteen controls each, zero providers and code-health clear. See
[config metadata recovery](config-metadata-recovery.md). No measured usage/RAM/cache
saving or original-user conversation adoption is claimed. Historical counts overlap.

# v0.7.12: isolated authority caller fixtures

724 pinned paths; runtime source unchanged from v0.7.11. Seventeen test files repair
native config-loader signatures, unavailable-primary isolation and launcher-aware
client PATH assertions. Additional direct callers: 122 files / 719 passed /
0 failed, zero retries; code-health clear. The original 58 failures reproduce on
pre-v0.7.11 runtime bytes. See [authority caller verification](authority-caller-verification.md).
No model calls, production quota/fallback changes or Gateway restart. Historical
counts below overlap and are not a whole-project green claim.

# v0.7.11: profile preparation cancellation and shutdown custody

707 pinned paths. All bootstrap writes and the store opener drain their physical
executor Future before cancellation releases profile custody. Native regression:
273 files / 2,349 passed / 0 failed / 16 existing
skips, zero retries. Final focused selection: 26 passed, overlapping the broad
selection. Installed Linux/macOS: 7 native controls each; code-health clear and
zero provider calls. See [profile bootstrap custody](profile-bootstrap-custody.md).
No original-user conversation adoption or usage/RAM/cache saving is claimed.
Historical results below overlap.

# v0.7.10: atomic fresh schema with fewer initialization commits

703 pinned paths. An empty SQLite schema gets one native declaration transaction;
existing stores retain their previous lock/reconcile behavior. See [fresh schema startup](fresh-schema-startup.md) for the 35.4% fresh-only median improvement and
limits. Native regression: 272 files / 2,335 passed / 0 failed / 16 existing platform
skips, zero retries; code-health clear. Installed Linux/macOS: 8 native controls each,
network denied, zero providers. This is not a whole-Gateway RAM/token/cache/latency
or original-user adoption claim. Historical results below overlap.

# v0.7.9: canonical groups work with ready standby

701 pinned paths. Canonical room controls distinguish an armed standby coordinator
from an unarmed or stopped runtime. Native create/admission wakes its owner once;
empty profiles retain zero idle supervisor threads. See [standby group controls](standby-group-controls.md) for scope. The current selection passes 51 files / 283
tests, zero retries, including all three group failures recorded in v0.7.8. Installed
Linux/macOS acceptance each passes 8 controls and one deterministic offline member
execution, with zero provider calls. Code-health is clear. Original macOS Gateway
and Desktop bundle adoption remain separate; no original-user workload savings claim.
Historical counts below overlap and are retained as history.

# v0.7.8: keep served profiles responsive during cold SQLite open

699 pinned paths. Existing owned executor and scope-aware handle cache; cancellation
drains physical opens and shutdown retains writer visibility. See [profile startup
I/O](profile-startup-io.md) for measured scope and the pre-existing group-control
failure reproduced on the before version. Focused regression: 16 files / 48 passed;
wider selection: 159 passed / 3 existing failures; native Linux/macOS: 8 controls
each, zero inference; native code-health clear. Historical counts below overlap.
No universal startup, RAM, token or original-session adoption claim is made.

# v0.7.7: reuse static plugin manifest metadata

The consolidated stable kit contains 696 pinned paths. Manifest discovery reuses
the existing YAML file cache, then copies metadata for each caller. Native reload,
permission, profile and plugin execution gates stay in place. See [manifest metadata
reuse](plugin-manifest-cache.md) for measured scope and limits.

Current validation: 15 regression files / 203 passed, zero retries; 8 installed
synthetic-home controls per Linux/macOS, zero inference; native code-health clear.
Overlapping historical counts below are not summed. Whole-Gateway task/token/RAM
savings and original-user model-backed adoption remain unproven.

# v0.7.6: demand-start hosted room supervisors

The consolidated stable kit contains 694 pinned paths. Empty canonical hosted
profiles remain ready without a supervisor thread. Existing producers wake
immediately; persisted-room fallback uses the existing watcher. Stop and profile
ownership fences are preserved. See [hosted standby](hosted-room-idle.md) for scope.

Current validation: 9 native test files / 102 passed, zero retries; 6 installed
synthetic-home controls on Linux and 6 on macOS, zero inference. Native code-health
reported no findings. These counts overlap earlier evidence and must not be summed.
Original-user task savings and model-backed adoption remain unproven.

# v0.7.5 native skill aliases on Kanban cards

The consolidated stable kit contains 689 pinned paths. Preflight keeps declared
names accepted by the native loader and reuses the existing catalog cache for
unresolved names. Canonical same-file symlink aliases agree across catalog/loader;
different-file ambiguity and owner/frozen-worker gates remain native.
See [skill discovery](skill-discovery.md) for cold/warm measurements and limits.

The current selection passed 26 files / 472 cases, zero retries. Installed native
Linux/macOS acceptance each passed 17 controls with zero inference. Scoped native
code-health comparison reported no findings, and strict Ruff found no new issues.
Earlier records below are historical; overlapping counts are not summed. This is a
backend-only change; the previously verified Desktop package is unchanged.

# v0.7.4 cycle-safe skill discovery

The consolidated stable kit contains 687 pinned paths. One physical-identity,
branch-local traversal is shared by skill indexing, catalog signature checks and
Kanban preflight. It bounds symlink cycles without dropping independent aliases
or deeply nested valid skills, and retains native dependency/support exclusions.
See [skill discovery](skill-discovery.md) for measurements and evidence limits.

The relevant selection passed 25 files / 463 cases, zero retries. Native installed
Linux/macOS checks each passed 11 controls in isolated homes with zero inference.
No new strict scoped lint findings were introduced; an existing Kanban finding
remains. Earlier test/UI records below are historical and were not rerun or summed.

# v0.7.3 assignee-scoped preflight

The consolidated stable kit contains 683 pinned paths. Native config resolution replaces
two raw YAML behavior reads and preserves configured external skills at card creation.
Frozen workers keep their own snapshot; cross-profile creation defers unavailable
capability inspection to the native dispatcher, which still checks before claim/spawn.
Existing role/ownership metadata gates remain in place. See the [guide](assignee-preflight.md).

The relevant Python selection has 18 files / 208 passing cases by latest per-file
results, zero retries. The source guard passes. Native installed Linux/macOS tool,
config and SQLite acceptance each passed eight controls using synthetic files with
zero inference requests. Candidate runs and repeated hosts are not summed. Earlier
policy/UI suites below are historical baseline, not newly rerun for this change.

# v0.7.2 compact bot settings

Two Desktop presentation paths keep model/effort ahead of expanded role fields and
place optional avatar controls in an Appearance disclosure. See the [editor guide](desktop-bot-settings.md).
Native Linux/macOS typecheck and build, prepared offline packaging, local Mac signature
verification, and rendered packaged-app interaction checks are recorded separately.
The installed packages each passed the same 11 interaction checkpoints in isolated
synthetic homes with zero inference requests. These overlapping host/candidate runs
are not summed. The initial compact editor was checked after fonts settled; model
and effort settings, Save/Cancel, navigation, Workflow, Hub and History were covered.
This revision makes no Python runtime, dependency, account or quota changes. The
v0.7.1 policy suite below is prior evidence; overlapping runs are never summed.

# v0.7.1 optional reasoning effort ceilings

The consolidated stable kit now contains 681 pinned paths. See the [effort-limit guide](reasoning-effort-limits.md) for policy, request boundaries and exact evidence limits. Current change: an 86-file Python selection has 645 passing cases by latest per-file results; 84 files passed the integrated run and two repaired child-environment harness files passed separately. Desktop: 3 files / 25 PASS, typecheck/build PASS, and 5 rendered source-mode checkpoints with an actual isolated backend, zero inference. Historical v0.7.0 broad-suite counts below are baseline evidence, not a rerun on this revision; do not sum overlapping scopes. A separate inherited raw-YAML source guard remains failing and is documented explicitly in the guide. Original-session, packaged-public-build and provider workload acceptance remain separate.

# v0.7.0 consolidated stable kit

See the [complete stable guide](stable-full-kit.md) and [667-path inventory](../patches/stable-full/manifest.json). Broad offline Python: 218 files, 2737 PASS, 13 SKIP, zero failures; UI: 60 files, 383 PASS; typecheck/build PASS. Later two synthetic-only fixture edits: 33 PASS, overlapping the broad scope, not additional unique cases. Native apply/reverse/reapply passed on Linux and macOS. Linux rendered source-mode checks passed 11 interaction checkpoints, including explicit Kanban opt-in, upstream-card navigation, a native Hub page save, and retained-message reopening. They use the actual backend and a separate synthetic home, with no inference; original-session and packaged-public-build adoption remain separate acceptance.

# Verification record

## Initial cumulative patch acceptance (v0.1.0)

This record describes the exported artifact's offline acceptance. It contains no production logs, prompts, accounts, task/run IDs or private machine paths.

| Check | Result | Scope |
|---|---|---|
| Patch base verification | PASS | Exact publicly available upstream commit and all 279 before hashes |
| Normal Git apply check and apply | PASS | Separate disposable checkout, not a running installation |
| Installed source verification | PASS | All 279 resulting hashes match the export manifest |
| Reverse apply and base restoration | PASS | All original bytes and absence states restored, then reapplied for regressions |
| Python source syntax | PASS | 242 changed/added Python source and test files |
| Exported Hermes Python regressions | 964 passed, 0 failed | 109 input files through the canonical per-file runner, zero retries, three workers |
| Desktop UI unit regressions | 56 passed, 0 failed | Seven changed UI test files; no rendered desktop/model test |
| Companion tool regressions | 11 passed, 0 failed | Wrong revision, unrelated work, existing new targets, traversal, symlinks, changed/missing/unlisted files |
| Roles and skills | Eight roles, ten skills | Rewritten English templates; no live persona/configuration export |
| Working-tree secret scan | PASS | Gitleaks 8.30.1, default rules, fully redacted output, allow-comment bypass disabled |
| Privacy review | PASS for reviewed identifiers and file inventory | Every public file plus full patch contents; separate private identifiers review |
| Historical-secret detection control | PASS | A synthetic local-only credential was committed then deleted; current-tree scan was clean and all-history scan detected it |

macOS-tagged Python checks in five files were skipped on the Linux test host. This is not macOS acceptance, a full upstream test-suite result, or a whole-repository lint/build claim. The desktop tests are unit tests, not visual or live-session acceptance.

Three test files were generalized for distribution: a machine-specific home assertion became a portable assertion, a diagnostic sentinel became short synthetic data, and a credential-redaction fixture now constructs unmistakably artificial input at runtime. No live source file was edited for these export changes.

The dedicated scanner checks both the exact committed tree and all reachable Git history before publication. The initial history is created fresh with a neutral project author/committer, and the final archive is generated from Git's explicit tree rather than a working-directory copy. `RELEASE-MANIFEST.json` records every payload file's SHA-256; the manifest itself is bound by the Git commit and archive hash.

All upstream-base source tests used the existing approved test environment. The test runner's normal isolation created temporary homes; no model acceptance job, provider/allowance probe, dependency install or service restart was used to create evidence. Private source hashes were compared afterward and remained unchanged.

No general token-saving percentage, billing saving, cross-bot provider-cache origin, unlimited cache retention or live startup speedup is established by this release. Measure actual authorized work with matched identities and honest coverage if evaluating impact on your own installation.

## Team and multi-account update (v0.2.0)

The cumulative 279-file Hermes patch is unchanged. This update adds a standard-library-only offline planner, fifteen public role templates, a 34-profile topology, six Web specialists, native config fragments and English setup guides. Account identities, usage snapshots, tasks and budgets are synthetic. No live profile/account is exported or changed.

The companion's full unittest suite covers new-session route choice, public/private gates, capability readiness, shared account budgets/duplicate aliases, hour/day/parallel limits, cooldown, missing/stale evidence, exact session pins, existing running work, dependency waits, provider mismatch, secret-field rejection and no network/input mutations. New behavior was observed failing before implementation, including a reproduced duplicate-handle/split-budget case. Current release acceptance is regenerated after all files are finalized; previous Hermes regression counts above are not added to the new companion-test count or represented as newly rerun.

The planner is not a native account selector or live quota enforcement layer. Setup documentation separates native pool ownership and manual profile configuration from offline recommendations. A real-bot/model acceptance run was not requested or performed for this update.

### Reproduce native config compatibility offline

In the isolated, supported Hermes checkout, copy `verification/native_profile_examples.py` to `tests/hermes_cli/test_legion_native_profile_examples.py` and copy the 34 `profiles/native/*.config.example.json` files to `tests/hermes_cli/fixtures/legion-native-fragments/`. Run that test file through the checkout's canonical `scripts/run_tests.sh` and existing managed test environment, with retries disabled. This uses Hermes' own isolated-home fixtures, effective config loader, pool-strategy reader and profile argument parser; no actual credential pool is loaded, no account is logged in, and socket creation is denied during effective-config checks. The test refuses a missing fragment directory instead of reporting an empty run as success.

Historical v0.2.0 team acceptance: **34 companion tests passed, zero failures**, plus **36 native configuration/parser cases passed, zero failures**. The latter cover all 34 distributed fragments, the documented native create command, and safe merging over a pre-existing legacy fallback chain. These are separate groups; prior cumulative-patch results are historical and were not rerun for this documentation/planner-only update.


## Public usability audit and fixes (v0.2.1)

The review began with an anonymous clone and public v0.2.0 release download. All six documented planner examples ran offline, but targeted regressions exposed two gaps: a plan could select another task for an already busy session, and Python's JSON reader accepted nonstandard Infinity values that could keep a snapshot eligible indefinitely. New tests failed on the published implementation before the repair.

The planner now fences sessions with running work regardless of task ordering, reserves a session after its first selection, rejects NaN/Infinity input and requires finite observation/snapshot times. It still only prints recommendations; it cannot dispatch, authenticate, enforce native credential selection or change live state.

The setup guide now gives exact fresh-home/profile commands, targeted model/pool/fallback updates, model-placeholder refusals and SOUL installation. The installation guide includes public base-checkout commands. Changing a home variable is explicitly distinguished from selecting a CLI installation. Both current and legacy fallback chains are cleared while unrelated settings are preserved.

Fresh acceptance for this update: **38 companion tests passed, zero failures**; separately, **37 native cases passed, zero failures**, covering 34 config fragments, argument parsing, legacy fallback merging and one complete three-profile setup walkthrough. The walkthrough invokes native command parsers/handlers for create, config path/set/get and verifies an existing delegation cap survives. It uses isolated homes, synthetic instructions/models, disabled container-service registration and denied network/multiplexer access. No OAuth flow, credential selection, model request or live-worker test was run.

A separately guarded full CLI entrypoint probe stopped at the native home-bootstrap boundary; it is not counted as a passing full-launch test. No live source or bootstrap behavior was changed to make it pass. Packaged launchers, platform services, provider/model availability and real authentication remain operator checks. These limitations matter when adopting a template on another machine.

The cumulative source patch and its 279-file manifest are unchanged. The previous 964 Python and 56 UI results are historical, not newly rerun for this planner/documentation fix. Files, all reachable Git history, release payloads and known private identifiers/credential values are reviewed before publication; reports remain outside the repository.


## Offline preparation and diagnostics (v0.3.0)

New tools preview/export registered config and SOUL templates to a fresh private directory and inspect explicit JSON inputs/bundle integrity. The planner adds optional per-candidate explanations while preserving its original decisions, reservations and pins. Runtime/auth readiness stays unknown. No account mapping or quota snapshot is exported, and no native config is installed automatically.

Fresh companion acceptance: **64 tests passed, zero failures**. New regressions were observed failing before implementation, including missing offline tools/explanations, empty Web model references and false readiness for an empty team. The suite covers overwrite/link/live-root refusal, model/secret-field validation, all 34 registered exports, bundle corruption and semantic fallback checks, safe diagnostic output, stale snapshots, no network/process execution on the bundle path, explanation equivalence and pinned/busy sessions.

A checkout-inspection regression proved that Git could execute a configured filesystem-monitor helper. The verifier now disables it, external diff/text conversion, lazy fetch, prompts and optional locks. The regression passes without running that helper. On a fresh isolated pinned checkout, doctor passed both the original base and exact applied-source state; no Hermes import was used for these inspections. Git apply reported existing cumulative-patch whitespace warnings, not an apply refusal; the unchanged target hashes passed.

Separately, **37 native cases passed, zero failures**, using all **34 newly generated synthetic config fragments** as the native harness inputs, plus parser/legacy-fallback/three-profile setup checks. Use the existing native verification recipe; for generated fragments, copy each `profiles/<id>/config.example.json` to the fixture directory as `<id>.config.example.json`. The approved existing upstream-managed test environment and canonical runner were used with zero retries. No dependencies were installed. This is offline config acceptance, not actual provider authorization, model capability, packaged startup or live routing.

The 279-file cumulative source patch remains unchanged. Source/profile guards are compared around the work, and public files, reachable Git history and release payloads are scanned before publishing. Historical source/UI counts above are not rerun or added to these results.


## Repeated attachment fix (after v0.3.0)

The current main branch extends the cumulative patch to 280 files. Repeated built-in
references in one message now expand once per kind, target and line range. Original
user text and reference metadata remain intact. Distinct ranges remain separate;
plugin references retain their existing behavior. No cache survives to the next message.
The 16-expansion work limit applies to distinct built-in attachments.

Offline regressions first reproduced two failures: duplicate URL extraction and
16 copies of the same file preventing a later distinct file from being attached.
The final new regression file passes 5 cases; the existing reference, plugin,
concurrency, CLI and Gateway files pass 48 cases. These are separate cases, not
summed historical test runs. No model or real URL request was made.

One synthetic 30,000-character file referenced 16 times, with a 1,000,000-token
context limit, produced these results using the native preprocessor:

| Metric | Before | After |
|---|---:|---:|
| Estimated injected tokens | 120,176 | 7,511 |
| Output characters | 480,985 | 30,340 |
| Peak traced Python allocations (bytes) | 6,134,460 | 257,107 |

This single offline sample is not a whole-process RSS benchmark, billed token
measurement or evidence of savings across production workloads. Already-running
processes must load the changed module through their normal safe lifecycle before
runtime activation can be claimed. Provider quotas and fallback settings are unchanged.
The v0.3.0 tag and release remain immutable; these results describe the newer main branch.


## Cache memory boundary correction (after v0.3.0)

The current main branch now contains 282 patched or added files. Automatic cache
budgeting uses the smaller finite memory.high/memory.max value in the selected
cgroup, rather than blindly preferring memory.high. The own-cgroup/root lookup
order and v1 fallback remain unchanged. This does not add ancestor traversal or
change operator-configured limits, quotas, provider selection or fallback policy.

The Linux [cgroup v2 documentation](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
distinguishes the high throttling threshold from the maximum memory boundary.
An offline regression with memory.high=8 GiB and memory.max=2 GiB previously
produced a 5,324 MiB auto budget; it now produces 1,331 MiB, preserving the existing
65% headroom policy. Three control combinations retained their expected budgets.
All 43 tests across the boundary regression and existing cache-pressure suite pass.
No model calls or live memory-limit changes are involved. These are correctness
results, not measured production RSS savings. Immutable release tags are unchanged.


## Durable idle-cache eviction (after v0.3.0)

Idle-TTL and cache-size eviction now use the same persisted-transcript check as
memory-pressure eviction. Previously, both paths could remove the only current
copy of a conversation while the session DB lagged behind. Unflushed or unknown
transcript state now retains the agent; a later sweep may evict it once the flush
index catches up. Active agents remain protected. Explicit user-directed session
reset/model changes retain their existing semantics.

Two native regression cases first failed on the prior source (one per policy),
then passed with the fix. All 73 cases across the new durability regression,
existing agent-cache tests and cache-pressure tests pass offline. Three existing
eviction fixtures now explicitly represent persisted transcripts; their original
release-order and bounded-cache assertions remain intact. No model calls are used.

This intentionally favors conversation preservation over RAM reduction during a
persistence failure. It does not repair a failed database or impose a hard memory
limit. No production memory-savings percentage is claimed.


## Explicit usage-log coverage (after v0.3.0)

The read-only usage attribution CLI now accepts an explicit log-file budget:

```sh
python -m hermes_cli.usage_attribution --home /path/to/hermes-home --hours 24 --max-log-files 512
```

The default remains 32 recent uncompressed files. The accepted range is 1–512,
with at most 2 MiB read per file. The report includes the chosen budget, files
sampled, omitted files, cut tails and unknown time coverage. An expanded scan can
read up to 1 GiB; use it for a deliberate audit rather than frequent polling.
Compressed logs and profiles beyond the existing 128-profile bound are still not
read. Zero omitted files does not establish complete time-window coverage.

Five new offline cases verify expanded CLI collection, unchanged lightweight
defaults, invalid-budget rejection before I/O and private-record exclusion.
Together with the existing attribution tests, all 13 cases pass. The installed
standalone CLI was exercised read-only against existing logs before publication;
no Desktop or Gateway restart is required. No model calls, new keys, database
initialization, quota changes or paid fallback are involved.

Compare before/after using equal coverage and matched time windows. More observed
attempts after increasing the budget means improved visibility, not increased
usage; fewer rows in a partial scan do not prove savings. Runtime logs, identifiers
and measurements from private projects are not part of this public package.

## v0.3.1 release verification

This release includes the four post-v0.3.0 changes above: repeated attachment
deduplication, correct cache memory-boundary selection, durable idle-cache
eviction and an explicit usage-log scan budget. The cumulative inventory contains
287 source/test files, including 115 Python test files. Earlier release tags
remain unchanged.

The release integration run passed 143 distinct native cases in 12 relevant
test files, with zero failures and zero retries. The companion tools and examples
are checked separately; historical overlapping runs are not added to this count.
The source patch and pinned upstream revision are unchanged by release packaging.

Memory-boundary detection does not configure MemoryHigh or MemoryMax. An operator's
MemoryHigh can throttle work; MemoryMax can trigger an OOM kill. This release
preserves active agents and unflushed conversations during automatic cache
eviction. It does not promise that an externally imposed hard limit is safe for
every workload.

The locally installed runtime files were compared with the public inventory
before release. Offline results establish regression coverage, not measured
production RAM, latency, billing or cross-bot cache savings. No model requests
are used for release verification, and no live limits or provider settings are
changed by packaging.


## Growing-file preview bounds (after v0.3.1)

A pre-read file size is advisory: an ordinary log can grow between stat and open.
Bare file references now bound the actual decoded read to the existing inline
character budget plus one sentinel character. Oversized content retains the
existing on-disk guidance rather than injecting a partial preview. Folder-entry
line counting likewise reads at most its existing 4 MiB ceiling plus one sentinel
byte; growth beyond that produces a fresh byte-size summary. Binary sniffing,
BOM decoding, allowed-root checks and SQLite read admission remain in place.

Two native regressions reproduced the unbounded reads before the fix; five final
cases cover growth and unchanged small/BOM/Unicode/exact-boundary behavior. All
67 cases in eight relevant reference, CLI, Gateway and SQLite inspection test
files pass offline with zero failures and zero retries. Ruff reports no findings
for the changed source and new regression file.

A synthetic file grew from six bytes to 8,388,614 bytes at the stat/open boundary.
With an existing 2,048-character inline budget, decoded text consumed fell from
8,388,614 to 2,049 characters. After warming the same metadata/import path, peak
traced Python allocations for this attachment sample fell from 16,920,866 to
209,393 bytes. Metadata-only reading fell from 8,388,620 to 4,194,311 bytes, including
the binary sniff. These are deterministic offline samples, not production RSS,
billed token or latency savings. No model requests, quota changes or paid
fallback are involved. The immutable v0.3.1 download does not include this newer
main-branch change.

## Explicit backup compaction (after v0.3.1)

The companion storage helper previews or compacts explicitly selected old SQLite
backup files. It streams compression and decompression, verifies exact SHA-256
and source identity, publishes an archive plus restoration metadata without
overwriting existing outputs, syncs before unlinking the original, and preserves
a free-space reserve. It does not operate on live databases or introduce SQL,
model calls, retention timers, provider changes or paid fallback.

Eleven offline cases cover read-only planning, byte-exact recovery, private-content
exclusion, sidecar/recent/link/path refusal, low space, existing outputs, source
growth, sync failure and canonical duplicate selections. The CLI examples are
also exercised against temporary synthetic SQLite snapshots. The native source
patch remains unchanged; this helper is newer than the immutable v0.3.1 release.


## Active and resumable scratch retention (after v0.3.1)

Automatic scratch retention no longer reaps processes by idle mtime. It checks
same-user working directories, executables, open files and command paths; unknown
process visibility defers the sweep. Git worktrees, environment/project markers
and `.keep` markers are preserved, including their registrations and uncommitted
files. Incomplete workspace scans retain data. Explicit operator-directed reaping
utilities remain separate from automatic retention.

Fresh entries skip recursive traversal. The native Gateway housekeeping table
runs protected scratch cleanup hourly under each served profile, with no added
startup sweep from that table. Existing opportunistic boot retention uses the
same protected policy. The original 24-hour idle threshold for eligible disposable
entries is unchanged. No extra model turn, provider, quota or fallback is involved.

Five failures on the old source reproduced live-process termination, deletion of
an open file, deletion of the caller's cwd, deletion after failed ownership
inspection and loss of resumable workspace data. Fifteen final regressions use
real kernel-backed child processes and controlled process visibility, and cover
missing inspectors, incomplete scans, normal disposal and fresh-entry behavior.
Four further failures exposed symlink/relative command paths; six combinations
now verify that the same process resumes reading its input after the sweep.
An additional cadence/scope test verifies two profile homes after the first hour.
All 58 cases across nine relevant native files pass offline, with zero retries.
Existing explicit reaping tests still verify their audit and cleanup contract;
the worktree test now verifies retention rather than automatic destruction.

These checks do not establish recovered production bytes or response-time savings.
An unreadable process must remain unknown. No live sweep should bypass that refusal
to manufacture a successful cleanup. The immutable v0.3.1 release is unchanged.


## v0.3.2 release verification

This release packages growing-file preview bounds, active/resumable scratch
retention and the explicit offline backup-compaction helper. The cumulative
source inventory contains 295 files, including 120 native Python test files.
A fresh integration run passed 215 distinct cases in 23 relevant native files,
with zero failures and zero retries. Companion tools and examples separately
passed all 75 cases. These counts do not add earlier overlapping runs.

The full patch passed fresh base/apply/installed verification on the pinned
upstream revision. Locally installed runtime bytes were matched against all
175 runtime inventory entries. Installed-source retention was separately
exercised with network/process/signal actions denied. Unknown process ownership
correctly deferred deletion; this is preservation evidence, not reclaimed bytes.
Runtime lifecycle acceptance is deployment-specific and does not certify an
actual hourly sweep or production usage/RAM/latency improvements.

Release files, reachable Git history, private-identifier checks and known private
credential comparisons are reviewed before publication. Runtime data, backup
archives, local configuration and operational receipts are excluded from the
public archive. Earlier releases remain immutable.


## Derived-cache disk-pressure preservation (after v0.3.2)

The first post-v0.3.2 change added one regression file, bringing that inventory to 296
source/test files, including 121 native Python test files. A fresh relevant native
run passed 59 cases across eight files, with zero failures and zero retries. These
cover document conversion, persistent search reuse, cross-process exclusion and
existing expiry/profile boundaries. Eight new cases cover low/unknown free-space
measurements, failed temporary-file creation/publication, replacement at capacity,
normal quota enforcement and encoded-byte admission at the reserve boundary.

Five cases first failed on the prior implementation; a separate encoded-byte
boundary case also failed before the fix. Disposable derived-cache payloads now
leave a one-GiB free-space reserve on their own filesystem. Replacement publication
finishes before evicting other hits, and replacement accounting excludes the old
version of that same key. Existing per-entry, total-byte, count and TTL policies
remain in place under the existing index lock. An in-progress publication can
temporarily require one additional bounded file; admission accounts for its full
encoded size.

Installed-source offline acceptance used real temporary cache files with network,
process and signal actions denied. In the synthetic failed-publication workload,
three conversion executions before the fix became two with the installed fix
because the previous hit survived. A simulated full filesystem produced zero
new cache payloads. These results do not establish production token, RAM or
latency savings. The reserve gates derived-cache payloads; it does not govern all
other application or filesystem writers. No new model requests, paid fallback,
quota changes, hard RAM limits or embedding-service actions are introduced.

The v0.3.2 release and its archive remain immutable. This post-release change is
identified separately on main and passes fresh full-patch compatibility checks
against the same pinned upstream revision before publication.


## v0.3.3: storage pressure and idle-only update safety

The cumulative patch now contains 300 source/test files, including 122 native
Python test files. A fresh combined run passed 144 native cases across 15
relevant files with zero failures and zero retries; two existing platform cases
were skipped on the test host. The 75 companion cases are checked separately.
Earlier overlapping results above are historical and are not added to this count.

Two reproduced predicate failures showed that unreadable background-process or
delegation observations could be interpreted as idle. The predicate now keeps
the host awake on either failure. The new opt-in control request uses a separate
verb, so an older server cannot ignore an idle condition and silently run the
legacy bounded-drain request. Admission checks native work on the Gateway loop
immediately before restart. Old explicit pause behavior remains covered.

New control tests use the production socket setup and a real native registry
process: an idle-only update is refused while its script is alive, then the same
script resumes and finishes after release. Other cases cover active agents,
unreadable cron/API work, clean idle acceptance, older servers and expired queued
callbacks. The first legacy test harness used a different temporary home than
the serving socket; correcting its home made the unchanged legacy control pass.
That harness failure is not counted as a runtime defect.

Local publication backs up only affected source files and records prior absence
for a new sibling. Bootstrap of the first strict-capable server requires a fresh
idle audit; future automatic activation requests require its strict ACK and do
not fall back to signals or legacy pause. Serving-process identity, canonical
source binding, file hashes and unchanged configuration are verified separately.
No model calls or live workload are created to manufacture acceptance.

The prior two native completed-card samples have incomplete log coverage and
predate these fixes; they do not establish after-patch RAM, latency or usage
savings. Production impact and autonomous goal/skill behavior remain separate
acceptance work. Public archives contain source/examples only, never private
operational receipts, live databases or credential stores.

## Native Captain goals and delegated decisions (v0.3.4)

The Captain policy and new on-demand goal-driven-execution skill describe authority for reversible implementation choices, bounded correction, parallel ready work and verified delivery. Material scope/cost/access/irreversibility and rights/review/publication decisions retain their gates. This is guidance within existing native permissions, not a guarantee of autonomous model behavior.

The native `hermes goal status|show|ensure` command uses the current bound session/profile and existing GoalState/contract store. Self-setting defaults off and requires profile opt-in. It preserves active/paused/cleared goals, existing caps and concurrent owner changes. Status avoids transcript/system-prompt materialization. Setting metadata invokes no judge, kickoff, dispatch or model. The CLI refreshes goal state at its existing post-turn boundary, preserving cached state and skipping evaluation if observation fails.

Final new-file acceptance: **26 native tests passed, zero failures**, with zero retries. Controls cover actual SQLite state/contract persistence, parser integration, profile/session scope, missing/closed sessions, disabled profiles, preserved pauses and budgets, concurrent writes, worker refusal, bounded stdin, stale CLI state and a committed write whose readback fails. The initial adoption harness used the wrong mixin; after correction, all three stale-state cases failed against the unchanged implementation and passed with the fix. A separate full relevant goal/parser run passed **182 cases in eleven files**, including the earlier 25-case revision of the new file. These overlapping results are not added together.

Installed-source acceptance used native read-only session metadata and skill discovery/view with network denied. Existing retained paused goal metadata remained byte-identical; when its session record was absent, the helper correctly refused to reactivate it. A current existing open session was inspected without setting a test goal. The profile changed only its explicit self-management permission plus generic instruction/skill content; models, quotas and existing turn caps were preserved. Source-only rollback backed up approximately 529 KB of source and two small profile files, with no database snapshot.

No model request or live synthetic worker was used for these checks. Skill discovery and metadata inspection do not prove that an existing cached Captain has already read new guidance or completed autonomous work. Use normal authorized work to establish that evidence, and retain the idle activation and prompt-prefix constraints described in the goal guide. The patch inventory now contains 305 source/test targets: 182 runtime files and 123 Python test files. Historical acceptance counts above remain historical.

## Atomic continuation controls (v0.3.5)

Native goal, heartbeat and loop migration previously used separate best-effort child-copy and parent-clear writes. The save functions suppressed write errors, so migration could report success and clear the parent after a refused child write. Refusing the parent archive could instead leave both rows active. An unreadable child value could also be mistaken for absence and overwritten. Real temporary SQLite triggers and simultaneous native writer calls reproduced these failures before implementation; no live incident or model request was created.

The three existing migration entrypoints now use one native SessionDB transaction. Reads, exact child-value insertion and parent archival share the native writer's lock, commit/rollback and storage-identity guards. Any existing child metadata is preserved, including cleared or unreadable state. Pauses, counters, caps, waits, routing and unknown checkpoint fields remain intact. Concurrent continuation attempts commit at most one child. A failed or unconfirmed transaction returns false; it is not permission to replay compression or model calls. Compression itself retains its existing best-effort behavior. Recovery of continuation scheduling after persistent storage failure still requires normal-work evidence; this change protects durable state and does not establish automatic recovery for every storage fault.

Fresh native acceptance: **228 passed, zero failures, six files, zero retries**. This includes **30 new cases** for child/parent write refusal, full rollback, existing child data, active/paused/done/cleared states, concurrent continuations and profile isolation. The other files exercise existing goal, heartbeat, loop, self-goal and real compression-rotation paths with model boundaries replaced offline. The new file initially produced 23 failures and seven passing controls on the unchanged implementation; those overlapping development runs are not summed.

Installed canonical-source acceptance passed **12 cases** using an explicitly isolated native store, with network denied and no live goal changes. Existing source baseline bytes were reused for rollback: **132,249 bytes** covering three original files plus one original absence, without a database snapshot. All 97 observed config/SOUL hashes stayed unchanged during installation.

A trace of the actual native SQLite writer measured these successful single-migration workloads:

| Control | Before committed transactions | After committed transactions |
|---|---:|---:|
| Goal | 2 | 1 |
| Heartbeat | 2 | 1 |
| Loop | 2 | 1 |

This is an offline transaction-count measurement, not production usage, disk-byte, latency or RAM savings. The observed retained live orphan-goal metadata has not been attributed to this failure class and was left unchanged. Current public inventory: **309 source/test targets**, including **185 runtime files and 124 Python test files**. Historical acceptance above remains historical.

## Local memory attribution (v0.3.6)

The private Gateway control socket now accepts an explicit `memory-stats` request.
It reads scalar process/cache/tool/registry observations without formatting cached
values, opening a session database, trimming memory or starting inference. Normal
status stays unchanged. The optional allocation query observes an existing Python
profiler; it never enables one. A registered native startup option permits a
deliberate idle profiling window and defaults to disabled. The Gateway's runtime
settings initialization moved into a small sibling, reusing one effective config
snapshot for timing and diagnostic settings while retaining existing getters.

Fresh native acceptance passed **72 cases across nine relevant files**, with
zero failures, zero retries and **one legitimate skip**. Eighteen passing cases
in the new file cover real local-socket dispatch, private-value exclusion,
nonblocking registry counts, unavailable SQLite tracking, no database/trim side
effects, allocation-path sanitization, bounded startup settings and real native
Gateway configuration consumption. The SQLite allocator integration case skips
when the host extension does not export the required symbols; a skip is not a
successful allocator measurement. Companion examples/tools are checked separately
and historical overlapping test counts are not added.

Installed-source acceptance observed the actual Gateway through its native local
socket after an idle-only lifecycle change, matched the runtime source inventory
and preserved configuration. A temporary startup profiling window produced
aggregate allocation metadata without a model request. Returning to a normal
process was verified separately. Profiling itself consumes RAM/CPU; its overhead
must not be presented as a leak, workload speed or savings. These observations
identify areas for further investigation and do not establish a root cause or
production reduction in memory, tokens or latency.

The cumulative inventory contains **312 source/test targets: 187 runtime files
and 125 Python test files**. Full patch compatibility is checked against the same
pinned upstream revision. Public release artifacts include generic source,
examples and documentation only; private runtime measurements, configuration,
backup files and operational receipts remain excluded.

## Reuse immutable bundled locale parses (v0.3.7)

An isolated native 36-home workload reproduced repeated parsing of the same
bundled English source. Every home retained a separate set of flattened keys and
translation strings even though the file was unchanged. Three new tests first
failed on repeated profile reads, overlay resets and concurrent cold loads; five
other controls already passed. Sharing whole merged catalogs would mix private
overlays, and sharing plugin modules would change plugin state isolation, so
neither is part of this repair.

A small sibling now reuses the native parser's immutable result for a verified
source file. A serialized standard-library LRU retains at most 32 source versions;
file identity, size, modification/change stamps and ownership/mode invalidate its
key. Each caller receives a new mutable dictionary. Existing overlay/plugin
precedence, missing-file fallback, packaged locale roots and error reporting are
preserved. No configuration switch, provider route or model tool was added.

One offline reproduction before and after the change measured this specific
cold locale-loading path:

| Measurement, 36 homes | Before | After |
|---|---:|---:|
| Bundled file parses | 36 | 1 |
| Distinct mutable catalog dictionaries | 36 | 36 |
| Retained traced Python bytes | 29,041,096 | 6,687,904 |
| Elapsed seconds with allocation tracing disabled | 5.308 | 0.161 |

The retained-allocation difference is 22,353,192 bytes (about 21.3 MiB) in this
synthetic workload. Timing and allocation measurements use separate processes;
the timing row excludes profiler overhead. These single-run results describe
this path, not overall Gateway startup, provider response time, token use or
all production RAM. No inference or live task was created for measurement.

Fresh combined native acceptance passed **163 cases across fourteen relevant
files**, with zero failures, zero retries and one existing SQLite-symbol skip.
This includes eight new locale cases and two new observation cases. Controls
cover private overlays, caller mutation, same-size edits with restored mtime,
atomic replacement, packaged roots, concurrent reads, failed/missing sources,
bounded reuse, plugin precedence and CLI/TUI/Gateway consumers. Historical
overlapping runs are not added to this count.

Installed canonical-source acceptance compared all 3,433 entries across 36
isolated native catalogs and verified overlay isolation, with network/process
actions and live-state reads denied. The first acceptance harness refused a
required managed Python library read before reaching behavior checks; permitting
only the interpreter's declared library directories corrected that harness.
No runtime workaround or dependency change was needed.

After native idle-only activation, the actual Gateway's local observation showed
one populated bundled cache, one computation miss and repeated hits. The new
counter reads an already-loaded cache and exposes no paths, translation values or
profile identities. Runtime source hashes, source permissions and unchanged
configuration were checked separately. Process RSS snapshots across a restart
are not a controlled production savings benchmark, so no causal whole-process
reduction is claimed from them.

Only affected source files were backed up; no database snapshot was made. The
complete inventory is **315 source/test targets: 189 runtime files and 126 Python
test files** against the same pinned upstream revision. Release files, reachable
history, metadata and archives undergo the existing privacy review before
publication. User goals/pauses, quotas, accounts, models, project gates and
embedding services remain outside this change.

## Share immutable bundled plugin code (v0.3.8)

Native plugin discovery followed by Gateway configuration materializes platform
adapters under separate profile namespaces. A four-home reproduction created
328 modules from 82 source files with no messaging platform enabled. The dominant
allocation site was Python's repeated bytecode decoding. Module isolation is
intentional: sharing module objects or skipping configuration hooks would change
behavior. This repair shares only immutable compiled code and its constants.

Eligible bundled imports use Python's existing per-directory importer cache with
a bounded source loader. Each execution receives a new native module/globals
dictionary. Source paths, content digests and interpreter optimization distinguish
code versions; current source access is checked on hits. Changed files cannot
inherit stale timestamp-only bytecode. Old sibling modules remain unchanged until
their own reload. Native private-plugin imports, host routing, custom importers,
extension/sourceless loaders, permissions and activation/registration gates are
preserved. The cache does not store module globals or live configuration.

A controlled offline comparison ran the original loader and the installed
candidate's logic in fresh processes, with networking and process actions denied
apart from native checkout-local read-only version metadata. The original loader
was observed loaded before restoring the isolated development checkout; canonical
runtime source was not changed by the baseline experiment. Both workloads served
36 synthetic homes, materialized 2,952 scoped modules from 82 source files, kept
the same registry/compatibility outcomes and enabled zero messaging platforms.

| Untraced offline workload, 36 homes | Original | Candidate |
|---|---:|---:|
| Process RSS after discovery/configuration | 486,899,712 bytes | 224,198,656 bytes |
| Process PSS at the same stage | 475,310,080 bytes | 212,675,584 bytes |
| Elapsed discovery/configuration | 10.161 s | 8.985 s |

This single-run workload observed about **250.5 MiB less RSS** and a shorter
component startup time. Allocation tracing was disabled for these rows. The first
cold profile incurred extra compilation/allocator cost; benefits are established
for this multi-profile reproduction, not every single-profile process, end-user
response time or token usage. The cache retains at most 128 code versions and
loads sources above one MiB without caching; it is not an application-wide RAM cap.

Fresh native acceptance passed **242 cases across thirteen relevant files**, with
zero failures, zero retries and one existing SQLite-symbol skip. Four initial
reuse/reload tests failed on the prior implementation; a later initializer control
also failed before its corresponding change. The new file now passes fourteen
cases covering independent scopes/state, nested imports, force reload, same-size
edits with restored mtime, unaffected siblings, concurrent loads, current source
read refusal, custom finders/loaders, large sources, failure cleanup, sourceless
imports, cache eviction and private-plugin passthrough. Two new diagnostic cases
verify count-only observation and no initialization of an absent cache. Existing
plugin lifecycle, historical compatibility, event, host-isolation, registry and
config-loader tests are included; earlier overlapping runs are not added.

Installed canonical-source offline acceptance separately verified code reuse,
independent profile state, fresh reload and preservation of a sibling's old code,
with live-state reads and network actions denied. Native idle-only activation then
produced positive code-cache reuse counters from the actual Gateway. Runtime
source hashes and unchanged configuration were checked. Idle RSS snapshots across
that restart are operational observations, not a controlled benchmark for every
production workload. No inference work was created to obtain evidence.

Only three affected runtime source paths were installed after small source-only
backups; no database snapshot was made. Cumulative inventory: **318 source/test
targets, including 191 runtime files and 127 Python test files**, against the same
pinned upstream revision. Public files, reachable history, metadata and release
archives are reviewed before publication; private measurements, source locations,
configuration, credentials and operational receipts remain excluded. Quotas,
models, accounts, goals, user pauses, project gates and embedding services are
unchanged by this source repair.

## Trustworthy compact bot activity (v0.3.9)

The cumulative inventory now has **332 source/test targets**, including **131
Python test files**. This update fixes three reproduced presentation boundaries:
compression-tip rows retaining root activity fields; worker projections omitting
bounded detail and terminal time; and recently completed/offline workers still
qualifying for worker-driven activity. Bot rows now use the native tools icon
with a short description and a full localized tooltip, keeping the canonical
conversation preview and opening route unchanged.

Regressions were observed failing before implementation. Fresh offline native
acceptance passed **64 cases across seven files**, with zero failures or retries.
Separately, **67 renderer cases across six files** passed, including canonical
opening, no pre-warm on paint, terminal/offline behavior and locale coverage.
The renderer type check and production renderer build passed; the changed scope's
native code-health comparison reported zero new findings. These are separate
checks, not a sum of historical suites.

The installed native source was then checked with **nine cases across two files**
using the canonical runner. This is a subset repeated against the installed
location, not nine additional unique cases. Only selected source/test files were
published locally; permissions and ownership were restored, configuration hashes
were preserved and no database backup/restore was performed.

Browser validation used actual native components, production-generated styles
and synthetic data. Active detail, terminal clearing, offline exclusion, title
fallback and unchanged canonical preview were verified; the final observed
console had no errors or warnings. Private fixture issues were corrected without
changing production behavior: home isolation was incomplete, a generated Vite
cache was eligible for source transformation, and rebuild output was being watched
as fixture styles. The same 2 GiB child heap cap was retained; no dependencies,
model requests, quota settings or paid routes were added.

Native worker recency is not process-liveness proof. No end-to-end live workload
or model-token saving is claimed from this UI change. The current local source
is installed, but activation of the already-open Desktop and Gateway remains a
separate idle-lifecycle check; the redesigned Workbench mockup is not deployed.
Historical benchmark and regression counts above remain separate.

## Metadata-only runtime bindings (v0.3.10)

The cumulative patch now has **333 source/test targets**, including **132 Python
test files**. Small model-config reads no longer hydrate a session's full system
prompt or tool context. The full-session reader and existing runtime binding
semantics are preserved; this is a projection change, not an additional cache.

Two native read-policy regressions first failed on the previous implementation
when SQLite denied prompt access. Fresh acceptance passed **73 cases across seven
files**, with zero failures or retries. The new file contains three cases:
normal/read-only thread binding under the read policy, plus default/null/nested
value and committed-update controls. Existing read-pool, session-route and
onboarding consumers are covered by the wider run. The scoped native code-health
comparison found no new findings.

The same three new cases then passed against the installed canonical source.
This installed check is a subset, not three additional unique cases. Installation
changed one source file and one test file after fresh idle/ownership checks, with
a small source-only rollback, exact permission restoration and unchanged
configuration. No database copy or restore was performed.

The [isolated measurement](session-metadata-reads.md) uses a synthetic context and
reports lookup time and traced Python allocations only. It does not establish a
whole-process RAM, production token, total response-time or billing improvement.
No model call or provider/allowance probe was made for this change. Existing
quotas, fallback policy, session models, user gates and embedding services remain
unchanged. Runtime activation is a separate native idle-lifecycle observation.

The new release inventory carries its own version label; earlier immutable tags
and archives are not rewritten. The redesigned Focus/Workspace interface remains
an interactive prototype and is not included as a deployed redesign in this
source release. Prior overlapping test counts remain historical.


## Native Focus and Workspace (v0.4.0)

The exported patch now contains **352 source/test targets**, including **134 Python test files**. Unlike the earlier prototype-only work, this release contains native renderer components and an owned-session configuration intent. The original composer, transcript, bot roster, layout tree and plugin routes remain in use.

Fresh UI acceptance passed **85 cases across ten files**, with zero failures. These cover navigation and native session doors, late plugin registration, separate layout scopes, goal drafts and explicit saves, busy/stale refusal behavior, Ctrl/Cmd+Enter containment, unknown evidence and existing session-control behavior. A render regression exercises 100 unrelated streaming updates without another shell commit or an implicit read while Catch up is closed. This is a component-level observation, not a whole-app speed or token measurement.

The native session-control file passed **31 cases**, including the new goal form, preserved counters/gates/waits, busy refusal, stale revision, declared input shape, configured turn limits and malformed-limit refusal. Generated TypeScript/OpenRPC checks also passed. A wider goal-command/gate run passed during development; its overlapping counts are not added here.

Renderer typechecking and the production renderer build passed. The scoped before/after code-health comparison covered 23 changed files with no new blocking or advisory findings. No dependencies, account bindings, quotas, fallback routes or embedding services were changed.

Rendered review used the actual native presentation components with synthetic data and no live transport. It covered desktop Focus/Workspace, goal and feature dialogs, and 320/360-pixel child viewports. Review found and corrected a wrapped rail caption, crowded secondary form fields and narrow-screen navigation overflow. Browser tests used a test-only registered language pack to check the Thai strings; production language selection was not altered. The desktop package was built using existing admitted tools and verified staged assets; replacing or loading an already-open app remains a separate graceful idle-lifecycle step.

English guides and the complete cumulative patch are distributed; private host reports, configuration, conversations and screenshot fixtures are not. Public files, all reachable Git history, and the exact release archive are reviewed before publication. Companion/archive acceptance is recorded separately from native regression evidence. Real workload billing, cross-bot cache sharing and live model behavior are not inferred from these tests.


## Goal draft ownership (v0.4.1)

An offline native-component regression reproduced a dismissed Goal draft appearing in a second chat when both chats already had cached, empty control snapshots. Empty native controls legitimately share an empty state revision, so a revision check alone cannot identify which chat owns an unsaved form.

The editor now starts a separate component instance when its pinned runtime session changes. Reopening it in the same chat still retains the dismissed draft; opening it in another chat starts from that chat's native goal state. Background state updates continue to leave the open, pinned draft alone. No model prompt, automatic goal start, quota change or new persistence store was added.

The regression failed before the change and passed afterward. The relevant UI suite passed **85 cases across ten files**, with zero failures; this run overlaps the v0.4.0 evidence and is not an additional 85 independent cases. The full renderer TypeScript check passed, and the two-file native health comparison reported zero blocking or advisory findings. Native Python behavior was unchanged and its earlier suites were not repeated. Desktop package loading remains a separate graceful lifecycle step.


## Per-Captain setup checks (v0.4.2)

This documentation update makes profile-scoped goal opt-in and skill discovery explicit for every intended Captain, including the terminal's current launch home. A Desktop selection does not select the terminal profile. The native source patch, its 352 targets and all default permissions are unchanged. The guide supplies a short on-demand instruction pointer instead of copying the whole execution method into every conversation prefix.

A separate local adoption check used the native configuration writer to enable only the requested profile's self-management permission. A raw semantic comparison preserved every other configuration value, including model/provider settings and existing limits. The existing published skill was installed without modification, and native skill discovery/view resolved the exact published bytes. Session-database access and network/model actions were denied during those checks; no goal was created, resumed or replaced. A plugin initializer was refused by the strict inspection guard, so this is not whole-plugin runtime acceptance. Existing file permissions and process identities were checked separately.

These are configuration and discoverability results, not evidence that a cached Captain has consumed the guidance or completed autonomous work. Actual behavior still needs a normal authorized task. No source or UI suite was repeated for this documentation-only update. Earlier test counts remain historical; exact release inventory, archive, privacy and Git-history checks are performed for this release.


## Compatible startup checker reuse (v0.4.3)

The cumulative inventory now contains **354 targets**, including **135 Python test files**. One runtime source file and one regression file extend the prior release. A selected PM checker can belong to a different launcher scope while a matching published checker remains cached. Previously, no-bootstrap resolution refused that cache and bootstrap resolution tried preparation. Two regressions reproduced those behaviors before the fix.

The resolver now reuses an exact compatible published generation under the existing preparation lock and child lease, without rewriting the current selection. The native application dependency check still decides whether dependencies are current. The regression matrix covers no-bootstrap and bootstrap cache hits, selected-generation priority, corrupt/non-object/missing/mismatched publication metadata, directory/marker symlinks, unusable interpreters, selection preservation and collector protection.

An eight-file native PM/source-launch run passed **55 tests**, with zero failures and one existing Windows-only skip on Linux, using the canonical per-file runner with zero retries. After a test-only table refactor required by code health, the final new regression file passed all **10 cases**. A separate existing symlinked-home alias regression passed. These runs overlap and are not summed. No dependency bootstrap integration test requiring installation was executed. Scoped code health reported zero new blocking or advisory findings.

After a guarded two-file local source adoption, an actual native `venv_is_current` request under the existing Desktop wrapper runtime scope returned true where the preceding observation had returned false. It used one preexisting unselected compatible checker and the normal native read-only worker. PM selection, application environment selection, dependency facts, lockfiles and 99 guarded configuration/skill inputs stayed unchanged; no PM generation was created. The normal validation/worker lease mechanism was allowed. Desktop/Gateway identities were preserved. No model request, service restart or additional Desktop launch was performed.

This establishes repair of the false stale-dependency check. The earlier observed launch delay is not assigned entirely to this defect, and no end-to-end latency or token saving is claimed. The next normal launch and authorized work remain the acceptance path for those measurements. Public payload, history, archive and identifier/credential review are performed separately before publication.

## Native work-surface correction (v0.4.4)

The original Focus release changed navigation, but a real user report showed that the old Sessions navigation and a dense Kanban still competed with it. New regressions reproduced 2,000 completed cards mounted on the current-work canvas, the Sessions pane remaining open beside Work, mismatched Models/Usage destinations and a Bots rail selection that did not follow the actual visible pane. These cases failed before correction.

The cumulative export now contains **369 source/test targets**, including **135 Python test files**. The patch retains the same pinned upstream base. It changes native presentation and navigation, not credentials, quotas, task ownership, dispatch or model routing.

Current offline acceptance: **483 cases passed across 66 native UI test files** covering Focus, the real sidebar and Kanban components, compact Intro, and affected existing fixtures. The navigation file was rechecked after a TypeScript-only fixture correction. TypeScript checking and the scoped 21-file code-health ratchet passed. These overlapping runs are not added together.

A broader UI run completed with 10,911 passing cases, five failures and two asynchronous fixture-teardown errors. The identified title/fixture problems were corrected and their targeted tests passed. A later full run ended with SIGTERM before its summary, for an unproven reason. This release therefore does **not** claim an all-upstream UI-suite pass. Existing storage/provider/dialog fixtures retain their behavior assertions; no failing test was removed or weakened to force a green result.

A separate real Electron main/preload/renderer and real native backend were launched with disposable home, user-data and account directories. **40 entry/interaction checks and 71 settings subpages passed** after waiting for each actual surface. Checks included the parked fixture card's native detail dialog, search and restoration, empty History return, New task open/cancel, feature search, Models/Usage selection, Bots highlighting, and laptop-width rendering. No renderer exception or failed native HTTP response was observed in the final journey.

The fixture task was explicitly blocked and unassigned in the disposable database. It had no worker, run, fabricated completion or production receipt. Model metadata requests went only to a local test server; inference endpoints were not called. External backend networking and optional tool installation were denied. Earlier harness attempts had readiness, viewport and navigation-selector mistakes; their failures were retained privately and are not counted as application regressions or passing acceptance.

This is real isolated-app acceptance, **not** hands-on control of an existing production window. It does not test authenticated provider calls, paid fallback, sending messages, execution/scheduling, downloads, audio, GPU work or destructive actions. Hosted catalogs and update checks can report unavailable under offline guards. Opening those screens is not proof of their external services. Deployment still requires a normal idle lifecycle; source or staged-package readiness does not prove that an already-open Desktop loaded the correction.

No prompt, production screenshot, session/task/run identity, machine-specific test launcher, private log or account data is distributed with this record. The public patch contains portable native component regressions. No model call, quota probe, new dependency or paid fallback was used to produce this acceptance.

## Native Spaces, Workflow and richer chat (v0.5.0)

The cumulative patch contains **413 source/test targets**, including **138 Python test files**, against the same pinned upstream base. Workflow exposes actual dependency edges and recorded attempt history. The full Bots workspace and one Focus rail use native navigation. Library disables unready previews; chat retains native Markdown/Mermaid with optional literal-data cards. Spaces adds explicitly shared local pages/file copies and read-only member access.

| Acceptance | Result | Boundary |
| --- | --- | --- |
| Relevant native UI tests | 201 passed across 34 files | Workflow ancestry/history, navigation, preview transport, answer cards, session-picker clicks and Spaces |
| Current native Python tests | 38 passed, 6 platform skips across 3 files | Board API, filesystem and Spaces; canonical runner, zero retries |
| TypeScript | Passed | Complete Desktop typecheck |
| Scoped code health | No new blocking or advisory findings across 47 paths | Compared with exact prior installed bytes/absence |
| Isolated real Electron UI | 55 flows and 71 settings pages passed | Actual main/preload/renderer and native backend with disposable homes |
| Model calls / external-app opens | 0 / 0 | Inference POSTs counted; external application opening refused and counted |
| Renderer exceptions | 0 | Final candidate journey |

Native UI checks covered fork/join dependency paths, recorded bot attempts, selection of a destination's upstream path, native-card opening, missing/archive files disabled before preview, text/nested folders, sanitized HTML, PDF, audio, images, Bots groups/search, session selection with a stationary pointer, a real native chat displaying a table/cards/Mermaid, and desktop/narrow layouts. The recorded task attempts are canonical native test fixtures; no bot or worker was spawned and no production execution receipt was manufactured.

Spaces acceptance created a Space with two explicitly selected profiles, wrote a page, imported a chosen fixture file, opened it internally, removed it after confirmation, restored it and verified the original file bytes stayed unchanged. The owned test app's file-chooser selection was supplied by the harness; actual native file reads, import API, storage, preview, trash and restore were exercised. Separate backend regressions use two genuine named-profile environments to read the same canonical store/content hash, deny a nonmember and a revoked member, reject stale writes, bound text reads and refuse export overwrite. This proves API/CLI policy on test profiles, not operating-system isolation or a live model's behavior.

A delayed preview arriving after switching Spaces is discarded. An actual stationary-pointer session selection failure was reproduced in the isolated app and fixed at the native command-menu pointer policy, rather than forcing the test to click through it. Earlier harness launch/profile-seed and double-serialized preview-body failures were retained privately; the final real journey passed after correcting them. Existing wider upstream-suite limitations from v0.4.4 remain in force. Earlier overlapping counts are not added to this acceptance.

No production conversation, screenshot, task/run identity, credential, machine-specific launcher or private log is shipped. Source adoption, packaged build, fresh-process activation and isolated interactions remain distinct evidence. No direct production-window visual control is claimed where enabled native controls are unavailable. No model request, allowance probe, dependency installation, quota/fallback change or embedding-service action was used for this acceptance.


## Unified Hub and persistent Focus sidebar correction (v0.5.1)

A real user report identified the exact trigger: pressing the old top-left sidebar toggle restored the legacy Sessions/Bots column despite the new Focus rail. Two offline regressions reproduced it through the real positional layout action with an already-closed sidebar preference and through the actual titlebar control. Both failed before the correction.

Focus now omits the old titlebar trigger, refuses the legacy positional/sidebar toggle actions in the main window, and observes the actual collapsed-side state in addition to the old per-pane flag. Wide and secondary-window controls keep their existing behavior. A separate real-store regression reproduced a stale Focus listener closing the Wide sidebar during the mode switch; the callback now rechecks the current mode before closing anything. Its draft-preservation and mode-switch cases passed, including a real isolated-app round trip. The layout scope, sessions, draft text and running backends are not destroyed to hide a panel. Existing right-side/flip/persistence tests retain their behavior checks.

Hub combines Library chat outputs and shared collection items in one destination, header, search and type filters. Named collections retain explicit bot membership; chat outputs are not automatically copied or shared. Existing `/artifacts` and `/spaces` links resolve to the Hub surface. The new owner aggregate returns at most 1,000 non-trashed metadata records in one query, with no content bytes or bot CLI privilege change. The existing bounded transcript index and native file viewers are reused.

Fresh acceptance: **97 native UI tests across 16 files**, **35 native Python tests with six existing platform skips across two files**, complete Desktop typecheck, and scoped health checks across **20 paths** with no new blocking/advisory findings. An isolated real Electron/backend journey passed **57 flows and 71 settings pages**, including the missing titlebar trigger, sidebar keyboard action, mixed-source search, internal previews, collection membership, import, trash and restore. No inference POST or external application open was used. An initial harness expected an exact page name without its new collection-provenance caption; correcting the accessible-name match exercised the same real control successfully.

The cumulative export has **419 source/test targets** and the same pinned upstream base. Companion and fresh-checkout patch acceptance are regenerated separately. Earlier overlapping counts are historical, not added here. No model prompt, toolset, quota, fallback policy, user gate or embedding service is changed. Source installation, package preparation, graceful activation and isolated visual checks remain separate evidence.

## Main-window history access and quiet Slack status (v0.5.2)

The remaining sidebar trigger was reproduced in main Wide mode. It is now omitted in both main modes, and the legacy column stays closed through mode changes and the sidebar shortcut; secondary-window controls keep their native behavior. A direct History door restores saved-chat access without bringing back the crowded column.

A native database regression seeded an older conversation followed by 205 newer ones. The prior route ignored the requested search and returned 50 newer records; the corrected route finds the original saved title or ID. History requests bounded 50-row pages, searches only after explicit submission, surfaces read errors, and binds results/cache/selection to the captured connection and profile. A delayed old-owner response is discarded. The isolated real application searched and opened the older saved transcript by its existing ID without inference.

The Slack regression exercised the actual base-adapter/runner lifecycle with an in-memory wire transport. Turning off automatic status notices previously still sent the paused boilerplate; it now emits nothing while the emergency stop remains engaged. Default-on behavior, other-platform notices, recognized control commands and multiplexed per-profile notice routing retain their tested contracts. This is offline wire-policy evidence, not a live Slack delivery test.

Fresh verification covers 203 native Python tests for the history route and existing web server, 10 relevant Gateway tests, the targeted native UI tests, complete Desktop typecheck, and 19-path scoped health with no new blocking/advisory findings. An isolated real Electron/backend journey passed 58 flows and 71 settings pages with zero renderer exceptions, inference POSTs or external application opens. These counts describe separate suites and are not combined with previous overlapping acceptance totals.

The cumulative patch contains 432 source/test targets against the same pinned upstream base. Production adoption, graceful Gateway reload, packaged Desktop activation and isolated UI interaction remain separate evidence. No production conversation, credentials, Slack message identifiers, private configuration, screenshots or cleanup reports are exported. Companion tests and fresh pinned-checkout patch acceptance are regenerated separately before publication.


## Native feature parity and older-search pinning (v0.6.0)

Twelve gaps were confirmed by a separate read-only comparison of the original interface, native routes/actions and the new presentation. The release restores the full saved-chat/project manager in both modes; native history row actions, filters, pins and archived view; bot/group/section/Screen entries; visible device/profile context; combined goal/loop/heartbeat controls; pane/status-only plugin discovery; cache accounting display; and friendly route labels. See [the usage matrix](desktop-feature-parity.md).

Fresh final UI acceptance: **34 files, 303 tests passed, zero failures**. This includes profile/connection routing, project creation and native project/worktree menus, bot sections/groups, Screen identity boundaries, plugin registration/error isolation, session actions and pin synchronization, cache unknown/invalid/zero arithmetic, retained drafts, and delayed control submission bound to the original chat. Historical overlapping runs are not added to this total. Type checking passed. Scoped source-health review reports zero blocking findings and zero advisories against this change's baseline.

The actual isolated Electron main, preload, compiled renderer and native backend passed **21 interaction steps**, with zero inference POSTs, zero unexpected external applications and zero renderer errors. Checks include search outside the newest 200 rows, native row menus, an actual older-chat rename/pin, filters, a single project dialog, native bot/group forms, actual local section creation, the New Bot palette path, context selection without changing owner, synthetic pane/status plugins, a disabled-plugin boundary, provider-reported cache display from synthetic counters, combined paused goal/loop/heartbeat state, Focus/Workspace and a narrow viewport. Some earlier UI harness selectors used a visible caption instead of its accessibility name; corrected selectors are retained separately from the product regression.

The interaction review exposed an additional product defect: a search-only older conversation lost its visible pin after search was cleared. Regression tests first reproduced dropped profile metadata and the absent adoption path. The repair retains the native search owner and makes the row available before existing pin synchronization. The final native rename/pin journey passes. Fresh loaded records and a same-ID record belonging to another profile are preserved.

The cumulative patch contains **466 source/test targets**, including **326 paths outside the Python test tree and 140 Python test paths**, against the unchanged pinned upstream base. Private production source adoption changes 47 exact files, preserves 99 configuration/instruction inputs and existing process identities, and copies no databases. Packaged activation remains a distinct graceful-lifecycle step. Gateway/backend routing and scheduler code are unchanged by this UI release.

These checks do not authorize or prove a native introductory model call, remote Screen connectivity, real private-monitor behavior, production cache savings or cross-bot cache sharing. The model-free form checks open and cancel native bot creation. Private installed plugins are inspected for registration compatibility; synthetic plugins test their registration shapes without executing private behavior or enabling a monitor. Existing pause, quota, review, owner and no-paid-fallback gates remain in force. No local embedding service is changed.


## Always-visible workspace context (v0.6.1)

The owner requested device/profile information on screen without opening an information popover. Eight source/test paths replace that dialog with a permanent context row above the native workspace. It displays real device/profile names and existing gateway connection state; the named profile selector invokes the established native selection action only after an explicit different choice. No new polling, profile fetch loop, model call or provider configuration is added.

Fresh offline acceptance: **11 files, 46 tests passed**; type checking and scoped source-health review passed. Regressions cover immediate visibility, native status updates, display-name updates, exact canonical profile selection, no owner action on mount or opening, no reset when reselecting the current profile, pending-selection refusal, placement outside the rail and retained native chat drafts. Existing connection-selector cases cover its routing and confirmation paths.

The real isolated Electron main/preload/compiled renderer/native backend passed **7 checks**, with zero inference POSTs, external application opens or renderer errors. It verifies the visible values before any click, readable checked menu entries, Focus/Workspace placement, opening an existing transcript and retaining an unsent draft. A 560-pixel responsive context check lowers the minimum window size only in the disposable QA application, then verifies the actual inner width and lack of context-row overflow; it does not change production minimum window settings or certify the entire app for mobile use. Light/dark screenshots are private QA evidence.

The cumulative patch now contains **469 source/test targets**: **329 paths outside the Python test tree plus 140 Python test paths**. Exact source publication, native package construction, graceful lifecycle activation and isolated UI interaction remain separately recorded. Existing runtime identities and 99 configuration/instruction inputs are preserved during source publication. No database copy or restoration, allowance probe, paid fallback or local embedding-service action is performed.


## User-perspective usability repairs (v0.6.2)

The review repaired nine usability areas: preview Back/history, full-history search discovery, Workflow fit/focus, explicit model usage at bot creation, skill selection and footer visibility, scoped Hub no-match recovery, reported bot model/provider badges, visible New chat and compact permanent context. Further interaction review removed automatic chat/profile navigation from create-only bot creation and delayed graph focusing until its layout is committed.

Offline regression coverage includes real native component behavior, profile/revision boundaries, exact-query search handoff and deliberate create-only versus introduction choices. Native isolated Electron acceptance uses more than 200 saved conversations, 17 task cards and installed skills, with inference denied. See the [usability guide](desktop-usability.md) for the actual controls and limits. UI checks do not certify remote Screen access, live provider authorization or production savings.

Final acceptance for this release: **15 UI files, 58 tests passed**, scoped source-health review reports no new findings, and renderer type checking passed. The actual isolated Electron main/preload/renderer/backend passed **10 journey checks** at 1280×900, 1280×720 and a 640-pixel narrow fixture viewport, with zero inference POSTs, renderer errors or external-application opens. A real disposable bot was created with introduction off, retaining the current profile and returning to the bot cards. The context row measured 45 pixels at laptop height, down from the reviewed 74 pixels. These results establish behavior in the isolated test; they do not establish production performance savings. The cumulative patch contains **479 source/test paths**, comprising **339 outside the Python test tree and 140 Python tests**.


## Follow-up interaction review (v0.6.3)

The baseline isolated UI reproduced three new behavior defects: Zoom out increased a fitted graph from about 27% to 35%, a repeated New chat retained the same unsent draft/tab, and Escape discarded an unsaved Hub document. The native create/preview/trash/restore lifecycle already worked and is preserved. Membership discovery and current-navigation/short-window access were also improved.

Final offline coverage: **9 UI files, 45 tests passed**; renderer type checking and scoped source-health review passed. Tests cover monotonic zoom, material discard confirmation, pending-save input locks and refusal retention, local member search with hidden/absent selections, route indication, exact native action forwarding and unchanged plugin restrictions.

The actual isolated Electron main/preload/renderer/backend passed **7 checks**, including the initial shell and six interaction journeys, at 1280×900 and 1024×600. The real disposable membership write, page save, edit discard, trash/restore and draft-preserving new tab all passed. Inference POSTs, renderer errors and external-application opens were zero. Source installation, package readiness and native activation remain separate evidence; these isolated interactions do not establish provider allowance or production token savings.

The cumulative patch contains **481 source/test paths**, comprising **341 outside the Python test tree and 140 Python test paths**, against the same pinned upstream base.


## Search and loading resilience (v0.6.4)

A fresh review reproduced whitespace-sensitive bot/Hub searches, redundant Hub filter reads, missing loading feedback and stale saved-chat search state on failed requests. New offline controls failed against the preceding behavior before repair. The first hook harness needed a partial module mock; that setup failure is not counted as a product failure.

Final scoped offline coverage: **6 UI test files, 30 tests passed**. Renderer type checking and source-health comparison passed with zero new blocking findings. Coverage includes query/profile isolation, late responses, explicit retry without timer retry, pasted searches, local filter reads, Trash routing, pending member catalogs and retained selections on read failure. Historical overlapping suites are not added to this count.

The exact renderer and native Electron main/preload/backend passed **six isolated real-app checks** with synthetic chats and collections. A test-only wrapper exposed the native Node HTTP client to inject bounded delay and HTTP 503 responses; an earlier Electron net.fetch hook did not intercept this transport and supplies no fault evidence. The accepted run observed actual transport interception, no stale prior search hit, manual recovery, zero new item-list reads across four local type-filter changes, zero renderer errors, zero external-app opens and zero inference POSTs. A separate regression measured three redundant type-filter reads before repair and zero afterward. These are request-count controls, not production latency or LLM-token savings measurements.

Nine exact source/test files were installed locally with permissions restored and configuration inputs preserved, and the native package was built from the installed source. The existing owner Desktop remained on its earlier package because enabled native controls could not unambiguously address its Wayland window for normal Quit; it was not signalled or force-killed. Source installation, staged package readiness and active-window adoption remain separate. This release does not certify that a production window has loaded the new renderer.

The cumulative patch contains **484 source/test paths**, comprising **344 outside the Python test tree and 140 Python test paths**, against the same pinned upstream base. Public inventory, Git history and release archives are checked independently before/after publication. No private UI evidence or operational paths are included in the public artifact.


## Portable prompt-cache preference (v0.6.5)

A companion review found a local configuration-only opt-in to an already existing native `prompt_caching.cache_ttl: auto` feature. The public addition is a minimal synthetic merge fragment and an English per-home/profile recipe. Full live configs, chat transcripts and private measurements were not copied. No new Hermes runtime patch is claimed by this release; the cumulative source/test patch remains 484 paths.

Offline native acceptance exercised three isolated home cases with eleven source controls each. The native per-key setter preserved unrelated settings; a root edit left an unselected profile at its existing default, and explicit opt-ins reached the native initialization helper. Existing destination clamps remained effective. Network/model access and arbitrary subprocesses were denied. Preliminary harness controls refused additional local Git metadata during import, and a fixture then mutated a returned read-only config mapping. Those harness failures are retained privately and are not counted as product failures; the accepted controls permit only local read-only metadata and compare config values without mutating them. No dependency was installed or model called.

The CLI parser/profile-selection path was already covered by the earlier setup acceptance; these new controls exercise the real setter and initializer directly, not a full packaged CLI launch. Existing live opt-in values were inspected read-only. Previously initialized production agents, provider TTL support, cross-bot cache reuse and token savings remain unmeasured. Existing Desktop renderer activation from v0.6.4 is still pending; no restart is implied by exporting a setting.


## Versioned shared-guidance prefix (v0.6.6)

Four new controls failed against the preceding builder: worker guidance, skill-dependent help and surface hints split the common prefix, and request diagnostics did not recognize v4. The fix uses v4 for newly permitted prompt builds while retaining v1/v2/v3 restoration. Applicable role, skill, execution and surface instructions remain in the full prompt; permissions, frozen tools, routes, quotas and TTL preferences remain unchanged.

The final canonical offline run covered **10 files / 142 passed / 0 failed**, zero file retries, including native fake-provider tool-loop prefix contracts, restore, model-switch and atomic compaction controls. Existing tests that asserted role/surface hints lived specifically in the old static tier now assert their continued presence in the full new-layout prompt; legacy byte/key controls remain separate. Scoped source-health review reported zero new findings. The installed-source smoke assembled two native v4 transport requests without sending them, retained own-role content and tool schemas, and matched six original v1/v2/v3 cache keys. All six synthetic old full-prompt/static hash controls also matched.

The synthetic shared leading text grew from 1,895 to 2,746 characters without changing either full prompt's length. This is not a provider cache-hit percentage or a production token/latency reduction. A bounded read-only historical-record inspection supplied no v4 adoption/savings proof and its private data was not exported. No new model/provider request was used to measure adoption.

Five exact source/test files were installed locally under native update custody before public export, with target-only rollback files and restored mode/ownership. Configuration/instruction hashes and running process identities were preserved. Fresh imports can build v4; already cached prompts remain as they were. Existing pending Desktop renderer adoption is independent and was not forced. The cumulative patch now has **485 source/test paths: 344 outside the Python test tree and 141 Python tests**, on the same pinned upstream base.


## Bounded native title recall (v0.6.7)

A native fixture reproduced full-transcript hydration before a small title-match response and before rejecting excluded history. The repair uses the existing message-bookend API, preserves the anchored view and continuation counts, and filters time/exclusion metadata before payload reads. Failure in a present bounded API reports unavailable history without retrying the full transcript.

The final native run passed **4 files / 76 tests / zero failures**, with zero file retries. Native live-import acceptance used five alternating before/after runs against one synthetic 256-message SQLite fixture: median 6.74→2.00 ms, 4.52→0.37 MiB peak Python traced allocations and 265→17 hydrated rows, with byte-equivalent returned responses. Both metadata-filter controls loaded zero message rows. The measurements are synthetic query/allocation results, not total-process RAM, billing, cache-hit or model-latency savings. A separate read-only existing-conversation check also preserved the result; no private title, transcript, ID, response hash or workload measurement was exported.

The exact runtime and regression file were installed locally under native update custody before export, preserving target permissions/ownership and target-only rollback evidence. Scope health reported zero new findings. Relocated maintenance artifacts retained their original-path aliases and source hashes; the native title-recall regression file passed its eight tests again after relocation. No provider request, quota change, paid fallback or embedding-service action was used.

The cumulative patch now has **486 source/test paths: 344 outside the Python test tree and 142 Python tests**, on the same pinned upstream base. Public checkout/apply acceptance, companion tests, complete Git history, archives and anonymous release readbacks are verified separately; overlapping runs are not added together. A fresh authenticated runtime status check found idle mounted chats, while the running Desktop package still differed from the prepared UI package. This release does not claim that the pending renderer was activated.

## Portable review of external memory and storage

The optional memory guide was checked against ai-memory v3.2.5's published configuration source. Its TOML example is parsed offline and names reviewed top-level, authentication and maintenance fields. This is not an end-to-end Hermes adapter or service deployment test. Native memory/search remain available without the optional service. The review does not enable providers, hooks, history backfill, MCP or protected embedding services, and no existing private configuration or memory store is copied into the release. A longer matched-work comparison is still required before claiming a recall/usage benefit or expanding a pilot.

The storage guide describes explicit inactive-artifact relocation and post-acceptance disposal boundaries. It publishes neither machine paths nor local migration inventories, firmware data, database snapshots, private logs or rollback contents.


## Context-free search metadata (v0.6.8)

The native SQLite authorizer reproduced prompt/tool hydration while search only
needed session identity. Fixing the search helper alone left title discovery
failing, exposing a second full-context reader in title-to-ID resolution. Both
call paths now use narrow native queries. Existing full-session/title APIs remain
unchanged; canonical Bot Chat priority, numbered continuation ordering, wildcard
escaping, freshness and legacy adapters are preserved. A failed present metadata
reader does not retry the heavyweight path.

The final native run passed **9 files / 395 tests / zero failures**, with zero
file retries. Six new controls exercise normal/read-only public discovery under
SQLite column denial, exact small/fresh/missing metadata, legacy compatibility,
failure without heavy retry and canonical/numbered titles. Scoped health reported
zero new findings. The newly exported title module's original bytes matched the
pinned upstream blob available locally; no history fetch was needed.

Five alternating installed-module runs against one synthetic read-only fixture
preserved the exact response. Median query time was 4.955→1.683 ms and peak Python
traced allocations 2,016,703→79,003 bytes. Two full-session reads plus one full
title read became zero, with context materialization 5,799,987→0 characters. These
measure local synthetic query/allocation work, not RSS, billed tokens, cache hits,
model input context or production latency. A separate real saved-conversation
read-only comparison retained the result; no private evidence or workload numbers
are published. No manual model request was made.

Four exact source/test files were installed under native update custody before
export, with target-only rollback and restored permissions/ownership. The
cumulative patch contains **488 source/test paths: 345 outside the Python test
tree and 143 Python tests**, against the same pinned upstream base. Companion
acceptance, base/apply/installed manifests, public history and release archives
are checked separately; overlapping test runs are not added together.


Local adoption was then checked at an idle boundary with no worker turn active.
Gateway used its existing native idle-only update control; Desktop exited through
its normal native Quit menu and reopened once with the already tested package.
Fresh source/process identity, authenticated read-only readiness and the same
saved-session/model binding were observed. Configuration/instruction hashes
remained intact, and no model or manual session-resume call was used. This is
source/readiness/continuity acceptance; it does not claim every production screen
was visually exercised or every bot has already used the optimized query path.


## Notification destination metadata (v0.6.9)

Native destination resolution still read full prompt/tool context merely to
check that the current/candidate session existed. A SQLite-authorizer regression
failed in both normal and named-profile read-only paths. The resolver now reuses
the native small metadata API; missing extensions keep legacy compatibility,
while failure in a present reader holds work without a heavy retry.

The final native run passed **10 files / 75 tests / zero failures**, zero file
retries. Four new controls join the existing compression delivery, stale-parent,
branch/delegate, foreign-profile, claimed-receipt/no-replay, owner-hold, stopped-turn,
retry and terminal-release contracts. These offline fixtures do not establish a
live intended-session ACK. Scoped source health reported zero new findings.

Installed-source paired acceptance used the existing production interpreter and
native dependency activation, with launch preparation frozen only in the private
measurement process to prevent PM rebuild/relaunch. Earlier guarded preparation
and unactivated-interpreter failures are retained privately and are not product
failures or accepted benchmark runs. The final five alternating synthetic pairs
included native read-only store open/read/close: median 3.951→1.713 ms, peak Python
allocations 1,900,776→21,140 bytes, full session reads 3→0, hydrated context
characters 3,735,552→0, with the same destination set. A separate real saved-chat
owning-store comparison also retained the set, with no notification, receipt,
model or inference action. No private evidence/workload values are published.
These measurements are not RSS, token, cache-hit or production latency savings.

The exact runtime and regression files were installed locally before export,
with target-only rollback and restored mode/ownership; configuration/instruction
hashes and active process identities were preserved. The cumulative patch now
contains **489 source/test paths: 345 outside the Python test tree and 144 Python
test paths**. Companion, base/apply/installed, complete history, archive and
anonymous readback checks are performed separately. Native source adoption and
visual/behavior acceptance remain distinct.


At the next verified idle boundary Desktop exited through one normal native tray
Quit event and reopened once with the same tested package. Fresh source/process
identity, native backend/main-renderer readiness, the original durable session and
model binding, and 99 protected configuration/instruction hashes were verified.
Gateway retained its existing process identity. A transient read-only observation
lost the backend listener during normal shutdown; its exact original app/backend
were then observed terminal before launching. No repeated Quit, signal, model or
manual resume call was used. This is source/readiness/continuity acceptance, not a
full production visual journey or a manufactured notification-delivery receipt.


## MRU selection and export preflight IDs (v0.6.10)

Native latest-session lookup and the two unfiltered export preflight paths read
full session context merely to obtain IDs. The regular `search_sessions` API now
also supports an explicit ID/recency-only projection; source/workspace predicates,
ordering and pagination remain shared. Actual resume, backup, import and full
session readers keep their original payloads. Filtered export already uses a
narrow candidate query and remains intact. Console also resolves its configured
per-session bound before enumeration, so a disabled guard issues no ID scan.

The final native run passed **10 files / 349 tests / zero failures**, zero file
retries. Eight new cases include actual SQLite prompt/tool/model-config read
denial, native ID ordering/page equivalence and MRU/oneshot/workspace fallback,
actual parsed CLI and Console budget refusals without touching existing output,
full successful backup equality and disabled-guard behavior. Existing batching,
compacted backup/import round-trip, retention/export selection and SessionDB
controls passed. Preliminary fixture signature/parser-wiring mistakes are retained
privately, not counted as product bugs. Scoped health reported zero new findings.

Five alternating installed-module pairs against a 32-session synthetic SQLite
fixture preserved the exact ID order and native count-guard result. Median local
query time was 51.292→0.979 ms; peak Python allocations 42,107,726→17,001 bytes;
session rows remained 32 while hydrated context characters fell 41,943,520→0.
The measured path is ID enumeration plus preflight, not the full backup payload,
RSS, model input, tokens or cache-hit rate. A separate existing-history read-only
comparison preserved the order/guard without writing an export/restore or calling
a model. Private workload data and identifiers are excluded.

Five exact source/test files were installed locally under native update custody
before export, preserving target mode/ownership, target-only rollback and
configuration/process guards. The two newly exported runtime modules' original
bytes matched the locally available pinned upstream blobs. The cumulative patch
contains **492 source/test paths: 347 outside the Python test tree and 145 Python
test paths**. Companion, pinned base/apply/installed, Git history, archive and
anonymous-public checks remain separate. No quota/provider/paid-fallback,
embedding-service, schema or model-context change was made.


Fresh CLI imports use the installed source directly. At an idle boundary Desktop
also exited through one normal native Quit event and reopened once with the same
tested UI package. Fresh process/source identity, authenticated native backend
and main-renderer readiness, the original saved session/model and 99 protected
configuration/instruction hashes were verified. Gateway retained its process
identity; no database snapshot, forced stop, model or manual resume call was used.
This source/readiness acceptance is separate from a full production visual journey.


## Chunked JSONL export and Terra reasoning (v0.6.11)

The native export suite passed **57 tests in 11 files**, with zero failures and
file retries. A subsequent hard-link regression exposed an inode-semantics
change; after repair, a focused four-file run passed **21 tests**, zero failures.
The runs overlap and must not be summed. Tests cover native CLI/Console export,
Unicode bytes, empty output, prompt-only/stdout behavior, staged serializer and
fsync failures, symlinks, hard links, read-only targets, missing parents, special
files and deleted-profile guards. Existing backup/import, retention and formats
remain covered. Scoped health reported zero new blocking findings or advisories.

Three full synthetic SQLite-to-JSONL exports per version produced identical bytes.
Median traced Python peak decreased from 107,491,242 to 24,736,700 bytes for this
fixture. A fresh installed-source run also matched the same synthetic output,
and a bounded read-only existing-history comparison matched full and prompt-only
serialization without persisting private history. These measurements include
payload load and serialization, but are not whole-process RSS, production usage,
model latency, cache-hit, or billing evidence.

An independent native transport regression caught Terra's `max` being clamped to
`xhigh`. Its compatibility change and controls passed **79 tests in seven files**,
zero failures. Fresh installed request construction preserves the configured
effort; this offline check is not an inference or quota-consumption benchmark.
The two source changes were installed locally under native custody with scoped
rollback. Runtime activation for already-running processes is separate from fresh
CLI import acceptance. The cumulative patch contains **496 paths: 349 outside
the Python test tree and 147 Python test paths**.

## Per-task reasoning effort (v0.6.12)

Five offline native test files passed **118 tests**, with one existing skip and
no failures. A later focused run passed **3 tests**; the runs overlap and must
not be summed. The focused tests use an isolated Kanban database and actual
tool registration and worker argument construction: they cover Sol and Terra,
normalization of `HIGH`, rejection before card creation for invalid effort, and
inheritance when omitted. They do not dispatch a production task or call a model.

The change was installed locally with a scoped rollback before publication. A
fresh process can load the installed code; a previously mounted agent may retain
cached tool definitions until its normal lifecycle refresh. Offline validation
does not prove a live Captain has selected a model or that a bot completed a task.

## Verified completion at budget checkpoints (v0.6.13)

An offline native regression suite passed 113 tests across five files; a later 21-test run of one of those files overlaps and is not an additional total. Tests cover iteration and wall-clock checkpoints and rejected or unverified ownership. One representative real worker completed a synthetic task at the iteration checkpoint with no subsequent tool or model call. This is not a measurement of every profile or a long-term usage reduction.

## Usage reporting during log rotation (v0.6.14)

A deterministic regression reproduced a file disappearing between enumeration and sorting. The native offline suite passed 31 tests across four related files after the fix. A read-only before-and-after check over the same real 24-hour window returned the same sample counts; no log rotated during that check, and the existing file budget left some files unsampled. This does not establish complete usage or a reduction in model calls.

## Older session restoration (v0.6.15)

The related offline suite passed 82 tests across three files, including owner changes, list readiness, lookup failure and stale navigation. A packaged Electron build was closed and relaunched against an isolated backend seeded with 55 synthetic sessions; the oldest session, omitted from the first page of 50, was restored. The mock provider received no prompts. This is not evidence that a particular existing session was restored or a live workload benefited. The source and package were installed locally before publication with a scoped rollback; actual UI behavior remains a separate check.

## Explicit usage attribution boards (v0.6.16)

Four related files passed 26 offline cases, including a synthetic external board, aliases, missing and non-regular paths, a symlink loop, and the 64-board limit. A separate Python 3.12 check covered symlink-loop resolution. The exact installed files passed the same suite in a read-only, network-isolated environment; these overlapping runs are not summed. In one identical existing seven-day sample, an explicitly selected isolated test board increased exact matched attempts from 7 to 91. One other board was unavailable in the sandbox, 52 log tails were cut, and compressed logs were not read. This is provenance coverage for a selected test board, not a model-usage saving or full production coverage. No model call was made for the measurement.

## Captain routing guidance (v0.6.17)

The Captain role template exposes the optional planner/executor split in its own loaded identity rather than relying solely on an external reference. This is static template guidance; offline template and package checks do not demonstrate live Captain compliance, real-bot orchestration or usage savings. Profile identities, model selection and dispatch remain operator-controlled.

## Per-task CLI reasoning (v0.6.18)

Five related test files passed 22 offline cases against the candidate and the same 22 cases against installed source in a network-isolated environment; these are overlapping runs. The new cases cover normalized effort, `none`, invalid input without card creation, omitted effort and propagation from CLI to task and worker arguments. No live dispatch, model call or quota measurement was performed.

## Cross-profile cache cohorts (v0.6.19)

Five related test files passed 32 offline cases on the candidate and the same 32 cases on installed source in a network-isolated environment; these overlapping runs are not summed. Cases cover distinct profiles, duplicate and conflicting records, missing fields, invalid values, unknown accounts, failed calls, CLI opt-in and output privacy. The feature reads existing logs only and performs no provider request. Cohort equality is observational evidence, not a claim of shared cache origin or savings.

## Verified goal waits (v0.6.20)

Eleven related test files passed 298 cases with 4 Windows-only skips on both the offline candidate and installed source in isolated Linux runs; the runs overlap and are not summed. Cases include a real isolated sleeper, saved state, PID reuse, registry error or missing handle, watch triggers, legacy targets and CLI/Desktop pause notices without dispatch. No provider request was made. An idle preflight is required for source installation; existing processes need a safe reload before they use new code. These tests do not establish live task behavior or measured token savings.

## Snapshot integrity and traversal (v0.6.21)

Nine related test files passed 141 offline cases on the candidate and on installed source in isolated Linux runs; these overlapping runs are not summed. Cases cover failed file and database copies, missing or inaccessible state, oversized files, unreadable directories, excluded subtrees, preserving the older snapshot, and incomplete restoration. Read-only enumeration of one existing board root returned the same included file names while skipping excluded subtrees; its timing is a single local sample, not a general backup-speed or disk-savings claim. No production backup was restored, no existing recovery snapshot was removed, and no provider request was made.

## Safe autonomous reassignment (v0.6.22)

Thirteen related test files passed 235 offline cases with one skip on the candidate and on installed source in isolated Linux runs; the overlapping runs are not summed. Regressions cover a live isolated sleeper and manual claims, stale bot status, concurrent completion, claims and reassignment, new and prior explicit holds, released historical holds, and sticky failures. No live card was reassigned and no provider request was made. These tests do not prove production behavior, current bot availability, or usage savings.

## Passive intermediate task status (v0.6.23)

Seventeen related files passed 183 offline cases against installed source in an isolated Linux run. An earlier candidate suite passed 182 cases, followed by 18 focused cases including a real dashboard transition; these runs overlap and are not summed. Cases cover passive status visibility, actual completion and review delivery, parent invalidation, changed-lane and unknown metadata, busy sessions, renderer failure, and pre-existing pending or ambiguous receipts. No live task or provider call was used for verification. One read-only seven-day sample found no matching historical status receipts in the boards inspected, so runtime usage savings remain unmeasured.

## Concurrent task idempotency (v0.6.24)

The previous implementation produced two tasks in isolated simultaneous two-connection and two-process reproductions. After the fix, 16 related files passed 270 tests with one Windows-only skip against the installed source on Linux. Coverage includes existing-key read-only fast paths, distinct keys, archived reuse, nested graph transactions and rollback. No production task or model call was created for this verification; production usage savings were not measured.

## Dispatch pause and shared capacity (v0.6.25)

Twenty-four related test files passed 279 offline cases with one Windows-only skip against installed source on Linux. Cases cover direct and dashboard pause, an existing worker, a pause during a tick, root pause, resume, dashboard and daemon caps, independent profiles, two simultaneous processes on separate boards, unavailable or contended locks, unknown board capacity, and read-only WAL counts. In a small synthetic tmpfs sample, five runs of 16 fake admissions across four boards took a median 134.401 ms before and 143.475 ms after; this does not measure production latency. Actual behavior under a resumed live dispatcher and usage impact remain unverified.

## Emergency-stop inspection failures (v0.6.26)

Thirteen related test files passed 148 offline cases against installed source on Linux; macOS-specific tests were skipped. Injected filesystem errors exercised profile and fleet-root paths, cron, gateway and Kanban admission. The tests do not establish that an I/O failure occurred in production or measure production usage.

## Honest pause and resume status (v0.6.27)

Twenty-one related files passed 264 offline tests against installed Linux source; macOS-specific tests were skipped. Tests cover CLI and gateway responses, partial deletion, unreadable state, unsaved reasons, localization catalog parity, and a real mode-000 directory in an isolated temporary home. These cases do not prove a production I/O failure occurred or measure usage savings.

## Global pause across profiles (v0.6.28)

Twenty-two related files passed 282 offline tests against installed Linux source; macOS-specific tests were skipped. Tests cover CLI and gateway controls, separate profiles and roots, cron and Kanban guards, existing work, failed root resolution, concurrent creation, reason preservation and localization parity. A separate isolated multi-process smoke used installed code and a real temporary process; no production model request was created.

## Linked emergency-stop safety (v0.6.29)

Eighteen related files passed 206 offline tests against installed Linux source. Tests cover dangling and valid symbolic links, hard links, link replacement between inspection and open, a no-NOFOLLOW capability fallback, short writes, ordinary sentinel mode preservation, cron and Kanban guards, and I/O failures. A separate isolated multi-process smoke used installed code and a real temporary process; no production model request was created and no production incident is asserted.

## Scoped and fresh reassignment status (v0.6.30)

Twenty-six related files passed 431 offline tests against installed Linux source; four Windows-specific cases were skipped. Regressions cover fleet isolation, context-local custom roles, stale and malformed snapshots, timestamp boundaries, unreadable or disappearing files, and blocked quota-failure behavior. A separate native registry/SQLite smoke used only temporary boards; no production card was reassigned or model request made.

## Scoped session links (v0.6.31)

Ten related files passed 239 offline tests against the installed Linux source; three Windows-specific cases were skipped. Temporary SQLite fleets covered direct links, profile mismatch, identical IDs, tombstones and live-context exclusion. A separate installed-source smoke used synthetic data only; it emitted an isolated update-bootstrap warning and did not validate a production session or measure model usage.

## Session link identity (v0.6.32)

Ten related files passed 245 offline tests against installed Linux source; three Windows-specific cases were skipped. Temporary SQLite fleets covered profile-switch round trips with colliding IDs, default and named profiles, discovery, browsing, aliases and reserved names. A separate installed-source smoke used synthetic data only; it emitted an isolated update-bootstrap warning and did not validate a production session or measure model usage.

## Session-scoped recovery (v0.6.33)

Twenty related files passed 318 offline tests against installed Linux source; three Windows-specific cases were skipped. Synthetic SQLite sessions covered middle-of-history tool output, colliding profiles, unrelated hits, visibility, bounded excerpts, Boolean queries, Thai, concurrency and interruption cleanup. A separate installed-source smoke used synthetic data and emitted an isolated update-bootstrap warning; production recall and real usage savings were not verified.

## Recoverable tool results after compaction (v0.6.34)

Thirty related test files passed 457 offline tests against installed Linux source. Isolated SQLite tests covered in-place and rotation publication, row-ID and unique call-ID resolution, ambiguous and missing originals, prior rewinds, concurrent appends, rollback, scoped search and removal of private markers. A native compressor with a deterministic local summary also recovered a demoted result. These fixtures do not establish production occurrence or quantify real usage savings.

## Bounded session recall (v0.6.35)

Twenty-five related test files passed 283 offline tests against installed Linux source. Isolated database fixtures cover rewinds and hidden rows, concurrent changes to title and search results, profile collisions, Unicode and structured pages, legacy readers, and recovery of compacted tool output. One synthetic scroll of eleven large messages returned 178,005 bytes before and 18,611 bytes after; this is not a measurement of production usage or model tokens. No model calls were made.

## Structured session recall (v0.6.36)

Twenty-nine related test files passed 361 offline tests on the installed Linux source. Isolated SQLite fixtures cover multilingual text, image payload exclusion, JSON-escaped tool arguments, byte offsets, unpaired surrogates, read-only and concurrent queries, deadlines, rewinds, and existing prompt-cache and profile boundaries. In three synthetic runs using 12 MB plain bodies, median scoped-search time changed from 19.36 to 28.27 ms; for a tool-argument hit with an unrelated 12 MB body it changed from 60.35 to 42.43 ms and peak RSS increase from 58,396 to 23,000 KiB. A separate 10 MB multimodal fixture was found after the change but not before. These are synthetic measurements, not live model usage or token savings. No model calls were made.

## Search log privacy (v0.6.37)

Eight related test files passed 138 offline tests on the installed Linux source. Synthetic successful, empty, and failed searches confirmed that slow-search logs retain diagnostic metadata without the search text. The gateway was reloaded using its native idle-only control. No model calls were made.

## Search expression fallbacks (v0.6.38)

A Linux offline regression suite checked exact phrases, mixed CJK text, boolean operators, punctuation, and Latin prefixes with native CJK and trigram indexes. Fifteen targeted cases passed on the installed source, with ten existing CJK-index cases. A separate ten-file search suite passed 186 tests on the candidate. The gateway reloaded through its idle-only control. No model calls were made. These tests do not establish production latency or usage savings.

## Bounded full-text search snippets (v0.6.39)

A Linux offline regression suite exercised long CJK and Latin tokens, long highlights, literal marker-like text, multiple hits, and the session search tool. Seven targeted cases and 15 earlier phrase-fallback cases passed against installed source. A separate 15-file search suite passed 220 tests on the candidate; these suites overlap. In one synthetic three-hit run with roughly 8 MiB per message, the tool response shrank from 25,170,683 bytes to 5,293 bytes and sampled peak RSS increase fell from 114,344 KiB to 41,156 KiB. One-hit peak RSS remained high because SQLite may materialize a large field. These figures are not production usage or latency measurements. The gateway reloaded through idle-only control; no model calls were made.

## Read-only cross-profile CJK search (v0.6.40)

Offline synthetic tests covered cross-profile search, tokenizer and index absence, stale indexes, a caller-owned transaction, a concurrent writer, and percent-sign fallbacks. Sixteen focused tests, 199 wider search tests, nine state tests and 80 read/write safety tests passed; seven platform-specific cases were skipped. These suites overlap. After installation, a three-file suite passed 91 tests on installed source. In a synthetic 40-run profile-open test, the query returned two matching rows instead of one, with median open times of 1.494 ms versus 1.421 ms before the change. This is not a production usage or speed measurement. The gateway reloaded through idle-only control; no model calls were made.

## Structured global recall (v0.6.41)

A 22-file offline suite passed 456 tests on both the candidate and installed source. Tests
cover nested escapes, word boundaries, Boolean/prefix queries, image-only and hidden-row
rejection, read-only CJK snapshots, bounded excerpts, timeout reporting, caller
transactions and progress handlers. Two timeout-injection tests were updated to target an
execution path that remains active after lazy evaluation; the retained assertions still
require a timeout. A synthetic 460,000-row mixed fixture with 30% large argument fields
passed all 15 trials: three trials each for two Latin terms, CJK, no-hit and frequent-word
queries. The frequent-word case returned all 20 expected results in 1.17–1.18 seconds,
compared with a three-second timeout in the earlier candidate. The slower Latin case took
2.78–2.82 seconds, so its deadline margin remains small. A private, bounded real-history
subset was searched in transient RAM storage with source identity and bounded-page checks;
it was not a search across a live production database. These results do not establish
natural-workload latency, usage savings, or compatibility with every SQLite build. The
gateway adopted the installed files through native idle-only reload. No model calls were
made.

## Bounded history byte readers (v0.6.42)

On the verified Python 3.14.7 / SQLite 3.53.1 runtime, 20,000 closed native Blob reads retained about 1.77 MB while their connection object remained alive. Closing and releasing that object returned the bookkeeping. This behavior agrees with the [CPython connection implementation](https://github.com/python/cpython/blob/v3.14.0/Modules/_sqlite/connection.c#L585-L590). The Hermes raw-search regression failed before the repair and passed afterward with a live-connection allocation budget below 256 KiB.

A 24-file offline suite passed 468 tests on both candidate and installed source, including concurrent-writer snapshots, caller transactions/handlers, invalid bytes, two-megabyte fields and bounded page reads. The synthetic 460,000-row fixture passed all 15 trials. Peak process RSS was about 63.8 MiB instead of 134.3 MiB in the preceding fixture run; this is not a production memory measurement. CJK searches took 1.54–1.57 seconds versus about 1.03 seconds before this repair, a deliberate tradeoff for bounded retained memory. Frequent-word queries stayed near 1.17 seconds; the slower Latin case stayed near 2.78–2.79 seconds and has little margin under the unchanged three-second deadline.

The gateway adopted installed source through native idle-only control. A permitted real-history subset was checked privately in transient RAM storage; this did not search an entire live profile or establish natural-workload usage savings. No extra model calls, provider probes or dependency changes were made.

## Deployment acceptance checklist (v0.6.43)

This documentation-only release separates exact installation, process adoption, interactive behavior and measured workload outcomes in an operator checklist. The v0.6.36 feature entry now identifies its global-search limitation as historical and links to the v0.6.41 correction. It does not change the cumulative native patch, model routing, quotas, provider settings or runtime defaults.

The exact release inventory and local documentation links are verified. Existing native regression and workload evidence above remain historical; no native suite or model task is repeated for unchanged source. Offline CI and public file/history/archive privacy checks validate the new artifact separately. The checklist does not certify that any particular deployment has completed every row.

## Answer cards in narrow chat tiles (v0.6.44)

An actual installed-package journey reproduced clipped card images beside an open HTML artifact. The native Playwright regression failed before repair and passed afterward. Seven related UI files passed 52 tests; two native Electron E2E tests passed, including older-session restoration. The runs overlap in behavior and are not summed. Renderer and E2E TypeScript checks passed. A preexisting restoration-test bridge type was narrowed so it no longer relies on an undeclared Window member.

After local source and package installation, six isolated native interaction checks passed for tables, supplied cards/images/links, Mermaid open/close, an interactive HTML artifact, malformed-source recovery and narrow chat layout. The artifact's local button updated and parent-document access was denied by its existing opaque sandbox. The 560-pixel test viewport lowers the minimum size only in the fixture; it is not a new production mobile-support claim. Model requests and external-application opens were zero. Offline font loading was denied; deliberately invalid card data exercised the existing error boundary and source-highlighting fallback, with their expected console messages. No uncaught renderer exception occurred.

Runtime lint retained the same 13 existing errors and three warnings; the new E2E file is clean. This is not a whole-repository lint claim. A two-GiB diagnostic TypeScript heap was insufficient; the renderer check passed with a four-GiB heap in the maintenance process. Service memory limits and dependency selection were unchanged. Owner Desktop remained closed, Gateway was not restarted and no model/provider probe was used. Production-window interaction and workload savings remain separate acceptance.

## Mac installation/update and backend startup (v0.6.45)

A native Apple Silicon experiment applied public v0.6.43 and v0.6.44 archives to separate exact-base checkouts. Base verification, normal Git apply and installed hashes passed for 569 and 570 paths respectively. Each version launched the existing Python 3.13 CLI. Across separate processes selecting the newer source with the same isolated home, one synthetic SessionDB row and its native search result remained available. The CLI version string still identifies upstream Hermes, not the Legion kit. No production source, application, credential store or real conversation was copied or replaced.

The public setup/doctor recipe also passed on macOS. Doctor reported `offline_ready: true` and `runtime_ready: unknown`; no native credentials or live profile configuration were generated. The companion suite initially failed on both system Python 3.9 and native Python 3.13 because the test fixture used the system's `/var` alias. Only the fixture root was canonicalized; the runtime exporter and explicit linked-destination refusal stayed unchanged. All 75 companion cases then passed on each interpreter and on Linux. These are overlapping cases, not 225 distinct tests.

Using admitted copies of existing native dependencies and packager suppliers, the patched native renderer/main/preload built and an arm64 package was produced with external networking denied. No dependencies or models were downloaded. An obsolete signing CLI flag was rejected before packaging; removing that harness flag allowed packaging. Certificate discovery was disabled, so the initial package did not pass strict signature verification. A separate local-only package copy was ad-hoc sealed with existing native entitlement files using the installed signing library, with no Apple credentials, timestamp, automatic entitlement rewrite or embedded provisioning profile. Deep strict signature verification passed. This is not notarization or a distributable Developer ID build. The host lacked the optional newer icon compiler and used the existing `.icns` fallback.

Actual Electron startup then exposed `NameError: name 'Path' is not defined` while importing the onboarding module on Python 3.13. A fresh-module annotation regression also failed before the repair on Linux Python 3.14, where deferred annotation evaluation had hidden the immediate import failure. The runtime repair adds the missing `pathlib.Path` import. The regression and two related native RPC/onboarding files passed 12 cases on Linux; the same import/annotation regression and a full native server import passed on the Mac. The exact two source/test files were installed locally with a scoped backup, original permissions and native update-lock custody while the owner Desktop was closed and no workers were active. Gateway identity, configuration and the Linux stop policy were preserved; no restart was required for this Python source repair.

After repair, two native Mac Electron tests passed: narrow answer-card layout beside an open HTML artifact, and cold restoration of a synthetic older session omitted from the first history page in the newly packaged app. The first uses source Electron; the second uses the local packaged executable and the explicitly selected patched backend. Mock-provider prompt counts were zero. A prior sandbox attempt denied local singleton IPC and was corrected to permit loopback and Unix sockets while keeping external networking blocked; no owner lock was deleted or process terminated. Original failures remain private evidence. The 12 native and two UI results cover different checks but are not a full upstream suite, full Mac feature audit, actual-provider acceptance or production-app adoption. No new usage, cache-saving, response-time or RSS improvement is claimed.

The cumulative patch now contains 572 paths. Existing patch hunks remain byte-identical; only the onboarding module and its import regression are added. Seven broken relative links in the installation page were repaired. Current public files, reachable Git history, release contents and notes are scanned for credentials and known private identifiers before publication. Machine identities, private paths, test homes, logs, screenshots, source clones and the Mac application package are excluded from the public payload.

## Scoped model catalogs (v0.6.46)

Six failing scope/concurrency/retention regressions and three controls first reproduced
incorrect catalog reuse and duplicate reads. A separate pricing reproduction showed
that capability arrays/objects could discard a catalog, and a boolean could become a
price. The final seven-file native suite passed 213 cases with zero retries, including
17 focused scope, disk-reuse, refresh, concurrency, retention and pricing cases.
Scoped Ruff found zero findings. The native health ratchet had zero unwaived blocking
findings; two documented broad exception catches preserve the inherited optional
provider-probe fallback rather than changing its failure behavior during this move.

A synthetic 1,000-model catalog fixture with eight simultaneous callers ran three
trials per version. Requests were [8, 8, 8] before and [1, 1, 1] after; all returned
the same catalog digest. Median elapsed time was 0.301 s versus 0.135 s; median peak
traced Python allocation was 3,615,725 versus 611,555 bytes. This equal-result fixture
uses baseline-compatible pricing data. The capability-shape failure was retained
separately and verified by correctness tests. These are synthetic transport results,
not service RSS, production latency, token usage or billing savings.

The exact three files were installed on Linux under native update custody with scoped
rollback bytes and original permissions. Native idle-only Gateway restart admission
was accepted; the replacement process postdated installation with zero active agents
and the existing emergency stop retained. No model call was made. Desktop remained
closed; no renderer rebuild was needed for this Python-only change.

Two native Mac trial UI cases passed in isolated homes with external networking denied:
narrow answer cards and cold restoration of an older saved session. Final runtime
ASTs matched those tested bytes after comment-only cleanup. The trial source hashes
were read back; the original Mac application and configuration were not changed.
These UI cases establish backend startup and those interactions, not full production
bot behavior. Natural-workload cache/usage acceptance remains incomplete because the
current read-only sample is dominated by test or unknown provenance and sparse task
bindings; no model requests were added to manufacture a favorable measurement.

## Credential-bound context windows (v0.6.47)

Native red cases demonstrated credential A's confirmed 131,072-token window being
reused by credential B whose catalog reports 65,536; unqualified legacy reuse;
credential/home-blind local memos; malformed provider-specific prices; callable
bookkeeping; unbounded scoped storage; and a lost parallel window write.
The final 14-file offline suite passed 302 cases with zero retries. The installed
Linux source separately passed the 19 focused cases (a subset, not 321 distinct
cases). Scoped Ruff found zero findings; the native health ratchet had zero
unwaived blockers, with two documented inherited best-effort exception policies.

Old fixture assumptions were updated explicitly: account-specific live windows now
use their scoped key while preserving unrelated and anonymous entries; reconciliation
spies include the credential argument; the negative-TTL test advances its clock rather
than depending on a private memo-key shape. Test isolation was corrected by placing the
checkout outside managed state and discarding owned stale compiled test caches after
that move. An early callable test mistakenly called its sentinel in the test itself;
it was corrected, then verified red on the exact baseline and green on the repair.
No test guard, runtime dependency or provider policy was weakened.

An isolated Mac native-Python smoke passed credential-bound overflow persistence,
separate-credential catalog resolution, explicit pin precedence, malformed prices
and non-minting bookkeeping. Two existing native UI journeys passed again with
external networking denied. This is trial-source evidence, not installation of the
custom desktop into the owner's original Mac application. No extra model calls,
provider allowance checks, changed quotas or paid fallback were used.

The exact eight files were installed on Linux under native custody and target-only
rollback, followed by focused acceptance and native idle-only Gateway adoption.
No renderer rebuild was needed; the owner Desktop remained closed. Production
before/after token, latency, quality and whole-service RAM savings are not established
by these tests. Official upstream version migration is a separate acceptance task;
this release preserves its pinned upstream base and does not claim that migration done.

## Stable transport repair (v0.6.48)

The separate seven-path unit was extracted against clean upstream v0.22.5, commit
`bf0203a794a07aac3ff764972ab9087baa4e4f4e`. The original cumulative patch and manifest
remain unchanged. The two new offline files first reproduced ten failures and one
passing origin-isolation control on that public base. After applying only the public
patch, eleven native files passed **88 tests**, zero failures and zero retries in
19.9 seconds. This is one scoped run, not a full upstream suite or an extra 88 tests
on top of overlapping installed-source results. Apply, exact before/after hash
verification, reverse-apply and reapply all passed in the separate checkout.

Native Linux installation had already preserved target ownership and modes under
update-lock custody. The Gateway adopted the files only after native idle admission;
existing profiles, auth stores, quotas, emergency stop and disabled Dashboard stayed
unchanged. A bounded real-provider synthetic developer loop then completed planning,
action, separate review and native terminal handoffs in about 50 seconds. Repeating
creation of the same pinned action returned the same task, and logs showed no further
model call after each terminal tool. The fixture used the same existing account via
native `key_cmd`, without copying OAuth refresh grants or writing bearer credentials
into the fixture. The isolated provider alias is an acceptance boundary, not proof of
production Captain adoption or every role and family. Raw logs, account metadata,
private paths and operational identifiers are not part of this release.

An initial loop exposed the worker wire-mode bug and failed at the planner. A later
loop produced and verified the artifact but hit its private four-turn ceiling before
review handoff. Increasing that fixture-only ceiling to six allowed the final loop;
production quota and bot turn settings were not changed. Failed attempts were retained
privately rather than reported as successful. No new paid fallback was used.

The release verifier now validates the digest and inventory membership of each
additional patch unit. Two new negative cases reproduced its previous omission;
all fifteen focused release-tool cases passed after repair. Separate companion tests,
privacy review, archive verification and GitHub CI are required before publication.
There is no new whole-service RAM, usage, cache-hit, throughput or macOS adoption claim.

## Ambient confirmations and stable upgrade (v0.6.49)

The installed Linux package reproduced a compact-window defect: after Save and
immediate reopen, the success toast covered the dialog's Save button. A loose
in-viewport assertion had passed; an actual center hit test failed because the
toast received the pointer. Ambient confirmations now use the layer below the
modal backdrop, while warnings, errors and actionable notices retain the existing
over-modal layer.

Seventeen notification component/store cases passed, including primary and
secondary recovery callbacks and bounded-stack dismissal. Full Desktop TypeScript
checks passed. The native health ratchet reported no new blockers or measurement
errors for the two paths. A test-only locator option rejected by TypeScript was
corrected; it was not a runtime defect. Existing packager/native dependencies were
consumed with external networking denied; no dependency install was performed.

The candidate and the installed packaged application both passed the real native
settings journey: open Bots, edit role/model/effort, save, reopen and verify retained
values; shrink from 1440×1000 to 1000×760, scroll, verify the full Save rectangle and
its pointer target, and operate Cancel. The fixed installed package returned Save
as the hit target at the same point where the original package returned the toast.
The backend ran in an isolated home using the unmanaged source with the relevant
installed settings/workflow paths matched. Original chats, projects and accounts
were not used. External networking was denied; the only observed resource error
was a blocked optional Google Fonts stylesheet. No model inference was requested.
This is installed-package acceptance in isolation, not the owner's original-window
session adoption, a complete UI audit or Mac deployment proof.

Exact two-source publication and an atomic Desktop image swap used native custody
while the owner application was closed. Gateway identity, profile/auth/config
hashes, modes and ownership were preserved; no Gateway restart occurred. The
rollback image shares 1,170 unchanged files with the active image and keeps the
changed bytes separately, avoiding another complete binary copy.

The nine-path public unit contains the unchanged seven-path v0.6.48 transport
repair plus these two frontend paths. Its native notification cases passed again
on the clean pinned public base using existing matching workspace dependencies.
An initial isolated run lacked the workspace-specific dependency link and failed
before tests; no dependency was installed to correct that fixture. Clean full
apply/reverse/reapply, exact seven-to-nine-path upgrade, and incremental rollback
that retains the transport changes all passed. The inherited 88 transport tests
were not rerun or added to the 17 UI cases as a new combined suite. Earlier full
THINK/ACTION developer acceptance remains limited to its documented scope.

The public release verifier also checks incremental-patch digests and inventory
membership. Two negative upgrade cases first failed; the repaired verifier passes
the scoped cases. No production token/RAM/cache/latency savings, full-fleet
THINK/ACTION adoption or new Mac parity is claimed by this release.

## Native role workflow integration (v0.6.50)

See [stable role workflows](stable-role-workflows.md#verification-boundary) for the clean-base Python/UI scope, one real Captain/developer loop, retained failures and explicit provider/Mac/usage limits. These results do not replace the historical cumulative-kit verification above.

## ARM64 installation and evidence boundaries (v0.6.51)

The [Mac guide](macos-install-update.md#choose-the-patch-base-first) now separates
the cumulative v0.22.2 walkthrough from the alternative v0.22.5 role unit, avoiding
an incompatible full-patch stack or an assumed interpreter upgrade. Patch bytes,
native runtime behavior and dependency locks are unchanged by this documentation
release.

In a separate custom native ARM64 installation, matching PM preparation, Desktop
typecheck/build/packaging, normal CLI source/runtime readback and strict ad-hoc
signature verification passed. The installed application then passed the
role/model/effort, reciprocal-pair, compact-button and navigation journeys using
isolated user data with zero inference requests. See the
[deployment checkpoint](macos-install-update.md#later-arm64-deployment-checkpoint)
for the scope and retained original-session/provider limits. The custom host's
private configuration, account material, logs, screenshots, backups and source
manifest are not published here. This release does not ship a Mac binary or
claim a new production usage, cache, latency or RAM saving.

## Cache miss evidence (v0.6.52)

The optional [four-path cache unit](cache-miss-evidence.md) corrects an unsupported causal inference: a 300-second idle gap was labelled confirmed expiry for all routes. It now records an unexplained provider-reported miss; known Hermes changes and historical metric vocabulary remain intact. Requests, prompt/cache policy, effort, account routes and telemetry consent are unchanged.

The two route regressions and the relay-storage integration failed before repair. Four native files passed 172 tests with zero retries, and the same scoped suite passed on the pinned clean public base. These overlapping checks are not summed. Native production-interpreter readback passed on Linux and ARM64 macOS, with only the idle Linux Gateway reloaded. No original Mac session/Gateway was started, no provider was called, and no usage or cache-hit improvement is claimed. Public apply/reverse/reapply and inventory, history, archive and privacy verification are separate release checks. Older cumulative/runtime/role patch bytes are unchanged.

## Historical privacy maintenance (v0.6.53)

Private operational references were removed from two legacy comments throughout reachable history. A private compact Git bundle preserves reversible recovery outside the publication. All original branches/tags and neutral authorship/tagger metadata were retained; corrected objects and release digests differ. Native Git application reconstructed and checked historical source hashes, and Python ASTs matched before/after the comment-only changes. Per-tree release inventories and tagged archive contents were verified independently before publication. See [privacy maintenance](privacy-maintenance.md) for consumer migration and the limits of repository/cache erasure claims. No Hermes runtime, model request, account, quota or existing worker changed for this maintenance. Native behavior test results remain historical and are not relabelled newly rerun.


## Missing-skill worker results (v0.8.20)

Known all-missing Kanban preloads now return a structured failed result instead
of crashing the managed worker into an unknown admission. See
[missing-skill worker results](missing-skill-worker-results.md) for the failed
regression, 90 related passing cases, native checks on both hosts and a fresh
zero-request card. The fixture is blocked by its existing no-retry policy;
ordinary retry policy, partial preload behavior and unknown crash handling are
unchanged. All 958 installed targets match on both hosts. Desktop UI and
continuous production Captain behavior are not newly validated by this change.

## Recall Unicode validation work (v0.8.21)

The [Unicode scan optimization](recall-unicode-work.md) preserves surrogate
handling while removing per-character Python callbacks. A portable registered-tool
work-budget regression failed before repair and passed afterward; 213 scoped
Python cases across 13 files pass without retries. Native Linux/Mac exhaustive
Unicode and nested-shape checks agree. A fresh native full-recall card returned
all three codes in three physical requests without a post-completion request.
All 959 installed kit targets match on both hosts. No new general latency,
provider cache-saving or Desktop UI claim is made.
