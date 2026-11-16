# Hermes Legion v0.33.6 — Announce compact bot work correctly

## What you will notice

In Bots → Manage team, a compact bot's accessible name and name tooltip now say
Working while that available bot has eligible work. Previously the button could
say Ready even while its child task was running. When no eligible work remains,
the row returns to its existing connection status. Unavailable sources keep their
unavailable status. The bot's conversation preview and click destination stay intact.

Apply the consolidated stable source kit and rebuild Desktop. This patch does
not install the rebuilt owner's daily app or change backend activity eligibility.

## Implementation and checks

BotRow already derives an exact-owner mood for its face. A small local status
function lets the existing rowTooltip use the existing translated Working label for an available, non-idle mood;
otherwise it keeps the source label. The same string supplies the button name
and name tooltip. No new state, polling, request, API, locale, dependency or
worker lifecycle mutation. Availability and worker-recency rules remain unchanged.

Two behavior failures reproduce missing group/worker work names while 12 controls
pass. Tests render the real BotRow and mood derivation: one ended worker cannot
hide another eligible worker; all-ended and stale observations restore Ready;
a group turn updates only its exact source owner; unavailable status wins even
when group state gives the bot a non-idle mood. Preview and canonical-open checks
remain covered. Final nearest selection: 46 passes across four files. Scoped lint,
renderer types and bounded build pass. The inherited alias-test act warning and
ineffective dynamic-import build warning remain.
Two changed patch sections pass pinned-base apply/hash/reverse; 1086 targets and
test selection remain unchanged. Scoped upstream health comparison has no
blocking or advisory findings; BotRow retains its existing complexity cap.

## Native Local evidence and limits

The retained unchanged before build's native compact button says Ready while a
real child runs. The final rebuilt artifact says Working for that child's row,
still Working after its normal heartbeat and Refresh, then Ready after native
completion and parent delivery. Clicking the row reopens the same canonical
Bot Chat ID; parent previews and child detail stay separate. One actual Send,
one child and four controlled loopback model calls; no lifecycle rows seeded.
Only model content/timing is simulated. Native AX names are verified alongside
screenshots; spoken VoiceOver and independent tooltip interaction were not tested.

The final artifact initially stalled on Not connected. One native View → Reload
restored Connected before any Send, model call or stored session. Startup cause
remains unresolved; this patch does not claim cold-start reliability. The working
status flow then passes on the same process/build. Earlier intermediate native
proof remains separate from final-artifact acceptance.

The final actual 60.083-second SSH-zero gate passes; 1,923 bounded samples stay at
most four Hermes processes, with observer-inclusive RSS 1,217,249,280 bytes. An earlier
intermediate cohort also passes 60.125 seconds and closes normally. These are
samples, not continuous peaks, physical RAM or production savings. Both cohorts
end all owned processes, model threads and ports, then restore original config
bytes/modes and the 313-entry trial bundle with strict signature. No owner app/data,
other host, ESTOP, pause or timer changes. Required companion, tracked-copy release
and exact secret gates apply before driver handoff.

Legacy backends, real providers, managed subprocesses, daily-app adoption,
remote/ai, Linux and full accessibility acceptance remain open. Existing work
eligibility and source-status reporting remain the boundary for this label.
