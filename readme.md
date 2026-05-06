
## PWG Sanskrit Dictionary Processing

Scripts and data for correcting and enriching the **PWG** (*Petersburger Wörterbuch*, Sanskrit-Wörterbuch, Böhtlingk & Roth, 1855–1875) as part of the [Sanskrit Lexicon](https://github.com/sanskrit-lexicon) project. The primary focus is building clickable link targets from `<ls>` literary-source abbreviations to scanned PDF pages, along with link-splitting, XML markup normalisation, and digitisation quality improvements. The primary input is `pwg.xml`, maintained in the sibling [pwgxml](https://github.com/sanskrit-lexicon/pwgxml) repository; corrections are applied across related dictionaries (PW, MW, PWKVN, SCH).

---

### Directories

| Directory | Contents |
|---|---|
| `pwg_ls/` | Round 1 — extraction and analysis of `<ls>` (literary source) tags from pwg.xml |
| `pwg_ls1/` | Round 2 — authority/bibliography record refinement (begun Dec 2017) |
| `pwg_ls2/` | Round 3 — per-source corrections; subfolders named by abbreviation (`RV/`, `ak/`, `mbh1/`, …) |
| `pwgissues/` | One folder per GitHub issue (`issueNNN/` for analysis, `issueNNNfix/` for correction scripts) |
| `verbs01/` | Early verb and upasarga analysis against PWG headwords |
| `verbs01a/` | Verb identification correlated with Monier-Williams (MW) dictionary (begun Mar 2020) |
| `RussianWords/` | Russian etymologies in PWG |
| `pwgheader/` | Volume and header metadata |
| `misc/` | Accent display, encoding conversion, and other utilities |

---

### How It Works

Corrections to `pwg.xml` are never made directly. Instead, scripts produce **change files** that are applied by `updateByLine.py`:

```
1234 old original line text
1234 new replacement line text
```

Three operations are supported: `new` (replace), `ins` (insert after), and `del` (delete). All files must be UTF-8.

#### Issue workflow

Each GitHub issue gets a folder under `pwgissues/`:
- `issueNNN/` — analysis scripts, index files, and a `readme.txt` that serves as a running log of commands executed and results observed.
- `issueNNNfix/` — correction scripts applied to `pwg.xml` and sibling dictionaries (PW, MW, PWKVN, SCH, …). Newer issues may keep everything in `issueNNN/`.

#### Link-target workflow

For sources that need clickable page links:
1. Build a tab-separated index file mapping book sections (volume, chapter, verse) to PDF page numbers.
2. Run `make_js_index.py` to validate the index and produce `index.js`.
3. Run `lsfix2.py` to rewrite `<ls>` tags across all related dictionaries (PWG, PW, MW, etc.) with the link targets.

#### Literary source (`<ls>`) analysis pipeline

Run from `pwg_ls/pwg_dhaval/abbrvwork/`:

```sh
sh makeabbrv.sh
```

This runs: `abbrv.py` → AS→IAST transliteration → `php displayhtml.php` → `abbrvoutput/display.html` for human review.

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
| 2021 | `pwg_ls2` begun; Rig-Veda `<ls>` markup; VN corrections from Andhrabharati |
| 2022 | Per-source markup improvements: Spr. (II), AV, P., MBH, Ramayana, AmaraKosha |
| 2023 | Unknown and numeric `<ls>` cleanup |
| 2024 | Link target work: KATHAS, MANU, VN, and many more sources |
| 2025 | Link-splitting (#160) completed for 30+ sources: RAGH., MBH, M., KATHĀS., ŚĀK., TAITTIRĪYA texts, ŚAT. BR., MEGH., MĀLAV., and more; image quality improvements for vol. 6 (#161); additional link targets (#168, #169); automated index checking by Dhaval Patel |
| 2026 | Repository organisation: CLAUDE.md, issue labelling, severity labels, milestone and project triage; full audit of all 167 issues for label/milestone/project consistency |

---

### Projects & Milestones

Work is organised into four GitHub Projects (org-level kanban boards), each mirroring a milestone:

| Project | Milestone | Open | Closed | Scope |
|---|---|---|---|---|
| [**Dictionary to Book**](https://github.com/orgs/sanskrit-lexicon/projects/5) | [milestone](https://github.com/sanskrit-lexicon/PWG/milestone/1) | 23 | 57 | Making all literary source abbreviations click-through to scanned source pages — link targets and link splitting |
| [**Structured Data**](https://github.com/orgs/sanskrit-lexicon/projects/7) | [milestone](https://github.com/sanskrit-lexicon/PWG/milestone/3) | 16 | 19 | XML markup normalization, structured data improvements, and resolving interpretation questions |
| [**Digitization Quality**](https://github.com/orgs/sanskrit-lexicon/projects/6) | [milestone](https://github.com/sanskrit-lexicon/PWG/milestone/2) | 12 | 22 | Fixing errors from the original digitization: scan quality, encoding, text corrections, bugs |
| [**Major Enhancements**](https://github.com/orgs/sanskrit-lexicon/projects/8) | [milestone](https://github.com/sanskrit-lexicon/PWG/milestone/4) | 12 | 6 | Large new content additions: Cologne/Andhrabharati material, Weber's Nachlass, verb markup, bibliography |

---

### Issue Typology

Issues track two broad concerns: **enriching the XML** (adding links, fixing markup) and **improving the digitization** (scan quality, encoding, text errors).

#### Solved (closed issues)

| Type | Description | Examples |
|---|---|---|
| **Link targets** | Building clickable references from `<ls>` abbreviations to scanned PDF pages — the bulk of the work. Each issue researches one source, constructs an index, and installs links across all related dictionaries (54 issues, 60+ sources). | RAGH., MBH, ŚĀK., BHAGAVADGĪTĀ, MEGHADŪTA, AMARAKOSHA, HITOPADEŚA, GĪTAGOVINDA, VIKRAMORVAŚĪ, ŚATAPATHABRĀHMAṆA, TAITTIRĪYABRĀHMAṆA, HALĀYUDHA |
| **Link splitting** | Combined references like `SOURCE N,N` pointed to a single target; split into individual page links (3 issues, 30+ sources). Main work coordinated under [#160](https://github.com/sanskrit-lexicon/PWG/issues/160); KATHĀS. [#71](https://github.com/sanskrit-lexicon/PWG/issues/71) and ŚAT. BR. [#170](https://github.com/sanskrit-lexicon/PWG/issues/170) resolved separately. | MBH, RAGH., ŚĀK., Spr. (I & II), BHARTṚHARI, KATHĀS., TAITTIRĪYA texts, ŚAT. BR., MEGH., MĀLAV., RĀJAT. |
| **`<ls>` markup** | Normalizing the content of literary-source tags: removing numeric orphans, resolving unknowns, stripping gratuitous spaces, correcting irregular tag forms; missing references added for Kosha and grammatical sources (15 issues). | [#45](https://github.com/sanskrit-lexicon/PWG/issues/45), [#46](https://github.com/sanskrit-lexicon/PWG/issues/46), [#64](https://github.com/sanskrit-lexicon/PWG/issues/64), [#65](https://github.com/sanskrit-lexicon/PWG/issues/65), [#77](https://github.com/sanskrit-lexicon/PWG/issues/77), [#113](https://github.com/sanskrit-lexicon/PWG/issues/113), [#114](https://github.com/sanskrit-lexicon/PWG/issues/114), [#115](https://github.com/sanskrit-lexicon/PWG/issues/115), [#117](https://github.com/sanskrit-lexicon/PWG/issues/117), [#127](https://github.com/sanskrit-lexicon/PWG/issues/127) |
| **Text corrections** | Corrections to German definitions and minor typos in the dictionary text. | [#27](https://github.com/sanskrit-lexicon/PWG/issues/27), [#36](https://github.com/sanskrit-lexicon/PWG/issues/36) |
| **Content enhancement** | Content additions and display improvements: Russian etymologies, accent display, scansion symbols, bibliography work (8 issues). | Russian etymologies [#6](https://github.com/sanskrit-lexicon/PWG/issues/6), [#14](https://github.com/sanskrit-lexicon/PWG/issues/14), [#17](https://github.com/sanskrit-lexicon/PWG/issues/17); accents [#9](https://github.com/sanskrit-lexicon/PWG/issues/9); scansion symbols [#29](https://github.com/sanskrit-lexicon/PWG/issues/29); bibliography [#20](https://github.com/sanskrit-lexicon/PWG/issues/20) |
| **Encoding & text** | SLP1 encoding conversion, Greek text rendering, hyphen/dash normalization, accent coding, single-letter italics (9 issues). | [#5](https://github.com/sanskrit-lexicon/PWG/issues/5), [#11](https://github.com/sanskrit-lexicon/PWG/issues/11), [#13](https://github.com/sanskrit-lexicon/PWG/issues/13), [#19](https://github.com/sanskrit-lexicon/PWG/issues/19), [#34](https://github.com/sanskrit-lexicon/PWG/issues/34), [#43](https://github.com/sanskrit-lexicon/PWG/issues/43), [#55](https://github.com/sanskrit-lexicon/PWG/issues/55), [#56](https://github.com/sanskrit-lexicon/PWG/issues/56) |
| **Scan quality** | Replacing blurry or missing scan pages with clearer images (3 issues). | [#16](https://github.com/sanskrit-lexicon/PWG/issues/16), [#40](https://github.com/sanskrit-lexicon/PWG/issues/40), [#161](https://github.com/sanskrit-lexicon/PWG/issues/161) |
| **Bug fixes** | Broken download links, bad XML tags (`<UL/>`), unresolved `{?}` placeholders, page-number and link bugs (6 issues). | [#1](https://github.com/sanskrit-lexicon/PWG/issues/1), [#10](https://github.com/sanskrit-lexicon/PWG/issues/10), [#21](https://github.com/sanskrit-lexicon/PWG/issues/21), [#25](https://github.com/sanskrit-lexicon/PWG/issues/25), [#66](https://github.com/sanskrit-lexicon/PWG/issues/66), [#80](https://github.com/sanskrit-lexicon/PWG/issues/80) |
| **Questions resolved** | Terminology and interpretation questions that were researched and answered (5 issues). | [#2](https://github.com/sanskrit-lexicon/PWG/issues/2), [#103](https://github.com/sanskrit-lexicon/PWG/issues/103), [#108](https://github.com/sanskrit-lexicon/PWG/issues/108), [#126](https://github.com/sanskrit-lexicon/PWG/issues/126), [#165](https://github.com/sanskrit-lexicon/PWG/issues/165) |

#### Open (work ahead)

| Type | Description | Examples |
|---|---|---|
| **Link targets** | Several sources still need their index built and links installed (18 open issues). | AITAREYABRĀHMAṆA [#159](https://github.com/sanskrit-lexicon/PWG/issues/159), CAURAPAÑCĀŚIKĀ [#150](https://github.com/sanskrit-lexicon/PWG/issues/150), Prātiśākhya texts [#41](https://github.com/sanskrit-lexicon/PWG/issues/41), [#42](https://github.com/sanskrit-lexicon/PWG/issues/42), NĀRADA PAÑCARĀTRA [#137](https://github.com/sanskrit-lexicon/PWG/issues/137), VS. PRĀT. [#139](https://github.com/sanskrit-lexicon/PWG/issues/139), YĀSKA'S NIRUKTA [#167](https://github.com/sanskrit-lexicon/PWG/issues/167), MBH Bombay-Calcutta [#158](https://github.com/sanskrit-lexicon/PWG/issues/158), RV. Prātiśākhya [#173](https://github.com/sanskrit-lexicon/PWG/issues/173), Ramayana Bombay [#60](https://github.com/sanskrit-lexicon/PWG/issues/60) |
| **Link splitting** | Remaining combined `N,N` references not yet split (5 open issues). | M. (Manu) [#74](https://github.com/sanskrit-lexicon/PWG/issues/74), YĀJÑ. [#172](https://github.com/sanskrit-lexicon/PWG/issues/172), ṚV. [#133](https://github.com/sanskrit-lexicon/PWG/issues/133), RAGH. Calc. [#142](https://github.com/sanskrit-lexicon/PWG/issues/142), KĀTY. ŚR. 2-param [#145](https://github.com/sanskrit-lexicon/PWG/issues/145) |
| **Markup** | XML markup normalization and structural improvements: unresolved `<ls>` tags, `<lex>` formatting, display upgrades, and editorial questions about literary-source forms. | Abhidhānacintāmaṇi [#116](https://github.com/sanskrit-lexicon/PWG/issues/116), Sch. [#35](https://github.com/sanskrit-lexicon/PWG/issues/35), `<ls>?` cleanup [#47](https://github.com/sanskrit-lexicon/PWG/issues/47), `<lex>` formatting [#91](https://github.com/sanskrit-lexicon/PWG/issues/91), expanding abbreviations [#26](https://github.com/sanskrit-lexicon/PWG/issues/26), markup upgrade [#18](https://github.com/sanskrit-lexicon/PWG/issues/18), titular refs [#106](https://github.com/sanskrit-lexicon/PWG/issues/106), commentarial refs [#107](https://github.com/sanskrit-lexicon/PWG/issues/107) |
| **Text corrections** | Errors in the German definitions and Sanskrit text of the dictionary itself. | German words [#67](https://github.com/sanskrit-lexicon/PWG/issues/67), preverbs [#44](https://github.com/sanskrit-lexicon/PWG/issues/44), `Page6` spacing [#63](https://github.com/sanskrit-lexicon/PWG/issues/63), abbrev suggestions [#58](https://github.com/sanskrit-lexicon/PWG/issues/58), Ṛv. PRĀTIŚ. [#90](https://github.com/sanskrit-lexicon/PWG/issues/90), miscellaneous [#128](https://github.com/sanskrit-lexicon/PWG/issues/128), minor text [#171](https://github.com/sanskrit-lexicon/PWG/issues/171) |
| **Content enhancement** | Major additions that go beyond correction — new material or structural upgrades. | Cologne/Andhrabharati additions [#37](https://github.com/sanskrit-lexicon/PWG/issues/37), [#163](https://github.com/sanskrit-lexicon/PWG/issues/163), Weber's Nachlass [#61](https://github.com/sanskrit-lexicon/PWG/issues/61), bibliography cleaning [#22](https://github.com/sanskrit-lexicon/PWG/issues/22), verb markup [#7](https://github.com/sanskrit-lexicon/PWG/issues/7), [#31](https://github.com/sanskrit-lexicon/PWG/issues/31), [#32](https://github.com/sanskrit-lexicon/PWG/issues/32), upasarga access [#28](https://github.com/sanskrit-lexicon/PWG/issues/28), apply VN [#52](https://github.com/sanskrit-lexicon/PWG/issues/52) |
| **Encoding** | Transcoding edge cases. | Vowel-marker transcoding [#78](https://github.com/sanskrit-lexicon/PWG/issues/78) |
| **Scan quality** | Blurry or missing scan pages still needing replacement. | VN missing pages [#39](https://github.com/sanskrit-lexicon/PWG/issues/39), [#76](https://github.com/sanskrit-lexicon/PWG/issues/76) |
| **Bug fixes** | Known errors in link behaviour or XML structure. | Hariv. link bug [#79](https://github.com/sanskrit-lexicon/PWG/issues/79) |
| **Questions / interpretation** | Open scholarly questions about how to handle specific reference forms. | Commentarial literature [#107](https://github.com/sanskrit-lexicon/PWG/issues/107), [#166](https://github.com/sanskrit-lexicon/PWG/issues/166), titular refs [#106](https://github.com/sanskrit-lexicon/PWG/issues/106), ŚKDR. linking [#118](https://github.com/sanskrit-lexicon/PWG/issues/118), UTTARAR. [#131](https://github.com/sanskrit-lexicon/PWG/issues/131), [#132](https://github.com/sanskrit-lexicon/PWG/issues/132) |

---

### Contributors

- **Jim Funderburk** ([@funderburkjim](https://github.com/funderburkjim)) — project lead
- **Mārcis Gasūns** ([@gasyoun](https://github.com/gasyoun)) — Russian etymologies, accents, tooling, issue and project organisation
- **Dhaval Patel** ([@drdhaval2785](https://github.com/drdhaval2785)) — automation of link-splitting and index checking
- **Andhrabharati** — VN text corrections and index data
- **Thomas Malten** — original bibliography digitization (`pwgbib_orig.txt`)
