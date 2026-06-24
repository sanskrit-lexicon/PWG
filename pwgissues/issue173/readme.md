# Issue 173 — ṚV. PRĀT. / ṚV. Prāt. (Ṛgveda Prātiśākhya)

Created 2025-11-14. Replicates the issue169 workflow for the Ṛgveda Prātiśākhya references in PWG, PW, PWKVN, and SCH.

## Index

Provided by Andhrabharati as two files:

| File | Records | Contents |
|---|---|---|
| `rvps1.txt` | 141 | Volume 1 (patala 1–6, pages 22–149) |
| `rvps2.txt` | 230 | Volume 2 (patala 7–18+, pages 8–236) |

Combined via `combine_index.py` into `index.txt` (371 records, 7 columns: page, patala, fromv, tov, ipage, Remarks, volume).

Index structure:
- `vp` field: `{volume}_{page:03d}` → e.g. `1_022` → `rvps1_022.pdf`
- `patala` field: patala number (may be null for pages with no sūtra mapping)
- `fromv`/`tov`: sūtra range (may be null for index-only pages)
- 43 records for patala 18 and 1 for patala 20 are in the index but are **not coverable** by the scan (index ends at page 236, patala 18+ beyond scan coverage)

## Scan Repository

Created at `sanskrit-lexicon-scans/rvps/`:

- `app0`: 1-parameter lookup by ipage (for pages without specific sūtra)
- `app1`: 2-parameter lookup by patala, sūtra

Link target: `https://sanskrit-lexicon-scans.github.io/rvps/app1?N,N`

## Dictionary Analysis

`lsfix2_parm.py` configures two lscode variants:

| Dictionary | lscode | Dictionary file |
|---|---|---|
| pwg | `ṚV. PRĀT.` | `temp_pwg_0.txt` |
| pw | `ṚV. PRĀT.` | `temp_pw_0.txt` |
| pwkvn | `ṚV. PRĀT.` | `temp_pwkvn_0.txt` |
| sch | `ṚV. Prāt.` | `temp_sch_0.txt` |

### Results

| Dictionary | True | None | False | Fixed |
|---|---|---|---|---|---|
| pwg | 1769 | 1 | 0 | 0 |
| pw | 88 | 1 | 0 | 0 |
| pwkvn | 9 | 0 | 0 | 0 |
| sch | 11 | 0 | 0 | 0 |

**Improvement**: Parenthetical annotations like `(14)`, `(20. 21)`, `(<is>Sūtra</is> 18)`, `(ed. MÜLLER)`, `(ed. M.)` are now recognized as valid standard refs via expanded sfx patterns in `get_REGEXes_standard()` (`lsfix2.py:97`). The PHP handler already extracts `N,N` correctly from such entries, so no dictionary changes are needed.

### pw corrections (3)

Three compound references were split into separate `<ls>` tags via `dict_replace2.py`:

| Line | Headword | Original | Corrected |
|---|---|---|---|
| 14456 | `anAnupUrvya` | `<ls>ṚV. PRĀT. 2,43. 11,8</ls>` | `<ls>ṚV. PRĀT. 2,43.</ls> <ls n="ṚV. PRĀT.">11,8</ls>` |
| 15001 | `aniNgya` | `<ls>ṚV. PRĀT. 5,20. 9,13</ls>` | `<ls>ṚV. PRĀT. 5,20.</ls> <ls n="ṚV. PRĀT.">9,13</ls>` |
| 411249 | `varRatas` | `<ls>ṚV. PRĀT. 17,8. 10</ls>` | `<ls>ṚV. PRĀT. 17,8.</ls> <ls n="ṚV. PRĀT. 17,">10</ls>` |

### pwg: No dictionary changes needed

`temp_pwg_1.txt` is identical to `temp_pwg_0.txt` — all 1769 True refs already produce correct links. The single remaining None ref cannot be auto-linked (see below).

### Remaining issues to review

**pwg None (1)**: `XIII, N. 2` — Roman numeral patala with "N." — cannot be linked.

