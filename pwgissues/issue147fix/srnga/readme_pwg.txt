
issue147fix/srnga

pwg link forms:
ŚṚṄGĀRAT. ([0-9]+)

python lsfix2.py pwg temp_pwg_0.txt lsfix2_pwg_0.txt

(True, 1) 91
('fixed', 1) 9

--------------------
# generate temp_pwg_1.txt from temp_pwg_0.txt and the 'fixed' elements

python dict_replace2.py temp_pwg_0.txt lsfix2_pwg_0.txt temp_pwg_1.txt
9 lines to change

-----------------------------------------------------------
# remake xml from temp_pwg_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue147fix/srnga
cp temp_pwg_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue147fix/srnga
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pwg temp_pwg_1.txt lsfix2_pwg_1.txt

(True, 1) 110


(- 110 91)  19 additional standard links

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
9 changes written to change_pwg_1.txt
