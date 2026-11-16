# Changelog

What you will notice after applying the source kit and adopting it through the
supported update or Desktop rebuild path. This kit does not install a rebuilt
Hermes.app. Linked notes identify opt-in memory settings and admission guards
that apply after adoption. Each entry states its adoption and verification limits.

## v0.33.5 — Keep list edits when closing Settings

Pressing Escape after editing a comma-separated list now saves it before closing
Settings. Previously that focused draft could disappear. Enter and moving focus
retain their existing behavior; empty entries and trailing commas use the same
parser. Apply the source kit and rebuild Desktop. Lost edits from an older build
are not recovered. Native Local before/after disk and reopen checks pass; the
after cohort required one Reload before the test, so cold startup remains open.
[Checks and limits](docs/release-notes-v0.33.5.md).

## v0.33.4 — Nudge compression ratios precisely

Compression Threshold and Compression Target arrows now move by 0.01, one
percentage point, instead of jumping by 1. For example, increasing 0.50 becomes
0.51. Count and timeout controls keep their existing whole-unit steps. Apply the
source kit and rebuild Desktop. Existing saved values are not rewritten; correct
an earlier mistaken ratio by typing its intended value.

[Checks and limits](docs/release-notes-v0.33.4.md).

## v0.33.3 — Scope Settings config actions

Export and Reset use the profile shown under **Applies to**. The target is kept
for the whole action, even if the selection changes while a read or confirmation
is pending. Reset names that profile before confirmation and reports a refused
save as failure. Apply the source kit and rebuild Desktop.

Native Local before/after exports, a named Reset dialog and Cancel passed;
config bytes remained unchanged. Reset writes and selection races are covered
offline only. [Checks and limits](docs/release-notes-v0.33.3.md).

## v0.33.2 — Keep untouched settings visible after import

Partial config imports preserve untouched fields on screen, including switches
and budgets. Repeating an import no longer requires reopening Settings to see
correct values. A file read superseded by an edit or leaving the view is discarded;
import again to apply it. Apply the source kit and rebuild Desktop.

Native Local first/repeated imports, next field edit, sparse disk readback and
Settings reopen passed. No native writer or backend change.
[Checks and limits](docs/release-notes-v0.33.2.md).

## v0.33.1 — Confirm config imports after saving

Settings says **Config imported** after the current native save succeeds.
Cancelling toolset removal or failing to save no longer reports success.
Non-object JSON is refused before editing. Restore write access and import again
after a save failure. Apply the source kit and rebuild Desktop.

Native Local cancellation, real permission refusal, retry, disk readback and
Settings reopen passed. Partial imports can still temporarily show omitted fields
as empty until reopen; their disk values remain preserved.
[Checks and limits](docs/release-notes-v0.33.1.md).

## v0.33.0 — See parallel bot work

Full Bots cards list recent observed workers with their own titles and progress.
The activity count and Working status share the same eligibility rule; stopping
the newest worker keeps an older active sibling visible. Compact rows keep one
stamp and add a count for multiple observations. Conversation previews stay separate.

Apply the source kit to the gateway and Desktop, restart the updated gateway,
and rebuild Desktop. Native Local before/after Send, Stop A, B heartbeat,
completion and parent delivery passed using controlled loopback replies.
Counts are bounded observations, not a process census.
[Checks and limits](docs/release-notes-v0.33.0.md).

## v0.32.0 — Read and enlarge chat charts

Click a chart to enlarge it with the house pan/zoom viewer. Open **Details** to
read full category and series names, units and unrounded parsed values, including
zero and negatives. Dense axes show fewer labels; every category remains in the
table. Details mounts its table only while open. Close or Escape returns to Chat.

Apply the source kit and rebuild Desktop. The native Local report workflow
covers Markdown table, chart and Mermaid together using controlled loopback
content. Number precision already lost during parsing cannot be recovered.
[Checks and limits](docs/release-notes-v0.32.0.md).

## v0.31.1 — Keep same-goal delegation cards separate

Two delegated calls with the same task name now show their own native child.
Stopping one leaves the other card running until that child completes. A missing
advertised child stays unknown instead of borrowing another child's outcome.
Apply the source kit and rebuild Desktop; older receipts without child IDs keep
their existing matching behavior.

