# Contributing

Use English documentation, role instructions and commit messages. Preserve legitimate multilingual product behavior and use synthetic fixtures.

Keep roles separate from provider lanes. Changes must retain ownership, dependency, rights, review, approval and quota fences. Never add paid fallback, model-backed polling or automatic retries to hide an ambiguous result.

For a code change, identify the pinned upstream base, add a meaningful offline behavior regression, update the patch and manifest coherently, and document any compatibility boundary. Do not mutate the historical cumulative patch without updating every affected hash and running the apply/reverse-apply checks.

Run `python3 -m unittest discover -s tests -v` and `python3 scripts/verify_release.py`. Also scan the entire working tree and Git history using the documented Gitleaks commands. Publication review includes every packaged file, patch context, Git metadata and release archive; a clean grep alone is insufficient.

Do not commit local scan reports containing paths or matches, production evidence, account inventories, databases, memory or chat exports. Synthetic public verification summaries must state exactly what was tested, without claiming a full Hermes suite or live token savings.

## Release policy

- PATCH (`x.y.Z`): fixes behavior that was broken for users.
- MINOR (`x.Y.0`): delivers one user-visible capability set, grouping related
  rounds of work. Accumulate internal guards and partial work on the working
  branch until the set is complete and proven live; a single internal guard
  does not justify a minor release.
- MAJOR (`1.0.0`): requires the main owner goal and explicit owner approval through
  the lead. Acceptance includes working Local and ai backends, zero remote links
  on cold Local startup, one compatible SSH master per host, at most four remote
  helpers, no orphan helpers, bounded reconnect, measured RAM targets,
  config/Bots/Chat walkthroughs, bot monitoring and live tables/charts/Mermaid.
  This policy does not authorize connecting to ai or bypassing controls.

Each new release needs a plain-language entry in [CHANGELOG.md](CHANGELOG.md)
describing what users will notice, adoption steps, evidence and tradeoffs; keep
`RELEASE-MANIFEST.json` coherent. Annotate its `vX.Y.Z` Git tag on the exact release
commit with neutral project metadata. Never move an existing release tag.

The v0.9.0–v0.27.0 versions remain historical. Their backfilled annotated tags
point to the original release commits, with current annotation dates. Pure
documentation/bookkeeping changes get no version bump; refresh the checkout's
inventory without replacing an existing tagged release artifact under the same
version. Future runtime releases resume the policy above.
