#!/usr/bin/env python3
"""
Generate TSV comparing <ls> tags between temp_pwg0.txt and temp_pwg1.txt.
Output columns: lnum, pwg0, pwg1, Pass/Fail.
Normalizes .</ls> -> </ls>. and )</ls> -> </ls>) for comparison.
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
    """Normalize tag so that .</ls> vs </ls>. and )</ls> vs </ls>) are equivalent."""
    tag = re.sub(r'[.)](?=</ls>)', '', tag)
    tag = re.sub(r'(?<=</ls>)[.)]', '', tag)
    return tag


def extract_content(tag):
    """Extract the reference content (between > and </ls>) from a tag."""
    m = re.search(r'>([^<]*)</ls>', tag)
    return m.group(1) if m else tag


def is_subsumed(c0, c1):
    """Check if reference content c0 appears as a whole ref within c1."""
    if c0 == c1:
        return True
    if c0 in c1:
        idx = c1.index(c0)
        if idx > 0 and c1[idx - 1] not in '. ':
            return False
        end = idx + len(c0)
        if end < len(c1) and c1[end] not in '. ':
            return False
        return True
    return False


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
    """Two-pass matching: exact multiset, then subsumption for remainder."""
    norm0 = [normalize_for_compare(t) for t in tags0]
    norm1 = [normalize_for_compare(t) for t in tags1]

    used0 = [False] * len(tags0)
    used1 = [False] * len(tags1)
    pairs = []

    # Pass 1: exact multiset matching
    for i, n0 in enumerate(norm0):
        for j, n1 in enumerate(norm1):
            if not used1[j] and n0 == n1:
                pairs.append((tags0[i], tags1[j], 'Pass'))
                used0[i] = True
                used1[j] = True
                break

    # Collect unmatched tags with their norm and content
    unmatched0 = [(i, tags0[i], norm0[i], extract_content(norm0[i])) for i in range(len(tags0)) if not used0[i]]
    unmatched1 = [(j, tags1[j], norm1[j], extract_content(norm1[j])) for j in range(len(tags1)) if not used1[j]]

    # Pass 2: subsumption matching (allow 1 pwg1 tag to match multiple pwg0 tags)
    sub_count = [0] * len(unmatched1)
    for i0, t0, n0, c0 in unmatched0:
        for e_idx, (j_orig, t1, n1, c1) in enumerate(unmatched1):
            if c0 and c1 and (is_subsumed(c0, c1) or is_subsumed(c1, c0)):
                pairs.append((t0, t1, 'Pass*'))
                used0[i0] = True
                sub_count[e_idx] += 1
                break

    # Remaining unmatched from pwg0
    for i, t0, n0, c0 in unmatched0:
        if not used0[i]:
            pairs.append((t0, '', 'Fail'))

    # Remaining unmatched from pwg1 (only if zero subsumption matches)
    for e_idx, (j_orig, t1, n1, c1) in enumerate(unmatched1):
        if sub_count[e_idx] == 0:
            pairs.append(('', t1, 'Fail'))

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
                if status in ('Pass', 'Pass*'):
                    tag_passes += 1
                else:
                    tag_fails += 1
                writer.writerow([lnum, t0, t1, status])

    print(f"Written {out_path} ({len(sorted_lnums)} blocks, {total_tags} total <ls> tags)", file=sys.stderr)
    print(f"Pass: {tag_passes}, Fail: {tag_fails}", file=sys.stderr)


if __name__ == '__main__':
    main()
