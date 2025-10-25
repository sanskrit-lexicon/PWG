
issue125fix

sch link forms:
Śāk.  1 parm or 2 parms
<ls>Śāk. ([0-9]+),([0-9]+)  ipage,line-number
<ls>Śāk. ([0-9]+)           verse
-----

sch0  includes other editions and spellings

python lsfix2.py sch0 temp_sch_0.txt lsfix2_sch_0_0.txt
(None,8),(True,1),(True,7),(fixed,1),(all,17) lsfix2_sch_0_0.txt

True: (+ 1 7) 8

sch option excludes other references to ŚĀKUNTALA
These are NOT LINKED
 3 matches for "Śāk. Ch."
 1 match for "Śāk. (Kāśm.)"
 2 matches for "Śāk. (Ch.)"

 (+ 3 1 2) 6
 Also, see 'additional other references' below
 There are 2 additional 'None'
 
 
python lsfix2.py sch temp_sch_0.txt lsfix2_sch_0.txt
(None,2),(True,1),(True,7),(fixed,1),(all,11) lsfix2_sch_0.txt

True:   (+ 1 7) 8

cp temp_sch_0.txt temp_sch_1.txt

Edit temp_sch_1.txt; examine 'fixed'  - 1 change.

python lsfix2.py sch temp_sch_1.txt lsfix2_sch_1.txt
(None,8),(True,4),(True,7),(all,19) lsfix2_sch_1.txt
 

Correct the None.
Also additional other references. Not linked
 3 Śāk. ed. Pischel
 4 Śāk. (Pischel)

This accounts for 7 of the 8 'None'.
The other None is ok, despite being flagged by lsfix2.

True is now (+ 1 4 7) 12
4 additional links

--------------------
# generate temp_sch_2.txt from temp_sch_0.txt and the 'fixed' elements
# no 'fixed' elements remain
# python dict_replace2.py temp_sch_1.txt lsfix2_sch_1.txt temp_sch_2.txt
# apply_repls: 9 lines changed

-----------------------------------------------------------
# remake xml from temp_sch_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue125fix
cp temp_sch_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh sch  ../../sch
sh xmlchk_xampp.sh sch
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue125fix
-- end of 'remake xml ...'


---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_sch_0.txt temp_sch_1.txt change_sch_1.txt
8 changes written to change_sch_1.txt


