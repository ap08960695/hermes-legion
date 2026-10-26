# Focus and Workspace

This release implements the approved interface in the native Hermes Desktop renderer. It does not embed an HTML mockup or replace the existing chat engine.

## Find the work without a crowded sidebar

Focus has four icon-led destinations: **Chat**, **Work**, **Bots**, and **Hub**. Hub replaces the former Library and Spaces doors. Short captions remain visible, and accessible names describe each control. **All features** opens a searchable catalog grouped by work, team capabilities, and system settings. Registered plugin pages are included when they become available.

Chat returns through the existing session-opening path. It does not create another conversation. Bots opens a full native workspace with role/source/status cards, search and group filters, using the existing canonical conversation rules; legacy installations fall back to the native roster or Profiles. Work opens an installed Kanban page, or the existing worker-runs page when no board is registered. Navigation never enables a plugin or dispatches a worker implicitly.

Use **Wide** to switch from Focus to Workspace, and **Focus** to return. The existing native Simple/Advanced layout scopes preserve their separate arrangements and underlying display preferences. A one-time presentation migration selects Focus; it does not rewrite model, account, quota or bot configuration. Existing keyboard shortcuts and advanced tools remain available.

On a narrow viewport, the primary destinations move to a bottom bar. Motion uses short, finite transitions and a selection accent, with reduced-motion support. There is no added frame loop or background animation scheduler.

## Current work and task history

Work uses the actual native Kanban board, card controls and detail dialog. Focus closes the old permanent Sessions/Bots side pane so the canvas has its own space. **All features → Sessions** opens the existing session picker. The old top-left sidebar trigger is absent in Focus, and its positional/keyboard actions cannot restore the legacy Sessions/Bots column; Wide retains the original advanced layout. Click and touch selection work immediately, including when the pointer has not moved. The Sessions pane keeps its New session entry and real project/session tree instead of repeating the global navigation. The rail follows the focused destination: leaving the Bots pane for Work, Hub or Chat clears its highlight even if the roster remains mounted.

**Current work** excludes completed and archived columns. **History** shows terminal columns and initially mounts at most 50 cards per column; **Show more** adds another 50. Search still filters the complete board data already fetched from the native API, including older history beyond the visible batch. This bounds rendering, not backend fetching. It is not server pagination or an archive/delete operation. Unknown statuses remain in Current work rather than disappearing.

Status summaries show native Running, Ready and Blocked counts separately. Review and owner decisions are not relabeled as running work. Changing views clears selections, and empty history has its own explanation and a return-to-current-work button. Native ownership, status-transition, drag/drop and active-worker gates remain authoritative.

**Models** opens main model configuration; **Accounts** opens provider accounts; **Usage** opens the native Usage section. The empty Chat screen has a compact localized heading inside Focus; the standalone intro remains unchanged outside that integration. No account, model or language is changed by these presentation choices.

## Follow real work in Workflow

Choose **Work → Workflow** for a graph of native card dependencies. Arrows point from prerequisites to dependent work. Parallel branches and joins come from recorded links, never from guessed status order, similar names or timestamps. Disconnected cards stay disconnected. Click a node to select it; **Open card** uses the existing native detail dialog.

The selected node's inspector shows **Recorded bot runs** directly inside Workflow: profile, attempt/run number, native outcome and recorded start time. Repeated attempts remain separate. Current assignment is shown separately and never counted as historical execution. A claim/run record does not prove a model call or successful output. Missing history remains explicitly unknown.

Select a destination to highlight its recorded upstream path and dim unrelated branches. The inspector lists upstream cards you can select; **Show all paths** clears the highlight. Moving arrows and a node accent apply only to native `running` tasks with a worker PID and a heartbeat no older than 120 seconds. Ready, scheduled, stale, owner-waiting and unknown work is not animated as running. Reduced-motion preferences disable the effects.

Use zoom, **Fit graph**, scrolling and keyboard focus. The initial graph is bounded to 80 cards and 240 visible edges; completed prerequisites can be included without mounting unrelated history. Cycles and omitted/external links produce a notice. The backend exports at most 5,000 links, only between returned cards. Existing board, tenant, archive and connection boundaries remain controlling.

