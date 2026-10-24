# Multiple accounts without multiplying quota

## Native storage remains authoritative

Use Hermes' existing credential pools. They hold multiple credentials for one provider; cross-provider fallback is a different mechanism and remains disabled in the fragments. A paid subscription already authorized by an operator is not the same as introducing metered paid fallback. Legion adds neither an account store nor an authentication proxy.

There are two native arrangements:

1. **Shared root/provider pool:** several role profiles borrow the existing root pool. Different roles and Web/native variants can consume the same underlying account. Never count each profile as having a separate quota.
2. **A profile-owned provider pool:** authenticate explicitly inside a fresh profile when it genuinely needs its own independent account. That provider's local login takes precedence over the borrowed root login. Do not copy or symlink single-use OAuth token files to manufacture independent credentials.

See the pinned upstream [profile guide](https://github.com/NousResearch/hermes-agent/blob/d923a5eb487a17c0a68801bba9ef0f56c81040a8/website/docs/user-guide/profiles.md) and [credential pool guide](https://github.com/NousResearch/hermes-agent/blob/d923a5eb487a17c0a68801bba9ef0f56c81040a8/website/docs/user-guide/features/credential-pools.md). Provider-specific exceptions remain authoritative; not every provider supports independent account pools.

## Role → profile → pool → account

`examples/team.full.json` uses aliases such as `account-codex-a`, `principal-codex-a` and `local-label-codex-a`. These are invented reference labels. `auth_scope: root` describes the operator's native root/provider pool; it is not a path and is not a new Hermes config setting. `credential_ref` is a local label/handle to resolve during native setup, never a token.

For an actual installation, privately map each alias to a native account identity and its quota scope. Two logins or aliases of one underlying account must retain the same `principal_ref` and `quota_group`. The validator rejects a split group for the same principal or a duplicate provider/auth-scope/credential handle. Different native labels can still refer to the same real account: an operator must canonicalize that identity using native metadata. An offline file cannot authenticate or discover that fact.

A profile's account list is a **planning allowlist**, not a native `config.yaml` field. The planner may recommend one account; Hermes' native pool still decides the actual credential. `fill_first` alone does not pin a named credential, restrict a pool to the planning allowlist or enforce a reservation. Confirm native pool ownership and selection before treating a recommendation as executable. Do not add unsupported account-selector keys to Hermes configuration.

## Session stability

Keep the existing profile/account recommendation for a continued session. The offline planner accepts a separate pins file; if a pinned account is unavailable or cooling down, it holds instead of silently moving the conversation. New sessions can use other already authorized healthy accounts. Running work is always left alone.

Changing accounts/routes mid-conversation can affect cache reuse. A pin expresses a preference, not a guarantee of provider-side cache retention or actual native credential affinity. Native safety, expiration and provider limits still take precedence. Do not force a model restart, refresh a token or issue an allowance probe to test a pin.

## Private-data boundaries

Public-only routes cannot receive confidential tasks. Use a private-data route only when the operator's project/provider policy permits it. Templates do not certify any provider's data handling. Keep real account identifiers, emails, credentials, usage snapshots and pins outside the repository. Do not publish a native `auth.json`, `.env` or copied production profile.
