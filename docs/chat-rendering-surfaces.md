# Chat rendering across surfaces (v0.8.38)

Hermes renders the same assistant text on three surfaces with different
capabilities. The model is now told what each one can show, and the web dashboard
shows tables.

| Surface | Tables | Code | Math | Mermaid / chart fences |
| --- | --- | --- | --- | --- |
| Desktop app | yes | highlighted | yes | rendered as diagrams and charts |
| TUI (terminal) | yes | yes | shown as Unicode | not rendered; the hint steers the model to tables or indented sketches |
| Web dashboard session viewer | yes (new) | yes, with a language label (new) | no | shown as labelled source |

## Read and enlarge Desktop charts (v0.32.0)

Click a valid chart to open the existing pan/zoom viewer. Its full view includes
title, unit and legend. Below the inline chart, open **Chart values** to read
every category, series and parsed value. Full labels, repeated category names,
decimals, zero and negative values stay distinct. Press Tab after opening the
disclosure to focus the table area, then use the arrow keys or Page Up and Page
Down to scroll. Both the disclosure and table area show a keyboard focus
outline, including in forced colors. In Chat, focus stays in the disclosure
or table when you move the pointer. In a short Chat window, keyboard focus
brings the caption below the pinned prompt when there is room above the
composer. Closing the disclosure removes the table until you reopen it.

Dense Cartesian axes show at most four category ticks; all plotted data and the
full table remain. Existing parser bounds and text escaping stay in place.
The table does not round numeric values, but JSON/JavaScript precision lost
during parsing cannot be restored. This adds no data fetch, model request or
saved-text mutation. The shared viewer registers its opener through the normal Dialog/Trigger
contract. In the native shell, Close and Escape return to Chat with the composer
focused.

Apply the source kit and rebuild Desktop. Existing translations provide Open
preview, Details and Category; viewer toolbar language behavior stays unchanged.
[Verification and limits](release-notes-v0.32.0.md).

## Native Local Mac acceptance (2026-11-16, after v0.29.0)

The existing Desktop renderer passed a bounded native Mac walkthrough:

- A Markdown table displayed its English headers, Thai/English cells and counts.
- A valid `chart` fence displayed a bar chart with values 3, 5 and 2, title,
  category labels and units.
- A valid `mermaid` fence displayed Read -> Check -> Done after its deferred
  renderer loaded. Open diagram opened the viewer; Escape returned to Chat.
- An incomplete chart specification stayed readable as source. Its following
  text and the surrounding valid formats remained visible.
- The cases fit wide and narrow windows. Closing the chat tab and reopening
  the same saved chat from History retained the rendered formats and fallback.

The isolated Local chat was created through the native session API; its saved
assistant text was synthetic. Screenshots measured 3010x1776 and 1712x2018
pixels, not CSS viewport sizes. The launch passed its 60-second SSH-zero gate;
all owned processes stopped, the gateway closed, configuration stayed exact,
and the original trial bundle was restored with a verified strict signature.
Owner data and other hosts were untouched. Private images and receipts remain
outside the package, referenced by the local work report.

No runtime change or new feature was needed. This is acceptance documentation;
it adds no version and does not replace the existing v0.29.0 tag or artifact.
Large tables, streaming, line/pie charts, other Mermaid families, clipboard/file
exports, live model generation, Linux parity and daily-app adoption were not
checked. This bounded display proof does not close the entire Chat walkthrough.

## Changes

- `agent/prompt_builder.py`: the `tui` platform hint names what renders and says
  that ```` ```mermaid ```` and ```` ```chart ```` fences print as raw source. It
  stays one static line, so a session's cached prompt prefix stays stable. Sessions
  started before this release keep their old hint.
- `web/src/components/Markdown.tsx`: GitHub tables, using the TUI's divider rule,
  render as a scrollable `<table>`, with inline formatting kept in each cell. A
  fenced block shows its language, so a mermaid or chart fence can be recognised.
  A lone line containing a pipe stays text.

## Evidence and limits

- Two of the three new web cases fail on v0.8.37 and pass now. All 452 web cases
  in 66 files pass, and the TypeScript check is clean.
- The TUI hint case fails on v0.8.37. 97 prompt-builder and hint cases pass.
- The 12 native check groups pass, except `profile-archives` for untracked packager
  archives in the dev checkout.
- The source files are installed in the live Linux and Mac checkouts with matching
  SHA-256 values.
- The web bundle builds into a scratch directory. The installed `web_dist` was not
  rebuilt, because another session is testing the running dashboard on Linux.
  Rebuild it with `npm run build` in `web/` when that dashboard is free.

## TUI agents panel shows what a subagent is doing (v0.8.39)

The Desktop bot row already showed a worker's tool, step, elapsed time and tokens.
The TUI's docked agents panel showed only the latest note. A running subagent's row
now also shows its current tool and step, for example
`Reading the config · read_file config.yaml · step 4`. A tool already shown as the
note is not repeated.

Two new cases cover this, and one of them fails on v0.8.38. All 1,882 TUI cases
pass (2 skipped), and the TypeScript check is clean. The local `hermes-ink` package
had to be built first, because its `dist/` was missing in the dev checkout. Source is
installed on Linux and Mac with matching hashes. These git-checkout installs ship no
prebuilt `hermes_cli/tui_dist`, so the TUI launcher rebuilds `ui-tui/dist` by itself
when the sources are newer (`_tui_need_rebuild`). Only `web_dist` needs a manual
`npm run build`.

## Bounded Git-label cache (v0.8.53)

The terminal status bar reads Git labels directly from local files. Its five-second
cache previously retained every distinct working directory indefinitely, including
empty labels outside repositories. It now retains at most 128 directory entries,
evicting the oldest inserted entry when a new one exceeds that bound. Fresh hits
do not walk the Git directory or reorder entries; an expired refresh keeps its
insertion position. The existing five-second freshness rule remains unchanged.

The same helper serves the classic status snapshot and modern layout. Branches,
worktree pointers, optional UTF-8 BOMs, detached HEAD labels and outside-repository
results retain their behavior. No subprocess, provider request, background cleanup,
new setting or renderer change is introduced.

Seven native regression/control cases pass after three failures on the previous
implementation. They cover 512 real directories for both positive and empty labels,
the exact five-second boundary, hit-time I/O refusal, eviction/recomputation and
expired refresh ordering. Fifty adjacent native status/layout cases also pass.

Separate native Mac Python 3.14.9 processes run the same 512-directory fixture,
with identical paths, a fixed clock and prebuilt workload bookkeeping. All returned
labels match. Tracing begins after module warmup/cache clear; net retained traced
Python allocation is compared against an idle snapshot after garbage collection:

| Observation | Before | After |
| --- | ---: | ---: |
| Retained cwd entries | 512 | 128 |
| Net retained traced allocation | 147,730 bytes | 49,625 bytes |

This is one synthetic component measurement, not process RSS, whole-service RAM,
latency or billed savings. The entry bound is not a byte limit or a measured optimal
capacity. Idle expired entries can remain within the bound. Cycling through more
than 128 directories may require additional file reads. Owner source/services are
not updated or restarted by this acceptance; adoption remains separate.
