# Chat rendering across surfaces (v0.8.38)

Hermes renders the same assistant text on three surfaces with different
capabilities. The model is now told what each one can show, and the web dashboard
shows tables.

| Surface | Tables | Code | Math | Mermaid / chart fences |
| --- | --- | --- | --- | --- |
| Desktop app | yes | highlighted | yes | rendered as diagrams and charts |
| TUI (terminal) | yes | yes | shown as Unicode | not rendered; the hint steers the model to tables or indented sketches |
| Web dashboard session viewer | yes (new) | yes, with a language label (new) | no | shown as labelled source |

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
