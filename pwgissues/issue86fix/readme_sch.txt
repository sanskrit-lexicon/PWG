issue86fix/readme_sch.txt
09-29-2025 begun ejf
fix sch references to  Pañcatantra, Kosegarten, 1848  

--------------------------------------
forms of reference:
 sch: 
  Pañcat. N,N  : ipage, linenum
  Pañcat. R,N  : tantra, verse  R is roman numeral. I,II,III,IV,V
  Pañcat. Pr. N : prastava N = verse

We use lsfix2_r1.py, with parmfile lsfix2_parm.py
 This version handles both N,N and R,N.
 It is specific to PAÑCAT.

============================================================
# split work for sch
python lsfix2_r1.py sch2 temp_sch_0.txt lsfix2_sch_0_r1.txt
(True,24),(fixed,2),(all,26) lsfix2_sch_0_r1.txt

No changes needed.  2 fixed need to split

----------------------------
# generate temp_sch_2.txt from temp_sch_0.txt and the 'fixed' elements

python dict_replace2.py temp_sch_0.txt lsfix2_sch_0_r1.txt temp_sch_2.txt
apply_repls: 2 lines changed

-----------------------------------------------------------
# remake xml from temp_sch_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue86fix
cp temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh sch  ../../sch
sh xmlchk_xampp.sh sch
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue86fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2_r1.py sch2 temp_sch_2.txt lsfix2_sch_2_r1.txt

(True,28),(all,28) lsfix2_sch_2_r1.txt

(- 28 24) 4 additional standard links

---- documentation in change files
python diff_to_changes_dict.py temp_sch_0.txt temp_sch_2.txt change_sch_2.txt
2 changes written to change_sch_2.txt
