
## PWG Sanskrit Dictionary Processing

Scripts and data for digitizing, correcting, and enriching the **PWG** (*Petersburger Wörterbuch*, Sanskrit-Wörterbuch, Böhtlingk & Roth, 1855–1875) as part of the [Sanskrit Lexicon](https://github.com/sanskrit-lexicon) project. The primary input is `pwg.xml`, maintained in the sibling [pwgxml](https://github.com/sanskrit-lexicon/pwgxml) repository.

---

### Directories

| Directory | Contents |
|---|---|
| `pwg_ls/` | Round 1 — extraction and analysis of `<ls>` (literary source) tags from pwg.xml |
| `pwg_ls1/` | Round 2 — authority/bibliography record refinement (begun Dec 2017) |
| `pwg_ls2/` | Round 3 — per-source corrections; subfolders named by abbreviation (`RV/`, `ak/`, `mbh1/`, …) |
| `pwgissues/` | One folder per GitHub issue (`issueNNN/` for analysis, `issueNNNfix/` for correction scripts) |
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

The literary source (`<ls>`) pipeline in `pwg_ls/pwg_dhaval/abbrvwork/` runs as:

```sh
sh makeabbrv.sh
```

This extracts all `<ls>` tags from pwg.xml, converts Anglicized Sanskrit to IAST, and generates `abbrvoutput/display.html` for human review.

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
| 2025 | Large-scale link-splitting corrections (#160); image quality improvements (#161); automated index checking by Dhaval Patel |

---

### Issue Typology

Issues track two broad concerns: **enriching the XML** (adding links, fixing markup) and **improving the digitization** (scan quality, encoding, text errors).

#### Solved (closed issues)

| Type | Description | Examples |
|---|---|---|
| **Link targets** | Building clickable references from `<ls>` abbreviations to scanned PDF pages — the bulk of the work. Each issue researches one source, constructs an index, and installs links across all related dictionaries. | RAGH., MBH, ŚĀK., BHAGAVADGĪTĀ, MEGHADŪTA, AMARAKOSHA, HITOPADEŚA, GĪTAGOVINDA, VIKRAMORVAŚĪ (60+ sources) |
| **Link splitting** | Combined references like `SOURCE N,N` pointed to a single target; these were split into individual page links. Coordinated under [#160](https://github.com/sanskrit-lexicon/PWG/issues/160), covering 30+ sources. | MBH, M. (Manu), RAGH., ŚĀK., Spr. (I & II), BHARTṚHARI, KATHĀS., TAITTIRĪYA texts |
| **`<ls>` markup** | Normalizing the content of literary-source tags: removing numeric orphans, resolving unknowns, stripping gratuitous spaces, correcting irregular tag forms. | [#64](https://github.com/sanskrit-lexicon/PWG/issues/64), [#65](https://github.com/sanskrit-lexicon/PWG/issues/65), [#77](https://github.com/sanskrit-lexicon/PWG/issues/77), [#127](https://github.com/sanskrit-lexicon/PWG/issues/127) |
| **Encoding & text** | SLP1 encoding conversion, Greek text rendering, hyphen/dash normalization, scansion symbols, single-letter italics. | [#11](https://github.com/sanskrit-lexicon/PWG/issues/11), [#34](https://github.com/sanskrit-lexicon/PWG/issues/34), [#55](https://github.com/sanskrit-lexicon/PWG/issues/55), [#43](https://github.com/sanskrit-lexicon/PWG/issues/43) |
| **Scan quality** | Replacing blurry or missing scan pages with clearer images. | [#40](https://github.com/sanskrit-lexicon/PWG/issues/40), [#161](https://github.com/sanskrit-lexicon/PWG/issues/161) |
| **Russian etymologies** | Identifying and tagging Russian words embedded in the dictionary. | [#6](https://github.com/sanskrit-lexicon/PWG/issues/6), [#14](https://github.com/sanskrit-lexicon/PWG/issues/14) |
| **Bug fixes** | Broken download links, bad XML tags (`<UL/>`), unresolved `{?}` placeholders, Hariv. link bugs. | [#1](https://github.com/sanskrit-lexicon/PWG/issues/1), [#21](https://github.com/sanskrit-lexicon/PWG/issues/21), [#66](https://github.com/sanskrit-lexicon/PWG/issues/66), [#80](https://github.com/sanskrit-lexicon/PWG/issues/80) |

#### Open (work ahead)

| Type | Description | Examples |
|---|---|---|
| **Link targets** | Several sources still need their index built and links installed. | AITAREYABRĀHMAṆA [#159](https://github.com/sanskrit-lexicon/PWG/issues/159), CAURAPAÑCĀŚIKĀ [#150](https://github.com/sanskrit-lexicon/PWG/issues/150), Prātiśākhya texts [#41](https://github.com/sanskrit-lexicon/PWG/issues/41), [#42](https://github.com/sanskrit-lexicon/PWG/issues/42), Ramayana Bombay [#60](https://github.com/sanskrit-lexicon/PWG/issues/60), NĀRADA PAÑCARĀTRA [#137](https://github.com/sanskrit-lexicon/PWG/issues/137) |
| **Link splitting** | Remaining combined `N,N` references not yet split. | YĀJÑ. [#172](https://github.com/sanskrit-lexicon/PWG/issues/172), ṚV. [#133](https://github.com/sanskrit-lexicon/PWG/issues/133), RAGH. Calc. [#142](https://github.com/sanskrit-lexicon/PWG/issues/142), KĀTY. ŚR. 2-param [#145](https://github.com/sanskrit-lexicon/PWG/issues/145) |
| **Missing markup** | Sources where `<ls>` tags are present but resolution is incomplete or absent. | Abhidhānacintāmaṇi [#116](https://github.com/sanskrit-lexicon/PWG/issues/116), Sch. [#35](https://github.com/sanskrit-lexicon/PWG/issues/35), VN missing pages [#39](https://github.com/sanskrit-lexicon/PWG/issues/39), [#76](https://github.com/sanskrit-lexicon/PWG/issues/76) |
| **Text corrections** | Errors in the German definitions and Sanskrit text of the dictionary itself. | German words [#67](https://github.com/sanskrit-lexicon/PWG/issues/67), preverbs [#44](https://github.com/sanskrit-lexicon/PWG/issues/44), minor text [#171](https://github.com/sanskrit-lexicon/PWG/issues/171), `Page6` spacing [#63](https://github.com/sanskrit-lexicon/PWG/issues/63) |
| **Content enhancement** | Major additions that go beyond correction — new material or structural upgrades. | Cologne/Andhrabharati additions [#37](https://github.com/sanskrit-lexicon/PWG/issues/37), [#163](https://github.com/sanskrit-lexicon/PWG/issues/163), Weber's Nachlass [#61](https://github.com/sanskrit-lexicon/PWG/issues/61), bibliography cleaning [#22](https://github.com/sanskrit-lexicon/PWG/issues/22), verb markup [#7](https://github.com/sanskrit-lexicon/PWG/issues/7), upasarga access [#28](https://github.com/sanskrit-lexicon/PWG/issues/28) |
| **Encoding/structural** | Transcoding edge cases, XML tag normalization, markup improvement. | `<ls>?` cleanup [#47](https://github.com/sanskrit-lexicon/PWG/issues/47), vowel-marker transcoding [#78](https://github.com/sanskrit-lexicon/PWG/issues/78), `<lex>` formatting [#91](https://github.com/sanskrit-lexicon/PWG/issues/91), markup upgrade [#18](https://github.com/sanskrit-lexicon/PWG/issues/18) |
| **Questions / interpretation** | Open scholarly questions about how to handle specific reference forms. | Commentarial literature [#107](https://github.com/sanskrit-lexicon/PWG/issues/107), [#166](https://github.com/sanskrit-lexicon/PWG/issues/166), titular refs [#106](https://github.com/sanskrit-lexicon/PWG/issues/106), ŚKDR. linking [#118](https://github.com/sanskrit-lexicon/PWG/issues/118) |

---

### Contributors

- **Jim Funderburk** ([@funderburkjim](https://github.com/funderburkjim)) — project lead
- **Mārcis Gasūns** ([@marcis-gasuns](https://github.com/marcis-gasuns)) — Russian etymologies, accents, tooling
- **Dhaval Patel** ([@drdhaval2785](https://github.com/drdhaval2785)) — automation of link-splitting and index checking
- **Andhrabharati** — VN text corrections and index data
- **Thomas Malten** — original bibliography digitization (`pwgbib_orig.txt`)