Workflow opts into links on the existing board read only while selected. It reuses native event invalidation and the existing fallback cadence. Selecting a node reuses the native task-detail query; it adds no model call, worker dispatch, automatic retry or separate polling loop. Reading the graph never changes task status.

## Open files inside Hub

Click a file in **Hub** to open the internal viewer. Text and source files use the native read-only editor; HTML has a sanitized, opaque sandbox with scripts and external resource loading disabled. Images, PDFs, audio and supported video use embedded viewers. Image cards also have an explicit **Open** button.

**Browse containing folder** lists files and subfolders inside the same dialog. Selecting a file opens it within Hermes; **Copy path** copies its resolved location. Existing native file and size guards still apply. A bounded metadata preflight disables unsupported, missing, unreadable and oversized files before opening the viewer. Explicit Refresh rechecks the visible batch; there is no new polling loop. A successful click reads once before opening the dialog, so stale entries do not create a known-failing preview. Files that disappear after the check remain unavailable in the app. This view does not edit, rename, delete or execute files. Office/archive conversion is not included. Ordinary web links retain their existing link behavior.

A file read is pinned to its originating connection, profile and session. Relative paths resolve against that session's working directory. Switching the active gateway/profile does not silently redirect an already captured file to another machine. Closing a viewer discards late responses. Previewing a file does not ask a model to read or describe it.

## Shared collections and richer answers

[Hub collections](shared-spaces.md) provides local pages, explicitly imported file copies, selected read-only bot membership, and recoverable removal. It does not import old conversations or dispatch bots automatically. [Rich answers](rich-answers.md) documents native Markdown tables, Mermaid and opt-in cards with supplied images and sources.

## Configure an existing session's goal

Open **All features → Goal**, or **Catch up → Configure goal**. The form combines:

1. The objective and an explicit completion criterion.
2. Decision authority within the already approved scope.
3. References to enabled skills installed for the session's actual owner.
4. Optional additional outcome, constraint, and stop/ask conditions.

The form is pinned to the original session and state revision. Incoming state cannot overwrite an unsaved draft. Escape keeps that draft when reopening the editor for the same chat; Cancel discards it. Opening the editor for a different chat starts from that chat's own goal state, without carrying over the first chat's draft. Ctrl/Cmd+Enter is contained inside the form and cannot send an unrelated chat draft.

Saving uses a narrow native configuration intent. It does **not** submit a prompt, draft a contract with a model, start a worker, or retry a failed task. Work starts through the normal next-message flow. A busy session or stale revision refuses the save and leaves the draft intact.

A new goal uses the profile's existing `goals.max_turns`. Editing preserves its turn counter, limit, pause, gates and wait barrier. Invalid configured limits are refused rather than replaced with a larger allowance. A completed goal must be cleared through the existing controls before another is configured.

Skill references do not enable tools, install skills or grant new permissions. Decision text does not waive owner, review, rights, spending or publication gates. Existing quotas and the no-paid-fallback policy remain controlling.

## Catch up from evidence already received

Catch up shows native goal and session state, provider notices, explicit process/session/time wait barriers, and links to unread finished conversations, worker runs and the output library. It reads existing stores only while open; it adds no polling, inference or replay mechanism.

A finished reply is distinguished from a completed goal. An unavailable snapshot remains **Not reported**, rather than being described as absent or successful. Wait targets and reported timestamps are shown without invented completion estimates.

The output library retains its original file and source-chat links. A file's presence is not evidence of review or permission to publish. The new presentation does not manufacture draft/reviewed/ready labels when a native workflow has not supplied that binding.

## Installation and verification

Apply the complete pinned patch using [installation and rollback](installation-and-rollback.md), then use the normal native Desktop build and idle lifecycle. Updating source alone does not reload an already-open renderer. Finish or preserve active work, quit normally, and launch the rebuilt package; avoid replacing assets underneath a running Desktop.

The implementation uses existing native components, icons, locale infrastructure, layout stores and owned-session transport. English copy is complete. Thai strings can be used with a registered Thai language pack; this patch does not force a global language change.

See [verification](verification.md#native-work-surface-correction-v044) for the offline evidence and limits. No live model call, allowance probe or paid fallback was used for this change. Offline render tests do not establish production token savings or certify every operating system.
