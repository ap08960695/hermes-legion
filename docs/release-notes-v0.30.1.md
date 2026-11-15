# Hermes Legion v0.30.1 — Clean saved background reports

## What you will notice

Opening a saved background-task report shows its task outcomes, partial output
and result without the canonical gateway notice or trailing internal transcript
path. Process completion logs also close their wrapper correctly. This fixes
unwanted implementation text seen on the native Local app in v0.30.0.

Apply the source kit and rebuild Desktop. This is a renderer-only bug fix; the
kit does not replace the installed app or restart existing work. Previously
saved native reports benefit when their framing matches the canonical format.

## Behavior and compatibility

The gateway appends a machine-provenance notice for the model. The report parser
expected a transcript path at the end, so the appended notice prevented that
cleanup. It also caused the process parser to remove the notice's closing bracket
instead of the process wrapper's bracket.

The fix removes one exact terminal gateway footer from recognized producer
envelopes in the local display input before the existing parser runs. It retains
the upstream whitespace normalization. Unwrapped legacy reports, embedded notice
text, near matches and text followed by an additional suffix keep their existing
treatment. The exact EOF notice is reserved provenance within producer envelopes;
this does not add structured report framing or a general text scrubber.

Stored history, model notification content, per-child outcome metadata, caching,
backend authority and control are unchanged. No model request, dependency,
configuration, API or database field is added. Arbitrary paths or similar prose
inside a child's actual report remain report content.

## Verification and limits

Seven new cases include three genuine failures on the original implementation
and four preservation controls. All ten nearest tests pass, including the three
existing cases. Scoped lint, renderer types and build pass; the pre-existing
Vite dynamic-import warning remains. Two changed source/test sections pass
pinned-base apply/hash/reverse checks; the other 1077-target kit sections and
explicit test selection are retained without an unchanged-suite resweep.

Native acceptance opened a SQLite backup of the genuine v0.30.0 two-child
completion in a fresh isolated Local home, using the rebuilt renderer. The same
report kept both outcome/name pairs, partial output and successful result while
hiding the terminal trace and notice. The source database hash and copied row's
content/metadata stayed exact. Message count/API accounting were unchanged;
no new Send/model work was submitted. Cross-home live resume was refused by the
existing profile guard (profile_mismatch); this acceptance covers reading saved
history, not resumed work or a new delegation lifecycle. The original warning
capture is retained separately from the final report screenshot.

The actual 60-second launch gate had zero SSH attempts/executions. Across 1120
samples, Hermes process count stayed at most four and RSS including the observer
peaked at 989,478,912 bytes. Samples can miss transients and do not measure physical
RAM or production savings. All owned processes stopped, the gateway port closed,
and the original 313-entry trial bundle, strict signature and exact baseline
config were restored. Owner data, other machines and existing stops were untouched.

Whole native suite, daily-app adoption, Linux parity, cross-home resume, live
pre-Reload completion-summary visibility and production efficiency remain open.
