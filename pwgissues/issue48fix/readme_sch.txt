
issue48fix

sch link forms:
2 parms is Calcutta edition
3 parms is Bombay edition
<ls>MBh. ([0-9]+),([0-9]+),([0-9]+)  # bombay edition
cd<ls>MBh. ([0-9]+),([0-9]+)  # calcutta edition

python lsfix2.py sch temp_sch_0.txt lsfix2_sch_0.txt

(True, 3) 726
('fixed', 3) 10
(True, 2) 34
(False, 2) 1
(None, 2) 41
('fixed', 2) 4

cp temp_sch_0.txt temp_sch_1.txt

Edit temp_sch_1.txt to resolve the None and False

python lsfix2.py sch temp_sch_1.txt lsfix2_sch_1.txt

866 lines written to lsfix2_sch_1.txt
(True, 3) 813
('fixed', 3) 10
(True, 2) 35
('fixed', 2) 4
(None, 2) 4

classification 'None':
 3 Vardh
 1 [other]

--------------------
# generate temp_sch_2.txt from temp_sch_1.txt and the 'fixed' elements

python dict_replace2.py temp_sch_1.txt lsfix2_sch_1.txt temp_sch_2.txt
14 lines to change
apply_repls: 14 lines changed

-----------------------------------------------------------
# remake xml from temp_sch_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue48fix
cp temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh sch  ../../sch
sh xmlchk_xampp.sh sch
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue48fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py sch temp_sch_2.txt lsfix2_sch_2.txt
882 lines written to lsfix2_sch_2.txt
(True, 3) 835
(True, 2) 43
(None, 2) 4

(- (+ 835 43) (+ 726 34) )  118  additional standard links

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_sch_0.txt temp_sch_1.txt change_sch_1.txt
50 changes written to change_sch_1.txt

python diff_to_changes_dict.py temp_sch_1.txt temp_sch_2.txt change_sch_2.txt
14 changes written to change_sch_2.txt

