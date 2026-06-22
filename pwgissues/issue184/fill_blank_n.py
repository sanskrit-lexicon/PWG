#!/usr/bin/env python3
"""
Fill blank <ls n=""> tags with inferred book prefix from preceding context.
Reads temp_pwg2.txt, writes temp_pwg3.txt.

Comma-count inheritance:
- ref_commas == expected_commas -> use bare book_prefix, update last_full_ref
- ref_commas > expected_commas  -> use bare book_prefix, DON'T update last_full_ref
- ref_commas < expected_commas  -> inherit diff parts from last_full_ref, DON'T update
"""
import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IN_PATH = os.path.join(SCRIPT_DIR, 'temp_pwg2.txt')
OUT_PATH = os.path.join(SCRIPT_DIR, 'temp_pwg3.txt')


def strip_is(content):
    return re.sub(r'<is[^>]*>.*?</is>', '', content)


def extract_book_prefix(n_attr, content):
    if n_attr and n_attr.strip():
        n_val = n_attr.strip()
        m = re.search(r'\d', n_val)
        if m:
            return n_val[:m.start()].rstrip(' ,.')
        return n_val.rstrip(' ,.')
    clean = strip_is(content).strip()
    m = re.search(r'\d', clean)
    if m:
        return clean[:m.start()].rstrip()
    return ''


def extract_ref(content, book_prefix):
    clean = strip_is(content).strip()
    if book_prefix and clean.startswith(book_prefix):
        ref = clean[len(book_prefix):].strip().lstrip('.')
        return ref
    m = re.search(r'\d', clean)
    if m:
        return clean[m.start():].strip()
    return clean


def inherit_prefix(book_prefix, ref_commas, expected_commas, last_full_ref):
    diff = expected_commas - ref_commas
    if diff <= 0:
        return book_prefix
    parts = last_full_ref.rstrip(',').split(',')
    inherited = ','.join(parts[:diff]).strip()
    return f'{book_prefix} {inherited},' if inherited else book_prefix


# Read input
with open(IN_PATH, 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
output_lines = []

book_prefix = ''
last_full_ref = ''
expected_commas = 0
changed = 0

ls_pat = re.compile(r'(<(?:ls|ls\s+n="[^"]*")>)(.*?)(</ls>)')

for line in lines:
    # Reset state at entry boundary
    stripped = line.strip()
    if stripped == '<L>' or stripped == '<LEND>':
        book_prefix = ''
        last_full_ref = ''
        expected_commas = 0
        output_lines.append(line)
        continue

    # Process each <ls> tag in the line
    parts = []
    pos = 0
    for m in ls_pat.finditer(line):
        parts.append(line[pos:m.start()])
        tag_open = m.group(1)
        content = m.group(2)
        tag_close = m.group(3)

        if tag_open == '<ls>':
            # Plain <ls> - update state from content
            bp = extract_book_prefix('', content)
            if bp:
                book_prefix = bp
            ref = extract_ref(content, bp)
            if ref:
                last_full_ref = ref
                expected_commas = ref.rstrip(',').count(',')
            parts.append(tag_open + content + tag_close)

        elif tag_open.startswith('<ls n=""'):
            # Blank <ls n=""> - fill prefix
            ref = content.rstrip('.')
            if book_prefix and ref:
                rc = ref.count(',')
                new_prefix = inherit_prefix(book_prefix, rc, expected_commas, last_full_ref)
                new_open = f'<ls n="{new_prefix}">'
                parts.append(new_open + content + tag_close)
                changed += 1
                if rc == expected_commas and book_prefix:
                    last_full_ref = ref
                # rc > expected_commas or rc < expected_commas: don't update last_full_ref
            else:
                parts.append(tag_open + content + tag_close)

        else:
            # Named <ls n="..."> - update state from n= and content
            n_val = re.search(r'<ls n="([^"]*)"', tag_open)
            if n_val:
                nv = n_val.group(1)
                bp = extract_book_prefix(nv, content)
                if bp:
                    book_prefix = bp
            ref = content.strip().rstrip('.')
            if ref:
                rc = ref.strip().rstrip(',').count(',')
                # Only update if this ref establishes a new expected_commas baseline
                # For tags with n=, use the full content as reference
                last_full_ref = ref
                expected_commas = rc
            parts.append(tag_open + content + tag_close)

        pos = m.end()

    parts.append(line[pos:])
    output_lines.append(''.join(parts))

output = '\n'.join(output_lines)

with open(OUT_PATH, 'w', encoding='utf-8') as f:
    f.write(output)

old_blanks = len(re.findall(r'<ls n="">', text))
new_blanks = len(re.findall(r'<ls n="">', output))
print(f'Blank <ls n=""> tags: {old_blanks} -> {new_blanks} ({changed} filled)')
