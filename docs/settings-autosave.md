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

## Limits

All config operations share one ordered queue because legacy aliases and registry
connections can target the same file. An unresolved failed write can therefore
block other config reads/writes until its destination recovers. Routing changes
must not silently send retained edits to a replacement destination.

Pending edits live in process memory. Forced termination, a crash or power loss
is not covered. Failure recovery is verified in automated tests, not by native
network-failure injection. Specialized editors outside the shared config page
retain their existing save behavior.
