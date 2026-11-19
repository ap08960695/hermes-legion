# Desktop usability

## Finding work and conversations

The rail offers **New chat**, **History** and **Search**. New chat opens a native blank tab from a chat, retaining any earlier unsent draft. Choose a chat zone first or drag **New chat** to the zone's tab strip to place the new tab there. Ctrl+T (⌘T on Mac) opens a new tab in the focused chat zone.

**Search** first lists recent conversations and commands. Type a phrase and choose **Search in messages** to see the first page of saved-chat matches on the active connection and profile. Use the arrow keys to select a chat and Enter to open it. Matched words are highlighted in message previews. If a chat matched by title or saved session ID, its result names that match and shows the preview as plain text. The results announce how many chats are shown. **Search all saved chats** carries your query into History for additional filters. Sending the same query again reapplies it after an edit in History. Going Back to an unfiltered History page clears the search. Forward reapplies the saved-chat query. Press Escape to return to commands with your query intact, then Escape again to close Search. Holding Backspace clears the query while keeping message search open. Press Backspace again on the empty field to return to commands. While an input method is composing text, Backspace stays with text editing.

When you switch devices, History and message search pause until the switch
settles. Your query stays in place, and results refresh on the active device.
If a saved-chat search fails in History, use **Retry**. Activating the
focused button returns keyboard focus to the search field.

![Search in messages fixture with three saved chats and the second result selected by keyboard.](images/saved-message-search-fixture.webp)

Open **Settings** from the navigation rail in Focus or Workspace. In a compact window it sits beside **History**. The Settings shortcut (⌘, on Mac, Ctrl+, on Windows and Linux) and the command palette also open Settings. Typing in Settings opens its search with the first character already entered. Standalone chat windows have a Settings gear in their titlebar.

In Hub, **Back** returns through the actual file/folder navigation history. At the starting file it returns to Hub and retains the previous search. Folder browsing and supported previews remain inside Hermes. Missing, inaccessible and unsupported files keep their existing preview gates.

A collection search names its scope. No matches are distinct from an empty collection. Use **Clear search and filters** to recover the collection or **Search all Hub** to keep the query and expand its scope. Searching does not grant bot membership or share a private chat file.

## Recovering an earlier message

Open the failed-message notice to read the full text and see any original attachments you need to review or reattach. **Park draft and edit failed message** puts the earlier text in this chat's composer and saves what you were typing. **Return to parked draft** brings back the draft and saves edits to the other message.
If saving the switch fails, a message appears beside that saved draft.
Your current draft stays in the editor and you can retry from the same row.
While previewing sent messages in the composer, press **Down Arrow** until
your current draft returns. Saved-message restore is available again then.

Review the recovered message before you press Send. Sending the original payload uses its original submission ID on a gateway that supports idempotent admission. If you revise the text or replace attachments, confirm **Send as new message**. The earlier message may already have reached the gateway.

When you discard a saved message with the keyboard, focus returns to the recovery summary while other saved messages remain. After the last discard, you can keep typing in the current draft.

When Hermes recovers an unsent draft from a deleted chat, it keeps the original saved copy until it saves the draft in the new chat. If **Undo** cannot save a restored draft back to its original chat, an error appears beside Undo. The draft stays in the editor and you can retry.

When **Restore draft** copies an unassigned draft, focus returns to the composer.
If the copy fails or the chat already has a saved draft, the notice explains
the failure and keeps **Restore draft** available.

![Failed-message recovery fixture before and after parking the current draft.](images/draft-recovery-fixture.webp)

## Checking the configured provider

**Settings → Accounts** shows the selected profile's configured provider and model on the active connection. A current per-account reading includes its timestamp. If the first read fails, Accounts shows a load error. A failed refresh keeps any cached readings visible. A provider without a reading shows that quota is unreported, while a configured local endpoint is labeled separately. Gemini API and AGY subscription reports have separate provider identities. **Refresh** checks supported quota sources and keeps keyboard focus while the request runs. If you switch devices during a refresh, returning to the same device and profile shows **Refreshing** until its request ends. When a quota window passes its reported reset time, the next display update marks that window stale until Refresh supplies a current reading. The reset time stays available by keyboard when a window becomes stale. Other windows remain visible.

