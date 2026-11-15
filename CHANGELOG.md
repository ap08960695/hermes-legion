# Changelog

What you will notice after applying the source kit and adopting it through the
supported update or Desktop rebuild path. This kit does not install a rebuilt
Hermes.app. Linked notes identify opt-in memory settings and admission guards
that apply after adoption. Each entry states its adoption and verification limits.

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
