
issue134fix

---------------------------------------------
# TS. corresponds to linktarget
pw TS. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)

Other refs starting with 'TS.' (these excluded in further analysis)
  5  matches for "TS. PRĀT."
 
These are excluded in lsfix2 analysis.
python lsfix2.py pwkvn temp_pwkvn_0.txt lsfix2_pwkvn_0.txt
(None,7),(True,151),(all,158) lsfix2_pwkvn_0.txt

cp temp_pwkvn_0.txt temp_pwkvn_1.txt
# edit changes to temp_pwkvn_1.txt

python lsfix2.py pwkvn temp_pwkvn_1.txt lsfix2_pwkvn_1.txt
(None,3),(True,154),(all,157) lsfix2_pwkvn_1.txt

====================================

None info:
14765	kAmyezwi	<ls n="TS.">2,374</ls>	
16100	dUreheti	<ls n="TS. 1,1008,">12</ls>	
69359	rAzwraBft	<ls>TS. 3,4,7</ls>	

---------------------------

# generate temp_pwkvn_2.txt from temp_pwkvn_1.txt and the 'fixed' elements
# no fixed items for pwkvn
#python dict_replace2.py temp_pwkvn_1.txt lsfix2_pwkvn_1.txt temp_pwkvn_2.txt

-----------------------------------------------------------
# remake xml from temp_pwkvn_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue134fix
cp temp_pwkvn_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwkvn  ../../pwkvn
sh xmlchk_xampp.sh pwkvn
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue134fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

# skip this: no pwkvn_2
#python lsfix2.py pwkvn temp_pwkvn_2.txt lsfix2_pwkvn_2.txt

Additional links: 3
---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwkvn_0.txt temp_pwkvn_1.txt change_pwkvn_1.txt
5 changes written to change_pwkvn_1.txt

===========================================

chkidx compares the kosha references and the link target index.

lsfix3.py is variation of lsfix2.py.  It prepares the input to chkidx.

python lsfix3.py pwkvn temp_pwkvn_1.txt lsfix3_pwkvn_1.txt
(True,154),(all,154) lsfix3_pwkvn_1.txt
( see readme_pwg.txt )

python chkidx.py lsfix3_pwkvn_1.txt index.txt lsfix3_chkidx_pwkvn_1.txt
153 instances find ipage out of 154
1 references NOT FOUND in index


