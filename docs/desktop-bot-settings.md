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

## Creating and reopening a Local group

Open **Bots → New group chat**, select two to six bots from the same Local
authority, name the room and choose **Create Group**. One selected bot leaves
Create disabled. Cancel leaves no room behind; reopening resets the draft.
Creating a room does not send a message. Sending is a separate action that can
run the selected bots through their existing model routes and quota.

For a backend with canonical groups, the room stores its initial members on
the gateway authority. Return with **Back**, choose **Manage team**, then click
the saved group name to reopen it. The bot cards' **All groups** filter and
legacy **Manage groups** metadata are separate from canonical room membership.
The canonical room displays its members but offers no membership-edit control.
Creating the initial roster does not prove later add/remove support.

Native Local acceptance used a fresh isolated home and the v0.29.3 renderer.
A synthetic bot was created with introduction off, then joined the default bot
in a new room. Independent read-only SQLite inspection confirmed exactly one
room with both Local profile targets. After Back → Manage team → saved group,
the same room ID and complete membership remained. A cancelled one-member draft
had left the room and event tables empty. Profile metadata/config stayed
byte-identical during group operations; background runtime files are separate.

The completed launch passed an actual 60-second gate with zero SSH attempts or
executions, at most four sampled Hermes processes and sampled RSS below 4 GiB.
Owned processes stopped and the original trial bundle/config were restored.
No group message, model run or worker task was created; native event, session
and driver-task tables remained empty. Screenshots and private readback receipts
are retained in the local work report, outside this source kit.

This proves creation, cancellation and in-app reopening for the controlled case.
It does not prove restart persistence, canonical membership editing, active
worker monitoring, owner-app adoption or another backend. No runtime source
changed in this acceptance round; no new version or performance saving is claimed.


## Naming a saved Local room (v0.31.0)

Open the room, choose **Rename**, edit **New name**, then **Save**. A blank name
cannot be saved; Cancel leaves the saved room unchanged. Successful confirmation
updates the room header and main-tab caption while keeping the current unsent
chat message. **Back → Manage team** lists the saved name for reopening.

The control uses the existing gateway `groups.rename` contract for the room's
canonical ID and authority. It appears only if `groups.capabilities` advertises
that method. Readback must match the requested name before the editor closes.
Errors keep the draft; an unchanged explicit retry in the open editor reuses its
event ID. There is no automatic write retry, new room, member change or model call.
This does not add a concurrent-edit lock. Cancelling/reopening starts a new edit.

Rebuild the complete Desktop source kit, including the SDK caption update. An
older Desktop SDK retains its previous tab-caption behavior until reopening.
The earlier creation-only acceptance above remains historical; see the
[v0.31.0 notes](release-notes-v0.31.0.md) for the current workflow proof and limits.