The bottom-bar **Account usage** picker offers the default and active profiles.
Switching devices or active profiles returns the picker to **default**.

![Accounts fixture with Gemini API, a separate AGY reading, a NIM reading, and a local model.](images/accounts-provider-fixture.webp)

## Reading Workflow

**Fit graph** fits both dimensions. Large graphs may need small overview text; select a destination to highlight its recorded ancestry and use **Focus selected card** to return that task to readable size. Focusing scrolls after the scaled layout is committed. Bot journeys remain based on recorded runs and dependencies. No animation fabricates progress or dispatches work.

## Choosing and creating bots

Use **New bot** or **New group chat** in the Bots workspace header. In **Manage team**, the roster toolbar has a separate **New section** button. The standalone Bots roster keeps its creation menu.

Cards show the model and provider already reported by the roster. Missing values say **not reported**. These are configured profile values: an existing chat can retain a different model. They do not prove provider readiness or remaining allowance. The display adds no provider or quota probe.

**New bot** defaults to create-only. It creates the profile, refreshes the team and keeps the current page/profile. It does not start a chat or inference. The optional **Start an introduction after creation** control explicitly discloses that the introduction is a real model call under the bot's existing route and quota. Native readiness and confirmation gates still apply. Remote creation retains its own source routing. No paid fallback is added.

## Setting goals and keeping context

The goal editor searches enabled installed skills locally, shows the selected count and retains choices while filtering. Skill references do not enable tools, alter permissions or start a goal. Pressing Enter in skill search does not submit the form. Existing session/revision-bound saving and explicit completion criteria remain authoritative. The Save surface stays outside the form’s scroll area and uses the native opaque dialog background.

Device, profile for new chats and connection state remain visible above the workspace. The compact row preserves readability on a laptop-height window. Native device/profile selectors and draft ownership remain unchanged.

## Reconnecting to Local

Desktop reopens the Local socket after it drops, including during initial
sidebar loading. The reconnect uses a fresh ticket from the canonical gateway
and waits with jittered backoff capped at 15 seconds between attempts. Tabs
and drafts stay open. If the runtime refuses to start because it needs repair,
use **Reconnect gateway** after resolving the reported reason.

## Verification boundaries

Regression tests and real isolated Electron interactions use disposable conversations, files, bot profiles and paused controls. Provider inference is denied and counted. Production source adoption, package preparation, graceful activation and isolated visual acceptance are separate evidence. No remote Screen transport, provider authorization, allowance or production worker execution is certified by these checks.


## Interaction safeguards (v0.6.3)

After a fitted overview, **Zoom out** always makes the graph smaller; controls disable at their manual limits. Fit can still show a larger graph at a smaller overview scale.

Closing a changed Hub document asks whether to **Keep editing** or **Discard changes**. Unchanged forms close directly, and successful saves close without a discard question. Inputs stay disabled during a pending save; a refused save keeps the draft and reports the error without retrying.

**Manage bot access** searches locally by a bot's reported name or canonical identity, shows the selected count and keeps selected members outside the search result. An existing member missing from the reported profile list remains visible with an explicit label. Filtering does not save membership or grant access.

History/Projects and Settings indicate the current destination. The navigation rail scrolls on short windows rather than leaving its lower controls inaccessible.


## Resilient searches and lighter browsing (v0.6.4)

Pasted bot-role and Hub-title queries ignore surrounding whitespace. Changing Hub's All/Pages/Images filters uses the already loaded collection list; entering or leaving Trash still reads the correct server scope. A pending list shows **Loading collection items…** instead of claiming that a collection is empty.

Saved-chat search retires results from another query or profile immediately. A failed full-text request shows a small error with **Retry**, keeps any applicable local matches, and does not reuse the previous full-text hits. There is no new retry timer or polling loop. Retry makes one new debounced search request through the existing native transport.

**Manage bot access** distinguishes a pending profile catalog, a failed read and a successfully loaded empty catalog. Existing selections remain visible and are never relabeled as missing before the catalog is available. Saving stays disabled while that read is pending or failed. Use **Retry** to recover explicitly; no membership write occurs during loading, filtering or retrying.
