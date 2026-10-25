# Focus and Workspace

This release implements the approved interface in the native Hermes Desktop renderer. It does not embed an HTML mockup or replace the existing chat engine.

## Find the work without a crowded sidebar

Focus has four icon-led destinations: **Chat**, **Work**, **Bots**, and **Library**. Short captions remain visible, and accessible names describe each control. **All features** opens a searchable catalog grouped by work, team capabilities, and system settings. Registered plugin pages are included when they become available.

Chat returns through the existing session-opening path. It does not create another conversation. Bots opens the installed native roster, whose canonical conversation rules are unchanged; without that pane it opens Profiles. Work opens an installed Kanban page, or the existing worker-runs page when no board is registered. Navigation never enables a plugin or dispatches a worker implicitly.

Use **Wide** to switch from Focus to Workspace, and **Focus** to return. The existing native Simple/Advanced layout scopes preserve their separate arrangements and underlying display preferences. A one-time presentation migration selects Focus; it does not rewrite model, account, quota or bot configuration. Existing keyboard shortcuts and advanced tools remain available.

On a narrow viewport, the primary destinations move to a bottom bar. Motion uses short, finite transitions and a selection accent, with reduced-motion support. There is no added frame loop or background animation scheduler.

## Configure an existing session's goal

Open **All features → Goal**, or **Catch up → Configure goal**. The form combines:

1. The objective and an explicit completion criterion.
2. Decision authority within the already approved scope.
3. References to enabled skills installed for the session's actual owner.
4. Optional additional outcome, constraint, and stop/ask conditions.

The form is pinned to the original session and state revision. Incoming state cannot overwrite an unsaved draft. Escape keeps that draft; Cancel discards it. Ctrl/Cmd+Enter is contained inside the form and cannot send an unrelated chat draft.

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

See [verification](verification.md#native-focus-and-workspace-v040) for the offline evidence and limits. No live model call, allowance probe or paid fallback was used for this change. Offline render tests do not establish production token savings or certify every operating system.
