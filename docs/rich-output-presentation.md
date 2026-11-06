# Rich output presentation

Sparse bar charts now use narrower rounded bars, visible values and rounded axis intervals. Chart titles and units share a compact heading; existing per-value descriptions and series legends remain available. Dense charts omit direct values to avoid overlapping labels.

Markdown tables use a restrained header tint, aligned numeric glyphs and a row hover cue while retaining column resizing and horizontal scrolling. Mermaid flowcharts use neutral light/dark styling, rounded nodes and gentler connections; strict sanitization, render caching, source fallback and click-to-expand behavior remain intact. No rendering dependency was added.

Compact navigation also reserves enough label width when a native scrollbar appears, preventing short labels from splitting inside a word.

## Verification scope

Fourteen focused renderer tests pass, including zero, negative and mixed-sign bars, accessible diagrams, cached rendering and Markdown overflow. Desktop type checking and the changed-component lint pass. A browser fixture using the actual components was visually checked at 1000 and 390 pixels, including dark mode, with no page errors or horizontal page overflow. Linux rendering ran with GPU devices unavailable.

Linux and Mac packages were rebuilt and installed before publication, with all 961 source targets matching the cumulative manifest. The signed Mac application and its Finder installation match. Native Mac saved-chat checks passed at 1505 × 888 and 800 × 700, including diagram expansion and dismissal, readable navigation labels and unchanged stored content. The fixture recorded zero new model calls or tokens; the production configuration remained unchanged and the private test Gateway was stopped. These checks cover saved-output rendering, not every application workflow.
