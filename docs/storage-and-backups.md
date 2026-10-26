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

The companion helper operates only on files explicitly selected under
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
From v0.3.2, the source patch preserves active paths, Git worktrees, project or
environment markers and explicit `.keep` markers during automatic retention. Put
a `.keep` file in an artifact directory that must survive; a marker in the scratch
root preserves that whole root. Store long-term work outside disposable scratch.

The existing 24-hour idle threshold remains for eligible disposable entries. The
Gateway checks them hourly under each served profile. Existing opportunistic boot
checks share this policy. Process visibility failures or incomplete workspace
scans retain data, and automatic cleanup never signals a process. Command paths are resolved
through symlinks and relative to the owning process cwd, including option values.
Closed stale
artifacts can be removed when their ownership is observable. Fresh directories
skip recursive scans. This policy is intentionally conservative: retained workspaces
can still consume substantial space and need an operator's separate disposition.
Do not interpret a skipped sweep as successful reclamation.
Do not run a broad scratch/cache deletion merely because a dashboard reports
disk pressure. Reports, raw backup files and private cleanup plans do not belong
in this public repository.


## Derived-cache reserve on current main

The post-v0.3.2 derived document/search cache writer leaves at least 1 GiB free on
the cache filesystem after accounting for the full encoded incoming payload.
Low or unreadable free-space measurements leave a successful conversion usable
without publishing another disposable payload. Existing useful hits survive
temporary-file or rename failures, and replacing a key does not count its old
version twice against cache quotas. Quotas and expiry remain enforced under the
existing cross-process index lock after successful publication.

This is an admission check for optional derived cache files. Other writers may
consume space concurrently; monitor the filesystem and preserve durable data
instead of treating this reserve as a whole-disk guarantee. It does not install
MemoryHigh or MemoryMax limits or stop running workers.


## Generated Desktop package rollbacks

A packaged Desktop contains large runtime binaries. Do not retain a complete package for every small UI revision indefinitely. After checking package hashes and current process ownership, keep the currently running package, its verified recovery snapshot and the immediately previous verified recovery package. Retire older generated package directories only from an explicitly inventoried build-products scope while holding the native Desktop build lock.

Count unique file inodes and remaining hard links before reporting reclaimed storage. A hardlinked copy's apparent size is not independently reclaimable space. Confirm that no process executes, maps or holds files in the deletion set, and verify the kept package hashes afterward. Filesystem free-space deltas can include unrelated concurrent writes.

This is an operational retention boundary, not a new automatic deletion daemon. It does not authorize deleting conversation databases, project data, source-file rollback evidence, held incident/recovery snapshots, models, active test environments or unknown old cache directories. Retain small source backups, manifests and acceptance receipts separately. An unactivated staged package is not evidence that a running Desktop has loaded a patch.
