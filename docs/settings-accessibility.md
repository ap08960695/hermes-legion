# Name settings controls for assistive navigation

The shared settings editor displayed a field title beside its control without
giving the control an accessible name. For example, Memory Budget and Profile
Budget appeared as unnamed numeric inputs to assistive navigation. Closed selects
announced their value without the setting name.

The shared editor now passes its existing localized title to numeric, text,
multiline, object, list, enum, searchable and free-input controls. This preserves
the displayed copy, layout, values and save behavior. Boolean rows already had
names. Specialized settings editors outside this shared component are not covered
by this repair.

## Acceptance

Nine regression cases initially failed on the preceding source. One fixture's
voice label was corrected from `Voice` to the existing `OpenAI Voice`; the final
six-file selection passes 33 tests, including typed values and localized numeric
labels. Renderer type checking, scoped lint and source-health checks pass.

Linux and ARM64 Mac packages were rebuilt and installed before publication, with
matching renderer source hashes. The packaged files match compiled output on each
host. The 922-path source kit applies, reverses and reapplies with exact hashes.
The production Linux Gateway was not restarted. Mac packaging and Finder adoption
are verified; interactive Mac UI acceptance is still separate.

The installed Linux app was exercised through its native private Gateway in a
network-isolated home without GPU devices. Settings → Memory & Context exposes
named Memory Budget, Profile Budget and Memory Provider controls. Changing Memory
Budget through its accessible name persists after the native write completes and
the page reloads. Screenshots at 1280 and 640 pixels show the saved value. The
earlier toggle test also survives reload. No workers or model requests run.
The only observed console resource errors were the offline Google Fonts request.

## Save limitation in v0.8.11

Reloading immediately after an edit, before the existing 550 ms autosave debounce
fires, discards the pending value. This was reproduced in v0.8.11. The subsequent
[v0.8.12 autosave repair](settings-autosave.md) addresses it. Successful persistence checks waited for the actual file write;
they do not prove that immediate reload or app exit preserves pending edits.
