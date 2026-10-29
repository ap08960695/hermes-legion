# Complete, ordered config backups

The native config-backup helper had three publication faults: distinct saves in
the same clock second could reuse a name and silently skip the newer config;
recovery could read a partially copied good file; and a failed copy could leave
that broken file as the newest recovery candidate. Rotation also used a listing
captured before copying, so six simultaneous writers with `keep=2` left seven
files in the reproduced case.

Backups are now copied into a hidden temporary file in the same backup directory.
After copying and file fsync, a plain atomic replace publishes the completed file;
the native directory-fsync helper follows. Recovery only lists published names.
An ordered nanosecond suffix plus the temporary file's unique suffix prevents
same-second name collisions. Each writer then rotates a fresh published listing.
On copy failure its own temporary file is removed and the previous good copy
remains available. No new dependency, lock pool, background job or setting is added.

## Existing behavior retained

- Default retention is still five copies per reason, with the existing `keep`
  override. Unchanged content still deduplicates in normal sequential saves.
- Published names retain `config.yaml.<reason>.<date>` with an additional unique
  suffix. Existing legacy names remain readable and native migration is retained.
- Backup bytes, source permissions and modification time are preserved by `copy2`.
- Owner-named sibling copies remain untouched. No existing user backup, database
  snapshot or recovery history is deleted, compressed, restored or rewritten by
  installing this patch. Future native backup calls apply their existing retention.
- Recovery still refuses a damaged newest published good copy rather than silently
  guessing an older configuration. Strict config and terminal-security readers
  retain their existing refusal behavior.

This change bounds the demonstrated concurrent rotation case; it does not promise
single-copy deduplication of identical simultaneous writes, immunity to all source
file races, or universal power-loss durability on every filesystem.

## Verification

All four behavioral regressions failed before the fix. The final native selection
passed 1,230 tests in 173 files, with zero failures,
4 existing platform skips and zero file retries. Code-health is clear.
Focused and historical runs overlap and are not added to this result.

Installed Linux and macOS each pass seven production-Python checks using private
synthetic files: rapid-save ordering/deduplication, reader visibility during a
barrier-controlled partial copy, failed-copy cleanup, six parallel writers with
retention two, byte/mode/mtime preservation, legacy migration and cold good-config
recovery. The last case uses a native SQLite local session created while config
is valid, followed by rapid owner-limit changes and damaged YAML: after clearing
the native config caches, the final request builder recovers the latest `high`
ceiling instead of the earlier `max`. It sends no provider request.

The initial standalone harness instead tried creating a new terminal-capable
session after corrupting YAML. The existing terminal-security reader correctly
refused that operation. The harness ordering was corrected; that security gate
was not changed or bypassed.

No account, model, quota, paid fallback, worker policy, prompt, tool list, dependency
or original user database changes. The original macOS Gateway is not started for
proof and no Desktop bundle is rebuilt. This is backup correctness and bounded
future retention, not a measured disk/RAM/token saving, provider-backed run or
proof of adoption by an original user conversation.
