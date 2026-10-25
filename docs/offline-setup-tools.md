# Offline doctor and setup bundles

These tools prepare and inspect files; they do **not** install profiles, authenticate, run Hermes, dispatch work or call a model. Only Python's standard library is needed. Run the commands from the Legion repository root. The shell examples target POSIX/Linux.

## 1. Inspect a team before setup

```sh
python3 scripts/legion_doctor.py --team examples/team.small.json
```

This intentionally exits **1** because the reference team contains `CHOOSE_EXISTING_MODEL_ID` placeholders. The JSON report identifies `model-placeholder` for each affected profile. Rejected JSON values, credentials and private paths are not echoed in diagnostic messages. It does not inspect native auth stores or discover actual accounts. Only explicit JSON inputs are supported; do not supply `auth.json`, `.env` or a raw production configuration.

A report has two separate outcomes:

- `offline_ready`: the requested, supported static checks passed. Exit **0** means those checks passed; exit **1** means invalid input or a failed check. Optional checks that were not requested are `unknown`.
- `runtime_ready`: always `unknown`. A syntactically valid model ID is not proof of authorization, available quota, tools or model availability. An intact bundle is not a live setup receipt.

A valid, explicitly supplied snapshot can be checked with `--team`, `--snapshot` and optionally `--now`. Stale/non-finite observations fail; the doctor does not refresh them. This checks schema and freshness, not actual provider balances or credential selection. Real dispatch must still use native readiness and quota gates. Never use the synthetic observation clock for real data.

## 2. Preview the five-profile starter team

The model names in `examples/models.small.synthetic.json` are fabricated for offline demonstration. They deliberately have no real account, provider entitlement or live-model acceptance claim. `CHOOSE` / `PLACEHOLDER` values are refused by the exporter; the synthetic `example-*` names demonstrate file formatting only.

```sh
python3 scripts/legion_setup.py --team examples/team.small.json --models examples/models.small.synthetic.json
```

Without `--output`, the tool prints JSON with `written: false` and a new-file unified `diff`. It writes no bundle. The diff includes config fragments, generic English SOUL instructions and an integrity inventory. It contains no account/credential map or quota snapshot.

For a real preparation, create a private model-map JSON **outside this repository** with the same profile IDs and supported model IDs from already authorized routes. Do not put tokens, emails, account identities or endpoint secrets in that file. The exporter rejects unknown model-map keys, secret-shaped fields in team inputs and obvious credential prefixes used as model names; these checks are not a replacement for reviewing your own inputs. It does not verify or add provider access.

The exporter supports subsets of the 34 registered templates. Select profiles in a private copy of the team file, retain its schema/policies and valid account references, then supply model references for those profiles. Changing a registered template's role/provider is refused. Account aliases remain planner metadata and are **not exported** into native config. A `--models` value overrides that selected profile's model field; other fields are never merged from a real profile.

## 3. Export into a fresh directory and inspect it

Choose a new directory under an existing private parent, outside both the Legion checkout and your live Hermes home. This block refuses an existing destination; pick another name instead of removing data.

```sh
export LEGION_BUNDLE="$HOME/hermes-legion-preview"
test ! -e "$LEGION_BUNDLE"
python3 scripts/legion_setup.py --team examples/team.small.json --models examples/models.small.synthetic.json --output "$LEGION_BUNDLE"
python3 scripts/legion_doctor.py --bundle "$LEGION_BUNDLE"
```

The destination is created with mode `0700`, files with `0600` (a stricter umask may restrict these further). Existing destinations, linked ancestors, the Legion checkout, the default home and an explicit `HERMES_HOME` are refused. The tool does not discover every possible custom deployment location: choose your output parent carefully. It reserves a fresh directory exclusively and never overwrites files. An I/O failure can leave an incomplete new bundle; doctor will refuse it. Do not retry into that directory.

Each selected profile receives `profiles/<profile-id>/config.example.json` and `SOUL.md`. JSON fragments are also valid YAML, but no native `config.yaml`, credential store, service file, executable installer or restart script is generated. Config contains only the chosen model/provider, `fill_first` pool strategy and empty current/legacy fallback chains. Native quotas, concurrency caps, account ordering, session/model bindings and project gates are not copied or changed.

Doctor checks the exact file inventory/hashes, recognized profile identity, model syntax/lane, generic SOUL content and disabled fallback policy. Missing, altered, unlisted or symlinked payload files fail. Rehashing an enabled fallback into the manifest does not bypass the semantic checks. The manifest is an integrity inventory, not a digital signature or a secret scanner.

## 4. Optionally check source compatibility

Only point this check at an isolated checkout prepared by the [installation guide](installation-and-rollback.md). Base and installed are different source states; the verifier deliberately refuses unrelated modified or untracked files.

```sh
python3 scripts/legion_doctor.py --bundle "$LEGION_BUNDLE" --checkout "$HERMES_CHECKOUT" --phase installed
```

Use `--phase base` before applying the patch. This runs only the existing checkout verifier's read-only Git commands and file hashes; it never imports Hermes. Git filesystem-monitor helpers, external diff/text conversion, lazy fetching, interactive prompts and optional index locks are disabled for inspection. A different revision or changed target fails, rather than triggering an update/install.

## 5. Review and adopt separately

Review the generated diff and files. If an operator chooses to deploy them, follow the [native fresh-home setup recipe](setup-multi-account.md), create only the selected fresh profiles, set individual config keys and copy the corresponding reviewed SOUL. Do not replace a full existing config with a fragment. Preserve all native caps and pool ownership; a recommended planning account does not pin the actual native credential.

Actual authentication, runtime lifecycle and real-bot acceptance are separate operator-controlled steps. No workflow here restarts an existing worker, raises quota, retries inference, uses paid fallback or touches a local model/service.
