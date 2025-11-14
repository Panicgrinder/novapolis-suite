from __future__ import annotations

import hashlib
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def find_python(root: Path) -> str:
    venv_py = root / '.venv' / 'Scripts' / 'python.exe'
    if venv_py.exists():
        return str(venv_py)
    return 'python'


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    python = find_python(root)

    agent_dir = root / 'novapolis_agent'
    cover = agent_dir / '.coveragerc'

    art_dir = root / 'outputs' / 'test-artifacts'
    art_dir.mkdir(parents=True, exist_ok=True)
    junit_xml = art_dir / 'junit.xml'
    cov_xml = art_dir / 'coverage.xml'
    summary_path = art_dir / 'summary.txt'

    FailUnder = 80
    max_test_files = 400

    # safety collect-only check (similar to existing PS1 guard)
    try:
        collect = subprocess.run(
            [python, '-m', 'pytest', '--collect-only'],
            cwd=str(agent_dir),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
            text=True,
            timeout=300,
        )
    except Exception as e:
        print('Collect-run failed:', e)
        return 3

    collected_lines = [l for l in collect.stdout.splitlines() if '::' in l]
    collected_files = [l.split('::', 1)[0].strip() for l in collected_lines]
    unique_files = sorted(set(collected_files))
    file_count = len(unique_files)
    if file_count > max_test_files:
        print(f'STOP: Zu viele Testdateien gesammelt ({file_count} > {max_test_files}). Bitte Scope prüfen.')
        return 2

    # build pytest args
    args = [python, '-m', 'pytest']
    args += [
        '--cov',
        '--cov-report=term-missing',
        '--cov-branch',
        f'--cov-config={str(cover)}',
        f'--cov-report=xml:{str(cov_xml)}',
        f'--junitxml={str(junit_xml)}',
        f'--cov-fail-under={FailUnder}',
    ]

    print('Running:', ' '.join(args))
    proc = subprocess.run(args, cwd=str(agent_dir))
    exitcode = proc.returncode

    ts = datetime.now().strftime('%Y-%m-%d %H:%M')
    lines = [
        f'timestamp: {ts}',
        f'exitcode: {exitcode}',
        f'junit: {str(junit_xml)}',
        f'coverage_xml: {str(cov_xml)}',
    ]
    summary_path.write_text('\n'.join(lines), encoding='utf-8')

    if exitcode == 0:
        print('Pytest PASS')
    else:
        print(f'Pytest FAIL ({exitcode})')

    return exitcode


if __name__ == '__main__':
    raise SystemExit(main())
