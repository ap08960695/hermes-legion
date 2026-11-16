# Keep settings edits when leaving the page

In v0.8.11, editing Memory Budget and immediately closing the settings panel
discarded the edit. The renderer cancelled its 550 ms debounce on unmount; an
immediate reload had the same result.

The shared config editor now hands each sparse edit to Electron immediately.
Electron owns the debounce and ordered writes, captures the original route, and
flushes accepted edits before a config read, profile rename/delete, window close
or application quit. Adjacent compatible edits can coalesce. Legacy routing and
explicit registry routing retain their existing destination semantics.

Failed and unsent writes remain queued in order. A refused save is a failure,
and a subsequent successful read cannot hide it. If a close or quit cannot save,
the window stays available and a nonmodal notification reports the failure;
another explicit close retries. Changes to credentials or tenant headers split
the captured route. Profile and connection switches isolate drafts and cache
acknowledgements, including replies that arrive after navigation.

From v0.8.15, the shared merge also [preserves nested edits followed by a null
section](settings-null-sections.md), matching the native API rather than dropping
those edits during coalescing.

## Lists commit before Escape closes Settings (v0.33.5)

Focused comma-separated lists now commit through their existing blur handler
before Escape closes Settings. For example, an added Environment Passthrough
entry survives closing and reopening the page. Typing remains a local draft
until commit; Enter, ordinary blur, trimming and empty-list parsing retain their
existing behavior. IME cancellation does not trigger the new Escape commit.
This does not add a general save-on-unmount or crash-recovery mechanism.
[Checks and limits](release-notes-v0.33.5.md).

## Fractional compression arrows (v0.33.4)

Under **Memory & Context → Context & compression**, Threshold and Target arrows
change the stored ratio by 0.01, one percentage point. Increasing 0.50 becomes
0.51; counts and seconds retain their existing unit steps. Typed numeric values
use the existing save path. Updating does not rewrite earlier saved settings or
add new range validation. [Checks and limits](release-notes-v0.33.4.md).

## Export and Reset use the displayed profile (v0.33.3)

Settings Actions captures the displayed **Applies to** profile and connection
when Export or Reset starts. Changing the selection while a read or confirmation
is pending keeps that action on its original target. Reset names that profile
before confirmation; Cancel performs no defaults read or write. A refused Reset
save reports failure. Reset retains the native merge behavior; it does not remove
extra configuration keys. [Checks and limits](release-notes-v0.33.3.md).

## Partial imports preserve the form (v0.33.2)

Import merges sparse JSON into the displayed record with the same section rules
as the native writer. Untouched switches, budgets and other fields keep their
values during pending, failed and repeated imports. A following ordinary edit
still submits only its intended change. Empty imports preserve the form; explicit
values retain the existing null/list semantics. A file read superseded by a
newer edit or leaving the view is discarded; import again to apply it. Native
Local first/repeated imports, next edit and reopen passed.
[Checks and limits](release-notes-v0.33.2.md).

## Import acknowledgements (v0.33.1)

Actions → Import config announces success only after the current native save
acknowledges it. Cancelling toolset removal, failing a save, leaving the view or
superseding the import cannot produce a stale success toast. Save failures retain
their existing guidance; restore write access and import again. Non-object JSON
is refused before changing the draft. Admitted native saves retain their owner
and cache behavior. Native Local cancellation, permission refusal, retry and
reopened-value checks passed.
[Detailed checks and limits](release-notes-v0.33.1.md).

## Verification

- 72 tests across nine UI and Electron files pass. Regression cases cover
  immediate handoff, rapid reverts, failed predecessor recovery, routing aliases,
  tenant headers, profile/connection switches and quit ordering.
- Renderer and Electron type checks, scoped lint and source health pass.
- Linux and ARM64 Mac packages were installed before publication. Both have the
  same source hash; packaged files match their compiled output. Mac Finder
  adoption is verified; this release does not claim interactive Mac acceptance.
- The installed Linux app, using its native private Gateway and an isolated
  home, preserves an edit followed immediately by Escape, renderer reload,
  window close and app quit. Closing the window is followed by a cold reopen
  and UI readback. Quit is checked against the saved file.
- No GPU devices were available to the Linux test. No worker or model request
  ran, and the production Gateway was not restarted.

## Local profile persistence acceptance (v0.33.3 follow-up)

On the Mac, the native shared editor saved Memory Budget for two Local profiles
independently: default from 3111 to 3333 while scope-b was active, then scope-b
from 4222 to 4333. Disk readback after each edit showed the intended profile
changed and all other config values preserved. The untouched profile stayed byte
exact after the first edit. Switching back and reopening Settings showed 3333.

