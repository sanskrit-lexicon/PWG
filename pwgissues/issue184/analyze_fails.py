#!/usr/bin/env python3
"""
Generate TSV comparing <ls> tags between temp_pwg0.txt and temp_pwg1.txt.
Output columns: lnum, pwg0, pwg1, Pass/Fail.
Normalizes .</ls> -> </ls>. and )</ls> -> </ls>) for comparison,
and collapses spacing differences.
"""

import os
import re
import sys
import csv

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILES = ['temp_pwg0.txt', 'temp_pwg1.txt']


def read_file(name):
    path = os.path.join(SCRIPT_DIR, name)
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def normalize_for_compare(tag):
    """Normalize tag so that .</ls> vs </ls>. and )</ls> vs </ls>) are equivalent,
    and spacing differences like VI,75 vs VI, 75 are ignored."""
    tag = re.sub(r'[.)](?=</ls>)', '', tag)
    tag = re.sub(r'(?<=</ls>)[.)]', '', tag)
    tag = re.sub(r'  +', ' ', tag)
    tag = re.sub(r', +', ',', tag)
    return tag


def extract_block_tags(text):
    """Return dict of Lnum -> list of raw <ls> tag strings."""
    blocks = {}
    pos = 0
    ls_re = re.compile(r'<ls(?:\s+n="[^"]*")?[^>]*>.*?</ls>[.)]?')
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

        tags = ls_re.findall(block_text)
        blocks[lnum] = tags
        pos = block_end

    return blocks


def match_tags(tags0, tags1):
    """Greedy multiset matching: matches each normalized tag from tags0 to
    the first unused match in tags1, then appends remaining unmatched tags."""
    norm0 = [normalize_for_compare(t) for t in tags0]
    norm1 = [normalize_for_compare(t) for t in tags1]

    used = [False] * len(tags1)
    pairs = []

    for i, n0 in enumerate(norm0):
        matched = False
        for j, n1 in enumerate(norm1):
            if not used[j] and n0 == n1:
                pairs.append((tags0[i], tags1[j], 'Pass'))
                used[j] = True
                matched = True
                break
        if not matched:
            pairs.append((tags0[i], '', 'Fail'))

    for j in range(len(tags1)):
        if not used[j]:
            pairs.append(('', tags1[j], 'Fail'))

    return pairs


def main():
    data = {}
    for fname in FILES:
        print(f"Reading {fname}...", file=sys.stderr)
        text = read_file(fname)
        data[fname] = extract_block_tags(text)
        print(f"  {len(data[fname])} blocks", file=sys.stderr)

    out_path = os.path.join(SCRIPT_DIR, 'temp_ls_compare_detail.tsv')

    all_lnums = set()
    for d in data.values():
        all_lnums.update(d.keys())
    sorted_lnums = sorted(all_lnums, key=lambda x: int(x))

    total_tags = 0
    tag_passes = 0
    tag_fails = 0
    with open(out_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['lnum', 'pwg0', 'pwg1', 'Pass/Fail'])

        for lnum in sorted_lnums:
            tags0 = data['temp_pwg0.txt'].get(lnum, [])
            tags1 = data['temp_pwg1.txt'].get(lnum, [])

            pairs = match_tags(tags0, tags1)
            for t0, t1, status in pairs:
                total_tags += 1
                if status == 'Pass':
                    tag_passes += 1
                else:
                    tag_fails += 1
                writer.writerow([lnum, t0, t1, status])

    print(f"Written {out_path} ({len(sorted_lnums)} blocks, {total_tags} total <ls> tags)", file=sys.stderr)
    print(f"Pass: {tag_passes}, Fail: {tag_fails}", file=sys.stderr)


if __name__ == '__main__':
    main()
