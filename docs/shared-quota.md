# Shared quota and capacity accounting

Quota belongs to the actual native account/scope, not the bot's display name. Web and native profiles referencing the same actual quota scope share one budget. Do not assume every product surface has either shared or separate limits: derive the real scope from native/provider evidence, and use a conservative shared scope while it is unknown.

The offline snapshot supplies `max_parallel`, `active`, `remaining_hour`, `remaining_day` and `cooldown_until` for each group. These are **operator-supplied simulated remaining request reservations**, not new limits or a full billing ledger. Examples are fabricated numbers. For a real planning snapshot, use the most restrictive current applicable provider/account/host/project cap and budget. Never raise a native limit to match an example.

Each planned task reserves one worker slot and its declared `request_budget` from both remaining counters in an in-memory copy. Aliases sharing a quota group debit the same copy. A request budget must be a conservative bound on the work being proposed; it is not an observed token count or a promise of exactly one future model request. If a native quota cannot be represented in these units, do not invent a conversion or an unlimited balance: hold and use native eligibility instead.

Missing, invalid, exhausted or stale budget/readiness data means HOLD. Cooling-down groups stay cooling down; the planner neither resets them nor retries inference. All groups exhausted means HOLD, never a metered paid fallback. Existing active counts must include other bots and workers already using the account.

The returned reservations are a **single-plan simulation only**. They are not persisted or synchronized across invocations, processes or machines. Never run independent copies and treat their totals as a live shared quota allocator. Real dispatch, leases, cooldown updates and accounting remain Hermes' native source of truth.
