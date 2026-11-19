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

---

# Work Cards lane

Branch `lane/work-cards` targets the Mac repository. Base `bae663f`.
Changes apply to stable-full on upstream `bf0203a794a07aac3ff764972ab9087baa4e4f4e`.

- **ACTION scope.** Preview compares open cards on the same checkout. Proceed
  confirms the inspected scope, Sequence adds native dependencies, and Re-scope
  leaves the ACTION uncreated. The tool also returns conflicts before insertion.
- **Revisions.** Track work pairs the handoffs around the latest request for
  changes. It shows run-labelled checks and reads hash-matched text on demand,
  including retained attachments after scratch cleanup.
- **Usage.** Accepted deliveries show THINK, ACTION, revisions, REVIEW and judge
  usage with native run evidence. Exact bindings and deduplication govern partial
  totals. Missing amounts stay unavailable.

## Verification

- 96 focused Python tests and 26 Kanban renderer tests.
- Renderer type check and affected lint, 137 source-kit tests, release inventory,
  and stable-full forward and reverse application with manifest verification.
- Checksum-pinned Gitleaks directory and all-ref history scans before commits.
- Browser fixtures with synthetic REST payloads and GPU disabled.
  [Scope](docs/images/work-card-scope-fixture.webp) ·
  [Revision](docs/images/work-card-revision-fixture.webp) ·
  [Usage](docs/images/work-card-usage-fixture.webp)

## Open risks and merge notes

- Scope comparison samples up to 128 open cards. An unresolved checkout or
  missing scope can leave coverage incomplete. Older artifact text may be gone.
- Usage is partial, with bounded fallback diagnostics and no pricing lookup.
  Native Desktop installation and provider-backed acceptance remain unverified.
- Preserve concurrent stable-full sections when merging and refresh both
  manifests. The lane has no version bump, tag or migration.
