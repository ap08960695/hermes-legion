# Desktop feature parity

The new presentation must retain native Hermes workflows. This release repairs twelve gaps found by comparing the original navigation and registered features with the Focus/Workspace interface. It adds no scheduler or model-routing policy.

| Workflow | Entry and behavior |
|---|---|
| Saved conversations | **History**, or **All features → Sessions**, opens a full central manager in both Focus and Workspace. Full-text search can find conversations outside the loaded recent page. |
| Conversation actions | Use a row's context menu or action button for native rename, pin, archive, delete, branch, export, unread and project actions. Native confirmations and availability rules apply. |
| Filters and ordering | Open **Filters** in the session section header. Native grouping, ordering, archived view, status/profile/project filters and pins remain available. |
| Projects and worktrees | **History → Projects**, or **All features → Projects**, exposes the native project/folder manager, project menus and repository/worktree controls. Plain project palette selection reveals this manager; the new-chat modifier retains its original behavior. |
| New bots | **Bots → New bot**, or the **New Bot** palette command, opens the existing creation form. Creation defaults to create-only: it keeps the current page/profile and does not open a chat or call a model. The explicit introduction option uses the existing route/readiness gates. Opening or cancelling the form does not infer. |
| Groups and sections | **Bots → New group chat** opens member selection. **Manage team** exposes native section creation, rename, membership and group actions. **Show bot cards** returns to the card view. |
| Bot Screen | A bot card offers its native Screen entry when its source is available. Existing transport, capability, installation and owner checks still decide whether Screen can connect. |
| Device and profile | A permanent row above the workspace shows the device name, selected profile name and live connection state in both Focus and Workspace. No dialog is needed to read the values. Open the native device selector or named profile menu only when changing context. Existing conversations retain their owner; changing the new-chat context does not migrate a running conversation. |
| Goals, loops and heartbeats | **Catch up** shows the native control sections together. **Configure goal** retains the revision-bound editor. Existing native actions, turn limits, pause/wait state and confirmation rules remain authoritative. Creating a loop/heartbeat still uses the supported native commands. |
| Plugin discovery | **All features** includes loaded pane-only plugins and a clearly labeled status entry for status-only plugins. Listing metadata does not render a second plugin instance, enable a disabled monitor or execute its actions. |
| Cache analytics | **All features → Usage** shows cached input tokens and their share of reported input, using the existing analytics response. Missing or inconsistent evidence is not displayed as zero or 100 percent. Provider cache reads do not establish cross-bot sharing or financial savings. |
| Friendly destinations | Plugin routes use their title or a readable fallback instead of a raw `/bots` route string. |

The permanent legacy session/bot column stays closed. The central history/project manager deliberately reuses native components and actions; it is a destination, not a second sidebar layered over chat. Only one project-dialog owner renders on these manager pages. A hidden legacy bot pane cannot consume a form request intended for the visible Bots workspace.

## Additional review fixes

A full UI interaction exposed a separate older-chat issue: a server-only search hit could be pinned but disappeared when search was cleared because the loaded list had no row or profile for it. Pinning now adopts that exact metadata before the existing pin synchronization runs. Fresh loaded metadata and same-ID rows belonging to another profile are preserved. Search mapping retains the profile returned by the native endpoint.

The review also preserves the original chat target for delayed goal submissions, distinguishes an unavailable control snapshot from an empty one, avoids route-mirror entries in the feature catalog, and distinguishes plugin status links from page links.

## Verification boundaries

Tests use disposable profiles, conversations, paused controls, files and synthetic runtime plugins. No production bot, account or private plugin is exported as a fixture. The native Electron application, preload, renderer and backend are used in isolation. Provider inference is denied and counted. Private installed plugins are inspected for registration compatibility without enabling a monitor or executing its private behavior.

Opening/cancelling creation forms does not certify provider authorization or an introductory model response. Screen entry coverage does not certify a remote screen transport. Synthetic cache counters test display arithmetic; they are not a production cache measurement. Source installation, native package construction, graceful activation and interactive UI evidence are recorded separately. See the [verification record](verification.md).

## Always-visible context (v0.6.1)

The context row replaces the rail button and information dialog. It remains visible while reading chat, opening History/Projects, using Bots/Hub or switching presentation modes. Device, selected profile and Connected/Connecting/Not connected are separate labeled values. Profile display names are presentation only; selection still uses the canonical native profile identity and existing action. The active choice is checked in the menu.

The row reads existing stores and adds no network refresh, timer, model call or provider route. Opening the menu and choosing the already-selected profile leave the current chat alone. A pending device/profile switch disables conflicting profile choices. Explicit changes continue through native routing, confirmation and draft handling. Unknown device identity is labeled as unreported.


## Follow-up interaction repairs (v0.6.3)

**New chat** calls the existing native new-tab handler, including when an unsent draft is already open. Previous drafts remain in their own tabs; plugin action permissions are unchanged. History/Projects and Settings have their own current-page indication even when a bot pane was previously focused. The rail scrolls at short window heights so lower actions stay reachable.

Hub protects dirty page edits from accidental Escape, close or cancel; discarding is explicit. Fields cannot change while their single save is pending. Membership search uses reported bot titles and canonical names, preserves choices outside the filter, and retains existing members absent from a partial profile list. Native revision and access checks still govern saving.
