#!/usr/bin/env python3
"""Preview or export generic setup fragments. Never install or authenticate."""
import argparse
import difflib
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys

from legion_plan import fields, read_json, validate

ROOT = Path(__file__).resolve().parents[1]


def model_reference(value):
    if (not isinstance(value, str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_./:-]{0,159}', value)
            or value.endswith('/')
            or any(word in value.upper() for word in ['CHOOSE', 'PLACEHOLDER'])
            or re.match(r'(?i)(sk-|ghp_|github_pat_|hf_|eyJ)', value)):
        raise ValueError('choose a non-secret model reference')
    return value


def registry():
    team = read_json(ROOT / 'examples/team.full.json')
    validate(team, {}, [], {})
    return {p['id']: p for p in team['profiles']}


def registered(profile, known):
    fields(profile, {'id', 'role', 'provider'}, {'id', 'role', 'provider'})
    base = known.get(profile['id'])
    if not base or any(profile[k] != base[k] for k in ['role', 'provider']):
        raise ValueError('unsupported template')
    return base


def soul_path(profile):
    if profile['id'].endswith('-web'):
        return ROOT / 'profiles/web' / profile['id'].removeprefix('legion-') / 'SOUL.md'
    return ROOT / 'profiles' / profile['role'] / 'SOUL.md'


def plain_file(path, root):
    if not path.is_relative_to(root) or any(p.is_symlink() for p in [path, *path.parents]):
        raise ValueError('linked input refused')
    if not path.is_file():
        raise ValueError('required file missing')
    return path.read_bytes()


def make_files(team, models):
    validate(team, {}, [], {})
    if not team['profiles'] or not isinstance(models, dict):
        raise ValueError('select at least one profile')
    ids = {p['id'] for p in team['profiles']}
    if set(models) - ids:
        raise ValueError('unknown model override')
    known = registry()
    files, profiles = {}, []
    for profile in team['profiles']:
        identity = {k: profile[k] for k in ['id', 'role', 'provider']}
        registered(identity, known)
        model = model_reference(models.get(profile['id'], profile['model']))
        if model.startswith('chatgpt-web/') != profile['id'].endswith('-web'):
            raise ValueError('model lane differs from template')
        provider = profile['provider']
        config = {'model': {'provider': provider, 'default': model},
                  'fallback_providers': [], 'fallback_model': [],
                  'credential_pool_strategies': {provider: 'fill_first'}}
        prefix = 'profiles/' + profile['id'] + '/'
        files[prefix + 'config.example.json'] = (json.dumps(config, indent=2) + '\n').encode()
        files[prefix + 'SOUL.md'] = plain_file(soul_path(profile), ROOT)
        profiles.append(identity)
    files['README.md'] = (
        '# Offline setup bundle\n\n'
        'These fragments are previews, not installed profiles. No account mapping or credentials are included.\n'
        'Review each model ID and SOUL. Use the native fresh-home setup guide in Hermes Legion; '
        'apply individual config keys, never replace an existing full config. Preserve native quotas, '
        'project gates and session ownership. Both fallback chains must remain empty.\n'
        'No startup, login, inference or service command is executed by this bundle. '
        'Native account selection, model capabilities and actual runtime readiness remain unknown.\n'
    ).encode()
    manifest = {'schema_version': 1, 'kind': 'legion-setup-bundle',
                'quota_policy': 'inherit-native', 'paid_fallback': False, 'profiles': profiles,
                'files': [{'path': rel, 'sha256': hashlib.sha256(data).hexdigest()}
                          for rel, data in sorted(files.items())]}
    files['bundle.json'] = (json.dumps(manifest, indent=2) + '\n').encode()
    return files


def write_bundle(output, files):
    output = output.absolute()
    # Check lexical ancestors before resolving: resolve() alone would hide a link.
    if output.exists() or any(p.is_symlink() for p in [output, *output.parents]):
        raise ValueError('destination must be fresh and unlinked')
    output = output.resolve()
    protected = [ROOT, Path.home() / '.hermes']
    if os.environ.get('HERMES_HOME'):
        protected.append(Path(os.environ['HERMES_HOME']).expanduser().resolve())
    if any(output == root or output.is_relative_to(root) for root in protected):
        raise ValueError('destination inside a protected root')
    if not output.parent.is_dir():
        raise ValueError('choose an existing parent directory')
    output.mkdir(mode=0o700)  # Exclusive reservation; never replace a destination.
    for rel, data in files.items():
        target = output / rel
        target.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
        with target.open('xb') as stream:
            os.chmod(target, 0o600)
            stream.write(data)


