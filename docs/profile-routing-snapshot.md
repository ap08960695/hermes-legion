# Inspect saved bot routing in one native command

A coordinator should not need several searches and full config-file reads just
to identify a role pair and the fleet's dispatch allowlist. Use the existing CLI:

```sh
hermes profile list --routing-json
```

The optional flag leaves the ordinary human profile table unchanged. Its compact,
stably sorted JSON describes saved model/provider/effort settings, reciprocal
THINK/ACTION links and dispatch-policy admission. It uses native profile names,
workflow validation, effort ceilings and fleet allowlist resolution. It does not
walk skill trees, inspect auth files, expand secret variables, start a Gateway,
probe account readiness or call a model. Native CLI startup keeps its own normal
environment/bootstrap behavior; the snapshot reads only routing metadata.

## How a coordinator should use it

1. Read the snapshot once for the current coordination task, rather than searching
   profile files to reconstruct the same metadata. An admitted THINK/ACTION pair
   requires reciprocal role linkage and admission for both profiles.
2. Choose the matching role; THINK produces a genuine bounded native plan before
   ACTION. Keep plan binding, write scopes, independent review and idempotency.
3. Create genuinely independent tasks before waiting; shared write scopes and
   real dependencies remain serialized. Stay within existing host/account caps.
4. Wait for native completion events. Do not poll through the model or repeat a
   completed/unknown action to obtain proof.

`dispatch_admitted` is not provider availability or permission to run held work.
`readiness` is always `not_probed`. Current stop state, claims, quotas, provider
holds, task permissions and resource gates are rechecked by the existing native
execution paths. Saved settings do not change a live session's model binding.
There is no new model tool, background cache or prompt reload. Existing sessions
keep their prefixes; use the command when a new coordination task needs it.

Only live profiles named by this fleet's allowlist are read. With no explicit
allowlist, native legacy admission applies. The result is bounded to 64 entries;
`total_profiles` and `truncated` disclose an incomplete listing. A counterpart
outside the allowlist is `not_admitted` without reading its config. Corrupt or
incompatible data fails closed, without YAML contents or corrupt-backup writes.
Output is local metadata, not a public export of an owner's fleet.

## Verification and limits

The feature first failed six checks. Final focused selection: four files / 29
passed. Broader profile/workflow selection: 84 files / 738 passed / six existing
platform skips / zero failures and retries. The runs overlap and are not added.
Seven installed native CLI checks each on Linux and macOS pass with socket
connections denied, synthetic credentials and no model requests. They cover the
real parser/handler, native pair/admission metadata, effort ceiling, secret-field
exclusion and unchanged config. The old editor snapshot retains its default
behavior; the CLI supplies an explicit readonly diagnostic reader.

A representative synthetic real-provider coordination case is measured separately.
These offline checks alone do not prove fewer model calls, parallel bot completion,
original-user adoption, all family readiness or lower bills.

## Owning source launcher and real-case boundary

A fresh native coordinator used this command once, but its tool shell selected a
console script from the dependency venv's older build-time source snapshot. The
flag was rejected and the native worker correctly completed a capability block
after seven physical provider requests. No child task was created, the failed
card was not replayed, and no config-file fallback or quota bypass was used.

The terminal environment now gives its owning checkout's existing executable
launcher the same priority already given to a sealed payload's launcher. Other
user toolchain paths retain their order. This reuses the current published
launcher, without writing a shim, changing PM environment selection, exposing
Hermes PYTHONPATH to arbitrary programs or installing dependencies. Without an
owned executable, existing operator precedence remains.

Two real-shell regressions failed first, and the missing-launcher control passed.
The final integrated selection passed 835 tests across 88 files with eleven
existing platform skips, zero failures and retries. Installed actual-owner
terminal checks on Linux/macOS resolve bare hermes to the owning launcher,
run the real metadata command and preserve config. The original macOS Gateway
remains unstarted.

An artificial custom data root with no committed dependency environment correctly
refuses a managed store-Python launcher under the no-lazy-install guard. It is not
a provider failure or permission to create an environment. Isolated process-entry
CLI checks and actual-owner terminal checks are distinct evidence. Full parallel
bot coordination after this repair remains unproven; do not substitute metadata
visibility or a successful terminal command for a completed worker graph.
