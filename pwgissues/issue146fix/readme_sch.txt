
issue146fix

sch link forms:
<ls>Kumāras. ([0-9]+),([0-9]+)

python lsfix2.py sch temp_sch_0.txt lsfix2_sch_0.txt

41 lines written to lsfix2_sch_0.txt
(True, 2) 36
(None, 2) 4
('fixed', 2) 1


cp temp_sch_0.txt temp_sch_1.txt

Edit temp_sch_1.txt to resolve the None

print changes
20700 : BUtArTa : Kumāras. VII,13 : Kumāras. 7,13 : print change
17708 : padmaka : Kumāras. I,7 : Kumāras. 1,7 : print change

python lsfix2.py sch temp_sch_1.txt lsfix2_sch_1.txt
43 lines written to lsfix2_sch_1.txt
(True, 2) 42
('fixed', 2) 1


--------------------
# generate temp_sch_2.txt from temp_sch_0.txt and the 'fixed' elements

python dict_replace2.py temp_sch_1.txt lsfix2_sch_1.txt temp_sch_2.txt

-----------------------------------------------------------
# remake xml from temp_sch_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue146fix
cp temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh sch  ../../sch
sh xmlchk_xampp.sh sch
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue146fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py sch temp_sch_2.txt lsfix2_sch_2.txt
44 lines written to lsfix2_sch_2.txt
(True, 2) 44

First parm should be 1-7 in our (1838) edition.
But 13 exceptions probably refer to unknown 1868 edition.

9 matches for "<ls>Kumāras. [0-9][0-9]," in buffer: lsfix2_sch_2.txt
1 match for "<ls n="Kumāras.">[0-9][0-9]," in buffer: lsfix2_sch_2.txt
1 match for "<ls n="Kumāras. [0-9][0-9],">" in buffer: lsfix2_sch_2.txt
2 matches for "<ls>Kumāras. [89]," in buffer: lsfix2_sch_2.txt

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_sch_0.txt temp_sch_1.txt change_sch_1.txt
4 changes written to change_sch_1.txt

python diff_to_changes_dict.py temp_sch_1.txt temp_sch_2.txt change_sch_2.txt
1 changes written to change_sch_2.txt

