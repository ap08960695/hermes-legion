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
