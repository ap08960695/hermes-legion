# Preserve settings edits followed by a null section

From v0.8.15, the shared settings merge follows the native config API's treatment
of null sections. Updating a nested setting and then sending `null` for its parent
while autosave is pending no longer drops the accepted edit.

For example, consider these consecutive patches:

```json
{"auxiliary":{"vision":{"model":"updated-model"}}}
{"auxiliary":{"vision":null}}
```

The native API ignores null over an existing mapping. Sent separately, these
patches retain the new model. Previously, Desktop's coalescing helper replaced the
mapping with null, and the backend ignored the resulting patch: the old model
remained. The renderer also used this helper for its optimistic settings cache.

The helper now preserves a mapping when the next value is null. Null still replaces
scalar and list leaves, and arrays keep their replacement semantics. Debouncing,
captured destinations, ordered writes, failure retention and close/quit guards are
unchanged. This does not make null a command to delete an entire config section.

## Evidence

Two new regressions failed before the repair. The five-file related selection
passes 30 tests, including the Settings component and native queue/route/quit
contracts. Electron type checking, scoped lint and the source-health ratchet pass.

A separate isolated check sent the actual queue's emitted patches through the
installed native config handler into temporary files. Before the fix, sequential
and coalesced writes persisted different model values. After the fix they match,
with the unrelated provider and endpoint preserved. The same native check passes
on ARM64 macOS. Neither check made a model request or exposed GPU access.

Linux and Mac source inventories match all 953 patched paths. Both native packages
were rebuilt and installed before publication; their bundled files match the build
outputs and source fingerprints, and the Mac application passes strict signature
verification. Packaging used the standard source preparation route after an
offline attempt could not refresh its packaging receipt. No dependency or lockfile
change is part of the patch.

These are queue-to-native-storage and package checks. A new visual Desktop journey
was not run for this change. They do not establish crash durability, general
cross-profile failure recovery, production usage savings or a change to the
existing single config-write lane.
