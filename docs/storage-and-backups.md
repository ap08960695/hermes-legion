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

### Backup-root boundary (v0.8.52)

Snapshot compaction now rejects a symlink at `HOME/backups` before resolving it.
Previously, resolving that entry first hid the link from later checks and allowed
preview and apply to select files outside the chosen home. Links to another
directory inside the home and dangling links are also refused. An explicitly
selected home alias still resolves normally; its `backups` entry must be physical.
Existing descendant-link, sidecar, identity and exclusive-output checks remain.

API and CLI regressions check refusal without changing target bytes or inventory,
including multiple selections. Physical nested backups still compact and restore
exactly. On ARM64 macOS, a synthetic database created by native Hermes is refused
through a linked root, then compacted through its physical root and reopened in a
fresh native process after exact-byte decompression. No owner database is used.
This closes the demonstrated pre-existing-link escape; pathname checks do not
establish protection against concurrent directory/link substitution.

## Age out disposable data on a schedule

Worker scratch trees, maintenance backups, side builds and evidence reports grow
without bound unless something retires them. One measured fleet held 83 GB in its
Hermes home, of which 34 GB was aged scratch, superseded backups and loose reports.
`scripts/legion_retention.py` previews (default) or applies a conservative policy:

```sh
python3 scripts/legion_retention.py --home "$HERMES_HOME"            # preview
python3 scripts/legion_retention.py --home "$HERMES_HOME" --apply    # perform
```

| Data | Default rule |
| --- | --- |
| `profiles/*/cache/scratch/*` | removed when no file inside changed for 7 days |
| `profiles/*/attachments`, `profiles/*/lcm-large-outputs` | files older than 14 days |
| `backups/*` | older than 7 days, but the newest 3 always stay |
| `side-work/*` | removed when idle for 7 days |
| `state-snapshots`, `profiles/*/state-snapshots` | newest 3 stay |
| `reports/*` directories | idle for 3 days: packed into `<dir>.tar.gz` and verified |

Every age and count is an option. Live databases, sessions, skills, memories,
configs and credentials are never selected. Anything a process of the same user
holds (working directory, executable, open file or mapping) is kept; on systems
without `/proc` the helper asks `lsof`, and if neither works it keeps everything.
Add `--protect PATH` for held rollback points or open-card workspaces. Run it
from a daily timer (systemd user timer or launchd) after reviewing one preview.
A timer that someone stopped during an incident stays stopped: include
"restart the retention timer" in your incident close-out.

## Retention safeguards (v0.8.2)

A protected descendant now preserves its containing directory. Before applying each
planned action, the helper observes process-held paths again and compares a complete
metadata fingerprint with the preview. Changed, unreadable, symlinked, special-file,
`.keep` and Git-marked trees remain in place. Nonfinite retention ages are refused.

Partial Linux process visibility is unknown, so all candidates stay. On macOS, lsof
warnings/errors, missing stable process IDs, and escaped filenames also retain all
candidates. The fallback compares process inventories before and after lsof. These
are conservative point-in-time checks, not a lock against arbitrary future writers.
A skipped cleanup is not reclaimed space; investigate the visibility gap instead of
replacing the guard with an empty process list. Explicit `--protect` paths remain
necessary for durable workspaces and held rollback points that no process has open.

Report packing now uses an exclusive temporary file, compares every archived file's
SHA-256 and the full inventory with the source, and reads through the gzip checksum
trailer. It syncs the archive and its directory, publishes without overwriting an
existing archive, and keeps an unchanged-source check before removal. Source changes,
archive corruption or new process holders preserve the original. The pack admission
check reserves the uncompressed source size plus 1 GiB. Each encoded write also
flushes pending output and checks that observed free space covers that write plus
1 GiB. Allocation and concurrent writers can still consume space after observation;
these checks are not a filesystem quota. An interruption after publication can leave both copies: inspect
and reconcile them explicitly instead of overwriting the archive.

The companion helper was installed with matching bytes on Linux and macOS. It does
not change the 909-path upstream source kit or Desktop packages. The host-specific
Linux scheduled wrapper was also changed to use these guards for its removal/packing
paths and to stop when either process or open-card protection cannot be read. It no
longer traverses unrelated project worktrees. That private wrapper is not a portable
installer supplied by this repository.

## Retention that can actually run (v0.8.35)

The v0.8.2 guard treated every same-user process it could not inspect as partial
visibility. A user systemd manager, `(sd-pam)`, `gpg-agent` and an SSH or SFTP
session are marked non-dumpable by the kernel, so their `/proc` links are closed to
their own user. On this Linux host the daily purge therefore kept everything and
exited 3 on every run: Hermes home reached 43 GB. Those named session daemons are now
skipped; any other closed process still makes observation unknown.

Three further gaps are closed:

