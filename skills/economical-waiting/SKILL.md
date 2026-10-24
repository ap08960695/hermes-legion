---
name: economical-waiting
description: Wait for existing operations without repeated inference.
---

# Economical Waiting

Use when a script or worker remains active. Record the native operation identity and completion channel. Prefer a native yield, completion event or one bounded wait. If observation is necessary, use coarse non-model checks with a deadline. Do not rerun a command because its response is slow or unknown. Notify only on completion, failure or required input. Inspect available independent work before waiting.

Use only existing authorized provider lanes and native quotas. No paid fallback, allowance probes or model-backed polling. Preserve owner decisions, rights, review and publication gates. Do not interrupt active workers or modify unrelated services. Report meaningful completion, failure or a material owner question; stay quiet on unchanged waits. Role guidance confers no additional tool or filesystem permission.
