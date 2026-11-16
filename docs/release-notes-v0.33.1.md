# Hermes Legion v0.33.1 — Confirm config imports after saving

## What you will notice

Settings → Actions → Import config now says **Config imported** only after the
current native save acknowledges success. Cancelling toolset removal or receiving
an autosave failure no longer produces a success message. The existing save
failure still explains how to recover; restore write access and import again.
JSON must contain an object before it can change the draft or submit a write.

Apply the source kit and rebuild Desktop. This bug-fix release does not replace
the daily Mac app or change native autosave ordering, route ownership or retries.

## Implementation and verification

The shared Settings editor returns the acknowledgement from its existing save
chain, including its version and mount/profile-generation checks. Import awaits
that result. A cancelled confirmation, failed save or superseded completion
returns false. An admitted save can still update its captured cache after the
view unmounts, without a stale import toast. No second writer, state store,
dependency, locale, API or backend change is added.

Eight new cases fail before implementation, with eight cases passing. The final
nearest selection passes 68 tests across Settings import/autosave, config helpers,
Actions and the config cache. Cases cover deferred success, rejection, ok:false,
cancelled removal, a newer field edit, unmount/cache acknowledgement and invalid
JSON root shapes. Scoped lint, renderer typecheck and build pass. Existing React
act warnings and the unrelated dynamic-import build warning remain. The first
typecheck caught a required notification message field; the final code follows
the existing empty-message pattern. Two changed sections pass pinned-base
apply/hash/reverse; 1085 targets and the test selection remain unchanged.

Native Mac acceptance uses a fresh Local-only home and the rebuilt renderer.
Before, a success toast appeared while destructive toolset confirmation was
still open; Cancel preserved the original config. After, confirmation and Cancel
showed no success. Making only the test config directory unwritable produced a
real native atomic-write PermissionError and actionable Autosave failed message,
with unchanged disk bytes and no import success. Restoring test-folder access and
retrying saved the checkpoint toggle and Memory Budget 2901. Readback preserved
all prior unrelated keys. Reopening Settings showed 2901 and the original memory
toggles/Profile Budget. A repeated import captured the five-second success toast
after the first successful retry's toast expired before capture.

The final launch passed a real 60-second SSH-zero gate; the whole run sampled at
most four Hermes processes and 928,481,280 bytes RSS including its observer. These
are sampled bounds, not continuous peaks or a production memory improvement.
The native database stayed empty: no Send or model request ran. All final owned
processes ended, the gateway port closed, and config bytes/modes plus the original
313-entry trial bundle and strict signature were restored. The baseline guardian
was absent on resume; its recorded identities, closed port and unchanged config
were checked independently before restoring the bundle. No normal baseline
controller-exit claim is made. Screenshots and private receipts remain outside
the public kit. Owner data, other hosts, ai, ESTOP, pauses and timers were untouched.

## Limits

Only Local native acceptance is established. The owner's daily app, ai/Linux,
full Settings coverage and production savings remain unverified. Partial imports
can temporarily display omitted fields as empty until Settings reopens; native
disk keys are preserved. That adjacent draft-display issue remains open. Existing
in-memory autosave retention still cannot survive a forced process termination.