Fresh native Local before/after runs reproduced both cards incorrectly showing
Stopped, then verified A Stopped / B Running and B Done. Only model content and
timing were controlled on loopback. [Checks and limits](docs/release-notes-v0.31.1.md).

## v0.31.0 — Name and reopen Local group chats

Create a Local room with two to six bots, cancel an unwanted draft, and reopen
its saved room from Manage team. The room now has **Rename**: change its name
without creating a replacement room or changing its members. The header and
main-tab caption update after the gateway confirms the name; the unsent message
stays in the composer. A failed write keeps the name draft and Save available.

Same-home native process restart retained the saved name and members; the final
UI updated the header/tab together without losing the unsent message. No model
call was made. This groups the earlier creation/reopen acceptance with the new
naming control. Apply the source kit and rebuild Desktop, including its SDK. Rename appears only
when the owning gateway advertises it. Canonical membership editing remains open.
[Checks, adoption and limits](docs/release-notes-v0.31.0.md).

## v0.30.2 — Show background reports without Reload

After Hermes finishes replying to a background completion, its task summary and
report now appear in the current chat through the existing history refresh.
You can open the result without reloading the app. Ordinary streamed turns keep
their existing read behavior; Stop clears the adoption flag before the next turn.
Apply the source kit and rebuild Desktop.

A fresh same-home native Local Send/delegate/Stop A/complete B flow showed both
outcomes and report before Reload, then one retained report after Reload.
Only model content/timing used a loopback fixture. See
[release notes](docs/release-notes-v0.30.2.md).

## v0.30.1 — Clean saved background reports

Opening a saved delegated report now hides the gateway's internal notice and
lets the existing terminal transcript-path cleanup work. Process logs also close
their wrapper correctly. Task outcomes, partial output and report content stay
available. Apply the source kit and rebuild Desktop.

The same genuine native saved report was checked before and after on an isolated
Local app. Its stored content and outcome metadata stayed exact. The copied
home's resume was refused by its existing profile guard; acceptance covers
reading history. See [release notes](docs/release-notes-v0.30.1.md).

## v0.30.0 — Reopen delegated task outcomes

A saved batch completion can now show which task was interrupted, completed or
failed beside its task name. Expand its compact summary after Reload, read the
existing report, then collapse or reopen it. Outcomes stay available even when
there is no report output. Task names are redacted and bounded for display.

Apply the source kit and rebuild Desktop. Native Local Stop A / complete B,
parent delivery, Reload and reopen passed with controlled loopback replies.
Older notifications keep their previous summary; this does not retrofit old
outcomes or relabel the original parked dispatch cards. Live pre-Reload summary
visibility and report trace cleanup remain open. See
[release notes](docs/release-notes-v0.30.0.md).

## v0.29.5 — Show stopped delegated responses

An interrupted child now shows Response stopped and a neutral stop icon on its
chat card. Partial output remains; real errors and completed work keep their
existing states. Apply the source kit and rebuild Desktop.

Actual native Local Stop A / keep B working, late-reply rejection, B completion
and parent delivery passed with controlled loopback replies. The fix changes
presentation only. Native async history without a child outcome remains parked;
no production saving or external-tool cancellation claim. See
[release notes](docs/release-notes-v0.29.5.md).

## v0.29.4 — Show delegated bot work

Bots shows Working while a native delegated child runs, with its observed
activity separate from the parent conversation preview. Refresh clears the
worker detail after native completion. Both canonical and legacy backend
projections recognize the child's source. Adopt the updated backend; the
existing renderer already supports these fields.

Actual Local UI Send, native delegation, advancing heartbeat, completion and
terminal Refresh passed with deterministic loopback replies. Four new cases
failed before; fourteen native test-body cases pass through a local assertion
runner (pytest unavailable). No production saving is claimed. See
[release notes](docs/release-notes-v0.29.4.md) for scope and limits.

## v0.29.3 — Keep bot model labels readable

Long provider names in Edit profile stay inside their dropdown instead of
overlapping Model. Both arrows remain visible; keyboard focus reveals the full
name. Apply the source kit and rebuild Desktop. The shared picker also serves
bot creation and advanced configuration.

