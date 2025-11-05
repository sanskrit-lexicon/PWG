
issue134fix

---------------------------------------------
# TS. corresponds to linktarget
mw TS. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)

Other refs starting with 'TS.' (these excluded in further analysis)

11 matches for "TS. Prāt."
 
These are excluded in lsfix2 analysis.

python lsfix2.py mw temp_mw_0.txt lsfix2_mw_0.txt

cp temp_mw_0.txt temp_mw_1.txt
# edit changes to temp_mw_1.txt

python lsfix2.py mw temp_mw_1.txt lsfix2_mw_1.txt
(None,578),(all,578) lsfix2_mw_0.txt

lsfix2 does not properly analyze the references for mw
(None,578),(all,578) lsfix2_mw_1.txt

classify the instances

not linked
 16 matches for "<ls>TS. [ivx]+, [0-9]+, [0-9]+\( f+\)?\.?</ls>"
313 matches for "<ls>TS. [ivx]+\( f+\)?\.?</ls>"
 22 matches for "<ls n="TS.">[ivx]+\( f+\)?\.?</ls>"
  8 matches for "<ls>TS. [ivx]+, [0-9]+\( f+\)?\.?</ls>"
  2 misc
    266204	jAyAnya	<ls n="TS. ii,">5</ls>
    674352	vizRvatikrama	<ls n="TS.">iii, 5, 3</ls>
    
linked
 206 matches for "<ls>TS. [ivx]+, [0-9]+, [0-9]+, [0-9]+\( f+\)?\.?</ls>"
   6 matches for "<ls n="TS.">[ivx]+, [0-9]+, [0-9]+, [0-9]+\( f+\)?\.?</ls>"
   3 matches for "<ls n="TS. [ivx]+, [0-9]+, [0-9]+,">[0-9]+\( f+\)?\.?</ls>"
   0 matches for "<ls n="TS. [ivx]+, [0-9]+,">[0-9]+, [0-9]+\( f+\)?\.?</ls>"
   1 matches for "<ls n="TS. [ivx]+,">[0-9]+, [0-9]+, [0-9]+\( f+\)?\.?</ls>"
   1 matches for "<ls n="TS. [ivx]+,">[0-9]+, [0-9]+\( f+\)?\.?</ls>"

====================================


# generate temp_mw_2.txt from temp_mw_1.txt and the 'fixed' elements
# not applicable for mw
# python dict_replace2.py temp_mw_1.txt lsfix2_mw_1.txt temp_mw_2.txt

-----------------------------------------------------------
# remake xml from temp_mw_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue134fix
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue134fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

---- documentation in change files
python diff_to_changes_dict.py temp_mw_0.txt temp_mw_1.txt change_mw_1.txt
2 changes written to change_mw_1.txt

===========================================

chkidx compares the kosha references and the link target index.

Not available for mw.

