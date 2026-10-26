# Desktop usability

## Finding work and conversations

The rail offers **New chat**, **History** and **Search**. New chat opens a native blank tab, retaining any earlier unsent draft. Search first lists recent conversations and commands; choose **Search all saved chats** to carry the exact query into the native History full-text search. This is not limited to the newest conversation page. Native profile, archive, pin and project rules still apply.

In Hub, **Back** returns through the actual file/folder navigation history. At the starting file it returns to Hub and retains the previous search. Folder browsing and supported previews remain inside Hermes. Missing, inaccessible and unsupported files keep their existing preview gates.

A collection search names its scope. No matches are distinct from an empty collection. Use **Clear search and filters** to recover the collection or **Search all Hub** to keep the query and expand its scope. Searching does not grant bot membership or share a private chat file.

## Reading Workflow

**Fit graph** fits both dimensions. Large graphs may need small overview text; select a destination to highlight its recorded ancestry and use **Focus selected card** to return that task to readable size. Focusing scrolls after the scaled layout is committed. Bot journeys remain based on recorded runs and dependencies. No animation fabricates progress or dispatches work.

## Choosing and creating bots

Cards show the model and provider already reported by the roster. Missing values say **not reported**. These are configured profile values: an existing chat can retain a different model. They do not prove provider readiness or remaining allowance. The display adds no provider or quota probe.

**New bot** defaults to create-only. It creates the profile, refreshes the team and keeps the current page/profile. It does not start a chat or inference. The optional **Start an introduction after creation** control explicitly discloses that the introduction is a real model call under the bot's existing route and quota. Native readiness and confirmation gates still apply. Remote creation retains its own source routing. No paid fallback is added.

## Setting goals and keeping context

The goal editor searches enabled installed skills locally, shows the selected count and retains choices while filtering. Skill references do not enable tools, alter permissions or start a goal. Pressing Enter in skill search does not submit the form. Existing session/revision-bound saving and explicit completion criteria remain authoritative. The Save surface stays outside the form’s scroll area and uses the native opaque dialog background.

Device, profile for new chats and connection state remain visible above the workspace. The compact row preserves readability on a laptop-height window. Native device/profile selectors and draft ownership remain unchanged.

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