The first app, gateway, helpers and watchdog all stopped before new processes
opened the same task home and profile files, retained in place. The new app read
3333 and 4333 through Settings without editing; both config hashes matched the
pre-restart snapshots. Both session stores stayed empty; no Send or inference ran.
Native saves tightened the synthetic files from 0644 to 0600 as designed; original
bytes and modes were restored after the last writer stopped.

Both Local launches passed actual 60-second SSH-zero gates, sampled at most four
Hermes processes, and closed normally. Observer-inclusive sampled RSS maxima were
907,018,240 and 874,299,392 bytes, without a memory-saving claim. The original
313-entry trial bundle and strict signature were restored. This follow-up adds
acceptance evidence, with no runtime change or new release. It does not establish
immediate-switch/quit flushing, failure recovery, crash durability, selector
persistence, other settings pages or remote behavior.

## Native keyboard and leave-page acceptance (v0.33.4 follow-up)

On the Mac, Settings search for `compression.threshold` returned the exact
Compression Threshold field. Down selected the result; Enter opened **Memory &
Context → Context & compression** and focused its highlighted row. Tab entered
the number control. ArrowUp changed 0.50 to 0.51, followed by navigation to
Persistent memory; returning showed 0.51.

Shift-Tab from that number control focused Auto-Compression. Space switched it
off, then Escape closed Settings. Independent native file readback showed only
the intended threshold and enabled changes, with all other values preserved and
the other profile's file byte exact. Reopening Settings showed 0.51 and the switch
off without another config change. Both session stores stayed empty; no Send,
model request or compression execution ran.

This verifies search routing, keyboard access and saved values after navigation
and closure. It does not establish that disk persistence completed before the
550 ms debounce deadline, crash durability, every Settings page or remote
behavior. The current v0.33.4 runtime was reused without a source or build change.

## Native Mac failed Quit and recovery (v0.33.5 follow-up)

With Settings applying to default while scope-b was selected for new chats,
Memory Budget changed from 3111 to 3456. The isolated settings folder deliberately
refused writes. Autosave showed write-access guidance; CmdQ caused another native
save failure and kept the same app/window open with draft 3456. The file still
contained 3111 and the other profile stayed byte exact.

After restoring write access, a second CmdQ, without another edit, saved the
retained value and exited normally. Native quit events and exit code 0 were
recorded before the test guardian began cleanup. All writers/helpers and the
first guardian ended before fresh processes reopened the same home and app data
with the same build. Settings read 3456; native config bytes matched the saved
file. This is byte preservation, not proof that no writes occurred on reopen.

