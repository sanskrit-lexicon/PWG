
issue98fix

cp temp_pwkvn_0.txt temp_pwkvn_1.txt

---------------------------------------------
# YĀJÑ. corresponds to linktarget
pwkvn YĀJÑ. ([0-9]+),([0-9]+),

python lsfix2.py pwkvn temp_pwkvn_0.txt lsfix2_pwkvn_0.txt
(None,2),(True,60),(fixed,1),(all,63) lsfix2_pwkvn_0.txt

cp temp_pwkvn_0.txt temp_pwkvn_1.txt
# edit changes to temp_pwkvn_1.txt

python lsfix2.py pwkvn temp_pwkvn_1.txt lsfix2_pwkvn_1.txt
(None,1),(True,61),(fixed,1),(all,63) lsfix2_pwkvn_1.txt

None instance:  
64298   pAYcanaKa       <ls>YĀJÑ. 290. fg.</ls>

--------------------------------

# generate temp_pwkvn_2.txt from temp_pwkvn_1.txt and the 'fixed' elements

python dict_replace2.py temp_pwkvn_1.txt lsfix2_pwkvn_1.txt temp_pwkvn_2.txt
apply_repls: 1 lines changed

-----------------------------------------------------------
# remake xml from temp_pwkvn_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue98fix
cp temp_pwkvn_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwkvn  ../../pwkvn
sh xmlchk_xampp.sh pwkvn
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue98fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pwkvn temp_pwkvn_2.txt lsfix2_pwkvn_2.txt
(None,1),(True,63),(all,64) lsfix2_pwkvn_2.txt

Additional links: (- 63 60) 3

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwkvn_0.txt temp_pwkvn_1.txt change_pwkvn_1.txt
1 changes written to change_pwkvn_1.txt

python diff_to_changes_dict.py temp_pwkvn_1.txt temp_pwkvn_2.txt change_pwkvn_2.txt
1 changes written to change_pwkvn_2.txt

===========================================

chkidx compares the kosha references and the link target index.

lsfix3.py is variation of lsfix2.py.  It prepares the input to chkidx.

python lsfix3.py pwkvn temp_pwkvn_2.txt lsfix3_pwkvn_2.txt
(True,63),(all,63) lsfix3_pwkvn_2.txt

python chkidx.py lsfix3_pwkvn_2.txt index.txt lsfix3_chkidx_pwkvn_2.txt
63 instances find ipage out of 63
0 references NOT FOUND in index