Native Local wide/narrow screenshots, full-name tooltip and menu dismissal pass.
Ten real-Radix picker cases, types, build and scoped lint pass. Model changes
have component proof only this round; no profile was saved or inference run.
Owner-app adoption remains open. See [release notes](docs/release-notes-v0.29.3.md).

## v0.29.2 — Save bot descriptions without a helper

Edit profile uses the existing gateway writer for descriptions, avoiding a
separate Python process on supported backends. Native Local Save/reopen and
file readback preserve Thai/English text and line breaks. Missing or rejected
acknowledgment keeps the draft; CLI fallback is limited to an explicitly missing
method and checks its result. Apply the source kit and rebuild Desktop.

Eleven editor and nineteen SDK cases, types, build and scoped lint pass.
Older-backend fallback has component proof only. No production RAM saving is
claimed. See [release notes](docs/release-notes-v0.29.2.md).

## v0.29.1 — Keep bot edits after a failed save

Edit profile stays open with your draft when a description, appearance or
advanced section fails to save. A failed description write no longer also
announces success. Correct or retry explicitly; previously saved sections are
not rolled back. Existing older-gateway fallback and successful Save remain.

Apply the source kit and rebuild Desktop. Native Local before/after checks
used the same process guard to reject the description write; title-only Save
and reopen also passed. Five component cases, types and build pass. Successful
native description execution and owner-app adoption remain unverified.
See [release notes](docs/release-notes-v0.29.1.md).

## v0.29.0 — Activity on bot cards

- See reported worker activity directly on a bot card, separately from its
  conversation preview: description, tool, step, elapsed time and token totals.
- Received ended or unusable observations hide their activity using the same
  policy as the compact roster. Existing refresh and chat destinations remain.

Apply the source kit and rebuild Desktop. Controlled native SessionDB records
verified display at wide/narrow widths and disappearance after ending a record
and clicking Refresh. Actual worker lifecycle remains unverified. No model call
or new polling is added. See [release notes](docs/release-notes-v0.29.0.md).

## v0.28.1 — Readable status on bot cards

The Bots screen gives each card's status its own row above Open Screen,
Edit profile and Open chat. An inactive status no longer gets squeezed into
four lines beside these buttons. Apply the source kit and rebuild Desktop.
Native Mac before/after screenshots verify the correction; a narrow-window
check and empty-search recovery also passed. Live worker monitoring and
owner-app adoption remain untested. Existing scoped lint findings are unchanged.
See [release notes](docs/release-notes-v0.28.1.md) for checks and limits.

## v0.28.0 — Settings actions keep your place

- Find **Export config**, **Import config** and **Reset to defaults** under a
  named **Actions** button, with consistent wide and narrow layouts.
- Cancel a reset and continue with the keyboard: focus returns to Actions;
  Return opens its menu again.
- Keep an unsent Local draft when opening Settings for the first time after
  startup and returning to Chat.

Apply the source kit and rebuild Desktop to adopt this capability set. Native
Mac acceptance used isolated Local data: first-visit draft preservation,
Export/Import cancellation, and Reset Cancel focus at both window widths.
Completed imports, destructive reset, daily-app adoption and remote-host use
were not exercised. Older differently owned draft keys are not migrated.
See [release notes](docs/release-notes-v0.28.0.md) for checks and limits.

## v0.9.0–v0.27.0 — consolidated capability summary

These nineteen releases are grouped here so related improvements are easier to
find. Their original versions, release notes and commit history remain intact.
Measurements come from separate bounded Mac cases; do not add their percentages
or treat them as a production whole-app result.

### RAM and on-demand processes

- Unused cached stdio MCP servers can stay stopped until their first tool call
  ([v0.10.0](docs/release-notes-v0.10.0.md)). Cached discovery also leaves the MCP
  SDK unloaded until needed ([v0.11.0](docs/release-notes-v0.11.0.md)).
- Reading saved-session metadata avoids loading the turn engine before history
  is opened ([v0.12.0](docs/release-notes-v0.12.0.md)).
