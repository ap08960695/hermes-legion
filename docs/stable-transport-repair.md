# Stable transport repair

This optional source patch targets upstream Hermes **v0.22.5**, commit
`bf0203a794a07aac3ff764972ab9087baa4e4f4e`. It is independent of the older cumulative
Legion patch. Choose one compatible unit; do not apply this over `0001-legion.patch`.
The exact seven source/test paths and before/after hashes are in
[its manifest](../patches/stable-transport/manifest.json).

## Behavior repaired

- A native `key_cmd` can supply a rotating bearer after client construction. At the
  final HTTP request boundary, the Codex client now derives workspace and residency
  headers from that request's bearer. It replaces stale derived values, works for
  sync and async clients, and keeps existing compression. The hook neither calls
  the token supplier again nor logs the bearer. Identity headers are not added to
  other origins; optional compression is not required for identity handling.
- Native managed workers now keep the resolved frozen provider runtime, including
  `api_mode`, endpoint and credentials. A named Responses or Anthropic route no
  longer silently becomes Chat Completions. Session request overrides keep their
  precedence, and a fallback credential is never attached to the primary route.

This does not configure accounts, select models, increase quota, enable a fallback,
resume a fleet or install THINK/ACTION orchestration. Existing native ownership,
approval, independent-review and publication rules continue to apply.

## Apply and verify

Start in the Legion repository root. Choose a **new, nonexistent** checkout path
outside your running installation. Cloning reads public source; verification does
not import Hermes, read your auth stores or request a model.

```sh
set -eu
export LEGION_ROOT="$(pwd)"
export HERMES_CHECKOUT="/absolute/path/to/new-hermes-stable-checkout"
legion_manifest="$LEGION_ROOT/patches/stable-transport/manifest.json"
legion_patch="$LEGION_ROOT/patches/stable-transport/0001-stable-transport.patch"
legion_base_commit="$(python3 -c 'import json; print(json.load(open("patches/stable-transport/manifest.json"))["upstream_commit"])')"
test ! -e "$HERMES_CHECKOUT"
git clone --no-checkout https://github.com/NousResearch/hermes-agent.git "$HERMES_CHECKOUT"
git -C "$HERMES_CHECKOUT" checkout --detach "$legion_base_commit"
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase base --manifest "$legion_manifest"
git -C "$HERMES_CHECKOUT" apply --check "$legion_patch"
git -C "$HERMES_CHECKOUT" apply "$legion_patch"
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase installed --manifest "$legion_manifest"
```

Do not force past a revision, hash or unrelated-change refusal. Use upstream's
managed test environment and native `scripts/run_tests.sh`, with an isolated Hermes
home, to run the two new test files and the neighboring account-header, compression,
command-token, client-reuse and managed-worker routing/construct/frozen-policy cases.
The companion kit does not select or install dependencies for you.

Live adoption is separate: wait for active sessions, workers and child processes to
be safely idle, preserve affected bytes and ownership, and use native update custody
and the normal application lifecycle. There is no automatic restart or account copy
in this kit. A tested synthetic loop is not permission to resume held project work.

## Reverse on the isolated checkout

```sh
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase installed --manifest "$legion_manifest"
git -C "$HERMES_CHECKOUT" apply --reverse --check "$legion_patch"
git -C "$HERMES_CHECKOUT" apply --reverse "$legion_patch"
python3 "$LEGION_ROOT/scripts/verify_checkout.py" "$HERMES_CHECKOUT" --phase base --manifest "$legion_manifest"
```

Stop if the source changed after installation. Keep only the affected source rollback
while it is needed; do not duplicate a whole live home, restore a database or rewind
notification receipts. [Verification evidence and limits](verification.md#stable-transport-repair-v0648)
are separate from production usage or performance claims.
