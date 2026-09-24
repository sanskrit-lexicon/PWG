# H5466 — Full-set PWG ls taxonomy classifier (person+subtype, kośa, Hdschr, German series)

_Created: 24-09-2026 · Last updated: 24-09-2026_

_Field contract: [deep manual](https://github.com/gasyoun/Uprava/blob/main/docs/HANDOFF_LIFECYCLE_MACHINERY_DEEP_MANUAL.md)._

**Intended executor:** Fable

**Effort:** hard  _(trivial <15m · medium 15m–2h · hard 2h+)_

**Launch box:** any

**Gate:** none  _(none|human:|handoff:|external:|deploy:|until: — H3413)_

## Mission

## Mission
Build the MG-ruled full-set taxonomy classifier for PWG <ls> abbreviations in csl-observatory scripts/ beside pwg_ls_counts.py. Classes: person (flat + nullable subtype column: sanskrit-author/western/royal-mythic), book-work, journal-periodical, kosa/dictionary, manuscript-Hdschr, German-academy-series, commentary-of-work, edition-qualifier, unknown. Method (MG ruling): rules + MW name-lexicon cross-check + human-residue review sheet. Run AFTER the [Cologne Addition] entries land (repair first, then classify — MG).

## Inputs
- data/pwg_scan_index_tracker/andhrabharati_ls_diff/ (24-09 diff: 2680 values, 2006 exact-matched)
- CDSL pwgbib_input.txt tooltips as evidence channel
- PWG-ls.txt (Andhrabharati update) sha256 f44ae1bbccca1ceb508e9da0c1c389dcb93910fb570d0a4d962819cf756b5fd0
- MW name/person glosses via kosha (N. of authors/persons)

## Output
scripts/pwg_ls_taxonomy.py + classified TSV + --check gate + human-residue review sheet for MG adjudication.

**Goal / stop condition:** _<deterministic exit criterion + turn cap, paste-ready /goal — Uprava/GOAL_LOOP_CANDIDATES.md>_

## Acceptance (lock before work)

- **Done looks like:** _<concrete artifact, not a verb>_
- **Prove with:** _<command / PR / test>_
- **On our data:** _<fixture / baseline>_
- **Fail =:** _<named stop>_

## Evidence required

_Missing evidence is INCONCLUSIVE, never PASS (docs/PLAYBOOK_EVIDENCE_OF_DONE_2026.md)._

- [ ] _<artifact 1>_
- [ ] _<artifact 2>_
- [ ] _<own-data canary>_

## Delivery (five fields)

- **Changed:** _<what changed>_
- **Unchanged:** _<what stayed>_
- **Checks:** _<command + PASS/FAIL>_
- **Risks:** _<risks>_
- **Inspect:** _<verifier opens first>_

> **Moved from** `Uprava/handoffs/` 24-09-2026 per MG ruling: PWG-related handoffs live in the PWG repo (PWG-ru work stays in its own repos). Companion diff artifacts: [csl-observatory `data/pwg_scan_index_tracker/andhrabharati_ls_diff/`](https://github.com/sanskrit-lexicon/csl-observatory/tree/main/data/pwg_scan_index_tracker/andhrabharati_ls_diff).
