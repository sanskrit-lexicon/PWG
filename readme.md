
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

### Contributors

- **Jim Funderburk** ([@funderburkjim](https://github.com/funderburkjim)) — project lead
- **Mārcis Gasūns** ([@marcis-gasuns](https://github.com/marcis-gasuns)) — Russian etymologies, accents, tooling
- **Dhaval Patel** ([@drdhaval2785](https://github.com/drdhaval2785)) — automation of link-splitting and index checking
- **Andhrabharati** — VN text corrections and index data
- **Thomas Malten** — original bibliography digitization (`pwgbib_orig.txt`)