- One entry that cannot be removed (for example files a `docker run` created as root
  inside scratch) no longer aborts the rest of `--apply`. It prints `failed` and the
  exit status is 1.
- A tree containing another user's files is kept at planning time with that reason,
  instead of failing during removal.
- Links inside a tree such as `node_modules/.bin` no longer pin the whole tree; their
  targets are fingerprinted and never followed. A link at the candidate root is still
  kept.

Measured on Linux: 9.2 GB of idle root-owned build copies in worker scratch were
removed once with elevated rights. The daily `hermes-purge` timer, stopped when the
owner shut Hermes down on 2026-11-08, was restarted, because it uses no model or
network. To avoid new root-owned scratch, run containers with
`--user "$(id -u):$(id -g)"` or the Docker backend's `docker_run_as_host_user`.

## Retention on macOS and with periodic helpers (v0.8.36)

The macOS lsof path had the same failure: the GlobalProtect agent `PanGPS` is not
visible to the user's lsof, so every run kept everything. Retention last applied on
the Mac on 2026-11-02, and its launchd job was no longer loaded. `ps` now reports
each process name. A stable process that lsof omits is ignored only when its name is
on the same closed-daemon list. On Linux, a periodic `ping` (non-dumpable because of
file capabilities) intermittently made the daily purge keep everything; it is on the
list too.

Measured: the Mac preview went from `remove=0 keep=61` to 58 backup removals and 3
lossless report packs; `~/.hermes` went from 11 GB to 8.6 GB, and the launchd job is
loaded again. Linux and Mac run byte-identical helpers.

## Report validation failures (v0.8.49)

One rejected report no longer aborts later entries in `--apply`. The per-entry
boundary now handles the verifier's `ValueError`, truncated-stream `EOFError`,
tar errors and DEFLATE errors alongside existing filesystem errors. It prints a
`failed` diagnostic, counts the failure, continues independent entries, and still
returns exit status 1. Unexpected exception types are not caught.

Archive validation is unchanged. Unsupported report links and mismatched or
malformed archives remain refusals. Before publication, a rejected report keeps
its source and link targets, the temporary archive is removed, and no destination
archive is published. A failure after successful publication can still leave both
copies; inspect that state before any later attempt. Process visibility, protected
paths, ownership, age and unchanged-source checks remain in force.

Offline regressions run the real archive writer and verifier in synthetic homes.
They cover a linked report, changed archive payload, missing gzip trailer, invalid
tar header, invalid DEFLATE, and invalid appended gzip member. Each checks the
failed report's preservation and a later valid report's exact archived payload.
Process observations are controlled fixtures; these checks do not establish
production cleanup, reclaimed bytes or timer activation. Stopped timers stay off.

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

## Relocate inactive maintenance artifacts instead of losing evidence

Put new build, test, audit and release staging directories on a filesystem with
adequate free space. A different directory on the same filesystem does not free
the original volume. Check the actual mount/device identity and leave enough room
for the copy and verification, including concurrent writes.

For an explicitly selected inactive directory, preserve file bytes, sparse files,
hard links, symlinks, permissions, ownership and relevant extended metadata. Refuse
unsupported special files and review relative links that escape the selected
root: moving their parent can change their meaning. Check current cwd, executable,
open descriptors, mappings and process arguments against the exact paths; an old
modification time alone does not prove inactivity.

Copy into a new private destination, compare all regular-file SHA-256 values and
metadata, and flush destination data before retiring the originals. At a fresh
idle boundary, replace the original location with a link using an appropriate
atomic cutover where supported. Verify reads and the actual environment/tool
entrypoints through the old path, including a meaningful offline native check.
Preserve the original copy until cutover and ownership checks pass; if anything
changed or still uses it, retain it and resolve that condition first.

Keep relocation receipts and machine paths private. Record selected bytes and
filesystem free space separately: concurrent cleanup/writers can affect the
observed free-space delta. Do not migrate a live database, active environment,
credential store or model merely because it is large.

After release acceptance, explicitly inventoried fixture databases, extracted
archives, temporary public clones and superseded generated logs can often be
recreated. Confirm no process uses them, retain compact final results and required
rollback evidence, then retire only those selected disposable paths. Neither this
guide nor a successful release authorizes a blanket age sweep of user data.

## Verified maintenance retirement (v0.8.26)

