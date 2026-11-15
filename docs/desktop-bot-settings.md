# Visible bot model settings

Open **Bots → Edit profile** to review identity and model settings. The form keeps
Mode and provider/model/effort above the expanded role, family and counterpart fields.
The existing [per-model effort ceiling](reasoning-effort-limits.md) stays visible in a
compact window, including a profile already configured as THINK or ACTION.

Avatar, color, upload and manual image-generation controls are retained in a native
**Appearance** disclosure. Expand it when changing the look; opening that disclosure
does not invoke a model. Title/description, role pairing, advanced settings and the
sticky Save/Cancel footer retain their existing writers and ownership checks.

This is a presentation change. It does not change a model, effort policy, account,
quota, worker, prompt, tool list, dispatcher state or fallback. Existing backend
effort-limit enforcement is independent of whether a renderer has loaded the new form.

## Verification scope

The old editor reproduced the compact first-open clipping with an assigned role.
The repaired native packaged apps were checked using synthetic profiles and retained
messages, with no provider inference. Acceptance includes a compact initial opening
after fonts settle, reading the ceiling, low/high Save and reopen, another model
retaining max, Appearance disclosure, navigation, Workflow upstream selection, Hub
save and History reopening. Build/typecheck and native local signature verification
are separate checks. Earlier Python policy-suite counts are unchanged baseline
evidence, not a rerun for this presentation-only change.

Source application, an installed packaged app in an isolated home, an existing user's
window/session and provider-backed execution are separate evidence. No workload
usage or RAM percentage improvement is inferred from these interface checks.


## Recovering from a partial save

From v0.29.1, a failed description, appearance or advanced write keeps Edit
profile open with its draft and Save available. Existing error messages remain;
success and close require all attempted sections to succeed. The older-gateway
appearance fallback still counts as supported. Correct the draft or retry
explicitly; successful sections may already be persisted, with no rollback.

Native Local acceptance created a synthetic bot with introduction off, reopened
its saved profile, and exercised the same rejected description write before and
after the fix. The corrected form retained the draft; a subsequent title-only
Save and reopen passed. New group chat → Cancel returned to Bots. No prompt or
inference ran. Successful native description execution and group creation or
membership changes remain unverified. See the [release notes](release-notes-v0.29.1.md).
