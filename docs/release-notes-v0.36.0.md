# Hermes Legion v0.36.0 — Owner Inbox and Work Cards

## What you will notice

- **Waiting for owner** collects pending bot questions and approvals across
  profiles on the active connection. Answer in the inbox or open the bot's chat.
  Local questions with a linked Work card can open that card in its profile.
  If a reply fails, the draft stays available for retry.
- **Work** flags recorded path overlaps so teams can coordinate before editing
  the same place. Track Work shows delivery evidence and lets you choose an
  earlier revision round and open a text diff when both recorded files are still
  available. Reviewed results show the recorded usage when the gateway has it.
- **Accounts** shows the provider for the active profile. Chat can recover
  eligible unsent text after a failed send or reopen. Saved-message search
  opens the saved conversation in its original connection and profile.
- **Local** offers reconnect in place when available. Desktop also explains
  SSH states such as queued, disconnected or waiting for capacity when that
  information is available. On macOS, SSH ownership checks preserve
  spaces in installer paths.
- **Mermaid** renders offline in chat, Work cards and Hub Markdown previews.
  Keyboard users can reach diagram and chart controls, and diagrams offer
  source viewing and copying. [Mermaid guide](mermaid-diagrams.md)

## Desktop fixes

Keyboard focus stays visible and returns to the relevant control after common
actions in Inbox, Work, Bots and previews. Narrow windows keep form fields and
dialog actions reachable. Bots uses visible labels for profile and model fields,
and New group chat announces when a bot search has no matches. Delayed replies,
profile switches and failed refreshes received targeted fixes across Inbox,
chat, Accounts and Work.

## Mac evidence

These captures use synthetic Local data. The Inbox fixture exercised two
profiles, a failed answer and a retry. The Work fixture exercised earlier
revision rounds and requested a text diff from recorded fixture handoffs.

![Waiting for owner shows questions from Tester and Writer, with answer choices and a link to each chat.](images/v036-owner-inbox.webp)

![Track Work shows a selected revision round, the two handoff runs, and the button to open answer.txt's text diff.](images/v036-work-revisions.webp)

The full local macOS Desktop test run on integration commit `d1e4800`
discovered 1,836 test files. It recorded 16,795 passing tests, 37 skips
and zero failures.

The declared macOS Python selection covered all 1,547 files. The full
sweep reported 24 test failures across seven files with harness issues.
All seven files passed on corrected reruns, giving 15,021 passing tests
and 228 skips across the combined results.

Loopback OpenSSH checks cover connection reuse, helper admission and cleanup,
and reconnect backoff. The owner's installed Hermes.app, the real ai backend,
and tablet-to-Desktop answer recovery are outside this release's verification.
[Desktop SSH evidence](desktop-ssh-resources.md)

## Adopt the source kit

Use the [consolidated stable source kit](stable-full-kit.md) with the pinned
upstream revision. Follow the [Mac guide](macos-install-update.md) to rebuild
Desktop in a separate trial with its own home and a Local-only connection.
Keep the existing installation available while you try the new build.
[Installation and rollback](installation-and-rollback.md)
