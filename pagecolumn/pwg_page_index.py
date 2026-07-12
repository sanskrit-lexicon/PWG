#!/usr/bin/env python
"""PWG page/column co-location index -- "which words shared a printed column / page".

Boehtlingk-Roth's PWG (7 vols, St. Petersburg 1855-1875) is printed in TWO
columns per page; the canonical citation unit is the column (Spalte). The source
text csl-orig/v02/pwg/pwg.txt records, per entry header, the column an entry
STARTS in:

    <L>8<pc>1-0004<k1>aMSa<k2>aMSa<h>1
         ^^^^^^ volume 1, column 0004

This tool derives three views:

  1. COLUMN view  -- column (<pc>) -> entries that start in it        (native unit)
  2. PAGE view    -- physical page (2 columns merged) -> entries       (as in the book)
  3. REVERSE view -- entry/headword -> its column(s), page(s), volume   (lookup)

Page assumption: page_in_volume = (column + 1) // 2  (2 columns per page, column 1
on page 1). Column numbering restarts per volume in the source; the physical
page number is DERIVED, not stored, so verify against scans if the exact page
label matters (a fixed front-matter offset would shift all page numbers by a
constant within a volume). See pwg_page_verify.py for a scan-anchor sheet.

Idempotent and deterministic (no Date.now / randomness).
"""
import argparse
import collections
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# L-id may be a float (Cologne supplement/Nachtrag records, e.g. 26305.290);
# <h> homonym marker is optional.
HEADER_RE = re.compile(r'^<L>([\d.]+)<pc>(\d+)-(\d+)<k1>(.*?)<k2>(.*?)(?:<h>(\d+))?\s*$')
# internal column-break marker inside a long entry, e.g. [Page1-0002]
PAGEBREAK_RE = re.compile(r'\[Page(\d+)-(\d+)\]')
HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_SRC = os.path.join(HERE, '..', '..', 'csl-orig', 'v02', 'pwg', 'pwg.txt')


class Entry:
    __slots__ = ('L', 'vol', 'col', 'k1', 'k2', 'h', 'spans')

    def __init__(self, L, vol, col, k1, k2, h):
        self.L, self.vol, self.col, self.k1, self.k2, self.h = L, vol, col, k1, k2, h
        self.spans = {(vol, col)}  # every (vol,col) this entry occupies


def page_of(col):
    """Physical page within a volume, 2 columns per page."""
    return (col + 1) // 2


def parse_source(path):
    """Return list[Entry], filling .spans from embedded [PageV-CCCC] markers."""
    entries = []
    cur = None
    with io.open(path, encoding='utf-8') as f:
        for line in f:
            m = HEADER_RE.match(line)
            if m:
                L, vol, col, k1, k2, h = m.groups()
                cur = Entry(L, int(vol), int(col), k1, k2, h)
                entries.append(cur)
                continue
            if cur is not None:
                for pv, pc in PAGEBREAK_RE.findall(line):
                    cur.spans.add((int(pv), int(pc)))
    return entries


def pc_str(vol, col):
    return f'{vol}-{col:04d}'


def write_column_view(entries, out):
    """column -> entries that START there (native PWG citation unit)."""
    by_col = collections.OrderedDict()
    for e in entries:
        by_col.setdefault((e.vol, e.col), []).append(e)
    with io.open(out, 'w', encoding='utf-8') as f:
        f.write('column\tvolume\tpage\tn_entries\tL_ids\theadwords\n')
        for (vol, col), es in by_col.items():
            f.write('\t'.join([
                pc_str(vol, col), str(vol), str(page_of(col)), str(len(es)),
                ','.join('L' + e.L for e in es),
                ', '.join(e.k1 for e in es),
            ]) + '\n')
    return len(by_col)


def write_page_view(entries, out):
    """physical page -> entries whose START column falls on it (2 cols merged)."""
    by_page = collections.OrderedDict()
    for e in entries:
        by_page.setdefault((e.vol, page_of(e.col)), []).append(e)
    with io.open(out, 'w', encoding='utf-8') as f:
        f.write('page\tvolume\tcolumns\tn_entries\tL_ids\theadwords\n')
        for (vol, pg), es in by_page.items():
            cols = sorted({e.col for e in es})
            f.write('\t'.join([
                f'{vol}-p{pg:04d}', str(vol),
                '+'.join(pc_str(vol, c) for c in cols), str(len(es)),
                ','.join('L' + e.L for e in es),
                ', '.join(e.k1 for e in es),
            ]) + '\n')
    return len(by_page)


def write_reverse_view(entries, out):
    """entry -> where it is: start column, all occupied columns, page(s)."""
    with io.open(out, 'w', encoding='utf-8') as f:
        f.write('L_id\theadword\thomonym\tvolume\tstart_column\tpage'
                '\tall_columns\tall_pages\n')
        for e in entries:
            spans = sorted(e.spans)
            pages = sorted({(v, page_of(c)) for v, c in spans})
            f.write('\t'.join([
                'L' + e.L, e.k1, e.h or '', str(e.vol), pc_str(e.vol, e.col),
                f'{e.vol}-p{page_of(e.col):04d}',
                ','.join(pc_str(v, c) for v, c in spans),
                ','.join(f'{v}-p{p:04d}' for v, p in pages),
            ]) + '\n')
    return len(entries)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--src', default=DEFAULT_SRC, help='pwg.txt source path')
    ap.add_argument('--outdir', default=HERE, help='directory for the .tsv views')
    args = ap.parse_args()

    entries = parse_source(args.src)
    print(f'parsed {len(entries)} PWG entries from {args.src}')

    col_out = os.path.join(args.outdir, 'pwg_columns.tsv')
    pg_out = os.path.join(args.outdir, 'pwg_pages.tsv')
    rev_out = os.path.join(args.outdir, 'pwg_entry_locations.tsv')
    nc = write_column_view(entries, col_out)
    npg = write_page_view(entries, pg_out)
    write_reverse_view(entries, rev_out)
    print(f'  column view : {nc} columns   -> {col_out}')
    print(f'  page view   : {npg} pages     -> {pg_out}')
    print(f'  reverse view: {len(entries)} entries -> {rev_out}')


if __name__ == '__main__':
    main()
