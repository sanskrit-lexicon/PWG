
issue48fix

pwg link forms:
2 parms is Calcutta edition
3 parms is Bombay edition
<ls>MBH. ([0-9]+),([0-9]+),([0-9]+)  # bombay edition
<ls>MBH. ed. Bomb. ([0-9]+),([0-9]+),([0-9]+) 
<ls>MBH. ([0-9]+),([0-9]+)  # calcutta edition

python lsfix2.py pwg temp_pwg_0.txt lsfix2_pwg_0.txt

66779 lines written to lsfix2_pwg_0.txt
(True, 2) 66641
(None, 2) 108
('fixed', 2) 22
(False, 2) 4
('fixed', 3) 1
(True, 3) 3


cp temp_pwg_0.txt temp_pwg_1.txt

Edit temp_pwg_1.txt to resolve the None and False

43687 : palAyana : 15775. : 15774.  : print change
67140 : i : MBH. ed. Bomb. 1,6390 : MBH. 1,6390 : print change
112484 : sfkvi : MBH. ed. Bomb. 3,10397. : MBH. 3,10397. : print change
59359 : mahodarya : MBH. ed. Bomb. 13,7678. : MBH. 13,7678. : print change
60285 : mAsika : MBH. ed. Bomb. 14,2513 : MBH. 14,2513 : print change

--------------
python lsfix2.py pwg temp_pwg_1.txt lsfix2_pwg_1.txt

66774 lines written to lsfix2_pwg_1.txt
(True, 2) 66660
(None, 2) 85
('fixed', 2) 28
(True, 3) 1

66773 lines written to lsfix2_pwg_1.txt
(True, 2) 66660
(None, 2) 84
('fixed', 2) 28
(True, 3) 1

The remaining 'None' classified roughly:
 5 Bomb
18 adhy
 4 Kap
23 <ls>MBH. [0-9]+\.?</ls>
16 <ls>MBH. [0-9 .-]+</ls>
10 S\.
 8 misc. other
 (+ 5 18 4 23 16 10 8) = 84
---

cdsl displays do not link, except for
MBH. 7,6437,a  and MBH. 7,6437,b/
--- One sub-class of non-linked references ('None')
 dvAcatvAriMSa
  https://sanskrit-lexicon-scans.github.io/mbhcalc/?1.175065
  dvAcatvAriMSa occurs in the 'end of adhyAya 42' phrase
  
 {%der 42ste%}
<ls>MBH. 1. 8. 9. 13</ls> und <ls>R. GORR. 2. 3</ls> in den Unterschrr. der <is>Adhyāya</is> und <is>Sarga</is>.

--------------------
# generate temp_pwg_2.txt from temp_pwg_0.txt and the 'fixed' elements

python dict_replace2.py temp_pwg_1.txt lsfix2_pwg_1.txt temp_pwg_2.txt
28 lines to change

-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue48fix
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue48fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pwg temp_pwg_2.txt lsfix2_pwg_2.txt

(True, 2) 66752
(None, 2) 84
(True, 3) 1

(- 66753 66641)  111 additional standard links

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
47 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
28 changes written to change_pwg_2.txt

