# Complete Captain skill installation

An installed `SKILL.md` alone can look complete while its supporting delivery
reference is missing. A second Captain profile can also resolve an older copy,
or have no skill or goal permissions despite the main profile being configured.

The offline doctor accepts an explicit installed skill directory:

```sh
python3 scripts/legion_doctor.py --skill-copy "$CAPTAIN_HOME/skills/legion/goal-driven-execution"
```

Set `CAPTAIN_HOME` to the intended existing profile home before using this
example. Run separately for each intended Captain. The command hashes every
file in this release's `skills/goal-driven-execution` directory and compares
the corresponding installed files. `missing_files` and `different_files` name
relative paths; a mismatch exits 1. Extra owner files are retained and are not
validated by this comparison. The tool does not import Hermes, change files,
discover credentials or start a service or model.

A passing comparison establishes file parity only. `executed` remains false
and `runtime_ready` remains unknown. Native profile selection, skill discovery,
goal permission and actual use are separate checks.

## Adopt the complete directory

Review the installed copy before changing it. Preserve custom instructions and
owner additions; an unknown changed file needs review rather than replacement.
Copy the entire reviewed skill directory, including
`references/tracked-delivery.md`, into the intended profile's native skill
scope. Re-run the comparison and confirm native skill discovery resolves that
same copy. An entry file installed for a different profile is insufficient.

Use the existing [goal and decision policy](goals-and-delegated-decisions.md)
to opt in an authorized Captain. Both `goals.allow_self_management` and
`goals.delegated_decisions` belong to that profile. Keep existing goals, owner
pauses, turn caps, models, accounts and quotas. A pointer appended to an
existing SOUL keeps the detailed method on demand; it does not establish that
an existing cached agent has read it. Retain the current conversation prefix.

## v0.8.27 verification

Four regressions cover missing references, an older entry, a complete copy with
no runtime claim, and preservation of extra owner files. All 104 companion
tests pass. Actual native Python on Linux and ARM64 macOS passes the new CLI
comparison against the intended named Captain's installed two-file skill.

The reviewed two-file skill is installed in the intended named Captain on both
hosts. Native discovery, both goal flags and the SOUL pointer are checked for
the main and named Captain on each host. The Mac opt-in changes only the two
previously absent goal flags and appends the pointer; parsed unrelated settings,
existing SOUL prefixes, modes, ownership, extended attributes and saved goal
state are preserved. Linux permissions were already enabled.

The private bounded deployment checks pass four cases on each host, including
an owner edit after planning, a profile alias, normal opt-in, and metadata
preservation. Planned file hashes are rechecked before publication; unknown
owner edits are rejected. Mac config text is prepared with the native config
writer in private staging, then published while retaining the original file's
metadata. Staging copies are removed afterward.

The 974-path runtime patch and Desktop builds are unchanged. Both production
Gateways remain closed. No model request, real card dispatch or GPU work is
performed for this release. These checks prove installation and discoverability;
cached Captain adoption and unrestricted autonomous performance are not claimed.
