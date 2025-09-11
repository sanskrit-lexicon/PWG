
issue70fix

sch link forms:
<ls>Kathās. ([0-9]+),([0-9]+)

python lsfix2.py sch temp_sch_0.txt lsfix2_sch_0.txt

159 lines written to lsfix2_sch_0.txt
(True, 2) 154
('fixed', 2) 4
(False, 2) 1

The 'False' one: <ls>Kathās. 36,113 ff.</ls>
   Caused by the ' ff.' (not recognized by lsfix2.py)
   Links properly.


# generate temp_sch_2.txt from temp_sch_0.txt and the 'fixed' elements

python dict_replace2.py temp_sch_0.txt lsfix2_sch_0.txt temp_sch_2.txt

4 lines to change
apply_repls: 4 lines changed
8
-----------------------------------------------------------
# remake xml from temp_sch_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue70fix
cp temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh sch  ../../sch
sh xmlchk_xampp.sh sch
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue70fix
-- end of 'remake xml ...'


-------------------------------------------------------------
Create Some documentation files

python lsfix2.py sch temp_sch_2.txt lsfix2_sch_2.txt

(True, 2) 165
(False, 2) 1


(True, 2) 808
(None, 2) 1

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_sch_0.txt temp_sch_1.txt change_sch_1.txt
5 changes written to change_sch_1.txt

python diff_to_changes_dict.py temp_sch_1.txt temp_sch_2.txt change_sch_2.txt
47 changes written to change_sch_2.txt
