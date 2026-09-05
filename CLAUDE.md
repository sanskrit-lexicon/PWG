# CLAUDE.md

_Created: 06-05-2026 · Last updated: 05-09-2026_

**PWG** is the correction and enrichment layer for the large Petersburger
Wörterbuch (Böhtlingk & Roth, 1855–1875). Primary input is
[`../pwgxml/pwg.xml`](https://github.com/sanskrit-lexicon/pwgxml) (sibling
checkout, not tracked here). This repo does **not** hold the canonical
digitised source — that is
[csl-orig `v02/pwg/`](https://github.com/sanskrit-lexicon/csl-orig/tree/main/v02/pwg).

Landing page: [sanskrit-lexicon.github.io/PWG](https://sanskrit-lexicon.github.io/PWG/).
Repo map, `<ls>` program, and scan-link conventions:
[README.md](https://github.com/sanskrit-lexicon/PWG/blob/main/README.md).

## What to run

Obtain `pwg.xml` (from the parent of this checkout) if missing:

```sh
curl -o pwgxml.zip http://www.sanskrit-lexicon.uni-koeln.de/scans/PWGScan/2013/downloads/pwgxml.zip
unzip pwgxml.zip
rm -r pwgxml && mv xml pwgxml && rm pwgxml.zip
```

Apply a change file (never edit `pwg.xml` in place). There is **no**
repo-root `updateByLine.py` — each workdir carries a copy. Run from that
directory. Examples:
[pwg_ls2/ak/updateByLine.py](https://github.com/sanskrit-lexicon/PWG/blob/main/pwg_ls2/ak/updateByLine.py),
[misc/greek/updateByLine.py](https://github.com/sanskrit-lexicon/PWG/blob/main/misc/greek/updateByLine.py).

```sh
python updateByLine.py <input_file> <changefile> <output_file>
```

```
1234 old exact original line text
1234 new exact replacement line text
```

`ins` / `del` / `;` comments. UTF-8, no BOM.

Literary-source abbreviation pipeline — run from
[pwg_ls/pwg_dhaval/abbrvwork/](https://github.com/sanskrit-lexicon/PWG/tree/main/pwg_ls/pwg_dhaval/abbrvwork):
`sh makeabbrv.sh`. Sequential scripts in that folder:
[abbrv0.py](https://github.com/sanskrit-lexicon/PWG/blob/main/pwg_ls/pwg_dhaval/abbrvwork/abbrv0.py)
→ [abbrv1.py](https://github.com/sanskrit-lexicon/PWG/blob/main/pwg_ls/pwg_dhaval/abbrvwork/abbrv1.py)
→ [abbrv2.py](https://github.com/sanskrit-lexicon/PWG/blob/main/pwg_ls/pwg_dhaval/abbrvwork/abbrv2.py)
→ [abbrv3.py](https://github.com/sanskrit-lexicon/PWG/blob/main/pwg_ls/pwg_dhaval/abbrvwork/abbrv3.py)
→ [abbrv4.py](https://github.com/sanskrit-lexicon/PWG/blob/main/pwg_ls/pwg_dhaval/abbrvwork/abbrv4.py).
Bibliography match file:
[pwg_ls/pwgbib/digitization/pwgbib14_roman.txt](https://github.com/sanskrit-lexicon/PWG/blob/main/pwg_ls/pwgbib/digitization/pwgbib14_roman.txt).

`makeabbrv.sh` still calls sibling `transcoder/as_roman.py` and
`php displayhtml.php`. Those two files are **not** in current
`abbrvwork/`. Live AS↔Roman converters:
[as_roman.py](https://github.com/sanskrit-lexicon/PWG/blob/main/pwg_ls/pwgbib/digitization/as_roman.py)
and
[roman_as.py](https://github.com/sanskrit-lexicon/PWG/blob/main/pwg_ls/pwgbib/digitization/roman_as.py),
driven by
[as_roman.xml](https://github.com/sanskrit-lexicon/PWG/blob/main/pwg_ls/pwgbib/digitization/as_roman.xml)
/
[roman_as.xml](https://github.com/sanskrit-lexicon/PWG/blob/main/pwg_ls/pwgbib/digitization/roman_as.xml).
A nested `transcoder/` copy exists only under
[abbrvwork_v0/transcoder/](https://github.com/sanskrit-lexicon/PWG/tree/main/pwg_ls/pwg_dhaval/abbrvwork_v0/transcoder).
`displayhtml.php` is not in this repository. Current
[abbrv3.py](https://github.com/sanskrit-lexicon/PWG/blob/main/pwg_ls/pwg_dhaval/abbrvwork/abbrv3.py)
imports `transcoder` from `../../pwgbib/digitization` and uses local
[as_roman1.xml](https://github.com/sanskrit-lexicon/PWG/blob/main/pwg_ls/pwg_dhaval/abbrvwork/as_roman1.xml).

JavaScript literary-source indexes: copies of `make_js_index.py` live under
[pwgissues/issueNNN/](https://github.com/sanskrit-lexicon/PWG/tree/main/pwgissues)
(not at repo root). Run from the issue folder.

Link-target / scan work: a `<ls>` abbreviation becomes a click-through to
the scanned PDF page. Per-source folders live under
[pwg_ls2/](https://github.com/sanskrit-lexicon/PWG/tree/main/pwg_ls2);
each GitHub issue gets `pwgissues/issueNNN/` (analysis) + `issueNNNfix/`
(scripts). `readme.txt` in those folders is a run log, not a spec.

Full correction sequence (snapshot → apply → regenerate → validate):
[csl-corrections/docs/correction-workflow.md](https://github.com/sanskrit-lexicon/csl-corrections/blob/main/docs/correction-workflow.md).

## Do not

- Edit `../pwgxml/pwg.xml` directly.
- Commit or push [csl-orig](https://github.com/sanskrit-lexicon/csl-orig).
  Queue via
  [`/cologne-correction-queue`](https://github.com/gasyoun/claude-config/blob/main/commands/cologne-correction-queue.md).
- Recopy the org issue-label table into this file. Issues #89 and #99 are
  administrative noise — skip them in triage.

## Primer

[SANSKRIT_CONTEXT_PRIMER.md](https://github.com/gasyoun/github-spine/blob/main/SANSKRIT_CONTEXT_PRIMER.md).

Issues use the Cologne taxonomy — see
[`/cologne-issue-runbook`](https://github.com/gasyoun/claude-config/blob/main/commands/cologne-issue-runbook.md).
PWG uses org projects **1–4** (MWS is the exception with 5–8).

_Dr. Mārcis Gasūns_
