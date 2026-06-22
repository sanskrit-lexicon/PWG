# Base file

cd sanskrit-lexicon/csl-orig

git show c49ea17:v02/pwg/pwg.txt > temp_pwg0.txt
mv temp_pwg0.txt /path/to/PWG/pwgissues/issues/issue193/temp_pwg0.txt

# Opencode Big Pickle AI analysis

## Prompt

Identify `ls n="..."` entries in `temp_pwg0.txt` where the `n` attribute value ends with an alphabet character (not a period), and determine which are missing a terminal period (abbreviation errors) vs. valid full names/titles.

## Analysis

### Method

1. `rg -o 'ls n="[^"]*[A-z]"' temp_pwg0.txt | sort -u` — extract all distinct `ls n` values ending with a letter.
2. For each entry, count occurrences both without a period (`rg -c 'ls n="NAME"'`) and with a period (`rg -c 'ls n="NAME[.]"'`).

### Results

#### Category 1: Full names / titles (no period expected)

These are proper names, author names, book titles, catalog numbers, Roman numerals, or full words where the bare form is correct. The `with_period` count is 0.

| Entry | without_period | with_period |
|---|---|---|
| AINSLIE | 1 | 0 |
| ANUPADA | 5 | 0 |
| AV. Padapāṭha | 2 | 0 |
| BENFEY | 1 | 0 |
| BHARATA | 1 | 0 |
| BURNOUF | 1 | 0 |
| CARAKA | 38 | 0 |
| COWELL | 1 | 0 |
| Calcutta | 1 | 0 |
| Devarāja | 2 | 0 |
| Durgasiṃha | 4 | 0 |
| FOUCAUX | 1 | 0 |
| HIOUEN-THSANG | 48 | 0 |
| HIOUENTHSANG | 3 | 0 |
| HĀLA | 12 | 0 |
| Hist. de HIOUEN-THSANG | 1 | 0 |
| Hist. de la vie de HIOUEN-THSANG | 2 | 0 |
| JAIMINI | 1 | 0 |
| Journ. of the As. Soc. of Bombay | 1 | 0 |
| KRIYĀSAMUCCAYA | 1 | 0 |
| Kullūka | 1 | 0 |
| KÖPPEN | 2 | 0 |
| KĀLACAKRA | 24 | 0 |
| KĀTANTRA | 2 | 0 |
| KṚṢISAṂGRAHA | 1 | 0 |
| NIDĀNA | 1 | 0 |
| NĀGĀNANDA | 1 | 0 |
| Padapāṭha | 238 | 0 |
| PAÑCAT. ed. Bomb. IV & V | 1 | 0 |
| REINAUD, Mém. sur lʼInde | 9 | 0 |
| SOM. NALA | 2 | 0 |
| STENZLER | 1 | 0 |
| UPALEKHA | 1 | 0 |
| VAJRASŪCI | 1 | 0 |
| VARARUCI | 2 | 0 |
| VEDĀNTA | 1 | 0 |
| Verz. d. Oxf. H. 109,a | 1 | 0 |
| Verz. d. Oxf. H. 71,a | 1 | 0 |
| Vie de HIOUEN-THSANG | 25 | 0 |
| Vie de Hiouen-thsang | 1 | 0 |
| VĀMANA | 1 | 0 |
| WASSILJEW | 178 | 0 |
| WEBER, HĀLA | 1 | 0 |
| WEBER, Omina | 2 | 0 |
| WILSON, Sel. Works | 24 | 0 |
| WIND. Sancara | 3 | 0 |
| WINDISCHMANN, Sancara | 1 | 0 |
| WISE | 3 | 0 |
| Weber | 1 | 0 |
| YAŚNA | 1 | 0 |
| YAṢT | 1 | 0 |
| ṚV. Padapāṭha | 8 | 0 |

**Note:** `Padapāṭha` (238 occurrences, no period) appears as a standalone `ls` value as well as part of `AV. Padapāṭha` / `ṚV. Padapāṭha`. The bare occurrences should be verified as standalone tags vs. a regex substring match against multi-word entries.

#### Category 2: Likely missing a period

These are abbreviated source names where the majority form has a terminal period. The bare form is almost certainly an error.

