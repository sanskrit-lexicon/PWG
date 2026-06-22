#!/usr/bin/env python3
"""
Verify filled <ls n=""> tags in temp_pwg3.txt against pwg0.txt lookup.
"""
import os, re, json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Load lookup
lookup = json.load(open('/tmp/pwg0_lookup.json'))
pwg0 = open(os.path.join(SCRIPT_DIR, 'temp_pwg0.txt'), encoding='utf-8').read()
pwg3 = open(os.path.join(SCRIPT_DIR, 'temp_pwg3.txt'), encoding='utf-8').read()

# Find ALL non-empty n= tags in pwg3 (our filled ones)
pwg3_tags = re.findall(r'<ls n="([^"]+)">([^<]*)</ls>', pwg3)

correct = 0
wrong = 0
not_found = 0

for n_val, content in pwg3_tags:
    if not n_val.strip():
        continue
    content = content.strip()
    if content in lookup:
        prefixes = lookup[content]
        if n_val in prefixes:
            correct += 1
        else:
            if wrong < 10:
                print(f'WRONG: content="{content}", pwg3 n="{n_val}", pwg0 prefixes={prefixes}')
            wrong += 1
    else:
        not_found += 1

total = correct + wrong + not_found
print(f'\nVerification results:')
print(f'  Correct:           {correct} ({correct*100/total:.1f}%)' if total else '  Correct: 0')
print(f'  Wrong:             {wrong}')
print(f'  Not in pwg0:       {not_found}')
print(f'  Total checked:     {total}')
