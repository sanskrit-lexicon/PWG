# PWG — Petersburger Wörterbuch

_Created: 17-12-2017 · Last updated: 10-07-2026_

**PWG** (*Sanskrit-Wörterbuch*, Böhtlingk & Roth, 1855–1875) is the large,
seven-volume "Great Petersburg Dictionary" — the foundational Sanskrit–German
lexicon of the 19th century and the direct ancestor of Monier-Williams'
English dictionary. This repository is the correction and enrichment layer
for its Cologne digitisation, part of the [Sanskrit Lexicon](https://github.com/sanskrit-lexicon)
project's [Cologne Digital Sanskrit Dictionaries](https://www.sanskrit-lexicon.uni-koeln.de/)
initiative. A browsable landing page is published via GitHub Pages at
[sanskrit-lexicon.github.io/PWG](https://sanskrit-lexicon.github.io/PWG/).

## Why this matters

A scanned 19th-century dictionary is only as useful as its digital text is
trustworthy and its references are followable. PWG cites thousands of
literary sources by abbreviation (`RV.`, `MBH.`, `ŚĀK.`, …) — a scholar
reading an entry needs to click straight through to the actual scanned page
being cited, not just trust a typed reference. This repo's primary,
decade-long effort is building that click-through: turning `<ls>`
(literary-source) abbreviations into validated links to the scanned PDF
edition, alongside the ordinary digitisation work of fixing scan errors,
encoding problems, and markup inconsistencies. A large fraction of that
program is now finished (see Project Timeline below), and it currently feeds
downstream work such as the
[PWG→Russian translation layer](https://github.com/gasyoun/SanskritLexicography/tree/master/RussianTranslation)
and OCR'd front-matter editions.

The primary input is `pwg.xml`, maintained in the sibling
[pwgxml](https://github.com/sanskrit-lexicon/pwgxml) repository; corrections
found here are applied across related dictionaries (PW, MW, PWKVN, SCH) since
they share source material and markup conventions.

---

### Directories

| Directory | Contents |
|---|---|
| [`pwg_ls/`](https://github.com/sanskrit-lexicon/PWG/tree/main/pwg_ls) | Round 1 — extraction and analysis of `<ls>` (literary source) tags from pwg.xml |
| [`pwg_ls1/`](https://github.com/sanskrit-lexicon/PWG/tree/main/pwg_ls1) | Round 2 — authority/bibliography record refinement (begun Dec 2017) |
| [`pwg_ls2/`](https://github.com/sanskrit-lexicon/PWG/tree/main/pwg_ls2) | Round 3 — per-source corrections; subfolders named by abbreviation (`RV/`, `ak/`, `mbh1/`, …) |
| [`pwgissues/`](https://github.com/sanskrit-lexicon/PWG/tree/main/pwgissues) | One folder per GitHub issue (`issueNNN/` for analysis, `issueNNNfix/` for correction scripts) |
| [`verbs01/`](https://github.com/sanskrit-lexicon/PWG/tree/main/verbs01) | Early verb and upasarga analysis against PWG headwords |
| [`verbs01a/`](https://github.com/sanskrit-lexicon/PWG/tree/main/verbs01a) | Verb identification correlated with Monier-Williams (MW) dictionary (begun Mar 2020) |
| [`RussianWords/`](https://github.com/sanskrit-lexicon/PWG/tree/main/RussianWords) | Russian etymologies in PWG |
| [`pwgheader/`](https://github.com/sanskrit-lexicon/PWG/tree/main/pwgheader) | Volume and header metadata |
| [`prefaces/`](https://github.com/sanskrit-lexicon/PWG/tree/main/prefaces) | OCR'd front matter (titles, forewords, abbreviation lists, addenda) with EN/RU translations and consolidated single-file editions; methods + cite block in [`prefaces/METHODS.md`](https://github.com/sanskrit-lexicon/PWG/blob/main/prefaces/METHODS.md) |
| [`misc/`](https://github.com/sanskrit-lexicon/PWG/tree/main/misc) | Accent display, encoding conversion, and other utilities |

> An experimental LLM-assisted pilot (translation / literary-source targeting /
> structural-extraction / OCR-diff tracks over one dictionary slice — derived
> artifacts only, source untouched) lives on the separate
> [`deepseek-pilot`](https://github.com/sanskrit-lexicon/PWG/tree/deepseek-pilot/deepseek_pilot)
> branch, not on `main`. It is paused mid-scale-up and resumable (see the
> Status section below).

---

### How It Works

Corrections to `pwg.xml` are never made directly. Instead, scripts produce
**change files** (paired `old`/`new`/`ins`/`del` lines) that are applied by
`updateByLine.py` — the full change-file format and the end-to-end
snapshot → apply → validate → promote workflow are documented once, canonically,
in
[csl-corrections/docs/correction-workflow.md](https://github.com/sanskrit-lexicon/csl-corrections/blob/main/docs/correction-workflow.md).
A minimal `new` (replace) change file looks like:

```
1234 old original line text
1234 new replacement line text
```

All change files are UTF-8.

#### Issue workflow

Each GitHub issue gets a folder under
[`pwgissues/`](https://github.com/sanskrit-lexicon/PWG/tree/main/pwgissues):

- `issueNNN/` — analysis scripts, index files, and a `readme.txt` that serves
  as a running log of commands executed and results observed.
- `issueNNNfix/` — correction scripts applied to `pwg.xml` and sibling
  dictionaries (PW, MW, PWKVN, SCH, …). Newer issues may keep everything in
  `issueNNN/`.

#### Link-target workflow

For sources that need clickable page links:

1. Build a tab-separated index file mapping book sections (volume, chapter,
   verse) to PDF page numbers.
2. Run `make_js_index.py` to validate the index and produce `index.js`.
3. Run `lsfix2.py` to rewrite `<ls>` tags across all related dictionaries
   (PWG, PW, MW, etc.) with the link targets.

```mermaid
flowchart LR
    PDF["Source PDF"]
    IDX["index file\nTSV: section to page"]
    JS["index.js"]
    DICTS["PWG · PW · MW\nKVN · SCH · …"]

    PDF -->|"research"| IDX
    IDX -->|"make_js_index.py\nvalidate + build"| JS
    JS -->|"lsfix2.py\ninstall links"| DICTS
```

#### Literary source (`<ls>`) analysis pipeline

Run from `pwg_ls/pwg_dhaval/abbrvwork/`:

```sh
sh makeabbrv.sh
```

This runs: `abbrv.py` → AS→IAST transliteration → `php displayhtml.php` →
`abbrvoutput/display.html` for human review.

**Dependencies:** Python 3, [lxml](https://lxml.de/), PHP

---

### Project Timeline

| Period | Work |
|---|---|
| 2014 | Early experiments — Russian etymologies, accent processing |
| 2015 | Russian words extraction |
| 2016 | Bibliography digitization (`pwgbib`); foundation of literary source analysis |
| 2017 | Abbreviation extraction pipeline (`abbrvwork`); AS→IAST transcoding; `pwg_ls1` begun |
| 2018 | Russian work expanded |
| 2020 | Verb identification (`verbs01a`) correlated with MW verbs |
| 2021 | `pwg_ls2` begun; Rig-Veda `<ls>` markup; VN corrections from Nagabhushana Rao (@Andhrabharati) |
| 2022 | Per-source markup improvements: Spr. (II), AV, P., MBH, Ramayana, AmaraKosha |
| 2023 | Unknown and numeric `<ls>` cleanup |
| 2024 | Link target work: KATHAS, MANU, VN, and many more sources |
| 2025 | Link-splitting (#160) completed for 30+ sources: RAGH., MBH, M., KATHĀS., ŚĀK., TAITTIRĪYA texts, ŚAT. BR., MEGH., MĀLAV., and more; image quality improvements for vol. 6 (#161); additional link targets (#168, #169); automated index checking by Dhaval Patel |
| 2026 H1 | Repository organisation ([`CLAUDE.md`](https://github.com/sanskrit-lexicon/PWG/blob/main/CLAUDE.md), issue labelling, severity/milestone/project triage); AB (Andhrabharati) version reconciliation (#163, #180, #191); PWG front-matter OCR + EN/RU translations shipped ([`prefaces/`](https://github.com/sanskrit-lexicon/PWG/tree/main/prefaces)); repo-hygiene pass (structured PR template, changelog v1, Dependabot automerge, GitHub Pages landing page); an experimental DeepSeek-assisted pilot run over one dictionary slice on the [`deepseek-pilot`](https://github.com/sanskrit-lexicon/PWG/tree/deepseek-pilot) branch, then paused mid-scale-up |

---

### Status (as of 10-07-2026)

Two tracks are currently the active fronts:

1. **Content/front-matter** — OCR'd German front matter with EN/RU
   translations, published per-page and as consolidated single-file editions
   under [`prefaces/`](https://github.com/sanskrit-lexicon/PWG/tree/main/prefaces);
   most recently committed work.
2. **Markup/link-target** — the long-running `<ls>` program plus the
   Andhrabharati (AB) alternate-digitization merge (`<ab>` tag alignment
   finished at #180; v1 vs v1e diff tracked at #191).

An experimental LLM-assisted pilot on the
[`deepseek-pilot`](https://github.com/sanskrit-lexicon/PWG/tree/deepseek-pilot)
branch passed its go/no-go gate on all three runnable tracks (translate-EN,
literary-source targeting, structural extraction) at limit-20 scale, then began
a full scale-up that was stopped mid-run; it is resumable but not currently
active, and lives only on that branch. It produces derived artifacts only — the
canonical `pwg.xml`/`pwg.txt` source is never touched by it.

---

### Projects & Milestones

Work is organised into four GitHub Projects (org-level kanban boards), each
mirroring a milestone. Open/closed counts below are current as of 10-07-2026;
consult the linked milestones for live numbers.

| Project | Milestone | Open | Closed | Scope |
|---|---|---|---|---|
| [**Dictionary to Book**](https://github.com/orgs/sanskrit-lexicon/projects/5) | [milestone](https://github.com/sanskrit-lexicon/PWG/milestone/1) | 11 | 71 | Making all literary source abbreviations click-through to scanned source pages — link targets and link splitting |
| [**Structured Data**](https://github.com/orgs/sanskrit-lexicon/projects/7) | [milestone](https://github.com/sanskrit-lexicon/PWG/milestone/3) | 6 | 35 | XML markup normalization, structured data improvements, and resolving interpretation questions |
| [**Digitization Quality**](https://github.com/orgs/sanskrit-lexicon/projects/6) | [milestone](https://github.com/sanskrit-lexicon/PWG/milestone/2) | 2 | 33 | Fixing errors from the original digitization: scan quality, encoding, text corrections, bugs |
| [**Major Enhancements**](https://github.com/orgs/sanskrit-lexicon/projects/8) | [milestone](https://github.com/sanskrit-lexicon/PWG/milestone/4) | 8 | 12 | Large new content additions: Cologne/Andhrabharati material, Weber's Nachlass, verb markup, bibliography |

```mermaid
pie title Closed issues by milestone
    "Dictionary to Book" : 71
    "Structured Data" : 35
    "Digitization Quality" : 33
    "Major Enhancements" : 12
```

```mermaid
pie title Open issues by milestone
    "Dictionary to Book" : 11
    "Major Enhancements" : 8
    "Structured Data" : 6
    "Digitization Quality" : 2
```

---

### Labels

Every issue carries one **type** label and one **severity** label.

#### Type

| Label | Meaning |
|---|---|
| `link-target` | Building a click-through from a `<ls>` abbreviation to scanned PDF pages: researching the source, constructing a tab-separated index, and installing links across all related dictionaries |
| `link-splitting` | Combined references like `SOURCE N,N` that resolve to a single target need to be split into individual per-page links |
| `markup` | Normalising the content or structure of XML tags: `<ls>`, `<lex>`, and other elements |
| `text-correction` | Corrections to the German definitions or Sanskrit headwords in the dictionary text |
| `content-enhancement` | Additions that go beyond correction — new material, display upgrades, or structural improvements |
| `encoding` | SLP1/AS/IAST transcoding issues, character rendering (Greek, accents), hyphen/dash normalisation |
| `scan-quality` | Replacing blurry, skewed, or missing scan pages with clearer images |
| `bug` | Broken behaviour in links, XML structure, or download files |
| `question` | Scholarly or editorial questions requiring research before any code change |

#### Severity

| Label | Meaning |
|---|---|
| `minor` | Targeted, self-contained fix — typically a handful of lines or a single file |
| `medium` | Standard unit of work — building one link-target index, a batch of markup corrections, or a moderate content addition |
| `hard` | Large or complex effort spanning many sources, files, or dictionaries |

The org-wide issue taxonomy (label colours, milestone-by-type assignment,
multi-type priority order) is documented in the
[Cologne tooling runbook](https://github.com/sanskrit-lexicon/csl-observatory/blob/main/runbook/cologne-tooling-runbook.md).

---

### Contributors

- **Jim Funderburk** ([@funderburkjim](https://github.com/funderburkjim)) — project lead
- **Mārcis Gasūns** ([@gasyoun](https://github.com/gasyoun)) — Russian etymologies, accents, tooling, issue and project organisation
- **Dhaval Patel** ([@drdhaval2785](https://github.com/drdhaval2785)) — automation of link-splitting and index checking
- **Nagabhushana Rao** (@Andhrabharati) — VN text corrections and index data
- **Thomas Malten** — original bibliography digitization (`pwgbib_orig.txt`)

---

_Dr. Mārcis Gasūns_
