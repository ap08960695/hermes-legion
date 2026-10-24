# Architecture

Legatus coordinates; specialist roles execute bounded work through the native Hermes workflow. The task contract defines inputs, expected artifacts, verification and ownership. Dependencies determine what may run in parallel; explicit write scopes help prevent conflicting edits.

A provider lane supplies an existing authorized capability to a role. Route selection considers role, actual modality, current native eligibility and quota. Neither a bot name nor a subscription label proves capacity. Cooldowns and refusals remain refusals; no paid fallback is introduced.

The completion path uses durable native evidence. A successful completion tool result is followed by exact ownership and terminal-state checks. Only then can the worker stop without asking the model for another status read or summary. Incomplete evidence leaves the existing correction path available.

The wait path records an operation identity and its genuine completion signal. It checks for other independent ready work before waiting, then uses bounded non-model observation. A wait timeout is not permission to rerun the operation.

The context path favors stable instructions and tool schemas, compact recoverable handoffs, lazy skill loading and bounded outputs. Content-free diagnostics distinguish observed cache/token values from hypotheses about provider cache origin or billing.