def inspect_bundle(root):
    root = root.absolute()
    if not root.is_dir() or any(p.is_symlink() for p in [root, *root.parents]):
        raise ValueError('invalid bundle root')
    manifest = read_json(root / 'bundle.json')
    keys = {'schema_version', 'kind', 'quota_policy', 'paid_fallback', 'profiles', 'files'}
    fields(manifest, keys, keys)
    if (manifest['schema_version'] != 1 or manifest['kind'] != 'legion-setup-bundle'
            or manifest['quota_policy'] != 'inherit-native' or manifest['paid_fallback'] is not False):
        raise ValueError('unsupported bundle policy')
    known, required, profiles = registry(), {'README.md'}, {}
    if not isinstance(manifest['profiles'], list) or not manifest['profiles']:
        raise ValueError('missing profiles')
    for profile in manifest['profiles']:
        registered(profile, known)
        name = profile['id']
        if name in profiles:
            raise ValueError('duplicate profile')
        profiles[name] = profile
        required.update({'profiles/' + name + '/config.example.json', 'profiles/' + name + '/SOUL.md'})
    if not isinstance(manifest['files'], list):
        raise ValueError('invalid inventory')
    seen = set()
    for row in manifest['files']:
        fields(row, {'path', 'sha256'}, {'path', 'sha256'})
        rel = PurePosixPath(row['path'])
        if (rel.is_absolute() or '..' in rel.parts or row['path'] not in required
                or row['path'] in seen):
            raise ValueError('invalid inventory path')
        data = plain_file(root / row['path'], root)
        if hashlib.sha256(data).hexdigest() != row['sha256']:
            raise ValueError('bundle hash mismatch')
        seen.add(row['path'])
    observed = set()
    for path in root.rglob('*'):
        if path.is_symlink():
            raise ValueError('linked bundle refused')
        if path.is_file():
            observed.add(path.relative_to(root).as_posix())
    if seen != required or observed != required | {'bundle.json'}:
        raise ValueError('bundle inventory differs')
    for name, profile in profiles.items():
        prefix = root / 'profiles' / name
        cfg = read_json(prefix / 'config.example.json')
        fields(cfg, {'model', 'fallback_providers', 'fallback_model', 'credential_pool_strategies'},
               {'model', 'fallback_providers', 'fallback_model', 'credential_pool_strategies'})
        fields(cfg['model'], {'provider', 'default'}, {'provider', 'default'})
        model = model_reference(cfg['model']['default'])
        if (cfg['model']['provider'] != profile['provider']
                or model.startswith('chatgpt-web/') != name.endswith('-web')
                or cfg['fallback_providers'] != [] or cfg['fallback_model'] != []
                or cfg['credential_pool_strategies'] != {profile['provider']: 'fill_first'}):
            raise ValueError('unsafe native configuration')
        if plain_file(prefix / 'SOUL.md', root) != plain_file(soul_path(profile), ROOT):
            raise ValueError('non-template instructions')
    return len(profiles)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--team', type=Path, default=ROOT / 'examples/team.small.json')
    parser.add_argument('--models', type=Path)
    parser.add_argument('--output', type=Path, help='Fresh directory; omit to preview a new-file diff')
    args = parser.parse_args()
    try:
        files = make_files(read_json(args.team), read_json(args.models) if args.models else {})
        if args.output is not None:
            write_bundle(args.output, files)
            result = {'mode': 'offline-only', 'executed': False, 'written': True, 'file_count': len(files)}
        else:
            diff = ''.join(''.join(difflib.unified_diff([], data.decode().splitlines(keepends=True),
                           fromfile='/dev/null', tofile=rel)) for rel, data in sorted(files.items()))
            result = {'mode': 'offline-only', 'executed': False, 'written': False, 'diff': diff}
    except (ValueError, OSError, KeyError, TypeError, AttributeError):
        print('REFUSED: invalid setup input or destination; input values omitted', file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
