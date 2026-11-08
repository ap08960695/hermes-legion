# Compact card-worker schemas

Use this recipe for a newly created, stopped Kanban dispatcher worker using the
CLI toolset path. It needs only Kanban and session recall. Keep a Captain, an existing profile, and every held session/job
unchanged. A worker that needs terminal, files, browser or other capabilities
needs its appropriate role configuration instead.

Read [the fragment](compact-kanban-worker.config.fragment.json). It selects the
same two native toolsets as the bounded card experiment and uses the existing
`tools.tool_search.defer` setting. This list **replaces** the native default; do
not install only the six additional Kanban names. The other entries keep the
explicit deferral choices in that tested configuration. Names for unavailable
tools do not enable them. Review the list when changing the pinned Hermes kit.
Native tool-search mode must be `auto` (the default when unset) or `on`.
An explicit `off` disables deferral; review that choice before using the recipe.
The fragment deliberately does not override the mode.

Keep these eight tools direct: `kanban_show`, `kanban_complete`, `kanban_block`,
`kanban_request_review`, `kanban_request_changes`, `kanban_heartbeat`,
`kanban_comment`, and `session_search`. Defer `kanban_list`, `kanban_create`,
`kanban_link`, `kanban_attach`, `kanban_attach_url`, and `kanban_attachments`.
Native `kanban_schedule` is already deferred in the tested baseline: it is
registered outside the native core list, so the automatic non-core eligibility
rule still applies even when it is absent from this replacement list. Deferred
tools remain reachable through native search/describe/call and keep their
normal permission checks. Discovery can add model turns when they are needed.

## Configure and read back

1. Confirm the owner authorized creating the dedicated worker and selecting its
   model/account through native setup. Keep existing quotas, approvals, goals
   and routes. The fragment supplies no authentication or model choice.
2. Create a fresh profile with native `hermes profile create NAME --no-alias
   --description "Small Kanban and session-recall cards only"`. Stop if the name
   already exists; do not clone or reuse an older profile.
3. After approved native model/account selection, record a private baseline with
   `hermes --profile NAME config get --json`; keep credential values out of
   reports. Read the fragment and apply exactly three native keys: `toolsets`,
   `platform_toolsets.cli`, and `tools.tool_search.defer`. For each, use
   `hermes --profile NAME config set KEY JSON_VALUE`, passing that key's value
   from the fragment as JSON. Do not replace a whole existing config file.
4. For each key, run `hermes --profile NAME config get KEY --json` and compare
   the parsed value with the fragment. Capture the resolved configuration again
   and compare it with the baseline, excluding only those three leaf values and
   empty container keys introduced by them.
   Confirm model/account choices, quotas, goals and unrelated settings did not
   change; the fragment never supplies or copies an authentication file. A saved fragment is not a
   running or authenticated worker.
5. Start no Gateway, card or model merely to prove installation. A later native
   test needs its own available owner-authorized card scope. Read actual native
   task/run/session and usage receipts before making a performance claim.

One completed Linux arithmetic pair on the pinned v0.22.5 kit reduced total
input, including cached input, from 21,242 to 16,734 tokens. Both returned the
same completion result with two physical requests. This does not establish
general quality, latency, RAM or cache improvement, or live Captain adoption.
Exhausted card scope remains exhausted even when the request ceiling has room.
The fragment does not configure messaging/Desktop platform toolsets; their
surfaces and permissions need separate native checks before use.
