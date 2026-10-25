# Storage and backup policy

Hermes data, its installation and your temporary/test files can occupy different
filesystems. Check the free space on each relevant volume. A large source tree,
paused workspace or backup is not automatically disposable because it is old.
Keep transcripts, credentials, active jobs, project outputs and held rollback
points out of automatic cleanup.

## Avoid redundant full backups

For an ordinary source patch, preserve the changed files and their mode/owner
metadata. For a restart that does not change data formats, preserve the settings
and UI state actually affected. Do not copy a multi-GiB conversation database on
every small patch or status check. A database migration or state-destructive
operation needs a supported, consistent database backup instead.

The pinned upstream already writes compressed ZIP backups. Its native full-backup
CLI retains three matching complete archives by default; `--keep 0` means unlimited
retention. Select a private output directory with room for the new archive:

```sh
hermes backup --output /path/to/existing-private-backup-directory --keep 3
```

Retention applies to `hermes-backup-*.zip` in that output directory after a
successful full backup. It does not sweep arbitrary manually named directories.
The pinned updater's default pre-update mode is a quick snapshot; it keeps one
quick snapshot, while full pre-update ZIP retention defaults to five. Review your
actual configuration before changing these settings. Do not disable a required
migration or held rollback backup to save space.

## Compact explicitly selected older standalone snapshots

The main-branch companion helper operates only on files explicitly selected under
an existing `HOME/backups` directory. It does not import Hermes, query SQL rows,
scan your conversation contents, contact a model or restart a service.

Keep your newest immediate restore point and any held rollback files. Select only
completed snapshots that you know are closed and no longer needed at their
original path. Age and absence of sidecars alone cannot prove that no other
process has the file open. For an eligible standalone snapshot, preview first:

```sh
python3 scripts/legion_storage.py --home /path/to/hermes-home old-run/snapshot.db
```

Apply the same selection after reviewing it:

```sh
python3 scripts/legion_storage.py --home /path/to/hermes-home --apply old-run/snapshot.db
```

The helper requires a minimum age of 24 hours by default. It refuses links,
SQLite WAL/SHM/journal sidecars, existing archive outputs, changed input and
insufficient free space. It keeps a 1 GiB free-space reserve while writing and
uses bounded streaming reads; it will not chase a continuously growing file.
Concurrent unrelated writes can still exhaust a filesystem: this reserve is not
an OS disk quota.

It publishes `snapshot.db.gz` and `snapshot.db.gz.metadata.json`, verifies the
decompressed SHA-256, syncs the outputs, and only then unlinks the unchanged
selected source. Metadata includes original size, mode, owner IDs and modification
time. Reports contain metadata, not database rows. Keep both outputs private:
compression is not encryption or anonymization.

If interrupted after publication, both the original and a valid archive may
remain. The next attempt refuses existing outputs. Inspect that state rather
than overwriting or repeating the operation blindly. This helper does not
automatically delete old backups, run on a timer or change native retention.

## Verify a compacted snapshot without restoring it live

This command verifies an archive by streaming its bytes without loading the whole
database into memory or writing a restored database:

```sh
python3 - /path/to/private-backup/snapshot.db.gz <<'PY'
import gzip, hashlib, json, pathlib, sys
archive = pathlib.Path(sys.argv[1])
metadata = json.loads(pathlib.Path(str(archive) + ".metadata.json").read_text())
digest = hashlib.sha256()
size = 0
with gzip.open(archive, "rb") as stream:
    for chunk in iter(lambda: stream.read(1024 * 1024), b""):
        size += len(chunk)
        digest.update(chunk)
assert size == metadata["source_bytes"] and digest.hexdigest() == metadata["sha256"]
print("Verified exact backup bytes; no live database changed")
PY
```

These gzip files are standalone snapshot archives, not native `hermes import`
ZIP bundles. Restore into a new private location first, verify the metadata, and
use the owning application's supported recovery procedure. Never overwrite a
live database or rewind notification receipts to roll back a source-only patch.

## Temporary files and resumable work

Prefer bounded disposable caches and preserve a free-space margin before large
downloads or builds. Use a durable project/worktree location for work that must
resume after days. Age alone does not prove that a scratch tree is abandoned;
an active process can keep using files without updating their modification time.
Inspect process ownership and worktree state before removing a workspace.
Do not run a broad scratch/cache deletion merely because a dashboard reports
disk pressure. Reports, raw backup files and private cleanup plans do not belong
in this public repository.
