# Bot team, families and provider twins

Legion now describes a working team topology: a Captain, role-specific workers, native-provider twins, and six Web specialists. A role is a job contract; a profile is an executable Hermes identity; a provider lane supplies capability; a native credential pool supplies authorized account access. These are different things.

| Public role | Job |
|---|---|
| Legatus | Captain: coordinate, specify, route, inspect evidence, ask only material owner questions |
| Strategist | Architecture, planning and dependency decomposition |
| Scout | Research and source/reference collection |
| Oracle | Evidence analysis and decision briefs |
| Artificer | Implementation |
| Auditor | Independent review |
| Prober | Testing and acceptance evidence |
| Archivist | Documents and structured deliverables |
| Studio | Media/visual production |
| Vox | Voice scripting and authorized audio-workflow preparation |
| Scribe | Writing and compact recoverable handoffs |
| Prism | Visual analysis on a verified image-capable route |
| Sentinel | Operator and process observation |
| Steward | DevOps, release preparation and rollback |
| Custodian | Genuine incident/maintenance investigation |

The full example has **34 profiles**: Captain and planner, two native-provider variants for each of thirteen other families, and six Web specialists. The provider twins use distinct `-codex` / `-claude` profile IDs but follow the same family contract. Preferences vary by role; the example does not default every job to the same model/provider. Actual model IDs are deliberately operator-selected placeholders.

| Web specialist | Suitable role |
|---|---|
| Forge Web | Coding |
| Atlas Web | Research and documents |
| Citadel Web | Architecture and planning |
| Tribunal Web | Deep independent review |
| Spark Web | Short triage and tests |
| Press Web | Document batch preparation |

A suitable, genuinely ready public-data Web route is considered alongside native twins. Private data cannot enter a public-only route. A name or subscription label proves neither quota nor tools, vision or audio support. An independent reviewer is a different worker/run with the appropriate gates, not merely a second account name.

Start with `examples/team.small.json` if the full roster is unnecessary. Reference metadata in `roles.json` / `examples/` is **not** raw Hermes configuration. Native configuration fragments live under `profiles/native/`; follow [setup](setup-multi-account.md). No original private bot name, persona, account or rename map is included.

## Planning and execution

The Captain template names the optional Strategist role as a planning choice for complex work. A ready specialist can execute a bounded task directly, without a separate planning card when one adds no value. Create or assign cards only through the existing native workflow after checking duplicates, dependencies, permissions, holds and quotas. A template is guidance, not automatic dispatch or evidence that a particular session loaded it. Select only configured and authorized models and providers; existing account bindings and fallback policy remain in force.
