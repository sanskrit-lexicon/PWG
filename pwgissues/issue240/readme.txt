issue240 -- PWG ls abbreviations: full-auto diff of the Andhrabharati update
vs CDSL pwgbib (2026-09-24).

GitHub issue: https://github.com/sanskrit-lexicon/PWG/issues/240
(cc @Andhrabharati)

2680 distinct ls values (AB update, sha256 f44ae1bbccca1ceb508e9da0c1c389dcb9-
3910fb570d0a4d962819cf756b5fd0) vs 2838 pwgbib codes: 2006 exact-matched;
674 added (449 prefix-resolved, 10 case-only, 215 true unknowns); 832 removed
(86 prefix-cited, 19 case-only, 727 totally uncited). Case preserved; NFC +
whitespace collapse only; longest-prefix attribution per the CDSL method.

No working files here: all diff artifacts (REPORT.md with the MG rulings,
added/deleted/unknown TSVs, generator script) live in
sanskrit-lexicon/csl-observatory data/pwg_scan_index_tracker/andhrabharati_ls_diff/
(landing PR csl-observatory#235). Follow-up handoffs: H5465 (Cologne Addition
entries + defect list + upstream PR), H5466 (full-set taxonomy classifier).
