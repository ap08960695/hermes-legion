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
