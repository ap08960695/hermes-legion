# Hermes Legion v0.29.0 — Activity on bot cards

## What you will notice

- See a bot's reported worker activity directly on its card, below its
  conversation preview, without switching to Manage team.
- Read the reported tool, step, elapsed time and input/output token totals
  together. Missing facts stay absent; this display makes no model call.
- Keep the canonical conversation preview separate from the worker's activity.
  Open chat keeps its existing destination; the worker session is not a chat pin.

Cards reuse the existing localized activity component and tooltip from the
compact Bots rail. Received terminal, stale, retained, missing-source or
unreachable observations are hidden by that component's existing policy.
Activity follows the existing roster refresh; no new timer, request, worker,
connection, preference or dependency is added.

Apply the consolidated source kit to its pinned upstream base and rebuild
Desktop through its supported build path. This companion release does not
replace an installed app or change stored profiles.

## Native Mac display acceptance

The pre-change native Local app showed only Working for a controlled worker
observation. The corrected renderer showed the description, tool, step 3/8,
elapsed time and synthetic token totals in wide and narrow windows. Its
canonical conversation preview stayed separate. After the native SessionDB
record was ended and Refresh clicked, activity disappeared, Working became
zero, and the same conversation preview remained.

These were controlled, explicitly synthetic native SessionDB records, not an
executing worker or paid model task. They prove live UI rendering and received
observation transitions. Actual native worker lifecycle and the correctness or
timeliness of real workers' activity records remain unverified.

Wide screenshots measured 3010 by 1776 pixels; narrow screenshots measured
1714 by 2018 pixels. Both native cohorts passed their 60-second gates with
zero SSH attempts/executions and at most four sampled Hermes processes. All
owned native processes stopped, gateways closed, DesktopSSH was zero, and the
original trial bundles were restored with strict signature verification.
Configuration stayed byte-exact. Owner data and other machines were untouched.
Private images and receipts remain outside the release in the local work report.

## Regression and limits

A new rendered workspace regression failed on missing activity before the
change and passes after it. Seven UI cases across the workspace and reused
component pass, including terminal/stale/unavailable observation suppression,
canonical preview preservation and exact-owner click behavior. Renderer types
and build pass. Scoped lint introduces no diagnostic: the workspace's 47 and
test file's six preexisting findings remain. Both changed patch sections apply,
match their hashes and reverse to the pinned base; unrelated sections and the
existing test selection are retained. The kit remains 1064 paths.

To repeat, use isolated Local data with a canonical Bot Chat and a clearly
synthetic recent worker record; inspect cards at both widths, end the record,
refresh, and confirm activity disappears while the conversation preview stays.
Do not treat seeded tokens, timestamps or records as actual model or worker use.

Daily-app adoption, Linux parity, real worker execution, automatic lifecycle
tracking and end-to-end bot monitoring remain untested. The full Config/Bots/
Chat walkthrough and chat formats are still open. No production saving is claimed.
