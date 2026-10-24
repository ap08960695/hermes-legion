# Security policy

Never include credentials, tokens, private keys, cookies, prompts or production logs in a public issue, pull request or CI attachment.

For a potential Legion vulnerability, use this repository's private vulnerability-reporting facility if enabled. If no private reporting channel is available, do not disclose exploit details publicly; request a private contact without including the details. Security issues in upstream Hermes must follow the [upstream security policy](https://github.com/NousResearch/hermes-agent/security/policy).

The patch and role instructions operate inside Hermes' existing trust envelope. Prompt rules, quota policies, completion checks, diagnostic redaction and scanners are not an OS security boundary. Use appropriate process/container isolation for untrusted work.

This kit stores no shared account or API credential. Configure your own authorized authentication outside this repository. Do not add real credentials even for a test. A detected leak must block publication; deleting a file in a later commit does not remove it from history, and a publicly exposed credential requires revocation through its issuer.
