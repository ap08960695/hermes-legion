# Hermes Legion v0.33.2 — Keep untouched settings visible after import

## What you will notice

Importing a partial config keeps untouched fields visible with their current
values. For example, importing only Memory Budget no longer makes Persistent
Memory and User Profile look disabled or Profile Budget look empty. Repeating
the same import also keeps the form correct; reopening Settings is unnecessary.

If you edit the form or leave its scope while a file is still being read, that
stale read is discarded. Import again to apply it to the current form. Existing
save-error and toolset-removal confirmation behavior remains.

Apply the source kit and rebuild Desktop. This source bug-fix release does not
replace the daily Mac app or change the native writer.

## Implementation and checks

Import now merges sparse input into the displayed record using the existing
shared config merge. Omitted fields remain; explicit false, zero, list replacement
and scalar null retain native semantics. Null over an existing mapping remains
ignored. Existing version/generation counters fence delayed reads; no extra state,
writer, dependency, locale, API or backend behavior is added.

Seven new component/FileReader cases fail before the change, while 16 existing
cases pass. The final nearest selection passes 75 tests. Coverage includes held
and rejected saves, omitted values, exact sparse intent for the next ordinary
edit, empty and null-mapping imports, explicit values and delayed read versus
edit/unmount. Scoped lint, renderer types and build pass. A test-harness typing
error was corrected by awaiting the real FileReader loadend event. Existing
React act warnings and the unrelated dynamic-import build warning remain.
Two changed source/test sections pass pinned-base apply/hash/reverse; 1085 targets
and the test selection remain unchanged.

Native Mac before/after acceptance uses fresh Local-only homes and two actual
imports of the same memory-only file. Before, omitted switches look off and
Profile Budget stays empty after the repeated import. After, both switches stay
on and Profile Budget stays 1375 while Memory Budget changes from 2200 to 2901.
Disk readback contains only the requested memory override; inherited defaults
remain implicit and all original file keys remain equal. A following User Profile
toggle writes only its intended additional value, and Settings reopen reads it
back with the other values correct. No Send or model request runs.

Both launches pass actual 60-second SSH-zero gates and sample at most four Hermes
processes. Observer-inclusive sampled RSS maxima are 940,507,136 and 936,787,968
bytes. These are bounded samples, not continuous peaks or a memory-saving result.
All owned processes end, gateway ports close, and config bytes/modes plus the
original 313-entry trial bundle and strict signature are restored. Screenshots,
raw evidence and rollback copies remain outside the public kit. No owner data,
other host, ai, ESTOP, pause or timer is changed.

Native coverage is this Local Settings journey. Delayed-read races and rejected
saves have focused offline coverage; no new native failure injection is claimed.
Full Settings coverage, daily-app adoption and ai/Linux acceptance remain open.