A later explicitly selected cleanup retired duplicate exports/readbacks and completed test snapshot copies on Linux and Mac. It retained canonical archives and byte-verified compressed snapshot evidence, reducing selected allocation by 240.2 MiB net. See [the measured scope and process-observation safeguards](native-maintenance-continuation.md#retired-maintenance-copies). This was an operator-selected maintenance action; scheduled cleanup rules and permissions remain unchanged.


## Revalidate snapshot paths during compaction (v0.8.62)

The companion snapshot compactor already refuses linked backup roots and paths at
admission. It now repeats that rule using `lstat` on the unresolved file path and
parents before creating restoration metadata, publishing final outputs and removing
the original. The separate root refusal before resolution remains; an explicitly
selected home alias still resolves to its supported physical backup location.

Previously a parent could be moved outside the selected home and replaced with a
symlink after admission. The child file retained its identity, so the compactor
could remove the relocated original and report success. Its verified gzip survived;
this was an unwanted original removal, not proof of irrecoverable data loss.

Detected changes now refuse through the existing error path. Before publication,
no final archive/metadata is published. If publication already happened, the exact
original and verified archive/restoration metadata remain. Owned temporary files
are cleaned; unrelated/live files remain. Existing age, ownership, hard-link,
SQLite-header/sidecar, free-space, digest, identity, fsync and no-overwrite gates
remain. No automatic selection/deletion, SQL, model call or timer change is added.

Fifteen existing storage tests pass baseline. One new test exercises six subcases:
root/inner-parent relocation during compression, metadata writing and after
publication. All six fail before repair on Python 3.12.10 and Hermes' selected Mac
Python 3.14.9. After repair all 16 storage tests pass on both interpreters, including
actual SQLite creation, compression/readback, metadata hashes, supported home aliases
and CLI preflight/refusal. These are overlapping test selections, not 32 distinct
cases. No owner backup or live Hermes service is used.

Repeated path checks are not an atomic directory transaction: check-to-use races
remain. Keep selected snapshots closed and backup directories stable during apply.
This release detects the tested linked-parent windows; it does not claim arbitrary
concurrent namespace mutation is safe. Upstream source patch/manifest/test selection
remain byte-identical; this change belongs to the companion maintenance helper.


## Bind CLI selection to one physical home (v0.8.63)

The snapshot CLI resolves `--home` once, before inspecting any selection, and
uses that physical home for all preflight and per-file plan/apply calls. Supported
home aliases still work. Changing the alias during an invocation no longer
redirects later work to a different home whose snapshots were not inspected.

Previously, retargeting the explicit alias after preflight or between files could
make plan report another home's sizes, or make apply compact that home's snapshots.
The gzip archives survived, but the CLI mutated a different selection. Existing
backup-root/parent link refusal and every per-file validation remain; unavailable
homes still produce the controlled `REFUSED` error before mutation.

Sixteen existing storage tests pass baseline. A new multi-selection test has four
plan/apply × after-preflight/between-files subcases. Real symlink retargets fail
before repair on Python 3.12.10 and Hermes' selected Mac Python 3.14.9; all 18 tests
pass after repair on each. Assertions verify initial-home sizes, exact planned
originals or gzip/metadata readback, unchanged other-home/live/unrelated bytes and
owned-temp cleanup. Missing/dangling-home CLI controls also preserve files.

This binds one CLI invocation to a path, not an immutable directory identity.
Keep the physical home, its ancestors and backup namespace stable; existing
check-to-use races remain. No batch rollback, automatic selection, SQL, provider,
timer or retention-policy behavior is added. No production backup is exercised,
and the unchanged upstream source kit needs no new export or adoption target.


## Report activity after publication (v0.8.68)

Report packing already checked process activity before publishing its verified
archive. A report opened during the following directory sync could still have
its original pathname removed: its bytes and source stamp had not changed.
The shared packer now calls the same optional activity guard after publication
and directory sync, before the final source stamp and removal. Busy or unknown
observations refuse removal and retain both source and verified archive. The
existing apply failure report/exit 1 and later-entry processing remain.

The final source stamp stays after the potentially slow observation. A source
changed during an observation that returns idle is retained alongside the archive
of its earlier bytes. Preview/admission, retention ages, process-visibility rules,
protected paths, archive format, verification, reserve, exclusive publication and
temporary cleanup remain. Direct callers without an activity callback retain that
existing contract; this does not create a new observer or automatic cleanup job.

Original Mac behavior is reproduced with a real read-only descriptor opened only
after archive publication and successful directory fsync: the pathname disappears
and descriptor link count becomes zero, while the verified archive remains.
There is no irreversible-data-loss claim. New held/unknown cases fail at source
preservation on the original, as does a second-observer mutation control. The
fixed cases check exact archive bytes, source/FD inode and device, positive link
count, retained content, observable refusal/exit 1, later valid report removal and
archive, unchanged unrelated data and no task temp leaks. Observation is injected
at the existing boundary for synthetic fixture paths; it does not prove OS-wide
visibility or an operational production cleanup.

Retention selection: 28 tests run, 26 pass/two Linux-only skips on Python 3.12.10 and
Hermes' PM-selected Python 3.14.9, overlapping counts. Both interpreters reproduce
all three original preservation failures first. Full companion: 131 run, 129 pass/
two Linux skips. Native Python runs stdlib companion tests from a temporary cwd
with private HOME/HERMES_HOME/TMPDIR and -I/-B/-S, without importing or launching
Hermes services. No source/dependency clone or native application full-suite claim.

Activity checks remain non-atomic. Activation after the last check can still race
with deletion; atomic concurrency needs shared writer/retention ownership. This
release neither clears process-observation refusals nor changes owner controls,
ESTOP/pauses or stopped timers. No production data was purged or saving attributed.


## Encoded archive reserve (v0.8.70)

A source-size estimate cannot account for gzip/tar headers and trailers or later
space pressure. In a disposable Mac fixture, a one-byte report creates a 231-byte
archive after the original one-time admission accepts modeled free space of
1 GiB plus one byte. This demonstrates an admission gap, not actual disk pressure.

The shared packer now passes encoded output through a private write-only sink.
Before each write it flushes pending output, observes the containing volume, and
requires free space of at least 1 GiB plus the incoming encoded byte count. Equality
is accepted. Insufficient or unavailable space raises through the existing failure
path, retaining the source and removing the temporary archive. Gzip finalization
and trailer writes remain inside that cleanup scope; later eligible reports proceed.
The initial source-size admission, archive verification/checksum, source/activity
checks, exclusive publication and fsync ordering remain in place.

Real tar/gzip/file tests meter actual raw writes beneath buffering. They cover
encoded overhead, later unknown observations, trailer denial, write failure,
lossless ample-space readback, later-report progress, unchanged unrelated bytes
and temporary cleanup. A direct sink check covers exact admission, next-byte
refusal, flush-before-observation and unchanged flush/observation/write errors.
The original produces three source-preservation failures on each of Python 3.12.10
and Hermes' PM-selected 3.14.9. Fixed retention selection: 30 run, 28 pass/two
Linux skips on each interpreter; these counts overlap. Native Python runs only
stdlib companion tests from a temporary cwd with private HOME/HERMES_HOME/TMPDIR
and -I/-B/-S; no Hermes app, provider or service is launched.

This remains best-effort admission. Filesystem allocation granularity and other
writers can change actual space after observation; a hard limit requires a quota.
Extra flushes and volume observations add unmeasured packing cost. No production
cleanup, disk saving, whole-Hermes test or global disk-full prevention is claimed.
Owner data, ESTOP/pauses and stopped timers remain untouched.


## Web full-text write admission (v0.8.71)

Web extraction writes two kinds of optional text under the profile's web cache:
provider/format-specific reuse payloads and paging copies for truncated responses.
Previously neither checked volume space before the exclusive writer removed a
previous file. Actual isolated Mac probes replace both copies and the index with
zero volume observations under modeled full/unavailable space. This demonstrates
missing admission, not physical disk pressure or actual data loss.

One web-specific helper now checks the destination parent before either full-text
write. It requires observed free space minus the final UTF-8 byte count to remain
at least 1 GiB; equality is accepted. The paging check follows its existing character
cap and counts the appended truncation suffix. Each optional copy checks separately.
Low space raises through the existing optional-write handling; an unavailable volume
observation follows that same path. Prior payload/paging files remain, a fully refused
batch leaves the index exact, and only successful mixed-batch writes get new metadata.

The current provider result is still returned. If paging persistence is refused,
the footer reports that full text could not be stored and gives no saved path.
An expired prior entry remains expired, so a later request can fetch again under
the same TTL; a retained valid entry can still hit. No fallback, retry, route,
profile, policy/safety check, character cap, cache key or freshness change is added.
The shared generic spill writer's symlink-safe exclusive overwrite and remote-backend
readability remain; no owner installation or production cache was changed.

Thirteen cases join the existing storage-pressure file. Original code: eight
behavioral failures, thirteen passes including the eight prior cases. Four ASCII/Thai
budget rows across both writers, final capped text/suffix, mixed low/unknown/success writes,
and repeated registered extraction calls cover real files and index bytes. The
registered fixed-provider case keeps an unrelated hit and old copies, returns
fresh head/tail content, exercises normal safety/policy call sites and traps
fallback/provider switches. Both low and unknown observations are covered. All
124 cases across eight native cache/truncation/spill files pass, including final
exported reapplication on native Mac Python 3.14.9 (8.8 s); no tests retried/excluded.

Admission covers these full-text payload writes. Existing JSON-index persistence,
its 500-entry limit, derived-cache admission and retention policy remain unchanged.
It does not bound all cache files or prune old payloads. Allocation, metadata and
other writers can consume space after observation; a hard limit requires a quota.
Extra encoding/volume checks add unmeasured cost. No total-disk guarantee, production
cleanup, disk/RAM/model-usage saving, live provider request or full-Hermes-suite
result is claimed. Owner data, ESTOP/pauses and stopped timers remain intact.