Both Local cohorts passed actual 60-second SSH-zero checks and kept session
stores empty. Original config bytes/modes and the trial app bundle/signature
were restored after the last writer ended. No runtime change or new version was
needed. This covers failed application Quit and explicit retry; title-bar close,
crash, disk-full, network-failure and persistence-before-550-ms behavior remain
outside this native check. [Detailed evidence](verification.md#native-mac-settings-quit-recovery--v0335-follow-up).

## Native Mac title-bar close recovery (v0.33.5 follow-up)

With minimize-to-tray disabled, the native window close button was tested
separately from application Quit. Settings applied to default while scope-b was
selected for new chats. Memory Budget changed from 3111 to 3456 in an isolated
home that refused writes. After autosave failed, clicking the native close button
caused a new native flush failure and retained the same window, draft and
write-access guidance. The file stayed at 3111; the other profile stayed byte exact.

Restoring write access and clicking close again, without another edit, saved 3456
and destroyed the window before test cleanup. The Mac application remained alive;
this was a window close, with no application Quit. After all writers and the first
guardian ended, fresh processes reopened the same home, app data and build.
Settings read 3456 and the file matched its post-close bytes. Complete mapping
checks preserved unrelated settings. Both session stores stayed empty.

Both actual 60-second Local SSH-zero gates passed. All owned processes and ports
ended before original config bytes/modes and the trial bundle/signature were
restored. No runtime change or version bump was needed. This does not establish
zero writes on reopen, persistence before 550 ms, crash durability, disk-full or
network-failure recovery. [Detailed evidence](verification.md#native-mac-title-bar-close-recovery--v0335-follow-up).

## Native Mac Chat behavior persistence (v0.33.7 follow-up)

In **Settings → Chat → Behavior**, Reasoning Blocks was switched off for default
while scope-c was selected for new chats. Navigation went directly to Attachments
and back; the switch remained off. Native file comparison showed only the intended
global and local CLI reasoning flags changed. The other two profiles stayed byte
exact, and all unrelated default settings were preserved. Selecting scope-b showed
its unchanged on value; returning to default showed off.

Every first app, gateway, helper and guardian stopped before fresh processes
reopened the same home, app data and exact signed diagnostic bundle. Without
another edit, Settings showed default off and scope-b on. All three config files
matched their saved bytes and modes. No Send or inference ran; session, message,
delegation and hosted-room stores stayed empty.

Both launches passed actual 60-second Local SSH-zero gates. Original config bytes
and modes and the trial bundle/signature were restored after all writers ended.
No runtime change or new release was needed. This accepts the named preference's
navigation, profile isolation and restart readback; it does not verify reasoning
output rendering, persistence before 550 ms, crash recovery, every Chat control,
all Settings pages, selector persistence or remote behavior. Previous startup
paint symptoms remain unresolved. [Detailed evidence](verification.md#native-mac-chat-behavior-persistence--v0337-follow-up).

## Native Mac Workspace preference persistence (v0.33.7 follow-up)

In **Settings → Workspace → Shell environment**, Persistent Shell was switched
off for default while scope-c was selected for new chats. In **Files & execution**,
File Read Limit changed from 100000 to 120001. Navigation went directly from the
focused number input to Shell environment, without Enter or a separate blur step.
Returning showed the saved limit. Switching Settings to scope-b showed its
unchanged on/100000 values; default retained off/120001.

Native comparison found only `terminal.persistent_shell` and `file_read_max_chars`
changed in default. Every other default value and both other profile files were
preserved. After all first writers and the guardian ended, fresh app/gateway
processes reopened the same home, app data and exact signed bundle. Both profiles
showed their previous values without another edit; all three config files matched
their saved bytes and modes.

Both launches passed actual 60-second Local SSH-zero gates. All owned processes
and ports ended before original configs/modes and the trial bundle/signature were
restored. No runtime change or release was needed. This accepts saving and reading
these two preferences. No terminal, SSH backend or file-read tool executed; their
effects, numeric boundaries, persistence before 550 ms, crash durability, Projects
controls and the rest of Settings remain unverified. [Detailed evidence](verification.md#native-mac-workspace-preference-persistence--v0337-follow-up).

## Attachment size drafts on Escape (v0.33.8)

In **Settings → Chat → Attachments**, Escape now commits a focused Max preview /
image load size draft before closing the overlay. It uses the existing blur
commit and normalization. Empty input resets to 16 MB; below-minimum values use
the 1 MB floor. Enter and moving focus retain their behavior. IME compositions
do not trigger the new Escape save; unrelated unmounts do not save drafts.

This cap belongs to the device, despite the page's profile selector. Native
before/after checks reproduced 16 → 1 → Escape losing the draft before the fix
and retaining it afterward. Another profile showed the same 1 MB. Fresh processes
reopened the exact signed build with the same home and app data and read 1 MB
without another edit. Cap bytes/mode and all three unchanged profile configs
matched. All writers ended before original cap absence and trial bundle/signature
were restored. The first final observer was interrupted; its final resource
statistics are unavailable, and recovery verified closure before restart.

This accepts cap persistence only. Actual attachment rejection, uploads, native
IME, Image Attachments mode effects, crash durability and write-failure reporting
remain outside this proof. [Checks and limits](release-notes-v0.33.8.md).

## Native Mac Projects preference persistence (v0.33.8 follow-up)

In **Settings → Workspace → Projects & discovery**, default's Working Directory,
Automatic Repository Discovery, Repository Discovery Roots and Excluded Repository
Paths were edited while scope-c remained the profile for new chats. Discovery
was confirmed off in the native config before changing either path list. Every
cwd, root and exclusion stayed inside the isolated trial's synthetic directories.
The final exclusion edit was followed directly by navigation to Shell environment,
without Enter or a separate blur step. Returning retained all four values.

Settings profile switches showed scope-b and scope-c's distinct original paths
and on/off values; default retained its edits. Native comparison found only the
four intended default keys changed. All unrelated default values and both other
profile files were preserved. After every first writer and guardian ended, fresh
processes reopened the same home, app data and exact signed bundle. All three
profiles showed their saved values without another edit; saved config bytes and
modes matched the checkpoint.

Both actual 60-second Local SSH-zero gates passed. All owned processes/ports and
Computer Use ended before original config bytes/modes and the trial bundle/signature
were restored. No runtime change or version bump was needed. This accepts saving
and reading the four named preferences. Repository discovery results, empty-root
home scanning, cwd effects on tool execution, invalid paths, pending-save profile
races, crash recovery, daily-app adoption and Linux/ai remain unverified.
[Detailed evidence](verification.md#native-mac-projects-preference-persistence--v0338-follow-up).

## Limits

All config operations share one ordered queue because legacy aliases and registry
connections can target the same file. An unresolved failed write can therefore
block other config reads/writes until its destination recovers. Routing changes
must not silently send retained edits to a replacement destination.

Pending edits live in process memory. Forced termination, a crash or power loss
is not covered. Native Linux permission-failure recovery is now verified; see
[write-error guidance](settings-write-errors.md). Native network-failure injection
remains unverified. Specialized editors outside the shared config page
retain their existing save behavior.
