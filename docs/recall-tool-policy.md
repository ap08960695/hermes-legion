# Optional eager tool schema for recall workers

A worker dedicated to searching saved conversations can expose `session_search`
at initialization instead of discovering its schema during each task. This uses
the existing native `tools.tool_search.defer` setting. It changes tool visibility,
not search permissions, history boundaries or the mandatory first `kanban_show`.

The [merge fragment](../examples/native/recall-tools.fragment.json) contains the
pinned stable kit's 19 default deferred tool names minus `session_search`. Its
18-name list **replaces**, rather than extends, the selected profile's defer list.
It is optional and must not replace an entire config. Native automatic tool-search
selection remains in effect; other MCP and plugin tools may still be deferred by
their existing classification rules.

## Select a profile deliberately

Use this for a profile whose routine tasks need saved-history search. Making a
schema eager adds it to initial requests even when the task does not use it.
General-purpose profiles can therefore spend more input on irrelevant tools.
Do not distribute this setting across the fleet from the measurement below.

Before applying, inspect the selected profile's `config path` and record whether
`tools.tool_search.defer` is explicitly set, together with its previous value.
If customized, remove only `session_search` from that existing list instead of
overwriting it with this pinned example. Recheck native defaults after upgrades;
a copied list will not automatically inherit newly deferred core tools.

For an existing example profile with the pinned default defer list:

```sh
: "${HERMES_BIN:?Select the supported native Hermes executable}"
: "${RECALL_FRAGMENT:?Select examples/native/recall-tools.fragment.json}"
"$HERMES_BIN" --profile legion-archivist-codex config path
# Continue only after confirming this is the intended profile and recording its prior value.
recall_deferred_tools=$(python3 -c 'import json,sys; print(json.dumps(json.load(open(sys.argv[1]))["tools"]["tool_search"]["defer"]))' "$RECALL_FRAGMENT")
"$HERMES_BIN" --profile legion-archivist-codex config set tools.tool_search.defer "$recall_deferred_tools"
"$HERMES_BIN" --profile legion-archivist-codex config get tools.tool_search.defer
```

Select any other profile explicitly. The native per-key setter preserves unrelated
settings; root and other profile configs are separate. New agent initialization
reads the choice. Preserve active turns and use the normal idle adoption procedure
if needed. Roll back only this key to the recorded previous list; if originally
absent, use `config unset tools.tool_search.defer` on the same selected profile.
Do not restore a whole old config over newer unrelated edits.

## One bounded native comparison

Two isolated simple cards used the same task body, synthetic 256-message archive,
provider, model and reasoning effort. Both recovered the correct code from message
137 of a conversation approximately 30 days old; neither the answer nor its title
was in the task prompt. Each card searched the same content keyword once. There
were seven physical cloud requests in total, with no retry or fallback.

| Observed result | Default deferred search | Eager search |
|---|---:|---:|
| Correct, durably completed card | Yes | Yes |
| Physical model requests | 4 | 3 |
| Total input tokens, including cache reads | 45,436 | 35,838 |
| Uncached input tokens | 14,844 | 14,590 |
| Cache-read input tokens | 30,592 | 21,248 |
| Output tokens | 112 | 80 |

Both workers first called `kanban_show`, then searched and completed their card.
The default worker also called `tool_describe` before searching. Preparing the
schema removed that discovery turn in this pair: 25% fewer requests and 21.1%
fewer total input tokens. Uncached input fell only about 1.7%; this is **not** a
21.1% billing-saving measurement. Fewer repeated requests also reduce cache-read
tokens, so cache-hit percentage alone is not the optimization target.

This was one sequential pair. Runtime IDs, timestamps, provider caches and server
conditions differed. Observed durations were 75 and 11 seconds; they do not establish
a general latency improvement. Other tasks may discover tools differently, require
more searches, or never use recall at all.

An offline search-only schema comparison grew from 2,282 to 5,312 JSON bytes when
the schema was eager. These are neither full worker prompt sizes nor token counts.
The extra initial schema is the tradeoff for potentially avoiding a discovery turn.

## Verification boundary

The installed native runtime ran both cards in isolated homes with GPU devices
unavailable. Production settings, credentials and the stopped production queue
were preserved. This recipe adds no runtime patch and does not change production
profiles automatically. The cumulative 952-path source kit remains unchanged.

Offline native setter/readback checks cover the fragment as a real list, preserved
unrelated settings, unselected homes, eager search assembly and per-key rollback.
They use temporary homes with network and GPU access unavailable and make no model
requests. These configuration checks do not establish Mac UI adoption, fleet-wide
savings, semantic recall or unrestricted Captain continuation.
