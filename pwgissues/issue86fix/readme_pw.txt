issue86fix/readme_pw.txt
09-29-2025 begun ejf
fix pw references to  Pañcatantra, Kosegarten, 1848  

--------------------------------------
forms of reference:
 pw: 
  PAÑCAT. N,N  : ipage, linenum
  PAÑCAT. R,N  : tantra, verse  R is roman numeral. I,II,III,IV,V
  Pañcat. Pr. N : prastava N = verse

We use lsfix2_r1.py, with parmfile lsfix2_parm.py
 This version handles both N,N and R,N.
 It is specific to PAÑCAT.

============================================================
# split work for pw
python lsfix2_r1.py pw2 temp_pw_0.txt lsfix2_pw2_0_r1.txt
(None,6),(True,319),(fixed,17),(all,342) lsfix2_pw2_0_r1.txt


cp temp_pw_0.txt temp_pw_1.txt

Resolve the None and False  by edits to temp_pw_1.txt

133572 : har : PAÑCAT. ed. KOSEG. : PAÑCAT. :  print change
91092 : yuj : PAÑCAT. ed. KOSEG. : PAÑCAT. :  print change
78974 : Barts :  PAÑCAT. ed. KOSEG. : PAÑCAT. :  print change

------------------------------------------------
AFter revisions to temp_pw_1.txt:

python lsfix2_r1.py pw2 temp_pw_1.txt lsfix2_pw_1_r1.txt
(True,322),(fixed,19),(all,341) lsfix2_pw_1_r1.txt

----------------------------
# generate temp_pw_2.txt from temp_pw_1.txt and the 'fixed' elements

python dict_replace2.py temp_pw_1.txt lsfix2_pw_1_r1.txt temp_pw_2.txt
apply_repls: 19 lines changed

-----------------------------------------------------------
# remake xml from temp_pw_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue86fix
cp temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue86fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2_r1.py pw2 temp_pw_2.txt lsfix2_pw_2_r1.txt

(True,371),(all,371) lsfix2_pw_2_r1.txt

(- 371 319) 52 additional standard links

---- documentation in change files
python diff_to_changes_dict.py temp_pw_0.txt temp_pw_1.txt change_pw_1.txt
6 changes written to change_pw_1.txt

python diff_to_changes_dict.py temp_pw_1.txt temp_pw_2.txt change_pw_2.txt
19 changes written to change_pw_2.txt
