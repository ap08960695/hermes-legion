# Hermes Legion v0.33.8 — Keep attachment size edits when closing Settings

## What you will notice

In **Settings → Chat → Attachments**, edit **Max preview / image load size** and
press Escape while the number field is still focused. The limit now saves before
Settings closes. Previously the draft could disappear: a native 16 → 1 MB edit
reopened as 16, and no device cap file was written.

The cap belongs to this Desktop device, so profile switches show the same value.
The separate Image Attachments preference remains profile-specific. Enter and
moving focus keep their existing commit behavior. Empty input resets to 16 MB;
values below the minimum use the existing 1 MB floor. This fix does not recover
edits lost by an older build. Apply the consolidated source kit and rebuild Desktop;
the owner's daily app has not been replaced.

## Implementation and checks

AttachmentSizeSetting now blurs on non-composing Escape, matching the existing
list editor pattern. The blur starts the same commit before the overlay's window
handler unmounts the field. Both existing IME signals suppress this new commit;
the overlay's existing close behavior is unchanged. No cleanup-based save, new
parser, backend API, dependency, locale or schema change.

Ten rendered cases exercise the real Settings overlay and device store with an
IPC boundary fixture: valid, empty and below-minimum drafts, delayed completion
after unmount, Enter/blur controls, both IME signals, unrelated unmount and an
unchanged value. The backed production version fails four cases with 29 controls
passing; the fix passes all 33. Together with accessibility, device store and IME
cases, 76 checks pass across four files. Existing 23 React act-warning headers
also occur on the baseline; the new cases add none. Scoped lint, renderer types,
bounded renderer build and scoped health pass. Existing Vite warnings remain.

Only the two changed patch sections were checked against the pinned upstream
base with apply, after-hash, reverse and before-hash checks. Unrelated sections,
1088 targets and test selection remain. Unchanged broad source/mock suites were
not repeated. Companion unit, tracked-copy release and both secret scans are the
handoff gates.

## Native Local evidence and limits

On the before build, a focused 1 MB draft followed by Escape disappeared. On the
final build, the same action writes `{"maxMb":1}` before reopening Settings.
Reopening and selecting another Settings profile both show 1 MB. All three native
profile configs remain byte exact, including their modes.

The first final observer was interrupted before its closing statistics. Recovery
checked that every recorded process, guardian and port had ended, preserved that
raw evidence, and verified saved cap/config bytes and modes. Fresh processes then
reopened the same home, app data and exact signed diagnostic bundle, without
preparing or rewriting the fixture. The screen still showed 1 MB without another
edit, matching the saved cap bytes/mode. This is restart readback, not crash
durability evidence.

Before, final and reopened launches passed actual 60-second Local SSH-zero gates.
Completed before/reopened observers stayed at most four Hermes processes. The
interrupted observer has only its earlier 60-second resource sample, not final
statistics. All owned processes/ports and Computer Use ended; original device cap
absence and the 313-entry trial bundle/signature were restored. No Send, inference
or upload ran; session/message/delegation/hosted-room stores stayed empty. Owner
app/data, other machines, ESTOP, pauses and timers were untouched.

Actual attachment preview/rejection, Image Attachments mode effects, pending-read
races, native IME, crash/disk-full recovery, all Settings pages, daily-app adoption,
Linux/ai and cross-device transport remain unverified. Existing main-process write
failure reporting is unchanged. Earlier startup paint symptoms remain unresolved.
Resource observations are bounded samples, without peak-memory or savings claims.