| Entry | without_period | with_period | Assessment |
|---|---|---|---|
| AV | 1 | 2507 | Fix the bare `AV` to `AV.` (1 outlier) |
| BHĀG. P | 2 | 4234 | Fix to `BHĀG. P.` (last word `P` missing period) |
| DHĀTUP | 1 | 243 | Fix to `DHĀTUP.` |
| HIT | 1 | 456 | Fix to `HIT.` |
| KĀTY. ŚR | 3 | 1447 | Fix to `KĀTY. ŚR.` |
| MĀRK. P | 1 | 696 | Fix to `MĀRK. P.` |
| MEGH | 1 | 284 | Fix to `MEGH.` |
| P | 16 | 1721 | Fix to `P.` (16 bare occurrences) |
| R. GORR | 1 | 1151 | Fix to `R. GORR.` |
| Spr | 27 | 1717 | Fix to `Spr.` (27 bare occurrences) |
| ŚĀK | 21 | 778 | Fix to `ŚĀK.` (21 bare occurrences) |
| TS. PRĀT | 1 | 101 | Fix to `TS. PRĀT.` |
| Verz. d. B. H. No | 1 | 407 | Fix to `Verz. d. B. H. No.` (German "Nummer") |
| VOP | 1 | 303 | Fix to `VOP.` |

#### Category 3: Edge cases needing manual review

| Entry | without_period | with_period | Notes |
|---|---|---|---|
| HALL | 288 | 6 | Bare `HALL` (288x) dominates. The 6 instances of `HALL.` may be the errors, or `HALL` may actually be an abbreviation of "HALL." — needs manual inspection. |
| HIT. ed. SCHL | 1 | 1 | Equal counts (1 vs 1). Unclear which form is canonical. |
| MADHUS. ebend | 1 | 0 | "ebend" is German short for "ebenda" (ibid.). May or may not need a period — check convention. |
| SĀH | 1 | 2 | Marginal (total 3 occurrences). Likely `SĀH.` but verify. |
| p | 1 | 0 | Lowercase `p` appears once without period. May be a typo for `P.` |

### Summary of actionable fixes

The following abbreviations should have a period appended to the last word:

| Current | Fix to |
|---|---|
| `AV` | `AV.` |
| `BHĀG. P` | `BHĀG. P.` |
| `DHĀTUP` | `DHĀTUP.` |
| `HIT` | `HIT.` |
| `KĀTY. ŚR` | `KĀTY. ŚR.` |
| `MĀRK. P` | `MĀRK. P.` |
| `MEGH` | `MEGH.` |
| `P` | `P.` |
| `R. GORR` | `R. GORR.` |
| `Spr` | `Spr.` |
| `ŚĀK` | `ŚĀK.` |
| `TS. PRĀT` | `TS. PRĀT.` |
| `Verz. d. B. H. No` | `Verz. d. B. H. No.` |
| `VOP` | `VOP.` |

`p` (lowercase, 1 occurrence) needs manual inspection to determine its intended form.

## Step 1 script

`step1.py` applies all fixes (Category 2 + `HALL`, `HIT. ed. SCHL`, `MADHUS. ebend`, `SĀH`) to `temp_pwg0.txt` → `temp_pwg1.txt`.

```sh
python3 step1.py
```

Uses regex `ls n="VALUE"(?=[ >])` → `ls n="VALUE."` to ensure only exact attribute values are changed (not substrings like `AV` inside `AV. Padapāṭha`). All fixed entries verified — 0 bare forms remain in the output.

### Replacements applied

| Current | Fix to |
|---|---|
| `AV` | `AV.` |
| `BHĀG. P` | `BHĀG. P.` |
| `DHĀTUP` | `DHĀTUP.` |
| `HALL` | `HALL.` |
| `HIT` | `HIT.` |
| `HIT. ed. SCHL` | `HIT. ed. SCHL.` |
| `KĀTY. ŚR` | `KĀTY. ŚR.` |
| `MADHUS. ebend` | `MADHUS. ebend.` |
| `MĀRK. P` | `MĀRK. P.` |
| `MEGH` | `MEGH.` |
| `P` | `P.` |
| `R. GORR` | `R. GORR.` |
| `SĀH` | `SĀH.` |
| `Spr` | `Spr.` |
| `ŚĀK` | `ŚĀK.` |
| `TS. PRĀT` | `TS. PRĀT.` |
| `Verz. d. B. H. No` | `Verz. d. B. H. No.` |
| `VOP` | `VOP.` |
