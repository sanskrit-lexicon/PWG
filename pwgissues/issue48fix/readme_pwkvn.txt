
issue48fix

pwkvn link forms:
2 parms is Calcutta edition
3 parms is Bombay edition
<ls>MBH. ([0-9]+),([0-9]+),([0-9]+)  # bombay edition
<ls>MBH. ed. Bomb. ([0-9]+),([0-9]+),([0-9]+) 
<ls>MBH. ([0-9]+),([0-9]+)  # calcutta edition

python lsfix2.py pwkvn temp_pwkvn_0.txt lsfix2_pwkvn_0.txt

892 lines written to lsfix2_pwkvn_0.txt
(True, 3) 836
(True, 2) 46
(None, 2) 7
(False, 2) 1
('fixed', 3) 2


cp temp_pwkvn_0.txt temp_pwkvn_1.txt

Edit temp_pwkvn_1.txt to resolve the None and False

207961 : brahmalOkika : MBH. 13,150 (151),46 : MBH. 13,151,46 (150) : ref found @151 print change

python lsfix2.py pwkvn temp_pwkvn_1.txt lsfix2_pwkvn_1.txt

893 lines written to lsfix2_pwkvn_1.txt
(True, 3) 839
(True, 2) 47
(None, 2) 5
('fixed', 3) 2

Subsets of None
 3 Vardh
 2 [other]

--------------------
# generate temp_pwkvn_2.txt from temp_pwkvn_1.txt and the 'fixed' elements

python dict_replace2.py temp_pwkvn_1.txt lsfix2_pwkvn_1.txt temp_pwkvn_2.txt
2 lines to change
apply_repls: 2 lines changed
7

-----------------------------------------------------------
# remake xml from temp_pwkvn_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue48fix
cp temp_pwkvn_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwkvn  ../../pwkvn
sh xmlchk_xampp.sh pwkvn
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue48fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pwkvn temp_pwkvn_2.txt lsfix2_pwkvn_2.txt

895 lines written to lsfix2_pwkvn_2.txt
(True, 3) 843
(True, 2) 47
(None, 2) 5

(- (+ 843 47) (+ 836 46) )  8  additional standard links

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwkvn_0.txt temp_pwkvn_1.txt change_pwkvn_1.txt
3 changes written to change_pwkvn_1.txt

python diff_to_changes_dict.py temp_pwkvn_1.txt temp_pwkvn_2.txt change_pwkvn_2.txt
2 changes written to change_pwkvn_2.txt

