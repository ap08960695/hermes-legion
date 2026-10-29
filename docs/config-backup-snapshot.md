# Good backups contain the config generation actually parsed

Both native config readers previously parsed one generation of `config.yaml`,
then reopened its path to create the good backup. A concurrent edit in between
could replace the validated file with broken YAML or a valid but not-yet-loaded
config. The current process retained the validated settings, while a fresh process
could recover a different configuration or lose the usable backup entirely.

The default-merging and defaults-free effective readers now capture the file's
raw bytes and descriptor metadata together before parsing. Only after successful
parsing does the existing backup helper publish that exact captured snapshot.
Building the good backup no longer rereads a mutable source path. Ordinary setup,
corrupt-file and other backup callers retain their native live-file copy behavior.
There is no new cache, background writer, setting or dependency.

## Preserved contracts

- Keep raw UTF-8 bytes, including a BOM, CRLF line endings, comments and unexpanded
  environment templates. This is not YAML reserialization or expanded-secret export.
- Retain the parsed generation's permission mode and modification time, even if a
  later edit changes the source file's metadata before publication.
- Keep the native atomic publication, failed-write cleanup, same-second unique
  naming, default retention five per reason and sequential deduplication introduced
  or retained by [complete backup publication](config-backup-publication.md).
- Keep parser seams, default/managed merges, cache behavior, frozen-worker isolation,
  active-home-only backup scope and existing strict config/terminal refusal gates.
- A valid later configuration still becomes effective when normally read. This
  change does not undo an owner's valid limit removal or rewrite their config.

The snapshot is transient reader-local data and is not added to a persistent cache
or log. The snapshot path preserves bytes, mode and timestamps; it does not promise
to preserve every platform-specific extended attribute. No claim is made about
eliminating all filesystem races or providing universal power-loss durability.

## Verification and boundaries

Four behavioral cases failed on the previous native source: each of the two
readers parsed a Terra `high` limit, then a controlled concurrent edit replaced it
with either broken YAML or an unlimited mapping before backup. The old backup
contained that replacement. The fixed cases retain the original BOM/CRLF bytes,
permission mode, timestamp and parsed limit. Normal parsing remains at the native
loader seam; no source-text matching or fake operating system is used.

The final regression selection passes 1,234 cases in 174
files, zero failures, 4 existing platform skips, zero file retries.
Code-health is clear. Earlier focused and historical runs overlap and are not
added to these results or presented as a whole-project green.

Installed Linux and macOS each pass eleven production-Python controls with private
synthetic files and network denied. Seven retain the prior complete-publication,
metadata, legacy and native SQLite final-request recovery controls. Four inject
the source replacement after the actual parser returns, then clear the native
in-process caches and corrupt the current config: a fresh native read recovers
the validated `high` limit from the captured good backup. This is not inference.

No original user database, existing backup, account, model, quota, paid fallback,
prompt, tools or dependency is changed. No Desktop bundle is rebuilt or original
macOS Gateway started for proof. No measured dollar/token/RAM/disk saving or
original-user-conversation adoption is claimed.
