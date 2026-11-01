# Rich answers in native chat

The Desktop renderer keeps the existing chat history and Markdown engine. Comparison tables use quiet horizontal rules and retain resizing and horizontal scrolling. Existing Markdown images, source links, Mermaid diagrams and sandboxed artifacts remain available. The patch does not rewrite old conversations or ask a model to regenerate them.

## Opt-in answer cards

A message can contain a `cards` fenced JSON block. Values must come from the author or verified sources; the renderer never infers prices, facts or citations and never fetches page metadata.

````markdown
```cards
{
  "cards": [{
    "title": "Example computer",
    "price": "100 units",
    "description": "Illustrative data, not a product recommendation.",
    "facts": ["Example specification"],
    "sources": [{"title": "Example source", "url": "https://example.com/item"}]
  }]
}
```
````

Optional `images` is an array of supplied safe HTTP(S) image URLs or supported base64 image data URLs. Images load lazily; remote image URLs still contact their host when displayed, so prefer approved sources. Titles, price, description, facts and sources are literal supplied values. There is no shopping API, remote metadata resolver or autonomous browsing.

The parser bounds input to 256,000 characters, 16 cards, 6 images, 12 facts and 8 sources per card, with per-field limits. File/javascript URLs and credentials in URL authority are refused. Malformed complete JSON falls back to the source block; partial streaming content shows a loading state without repeatedly throwing. Invalid source data does not become an invented citation. Existing long-code artifact detection leaves `cards` blocks inline.

These are native display components, not an embedded ChatGPT page. Rendering does not add model requests, tools, paid providers or a background polling loop.

## Narrow tiles

Cards choose stacked or side-by-side content from the space available inside the chat tile, rather than the whole window. Images and supplied text stay inside that tile when a preview is also open. This does not change the pane layout or fetch additional images or metadata.

## Inline charts and diagram guidance

A `chart` fenced JSON block renders as an accessible inline SVG chart with no new
package, network request or model call:

````markdown
```chart
{"type": "bar", "title": "Calls per day", "labels": ["Mon", "Tue", "Wed"],
 "series": [{"name": "calls", "values": [120, 95, 60]}], "unit": "calls"}
```
````

`type` is `bar`, `line` or `pie`. The parser accepts at most 12 series and 200
points, finite numbers only, and series that match the label count. Anything else
falls back to the original code block, as Mermaid and cards do. Charts follow the
light/dark theme colours, include a legend and expose each value through a
tooltip title. Long chart fences stay inline instead of becoming a side artifact.

The Desktop platform hint now names the rich blocks the renderer already
supports — `mermaid` diagrams, `chart`, `cards`, `<details>` and callouts — and
asks the model to use them only when they clarify the answer. The hint is static
text in the cached context tier, so it changes the cached prefix once and does not
add per-turn cost.
