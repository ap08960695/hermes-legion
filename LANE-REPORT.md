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
