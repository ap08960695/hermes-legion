# Unified worker progress

The unified Gateway's `profiles.list` returned a worker identity and latest activity
stamp, but omitted the progress fields already supplied by the legacy roster. The
Desktop activity component consequently could not display step, elapsed time or
usage on this route. The same omission affected the current profile and hosted siblings.

Version v0.8.9 reads the existing progress columns in the same worker query, reuses
the shared bounded projection, and forwards the stored terminal timestamp. It adds
no query, polling loop, model call or dependency. Existing worker visibility and
reader scope are preserved. A terminal timestamp is forwarded when present; a
completed reusable worker session can retain a null timestamp and the UI's existing
activity freshness window still applies.

## Verification

Two regressions failed on the prior source with a missing activity-description key.
After repair, 36 tests across six roster/contract files pass. Scoped lint, source
health and independent code review found no blockers. Native installed production
Python passes three offline checks on Linux and ARM64 Mac. All 919 source paths
match both installed hosts; existing Gateway processes were not restarted.

Three small isolated cards completed through the native dispatcher, worker client,
Gateway and managed worker using an existing cloud connection. They used four
physical model requests in total. Two returned a short marker; one returned a
synthetic table, chart and Mermaid diagram. An earlier fixture launch failed before
any model request because its test hook imported runtime code before policy binding;
that failed run was retained and the fixture corrected in a new isolated case.
Production emergency stops and original board ownership were preserved.

The post-fix monitor run provided real observations with step 2, elapsed time, and
9.2k input / 68 output tokens. Its actual activity component and installed stylesheet
were rendered from a captured active observation at widths 320, 580 and 1280.
The rich response was also passed through the actual Markdown component, including
its chart and Mermaid rendering, at the same widths. These are component acceptance
checks using real card output; they are not full Desktop navigation or original-session
adoption. Test processes had no exposed GPU devices. No GPU inference was used.

No reduction in production latency, RSS, cloud cost or cache misses is claimed from
these short acceptance cases. Broad retention cleanup remains separate from this fix.
