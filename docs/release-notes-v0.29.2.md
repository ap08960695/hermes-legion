# Hermes Legion v0.29.2 — Save bot descriptions without a helper

## What you will notice

**Bots → Edit profile → Description → Save** uses the gateway's existing
profile writer. A supported gateway saves the description without starting a
separate Python CLI process. Reopening the editor shows the saved text,
including Thai characters and line breaks.

Save requires an explicit description-write acknowledgment. A rejected write,
missing acknowledgment or connection error keeps the draft and displays the
existing error. These failures do not trigger another writer automatically.

The previous CLI path remains only when the backend explicitly reports that
it lacks the profile configuration method. Its result must report code zero
and not be blocked. A backend that accepts the method but cannot acknowledge
the description write needs an upgrade; it is not treated as a successful save.
That legacy fallback can still start a CLI helper. No new backend method,
service, pool, dependency, connection or model call is introduced.

Apply the source kit to its pinned upstream base and rebuild Desktop through
the supported build path. This companion release does not replace the owner's
installed app. Keep a backend that supports description-write acknowledgments
for the helper-free path.

## Native Local acceptance

The retained v0.29.1 native image shows the CLI description write rejected by
the trial process guard. Matching editor baselines were checked; that unchanged
before case was not relaunched just to repeat it.

The corrected renderer was launched with a fresh isolated Local home and the
same process guard. A synthetic bot was created with introduction off. After
backing up its metadata and config, a Thai/English multiline description was
saved through the interface. The roster updated, Save closed successfully,
and reopening showed the exact text. Independent profile-file readback confirmed
the description and manual-description flag; all other metadata and the profile
config were preserved. Before/after native images measured 3010 by 1776 pixels.

The new launch passed its actual 60-second gate with zero SSH attempts or
executions and at most four sampled Hermes processes. Owned processes stopped,
the gateway port closed, and the original trial bundle and task root config
were restored. No prompt, inference or worker ran. Private images and receipts
remain outside the source release in the local work report.

## Regression and limits

Eleven editor component cases and nineteen SDK cases pass. Six new cases failed
on the previous writer. Coverage includes the scoped RPC payload, Unicode and
multiline text, rejected or missing acknowledgment, transport failure, explicit
legacy capability fallback and blocked/nonzero legacy results. The previous
draft-retention and appearance/advanced failure checks remain. Typecheck,
renderer build and scoped lint pass. Three changed patch sections apply, match
their hashes and reverse to the pinned base; unrelated sections are retained.

Legacy fallback has component proof, not a live older-backend test. Group
creation/membership, real worker lifecycle, owner-app adoption and Linux parity
remain unverified. No production RAM or latency saving is claimed.
