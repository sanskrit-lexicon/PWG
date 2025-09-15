
issue122fix

sch link forms:
<ls>MĀRK. P. ([0-9]+),([0-9]+)

python lsfix2.py sch temp_sch_0.txt lsfix2_sch_0.txt

35 lines written to lsfix2_sch_0.txt
(True, 2) 29
('fixed', 2) 4
(None, 2) 2


cp temp_sch_0.txt temp_sch_1.txt

Edit temp_sch_1.txt to resolve the None
----------------------------------
python lsfix2.py sch temp_sch_1.txt lsfix2_sch_1.txt

36 lines written to lsfix2_sch_1.txt
(True, 2) 31
('fixed', 2) 4
(None, 2) 1

None item:
pravftta   <ls>Mārk. P. 51,42,b</ls>

--------------------
# generate temp_sch_2.txt from temp_sch_1.txt and the 'fixed' elements

python dict_replace2.py temp_sch_1.txt lsfix2_sch_1.txt temp_sch_2.txt
4 lines to change
-----------------------------------------------------------
# remake xml from temp_sch_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue122fix
cp temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh sch  ../../sch
sh xmlchk_xampp.sh sch
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue122fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py sch temp_sch_2.txt lsfix2_sch_2.txt

2686 lines written to lsfix2_sch_2.txt

(True, 2) 39
(None, 2) 1

(- 39 35)  4 additional standard links

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_sch_0.txt temp_sch_1.txt change_sch_1.txt
2 changes written to change_sch_1.txt

python diff_to_changes_dict.py temp_sch_1.txt temp_sch_2.txt change_sch_2.txt
4 changes written to change_sch_2.txt

