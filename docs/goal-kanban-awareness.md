# Goal waiting across followed Kanban boards

A session's goal judge already receives a count of followed running, ready and
todo cards. The old reader opened only the selected board with a writable
connection. A goal following work on another registered board could therefore
see zero pending work; probing an empty or legacy home could also create or
migrate a database just to read that count.

The reader now discovers live boards through the native registry in the current
fleet, counts distinct followed tasks per database through read-only SQLite,
and deduplicates database aliases. It sees committed WAL rows without requiring
a checkpoint. Missing databases or legacy tables count as zero without schema
initialization. A corrupt or unavailable sibling database does not discard
healthy board counts. SQLite lock waits are bounded to 100 milliseconds per DB;
this is not a fleet-wide elapsed-time guarantee.

Explicit database pins, dispatched/delegated worker contexts and machine board
fences retain the original one-board resolution and skip fleet enumeration.
Archived boards and unrelated session IDs are excluded. Other homes and profiles
are not searched. Active statuses and notification ownership rules are unchanged.
This advisory count neither dispatches work nor grants a completion, review,
publication, provider, account or quota waiver. Discovery failure still degrades
to zero; it is not evidence that work completed.

The regression originally failed six cases with seven controls passing. The
final 15-file goal/board/notification selection passes 290 cases with no failures
or retries. Native acceptance uses production Python, actual installed modules,
real isolated SQLite data and a controlled judge decision: followed work is
visible and an already parked goal does not rejudge on three follow-up checks.
There are no external requests or model calls. This proves the read and parked
state mechanics, not an autonomous bot graph, original-session adoption, actual
production usage savings or all-platform runtime parity.

Linux and macOS installed acceptance each pass ten checks. The original macOS
Gateway remains stopped. Use an idle native update/reload or a fresh eligible worker; never
interrupt an active task merely to adopt this repair. Keep existing backup and
rollback custody until the remaining host checks are verified.
