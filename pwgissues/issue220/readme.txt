workflow log for issue220 — CDSL/AB merge
==========================================

## Objective
Normalize temp_cdsl_0.txt (CDSL) to match temp_ab_0.txt (AB) format
conventions, producing temp_cdsl_1.txt. AB_1 is AB passed through
unchanged (it already follows the target conventions).

## Direction
CDSL → AB. The previous step1.py tried block-aligned <ls> tag expansion
(AB→CDSL) but the gains were dominated by genuine content differences,
so the script was rewritten as a minimal set of CDSL-side format fixes.

## step1.py (current) — three CDSL transforms
1. `{%` before `<bot>` and `%}` after `</bot>`
   AB: `{%<bot>Hedysarum gangeticum</bot>%}` (AB_0 wraps bot tags)
2. `<k2>([^<]*)<h>([0-9]+)` → `<k2>\2. \1`  (hom number before headword)
   CDSL: `<k2>aMSa<h>1`  AB: `<k2>1. aMSa`
   Applies to headers only; with step 3 most headers now come from AB, so
   this mainly affects the 10 CDSL-only blocks.
3. Header merge: for each CDSL <L> block whose <L> number also exists in
   AB, replace CDSL's header line with AB's header line. (L number =
   full string, incl. decimal sub-numbers like 13188.1.)
   Replaced 123,356 of 123,366 CDSL headers; the 10 unmatched blocks are
   CDSL-only (14148.132, 14148.196, 26305.605, 37259.010, 37259.130,
   37259.135, 70027, 80800.04, 80800.10, 80800.17). AB has 0 unmatched.
   Third transform from the previous version (`^[0-9].` → <hom>) removed
   at the user's request — it matched 0 lines anyway.
4. Before a bare '— <ab>X</ab>' where X is in the set of <ab> contents
   that AB wraps after <div n="conj">, write '<div n="conj">'.
   The set is computed from AB: caus., partic., desid., intens., pass.,
   Caus., Desid., des., part., Intens., Denom., intrans., insens.
   Wrapped 2,683 bare CDSL markers (caus. 1728, desid. 422, intens. 288,
   partic. 161, pass. 48, Caus. 11, Desid. 9, des. 7, part. 4, Intens. 2,
   insens. 2, Denom. 1). Already-wrapped markers untouched (negative
   lookbehind). Remaining bare markers (Vgl. 14640, Viell., med., N. pr.,
   Z., S., …) are not in AB's set and stay bare.
5. '</ab> zu <ls' → '</ab>_zu_<ls'  (broad pattern, incl. <ls n=; CDSL)
   AB uses the underscore form predominantly (4,200 vs 771 spaced);
   CDSL had it spaced 4,950 times (8 underscored). Broadened to match
   AB's rule: CDSL_1 now 0 spaced, 5,257 underscore.
9. '</ab> des <ls' → '</ab>_des_<ls'  (CDSL)
   Same underscore convention for 'des': AB has 128 underscore vs 1
   spaced; CDSL had 129 spaced, 0 underscored. All 129 converted.
6. Collapse multiple spaces into one and remove trailing whitespace.
   AB is clean (0 lines with 2+ spaces, 2 trailing-ws lines); CDSL had
   180 multi-space lines. The rstrip runs at the END of the line
   pipeline (after the header merge), so it also strips the trailing
   space that AB's header <k2>graB,  carries. CDSL_1: 0 multi-space and
   0 trailing-ws lines. (AB_1 keeps its 2 trailing-ws lines; the
   stripped header is now the 1 non-identical shared header.)
7. '<div n="p">' → '<div n="pf">'
   AB uses <div n="pf"> predominantly (8,664 vs 15 <div n="p">); CDSL
   had 9,198 <div n="p"> and 0 <div n="pf">. All 9,198 converted.
8. AB: '</ab> zu <ls' → '</ab>_zu_<ls>'  (broad pattern, incl. <ls n=)
   AB had 771 '</ab> zu <ls>' plus <ls n= forms; now 0 spaced, 5,267
   underscore in AB_1 (was 4,200).

## Results
                 CDSL_1         AB_1
