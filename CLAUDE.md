# CLAUDE.md

_Created: 06-05-2026 · Last updated: 16-08-2026_

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

Apply a change file (never edit `pwg.xml` in place):

```sh
python updateByLine.py <input_file> <changefile> <output_file>
```

```
1234 old exact original line text
1234 new exact replacement line text
```

`ins` / `del` / `;` comments. UTF-8, no BOM.

Literary-source abbreviation pipeline (from
`pwg_ls/pwg_dhaval/abbrvwork/`): `sh makeabbrv.sh`.

Link-target / scan work: a `<ls>` abbreviation becomes a click-through to
the scanned PDF page. Per-source folders live under `pwg_ls2/`; each GitHub
issue gets `pwgissues/issueNNN/` (analysis) + `issueNNNfix/` (scripts).
`readme.txt` in those folders is a run log, not a spec.

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
