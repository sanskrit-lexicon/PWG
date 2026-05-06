# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **PWG Sanskrit Dictionary Data Processing** repository — part of the [sanskrit-lexicon](https://github.com/sanskrit-lexicon) project. It contains scripts and data for digitizing, correcting, and enriching the PWG (Petersburger Wörterbuch) Sanskrit dictionary.

The primary input is `pwg.xml` (located in a sibling `../pwgxml/` directory, not tracked in this repo). All processing reads from or produces corrections to that XML file.

## Getting the Input Data

Before running most scripts, obtain `pwg.xml` by running this script from the parent `GitHub/` directory:

```sh
curl -o pwgxml.zip http://www.sanskrit-lexicon.uni-koeln.de/scans/PWGScan/2013/downloads/pwgxml.zip
unzip pwgxml.zip
rm -r pwgxml && mv xml pwgxml && rm pwgxml.zip
```

## Key Commands

**Literary source abbreviation pipeline** (run from `pwg_ls/pwg_dhaval/abbrvwork/`):
```sh
sh makeabbrv.sh
```
This runs: `python abbrv.py $PWG` → transliteration → `php displayhtml.php` → `abbrvoutput/display.html`

**Apply line-level corrections to a dictionary file** (pattern used throughout `pwg_ls2/*/`):
```sh
python updateByLine.py <input_file> <changein_file> <output_file>
```
The `changein_file` is a UTF-8 text with paired lines: `NNN old <original>` / `NNN new <replacement>`. Lines beginning with `;` are comments.

**Generate a JavaScript index for a literary source** (used in `pwgissues/*/`):
```sh
python make_js_index.py <volume> <index_edit.txt> <output.js>
```

## Architecture

The work is organized in iterative rounds:

| Directory | Purpose |
|---|---|
| `pwg_ls/` | Round 1: Extract and analyze `<ls>` (literary source) tags from pwg.xml |
| `pwg_ls1/` | Round 2: Authority/bibliography record refinement (begun Dec 2017) |
| `pwg_ls2/` | Round 3: Per-source corrections; subfolders named by abbreviation (e.g., `RV/`, `ak/`, `mbh1/`) |
| `pwgissues/` | One folder per GitHub issue (`issueNNN/` for analysis, `issueNNNfix/` for the correction scripts) |
| `verbs01a/` | Verb identification and correlation with MW dictionary (begun Mar 2020) |
| `RussianWords/` | Russian etymologies extraction |
| `pwgheader/` | Volume/header metadata |

### Literary Source Pipeline (`pwg_ls/pwg_dhaval/abbrvwork/`)

Sequential scripts: `abbrv0.py` → `abbrv1.py` → `abbrv2.py` → `abbrv3.py` → `abbrv4.py`

Each step refines the extracted `<ls>` tags: raw extraction → separate pure-number refs → unique sorted list → sort by occurrence count → match with bibliography database (`pwgbib14_roman.txt`). Outputs land in `abbrvoutput/`.

Transliteration between **Anglicized Sanskrit (AS)** and **IAST/Roman** is done via `transcoder/as_roman.py` (and the reverse `roman_as.py`), driven by `as_roman.xml` mapping files.

### Issue-Driven Corrections (`pwgissues/`)

Each GitHub issue gets two folders:
- `issueNNN/` — analysis scripts, index building, `readme.txt` with the full workflow log
- `issueNNNfix/` — correction scripts applied to pwg.xml and sibling dictionaries (MW, PW, etc.)

`readme.txt` files in issue folders serve as living workflow logs — commands run, outputs observed, decisions made.

### `updateByLine.py` Pattern

Used across `pwg_ls2/*/` and `pwgissues/*/` to apply corrections. The change file format:
```
1234 old original line text here
1234 new replacement line text here
```
Supports `new` (replace), `ins` (insert after), and `del` (delete). All files must be UTF-8.

## Dependencies

- **Python 3** (scripts use `from __future__ import print_function` for legacy compatibility)
- **lxml** — XML parsing (`pip install lxml`)
- **PHP** — HTML display generation (`displayhtml.php`)
- **pwg.xml** — in sibling directory `../pwgxml/pwg.xml`

## GitHub Issue Conventions

### Milestones and projects

Every issue belongs to exactly one milestone, which mirrors an org-level kanban project:

| Milestone | Project | Scope |
|---|---|---|
| Dictionary to Book (1) | Project 5 | Link targets and link splitting |
| Digitization Quality (2) | Project 6 | Scan quality, encoding, bug fixes, text corrections |
| Structured Data (3) | Project 7 | Markup normalisation, structured data, editorial questions |
| Major Enhancements (4) | Project 8 | Large new content: verb markup, bibliography, Cologne material |

Issues #89 and #99 are administrative noise — skip them in any triage or audit.

### Type labels

Every issue has exactly one type label:

| Label | When to use |
|---|---|
| `link-target` | Building a click-through from a `<ls>` abbreviation to scanned PDF pages |
| `link-splitting` | Splitting combined `SOURCE N,N` refs into individual per-page links |
| `markup` | Normalising XML tag content or structure (`<ls>`, `<lex>`, etc.) |
| `text-correction` | Corrections to German definitions or Sanskrit headwords |
| `content-enhancement` | New material, display upgrades, or structural additions beyond correction |
| `encoding` | SLP1/AS/IAST transcoding, character rendering, hyphen/dash normalisation |
| `scan-quality` | Replacing blurry, skewed, or missing scan pages |
| `bug` | Broken links, XML structure errors, or broken download files |
| `question` | Scholarly or editorial questions requiring research before any code change |

### Severity labels

Every issue also has exactly one severity label:

| Label | When to use |
|---|---|
| `minor` | Targeted, self-contained fix — a handful of lines or a single file |
| `medium` | Standard unit of work — one link-target index, a batch of markup corrections |
| `hard` | Large effort spanning many sources, files, or dictionaries |

## Conventions

- Scripts are run from the directory containing them (relative paths assumed).
- `readme.txt` files in issue folders are workflow logs, not documentation — they record what was actually run.
- Intermediate outputs (`.txt` files in `abbrvoutput/`) are regenerated by scripts and not tracked.
- Corrections to `pwg.xml` are never made directly — they are expressed as change files applied by scripts.
