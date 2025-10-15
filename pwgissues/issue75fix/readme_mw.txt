
issue75fix

========================================
mwa "R. ed. Bomb."  
python lsfix2.py mwa temp_mw_0.txt lsfix2_mw_0_a.txt
(None,2),(all,2) lsfix2_mw_0_a.txt

No change. I don't find "aByAhf	<ls>R. ed. Bomb. i, 61, 7.</ls>" in link.

========================================
mwa1 "R (B.)"
python lsfix2.py mwa1 temp_mw_0.txt lsfix2_mw_0_a1.txt
(None,13),(all,13) lsfix2_mw_0_a1.txt

These 13 have the right form, variations on 
    <ls>R. (B.) [ivx]+, [0-9]+, [0-9]+\.?</ls>

======================================================
mwa2 "R (B)"
python lsfix2.py mwa2 temp_mw_0.txt lsfix2_mw_0_a2.txt
(None,15),(all,15) lsfix2_mw_0_a2.txt

These 15 have the right form, variations on 
    <ls>R. (B) [ivx]+, [0-9]+, [0-9]+\.?</ls>

cp temp_mw_0.txt temp_mw_1.txt 

Make changes to temp_mw_1 for the 1 None/
Also, apply the 'fixed' items manually


========================================
mwb: "R. ..."  EXCLUDES "R. ed. Bomb." and several other forms
========================================
R. 3 parms.

python lsfix2.py mwb temp_mw_0.txt lsfix2_mw_0_b.txt
(None,1899),(all,1899) lsfix2_mw_0_b.txt

1263 matches for "<ls>R. [ivx]+, [0-9]+, [0-9]+\( f+\)?\.?</ls>"
 308 matches for "<ls>R. [xiv]+\( f+\)?\.?</ls>"
  59 matches for "<ls n="R.">[ivx]+, [0-9]+, [0-9]+\( f+\)?\.?</ls>"
  32 matches for "<ls n="R. [xiv]+,">[0-9]+, [0-9]+\( f+\)?\.?</ls>"
  82 matches for "<ls n="R.">[xiv]+\( f+\)?\.?</ls>"
  29 matches for "<ls>R. [xiv]+, [0-9]+\( f+\)?\.?</ls>"
  35 matches for "<ls n="R. [xiv]+, [0-9]+,">[0-9]+\( f+\)?\.?</ls>"
   2 matches for "<ls n="R. [xiv]+,">[0-9]+\( f+\)?\.?</ls>"
   5 matches for "<ls n="R.">[ivx]+, [0-9]+\( f+\)?\.?</ls>"
85 remain

See mw_variants.txt  for the various ways MW refers to
 the Bombay and Gorresio editions. 

python lsfix2.py mwb1 temp_mw_1.txt lsfix2_mw_1_b1.txt
(None,1899),(all,1899) lsfix2_mw_1_b1.txt

# Include all ls starting with 'R.'

python lsfix2.py mwb2 temp_mw_1.txt lsfix2_mw_1_b2.txt
(None,1983),(all,1983) lsfix2_mw_1_b2.txt

#  classify lsfix2_mw_1_b2.txt
1262 matches for "<ls>R. [ivx]+, [0-9]+, [0-9]+\( f+\)?\.?</ls>"
 308 matches for "<ls>R. [xiv]+\( f+\)?\.?</ls>"
  60 matches for "<ls n="R.">[ivx]+, [0-9]+, [0-9]+\( f+\)?\.?</ls>"
  32 matches for "<ls n="R. [xiv]+,">[0-9]+, [0-9]+\( f+\)?\.?</ls>"
  82 matches for "<ls n="R.">[xiv]+\( f+\)?\.?</ls>"
  30 matches for "<ls>R. [xiv]+, [0-9]+\( f+\)?\.?</ls>"
  35 matches for "<ls n="R. [xiv]+, [0-9]+,">[0-9]+\( f+\)?\.?</ls>"
   2 matches for "<ls n="R. [xiv]+,">[0-9]+\( f+\)?\.?</ls>"
   5 matches for "<ls n="R.">[ivx]+, [0-9]+\( f+\)?\.?</ls>"
   3 matches for "<ls>R. [ivx]+, <ab>ch.</ab> [0-9]+\.?</ls>"
   3 matches for "<ls>R. vii, [0-9]+, [0-9]+, [0-9]+\.?</ls>"
   1 matches for "<ls>R. vii, 36, 45/46</ls>" 
------------
   1 match for '<ls n="R. (G)'
   2 matches for '<ls n="R. G.'
  15 matches for "<ls>R. (B)"
  67 matches for "<ls>R. (B.)"
  19 matches for "<ls>R. (G)"
   6 matches for "<ls>R. (ed. Bomb.)"
   6 matches for "<ls>R. (ed. Gorr.)"
   7 matches for "<ls>R. B."
  14 matches for "<ls>R. G."
   7 matches for "<ls>R. \[B.]"
   2 matches for "<ls>R. \[B]"
   4 matches for "<ls>R. \[G]"
   2 matches for "<ls>R. ed. Bomb\."
   2 matches for "<ls>R. ed. Bombay"
   1 match   for "<ls>R. ed. Gorresio"
   
-----------------------------------
# Nothing to  generate temp_mw_2.txt from temp_mw_1.txt and the 'fixed' elements

# python dict_replace2.py temp_mw_1.txt lsfix2_mw_1_b.txt temp_mw_2.txt
# apply_repls: 42 lines changed

-----------------------------------------------------------
# remake xml from temp_mw_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue75fix
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue75fix
-- end of 'remake xml ...'

---------------------------------------------------


Total additional 17

---- documentation in change files
python diff_to_changes_dict.py temp_mw_0.txt temp_mw_1.txt change_mw_1.txt
11 changes written to change_mw_1.txt

