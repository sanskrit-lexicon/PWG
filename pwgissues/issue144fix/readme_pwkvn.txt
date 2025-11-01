
issue144fix

pwkvn link forms:

TAITTIRĪYA  # no parms

# pwkvna TAITT. BR.
#  
python lsfix2.py pwkvna temp_pwkvn_0.txt lsfix2_pwkvna_0.txt
(True,1),(all,1) lsfix2_pwkvna_0.txt

anuvatsarIRa	<ls>TAITT. BR. 1,4,10,3</ls>

In contrast to pwg,  this TAITT. BR. references DOES resolve in
  our link target.
  
---------------------------------------------
# TBR. corresponds to linktarget
pw TBR. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)  
python lsfix2.py pwkvn temp_pwkvn_0.txt lsfix2_pwkvn_0.txt
(None,2),(True,50),(all,52) lsfix2_pwkvn_0.txt

cp temp_pwkvn_0.txt temp_pwkvn_1.txt
correct a few

python lsfix2.py pwkvn temp_pwkvn_1.txt lsfix2_pwkvn_1.txt
(None,1),(True,51),(all,52) lsfix2_pwkvn_1.txt

None info:
indrakarman	<ls>TBR. 2,549,6</ls>

---------------------------
# no 'fixed'
# generate temp_pwkvn_2.txt from temp_pwkvn_1.txt and the 'fixed' elements

#python dict_replace2.py temp_pwkvn_1.txt lsfix2_pwkvn_1.txt temp_pwkvn_2.txt
apply_repls: 20 lines changed

-----------------------------------------------------------
# remake xml from temp_pwkvn_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue144fix
cp temp_pwkvn_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwkvn  ../../pwkvn
sh xmlchk_xampp.sh pwkvn
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue144fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

#python lsfix2.py pwkvn temp_pwkvn_2.txt lsfix2_pwkvn_2.txt

Additional links: 
---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwkvn_0.txt temp_pwkvn_1.txt change_pwkvn_1.txt
1 changes written to change_pwkvn_1.txt

#python diff_to_changes_dict.py temp_pwkvn_1.txt temp_pwkvn_2.txt change_pwkvn_2.txt

===========================================

chkidx compares the kosha references and the link target index.

lsfix3.py is variation of lsfix2.py.  It prepares the input to chkidx.

python lsfix3.py pwkvn temp_pwkvn_1.txt lsfix3_pwkvn_1.txt
(True,51),(all,51) lsfix3_pwkvn_1.txt
example output line:
3326    aBiSAstar       <ls n="TBR. 3,10,">9,7</ls>     3,10,9,7

# cp ../issue144/index.txt  index.txt
# index1.txt  # revise by removing first field (volume)
  Note: kanda 1,2  from volume I (ipage 1-361)
        kanda 3 from volume III (ipage 1-293)
 
python chkidx.py lsfix3_pwkvn_1.txt index1.txt lsfix3_chkidx_pwkvn_1.txt
50 instances find ipage out of 51
1 reference NOT FOUND in index
None    11450   ajyAni  <ls>TBR. 5,7,2,5</ls>   5,7,2,5

