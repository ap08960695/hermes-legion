# Skill discovery and declared-name preflight

## v0.7.5: preserve native skill aliases on cards

A skill's declared frontmatter name can differ from its folder name. The normal
loader accepts that alias, but Kanban previously dropped it while creating the card.
Preflight now retains the requested alias and order. Ordinary directory names keep
the existing path that reads no skill bodies. When a requested name is unresolved,
preflight reuses the native catalog cache and its collision/precedence resolver.
It does not build another cache or registry, and multiple requested aliases share
one catalog read. The owner-resolved roots are passed explicitly; target-profile
config, external libraries and frozen-worker isolation remain native.

Multiple symlink views of the exact same resolved file now produce one canonical
alias owner in the catalog, matching the loader. Different files with equal names
still require the native ambiguity/precedence decision. The index can still expose
independent views. Existing project trust and quarantine traversal stays in place.

The existing catalog's 30-second freshness interval and explicit reload invalidation
apply to in-place metadata edits. Preflight is an installed-skill hint, not a grant
to execute disabled providers, bypass role/review gates or change a worker's tools.
It asks for hidden metadata without running platform/app offer checks; normal list
and UI filtering keep their existing rules. No prompt or conversation is rebuilt.

### Current evidence and tradeoffs

The final 26-file Python selection passed 472 cases, zero retries, including real
registry/SQLite alias persistence, profile separation, symlink identity, ambiguity,
metadata reload, and avoiding repeated metadata reads. Native code-health comparison
against the exact previous public source passed with no findings. Strict scoped
lint has no new findings; the existing unrelated Kanban finding remains.
Installed source on Linux and macOS each passed 17 native controls in isolated homes,
with network denied and zero inference. Host/repeated selection counts overlap.

A same-runtime Python 3.14.9 synthetic fixture timed 25 warm calls per case. Ordinary
names remained roughly comparable: median 0.756 before / 0.765 ms after. Four valid
aliases, previously all dropped, were all kept. Warm alias/missing-name checks used
zero skill metadata reads and took about 1.38 ms. The discarded first prototype
reread metadata every time and took about 21 ms; it was never installed.

An existing-profile read-only check with one real directory name and one synthetic
missing name timed 50 calls per version: warm median about 0.923 before / 1.691 ms
after. The first cold request enumerated 162 / 569 directories respectively because
alias fallback now populates the existing catalog. This correctness work has a
metadata cost; it is not evidence of faster overall workloads, lower token usage,
higher provider cache hits or lower RAM. Original user-session/provider adoption
remains unproven. No production board or conversation was used in these measurements.

## v0.7.4: cycle-safe traversal

The native skill index, catalog freshness signature and Kanban skill preflight now
share one directory traversal. A symlink back to an ancestor is pruned before the
directory is enumerated. Identity uses the physical device/inode, with a canonical
path fallback when an inode is unavailable. Identity is branch-local, so two
independent aliases of the same shared skill directory remain visible.

The traversal retains the native excluded-directory and support-directory rules.
Dependency trees and a skill's supporting references are not promoted into usable
skills by Kanban preflight. Ordinary deeply nested skills remain discoverable; the
index has no new arbitrary depth cutoff. The catalog keeps its existing six-level
signature scope and 30-second freshness interval, and still detects new installs.

No model request, eager skill-body loading, new cache, registry or dependency is
introduced. Profile boundaries, existing trust checks, role/review gates, account
selection, quotas, reasoning limits and fallback behavior remain unchanged.

## Evidence

A 25-file Python regression selection passed 463 cases with zero retries. It covers
branching cycles, independent shared aliases, deep trees, freshness, target-profile
preflight, frozen workers, project skill trust and existing skill guards. Counts
from overlapping test selections are not added together. Strict scoped lint reports
no new findings; an existing unrelated Kanban lint finding remains.

The actual installed source passed 11 native registry/config/SQLite and traversal
controls on each of Linux and macOS, in isolated synthetic homes with network calls
denied and zero inference requests. The same controls on two hosts are not summed
as independent feature coverage. This backend change does not require a UI rebuild.
Use the native idle update path for a running backend; do not interrupt workers.

## Measurements and limits

One synthetic fixture contains a real skill, 250 support archives and 250 dependency
chains. On the same Python 3.14.9 runtime, 25 timed warm preflight requests changed
from 1,004 to 2 directory enumerations per request. Median time changed from about
3.201 to 0.495 milliseconds; P95 changed from about 3.309 to 0.505 milliseconds.
These are directory enumerations, not all filesystem operations: physical identity
checks still require metadata reads. They are fixture results, not user-workload savings.

A separate read-only check of an existing configured profile made 50 requests before
and after installation. Total directory enumerations changed from 226 to 162, while
median time remained roughly comparable: about 0.973 to 0.943 milliseconds. No
production task, conversation, skill body, credential or model output was recorded.

These checks do not prove lower tokens, higher provider cache hits, lower RAM use,
overall latency gains or adoption by an already open original user session. No
provider-backed work was started to manufacture that evidence.
