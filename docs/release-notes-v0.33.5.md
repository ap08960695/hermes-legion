# Hermes Legion v0.33.5 — Keep list edits when closing Settings

## What you will notice

Editing a comma-separated Settings list and pressing Escape now keeps the edit.
Previously, Settings closed while the focused list's unsaved draft disappeared.
For example, adding a second Environment Passthrough entry now saves both entries
and shows them again when Settings reopens. Empty lists and trailing commas use
the same parsing as Enter or moving focus away.

Apply the source kit and rebuild Desktop. This release does not install a rebuilt
daily app or recover edits already discarded by an older build.

## Implementation and checks

The shared ListField kept raw typing local and committed only on blur or Enter.
Removing Settings on Escape did not deliver that blur. A non-composing Escape now
blurs the input synchronously through the existing parse/change callback before
the overlay's bubbling listener closes it. The event is not prevented or stopped.
The existing IME predicate protects the new Escape branch; Enter behavior, raw
draft editing, parsing, native writer, scope ownership and unrelated unmounts
retain their existing behavior. No new state, API, schema, locale or dependency.

Three regressions fail before the fix while 27 controls pass. The tests render
the real OverlayView, focus and edit the real list input, and issue Escape without
manually firing blur. They assert one parsed callback before actual teardown.
Cases include trimming, trailing/empty segments, an empty list, Unicode and an
absent initial value. Enter, ordinary focus departure, draft-only typing,
unrelated unmount and both IME signals remain covered. Final nearest selection:
73 passes across six files; scoped lint, renderer types and build pass. The
inherited dynamic-import build warning remains. Two changed sections pass
pinned-base apply/hash/reverse; 1086 targets and test selection remain unchanged.

## Native Local evidence and limits

On the Mac, the original app displays an added Environment Passthrough entry in
the focused draft, then loses it after Escape: disk and reopened UI retain only
the original entry. The rebuilt app receives the same comma-separated draft and
Escape. Settings closes; native disk contains both entries and reopening shows
both without another config change. Full parsed comparisons preserve every
other primary value and the other profile's bytes. Both session stores stay
empty; no Send, inference or terminal tool runs.

The after cohort initially stayed on Connecting despite a ready native gateway;
one native View → Reload restored Connected before the list test. Its cause is
unestablished, so cold-start readiness is not claimed. A transient screenshot
capture failure recovered through a fresh read without repeating the mutation.
Raw diagnostics remain separate from accepted list-flow evidence.

Both cohorts close normally and pass actual 60-second SSH-zero gates. Sampled
maxima are four Hermes processes each, with observer-inclusive RSS 958,857,216
and 1,006,927,872 bytes. These are bounded samples, not continuous peaks or a
memory-saving result. Every owned process and port ends before original config
bytes/modes restore. The original 313-entry trial bundle and strict signature
restore. No owner app/data, ai, other host, ESTOP, pause or timer changes.

Native IME interaction, persistence before the debounce deadline, crash recovery,
all Settings pages, daily-app adoption and remote/ai/Linux behavior remain open.
