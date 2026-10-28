# Compatibility

`patches/manifest.json` pins the upstream repository, base commit, patch hash and before/after hash of each target file. New files have a null before hash. The cumulative patch includes source, tests and generated contract changes that belong together.

The base verifier rejects a different HEAD, pre-existing changes, an unexpected new target or a symlink. The installed verifier checks exact resulting target bytes and rejects unrelated changes. Git's normal apply check is an additional independent guard.

This release does not claim general compatibility with the latest upstream, a provider's future API, every desktop platform or all imported skills. Model/provider identifiers and private account configuration are intentionally not supplied. Cross-platform tests must be run on their actual platform before claiming platform acceptance.

## Separate stable transport repair

The optional [stable transport repair](stable-transport-repair.md) targets a different exact upstream base using `patches/stable-transport/manifest.json`. It is not an update layer for the historical cumulative patch. It repairs request identity and worker transport resolution only; it does not install the cumulative UI, memory features or THINK/ACTION orchestration.

The expanded [stable runtime repair](stable-runtime-repair.md) supersedes the seven-path transport unit for new v0.22.5 checkouts. It includes an exact incremental upgrade and rollback for an unchanged seven-path installation; its full patch must not be stacked over the old full patch.
