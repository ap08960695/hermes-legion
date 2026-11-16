# Hermes Legion v0.33.0 — See parallel bot work

## What you will notice

A full Bots card now lists each recent observed worker, with its task title and
reported activity, tool, step, elapsed time and token facts. The activity count
follows those same observations. A longer list scrolls with keyboard access.
The compact bot row keeps the latest eligible stamp and adds a count when more
than one worker is observed. **Working** still counts bots, not workers.

Stopping the newest worker no longer makes the bot look idle while another
observed worker remains active. Finished workers disappear from the activity
list after refresh. The human conversation preview and Open chat destination
stay separate from worker metadata.

Apply the source kit to the gateway and Desktop, restart the updated gateway,
and rebuild Desktop. This source release does not replace the daily Mac app.
It groups parallel activity display, counts and consistent status into one
monitoring capability set.

## Behavior and compatibility

The existing roster read/cache now carries optional `worker_sessions`, alongside
the unchanged singular `worker_session`. The canonical own/sibling query reads
at most 20 visible worker rows. The legacy reader uses the same 20 mixed session
rows it already fetched, so it may observe fewer workers. Both reuse the same
safe per-worker projection and existing hidden/archive/profile visibility rules.
Private prompts, messages, model configuration and parent IDs are not projected.
No new query, polling timer, write route, dependency or database migration is added.

One client eligibility rule drives the list, count and working mood. It rejects
ended workers, observations outside the existing 150-second freshness window,
and retained/missing/unreachable sources. It bounds the list before filtering.
An absent parallel field uses the old singular stamp; explicit empty/null does
not resurrect it. Older clients retain the singular field.

These are bounded observations, not a process census. Workers outside the read
window or without a recent heartbeat may be absent. Payloads contain more bounded
metadata than before; no RAM, context, usage or latency saving is claimed.

## Verification

Seven new backend cases fail before the change, with 20 controls passing. All
27 native synchronous test bodies then pass using real SessionDB and task-local
fixture adapters. The managed interpreter has no pytest: this is not a canonical
pytest/conftest-suite result. The actual pytest regressions remain packaged and
selected for the normal upstream runner. An initial bounds fixture reused titles
against the native unique-title constraint; it was corrected before the valid
red run. Strict contract checks cover old rows, the 20-row bound and unknown
private fields.

Four UI regressions fail before implementation; the final nearest selection
passes 42 tests across eligibility, worker display, compact rows and Bots cards.
It covers two-to-one-to-none transitions, older-worker survival, absence versus
empty/null, expiry, the bound and compact rows without nested controls. Scoped
lint, types and renderer build pass. Inherited React act warnings in row tests
and the existing dynamic-import build warning remain. Twelve changed sections
pass pinned-base apply/hash/reverse; 1085 targets and test selection remain.

Native Mac before/after runs each start with an empty Local store and actual UI
Send, creating two native children in the same profile through `delegate_task`.
Before, Bots showed only A; stopping A produced Ready / Working 0 while B ran,
until B's next heartbeat restored Working. After, Bots showed both titles and
count 2. Stopping A left B and count 1 / Working visible immediately after Refresh,
before that heartbeat. The later heartbeat kept B's title beside its new waiting
activity. B completed, the real batch result reached the parent, and Refresh
showed Ready / Working 0 with no worker detail and the parent's new preview.

Read-only SQLite snapshots verify lineage, heartbeat, terminal state, B's saved
reply and refusal of A's late reply. Each run used five controlled loopback model
requests and one native batch delivery. Only reply content/timing were controlled;
no lifecycle records were seeded. Completed API counts were A=0/B=1; the native
interruption ledger still records A's attempted call. Synthetic token totals are
fixture accounting, not provider usage or production model-quality evidence.

Both launches passed actual 60-second Local gates with SSH0 and at most four
sampled Hermes processes. Observer-inclusive RSS maxima were
1,226,244,096/1,228,685,312 bytes over 2272/1753 samples. These are sampled resource
bounds, not continuous peaks or a memory comparison. Both process sets, gateway
and model ports and model threads ended. Original 313-entry trial bundle,
hashes, strict signature and baseline configs were restored. Owner data, other
hosts, ESTOP, pauses and timers were untouched.

Private images include r106-07-two-workers-baseline.jpg,
r106-13-older-hidden-refresh.jpg, r106b-06-two-workers.jpg,
r106b-12-B-refresh.jpg, r106b-13-B-heartbeat.jpg and r106b-14-terminal-ready.jpg.
Images, hashes, raw state and rollback receipts stay outside the public kit.
Native coverage is the canonical Local full card in one wide Mac window.
Compact-row/legacy/sibling behavior has offline coverage; native legacy/sibling,
managed-worker subprocess monitoring, large-list scrolling, narrow layout, Linux
parity and daily-app adoption remain open.
