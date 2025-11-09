
issue98fix

cp temp_pw_0.txt temp_pw_1.txt

---------------------------------------------
# YĀJÑ. corresponds to linktarget
pw YĀJÑ. ([0-9]+),([0-9]+),

python lsfix2.py pw temp_pw_0.txt lsfix2_pw_0.txt
(None,1),(True,194),(fixed,2),(all,197) lsfix2_pw_0.txt

cp temp_pw_0.txt temp_pw_1.txt
# edit changes to temp_pw_1.txt

python lsfix2.py pw temp_pw_1.txt lsfix2_pw_1.txt
(True,195),(fixed,2),(all,197) lsfix2_pw_1.txt

No None instances:  

---------------------------
MISC COMMENTS

END MISC COMMENTS

--------------------------------

# generate temp_pw_2.txt from temp_pw_1.txt and the 'fixed' elements

python dict_replace2.py temp_pw_1.txt lsfix2_pw_1.txt temp_pw_2.txt
apply_repls: 2 lines changed

-----------------------------------------------------------
# remake xml from temp_pw_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue98fix
cp temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue98fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pw temp_pw_2.txt lsfix2_pw_2.txt
(True,199),(all,199) lsfix2_pw_2.txt

Additional links: (- 199 194) 5

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pw_0.txt temp_pw_1.txt change_pw_1.txt
3 changes written to change_pw_1.txt

python diff_to_changes_dict.py temp_pw_1.txt temp_pw_2.txt change_pw_2.txt
2 changes written to change_pw_2.txt

===========================================

chkidx compares the kosha references and the link target index.

lsfix3.py is variation of lsfix2.py.  It prepares the input to chkidx.

python lsfix3.py pw temp_pw_2.txt lsfix3_pw_2.txt
(True,199),(all,199) lsfix3_pw_2.txt


python chkidx.py lsfix3_pw_2.txt index.txt lsfix3_chkidx_pw_2.txt
199 instances find ipage out of 199
0 references NOT FOUND in index
