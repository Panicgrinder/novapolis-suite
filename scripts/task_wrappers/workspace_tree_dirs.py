#!/usr/bin/env python3
import os
from pathlib import Path

root = Path(os.environ.get('WORKSPACE_FOLDER', Path(__file__).resolve().parents[2]))
out = root / 'workspace_tree.txt'

def write_dirs(path, out_file):
    with out_file.open('w', encoding='utf-8') as f:
        for dirpath, dirnames, _ in os.walk(path):
            level = dirpath.replace(str(path), '').count(os.sep)
            indent = ' ' * 4 * level
            f.write(f"{indent}{os.path.basename(dirpath)}/\n")

if __name__ == '__main__':
    write_dirs(root, out)