- Desktop ticket helpers start on demand, share a configurable limit and retire
  when idle ([v0.15.0](docs/release-notes-v0.15.0.md)). Low or unknown available
  memory delays new helpers within the existing deadline
  ([v0.16.0](docs/release-notes-v0.16.0.md)).
- Profiles can opt into idle stdio MCP retirement; explicit per-server policy
  still wins, so stateful servers can stay running
  ([v0.17.0](docs/release-notes-v0.17.0.md)). The on-demand gateway preset groups
  existing startup controls ([v0.18.0](docs/release-notes-v0.18.0.md)).
- Optional dashboard warmup can wait for the first local request
  ([v0.20.0](docs/release-notes-v0.20.0.md)). Disabled gateway warmup also defers
  host-toolchain checks until first use
  ([v0.27.0](docs/release-notes-v0.27.0.md)). Idle cache cleanup runs one job at a
  time per runner ([v0.21.0](docs/release-notes-v0.21.0.md)).

Less startup work can mean a slower first request or another cold start after
retirement. This is partial scale-to-zero: the gateway and some loaded modules
remain resident. v0.20.0 measured 213.734 → 183.781 MiB median idle RSS in its
canonical gateway case, with peak RSS essentially unchanged. v0.27.0 established
no RAM saving and measured higher peak RSS and a slower first turn. See each
release's evidence and scope before choosing settings.

### Desktop remote connections and helper limits

- Compatible SSH profiles share a transport within an app process. Checks queue
  one command per host, failure cooldown is bounded, and POSIX session loss
  stops and reaps guarded helper work
  ([v0.9.0](docs/release-notes-v0.9.0.md),
  [ownership and platform limits](docs/desktop-ssh-resources.md)). The known
  helper startup chain fits within four Python roles; this is not an OS-wide
  process quota or a guarantee across different app owners/authentication.
- Desktop checks wait when execution-host memory is low or unknown
  ([v0.13.0](docs/release-notes-v0.13.0.md)). Runtime lookups share ticket-helper
  admission ([v0.22.0](docs/release-notes-v0.22.0.md)). Ticket backlogs are bounded
  ([v0.24.0](docs/release-notes-v0.24.0.md)), as are fresh backend checks
  ([v0.25.0](docs/release-notes-v0.25.0.md)). Queuing can take longer or report busy.
- Cold Local startup leaves saved remote connections on demand rather than
  opening them for passive roster or Bot Relay polling
  ([v0.26.0](docs/release-notes-v0.26.0.md)). Explicit remote work can still connect;
  switching to Local does not disconnect remote work already opened.

Local mocks and isolated Mac acceptance do not establish real ai-host behavior,
Windows helper cleanup or adoption by the owner's installed app. No first
ai connection is authorized by these release notes. Config/Bots/Chat visual
walkthroughs remain unfinished because Computer Use capture was unavailable.

### Gateway diagnostics

`hermes gateway memory` reads one native local snapshot, including current RSS
on macOS when available ([v0.19.0](docs/release-notes-v0.19.0.md),
[usage and exit codes](docs/runtime-memory-diagnostics.md)). Unknown values stay
unknown. It adds no background polling or model call and does not trim memory.
Current RSS is not peak RSS or a memory-saving result.

### Update and cache safety

Repeated identical Desktop source-update checks share one running operation
([v0.14.0](docs/release-notes-v0.14.0.md)). Source checks also wait for sufficient
observed memory within their active deadline
([v0.23.0](docs/release-notes-v0.23.0.md)). These changes do not automatically
restart busy work or enable stopped timers.

Earlier disk, backup, cache/recall and doctor improvements from v0.8.46–v0.8.73
are grouped in the [v0.9.0 consolidated notes](docs/release-notes-v0.9.0.md).
v0.8.74–v0.8.76 additionally bound retained vision payload, prepare request-cache
admission before locking and recover overflowing web-cache TTL configuration;
see [vision cache behavior](docs/vision-cache-routes.md) and
[search cache behavior](docs/search-cache-memory.md). Disk reserve checks are
best effort, not a quota; no production reclaimed-disk or model-usage saving is
established by this summary.

Future releases receive their own entry under the
[release policy](CONTRIBUTING.md#release-policy). Historical release tags identify
their original commits; later documentation updates do not replace those release
payloads.
