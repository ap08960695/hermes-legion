# Hermes Legion v0.33.7 — Report group membership save failures

## What you will notice

In **Bots → Manage team**, right-click a bot and choose **Manage groups**.
If Hermes explicitly refuses to save a membership, the dialog now explains that
its change is only on this device and offers **Retry**. The group name stays
available after a failed join. Previously it disappeared without a warning,
even though the dialog promised that memberships synced to every machine.

Retry repeats the failed membership change only when you click it. A different
group name typed later stays intact. Join, membership checkboxes and Remove from
all groups wait for their save and block overlapping changes. Successful feedback
follows settlement. Changes remain visible locally; no automatic retry or rollback
is added. Older gateways retain their existing local fallback.

Apply the consolidated stable source kit and rebuild Desktop. This patch does
not install a rebuilt daily app or repair canonical hosted-room membership editing.

## Implementation and checks

The existing per-Bot membership function now returns saveBotMeta's three-way
outcome. One dialog handler owns join, toggle, remove-all, pending controls and
feedback. An explicit failure stays visible until a confirmed full membership
write; an unsupported reply cannot erase it. Remove-all remains sequential.
The existing ErrorState and generic Retry label are reused. The plugin message
contract and all nine registered catalogs cover the new warning and conditional
sync description. No backend API, schema, dependency, model call or polling change.

Real rendered dialog, membership and metadata logic run against a scripted RPC
boundary. Initial red: four failures with two controls. Retry and retained-failure
checks then fail twice with five controls before their implementation. Final nine
regressions and 25 nearby cases pass: 34 across four files. They cover pending
submission, local fallback, denied joins/removals, final remove-all confirmation,
explicit Retry, later draft retention and Japanese feedback. Renderer types and
bounded build pass; scoped official health reports zero blocking/advisory findings.
Scoped lint adds no diagnostics: six errors and one warning match backed baseline
bytes. Existing Vite deprecation and dynamic-import warnings remain.

Five changed sections pass pinned-base apply/hash/reverse checks. The kit has
1088 targets, with one new Desktop test selected; prior selection ordering and
metadata remain. Unchanged broad source/mock suites were not repeated.

## Native Local evidence and limits

On the unchanged before build, Create & join checked a group and cleared its
name while the target profile folder denied writes. Its native profile metadata
stayed absent, and the UI gave no failure warning. On the final build, the same
failure shows the warning, retained name and Retry. Restoring only folder write
access leaves the file absent; clicking Retry creates the intended membership.

Three Local profiles then join two groups through the native UI. A denied removal
keeps the native file unchanged while the local checkbox changes and warning
appears. Explicit Retry saves the removal while retaining the bot's other group.
Remove from all groups then clears only that bot's remaining memberships.

All first writers and the guardian stop before fresh app/gateway processes reopen
the same home, app data and exact signed diagnostic bundle. The retained bot has
both selections checked; the removed bot has neither. All three native metadata
and config files retain their pre-restart bytes/modes. Group counts agree with
the saved profile mappings. No Send, model fixture, inference or hosted room runs;
session/message/delegation/hosted-room stores stay empty.

Before, final and reopened cohorts pass actual 60-second SSH-zero gates. Sampled
Hermes counts stay at most four; observer-inclusive RSS maxima are 895,795,200,
913,227,776 and 886,013,952 bytes. These are bounded samples, not continuous peaks,
physical RAM accounting or savings. All owned processes/ports end and original
profile/config baselines, denied folder modes and the 313-entry trial bundle with
strict signature restore. No owner app/data, other host, ESTOP, pause or timer changes.

This covers the existing per-Bot legacy metadata dialog. Canonical room membership
mutation, the standalone room member picker, cross-device transport, actual group
dispatch, daily-app adoption, Linux/ai, spoken VoiceOver and narrow-window coverage
remain unverified. Unsupported/unavailable gateways keep the previous fallback;
only an explicit failed save contract triggers this warning. Prior startup paint
symptoms remain unresolved; these two final launches needed no Reload, without a
cold-start reliability claim. Required companion, release and secret gates apply.
