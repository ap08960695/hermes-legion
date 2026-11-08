# Private auxiliary OAuth refresh fixtures

The auxiliary credential-refresh test mocked credential reads, the refresh POST
and credential persistence, but left the native cross-process lock at the default
Claude Code login path. Protecting the real home made the test fail before the
mocked refresh was reached.

The fixture now sets the existing `CLAUDE_CONFIG_DIR` to its own `tmp_path`
before computing the client-cache key. It exercises the real native lock inside
that directory and keeps every refresh, write and cache-eviction assertion.
Production authentication code, shared-login behavior, provider selection and
retry policy are unchanged. The oversized test file shrinks by two lines.

The public clone walkthrough also pins v0.8.31, correcting its older v0.8.10
reference. Historical releases and their original assets remain available.

## Native checks

The original refresh case fails on Linux and ARM64 macOS when the real home is
protected. After the fixture change, all **245 tests in the same three native
auxiliary files pass on each host**, with one test worker and no file retries.
The 15 failures recorded in the older auxiliary-floor selection are included in
these files and no longer reproduce on the current source. The older 74-file
result remains historical; this is not a rerun of that selection or the entire
native suite.

Both hosts use matching isolated source checkouts and separately managed test
environments. Their 976 pinned paths match the installed kit. macOS also keeps
Git control metadata outside the protected installation; only runner scratch
and timing-cache locations are redirected. Real-home I/O guards, refresh/write
mocks and the native test assertions remain in place. Earlier macOS harness
refusals are retained and are not counted as passes.

The complete test runs observed sampled descendant-process RSS peaks of about
256.6 MiB on Linux and 281.0 MiB on macOS, including child process groups. These
are test-resource observations, not production RAM improvements. Networking
was denied and Linux GPU devices were unavailable. No model request, real card,
Gateway or application window was started.

The reviewed test file is installed on both hosts with its mode, owner and
extended attributes preserved. A small patch supports verified rollback.
Production configuration,
credentials, saved goals and held work are unchanged. The runtime source and
Desktop builds do not change; the pinned source manifest updates only this
existing test path.

## Static-check boundary

The changed fixture passes pinned Ruff and the code-health ratchet without a
new finding. Full native `scripts/check` is **not globally green**: the source
already has 41 Ruff findings and 16 Windows-footgun findings. The files carrying
the Ruff findings are byte-identical to the base of this fixture change; no
finding is suppressed. Those repository-wide findings remain separate work.
