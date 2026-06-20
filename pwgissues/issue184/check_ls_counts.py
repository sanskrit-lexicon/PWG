#!/usr/bin/env python3
"""
Read <L> blocks from temp_pwg0.txt, temp_pwg.txt, temp_pwg1.txt.
Compare actual <ls> tags per block (ignoring trailing period before </ls>),
output TSV.
"""

import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILES = ['temp_pwg0.txt', 'temp_pwg.txt', 'temp_pwg1.txt']


def read_file(name):
    path = os.path.join(SCRIPT_DIR, name)
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def normalize_tag(tag):
    """Strip trailing period from inner text of <ls> tag for comparison."""
    return re.sub(r'\.(?=</ls>)', '', tag)


def extract_block_tags(text):
    """Return dict of Lnum -> list of normalized <ls> tag strings."""
    blocks = {}
    pos = 0
    ls_re = re.compile(r'<ls(?:\s+n="[^"]*")?[^>]*>.*?</ls>')
    block_re = re.compile(r'<L>(\d+)')
    lend_re = re.compile(r'<LEND>')

    while pos < len(text):
        m = block_re.search(text, pos)
        if not m:
            break
        lnum = m.group(1)
        block_start = m.start()

        lend = lend_re.search(text, block_start)
        if not lend:
            break
        block_end = lend.end()
        block_text = text[block_start:block_end]

        tags = [normalize_tag(t) for t in ls_re.findall(block_text)]
        blocks[lnum] = tags

        pos = block_end

    return blocks


def main():
    data = {}
    for fname in FILES:
        print(f"Reading {fname}...", file=sys.stderr)
        text = read_file(fname)
        data[fname] = extract_block_tags(text)
        print(f"  {len(data[fname])} blocks", file=sys.stderr)

    out_path = os.path.join(SCRIPT_DIR, 'temp_ls_compare.tsv')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('Lnum\tpwg0_count\tpwg_count\tpwg1_count\tResult\n')

        all_lnums = set()
        for d in data.values():
            all_lnums.update(d.keys())

        sorted_lnums = sorted(all_lnums, key=lambda x: int(x))

        for lnum in sorted_lnums:
            tags0 = data['temp_pwg0.txt'].get(lnum, [])
            tags = data['temp_pwg.txt'].get(lnum, [])
            tags1 = data['temp_pwg1.txt'].get(lnum, [])

            result = 'Match' if tags0 == tags1 else 'Fail'
            f.write(f'{lnum}\t{len(tags0)}\t{len(tags)}\t{len(tags1)}\t{result}\n')

    print(f"Written {out_path} ({len(sorted_lnums)} blocks)", file=sys.stderr)

    matches = sum(1 for lnum in sorted_lnums
                  if data['temp_pwg0.txt'].get(lnum, []) == data['temp_pwg1.txt'].get(lnum, []))
    fails = len(sorted_lnums) - matches
    print(f"Tag-level matches: {matches}, Fails: {fails}", file=sys.stderr)


if __name__ == '__main__':
    main()
