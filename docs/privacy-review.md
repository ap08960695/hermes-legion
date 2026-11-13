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

## Read-only history check (v0.8.46)

`python3 scripts/verify_release.py --history` checks neutral author/committer
metadata across all refs and requires a clean checkout after checking the exact
release inventory. Its status command now disables `core.fsmonitor` for that
invocation, matching the checkout verifier's existing fence. A configured
repository helper cannot run through that status check; repository configuration
is left intact. This is a specific fsmonitor fence, not a sandbox for every Git
extension or configuration.

Four disposable-repository regressions cover clean acceptance (including the CLI
from outside this source directory), a real marker-writing fsmonitor hook,
dirty files whose updated hashes pass inventory checks, and non-neutral metadata
on another branch. The hook regression fails before the repair. Exact-tree,
symlink, file-type and patch-digest refusals remain in force.

Local ignored files and operational reports still prevent exact-tree verification.
For package-only verification, copy only Git-tracked public files with their current
working-tree bytes into a fresh temporary directory, then run the verifier there.
This does not check the original directory or its Git history. Do not add ignored
files or local reports to the release manifest to make verification pass. The
documented full-directory and all-history Gitleaks scans remain separate gates
before publication.
