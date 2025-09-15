
issue122fix

pwg link forms:
<ls>MĀRK. P. ([0-9]+),([0-9]+)

python lsfix2.py pwg temp_pwg_0.txt lsfix2_pwg_0.txt

('fixed', 2) 728
(True, 2) 4556
(None, 2) 129
(False, 2) 13


cp temp_pwg_0.txt temp_pwg_1.txt

Edit temp_pwg_1.txt to resolve the None and False

26359 : jagannATa : MĀRK. P. 1,8,29. : MĀRK. P. 18,29. : print change


----------------------------------
python lsfix2.py pwg temp_pwg_1.txt lsfix2_pwg_1.txt

5426 lines written to lsfix2_pwg_1.txt
('fixed', 2) 742
(True, 2) 4633
(None, 2) 51

Classification of the 'None':
14 <ls>MĀRK. P. S. [0-9]+, Z. [0-9]+.
21 <ls>MĀRK. P. S\. .*?</ls>
 3 <ls n="MĀRK. P.">S\..*?</ls>
 1 <ls>MĀRK. P. 657, Z. 5</ls>
 2 <ls>MĀRK. P. [0-9]+,[0-9]+,[0-9]+\.?</ls>   3 parameters
 1 <ls n="MĀRK. P.">[0-9]+,[0-9]+,[0-9]+\.?</ls>
 3 <ls>MĀRK. P. Einl. [0-9]+\.?</ls>
 3 <ls>MĀRK. P. [0-9]+\.?</ls>
 2 <ls>MĀRK. P. [0-9]+\. fgg\.</ls>
--------------------
# generate temp_pwg_2.txt from temp_pwg_0.txt and the 'fixed' elements

python dict_replace2.py temp_pwg_1.txt lsfix2_pwg_1.txt temp_pwg_2.txt

742 lines to change
apply_repls: 742 lines changed
1
-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue122fix
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue122fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pwg temp_pwg_2.txt lsfix2_pwg_2.txt

2686 lines written to lsfix2_pwg_2.txt

(True, 2) 6389
(None, 2) 51

(- 6389 4556)  1833 additional standard links

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
105 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
742 changes written to change_pwg_2.txt

