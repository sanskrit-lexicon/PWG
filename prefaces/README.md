# PWG — Front Matter (Prefaces, Title Pages, Abbreviation Lists)

OCR transcriptions **and English + Russian translations** of the front matter of the **Sanskrit-Wörterbuch** (Otto Böhtlingk & Rudolph Roth, *Großes Petersburger Wörterbuch*), St. Petersburg, Kaiserliche Akademie der Wissenschaften, 1855–1875.

Source: the Cologne digitization scan pages under
[pwgpref.html](https://sanskrit-lexicon.uni-koeln.de/scans/csldev/csldoc/build/dictionaries/prefaces/pwgpref.html).

For each scan page there are three files:

| suffix | language | content |
|---|---|---|
| `pwgprefNN.md` | German | faithful OCR transcription (original 19th-c. orthography) |
| `pwgprefNN.en.md` | English | translation of the German |
| `pwgprefNN.ru.md` | Russian | translation of the German |

Files carry a YAML header (source scan, section, volume, source URL; translations also carry `language` and `translation_of`). Sanskrit appears in Devanāgarī Unicode or Böhtlingk–Roth romanization as printed and is left **verbatim** in the translations; personal names, work titles, and bibliographic abbreviations are likewise kept as printed. Uncertain readings are marked `[?]`, unreadable spots `[illegible]`. The original PNGs are kept under [scans/](scans/).

## Consolidated single-file editions

The complete front matter is also assembled into one file per language (all 27 pages in order, with a table of contents):

| language | file |
|---|---|
| German (Deutsch) | [pwgpref_all.de.md](pwgpref_all.de.md) |
| English | [pwgpref_all.en.md](pwgpref_all.en.md) |
| Russian (русский) | [pwgpref_all.ru.md](pwgpref_all.ru.md) |

These are generated from the per-page files by [build_combined.py](build_combined.py) (`python build_combined.py`); edit the per-page files and re-run to regenerate.

## Contents

| # | Section | Vol. | German | English | Russian |
|---|---------|------|--------|---------|---------|
| 1 | Title, vol. 1 (*Die Vocale*, 1855) | 1 | [de](pwgpref01.md) | [en](pwgpref01.en.md) | [ru](pwgpref01.ru.md) |
| 2 | Foreword, 1 | 1 | [de](pwgpref02.md) | [en](pwgpref02.en.md) | [ru](pwgpref02.ru.md) |
| 3 | Foreword, 2 | 1 | [de](pwgpref03.md) | [en](pwgpref03.en.md) | [ru](pwgpref03.ru.md) |
| 4 | Foreword, 3 | 1 | [de](pwgpref04.md) | [en](pwgpref04.en.md) | [ru](pwgpref04.ru.md) |
| 5 | Foreword, 4 | 1 | [de](pwgpref05.md) | [en](pwgpref05.en.md) | [ru](pwgpref05.ru.md) |
| 6 | Foreword, 5 | 1 | [de](pwgpref06.md) | [en](pwgpref06.en.md) | [ru](pwgpref06.ru.md) |
| 7 | Abbreviations, 1 | 1 | [de](pwgpref07.md) | [en](pwgpref07.en.md) | [ru](pwgpref07.ru.md) |
| 8 | Abbreviations, 2 | 1 | [de](pwgpref08.md) | [en](pwgpref08.en.md) | [ru](pwgpref08.ru.md) |
| 9 | Abbreviations, 3 | 1 | [de](pwgpref09.md) | [en](pwgpref09.en.md) | [ru](pwgpref09.ru.md) |
| 10 | Abbreviations, 4 | 1 | [de](pwgpref10.md) | [en](pwgpref10.en.md) | [ru](pwgpref10.ru.md) |
| 11 | Abbreviations, 5 | 1 | [de](pwgpref11.md) | [en](pwgpref11.en.md) | [ru](pwgpref11.ru.md) |
| 12 | Title, vol. 2 (क — ट, 1858) | 2 | [de](pwgpref12.md) | [en](pwgpref12.en.md) | [ru](pwgpref12.ru.md) |
| 13 | Addenda to vol. 1 | 2 | [de](pwgpref13.md) | [en](pwgpref13.en.md) | [ru](pwgpref13.ru.md) |
| 14 | Addenda to vol. 2 | 2 | [de](pwgpref14.md) | [en](pwgpref14.en.md) | [ru](pwgpref14.ru.md) |
| 15 | Foreword, vol. 2 | 2 | [de](pwgpref15.md) | [en](pwgpref15.en.md) | [ru](pwgpref15.ru.md) |
| 16 | Abbreviations, vol. 2 (additions) | 2 | [de](pwgpref16.md) | [en](pwgpref16.en.md) | [ru](pwgpref16.ru.md) |
| 17 | Title, vol. 3 (1861) | 3 | [de](pwgpref17.md) | [en](pwgpref17.en.md) | [ru](pwgpref17.ru.md) |
| 18 | Foreword, vol. 3 | 3 | [de](pwgpref18.md) | [en](pwgpref18.en.md) | [ru](pwgpref18.ru.md) |
| 19 | Abbreviations, vol. 3 (additions) | 3 | [de](pwgpref19.md) | [en](pwgpref19.en.md) | [ru](pwgpref19.ru.md) |
| 20 | Title, vol. 4 (1865) | 4 | [de](pwgpref20.md) | [en](pwgpref20.en.md) | [ru](pwgpref20.ru.md) |
| 21 | Foreword, vol. 4 | 4 | [de](pwgpref21.md) | [en](pwgpref21.en.md) | [ru](pwgpref21.ru.md) |
| 22 | Title, vol. 5 (1868) | 5 | [de](pwgpref22.md) | [en](pwgpref22.en.md) | [ru](pwgpref22.ru.md) |
| 23 | Foreword, vol. 5 (part 1) | 5 | [de](pwgpref23.md) | [en](pwgpref23.en.md) | [ru](pwgpref23.ru.md) |
| 24 | Foreword, vol. 5 (part 2) | 5 | [de](pwgpref24.md) | [en](pwgpref24.en.md) | [ru](pwgpref24.ru.md) |
| 25 | Title, vol. 6 (1871) | 6 | [de](pwgpref25.md) | [en](pwgpref25.en.md) | [ru](pwgpref25.ru.md) |
| 26 | Title, vol. 7 (1875) | 7 | [de](pwgpref26.md) | [en](pwgpref26.en.md) | [ru](pwgpref26.ru.md) |
| 27 | Foreword, vol. 7 (final) | 7 | [de](pwgpref27.md) | [en](pwgpref27.en.md) | [ru](pwgpref27.ru.md) |

## Notes

- The forewords are the connected German prose (pages 2–6, 15, 18, 21, 23–24, 27). Title pages are short; the abbreviation lists (7–11, 16, 19) and addenda (13–14) are bibliographic / lexicographic — in the translations only the German scaffolding (headings, notes, glosses, "instead of … read …") is rendered, while every abbreviation key, source title, Sanskrit form, and reference is kept verbatim.
- The forewords are signed by Böhtlingk and Roth; closing places/dates are kept where printed (vol. 2: Tübingen, 14/26 Oct 1858; vol. 4: 17/29 Nov 1864; vol. 7: Jena und Tübingen, 4 Aug 1875). The vol.-5 foreword (24) is signed but bears **no** printed date.
- In the Russian files, personal surnames are kept in Latin script as printed in the original (with conventional Cyrillic forms used where helpful); this can be normalised to full Cyrillic if the project prefers.
- The small running header and the "Institute of Indology & Tamil Studies, Cologne University … 9.2.2007" digitizer footer are omitted from all files.
