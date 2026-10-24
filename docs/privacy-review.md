# Privacy review

The release boundary is an explicit manifest of public files. Source patch context is public too, including removed lines. A new repository history is used so deleted private files and original author metadata cannot travel with an old checkout.

The public tree contains only reviewed code changes, synthetic tests, English documentation, generic role templates and rewritten skills. No operational report, original persona, private rename map, production log, conversation, memory, database, account file, authentication state, browser data or credential is an export input.

Checks cover the full directory, exact Git commit/tree and all reachable history, metadata and the final archive. Gitleaks runs locally with redacted reports and no allow-comment bypass. A separate private-identifier review covers personal/project names, internal URLs, host paths, real operational IDs and other data that a credential scanner cannot recognize. No private identifier dictionary or finding snippet is distributed.

For a local review with Gitleaks 8.30.1:

```sh
gitleaks dir . --redact=100 --ignore-gitleaks-allow --no-banner
gitleaks git . --log-opts="--all" --redact=100 --ignore-gitleaks-allow --no-banner
python3 scripts/verify_release.py
```

Keep raw finding reports outside this repository. Investigate each finding; do not broadly suppress a rule merely to make a scan green. Synthetic credential-redaction tests construct conspicuously artificial input at runtime and never use a real credential. Scanners are evidence within a review, not a guarantee against every possible undiscovered identifier or secret.
