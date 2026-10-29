# Honor disabled async auxiliary retries

`auxiliary.transient_retries: 0` already disabled immediate same-provider retries
for synchronous auxiliary calls. The async path still retried a transient failure
once unconditionally, so one logical call could send a second physical request
against the saved setting.

The async path now checks the same configured zero budget before retrying and
preserves main-owned client authority. A positive budget retains the existing
maximum of one async retry; this change does not raise it to the sync default.
Sync behavior, timeouts, critical-task guards, request data, model effort, account
selection and provider/fallback routing are unchanged.

```yaml
auxiliary:
  transient_retries: 0
```

This setting controls immediate same-provider transport retry only. Existing
configured recovery/fallback authority is separate; preserve an explicit no-paid-
fallback policy rather than treating this setting as a provider allowlist.
A failed request keeps its real error. The change does not close a borrowed main
transport or silently replay a completed task.

## Evidence

The corrected regression first failed four checks while six controls passed.
It uses the real AsyncOpenAI SDK and native request/relay preparation with a
scripted HTTP boundary and fenced recovery exit, so it cannot call real providers.
Zero and negative-clamped budgets each send one request, even if a second would
succeed; a genuinely main-bound client also refuses the immediate retry. Positive
budgets retain two total attempts at most. Nontransient errors are not retried.

Final focused selection: three files / 24 passed, zero failures and retries.
The broader 125-file auxiliary/compression/goal selection has 1,270 passes and
20 failures. All 20 reproduce on the unchanged parent across the same six failed
files; zero new failures, not global-green. The exact inherited names are retained
in the reproducible test selection. Existing compression same-main-context,
auth/recovery and budget guards were not relaxed to make old fixtures pass.
Code-health found no new findings, without growing the already oversized module.

Installed Linux acceptance uses the original production interpreter, actual
canonical source, real SDK serialization and a local HTTP server. Only that
server's loopback socket is allowed; the recovery exit is fenced. Five cases:

| Saved budget | Controlled response | Physical primary requests |
| ---: | ---: | ---: |
| 0 | 503 | 1 |
| 1 | 503 | 2 |
| 6 | 503 | 2 |
| 0 | 200 | 1 |
| 1 | 400 | 1 |

No external provider or model is called. Original config, credentials, models,
quota, stop state and active work remain unchanged. The same five installed-source checks pass on macOS, without starting its original
Gateway.
Do not substitute cross-platform source apply or simulated faults for original
workload inference. These counts prove disabled retry admission, not a measured
billing, cache, RAM or production latency saving.
