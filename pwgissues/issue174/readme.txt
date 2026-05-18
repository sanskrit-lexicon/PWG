PWG issue #174 — enhance markup for common abbreviations
=========================================================

Working files for https://github.com/sanskrit-lexicon/PWG/issues/174.
Generated automatically as the "Phase A–F" first pass; everything here
is meant to *reduce* the human review surface, not replace it.

Inputs (from AB, attached to the issue)
---------------------------------------
  PWG_abbr_global.txt   787 global abbreviation forms (context-free)
  PWG_abbr_local.txt    164 context-dependent abbreviations (AB will overlay)
  AB_tags_PWG.txt       ~32 proposed new tag types

Scripts (run in order)
----------------------
  01_audit_global.py    crude first-pass audit (kept for reference)
  02_audit_refined.py   audit that excludes already-tagged content
                          → audit_refined.tsv
                          → audit_refined_summary.txt
  03_safewrap.py        per-line wrap of unambiguous abbreviations
                          (alpha≥3, not in DENYLIST)
                          → changes_safe.txt              (updateByLine format)
                          → changes_safe_stats.txt
                          → changes_safe_skipped.txt
  04_disambig.py        per-abbreviation worklists for the 48 deferred shorts
                          → disambig/<abbr>.txt           (one file each)
                          → disambig_index.txt
  05_make_pwgab.py      draft expansion table in MW format
                          → pwgab_input_draft.txt        (787 lines, 58 INFER)
  06_ab_tags_scan.py    occurrence count + candidates for AB's proposed tags
                          → ab_tags_scan.txt
  07_mw_crosscheck.py   identifies abbreviations shared with MW
                          → mw_overlap.txt               (136 exact)
                          → mw_diff_case.txt             (45 case-only)
                          → mw_pwg_existing.txt
                          → pwgab_with_mw_hints.txt

Headline numbers
----------------
  abbreviations in AB's global list:        787
  ambiguous (alpha < 3):                     48   → Phase C worklist
  raw occurrences in pwg.txt:               534,137
    already inside <ab>:                     1,731
    inside other tags (<ls>,<lex>,…):      333,895
    bare narrative (real wrap targets):    198,511
  Phase B applied:                          102,565 wraps over 88,854 lines
  remaining bare for review (Phase C):       ~96,000 in 48 abbreviations
  Phase D: pwgab_input_draft.txt:            787 lines, 58 flagged <INFER/>
  Phase F: identical to MW abbreviations:    136

Apply Phase B changes
---------------------
The change file is in the updateByLine.py format. To apply:

  cd <some scratch>/
  python /path/to/updateByLine.py \\
      ../../csl-orig/v02/pwg/pwg.txt \\
      changes_safe.txt \\
      pwg_with_abs.txt

The diff between pwg.txt and pwg_with_abs.txt will show every wrap.

Open items for human review
---------------------------
1. False positives in Phase B:
   - Currently only `vor.` is denylisted. Reviewers should grep
     `changes_safe.txt` for `<ab>X</ab>$` at end-of-line for any X that
     is also a common German word in narrative.

2. Local-abbreviation collision:
   - AB plans to overlay local abbreviations (e.g. `<ab n="dem und dem Ort">
     u. d. O.</ab>`) after globals are marked. Phase B will have wrapped
     parts of these (e.g. `<ab>u. d.</ab> O.`). AB's local pass overrides.

3. <INFER/> entries in pwgab_input_draft.txt:
   - 58 entries whose German expansion is uncertain. Filter with
     `grep '<INFER/>' pwgab_input_draft.txt`.

4. AB-tags semantics:
   - Several proposed tags (`<ns>`, `<iw>`, `<mng>`, `<ed>`, `<ms>`,
     `<pe>`, `<per>`) have zero current usage and no obvious heuristic.
     AB needs to specify intent before they can be applied.

5. Merging with csl-pywork:
   - The existing pwgab_input.txt at csl-pywork has 54 entries with a few
     formatting inconsistencies (e.g. `v.l.` vs `v. l.`). The draft uses
     the spelling from AB's global list. Merge decision is up to Jim.

Conventions followed
--------------------
- pwgissues/issueNNN/ folder structure (per CLAUDE.md)
- updateByLine.py paired-line change format (per pwg_ls2/*/)
- MW mwab_input.txt format for the expansion table
- All scripts: sys.stdout.reconfigure(encoding='utf-8'), `python -u`
