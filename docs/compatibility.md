# Compatibility

`patches/manifest.json` pins the upstream repository, base commit, patch hash and before/after hash of each target file. New files have a null before hash. The cumulative patch includes source, tests and generated contract changes that belong together.

The base verifier rejects a different HEAD, pre-existing changes, an unexpected new target or a symlink. The installed verifier checks exact resulting target bytes and rejects unrelated changes. Git's normal apply check is an additional independent guard.

This release does not claim general compatibility with the latest upstream, a provider's future API, every desktop platform or all imported skills. Model/provider identifiers and private account configuration are intentionally not supplied. Cross-platform tests must be run on their actual platform before claiming platform acceptance.

## Separate stable transport repair

The optional [stable transport repair](stable-transport-repair.md) targets a different exact upstream base using `patches/stable-transport/manifest.json`. It is not an update layer for the historical cumulative patch. It repairs request identity and worker transport resolution only; it does not install the cumulative UI, memory features or THINK/ACTION orchestration.

The expanded [stable runtime repair](stable-runtime-repair.md) supersedes the seven-path transport unit for new v0.22.5 checkouts. It includes an exact incremental upgrade and rollback for an unchanged seven-path installation; its full patch must not be stacked over the old full patch.

The [stable role workflow extension](stable-role-workflows.md) is a separately pinned 68-path unit on the v0.22.5 base. It includes the runtime repairs and native role/settings integration. Apply its full patch to a fresh matching checkout, not on top of another full kit.

The [cache-miss evidence unit](cache-miss-evidence.md) is a separate four-path repair on the exact v0.22.5 base. Its standalone verifier requires a clean matching checkout; it is not an updater or a cumulative feature pack.

## Consolidated stable alternative

The [v0.22.5 full kit](stable-full-kit.md) supplies 667 pinned source/test/UI paths as one alternative to the historical cumulative and smaller stable patches. Choose one exact manifest; do not stack full patches. Native clean-base apply/reverse/reapply was verified on Linux and macOS. Provider/session adoption and full platform test coverage are separate.
