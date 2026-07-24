# PWG front-matter OCR — methods and citation

_Created: 24-07-2026 · Last updated: 24-07-2026_

This note documents how the **PWG** (`prefaces/`) front-matter editions were produced so they can be treated as citable research objects. Page inventory and reading notes live in [README.md](README.md). Public index: [OCR'd prefaces](https://sanskrit-lexicon.github.io/csl-guides/dictionaries/ocr-prefaces). Operator manual: [Preface OCR pipeline](https://sanskrit-lexicon.github.io/csl-guides/dictionaries/preface-ocr-pipeline).

---

## What this is

Faithful Markdown OCR of the **Vorspann** of the *Sanskrit-Wörterbuch* (Otto Böhtlingk & Rudolph Roth, *Großes Petersburger Wörterbuch*), St. Petersburg, Kaiserliche Akademie der Wissenschaften, **1855–1875**, with English and Russian translations.

| Item | Value |
|---|---|
| Dictionary code | **PWG** |
| Repo | [sanskrit-lexicon/PWG](https://github.com/sanskrit-lexicon/PWG) |
| Source language | German (19th-c. orthography preserved) |
| Page count | **27** scan pages |
| Languages shipped | DE (source) · EN · RU |
| Consolidated editions | [pwgpref_all.de.md](pwgpref_all.de.md) · [pwgpref_all.en.md](pwgpref_all.en.md) · [pwgpref_all.ru.md](pwgpref_all.ru.md) |
| GitHub Pages (EN) | https://sanskrit-lexicon.github.io/PWG/prefaces/pwgpref_all.en.md |
| Tracking notice | [PWG#210](https://github.com/sanskrit-lexicon/PWG/issues/210) |

---

## Scan source

| Field | Value |
|---|---|
| Cologne index | [pwgpref.html](https://sanskrit-lexicon.uni-koeln.de/scans/csldev/csldoc/build/dictionaries/prefaces/pwgpref.html) |
| Per-page HTML | `…/prefaces/pwgpref/pwgprefNN.html` (NN = 01–27) |
| Image base | `https://sanskrit-lexicon.uni-koeln.de/scans/csldev/csldoc/build/_images/` |
| Local mirrors | [scans/](scans/) (27 PNGs, e.g. `pwg1-0000--01.png` …) |
| Page order | **csldoc toctree order** (not lexical sort of image filenames; PWG had filename swaps between some Foreword/Abbreviations pages) |

Each per-page file carries YAML: `source_scan`, `source_page`, `volume`, `source_url`.

### Page inventory (summary)

| Vol. | Sections (NN) |
|---:|---|
| 1 | Title; Foreword 1–5; Abbreviations 1–5 (`01`–`11`) |
| 2 | Title; Addenda vol. 1–2; Foreword; Abbreviations additions (`12`–`16`) |
| 3 | Title; Foreword; Abbreviations additions (`17`–`19`) |
| 4 | Title; Foreword (`20`–`21`) |
| 5 | Title; Foreword parts 1–2 (`22`–`24`) |
| 6 | Title (`25`) |
| 7 | Title; Foreword final (`26`–`27`) |

Full table with links: [README.md § Contents](README.md#contents).

---

## OCR policy (engines A / B)

Production skill: **`/cologne-preface-ocr`** (Claude Code command; Codex twin available).

| Engine | Role | Mechanism |
|---|---|---|
| **A — Vision band OCR** | **Author** of canonical `pwgprefNN.md` | Native-resolution column/band crops (longest side ≲ ~1900 px); vision model → faithful transcription. Never OCR a full downsampled page (fabricates text). |
| **B — Tesseract crop-then-OCR** | **Audit only** on CDSL | Optional comparison layer; **must not** auto-overwrite Engine A. Useful for coverage/layout flags. |

Hard rule: Engine B text is never promoted into canonical pages without a human/vision re-check of the scan band. Bake-off evidence (A as gold): [PD COMPARISON_PWG_OCR_A_VS_B.md](https://github.com/sanskrit-lexicon/PD/blob/main/COMPARISON_PWG_OCR_A_VS_B.md).

PD’s `feat/ocr-v2-pipeline` is a **sibling** pipeline for Deccan College PDF front matter — not a second author for CDSL PWG pages.

### Uncertainty markers

| Marker | Meaning |
|---|---|
| `[?]` | Uncertain reading (glyph/word) |
| `[illegible]` | Unreadable locus on the scan |

Digitizer running headers and the Cologne “Institute of Indology & Tamil Studies …” stamp/footer are **omitted** (not part of the printed book).

---

## Translation policy

- Source `.md` keeps 19th-c. German orthography in **prose** (*Theil, Litteratur, dass, citirt, …*).
- `.en.md` / `.ru.md` translate German prose scaffolding only.
- Left **verbatim** in all languages: personal names, work **titles** in expansions, years, and reference numbers.
- **Abbreviation keys (sigla):** aligned to the **human-edited body** `csl-orig/v02/pwg/pwg.txt` naming of the same works (H1569). OCR alone is not the authority for how a work is *named* in the legend. Every key rewrite is logged in the csl-guides change-log meta doc ([pwg_pref_key_body_align_changes.md](https://github.com/sanskrit-lexicon/csl-guides/blob/main/scripts/out/pwg_pref_key_body_align_changes.md)). Policy: [pref-body-naming-authority](https://github.com/sanskrit-lexicon/csl-guides/blob/main/docs/dictionaries/pref-body-naming-authority.md).
- On abbreviation lists and addenda, only headings, notes, and glosses such as “instead of … read …” are rendered in translation; keys follow the body-aligned source form.

---

## Regeneration

Consolidated single-file editions are built from per-page files:

```text
cd prefaces
python build_combined.py
```

Edit `pwgprefNN.md` / `.en.md` / `.ru.md`, then re-run. Do not hand-edit `pwgpref_all.*` except via the builder.

---

## Provenance

| Field | Value |
|---|---|
| Workflow | `/cologne-preface-ocr` (vision author; optional Tesseract audit) |
| First landed (approx.) | 2026 H1 (see repo history for `prefaces/`) |
| Methods note | 24-07-2026 (H1558) |
| Agent attribution | Production path = Claude Code vision skill (default tier Fable 5 / Opus 4.8 fallback); commits may land under the maintainer account after agent runs — see [preface-ocr-pipeline](https://sanskrit-lexicon.github.io/csl-guides/dictionaries/preface-ocr-pipeline) |
| License of this repo’s digital work | CC-BY-SA-4.0 (see root [CITATION.cff](../CITATION.cff) and [LICENSE](../LICENSE)) |
| Printed source | Public-domain 19th-c. imprint; always cite the book as well as the OCR |

---

## How to cite

Cite **two layers** when you use these files: (1) the printed PWG, (2) this digital front-matter OCR.

### 1. Printed source (preferred-citation in CITATION.cff)

Böhtlingk, Otto, and Rudolph Roth. *Sanskrit-Wörterbuch*. St. Petersburg: Kaiserliche Akademie der Wissenschaften, 1855–1875.

### 2. Front-matter OCR edition (this directory)

Gasūns, Mārcis, and Cologne Digital Sanskrit Lexicon project contributors. 2026. “PWG front-matter OCR (title pages, forewords, abbreviation lists, addenda): German transcription with English and Russian translations.” In *sanskrit-lexicon/PWG*, `prefaces/`. https://github.com/sanskrit-lexicon/PWG/tree/main/prefaces · methods: https://github.com/sanskrit-lexicon/PWG/blob/main/prefaces/METHODS.md · English consolidated: https://sanskrit-lexicon.github.io/PWG/prefaces/pwgpref_all.en.md

#### BibTeX

```bibtex
@misc{pwg_pref_ocr_2026,
  author       = {Gasūns, Mārcis and Cologne Digital Sanskrit Lexicon project contributors},
  title        = {{PWG} front-matter {OCR}: German transcription with English and Russian translations},
  year         = {2026},
  howpublished = {GitHub repository \texttt{sanskrit-lexicon/PWG}, directory \texttt{prefaces/}},
  url          = {https://github.com/sanskrit-lexicon/PWG/tree/main/prefaces},
  note         = {Methods: https://github.com/sanskrit-lexicon/PWG/blob/main/prefaces/METHODS.md. Scan source: Cologne csldoc pwgpref. License of digital edition: CC-BY-SA-4.0.}
}
```

Root [CITATION.cff](../CITATION.cff) points at both the printed book (`preferred-citation`) and this OCR package (`message` + `identifiers`). A Zenodo DOI may be added later when a release is cut; until then use the GitHub / Pages URLs above.

---

_Dr. Mārcis Gasūns_