**pw None (1)**: `Einl. 6` — Einleitung (introduction) reference — cannot be linked.

## basicadjust.php

Modified the master template at `csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php`:

### `ls_callback_pwg_href` (pwg/pw/pwkvn)
Added ṚV. PRĀT. section matching `ṚV. PRĀT. N,N` → `rvps/app1?N,N`

### `ls_callback_sch_href` (sch)
1. Added `'ṚV. Prāt.' => 'rvps'` to `$code_to_pfx`
2. Added rvps handler: `$pfx == 'rvps'` → `rvps/app1?N,N`

> The per-dictionary files (`sanskrit-lexicon/{pwg,pw,pwkvn,sch}/web/webtc/basicadjust.php`) are **not** edited directly — they are generated from the master template in a build step.

## Files

| File | Purpose |
|---|---|
| `rvps1.txt` | Volume 1 index (source) |
| `rvps2.txt` | Volume 2 index (source) |
| `combine_index.py` | Merges rvps1 + rvps2 into `index.txt` |
| `index.txt` | Combined index (371 records) |
| `make_js_index.py` | Generates `index.js` from `index.txt` |
| `index.js` | JavaScript index data for scan apps |
| `lsfix2_parm.py` | Target code configuration for lsfix2 |
| `lsfix2.py` | Analysis script (from issue169) |
| `lsfix2_pwg_0.txt` | pwg analysis output |
| `lsfix2_pw_0.txt` | pw analysis output |
| `lsfix2_pwkvn_0.txt` | pwkvn analysis output |
| `lsfix2_sch_0.txt` | sch analysis output |
| `temp_pwg_0.txt` | Original pwg text (from csl-orig) |
| `temp_pw_0.txt` | Original pw text (from csl-orig) |
| `temp_pwg_1.txt` | pwg after auto-fix (no changes) |
| `temp_pw_1.txt` | pw after auto-fix (3 changes) |
| `temp_pwkvn_0.txt` | Original pwkvn text |
| `temp_sch_0.txt` | Original sch text |
| `temp_mw_0.txt` | Original mw text (no ṚV. PRĀT. refs) |
| `dict_replace2.py` | Applies line-level corrections (from issue169) |
| `diff_to_changes_dict.py` | Generates change files from diffs (from issue169) |
| `digentry.py` | Entry extraction utility (from issue169) |
| `change_pw_1.txt` | The 3 pw corrections (updateByLine format) |
| `readme.md` | This file |

## Installation

### csl-corrections
```sh
cd /path/to/csl-corrections
git pull
git add .
git commit -m "issue173 rvps link target
Ref: https://github.com/sanskrit-lexicon/pwg/issues/173"
git push
```

### csl-websanlexicon
```sh
cd /path/to/csl-websanlexicon
git pull
git add .
git commit -m "issue173 rvps link target
Ref: https://github.com/sanskrit-lexicon/pwg/issues/173"
git push
```

### csl-orig (if changes needed)
```sh
# Verify only pw has changes:
diff temp_pw_1.txt /path/to/csl-orig/v02/pw/pw.txt
cd /path/to/csl-orig
git pull
git add .
git commit -m "issue173 rvps
Ref: https://github.com/sanskrit-lexicon/pwg/issues/173"
git push
```

### PWG repo (this issue directory)
```sh
cd /path/to/PWG/pwgissues/issue173
git pull
git add .
git commit -m "rvps link target
Ref: https://github.com/sanskrit-lexicon/pwg/issues/173"
git push
```

### Server sync
After pushing csl-orig, csl-websanlexicon, csl-corrections:
```sh
# On Cologne server:
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/
sh generate_dict.sh pw   ../../PWScan/2020/
sh generate_dict.sh pwkvn ../../PWKVNScan/2020/
sh generate_dict.sh sch  ../../SCHScan/2020/
```

## References

- GitHub issue: <https://github.com/sanskrit-lexicon/PWG/issues/173>
- Scan repo: <https://github.com/sanskrit-lexicon-scans/rvps>
- Issue169 (Rājataraṅgiṇī, prototype): `pwgissues/issue169/`
