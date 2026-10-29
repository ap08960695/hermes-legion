# Atomic fresh schema creation

Hermes initializes many tables and indexes when a new profile first opens its
SQLite session store. The declared schema previously used SQLite autocommit for
each DDL statement. A failure partway through could leave a partial declaration,
and fresh profiles paid repeated commit overhead.

A store with an empty SQLite schema now runs the same `SCHEMA_SQL` through Hermes'
existing transactional DDL helper inside one `BEGIN IMMEDIATE` transaction. The
complete declaration commits once; exceptions roll it back. The normal open and
recovery path can then initialize it again. This is not a schema-version change.

Any store with existing schema objects keeps the prior native declaration path.
It does not gain an unconditional write transaction that could block a settled
open behind another writer. Column reconciliation, legacy migrations, later
indexes/triggers and FTS setup run afterward as before, including FTS cross-process
admission and all deleted-WAL, holder, file-generation and lock guards. No pragma,
`FULL` durability, cache, provider, model, quota, fallback, dependency or configuration
policy is reduced to obtain the speedup. No production database is copied or restored.

## Validation

Two new contracts failed before the change: a fresh declaration was not in one
transaction, and denying the second table left the first table persisted. The
existing-data preservation control already passed. The final native selection
covers all storage test files plus the prior Gateway/TUI lifecycle selection:
272 files, 2,335 passed, 0 failed, 16 existing platform skips, zero retries.
Native code-health comparison is clear. Historical subset counts overlap.

Installed Linux and macOS acceptance each pass 8 controls using the production
interpreter and real private SQLite stores: fresh transaction visibility; committed
WAL with explicitly configured `FULL` durability; schema probes and integrity;
message/history/FTS search; settled reopen; read-only access; rollback on denied
DDL followed by an ordinary successful open; existing data preservation and the
legacy declaration path after an injected failure. Network is denied and no model
or provider request is made. The original macOS Gateway is not started for proof.
No Desktop bundle is rebuilt by this backend change.

## Measurements and limits

Four separate production-interpreter processes ran in ABBA order, each opening
16 fresh stores and then reopening those same stores, without a profiler. Apart
from the exact before/candidate schema module, the native source and settings are
the same. Median fresh open plus close was 170.9 / 172.0 ms before and 110.6 / 110.8 ms
after, about 35.4% lower when averaging those medians. Settled-open medians stayed
roughly 16.9-17.6 ms. All stores and messages were synthetic and private.

The earlier diagnostic cProfile run is separate: 16 fresh opens took 2.91 seconds,
with 2.31 seconds attributed cumulatively to schema initialization. Profiling adds
overhead and is not used for the raw before/after latency claim.

These figures measure new-store initialization. They do not prove faster startup
of an existing populated Gateway, lower model latency, RAM/token savings, better
provider cache hits or original-user conversation adoption. Existing-store safety
and reconciliation take priority over forcing the fresh optimization onto legacy
stores.
