
issue73fix

pwg link forms:
<ls>M. ([0-9]+),([0-9]+)

python lsfix2.py pwg temp_pwg_0.txt lsfix2_pwg_0.txt

22533 lines written to lsfix2_pwg_0.txt
(True, 2) 22523
(None, 2) 9
('fixed', 2) 1

cp temp_pwg_0.txt temp_pwg_1.txt

Edit temp_pwg_1.txt to resolve the None

No changes to None. All unlinked
 6  M. MüLLER
 2  M. ed. Calc.
 1  M. n. 94
 
--------------------
# generate temp_pwg_1.txt from temp_pwg_0.txt and the 'fixed' elements

python dict_replace2.py temp_pwg_0.txt lsfix2_pwg_0.txt temp_pwg_1.txt

22533 lines read from lsfix2_pwg_0.txt
1 lines to change
a
-----------------------------------------------------------
# remake xml from temp_pwg_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue73fix
cp temp_pwg_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue73fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pwg temp_pwg_1.txt lsfix2_pwg_1.txt

(True, 2) 22525
(None, 2) 9

1 additional standard link


---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
1 changes written to change_pwg_1.txt

