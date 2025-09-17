
issue48fix

pw link forms:
2 parms is Calcutta edition
3 parms is Bombay edition
<ls>MBH. ([0-9]+),([0-9]+),([0-9]+)  # bombay edition
<ls>MBH. ed. Bomb. ([0-9]+),([0-9]+),([0-9]+) 
<ls>MBH. ([0-9]+),([0-9]+)  # calcutta edition

python lsfix2.py pw temp_pw_0.txt lsfix2_pw_0.txt

4229 lines written to lsfix2_pw_0.txt
('fixed', 3) 203
(True, 3) 3364
(True, 2) 561
(None, 2) 88
(False, 2) 7
('fixed', 2) 6

cp temp_pw_0.txt temp_pw_1.txt

Edit temp_pw_1.txt to resolve the None and False

207961 : brahmalOkika : MBH. 13,150 (151),46 : MBH. 13,151,46 (150) : ref found @151 print change

python lsfix2.py pw temp_pw_1.txt lsfix2_pw_1.txt

4232 lines written to lsfix2_pw_1.txt
('fixed', 3) 203
(True, 3) 3371
(True, 2) 572
(None, 2) 79
('fixed', 2) 7

Subsets of None/False
29 Bomb
 5 Calc
40 Vardh
 5 [other]
(+ 29 5 40 5) 79  as expected

--------------------
# generate temp_pw_2.txt from temp_pw_0.txt and the 'fixed' elements

python dict_replace2.py temp_pw_1.txt lsfix2_pw_1.txt temp_pw_2.txt
209 lines to change

-----------------------------------------------------------
# remake xml from temp_pw_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue48fix
cp temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue48fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pw temp_pw_2.txt lsfix2_pw_2.txt

4514 lines written to lsfix2_pw_2.txt
(True, 3) 3848
(True, 2) 587
(None, 2) 79


(- (+ 3848 587) (+ 3364 561) )  510 additional standard links

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pw_0.txt temp_pw_1.txt change_pw_1.txt
16 changes written to change_pw_1.txt

python diff_to_changes_dict.py temp_pw_1.txt temp_pw_2.txt change_pw_2.txt
209 changes written to change_pw_2.txt

