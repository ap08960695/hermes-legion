# Mermaid diagrams in Desktop

Use a Mermaid fence in an assistant reply or a Markdown file. Chat, the
Markdown preview pane, and the Hub Markdown preview share the same renderer.
Hub also offers the original file in its Source tab.

````markdown
```mermaid
flowchart LR
  accTitle: Review workflow
  Draft --> Review --> Publish
```
````

Click the diagram to open the zoom and pan viewer. **Copy source** copies the
original Mermaid text. **Save SVG** saves a scalable image, and **Save PNG**
saves a raster image. The diagram uses the app's light or dark appearance at
render time. A failed diagram shows a short explanation and its source.

## Answer cards

An existing `cards` block can include one Mermaid diagram per card. Put the
source in the card's optional `mermaid` field, or put a Mermaid fence inside
the JSON string for `description` using escaped newlines.

````markdown
```cards
{
  "cards": [{
    "title": "Review workflow",
    "description": "Illustrative workflow.",
    "mermaid": "flowchart LR\n  Draft --> Review --> Publish"
  }]
}
```
````

## Supported diagrams and limits

Flowchart, sequence, class, state, Gantt, entity relationship, pie and mindmap
diagrams load from the local Desktop bundle. Mermaid runs at strict security
level with SVG labels inside an isolated renderer. In-diagram configuration,
custom styles, links, icon and image resources, and HTML labels are restricted.
Use plain text, or a line break within a label. SVG exports retain static SVG
and local references such as arrow markers.

Each render is limited to 12,000 characters, 160 lines, 100 edges, 512,000
characters of SVG and a five-second layout deadline enforced by Electron.
Raster exports fit within 4096 pixels per dimension. The helper starts when a
completed Mermaid fence needs rendering and closes after a brief idle period.

## Fixture verification

The [six-diagram fixture](../examples/mermaid-fixture.md) includes an invalid
fence. The light and dark captures use the Desktop components with synthetic
content. An isolated Linux Electron run also decoded all eight diagram types
in both themes, opened the exported SVG as a document, rejected active input,
and terminated a stalled helper while the main window stayed responsive.

[Light-theme fixture](images/mermaid-fixture-light.webp) ·
[Dark-theme fixture](images/mermaid-fixture-dark.webp)
