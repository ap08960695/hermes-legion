# Hermes Legion v0.32.0 — Read and enlarge chat charts

## What you will notice

Click a chart to open the same full-view pan/zoom controls used by Mermaid.
The larger view keeps its title, unit and legend. Open **Details** below the
inline chart to read full category and series names beside every parsed value,
including decimals, zero and negative values. Repeated category names stay on
separate rows. Close Details to remove its table from the page.

Dense category axes show fewer labels, so they do not pile up over each other;
Details retains every category and value. Close or Escape returns to Chat. Apply the source kit and rebuild
Desktop. The installed daily app is not replaced by this source release.

This groups chart enlargement, accessible tabular values and the native rich
report workflow into one reading capability set. Markdown tables and Mermaid
remain supported alongside chart fences in the same answer.

## Behavior and compatibility

The existing bounded chart parser and SVG drawing remain the source. The table
uses the same validated spec, indexed by position; it does not fetch data,
change saved text, round the parsed numbers or recompute statistics. JSON/JavaScript
number precision already lost during parsing cannot be recovered. Labels remain
subject to existing parser length limits. Bar, line and pie specs share the table.

The table mounts only while Details is open. It has a caption, column headers,
row headers and bounded scroll space; text is escaped by React. Full view mounts
only on demand, with intrinsic SVG dimensions and a viewBox for the house fit
logic. The shared viewer uses a normal DialogTrigger under its Dialog root,
which restores its opener in the component contract without a new keyboard
handler. The native shell refocuses the composer after Close or Escape. Its existing pan/zoom and
optional copy behavior remain. No new export feature, dependency, backend API,
polling timer, provider call, prompt/context change or schema migration.

Streaming/invalid chart fallback remains. The inline chart retains its original
size and values; only the density of category tick labels changes. Existing
translations supply Open preview, Details and Category. Existing viewer toolbar
labels retain their previous language behavior.

## Verification

Five original chart-feature cases fail before implementation, with seven controls
passing. Independent chart/shared close-focus cases fail on the first candidate.
The final nearest selection passes 19 tests across chart rendering, shared viewer
and fit behavior. It covers bar/line/pie data, full/duplicate labels, series/unit
mapping, zero/negative/decimal values, literal HTML-like text, lazy table mount/
unmount, intrinsic viewer geometry, close-focus restoration, dense ticks and
streaming/invalid fallback. Focused lint, types and renderer build pass; the
inherited dynamic-import warning remains. Four existing patch sections pass
pinned-base apply/hash/reverse; 1085 targets and test selection remain unchanged.

Native Mac acceptance used fresh empty Local homes and actual UI Send. The same
single controlled reply contained a Markdown table, nine-category/two-series bar
chart and Mermaid workflow. Before, the chart had overlapping category labels and
no full view or data table. After, the chart showed three spaced category ticks,
its larger view retained title/unit/legend, Zoom in and Reset worked, and Close
and Escape returned to Chat. The nine-row Details table retained full names,
repeated categories, zero, negatives and original parsed decimals. Collapsing
removed its rows. The Mermaid full-view/Escape path remained usable.

Native Reload, New chat, History and reopening the same saved report retained all
formats and chart values. Read-only snapshots kept its two messages unchanged.
One model request completed in each accepted cohort; opening the unsent New chat
draft added a second empty session but no request. Only model reply content and
timing were controlled on loopback; no lifecycle rows were seeded. The existing
native save trims the reply's terminal newline. Synthetic usage is not provider
usage, model quality or a saving measurement.

The shared close-focus contract has unit proof. In the native shell, focus moved
to the composer after both Close and Escape; this is not an opener-focus claim
for the whole app. Tests also isolated the toolbar tooltip consuming an initial
Escape before the modal. Native viewer closing succeeded on the exercised paths.

Accepted before/final launches passed actual 60-second Local gates with SSH0,
at most four sampled Hermes processes and observer-inclusive RSS maxima of
1,186,381,824/1,365,884,928 bytes over 1183/1917 samples. A preparatory launch was
stopped by its conservative process guard before CUA or Send: it counted an
app-owned login shell and the shell running an exact PID `ps` check as workers.
Raw records and negative identity/argument controls establish those two utilities;
the final guard retains their RSS/descendants and the original four-worker bound.
No resource or network limit was raised. The rejected run and failure log remain.

All three process sets ended; gateway/model ports and model threads closed.
Original 313-entry trial bundle, hashes, strict signature and baseline configs
were restored. No owner app/data, other host, ESTOP, pause or timer was touched.
Counts and RSS are samples, not continuous peaks or a RAM-saving comparison.
Private before/after images include r105-03-baseline-report.jpg,
r105c-03-readable-chart.jpg, r105c-04-full-data.jpg,
r105c-07-chart-full-view.jpg and r105c-20-history-data-retained.jpg. Dimensions,
hashes, raw state, control failures and rollback receipts stay outside the kit.

Native coverage is one wide Mac window and a bar chart; line/pie data have unit
proof. Native pan gestures, large tables, other Mermaid families, clipboard/export,
production model quality/usage, Linux parity and daily-app adoption remain open.
