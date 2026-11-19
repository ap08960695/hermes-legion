# Owner inbox lane

## Changes

- Added **Waiting for owner** to the Bots header with a live count and a keyboard-accessible inbox for the selected connection.
- Shows pending clarification and approval prompts across served profiles, with bot, age and available card or goal context. Answers and one-time approval decisions use the exact owning request. **Open chat** opens the full conversation.
- Canonical and standalone gateways stream content-free invalidations. Worker and compute-host responses wait for acknowledgement. Reconnects take a fresh snapshot.

## Verification

- Focused gateway suite passed 99 tests. The multiplex fixture uses two profiles with the same session ID and confirms that only the intended waiter receives the answer. Other cases cover scoped tickets, approval settlement and a lost compute-host acknowledgement.
- Desktop Vitest passed 40 tests across the inbox, workspace, Monitor and canonical socket routing. Renderer TypeScript and 137 source-kit tests passed.
- The browser fixture verified keyboard open, radio selection, submit, Escape, focus restoration and the accessibility tree. Both 8-second idle samples made zero inbox RPCs after initialization. The inbox sample ended 0.85 MB higher in retained JS heap and used 15 ms of renderer task time versus 19 ms for baseline.
- Stable-full apply, installed-target verification and reverse-apply passed on the pinned checkout. The release inventory and Gitleaks directory and history scans passed.
- Evidence is in `docs/images/owner-inbox-two-questions.webp`, `docs/images/owner-inbox-one-remaining.webp` and `verification/owner-inbox-idle.json`.

## Limits and merge

- Board-only gates remain in Work's **Needs owner** lane. Credential prompts and extended approvals use their native chat controls.
- Fixture evidence covers the two backend paths and renderer behavior. Native Mac, live SSH and whole-app idle RSS remain unmeasured.
- Merge the stable-full targets and regenerate patch hashes and the release inventory against the final combined tree. This lane leaves the release inventory unreleased.
