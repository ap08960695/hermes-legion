# Offline readiness, setup bundles and routing explanations

## Contract

Use only Python's standard library and explicit JSON inputs. Never import Hermes, read auth stores, authenticate, call a model, dispatch work or change a live profile. Native account pools, quotas, gates and session ownership remain authoritative.

- `legion_setup.py`: preview or export a selected subset of the registered team templates. Require non-placeholder model references, produce native JSON config fragments and generic SOUL files, and refuse an existing destination, symlinks and known live homes. Files contain no account mapping. No installer or executable adoption script is generated.
- `legion_doctor.py`: inspect explicit team/bundle inputs and optionally a pinned checkout through the existing read-only verifier. Report stable issue codes without echoing rejected values. Separate offline checks from unknown runtime/auth readiness. Refuse altered, missing, unlisted or linked bundle payloads and enabled fallback chains.
- `legion_plan.py --explain`: explain per-candidate role, privacy, capability, readiness, quota and cooldown rejection. Preserve the existing recommendation, reservations and pins; explanations do not execute work.

## Implementation plan

1. Add behavioral tests for export/preview, refusal without overwrite, integrity, placeholders, fallback, safe diagnostics and explanation equivalence. Observe failures before implementation.
2. Implement the bundle builder and doctor as small standalone tools, reusing existing team/schema and checkout validation. Use fresh private output directories and exclusive file creation.
3. Refactor the planner's eligibility predicate into reason codes and add an opt-in explanation view. Check the old output remains unchanged without the flag.
4. Run the full companion suite, documented commands on a fresh bundle, and native config compatibility checks on generated synthetic fragments in an isolated checkout.
5. Audit explicit public inventory, Git history and release payloads for private identifiers and credentials. Publish with the intended repository account and verify anonymous downloads. Compare live source/profile hashes afterward.

## Review focus

Existing destinations and linked ancestors must not be overwritten. Malformed or credential-bearing inputs must not be copied into errors. Unknown readiness must not become success. Optional diagnostics must not alter quota decisions. A bundle manifest is an integrity inventory, not proof of provider authorization or model capability.
