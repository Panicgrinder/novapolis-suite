#!/usr/bin/env python3
import os
from pathlib import Path

root = Path(os.environ.get('WORKSPACE_FOLDER', Path(__file__).resolve().parents[2]))
out = root / 'workspace_tree_full.txt'

def write_tree(path, out_file):
    with out_file.open('w', encoding='utf-8') as f:
        for dirpath, dirnames, filenames in os.walk(path):
            level = dirpath.replace(str(path), '').count(os.sep)
            indent = ' ' * 4 * level
            f.write(f"{indent}{os.path.basename(dirpath)}/\n")
            for filename in filenames:
                f.write(f"{indent}    {filename}\n")

if __name__ == '__main__':
    write_tree(root, out)
