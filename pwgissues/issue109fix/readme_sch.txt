
issue109fix

sch link forms:
2 parameters.
4 references of form Ragh. ed. Calc. N,N
  
5 references of form Raghuv. N,N

------
Ragh. ed. Calc.
python lsfix2.py sch temp_sch_0.txt lsfix2_sch_0.txt
(None,1),(True,3),(all,4) lsfix2_sch_0_a.txt

No changes here

---------------------
Also Raghuv. N,N

python lsfix2.py scha temp_sch_0.txt lsfix2_sch_0_a.txt
(None,1),(True,3),(all,4) lsfix2_sch_0_a.txt

cp temp_sch_0.txt temp_sch_1.txt

Edit temp_sch_1.txt to correct the 'None'

309 : akzowa : Raghuv. IV,69. : Ragh. 4,69. : print change

--------------------
# generate temp_sch_2.txt from temp_sch_1.txt and the 'fixed' elements
# Nothing to fix by splitting
# python dict_replace2.py temp_sch_1.txt lsfix2_sch_1.txt temp_sch_2.txt

-----------------------------------------------------------

# Add 'Ragh. ed. Calc." and "Raghuv." to schauth/tooltip.txt in csl-pywork

# Revise basicadjust.php in csl-websanlexicon (and csl-apidev) for "Raghuv."
# remake xml from temp_sch_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue109fix
cp temp_sch_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh sch  ../../sch
sh xmlchk_xampp.sh sch
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue109fix
-- end of 'remake xml ...'

---------------------------------------------------
---- lsfix2 file with sch_1

python lsfix2.py sch temp_sch_1.txt lsfix2_sch_1.txt
(True,2),(all,2) lsfix2_sch_1.txt

python lsfix2.py scha temp_sch_1.txt lsfix2_sch_1_a.txt
2 changes written to change_sch_1.txt


---- documentation in change files
python diff_to_changes_dict.py temp_sch_0.txt temp_sch_1.txt change_sch_1.txt
2 changes written to change_sch_1.txt

# python diff_to_changes_dict.py temp_sch_1.txt temp_sch_2.txt change_sch_2.txt
# 

