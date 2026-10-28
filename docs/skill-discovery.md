# Cycle-safe skill discovery

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
