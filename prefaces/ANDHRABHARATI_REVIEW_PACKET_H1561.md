# Review packet — PWG / PW front-matter EN (for @Andhrabharati)

_Created: 24-07-2026 · Last updated: 24-07-2026_

**Handoff:** [H1561](https://github.com/gasyoun/Uprava/blob/main/handoffs/H1561-Sonnet_PWG_andhrabharati-pref-review-packet_24.07.26.md)  
**Tracking issue:** [PWG#210](https://github.com/sanskrit-lexicon/PWG/issues/210)  
**Model (this pass):** Grok 4.5 (`grok-4.5`)  
**Non-goal:** full dictionary re-review; no re-OCR in this packet.

This is a **bounded sample** (3 page kinds × 2 dictionaries + ~10 abbreviation keys each with body counts), not an open-ended “please review everything” request.

Body counts come from the committed pref×body cross-check ([`pref_abbr_crosscheck.py`](https://github.com/sanskrit-lexicon/csl-guides/blob/main/scripts/pref_abbr_crosscheck.py), [csl-guides#123](https://github.com/sanskrit-lexicon/csl-guides/issues/123)): string occurrence in the dictionary body `.txt` (prioritisation only; **print/scan remains truth** for expansions). Counts verified 24-07-2026 against `pwg_pref_abbr_crosscheck.tsv` / `pw_pref_abbr_crosscheck.tsv`.

---

## 1. Sample pages (DE | EN)

All sample github.io URLs returned **HTTP 200** on 24-07-2026.

### 1.1 Title

| Dict | DE (source OCR) | EN |
|------|-----------------|----|
| **PWG** | [pwgpref01.md](https://sanskrit-lexicon.github.io/PWG/prefaces/pwgpref01.md) | [pwgpref01.en.md](https://sanskrit-lexicon.github.io/PWG/prefaces/pwgpref01.en.md) |
| **PW (PWK)** | [pwpref01.md](https://sanskrit-lexicon.github.io/PWK/prefaces/pwpref01.md) | [pwpref01.en.md](https://sanskrit-lexicon.github.io/PWK/prefaces/pwpref01.en.md) |

**PWG excerpt pair**

| DE | EN |
|----|----|
| SANSKRIT-WÖRTERBUCH … BEARBEITET VON Otto Böhtlingk und Rudolph Roth. … ERSTER THEIL. DIE VOCALE. St. Petersburg 1855 | SANSKRIT DICTIONARY (Sanskrit-Wörterbuch) … COMPILED BY Otto Böhtlingk und Rudolph Roth. … PART ONE. THE VOWELS. St. Petersburg 1855 |

**PW excerpt pair**

| DE | EN |
|----|----|
| SANSKRIT-WÖRTERBUCH IN KÜRZERER FASSUNG BEARBEITET VON OTTO BÖHTLINGK. … 1879. | SANSKRIT DICTIONARY IN SHORTER VERSION PREPARED BY OTTO BÖHTLINGK. … 1879. |

### 1.2 Vorwort / Foreword

| Dict | DE | EN |
|------|----|----|
| **PWG** | [pwgpref02.md](https://sanskrit-lexicon.github.io/PWG/prefaces/pwgpref02.md) | [pwgpref02.en.md](https://sanskrit-lexicon.github.io/PWG/prefaces/pwgpref02.en.md) |
| **PW** | [pwpref02.md](https://sanskrit-lexicon.github.io/PWK/prefaces/pwpref02.md) | [pwpref02.en.md](https://sanskrit-lexicon.github.io/PWK/prefaces/pwpref02.en.md) |

**PWG opening (register sample)**

| DE | EN |
|----|----|
| In den dreissig und etlichen Jahren, welche verstrichen sind, seitdem in Calcutta H. H. Wilson's Sanskrit-Englisches Wörterbuch erschien, hat das Studium der Sanskrit-Sprache und Literatur unter uns so mächtige Fortschritte gemacht, dass der Versuch, durch eine neue Bearbeitung des Wortschatzes dem sich immer weiter ausbreitenden und höher wachsenden Bau sicherere Stützen und Pfeiler zu geben, wohl an der Zeit sein möchte. | In the thirty-odd years that have passed since H. H. Wilson's Sanskrit–English Dictionary appeared in Calcutta, the study of the Sanskrit language and literature has made such powerful advances among us that the attempt to give firmer supports and pillars, through a new treatment of the vocabulary, to an edifice that is ever spreading further and growing higher may well be timely. |

**PW opening (register sample)**

| DE | EN |
|----|----|
| Neben dem vor wenigen Jahren vollendeten sogenannten Petersburger Wörterbuch in sieben Bänden schien es angemessen, eine kürzere Bearbeitung herzustellen, welche dem Bedürfniss der Anfänger und solcher Benützer entspräche, für welche der dort gegebene Apparat zu reich ist. | Alongside the so-called Petersburg Dictionary in seven volumes, completed a few years ago, it seemed fitting to produce a shorter treatment, one that would meet the needs of beginners and of those users for whom the apparatus given there is too rich. |

### 1.3 Abbreviations

| Dict | DE | EN |
|------|----|----|
| **PWG** (pref07) | [pwgpref07.md](https://sanskrit-lexicon.github.io/PWG/prefaces/pwgpref07.md) | [pwgpref07.en.md](https://sanskrit-lexicon.github.io/PWG/prefaces/pwgpref07.en.md) |
| **PW** (pref03) | [pwpref03.md](https://sanskrit-lexicon.github.io/PWK/prefaces/pwpref03.md) | [pwpref03.en.md](https://sanskrit-lexicon.github.io/PWK/prefaces/pwpref03.en.md) |

**PWG legend line**

| DE | EN |
|----|----|
| (Gedruckte Werke aus der Sanskrit-Literatur, die nur ganz gelegentlich citirt werden, sind mit einem Sternchen bezeichnet.) | (Printed works from Sanskrit literature that are cited only very occasionally are marked with an asterisk.) |

**Sample key pair (same key, both dicts)**

| | DE expansion | EN expansion |
|--|--------------|--------------|
| **PWG `AV.`** | Atharvavedasaṃhitâ, herausg. von R. Roth und W. D. Whitney. Berlin bei F. Dümmler. 1855. 8°. | Atharvavedasaṃhitâ, edited by R. Roth and W. D. Whitney. Berlin at F. Dümmler. 1855. 8°. |
| **PW `AV.`** | Atharvaveda, Ausg. von Roth und Whitney (Roth). | Atharvaveda, ed. by Roth and Whitney (Roth). |

Consolidated EN (full lists):

- PWG: https://sanskrit-lexicon.github.io/PWG/prefaces/pwgpref_all.en.md  
- PW: https://sanskrit-lexicon.github.io/PWK/prefaces/pwpref_all.en.md  

Methods / cite: [PWG METHODS](https://github.com/sanskrit-lexicon/PWG/blob/main/prefaces/METHODS.md) · [PWK METHODS](https://github.com/sanskrit-lexicon/PWK/blob/main/prefaces/METHODS.md)

---

## 2. Abbreviation keys × body counts

**How to read:** `body_count` = occurrences of the key string in the CDSL body export (`pwg.txt` / `pw.txt`). High count ≠ “expansion is correct”; zero ≠ “key is wrong in the legend” (body markup or alternate forms can hide a key). Flag `pref_only` means zero body hits under the cross-check’s match rules.

### 2.1 PWG (keys from abbreviations pages; sample of 10)

Source reports: [pwg_pref_abbr_crosscheck.md](https://github.com/sanskrit-lexicon/csl-guides/blob/main/scripts/out/pwg_pref_abbr_crosscheck.md) (395 keys parsed; 257 non-short hits).

| key | expansion (short) | body_count | note |
|-----|-------------------|----------:|------|
| `MBh.` | Mahābhārata, ed. Calc. | 67272 | top hit |
| `RV.` | Ṛgveda (Maṇḍala / Sūkta / Ṛc) | 58146 | top hit |
| `Bhag.` | Bhagavadgītā (Schlegel) | 33406 | on pref07 |
| `Bhâg. P.` | Bhāgavatapurāṇa | 30744 | on pref07 |
| `AK.` | Amarakośa (Colebrooke / Loiseleur) | 28273 | on pref07 |
| `AV.` | Atharvavedasaṃhitā (Roth & Whitney 1855) | 21528 | on pref07; long expansion note on numbering |
| `Ait. Br.` | Aitareyabrāhmaṇa (Pañcikā / chapter) | 5223 | on pref07 |
| `Bhartṛ.` | Bhartṛhari (Bohlen) | 1383 | on pref07 |
| `Burn. Intr.` | Burnouf, *Introduction… Buddhisme* (1844) | 1065 | on pref07 |
| `Âçv. Çr.` | Āśvalāyana’s Śrautasūtrāṇi (Ms., 12 Adhyāya) | 0 | `pref_only` — worth checking body form vs legend |

### 2.2 PW / PWK (keys from pref03+; sample of 10)

Source reports: [pw_pref_abbr_crosscheck.md](https://github.com/sanskrit-lexicon/csl-guides/blob/main/scripts/out/pw_pref_abbr_crosscheck.md) (302 keys; 209 non-short hits).

| key | expansion (short) | body_count | note |
|-----|-------------------|----------:|------|
| `Chr.` | Böhtlingk Chrestomathie, 2nd ed. | 7328 | top hit |
| `MBh.` | Mahābhārata (Bombay numbering) | 4710 | top hit |
| `Spr.` | *Indische Sprüche* (Böhtlingk) | 3272 | top hit |
| `Âpast.` | Āpastamba Dharmasūtra (Bühler) | 3078 | on pref03 |
| `AV.` | Atharvaveda (Roth & Whitney; Roth) | 2084 | on pref03 |
| `ṚV.` | Ṛgveda (Roth) | 1909 | — |
| `Med.` | Medinīkośa | 1870 | — |
| `AK.` | Amarakośa (Loiseleur) | 1478 | on pref03 |
| `Ait. Br.` | Aitareyabrāhmaṇa (Haug) | 273 | on pref03 |
| `Âçv. Çr.` | Āśvalāyana Śrautasūtra (Bibl. ind.) | 0 | `pref_only` — same pattern as PWG |

---

## 3. Explicit asks for @Andhrabharati

Concrete, sample-scoped questions (reply on [PWG#210](https://github.com/sanskrit-lexicon/PWG/issues/210) is enough):

1. **EN Vorwort register** — Looking only at the PWG and PW foreword excerpts above (and optionally the full pref02 pages): is the English scholarly register acceptable, or are there spots that sound too free / too stiff / wrong for 19th-c. Indological German?
2. **Abbr expansions vs print legend** — For the ten PWG and ten PW keys in §2: are the expansions faithful to the printed abbreviation list (not to modern preferred titles)? Flag any key where EN or DE OCR expansion diverges from your materials.
3. **Keys wrong vs your materials** — Any of the sample keys (or known high-frequency ones like `MBh.`, `RV.` / `ṚV.`, `AV.`) wrong, split differently, or obsolete relative to how you work with PWG/PWK day to day?
4. **Optional:** for `pref_only` rows (`Âçv. Çr.` etc.), do you recognise a body spelling that our string match would miss?

No need to re-OCR or re-review the full abbreviation lists unless something in this sample looks systematically off.

---

## 4. Results table (H1561 acceptance)

| Check | Result |
|-------|--------|
| Packet on PWG#210 with @Andhrabharati + concrete asks | yes (this file + issue comment) |
| Sample github.io links HTTP 200 | yes (7/7 checked 24-07-2026) |
| ~10 abbr keys × body_count from `pref_abbr_crosscheck` | yes (10 PWG + 10 PW) |
| Full dictionary re-review / close #210 without reply | out of scope — not done |

_Dr. Mārcis Gasūns_
