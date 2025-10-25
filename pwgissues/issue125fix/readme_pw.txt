
issue125fix

pw link forms:
ŚĀK.  1 parm or 2 parms
<ls>ŚĀK. ([0-9]+),([0-9]+)  ipage,line-number
<ls>ŚĀK. ([0-9]+)           verse
-----

pw0  includes other editions and spellings

python lsfix2.py pw0 temp_pw_0.txt lsfix2_pw_0_0.txt
(None,38),(True,57),(True,80),(fixed,3),(fixed,7),(all,185) lsfix2_pw_0_0.txt

True: (+ 57 80) = 137

pw option excludes other references to ŚĀKUNTALA
These are NOT LINKED
  4 matches for "ŚĀK. zu BĀDAR."
  4 matches for "ŚĀK. ed. PISCH."
  1 match for "ŚĀK. ed. PREMAC."
 12 matches for "ŚĀK. (PISCH.)"
  9 matches for "ŚĀK. CH."
  3 matches for "ŚĀK. PISCH."
  4 matches for "ŚĀK. (CH.)"
  1 match for "ŚĀK. (Kāśm.)"

 (+ 4 4 1 12 9 3 4 1) = 38 other references. Not linked.
 

python lsfix2.py pw temp_pw_0.txt lsfix2_pw_0.txt
(True,57),(True,80),(fixed,3),(fixed,7),(all,147) lsfix2_pw_0.txt

True:   (+ 57 80) 137

cp temp_pw_0.txt temp_pw_1.txt
Edit temp_pw_1.txt; examine 'fixed'  - 1 change.

python lsfix2.py pw temp_pw_1.txt lsfix2_pw_1.txt
(True,58),(True,80),(fixed,2),(fixed,7),(all,147) lsfix2_pw_1.txt

--------------------
# generate temp_pw_2.txt from temp_pw_0.txt and the 'fixed' elements

python dict_replace2.py temp_pw_1.txt lsfix2_pw_1.txt temp_pw_2.txt
apply_repls: 9 lines changed

-----------------------------------------------------------
# remake xml from temp_pw_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue125fix
cp temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue125fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pw temp_pw_2.txt lsfix2_pw_2.txt
(True,76),(True,84),(all,160) lsfix2_pw_2.txt

True: (+ 76 84) 160

Additional links: (- 160 137 ) 23
---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pw_0.txt temp_pw_1.txt change_pw_1.txt
1 changes written to change_pw_1.txt

python diff_to_changes_dict.py temp_pw_1.txt temp_pw_2.txt change_pw_2.txt
9 changes written to change_pw_2.txt

