# Cache layout observations

Prepared-request diagnostics record `shared_layout_version` as 1–4 when the effective instruction has a complete recognized common prefix, otherwise `null`. The field follows native instruction extraction and transport overrides. A cache-key prefix alone does not identify a prompt layout. Existing logs without this field remain unknown; timestamps cannot retrospectively identify their layout.

This content-free metadata does not change prompts, tool schemas, request options, cache keys or conversation history. It helps select future version-specific observations; it does not prove that requests share authenticated accounts, provider cache origin, or billing savings.

Validation: 21 new regression cases failed before the change; 35 related tests passed afterward. Installed Linux and Mac checks each exercised 25 cases and preserved all previous diagnostic fields and request contents. A fresh simple native arithmetic card completed with two successful provider requests; both recorded layout 4 and no request followed completion. No GPU was used and production gateways were not restarted.

## Bounded native card comparison

A later acceptance run used four fresh arithmetic cards: two profile-hint variants
under layout 3, followed by the same variants under layout 4. The baseline used
the installed native layout-3 implementation through a read-only default-version
overlay. Each card computed the same sum and completed through the native Kanban
lifecycle. Each used two successful provider requests, with identical tool
schemas and no request after completion. No production card was dispatched.

| Layout | Input tokens | Reported cached input | Cached proportion |
| --- | ---: | ---: | ---: |
| 3 | 42,361 | 9,984 | 23.57% |
| 4 | 42,349 | 26,240 | 61.96% |

Before each request, a guard verified that the effective instructions contained
the expected profile hint and layout. Fixture-only keyed digests confirmed that
the two layout-3 common prefixes and routing keys differed, while the layout-4
prefixes and keys matched. Each profile's own hint remained present. The second
layout-4 card reported 6,272 cached tokens on its first request; both layout-3
cards reported zero on their first requests.

This is one ordered pair per layout, without randomization or a provider-cache
reset. Provider retention and routing are outside the fixture's control; these
observations do not establish which earlier request populated the cache or a
repeatable billing/latency improvement. The first layout-3 card also missed on
its second request, contributing to the aggregate difference. Do not interpret
the percentages as a general savings forecast.

The acceptance harness initially targeted the wrong configuration location and
then the wrong platform name. Native tracing established that managed card agents
use `kanban`: the applicable override is root-level
`platform_hints.kanban.append`, not `agent.platform_hints` or a `cli` override.
The corrected run first checked native full prompt assembly, then verified the
actual outgoing requests. Earlier invalid comparisons and refused zero-request
cards were retained separately and excluded from the table. No product change
was needed for this harness correction.

Linux GPU devices were absent from the test environment. All four private
Gateways stopped after their cards; the production Gateway and 414 protected
files were unchanged. Raw requests, credentials, private routing keys, local
paths and task/session identifiers are not included in this summary.
