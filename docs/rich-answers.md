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
