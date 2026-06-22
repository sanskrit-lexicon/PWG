#!/usr/bin/env python3
"""
Add n= prefix to plain <ls> tags connected by em-dash to a preceding
tag that has a book abbreviation and reference.

<ls>BṚH. ĀR. UP. 5,2,1</ls>—<ls>3</ls>
→ <ls>BṚH. ĀR. UP. 5,2,1</ls>—<ls n="BṚH. ĀR. UP. 5,2,">3</ls>

Modifies temp_pwg2.txt in place.
"""
import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(SCRIPT_DIR, 'temp_pwg2.txt')

with open(PATH, 'r', encoding='utf-8') as f:
    text = f.read()

def derive_prefix(prev, nxt):
    m = re.search(r'[\d,]+$', prev)
    if not m:
        return prev.rstrip()
    trailing = m.group()
    book_part = prev[:m.start()].rstrip()
    prev_commas = trailing.count(',')
    nxt_clean = nxt.rstrip(')').rstrip('.').rstrip(',')
    nxt_commas = nxt_clean.count(',')
    if nxt_commas >= prev_commas:
        return book_part.rstrip(',')
    parts = trailing.split(',')
    inherit = max(0, prev_commas - nxt_commas)
    inherited = ','.join(parts[:inherit])
    return f'{book_part} {inherited},'

def repl(m):
    prev = m.group(1)
    nxt = m.group(2)
    if not re.search(r'[A-Za-z]', prev) or not re.search(r'\d', prev):
        return m.group(0)
    if re.search(r'[A-Za-z]', nxt):
        return m.group(0)
    prefix = derive_prefix(prev, nxt)
    return f'<ls>{prev}</ls>—<ls n="{prefix}">{nxt}</ls>'

pattern = re.compile(r'<ls>([^<]*)</ls>—<ls>([^<]*)</ls>')
result, count = pattern.subn(repl, text)

with open(PATH, 'w', encoding='utf-8') as f:
    f.write(result)

print(f'Replaced {count} occurrences')
