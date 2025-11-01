
issue144fix

sch link forms:

TAITTIRĪYA  # no parms

# scha Taitt. Br.
#  
python lsfix2.py scha temp_sch_0.txt lsfix2_scha_0.txt
(True,1),(all,1) lsfix2_scha_0.txt

In contrast to pwg,  this TAITT. BR. references DOES resolve in
  our link target.
  
---------------------------------------------
# TBR. corresponds to linktarget
sch TBR. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)  
python lsfix2.py sch temp_sch_0.txt lsfix2_sch_0.txt
(None,5),(True,45),(fixed,1),(all,51) lsfix2_sch_0.txt

cp temp_sch_0.txt temp_sch_1.txt
couple of changes

python lsfix2.py sch temp_sch_1.txt lsfix2_sch_1.txt
(None,3),(True,51),(fixed,1),(all,55) lsfix2_sch_1.txt

None info:  These are part of 'commentary' refs
13005	aBistaraRa	<ls>TBr. 3,483,9.</ls>	
21444	ADitsu	<ls>TBr. 1,58,3.</ls>	
23690	indrakarman	<ls>TBr. 2,549,6.</ls>	

---------------------------
# generate temp_sch_2.txt from temp_sch_1.txt and the 'fixed' elements

python dict_replace2.py temp_sch_1.txt lsfix2_sch_1.txt temp_sch_2.txt
apply_repls: 1 lines changed

-----------------------------------------------------------
# remake xml from temp_sch_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue144fix
cp temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh sch  ../../sch
sh xmlchk_xampp.sh sch
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue144fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py sch temp_sch_2.txt lsfix2_sch_2.txt
(None,3),(True,53),(all,56) lsfix2_sch_2.txt

Additional links: (- 53 45) 8
---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_sch_0.txt temp_sch_1.txt change_sch_1.txt
2 changes written to change_sch_1.txt

python diff_to_changes_dict.py temp_sch_1.txt temp_sch_2.txt change_sch_2.txt
1 changes written to change_sch_2.txt
===========================================

chkidx compares the kosha references and the link target index.

lsfix3.py is variation of lsfix2.py.  It prepares the input to chkidx.

python lsfix3.py sch temp_sch_2.txt lsfix3_sch_2.txt

(True,53),(all,53) lsfix3_sch_2.txt

example output line:
3326    aBiSAstar       <ls n="TBR. 3,10,">9,7</ls>     3,10,9,7

# cp ../issue144/index.txt  index.txt
# index1.txt  # revise by removing first field (volume)
  Note: kanda 1,2  from volume I (ipage 1-361)
        kanda 3 from volume III (ipage 1-293)
 
python chkidx.py lsfix3_sch_2.txt index1.txt lsfix3_chkidx_sch_2.txt
52 instances find ipage out of 53
1 reference NOT FOUND in index

None    2661    ajyAni  <ls>TBr. 5,7,2,5</ls>   5,7,2,5

