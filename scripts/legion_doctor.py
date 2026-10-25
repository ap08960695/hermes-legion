#!/usr/bin/env python3
"""Read explicit offline inputs. Runtime/auth readiness always remains unknown."""
import argparse
import json
from pathlib import Path
import subprocess
import time

from legion_plan import plan, read_json, validate
from legion_setup import ROOT, inspect_bundle, model_reference
from verify_checkout import verify


def diagnose(*, team=None, bundle=None, checkout=None, phase='installed', snapshot=None, now=None):
    checks = []
    if team is not None:
        try:
            validate(team, snapshot or {}, [], {})
            if not team['profiles']:
                raise ValueError('missing profiles')
            checks.append({'code': 'team-schema', 'status': 'pass'})
            for p in team['profiles']:
                try:
                    model_reference(p['model'])
                    status, code = 'pass', 'model-reference-syntax'
                except ValueError:
                    status, code = 'fail', 'model-placeholder'
                checks.append({'code': code, 'status': status, 'profile': p['id']})
            if snapshot is None:
                checks.append({'code': 'native-readiness-not-observed', 'status': 'unknown'})
            else:
                clock = time.time() if now is None else now
                plan(team, snapshot, [], now=clock)
                current = bool(snapshot) and snapshot['captured_at'] <= clock < snapshot['expires_at']
                checks.append({'code': 'snapshot-current' if current else 'snapshot-expired',
                               'status': 'pass' if current else 'fail'})
        except (ValueError, KeyError, TypeError, AttributeError, OverflowError):
            checks.append({'code': 'invalid-team-or-snapshot', 'status': 'fail'})
    if bundle is not None:
        try:
            inspect_bundle(bundle)
            checks.append({'code': 'bundle-config-soul-and-inventory', 'status': 'pass'})
        except (ValueError, OSError, KeyError, TypeError, AttributeError):
            checks.append({'code': 'invalid-bundle', 'status': 'fail'})
    if checkout is None:
        checks.append({'code': 'checkout-not-inspected', 'status': 'unknown'})
    else:
        try:
            verify(checkout, read_json(ROOT / 'patches/manifest.json'), phase)
            checks.append({'code': 'pinned-checkout-' + phase, 'status': 'pass'})
        except (ValueError, OSError, KeyError, TypeError, subprocess.SubprocessError):
            checks.append({'code': 'checkout-incompatible', 'status': 'fail'})
    return {'mode': 'offline-only', 'executed': False,
            'offline_ready': any(c['status'] == 'pass' for c in checks)
                and not any(c['status'] == 'fail' for c in checks),
            'runtime_ready': 'unknown', 'checks': checks}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--team', type=Path)
    parser.add_argument('--bundle', type=Path)
    parser.add_argument('--checkout', type=Path)
    parser.add_argument('--phase', choices=['base', 'installed'], default='installed')
    parser.add_argument('--snapshot', type=Path)
    parser.add_argument('--now', type=float)
    args = parser.parse_args()
    if args.team is None and args.bundle is None:
        args.team = ROOT / 'examples/team.small.json'
    try:
        if args.snapshot is not None and args.team is None:
            raise ValueError('snapshot requires team')
        result = diagnose(team=read_json(args.team) if args.team else None, bundle=args.bundle,
                          checkout=args.checkout, phase=args.phase,
                          snapshot=read_json(args.snapshot) if args.snapshot else None, now=args.now)
    except (ValueError, OSError, KeyError, TypeError, AttributeError):
        result = {'mode': 'offline-only', 'executed': False, 'offline_ready': False,
                  'runtime_ready': 'unknown', 'checks': [{'code': 'invalid-input', 'status': 'fail'}]}
    print(json.dumps(result, indent=2))
    return 0 if result['offline_ready'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
