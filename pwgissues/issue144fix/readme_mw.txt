
issue144fix

mw link forms:

# mwa Taitt. Br.
#  no references of this form in mw
#python lsfix2.py mwa temp_mw_0.txt lsfix2_mwa_0.txt

 
---------------------------------------------
# TBR. corresponds to linktarget
mw TBR. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)  
python lsfix2.py mw temp_mw_0.txt lsfix2_mw_0.txt
(None,257),(all,257) lsfix2_mw_0.txt

cp temp_mw_0.txt temp_mw_1.txt
couple of changes

python lsfix2.py mw temp_mw_1.txt lsfix2_mw_1.txt
(None,257),(all,257) lsfix2_mw_1.txt

Classification of instances 

not linked:
 109 matches for "<ls>TBr. [i]+\( f+\)?\.?</ls>"
   2 matches for "<ls n="TBr.">[i]+\( f+\)?\.?</ls>"
  14 matches for "<ls>TBr. [i]+, [0-9]+, [0-9]+\( f+\)?\.?</ls>"
   1 matches for "<ls n="TBr.">[i]+, [0-9]+\( f+\)?\.?</ls>"
     matches for "<ls n="TBr.">[i]+, [0-9]+, [0-9]+\( f+\)?\.?</ls>"
     matches for "<ls n="TBr. [i]+,">[0-9]+\( f+\)?\.?</ls>"
   5 matches for "<ls>TBr. [i]+, [0-9]+\( f+\)?\.?</ls>"
(+ 109 2 14 1 5) 131
linked:
 124 matches for "<ls>TBr. [i]+, [0-9]+, [0-9]+, [0-9]+\( f+\)?\.?</ls>"
   1 matches for "<ls n="TBr.">[i]+, [0-9]+, [0-9]+, [0-9]+\( f+\)?\.?</ls>"
   1 matches for "<ls n="TBr. [i]+, [0-9]+, [0-9]+,">[0-9]+\( f+\)?\.?</ls>"
     matches for "<ls n="TBr. [i]+, [0-9]+,">[0-9]+, [0-9]+\( f+\)?\.?</ls>"
     matches for "<ls n="TBr. [i]+,">[0-9]+, [0-9]+, [0-9]+\( f+\)?\.?</ls>"
     matches for "<ls n="TBr. [i]+,">[0-9]+, [0-9]+\( f+\)?\.?</ls>"
(+ 124 1 1) 126

(+ 131 126) 257  as expected
---------------------------
# no fixed elements to generate
# generate temp_mw_2.txt from temp_mw_1.txt and the 'fixed' elements
# python dict_replace2.py temp_mw_1.txt lsfix2_mw_1.txt temp_mw_2.txt

-----------------------------------------------------------
# remake xml from temp_mw_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue144fix
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue144fix
-- end of 'remake xml ...'

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_mw_0.txt temp_mw_1.txt change_mw_1.txt
1 changes written to change_mw_1.txt

===========================================

chkidx compares the kosha references and the link target index.
These programs don't work for mw

#python lsfix3.py mw temp_mw_2.txt lsfix3_mw_2.txt

# cp ../issue144/index.txt  index.txt
# index1.txt  # revise by removing first field (volume)
  Note: kanda 1,2  from volume I (ipage 1-361)
        kanda 3 from volume III (ipage 1-293)
 
#python chkidx.py lsfix3_mw_2.txt index1.txt lsfix3_chkidx_mw_2.txt

