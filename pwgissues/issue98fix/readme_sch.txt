
issue98fix

cp temp_sch_0.txt temp_sch_1.txt

---------------------------------------------
# YĀJÑ. corresponds to linktarget
sch Yājñ. ([0-9]+),([0-9]+),

python lsfix2.py sch temp_sch_0.txt lsfix2_sch_0.txt
(None,2),(True,58),(fixed,1),(all,61) lsfix2_sch_0.txt

cp temp_sch_0.txt temp_sch_1.txt
# edit changes to temp_sch_1.txt

python lsfix2.py sch temp_sch_1.txt lsfix2_sch_1.txt
(None,1),(True,59),(fixed,1),(all,61) lsfix2_sch_1.txt

None instance:
56337   pAYcanaKa       <ls>Yājñ. 290</ls>

--------------------------------

# generate temp_sch_2.txt from temp_sch_1.txt and the 'fixed' elements

python dict_replace2.py temp_sch_1.txt lsfix2_sch_1.txt temp_sch_2.txt
apply_repls: 1 lines changed

-----------------------------------------------------------
# remake xml from temp_sch_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue98fix
cp temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh sch  ../../sch
sh xmlchk_xampp.sh sch
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue98fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py sch temp_sch_2.txt lsfix2_sch_2.txt
(None,1),(True,61),(all,62) lsfix2_sch_2.txt

Additional links: (- 61 58) 3

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_sch_0.txt temp_sch_1.txt change_sch_1.txt
1 changes written to change_sch_1.txt

python diff_to_changes_dict.py temp_sch_1.txt temp_sch_2.txt change_sch_2.txt
1 changes written to change_sch_2.txt

===========================================

chkidx compares the kosha references and the link target index.

lsfix3.py is variation of lsfix2.py.  It prepares the input to chkidx.

python lsfix3.py sch temp_sch_2.txt lsfix3_sch_2.txt
(True,61),(all,61) lsfix3_sch_2.txt

python chkidx.py lsfix3_sch_2.txt index.txt lsfix3_chkidx_sch_2.txt
61 instances find ipage out of 61
0 references NOT FOUND in index

