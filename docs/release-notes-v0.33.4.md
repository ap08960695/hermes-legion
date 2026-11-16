# Hermes Legion v0.33.4 — Nudge compression ratios precisely

## What you will notice

In **Memory & Context → Context & compression**, increasing Compression Threshold
from 0.50 now gives 0.51; increasing Compression Target from 0.20 gives 0.21.
The two ratio controls move by one percentage point instead of a whole ratio unit.
Counts and timeout controls retain their existing whole-unit steps.

Apply the source kit and rebuild Desktop. This source bug-fix release does not
install a rebuilt daily app. Existing saved values are not rewritten: if an older
arrow click saved a mistaken ratio, type the intended value. Range validation
and compression policy remain unchanged.

## Implementation and checks

The shared ConfigField number input previously omitted `step`, so native HTML
stepping used 1 and saved the resulting numeric value through the normal writer.
One input attribute now gives exactly `compression.threshold` and
`compression.target_ratio` a 0.01 step. The choice gives one-percentage-point
precision, consistent with the CLI's whole-percent display. Schema carries no
step/default metadata; explicit field identity keeps zero, whole-valued ratios
and older unknown numeric fields predictable. No schema, API, backend, locale,
dependency, conversion, new state or generic writer change is included.

Eight focused ratio cases fail before the fix while 14 controls pass. The final
nearest selection passes 65 tests across six files. Real input `stepUp/stepDown`
and the resulting change callback cover Up/Down, zero, a whole-valued ratio and
an absent value. Memory counts, protected-message counts, timeouts, a legacy zero
and an unknown fractional field preserve unit stepping. The first test draft
asserted after React restored a fixed controlled prop; this harness error was
corrected before the genuine red run. Scoped lint, renderer types and build pass;
the unrelated existing dynamic-import build warning remains. Two changed source/
test sections pass pinned-base apply/hash/reverse. The kit stays at 1086 targets
with its existing explicit test selection.

Native Mac before/after uses fresh Local-only homes with two synthetic profiles.
With default selected while scope-b remains active, one ArrowUp originally saves
Threshold 0.5→1.5 and Target 0.2→1.2. The rebuilt app saves 0.5→0.51 and 0.2→0.21
through the same keyboard actions. Protected Recent Messages still moves
20→21→20. Full native config comparisons preserve every other value and the
other profile's bytes; reopening Settings reads 0.51/0.21 with no further write.
Both session stores remain empty. No Send, inference or compression execution runs.

Both cohorts close normally, pass actual 60-second SSH-zero gates and sample at
most four Hermes processes. Observer-inclusive RSS maxima are 905,887,744 and
898,891,776 bytes. These are bounded samples, not continuous peaks, physical RAM
or a memory-saving result. All owned identities and gateway ports end; original
config bytes/modes and the 313-entry trial bundle with strict signature restore.
Private screenshots, raw records and rollback copies stay outside the public kit.
No owner app/data, ai, other host, ESTOP, pause or timer is changed.

This proves ratio-control stepping, native persistence, count preservation and
Settings reopen. It does not prove compression effectiveness, arbitrary range
validation, full Settings coverage, daily-app adoption or remote/ai/Linux behavior.
