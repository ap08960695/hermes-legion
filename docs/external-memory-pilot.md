# Review an optional external-memory pilot

Hermes already has native memory and saved-conversation search. Start by checking
whether those capabilities answer the missing-recall case. The bounded
[title-recall repair](session-recall.md) needs no new service or tool schema.

An operator may separately evaluate
[ai-memory v3.2.5](https://github.com/akitaonrails/ai-memory/releases/tag/v3.2.5).
This companion does not install, enable, connect or export that service. The
following is a review recipe for a deliberately isolated pilot, not a claim of
native Hermes adapter compatibility or measured production savings.

## Establish the data boundary before capture

Use a fresh private data directory for one explicitly selected project and a
small set of consenting profiles. Keep the directory, its token files, database,
raw captures, wiki, wiki Git history and diagnostic logs outside the public
checkout. Use a distinct project boundary; do not point the pilot at a directory
containing unrelated projects or an entire user's history.

The reviewed upstream version enables first-session history backfill and managed
launch auto-wiring by default. Disable both before the first hook or managed
launch. The relevant definitions and environment overrides are in the pinned
[configuration source](https://github.com/akitaonrails/ai-memory/blob/v3.2.5/crates/ai-memory-cli/src/config.rs).
The following **new isolated configuration fragment** is TOML, not Hermes YAML:

```toml
bind = "127.0.0.1:49374"
backfill_on_start = false
run_autowire = false
capture_assistant = false
consolidate_on_session_end = false
llm_fallbacks = []

[auth]
bearer_token_file = "auth-tokens/pilot"

[maintenance]
embedding_backfill_interval_secs = 0
```

The port above is upstream's standard loopback example, not an instruction to
replace an existing listener. Choose a free address if another service owns it.
Create a private, nonempty token file through the upstream supported setup before
serving; do not put the token in this fragment, a command line or Git. Consult the
versioned [installation guide](https://github.com/akitaonrails/ai-memory/blob/v3.2.5/docs/install.md)
for config/data-dir and token-file resolution.

This fragment does not remove providers from a previously configured home.
Upstream defaults have no LLM provider, but inherited environment variables and
existing configuration can override them. Inspect the resolved settings in the
isolated environment: no LLM/remote-embedding provider, credential or fallback
should be configured for a zero-inference evaluation. Disabling session-end
consolidation alone does not prevent other LLM work when a provider is present.

Avoid broad `setup`, managed-launch auto-wiring, bulk history import,
`install-skills` and MCP registration during the initial comparison. Each can
change capture, prompts or tools beyond the selected pilot. Existing native
quotas, permissions, project isolation and no-paid-fallback rules remain in force.

## Check hooks and authentication without changing bots

Read the exact hooks used by the selected profiles. Review event payloads, cwd
and project identity, token handling, bounded timeouts and failure behavior.
Approve only the required commands through the existing native hook mechanism;
do not turn on global hook auto-accept. A failed optional memory hook should not
duplicate or restart the original task. Verify this with synthetic input and an
isolated failing endpoint before changing live hooks.

Client and server must both resolve the intended backfill-off setting. A client
environment override is not proof of the server's effective configuration. Turning
backfill off also does not undo captures that already happened. If unrelated
content entered a store, use the upstream supported remediation and verify every
affected data/history location privately before enabling capture again.

Capture-only hooks do not prove that a bot can search the external store. Adding
MCP or skills is a separate adoption change: it can alter tool schemas, prompt
prefixes and cache cohorts, and requires its own acceptance and comparison.

## Diagnose a local embedding configuration separately

For a deliberately unauthenticated loopback embedding endpoint, a copied dummy
API key can select the wrong authentication path or trigger an HTTP credential
guard. Verify the endpoint's intended authentication and the installed plugin's
configuration contract. Use a blank key only when that specific local endpoint
is intentionally unauthenticated; never remove a real service credential or
weaken remote HTTP/TLS checks to make a probe pass.

A successful vector or nonzero dense score proves neither useful recall nor
cross-bot prompt-cache sharing. First confirm that relevant memories exist and
that permitted profiles can retrieve them. Reuse an existing approved embedding
service; do not start, stop, reload or resize protected models for this recipe.

## Decide from matched work

Record a baseline before capture changes. Compare complete, similar work periods
with the same role/account/model, tool schemas, quotas and task mix. Track successful
recall, repeated reads, calls per completed task, input/cache-write/cache-read
tokens, start/response latency and memory/storage growth. Include failures and
coverage, and keep raw evidence private. A short idle probe, a sparse store or an
offline parser check cannot establish a usage reduction.

Keep the pilot small until a full comparison supports expansion. Roll back only
the pilot's exact hook/config changes at an idle boundary, preserving later owner
edits and captured evidence under an explicit private retention policy. Do not
restore a whole live database to undo a source or hook change.
