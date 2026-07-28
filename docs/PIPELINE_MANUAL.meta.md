# PIPELINE_MANUAL.md — metadoc

_Created: 28-07-2026 · Last updated: 28-07-2026_

Companion record for
[docs/PIPELINE_MANUAL.md](https://github.com/sanskrit-lexicon/PWG/blob/main/docs/PIPELINE_MANUAL.md)
— purpose, provenance, improvement backlog and revision history of the manual
itself (not of the pipelines it documents).

## Purpose

Give a new operator/contributor a runnable understanding of PWG's pipeline
family — the universal `updateByLine.py` correction loop, the link-target and
link-splitting workflows, the 2026 Andhrabharati v1e reconciliation stream,
the frozen `pwg_ls*` abbreviation/bibliography archaeology, the live prefaces
OCR and pagecolumn index — without reading ~900 Python files first, and
without stepping on the org's csl-orig batched-PR delivery rule.

## Audience

- **Operators** opening a new `pwgissues/issueNNN/` correction or link-target
  folder (cheat-sheet, walkthroughs 1–2, symptom table);
- **Maintainers** of the live surfaces — the AB/v1e residue issues, prefaces,
  pagecolumn (walkthroughs 3, 5, 6, appendix);
- **Historians/re-verifiers** of the frozen strands — `pwg_ls*`, verbs,
  convertwork, RussianWords, pwgheader (walkthroughs 4, 7, lifecycle table).

## Provenance

- Authored 28-07-2026 by Fable 5 (`claude-fable-5`) executing handoff
  [H1785-Fable_PWG_correction-linktarget-pipeline-manual_28.07.26.md](https://github.com/gasyoun/Uprava/blob/main/handoffs/H1785-Fable_PWG_correction-linktarget-pipeline-manual_28.07.26.md)
  (docs-debt batch H1782–H1786).
- Modelled on the PWK sibling manual
  ([PWK docs/PIPELINE_MANUAL.md](https://github.com/sanskrit-lexicon/PWK/blob/main/docs/PIPELINE_MANUAL.md),
  H530) and the
  [RussianRamayana Litpam-Indexator MANUAL.md](https://github.com/gasyoun/RussianRamayana/blob/main/Litpam-Indexator/docs/indesign-pipeline/MANUAL.md)
  gold standard.
- Source material: the repo's own per-folder `readme` logs (pwgissues/
  issue98fix, issue160, issue168, issue169, issue173, issue174–193;
  pwg_ls/pwg_dhaval abbrvwork + abbrvwork_v0; pwg_ls/pwgbib/digitization;
  pwg_ls1/pwgauth; all 15 pwg_ls2 folders; misc/{greek, convertwork,
  accentdisplay}; verbs01, verbs01a; RussianWords; pwgheader; prefaces
  METHODS/README; pagecolumn README), surveyed by three parallel Explore
  agents (Fable 5 `claude-fable-5` session, 28-07-2026); command sequences
  quoted verbatim from those logs, paths verified on disk that day.
- Point-in-time facts checked 28-07-2026: 111 pwgissues folders (#48–#193);
  17 `updateByLine.py` copies in 3 md5-distinct versions; v1e installed
  (issue191 audit, 14→32 tags); `changelog.md` double-`[Unreleased]` defect;
  `index.html` not linking `prefaces/`; issue184 readme-less.

## Ranked improvement backlog

| # | Item | Status |
|---|---|---|
| 1 | Merge the two `[Unreleased]` sections in [changelog.md](https://github.com/sanskrit-lexicon/PWG/blob/main/changelog.md) (manual appendix §5) | **done in the same PR as this manual** |
| 2 | Give [issue184](https://github.com/sanskrit-lexicon/PWG/tree/main/pwgissues/issue184) a readme (appendix §4) — its scripts feed issue190 | open |
| 3 | Expand [DATA_DICTIONARY.md](https://github.com/sanskrit-lexicon/PWG/blob/main/DATA_DICTIONARY.md) to the post-v1e 32-tag vocabulary (appendix §6) | open |
| 4 | Link `prefaces/` from the Pages landing `index.html` (appendix §7) | open |
| 5 | Standardise vendored `updateByLine.py` on the `pwg_ls2/01/` version when folders are touched; rename the lowercase-`l` `pratishakya/updateByline.py` | open |
| 6 | Live-verify the two safely re-runnable pipelines (`pagecolumn/`, `prefaces/build_combined.py`) and record fresh counts (the "measured, not copied" standard) | open |
| 7 | Regenerate `misc/changes_visarga_anusvara_accents.txt` against a pinned snapshot, or mark it superseded in place | open |
| 8 | Add a CI gate for `prefaces/` (consolidated-edition freshness vs per-page files) | open |

## Known limitations

- **Commands are transcription-verified, not re-executed.** PWG's pipelines
  mutate the sibling `csl-orig` working tree and most are one-time
  historical, so the manual quotes the in-repo readmes verbatim and verifies
  paths/files exist instead of re-running. Backlog #6 upgrades this for the
  two safe pipelines.
- Coverage of `pwgissues/` is by pattern (issue98fix, issue169, issue190, the
  AB stream), not per-folder; the folder index remains
  [pwgissues/readme.txt](https://github.com/sanskrit-lexicon/PWG/blob/main/pwgissues/readme.txt).
- `prefaces/` operational detail is deferred to its own
  [METHODS.md](https://github.com/sanskrit-lexicon/PWG/blob/main/prefaces/METHODS.md)
  and the csl-guides preface-ocr-pipeline page.
- The XAMPP-path remapping guidance assumes the flat `GitHub/` checkout
  convention; other layouts need their own remap.
- Point-in-time counts (111 folders, 17 copies, tag counts) date to
  28-07-2026 and drift with the tree.

## Intended use / known misuse

- **Intended use:** onboarding for a new operator opening a
  `pwgissues/issueNNN/` folder; the reference the org's skills
  ([/cologne-correction-queue](https://github.com/gasyoun/claude-config/blob/main/commands/cologne-correction-queue.md),
  [/cologne-batch-pr](https://github.com/gasyoun/claude-config/blob/main/commands/cologne-batch-pr.md),
  [/cologne-link-target](https://github.com/gasyoun/claude-config/blob/main/commands/cologne-link-target.md))
  point to for PWG-specific command sequences.
- **Known misuse:**
  - Treating quoted command sequences as live-tested — they are
    transcription-verified only; blind replay can mutate the sibling
    `csl-orig` working copy (several historical readmes have **no restore
    step**).
  - Using this manual to justify a **direct push to csl-orig** — the Delivery
    section is explicit: queue via `/cologne-correction-queue`, ship via the
    monthly `/cologne-batch-pr`.
  - Re-running the frozen strands (`pwg_ls*` Python 2, `misc/convertwork`
    Python 2.6, `pwg_ls2` commit-pinned change files) expecting idempotency —
    they were one-shot passes against since-moved targets.
  - Applying `misc/changes_visarga_anusvara_accents.txt` as-is (no recorded
    base commit; stale absolute line numbers).
  - Editing `pwg_ls/pwg_ru_coverage/` by hand — it is auto-generated in the
    SanskritLexicography repo on a schedule.

## Maintenance & sunset plan

- **Trigger for re-verification:** a new pwgissues generation shape (a
  successor to the issue190 staged-pipeline pattern), a change to
  `updateByLine.py`/`lsfix2.py` conventions, closure of backlog items 1–4, or
  the deepseek-pilot branch resuming — re-survey the affected walkthrough.
- **Owner:** whoever next touches a PWG pipeline in an operator/maintainer
  role picks up open backlog items opportunistically; no dedicated maintainer
  (repo pattern).
- **Staleness signal:** if [pwgissues/readme.txt](https://github.com/sanskrit-lexicon/PWG/blob/main/pwgissues/readme.txt)
  or any workspace readme diverges from what this manual quotes verbatim, the
  manual is stale for that section — re-survey with the same parallel
  Explore-agent pattern used to author it.
- **Sunset condition:** none planned; supersede only if PWG's tooling is
  consolidated org-wide (e.g. a shared
  [sanskrit-util](https://github.com/sanskrit-lexicon/sanskrit-util) engine
  replaces the vendored copies).

## Deprecation status

`active`

## Related documents

- [readme.md](https://github.com/sanskrit-lexicon/PWG/blob/main/readme.md) — repo overview, timeline, milestones, labels
- [CLAUDE.md](https://github.com/sanskrit-lexicon/PWG/blob/main/CLAUDE.md) — code contract (directory map, key commands, input-data fetch)
- [RUNBOOK.md](https://github.com/sanskrit-lexicon/PWG/blob/main/RUNBOOK.md) — issue-taxonomy/docs-cleanup autonomy script (not a pipeline manual)
- [DATA_DICTIONARY.md](https://github.com/sanskrit-lexicon/PWG/blob/main/DATA_DICTIONARY.md) — tag legend (stub; backlog #3)
- [prefaces/METHODS.md](https://github.com/sanskrit-lexicon/PWG/blob/main/prefaces/METHODS.md) — front-matter OCR methods + citation contract
- [pagecolumn/README.md](https://github.com/sanskrit-lexicon/PWG/blob/main/pagecolumn/README.md) — co-location index tool doc
- [csl-corrections correction workflow](https://github.com/sanskrit-lexicon/csl-corrections/blob/main/docs/correction-workflow.md) — the canonical 8-stage csl-orig procedure this manual defers to
- [PWK docs/PIPELINE_MANUAL.md](https://github.com/sanskrit-lexicon/PWK/blob/main/docs/PIPELINE_MANUAL.md) — the sibling manual this one is modelled on

## Revision history

| Date | Change | By |
|---|---|---|
| 28-07-2026 | Initial manual + this metadoc authored (H1785); 3-agent survey of all workspaces; commands quoted verbatim from in-repo readmes, paths verified on disk | Fable 5 (`claude-fable-5`) |

_Dr. Mārcis Gasūns_
