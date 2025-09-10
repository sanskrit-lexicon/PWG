
sch  
python lsfix2.py sch temp_sch_0.txt lsfix2_sch_0.txt

82 lines written to lsfix2_sch_0.txt
(None, 3) 3
(True, 3) 74
('fixed', 3) 1
('fixed', 2) 1
(True, 2) 3


cp temp_sch_0.txt temp_sch_1.txt

python lsfix2.py sch temp_sch_1.txt lsfix2_sch_1.txt

90 lines written to lsfix2_sch_1.txt
(True, 3) 85
('fixed', 3) 1
('fixed', 2) 1
(True, 2) 3


----------------------------
# generate temp_sch_2.txt from temp_sch_1.txt and the 'fixed' elements

python dict_replace2.py temp_sch_1.txt lsfix2_sch_1.txt temp_sch_2.txt

90 lines read from lsfix2_sch_1.txt
2 lines to change

-----------------------------------------------------------
# remake xml from temp_sch_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue136fix
cp temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh sch  ../../sch
sh xmlchk_xampp.sh sch
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue136fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py sch temp_sch_2.txt lsfix2_sch_2.txt

93 lines written to lsfix2_sch_2.txt
(True, 3) 87
(True, 2) 6

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_sch_0.txt temp_sch_1.txt change_sch_1.txt
3 changes written to change_sch_1.txt

python diff_to_changes_dict.py temp_sch_1.txt temp_sch_2.txt change_sch_2.txt
2 changes written to change_sch_2.txt
