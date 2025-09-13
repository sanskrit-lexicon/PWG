
issue149fix

pwg link forms:
MĀLAV.  1 parm or 2 parms
<ls>MĀLAV. ([0-9]+),([0-9]+)

python lsfix2.py pwg temp_pwg_0.txt lsfix2_pwg_0.txt

1086 lines written to lsfix2_pwg_0.txt
('fixed', 2) 58
(True, 2) 529
(True, 1) 465
('fixed', 1) 13
(False, 1) 6
(None, 1) 15

cp temp_pwg_0.txt temp_pwg_1.txt

Edit temp_pwg_1.txt to resolve the None and False

28488 : taTAgata : 63, ult. : 63,23 : print change 23 is last line of page 63 of malavikagni
26484 : jana : MĀLAV. 26. 28,28. : MĀLAV. 26. 28,8. : print change

python lsfix2.py pwg temp_pwg_1.txt lsfix2_pwg_1.txt

1092 lines written to lsfix2_pwg_1.txt
('fixed', 2) 59
(True, 2) 539
(True, 1) 471
('fixed', 1) 13
(None, 1) 10

The 10 'None' are all `MĀLAV. ed. Bomb.`

--------------------
# generate temp_pwg_2.txt from temp_pwg_0.txt and the 'fixed' elements

python dict_replace2.py temp_pwg_1.txt lsfix2_pwg_1.txt temp_pwg_2.txt

72 lines to change
apply_repls: 72 lines changed
1
-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue149fix
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue149fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pwg temp_pwg_2.txt lsfix2_pwg_2.txt

1178 lines written to lsfix2_pwg_2.txt
(True, 2) 671
(True, 1) 497
(None, 1) 10


(- (+ 671 497) (+ 529 465)) 174 additional standard links

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
11 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
72 changes written to change_pwg_2.txt

