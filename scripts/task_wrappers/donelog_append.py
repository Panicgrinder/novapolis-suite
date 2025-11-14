#!/usr/bin/env python3
import sys
from datetime import datetime
from pathlib import Path

root = Path(__file__).resolve().parents[2]
done_msg = sys.argv[1] if len(sys.argv) > 1 else None
done_author = sys.argv[2] if len(sys.argv) > 2 else None

if not done_msg:
    print('ERROR: doneMessage is required as first argument', file=sys.stderr)
    sys.exit(2)

if not done_author:
    import getpass
    done_author = getpass.getuser()

ts = datetime.now().strftime('%Y-%m-%d %H:%M')
path = root / 'novapolis_agent' / 'docs' / 'DONELOG.txt'
path.parent.mkdir(parents=True, exist_ok=True)
line = f"{ts} | {done_author} | {done_msg}\n"
with path.open('a', encoding='utf-8') as f:
    f.write(line)
print('DONELOG appended:', line.strip())
