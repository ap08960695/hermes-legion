# Hermes Legion v0.29.3 — Keep bot model labels readable

## What you will notice

In **Bots → Edit profile**, a long provider name stays inside its own dropdown
instead of running into the Model field. Both dropdown arrows remain visible.
Keyboard focus shows the full name in the existing tooltip; opening the menu
still exposes the full choice. The shared picker also serves bot creation and
advanced profile configuration.

The installed Radix selected-value component ignores its styling props. The
fix puts clipping on a real span around each selected value, leaving the arrow
outside. Model selection, routes and profile writers keep their existing behavior.
No dependency, backend helper or model call is added.

Apply the source kit to its pinned upstream base and rebuild Desktop through
the supported build path. This companion kit does not replace the installed app.

## Native Local acceptance

The retained before image shows the provider overlapping the neighboring field.
Its two changed source baselines match the prior kit. The corrected renderer
was checked in a fresh isolated Local app with the native gateway: wide
(3010 × 1776 pixels) and narrower (1712 × 2018 pixels) windows keep both labels
and arrows separate. Keyboard focus displayed the full provider tooltip. Both
menus opened; Escape preserved their selections. No Save, prompt or inference ran.

The completed trial passed an actual 60-second gate with zero SSH attempts or
executions, at most four sampled Hermes processes, and sampled RSS below 4 GiB.
All owned processes stopped, the gateway port closed, the task config stayed
byte-identical, and the original trial bundle was restored with its signature
verified. An interrupted first trial was separately closed and restored; its
missing final runtime receipt is not treated as completed acceptance. Private
screenshots and receipts remain outside the release in the local work report.

## Regression and limits

Ten picker tests pass using the actual SDK/Radix select controls. The clipping
contract failed on the previous implementation. Coverage includes long selected
text, arrows outside clipping, full tooltip labels, selection updates, cached
catalog reads and fallback behavior. Typecheck, renderer build and scoped lint
pass. Both changed patch sections apply, match their hashes and reverse to the
pinned base; unrelated sections are retained. The picker test is now explicitly
included in the Desktop test selection.

DOM tests prove component behavior; native screenshots prove the observed layout.
Native checks exercised menu dismissal without changing or saving a model.
Bot creation and advanced configuration use the shared fix but were not walked
live this round. Group mutations, actual worker monitoring, owner-app adoption
and Linux parity remain open. No production RAM or latency saving is claimed.
