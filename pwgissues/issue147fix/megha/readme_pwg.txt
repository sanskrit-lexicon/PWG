
issue147fix/megha

pwg link forms:
MEGH. ([0-9]+)

python lsfix2.py pwg temp_pwg_0.txt lsfix2_pwg_0.txt

2019 lines written to lsfix2_pwg_0.txt
(True, 1) 1792
('fixed', 1) 216
(False, 1) 6
(None, 1) 5

cp temp_pwg_0.txt temp_pwg_1.txt

Edit temp_pwg_1.txt to resolve the None and False

--------------
python lsfix2.py pwg temp_pwg_1.txt lsfix2_pwg_1.txt

2025 lines written to lsfix2_pwg_1.txt
(True, 1) 1803
('fixed', 1) 217
(None, 1) 5

The 5 None are of form 'MEGH. ed. ST.' (Stenzler edition)

--------------------
# generate temp_pwg_2.txt from temp_pwg_0.txt and the 'fixed' elements

python dict_replace2.py temp_pwg_1.txt lsfix2_pwg_1.txt temp_pwg_2.txt
216 lines to change

-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue147fix/megha
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue147fix/megha
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pwg temp_pwg_2.txt lsfix2_pwg_2.txt

2367 lines written to lsfix2_pwg_2.txt
(True, 1) 2362
(None, 1) 5


(- 2362 1792)  570 additional standard links

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
6 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
216 changes written to change_pwg_2.txt

