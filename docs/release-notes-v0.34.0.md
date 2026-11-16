# Hermes Legion v0.34.0 — Bot Monitor

## What you will notice

Open **Bots → Monitor** to see your bots and their current worker observations in
one table. You can scan what is working, its task and step, elapsed time, recorded
tokens/model, recorded cost when available, and the latest recorded issue without
opening every bot card. Search, status filters and column sorting stay local.
Manage team and the existing cards remain available.

**Recent reports** opens that bot's saved task outcomes, completion times and
bounded result/error excerpts. Completed, Error, Recorded stalled, Stopped and
Unknown keep distinct labels. Recorded issues searches the displayed latest
Error/Recorded stalled context; it does not search every historical report body.
**Open chat** uses the selected bot's canonical Bot Chat, including when invoked
from a worker row. It does not open an arbitrary recent side chat.

This batch also keeps model labels readable, makes rows reachable in short
windows, and returns focus to the report trigger after closing its dialog.
Keyboard navigation reaches hidden columns. If roster inventory fails, the last
scoped snapshot keeps its source labels and history, hides current workers, and
disables Open until a successful explicit refresh restores authoritative data.

Missing data remains unavailable. Worker and stored Bot Chat usage stay separate;
recorded amounts have partial coverage and are not added into an invoice. A
configured or recorded model label does not prove the model currently running.
Current worker eligibility remains the bounded existing policy: at most the
newest 20 observations per bot and a 150-second liveness window. This is an
observation dashboard, not an OS process census or a new worker controller.

## Adoption

This is a source kit, not a rebuilt Hermes.app. Apply the consolidated
[stable source kit](stable-full-kit.md) to its pinned upstream base and rebuild
Desktop through the supported [installation path](macos-install-update.md).
Existing adoption/rollback protections still apply. This round does not install
into the owner's daily app or connect to another machine. First ai connection
and owner-app adoption remain separate lead/owner actions.

The bundled agent-desktop source slices are unfinished, explicitly opt-in work
for the next capability set. The default remains `cua`. Status/capture/ref-input
code does not establish runtime input readiness or supported deployment on every
platform. See its [design and native boundary](design-agent-desktop.md#native-capture-and-mutation-runtime-boundary).
No new dependency, default-provider switch or automatic connection is introduced.

## Evidence for this capability set

Separate matching runs establish separate capabilities; no combined passing run
is invented. Responses, timing and usage in these controlled Local fixtures are
simulated. Delegation, file reading, SessionDB/ledger/delivery and canonical query/
navigation use the actual native paths.

| Capability | Native evidence | Boundary |
|---|---|---|
| Failed-read recovery and source authority | Round179 retains the failed snapshot, disables Open and recovers after explicit Refresh. | Inventory failure is simulated; not a real transport outage. |
| Working progress, elapsed and Completed report | Round180 follows the real file-read child, elapsed 17s → 32s, automatic removal and exact nonempty report. | Loopback model replies and usage are fixtures. |
| Error outcome/report | Round181 shows native worker settlement and the exact Error report. | HTTP400 is supplied by the loopback fixture. |
| Narrow Stop journey and controls | Round185 passes 480×620 worker search/Working filtering, elapsed sort, keyboard reach, authenticated interrupt, removal and exact Stopped report, including final ACK. | Wheel/trackpad panning is not proven. |
| Existing canonical chat reopening | Round187 matches explicit named Open to the pre-Open ID/profile/transcript; both DB inventories/messages/API counters stay unchanged, with no navigation model call. | Existing before navigation, not tested across app relaunch. |
| Recorded-issue search/context | Round186's guarded AX/pixels and independent DB readback agree on default-only Error membership, query retention, excerpt and reset. | Later report-click admission fails its phase budget; INVALID/STOP/noACK remains. This is corroborating observation, not accepted completion. |

The actual component/query/SDK/preload and DB regressions cover rendering,
usage/source selection, canonical identity, recorded outcomes, stale retention,
filter/sort and keyboard focus. The browser geometry check fails before the narrow
wrapper correction and passes after it. These results and patch-section
apply/hash/reverse checks were recorded when their source changed; unchanged
broad suites and all 1120 targets are not rerun for release bookkeeping.
[Detailed results and limits](verification.md), [capability audit](design-bot-monitor.md#release-gate-audit--2026-11-17).

Native live Recorded stalled/Unknown presentation, Error-only report-dialog
filter selection, wheel/trackpad pan, relaunch persistence and spoken screen-reader
behavior remain untested. Production billing, pricing accuracy, paid-provider
behavior, whole-service RAM savings, owner adoption and ai operation are not
established. Earlier failed trials remain failed; source tests do not turn those
failures into native passes.

## Before/after captures

Owner-local images remain private under `../evidence/`, outside the public source
inventory. This handoff does not upload or publish them.

- Narrow before-fix / working / Stopped: `bot-monitor-narrow-acceptance-20261117/`
  (`before-fix-181.jpg`, `active.jpg`, `stopped-report.jpg`). Before-fix belongs to
  a separate failed generation; it is not a controlled performance comparison.
- Working / advancing / Completed: `bot-monitor-worker-completion-20261117/`.
- Failed snapshot / recovered: `bot-monitor-query-authority-20261117/`.
- Existing chat before Open / reopened: `bot-monitor-canonical-reopen-20261117/`.
- Qualified recorded Error search: `bot-monitor-recorded-issue-search-20261117/`.

## Source release handoff

The source inventory is prepared as v0.34.0. This round does not commit, tag,
push, publish an archive or adopt the app. The driver re-runs companion unit,
tracked-copy release and full-directory/all-history secret gates, commits the
reviewed source inventory, and creates annotated `v0.34.0` on that exact commit.
Only the lead publishes through the normal sync. Do not move an existing tag.
The known absent `v0.33.7` and `v0.33.8` tags correspond to commits `065f6e6` and
`1b3ab5e`; the driver can backfill them separately without rewriting history.
Other historical tags are outside this review.
