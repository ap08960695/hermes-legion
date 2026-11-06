# Worker monitor readability

A long current-tool name could consume the whole progress row and clip step, elapsed
time and input/output tokens. Progress facts now wrap, including a tool name wider
than the row. The existing hover tooltip includes the activity description and all
displayed facts. Existing localization, live-worker eligibility and chat navigation
are preserved. No polling, model requests or telemetry fields are added.

## Verification

The new tooltip regression fails on the prior component. The repaired selection
passes 62 tests across seven files, including ended/retained workers, progress
formatting, roster navigation, pause notice and status snapshots. Renderer TypeScript,
scoped lint and source-health checks pass. Existing unrelated test warnings remain;
this is not a fresh full-Desktop-suite run.

An offline browser fixture renders the actual React component using the installed
stylesheet. With a long tool name, the original loses progress facts at row widths
440, 280 and 200 pixels. After repair, step, elapsed time and tokens stay inside all
three rows while resizing between viewport widths 1280, 580 and 320. The page is
nonblank, has no error overlay or page exceptions, and the narrow screenshot was
visually inspected. Tooltip pointer interaction is covered separately in the
component test. This fixture is not the full application or a live worker run.

Matching source was installed on Linux and ARM64 macOS before publication. Both
Desktop packages were rebuilt without launching Electron; the Mac Finder copy was
updated and passes strict signature verification. Packaged application assets match
the compiled output, and both compiler receipts match the current renderer source.
The first Linux packaging attempt could not fetch tool metadata with networking
denied; compilation succeeded, and packaging completed after allowing the normal
pinned build-tool acquisition. GPU access remained unavailable to the Linux build
and browser; the Mac build denied IOKit access.

The 914-path kit is checked against both installed source trees. Public patch
apply/reverse/reapply, the companion tests and release/privacy checks are separate
from UI acceptance. No production performance or usage saving is claimed.

## Live acceptance boundary

Owner stops, configuration and Gateway identity were preserved. A simple test card
was created and read back in blocked, unassigned state with no worker, run or session.
No GPU computation, model inference, worker launch, dispatch, session resume or
service restart was performed. The owner's original application session and live
worker monitor remain unverified; installing a rebuilt app does not prove adoption
by an already-running process.
