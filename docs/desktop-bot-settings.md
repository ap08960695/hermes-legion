# Visible bot model settings

From v0.29.3, long provider/model selections stay inside their own dropdowns,
leaving both arrows visible. Keyboard focus shows the full name in the existing
tooltip. Native Local wide/narrow layout and both menus' Escape behavior were
checked without changing or saving a model. See the
[release notes](release-notes-v0.29.3.md) for adoption and verification limits.

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
inference ran. That v0.29.1 check did not exercise successful native description execution or
group creation/membership. See the [release notes](release-notes-v0.29.1.md).


From v0.29.2, description Save uses the existing scoped gateway writer and
requires `applied.description === true`. False or missing acknowledgment and
transport errors retain the draft. Only an explicitly missing RPC method uses
the previous CLI path, which must return code zero and not be blocked.

Native Local Save/reopen now passes with the unchanged subprocess guard:
Thai/English text and line breaks persisted, with independent metadata readback
and unchanged profile config. No prompt or inference ran. An older backend that
cannot acknowledge description writes needs an upgrade. See the
[v0.29.2 release notes](release-notes-v0.29.2.md) for compatibility and limits.
