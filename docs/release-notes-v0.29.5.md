# Hermes Legion v0.29.5 — Show when a delegated response was stopped

## What you will notice

After you stop a delegated child, its chat card shows **Response stopped** with
a neutral stop icon. It no longer labels an explicit interruption as a red
Error. Partial output remains available. Genuine failures still show Error;
completed children keep their completion mark.

The renderer already receives an `interrupted` status. The card grouped it with
failures, and settled-result normalization also collapsed it into `failed`.
This fix preserves that explicit status and reuses the existing translated
stopped label and stop icon. Unknown outcomes remain failures. It adds no model
request, timer, dependency, translation key or cancellation mechanism.

Apply the source kit to its pinned upstream base and rebuild Desktop. Backend
control and authority checks are unchanged. The kit does not replace the owner's
installed app or restart a running session.

## Stop one child

Use Layout editor → Advanced → Done to reveal the session status stack. In the
parent chat, expand **Subagents**, select the child there, and choose **Stop**.
The other children can continue. The transcript's child-title button opens its
separate window; use the composer shelf for the in-place control.

A Stop request and terminal completion are different observations. It does not
undo completed work or guarantee that every external tool or provider request
can be cancelled immediately.

## Verification and limits

A real Local UI Send started two native delegated children. Stopping A ended its
native agent while B stayed active and advanced its normal heartbeat. A later
fixture reply could not overwrite A's terminal timestamp or persist a successful
response. B completed after its independent release, and the parent received a
native result reporting A interrupted and B completed. Only model content and
timing were simulated on loopback; the agents, control RPC, SQLite and renderer
remained native. Before/after screenshots show Error versus Response stopped.

The first diagnostic opened a child window and briefly sampled five Hermes
processes; the existing four-process guard stopped and restored it. The admitted
before/after cohorts used composer controls and stayed at four or fewer sampled
Hermes processes, below 4 GiB including the observer, with actual 60-second
Local/SSH-zero launch gates. All owned processes stopped, ports closed and the
trial app/config were restored. No other machine or owner data was touched.

Seven new regression cases cover live and explicit settled interruption, empty
and partial output, late progress, and genuine failures/completions. Five fail
on the original implementation; all 17 nearest cases pass after repair. Scoped
lint, renderer types and a bounded renderer build pass. The build retains an
unrelated dynamic-import warning. Four changed source/test sections pass pinned
base apply/hash/reverse checks; unrelated kit sections are retained.

Explicit interrupted settled results retain the stopped presentation in the
component. Native async dispatch history still restores its existing parked
rows when it has no per-child status; the parent result and issue notification
survive Reload. This release does not add durable child-outcome history or
redesign the global Agents view. Whole native suite, external-tool cancellation,
owner-app adoption, Linux parity and production efficiency remain unverified.
