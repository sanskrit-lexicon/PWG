#!/usr/bin/env python3
"""
Split consolidated <ls>P. ... <is>...</is> ...</ls> tags where
<is> XML tags prevent the multi-ref split in restore_ls_n.py
(which uses [^<]* and cannot match content containing XML tags).

<ls>P. 7,1,98. 99, <is n="Vārttika">Vārtt.</is></ls>
-> <ls>P. 7,1,98</ls>. <ls n="P. 7,1,">99, <is n="Vārttika">Vārtt.</is></ls>

Uses comma-count inheritance matching restore_ls_n.py behavior.
Modifies temp_pwg2.txt in place.
"""
import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(SCRIPT_DIR, 'temp_pwg2.txt')

with open(PATH, 'r', encoding='utf-8') as f:
    text = f.read()


def split_p_is(m):
    content = m.group(1)
    if '<is' not in content:
        return m.group(0)

    is_pos = content.index('<is')
    before_is = content[:is_pos]
    after_is = content[is_pos:]

    pieces = []
    remaining = before_is
    while True:
        m2 = re.search(r'(?<=[\d])\. ', remaining)
        if m2:
            piece = remaining[:m2.end() - 2]
            remaining = remaining[m2.end():]
            pieces.append(piece)
        else:
            pieces.append(remaining)
            break

    if len(pieces) <= 1:
        return m.group(0)

    first_text = pieces[0]
    m_book = re.search(r'\d', first_text)
    book_prefix = first_text[:m_book.start()].rstrip() if m_book else first_text
    first_numeric = first_text[m_book.start():] if m_book else ''
    expected_commas = first_numeric.count(',')
    last_full_content = first_numeric.rstrip('.')

    out = [f'<ls>{first_text}</ls>.']

    for i, piece in enumerate(pieces[1:]):
        is_last = (i == len(pieces) - 2)
        display = piece + after_is if is_last else piece

        ref_norm = piece.strip().rstrip('.').rstrip(',')
        commas = ref_norm.count(',')

        if commas == expected_commas:
            prefix = book_prefix
            last_full_content = ref_norm
        elif commas > expected_commas:
            prefix = book_prefix
        else:
            last_parts = last_full_content.split(',')
            num_to_inherit = expected_commas - commas
            inherited = ','.join(last_parts[:num_to_inherit]).strip()
            prefix = f'{book_prefix} {inherited},'

        out.append(f' <ls n="{prefix}">{display}</ls>')

    return ''.join(out)


pattern = re.compile(r'<ls>(P\..*?)</ls>')
result, count = pattern.subn(split_p_is, text)

with open(PATH, 'w', encoding='utf-8') as f:
    f.write(result)

print(f'Replaced {count} occurrences')
