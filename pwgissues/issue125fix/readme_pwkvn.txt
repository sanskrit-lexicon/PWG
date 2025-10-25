
issue125fix

pwkvn link forms:
ŚĀK.  1 parm or 2 parms
<ls>ŚĀK. ([0-9]+),([0-9]+)  ipage,line-number
<ls>ŚĀK. ([0-9]+)           verse
-----

pwkvn0  includes other editions and spellings

python lsfix2.py pwkvn0 temp_pwkvn_0.txt lsfix2_pwkvn_0_0.txt
(None,11),(True,4),(True,8),(all,23) lsfix2_pwkvn_0_0.txt

True: (+ 4 8) 12

pwkvn option excludes other references to ŚĀKUNTALA
These are NOT LINKED
 2 matches for "ŚĀK. ed. PISCH."
 3 matches for "ŚĀK. CH."
 3 matches for "ŚĀK. (PISCH.)"
 1 match for "ŚĀK. (Kāśm.)"
 2 matches for "ŚĀK. (CH.)"
 (+ 2 3 3 1 2) = 11  (All None)
 
python lsfix2.py pwkvn temp_pwkvn_0.txt lsfix2_pwkvn_0.txt
(True,4),(True,8),(all,12) lsfix2_pwkvn_0.txt

True:   (+ 4 8) = 12 

No changes to pwkvn
