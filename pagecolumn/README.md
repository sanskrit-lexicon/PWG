# PWG page/column co-location index

_Created: 12-07-2026 · Last updated: 12-07-2026_

"Which PWG headwords shared a printed **column** (*Spalte*) or **page**?" —
derived from the entry-start column that the source records in every header.

Böhtlingk-Roth's PWG (7 vols, St. Petersburg 1855–1875) is printed **two columns
per page**, and the canonical citation unit is the column. The source text
[`csl-orig/v02/pwg/pwg.txt`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/pwg/pwg.txt)
records, in every entry header, the column that entry **starts** in:

```
<L>8<pc>1-0004<k1>aMSa<k2>aMSa<h>1
     └──── volume 1, column 0004
```

## Tools

| Script | Produces |
|---|---|
| [`pwg_page_index.py`](pwg_page_index.py) | the three co-location views below |
| [`pwg_page_verify.py`](pwg_page_verify.py) | a scan-verification anchor sheet for the derived page numbers |

```sh
# from this directory; reads ../../csl-orig/v02/pwg/pwg.txt by default
python pwg_page_index.py            # -> pwg_columns.tsv, pwg_pages.tsv, pwg_entry_locations.tsv
python pwg_page_verify.py --per 10  # -> pwg_page_verification.tsv
```

The three `.tsv` views are **regenerable and git-ignored** (see
[`.gitignore`](.gitignore)) — rebuild them with the command above. Only the tools
and the small verification sheet are tracked.

### 1. Column view — `pwg_columns.tsv` (8,171 columns)

Each row is one printed column and the entries that **start** in it:

```
column   volume  page  n_entries  L_ids                          headwords
1-0004   1       2     13         L8,L9,L10,L11,L12,...,L20       aMSa, aMSaka, aMSaka, ...
```

### 2. Page view — `pwg_pages.tsv` (4,329 pages)

The two columns of a physical leaf, merged:

```
page      volume  columns          n_entries  L_ids       headwords
1-p0002   1       1-0003+1-0004    17         L4,L5,...    a, a, afRin, aMSa, ...
```

### 3. Reverse view — `pwg_entry_locations.tsv` (123,366 entries)

Where any single entry sits — start column, every column it occupies (long
entries span into the next column via `[PageV-CCCC]` markers), and page(s):

```
L_id  headword  homonym  volume  start_column  page      all_columns             all_pages
L3    a         3        1       1-0001        1-p0001    1-0001,1-0002,1-0003    1-p0001,1-p0002
```

## Caveats

- Grouping is by where an entry **starts**. A long entry spanning into the next
  column is counted at its start column only; its full span lives in the reverse
  view's `all_columns` / `all_pages`.
- **The physical page number is DERIVED, not stored** in the source:
  `page = (column + 1) // 2` (2 columns per leaf, column 1 on page 1). The
  **column** numbers are exact; the derived **page** number can be off by a
  constant per-volume front-matter offset. PWG is cited by column and the scans
  print column numbers, so [`pwg_page_verify.py`](pwg_page_verify.py) emits an
  anchor sheet ([`pwg_page_verification.tsv`](pwg_page_verification.tsv), 70
  rows: first/last leaf + 8 interior leaves per volume) with landmark headwords
  in SLP1/IAST/Devanagari and blank `scan_leaf` / `cols_on_leaf` / `offset` /
  `paired_ok` columns. If `offset` is constant per volume and `paired_ok` is all
  `Y`, the derivation holds (shifted by that offset); any mid-volume drift is a
  real defect.

## Provenance

Auto-derived from the csl-orig PWG source; no manual data. Ported from the
equivalent tool in the
[SanskritLexicography/RussianTranslation](https://github.com/gasyoun/SanskritLexicography/blob/master/RussianTranslation/src/pwg_page_index.py)
pipeline, trimmed to the source-only derivation (the RussianTranslation copy also
annotates that pipeline's translation cards).

_Dr. Mārcis Gasūns_
