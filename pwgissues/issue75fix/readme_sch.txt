
issue75fix

========================================
scha "R. ed. Bomb."  
python lsfix2.py scha temp_sch_0.txt lsfix2_sch_0_a.txt
(False,2),(None,8),(True,1),(True,317),(fixed,7),(all,335) lsfix2_sch_0_a.txt

True (+ 1 317) 318
cp temp_sch_0.txt temp_sch_1.txt 

Make changes to temp_sch_1 for the 1 None/
Also, apply the 'fixed' items manually

11088 : kUrca : R. ed. Bomb. II,91,77 : R. ed. Bomb. 2,91,77 : print change


python lsfix2.py scha temp_sch_1.txt lsfix2_sch_1_a.txt
(True,1),(True,356),(all,357) lsfix2_sch_1_a.txt

True: (+ 1 356) 357

scha Additional links: (- 357 318) 39


========================================
schb: "R. ..."  EXCLUDES "R. ed. Bomb." and several other forms
========================================
R. 2,3, or 4 parms.

python lsfix2.py schb temp_sch_0.txt lsfix2_sch_0_b.txt
(None,22),(True,1),(True,145),(all,168) lsfix2_sch_0_b.txt
True (+ 1 145) 146

Global change in temp_sch_1.txt:
 ';</ls>' -> '</ls>;'   41
 
python lsfix2.py schb temp_sch_1.txt lsfix2_sch_1_b.txt
(True,1),(True,175),(all,176) lsfix2_sch_1_b.txt

True (+ 1 175) = 176


----------------------------------

# Nothing to  generate temp_sch_2.txt from temp_sch_1.txt and the 'fixed' elements

# python dict_replace2.py temp_sch_1.txt lsfix2_sch_1_b.txt temp_sch_2.txt

-----------------------------------------------------------
# remake xml from temp_sch_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue75fix
cp temp_sch_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh sch  ../../sch
sh xmlchk_xampp.sh sch
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue75fix
-- end of 'remake xml ...'

---------------------------------------------------

scha:  (- 357 318)  39 additional

schb:  (- 176 146)  30 additional

Total additional (+ 39 30) 69  additional

---- documentation in change files
python diff_to_changes_dict.py temp_sch_0.txt temp_sch_1.txt change_sch_1.txt
8 changes written to change_sch_1.txt

