# Cache layout observations

Prepared-request diagnostics record `shared_layout_version` as 1–4 when the effective instruction has a complete recognized common prefix, otherwise `null`. The field follows native instruction extraction and transport overrides. A cache-key prefix alone does not identify a prompt layout. Existing logs without this field remain unknown; timestamps cannot retrospectively identify their layout.

This content-free metadata does not change prompts, tool schemas, request options, cache keys or conversation history. It helps select future version-specific observations; it does not prove that requests share authenticated accounts, provider cache origin, or billing savings.

Validation: 21 new regression cases failed before the change; 35 related tests passed afterward. Installed Linux and Mac checks each exercised 25 cases and preserved all previous diagnostic fields and request contents. A fresh simple native arithmetic card completed with two successful provider requests; both recorded layout 4 and no request followed completion. No GPU was used and production gateways were not restarted.
