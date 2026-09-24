# H5465 — 215 Cologne additions + pwgissues defect issue + upstream PR + kosha reg

_Created: 24-09-2026 · Last updated: 24-09-2026_

_Field contract: [deep manual](https://github.com/gasyoun/Uprava/blob/main/docs/HANDOFF_LIFECYCLE_MACHINERY_DEEP_MANUAL.md)._

**Intended executor:** OxAlpha

**Effort:** medium  _(trivial <15m · medium 15m–2h · hard 2h+)_

**Launch box:** any

**Gate:** none  _(none|human:|handoff:|external:|deploy:|until: — H3413)_

## Mission

## Mission
Draft [Cologne Addition] pwgbib_input.txt entries for the 215 unknown ls strings (convention per csl-pywork pwgauth readme), file the pwgissues issue documenting pwg.txt text defects from the 24-09 diff (AGAYAPĀLA, AMṚTABINDŪP./AMṚTAV. UP., AINSL, case + candrabindu/Ṣ-Ś variants; MG: we do not change pwg.txt, we propose), offer the additions upstream as a PR (MG: local overlay + upstream PR offer), and register the final artifact in kosha datasets.json. MG ruling: repair first, then classify — this handoff precedes the classifier handoff.

## Inputs
- C:\Users\user\Documents\mw\pwg_ls_vs_cdsl_unknown.tsv (215 rows)
- CDSL pwgbib_input.txt (csl-pywork v02 pwgauth)
- diff report: csl-observatory data/pwg_scan_index_tracker/andhrabharati_ls_diff/

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

## Execution record (24-09-2026)

✅ EXECUTED — intended executor OxAlpha; the assigned lane stalled after landing
the diff issue (PWG#240, 19:00), execution completed by GLM
(`zai-coding-plan/glm-5.3-flash`) on MG's explicit «бери» (takeover ruling
after an 80-min all-surface liveness probe).

| Deliverable | Where |
|---|---|
| 215 `[Cologne Addition]` pwgbib entries (c.2180–c.2394; 15 confident / 5 guess / 40 identity / 155 `= ?`; `check_pwbib` PASS) | [csl-observatory#236](https://github.com/sanskrit-lexicon/csl-observatory/pull/236) MERGED |
| pwgissues defect documentation (4 classes, proposals only) | [#240 comment](https://github.com/sanskrit-lexicon/PWG/issues/240#issuecomment-5820130011) |
| upstream PR offer | [csl-pywork#94](https://github.com/sanskrit-lexicon/csl-pywork/pull/94) MERGED (2844 → 3059 records) |
| kosha `datasets.json` row `pwg-ls-additions-215` | [gasyoun/kosha#645](https://github.com/gasyoun/kosha/pull/645) OPEN — merge pending MG stale-base-guard ruling (README count bump, see PR) |
