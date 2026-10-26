# Shared Spaces

Spaces is a local native Desktop feature for pages and copied files that selected bots can read together. It requires the complete Hermes Legion patch and a normal rebuilt Desktop lifecycle. It is not a connection to ChatGPT Space or a cloud synchronization service.

## Create and use a Space

1. Open **Spaces → New Space**, enter a title, and select existing bot profiles on that connection. An empty member list is private.
2. Use **New page** for Markdown or **Add files** to choose files explicitly. The app copies the selected bytes into the Space; it never moves or edits the original file.
3. Open supported files in the internal viewer. Unsupported formats remain listed with preview disabled. Use **Manage bot access** to add or revoke readers.
4. Use the trash icon to remove an item after confirmation. **Trash → Restore** recovers it. This is recoverable removal, not secure erasure.
5. **Copy bot reference** copies instructions and the Space ID. Give that reference to an appropriate bot through the normal work flow when needed; copying never sends a message or calls a model.

The workspace follows its captured native connection/profile. There is no automatic import of old chats, documents or private folders. The owner UI manages content; bot CLI commands are read-only.

## Read from an existing bot

Use the existing terminal tool in that bot's native profile environment:

```sh
python -m hermes_cli.spaces list
python -m hermes_cli.spaces items SPACE_ID --limit 50
python -m hermes_cli.spaces read SPACE_ID ITEM_ID --offset 0 --limit 8000
python -m hermes_cli.spaces export SPACE_ID ITEM_ID --output /owned/workspace/shared-file.pdf
```

Replace the identifiers from the owner UI or list output. The current native profile identifies the reader; no alternate-profile flag is provided. Profiles sharing one canonical Hermes root use the same catalog and content revision. Independent hosts/roots do not silently share storage.

List/items returns bounded metadata with a next offset. Read returns at most 32,000 text characters per request (default 8,000). Binary content requires explicit export; export creates a new file exclusively and refuses overwrite. Reuse unchanged item revisions, read only relevant sections, and avoid attaching the whole Space to every model request. No extra model call, new quota, provider route or paid fallback is introduced.

## Safety and limits

The existing authenticated owner UI controls membership and mutations. API/CLI membership is an application policy, not a new operating-system sandbox: a bot already granted unrestricted filesystem or terminal access keeps those privileges. Do not use this as isolation against a malicious process with the same OS access.

Native sensitive credential filenames are refused, but arbitrary document contents are not a secret scanner. Review files before sharing them. The catalog lives under the canonical Hermes root in `spaces/catalog.db`, created on the first explicit write, with private directory/file modes. This is separate from the existing conversation and Kanban databases.

Pages are limited to 1 MiB of UTF-8 bytes; each file to 8 MiB; the picker handles at most 16 chosen files per operation. The owner list is bounded to 500 Spaces and 1,000 items per Space; the bot CLI paginates this metadata. Writes use revision checks, so a stale edit or membership change is refused rather than silently overwriting newer data. Refresh before resolving a conflict. Removed copied bytes remain in trash until restored; this release has no purge button.

HTML uses the existing sanitized opaque preview sandbox; files are never executed. A preview/read does not grant approval to publish, edit the original source, change gates, or spend quota.
