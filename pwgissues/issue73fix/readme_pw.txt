
issue73fix

pw link forms:
<ls>M. ([0-9]+),([0-9]+)

python lsfix2.py pw temp_pw_0.txt lsfix2_pw_0.txt

(True, 2) 434
('fixed', 2) 30
(None, 2) 60
(False, 2) 2

cp temp_pw_0.txt temp_pw_1.txt

Edit temp_pw_1.txt to resolve the None and False

python lsfix2.py pw temp_pw_1.txt lsfix2_pw_1.txt

525 lines written to lsfix2_pw_1.txt
(True, 2) 437
('fixed', 2) 30
(None, 2) 58


None:
53 M. MÜLLER  (M. = MAX, unrelated to Manu)
 4 M. (JOLLY)  different edition
 1 M. (ed. JOLLY)  different edition
58 as expected

--------------------
# generate temp_pw_2.txt from temp_pw_1.txt and the 'fixed' elements

python dict_replace2.py temp_pw_1.txt lsfix2_pw_1.txt temp_pw_2.txt

525 lines read from lsfix2_pw_1.txt
30 lines to change
apply_repls: 30 lines changed

-----------------------------------------------------------
# remake xml from temp_pw_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue73fix
cp temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue73fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pw temp_pw_2.txt lsfix2_pw_2.txt

(True, 2) 504  
(None, 2) 58


 (- 504 434 ) == 70  additional standard links

---------------------------------------------------
First parm should be 1-7 in our (1838) edition.
But 33 exceptions probably refer to unknown 1868 edition.

27 matches for "<ls>M. [0-9][0-9]," in buffer: lsfix2_pw_2.txt
1 match for "<ls n="M.">[0-9][0-9]," in buffer: lsfix2_pw_2.txt
2 match for "<ls n="M. [0-9][0-9],">" in buffer: lsfix2_pw_2.txt
3 matches for "[89]," in buffer: lsfix2_pw_2.txt

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pw_0.txt temp_pw_1.txt change_pw_1.txt
2 changes written to change_pw_1.txt

python diff_to_changes_dict.py temp_pw_1.txt temp_pw_2.txt change_pw_2.txt
5 changes written to change_pw_2.txt

