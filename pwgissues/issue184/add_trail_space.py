#!/usr/bin/env python3
"""
Read temp_pwg1.txt, ensure each content line has a trailing space.
Write to temp_pwg2.txt.

Lines starting with <L> or <LEND> and blank lines are left unchanged.
"""
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

in_path = os.path.join(SCRIPT_DIR, 'temp_pwg1.txt')
out_path = os.path.join(SCRIPT_DIR, 'temp_pwg2.txt')

with open(in_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

out_lines = []
for line in lines:
    if line.startswith('<L>') or line.startswith('<LEND>') or line.strip() == '':
        out_lines.append(line)
    else:
        stripped = line.rstrip('\n')
        if not stripped.endswith(' '):
            stripped += ' '
        out_lines.append(stripped + '\n')

with open(out_path, 'w', encoding='utf-8') as f:
    f.writelines(out_lines)

print(f'Written {out_path}: {len(out_lines)} lines')
