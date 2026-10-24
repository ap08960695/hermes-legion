# Third-party notices

## Hermes Agent

The cumulative patch modifies or adds code relative to Nous Research's Hermes Agent. The upstream repository is https://github.com/NousResearch/hermes-agent and the compatibility base is pinned in `patches/manifest.json`. The upstream MIT license, including the copyright notice for Nous Research, is retained in `LICENSE`. Existing notices in patch context remain intact.

The companion documentation, role templates, verification tools and newly rewritten operating skills are distributed under that same MIT license. They are generic adaptations of operating practices; no private skill-library snapshot or third-party plugin bundle is included.

## Selective design inspiration

The feature catalog includes familiar agent-orchestration ideas such as compact recoverable handoffs, explicit write scopes and bounded completion checks. No oh-my-hermes installer, package or source bundle is included. This is an independent implementation using Hermes' existing interfaces.

## Verification tools

Gitleaks is used as an external local/CI scanner, not bundled as a binary. Its source and license are available at https://github.com/gitleaks/gitleaks. CI downloads an exact release with a pinned checksum. Python and Git are external prerequisites.
