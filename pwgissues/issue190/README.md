# issue190 — fg/fgg correction pipeline

Corrects misplaced `fg.`/`fgg.` (German "folgende") in `<ls>` citation tags of PWG dictionary data.

## Input

`temp_pwg0.txt` — source from the issue184 pipeline (sibling directory).

## Pipeline

Run all steps: `sh redo.sh`

| Step | Script | Input | Output | Changes | What it does |
|------|--------|-------|--------|---------|-------------|
| 1 | `step1.py` | temp_pwg0.txt | temp_pwg1.txt | 8501 | Merges adjacent `<ls>` pairs where the second tag contains only `fg`/`fgg`. Pattern: `</ls>.\s*<ls n="...">fgg</ls>` → `<ls>content. fgg.</ls>` |
| 2 | `step2.py` | temp_pwg1.txt | temp_pwg2.txt | 4856 | Extracts `fg.`/`fgg.` from the *n attribute* of the second tag and moves it to the first tag's content. Pattern: `</ls>.\s*<ls n="...fg...">content</ls>` |
| 3 | `step3.py` | temp_pwg2.txt | temp_pwg3.txt | 1081 | Second pass of step2 (catches consecutive fg-tag chains missed by left-to-right single pass). |
| 4 | `step4.py` | temp_pwg3.txt | temp_pwg4.txt | 386 | Merges when `fg.`/`fgg.` is at the *start of content* of the second tag. Pattern: `</ls>.\s*<ls>fg. rest</ls>` |
| 5 | `step5.py` | temp_pwg4.txt | temp_pwg5.txt | 100 | Looping pass for orphan `fg.`/`fgg.` at content start not caught by step4. Handles `<is>` elements in tag content using tempered dot `(?:(?!</ls>).)*?`. Two sub-patterns: no-period (space only) and with-period between tags. |
| 6 | `step6.py` | temp_pwg5.txt | temp_pwg6.txt | 80 | Normalizes redundant sequences: `fg.. fg` (42) and `fgg.. fg` (38) → single `fg`. |
| 7 | `step7.py` | temp_pwg6.txt | temp_pwg7.txt | 13 | Splits `<ls>` tags where `fgg.` appears mid-content (separating subsequent references). Extracts author from before-text when `n` attribute is absent. Merges parenthetical refs in the after-content. Skips split when `fgg.` is inside parenthetical (e.g. `(No. 79. fgg.)`). Uses `re.sub(r'\.\s*$', '', ...)` instead of `rstrip('.')` to avoid double-period issues with `(p. 570.)` patterns. |
| 8 | `step8.py` | temp_pwg7.txt | temp_pwg8.txt | 13 | Applies manual corrections from `log1.txt`. Reads `log.txt` (output of `rg "fg[g][.]* " temp_pwg7.txt`) and `log1.txt` (human-corrected version), does line-by-line string replacement on the data. |

## Output Files

- `temp_pwgN.txt` — output after step N
- `temp_pwg8.txt` — final output
- `log.txt` — raw `rg` output of remaining `fg`/`fgg` patterns in temp_pwg7.txt
- `log1.txt` — manually corrected version of log.txt

## Key Details

### Step7 logic
- Regex: `r'<ls(?: n="([^"]*)")?>([^<]*(?:<(?!ls|/ls)[^>]*>[^<]*)*?)fgg\.\s*((?:(?!\s*</ls>).)+?)</ls>(\.)?'`
- The `(?!ls|/ls)` lookahead prevents the content group from overreaching across `<ls>` boundaries.
- Parenthetical merge: splits `(S. 570)` across `\.\s+` then re-merges fragments that start with `(` and end with `)`.
- `has_content` check skips split when after-fgg content is just `)` (fgg inside parenthetical).
- Double-period fix: `re.sub(r'\.\s*$', '', before.rstrip())` correctly handles `(p. 570.)` cases.

### Step8
- Simple string substitution: each line of `log.txt` is replaced by the corresponding line of `log1.txt`.
- Only lines that differ between the two files trigger a replacement.
- Covers 13 cases: n-attribute fg/fgg extraction + ls-internal fg splits.
