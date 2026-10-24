# Contributing

Use English documentation, role instructions and commit messages. Preserve legitimate multilingual product behavior and use synthetic fixtures.

Keep roles separate from provider lanes. Changes must retain ownership, dependency, rights, review, approval and quota fences. Never add paid fallback, model-backed polling or automatic retries to hide an ambiguous result.

For a code change, identify the pinned upstream base, add a meaningful offline behavior regression, update the patch and manifest coherently, and document any compatibility boundary. Do not mutate the historical cumulative patch without updating every affected hash and running the apply/reverse-apply checks.

Run `python3 -m unittest discover -s tests -v` and `python3 scripts/verify_release.py`. Also scan the entire working tree and Git history using the documented Gitleaks commands. Publication review includes every packaged file, patch context, Git metadata and release archive; a clean grep alone is insufficient.

Do not commit local scan reports containing paths or matches, production evidence, account inventories, databases, memory or chat exports. Synthetic public verification summaries must state exactly what was tested, without claiming a full Hermes suite or live token savings.
