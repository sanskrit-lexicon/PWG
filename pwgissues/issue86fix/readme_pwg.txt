issue86fix/readme_pwg.txt
09-29-2025 begun ejf
fix pwg references to  Pañcatantra, Kosegarten, 1848  


--------------------------------------
forms of reference:
 pwg: 
  PAÑCAT. N,N  : ipage, linenum
  PAÑCAT. R,N  : tantra, verse  R is roman numeral. I,II,III,IV,V
  Pañcat. Pr. N : prastava N = verse


We use lsfix2_r1.py, with parmfile lsfix2_parm.py
 This version handles both N,N and R,N.
 It is specific to PAÑCAT.


============================================================
# split work for pwg
python lsfix2_r1.py pwg2 temp_pwg_0.txt lsfix2_pwg2_0_r1.txt
(False,101),(None,120),(True,7757),(fixed,545),(all,8523) lsfix2_pwg2_0_r1.txt

cp temp_pwg_0.txt temp_pwg_1.txt

Resolve some of the None and False  by edits to temp_pwg_1.txt

471 matches in 466 lines for "ed\. orn\." in buffer: temp_pwg_2.txt
 two main forms:
 PAÑCAT. ed. orn. ...
 ed. orn ...
These 'ed. orn.' do NOT generate links
------------------------------------------------
AFter revisions to temp_pwg_1.txt:

python lsfix2_r1.py pwg2 temp_pwg_1.txt lsfix2_pwg_1_r1.txt
(None,10),(True,7860),(fixed,583),(all,8453) lsfix2_pwg_1_r1.txt

----------------------------
# generate temp_pwg_2.txt from temp_pwg_1.txt and the 'fixed' elements

python dict_replace2.py temp_pwg_1.txt lsfix2_pwg_1_r1.txt temp_pwg_2.txt
apply_repls: 583 lines changed

-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue86fix
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue86fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2_r1.py pwg2 temp_pwg_2.txt lsfix2_pwg_2_r1.txt

(None,10),(True,9422),(all,9432) lsfix2_pwg_2_r1.txt

(- 9422 7757) 1665 additional standard links.
    but about (ed. orn. and ed. Bomb.)
    so (- 1665 500) = 1165 active links to link target

---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
314 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
583 changes written to change_pwg_2.txt
