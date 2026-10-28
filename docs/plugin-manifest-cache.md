# Plugin manifest metadata reuse

Every served profile discovers plugin manifests. Previously the same unchanged
bundled YAML file was parsed again for each profile. Discovery now uses Hermes'
existing read-only YAML file cache and its native file-signature invalidation.
A deep copy is made before normalization and PluginManifest construction, so
mutable lists, nested defaults, source, path and namespace remain caller-owned.
No second cache, new registry, timer, model request or configuration option is added.

Edits, replacement, deletion and permission revocation follow the existing native
file-reader rules. UTF-8 BOM and YAML 1.1 behavior are retained. Failed parses are
not cached. Plugin selection, capabilities, consent, module isolation, reload and
frozen conversation/tool behavior remain native. This cache covers local metadata;
it is unrelated to provider prompt caching or account allowance.

## Validation

The selected regression suite passed 15 files / 203 cases with zero retries,
including manifest versions, discovery/reload, module eviction, profile isolation,
BOM/booleans, nested mutation isolation, preserved-mtime rewrites, deletion, invalid
file repair and native permission revocation. Installed Linux and macOS acceptance
each passed 8 controls in synthetic homes with network denied and zero inference.
Native code-health comparison reported no findings. The original macOS Gateway
was not started for acceptance; no Desktop bundle was rebuilt.

## Measurements and limits

Using the same production interpreter and 107 public bundled YAML manifests,
25 warm passes performed 2,675 YAML parses before / 0 after initial population.
Warm median per pass: 18.63 / 1.39 ms. File-signature checks and caller copies still
run; this is a parsing reduction, not a claim that all discovery work disappears.

One matched, untraced startup comparison used 116 synthetic profiles, bundled default
plugin discovery, empty native stores and the native ready gate. Plugin discovery
phase: approximately 6.58 / 5.27 seconds. Final PSS: approximately 318.51 / 310.56 MiB.
Whole readiness time: 31.02 / 30.97 seconds, effectively unchanged: profile store and
authority initialization still dominate. These are component measurements and one
startup pair, not a universal speedup or proof of lower whole-Gateway RAM, token
usage, provider cache misses or original-user workload cost. No production board,
conversation or provider request was used.

Metadata is retained by the existing file cache; this change does not introduce a
separate retention policy. Per-profile manifest containers remain distinct.