Lines             593,597        594,904
<L> headers        123,366        123,356
<k2>              123,366        123,356   (all shared headers identical)
<h>                       0              0   (headers now come from AB)
{%<bot>              5,420        4,754   (CDSL has 666 more wrapped)
<bot>                5,420        5,323   (AB has 97 fewer bot tags)
<hom>               23,438       23,449
<div n="conj">         2,750        3,060   (gap 310; 2,683 bare markers wrapped)
</ab>_zu_<ls          5,257        5,267   (both sides 0 spaced; gap 10)
2+ space lines           0              0   (CDSL had 180; AB is clean)
trailing-ws lines        0              2   (CDSL stripped; AB keeps its 2)
<div n="pf">           9,198        8,664   (all 9,198 CDSL <div n="p"> converted)

Header alignment: all 123,356 shared <L> numbers have byte-identical
headers between CDSL_1 and AB_1, except 1: L 119835 (<k2>graB, ), whose
trailing space CDSL strips. Only the 10 CDSL-only blocks (above) keep
CDSL's own header.

Diff lines: 176,061  (raw full-file diff; no block alignment)

With transform 10 (space before '?' after '}' only; '>?' left unspaced
to match AB) the step1 raw diff is 175,209; final step2 diff 51,844
(below).

## step2.py — restore </ls> / <ls n="..."> tags into AB from CDSL
For line pairs (CDSL_1, AB_1) aligned within the same <L> block, if the
ONLY difference is that AB is missing some '</ls>' and/or '<ls n="...">'
tokens (subset deletion; nothing else differs), merge the missing tokens
into AB's line.  This is a character-level subsequence check: AB = CDSL
with zero or more of those tokens deleted, separators/other text retained.
AB's own '√' root markers (which AB writes after <hom>N.</hom> where CDSL
does not) are allowed as AB-side insertions and KEPT in the output — the
merge only ever adds ls tokens to the AB line, never removes AB content.

Matching within a <replace> run uses a maximum bipartite matching over
merge_ls(c, a) instead of positional pairing, so a line-merge on
the AB side (e.g. L 1607, AB merges the '1〉 loc.' and 'a〉 subst.' CDSL
lines) no longer shifts the pairing off-by-one and drops restorable
lines like <ls>VID. 187</ls>. <ls n="VID.">211</ls>.

  Restored lines (Phase A): 34,659
  Restored lines (Phase B):  5,398
  Output: temp_ab_2.txt  594,904 lines (same count as AB_1; line
  replacement only, no CDSL-only blocks added)
  Diff CDSL_1 vs AB_2:      51,844  (was 176,061 CDSL_1 vs AB_1)
  Word-diff change groups:  11,497 lines still differ in content
  Exhaustive re-scan: 0 lines in any non-equal region still have a
  restorable '-/+' pair in AB_2, so every remaining diff line is a
  genuine content difference (not a missing </ls>/<ls n=...>).

Phase B (git word-diff): runs
  git diff --no-index --word-diff=porcelain temp_cdsl_1.txt temp_ab_2.txt
  and stores the output in worddiff_porcelain.txt. Git's character-level
  alignment pairs CDSL's single entry line against AB's several lines when
  AB splits an entry (e.g. <div n="conj"> sections on their own lines, as
  in L 47 {#aMh#} and L 1087 {#aw#}): the first AB line is still CDSL
  minus ls tokens, so Phase A's within-line matching never sees it. For
  each '~'-terminated porcelain group, process its '-/+' segment pairs:
  if the '+' segment is the '-' segment with only ls tokens removed
  (is_subset_delete), restore the '-' segment into the AB line; otherwise
  keep '+' (AB's own content — '<ab>adj.</ab>' vs CDSL's '<lex>adj.</lex>',
  AB's '√', etc.).  A lone '-' that is entirely ls tokens is restored too.
  The AB line is located by exact match near the '@@'-anchored index
  (bounded search for git's stray '~' terminators around CDSL-only blocks).
  The pass iterates to a fixpoint: each restore shifts git's alignment and
  can unlock further '-/+' pairs, so the diff is re-run until nothing
  changes (the file is written back between iterations).

Note: the 194K diff is a raw comparison. It is NOT comparable to the
84K figure from the old script, which did block alignment (matching by
<pc>,<k1>), copied AB headers onto CDSL, and expanded AB's <ls> tags.
The 3 transforms here only align format conventions and headers; content
differences (renumbered <hom>, different examples, AB `!√` + <ab>denom.</ab>,
<bot> gaps etc.) remain and account for most of the diff.

## Runtime
step1.py: ~1.1s on M-series Mac.
