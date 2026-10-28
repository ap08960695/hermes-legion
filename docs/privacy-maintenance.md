# Historical artifact privacy maintenance

Private operational card references were found in two legacy source comments.
The affected comments were neutralized across the public commit graph and tagged
release payloads, and the corresponding source, patch and inventory digests were
regenerated. The Python abstract syntax trees before and after the comment repair
matched. This maintenance does not change runtime behavior or install, restart,
resume, reassign or send anything through an existing Hermes installation.

## What changes for consumers

Historical version names are preserved, but corrected commit and annotated-tag
objects and source-archive digests differ from previously downloaded copies.
`SHA256SUMS` is regenerated for releases that provide it. Use the inventory and
asset attached to the same corrected version; do not combine an old archive with
a new manifest. The read-only verifier should refuse mismatched copies.

If an existing local installation was built from earlier bytes, retain its own
scoped receipt and rollback, prepare a separate matching checkout and use the
native tested idle-update workflow. Do not force apply/reverse through a hash
refusal or reset a live source tree. No account, quota, provider, paid fallback,
telemetry-consent or project/rights/review/publication gate is changed by this
maintenance. No new model calls are needed to check the artifact.

## Evidence boundary

Checks cover the current public file inventories, reachable Git objects and
paths, neutral commit/tag metadata, regenerated release payloads and anonymous
readback. Current known identifiers and credential variants are compared
privately; values are not exported into the repository or reports made public.
A scan without findings is evidence for its checked scope, not proof about every
unknown historical secret.

A repository rewrite and asset replacement cannot guarantee removal of copies
already retained in third-party clones, forks or platform caches. The maintenance
therefore claims corrected current refs and release files, not universal erasure.
No credentials were identified by the operational-comment finding, and it should
not be described as a model-provider credential compromise.
