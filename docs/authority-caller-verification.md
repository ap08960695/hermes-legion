# Additional authority caller verification

The profile-custody release's lifecycle/storage selection was scoped; it did not
cover every direct caller of session authority initialization. An additional
122-file offline selection initially passed 661 cases and failed 58. Running the
17 failing files on the previous runtime produced the exact same set of 58
failures, so these are not new cancellation-fix regressions.

Seventeen test files now match the native contracts without changing runtime code:

- Config-loader doubles accept the native optional `config_path` parameter. The
  real loader still reads the owning profile's path; no TypeError fallback or
  profile-isolation bypass is added to production.
- The fallback-secret control explicitly disables external login adoption in its
  synthetic config. Its intended premise is an unavailable primary, not whichever
  Claude CLI login happens to exist on the developer's machine. The native frozen
  fallback chain, rotation refusal and credential assertions remain tested using
  loopback FakeLLMServer instances only. No real model or paid fallback is used.
- Client-environment cases assert that client versus daemon toolchain entries stay
  isolated, while allowing Hermes' documented launcher directory to be prepended.
  Locality, secret filtering, environment, prefill and plugin-warning assertions
  remain in place; the production PATH sanitizer is unchanged.

The final additional selection passes 719 cases in 122 files, zero
failures and zero file retries. The focused 17-file run overlaps that result and
is not added to it. Code-health is clear. Earlier lifecycle/storage test counts
are separate historical evidence, not a combined or whole-project green claim.

Only these test files are synchronized to the Linux and macOS source installations.
No Gateway restart, Desktop rebuild, model/account/quota/effort/fallback change or
user-database operation is needed. The earlier installed seven-stage native
custody controls on each host remain the runtime evidence; unchanged acceptance
is not replayed just to increase counts. The original macOS Gateway stays stopped.
No RAM, token, cache-hit or generation-latency improvement is inferred from fixing
these test fixtures.
