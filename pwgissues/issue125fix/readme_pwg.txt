
issue125fix

pwg link forms:
ŚĀK.  1 parm or 2 parms
<ls>ŚĀK. ([0-9]+),([0-9]+)  ipage,line-number
<ls>ŚĀK. ([0-9]+)           verse
-----
Another target:
ŚĀK. CH. N,N   CHEZY'S Ausgabe des ŚĀKUNTALA (GILD. Bibl. 187).
ŚĀK. BÖHTL. N,N  BÖHTL. edition  may be same as

pwg0  includes other editions and spellings

python lsfix2.py pwg0 temp_pwg_0.txt lsfix2_pwg_0_0.txt
(False,120),(None,311),(True,2436),(True,2469),(fixed,152),(fixed,277),(all,5765) lsfix2_pwg_0_0.txt


pwg option excludes other references to ŚĀKUNTALA
These are NOT LINKED
269 matches for "ŚĀK. CH."  (a few more with variant spellings)
  2 matches for "ŚĀK. ed. CH."   
  3 matches for "ŚĀK. BÖHTL."
  1 match for "ŚĀK. ed. BÖHTL."
  1 match for "ŚĀK. (ed. WILL.)"
  1 match for "ŚĀK. (ed. MON. WILL.)"
  1 match for "ŚĀK. ed. PREM."
  
python lsfix2.py pwg temp_pwg_0.txt lsfix2_pwg_0.txt

(False,120),(None,33),(True,2436),(True,2469),(fixed,152),(fixed,277),(all,5487) lsfix2_pwg_0.txt

True:   (+ 2436 2469) 4905

pwgCH : Splitting for "ŚĀK. CH."
python lsfix2.py pwgCH temp_pwg_0.txt lsfix2_pwg_0_CH.txt
(True,254),(True,3),(fixed,10),(all,267) lsfix2_pwg_0_CH.txt

# construct temp_pwg_1.txt by apply 'fixed' in lsfix2_pwg_0_CH.txt
python dict_replace2.py temp_pwg_0.txt lsfix2_pwg_0_CH.txt temp_pwg_1.txt

Edit temp_pwg_1.txt to resolve the None and False

Questions:
utsuka 62. 98,14. ad 62.   Why 62 repeated?
utsuka : <ls>ŚĀK. 80,8. ad 135.</ls>  utsuka not found at verse 135
kad : <ls>ŚĀK. 82,10. ad. 191.</ls> kad not found at verse 191
praveSaka : <ls>ŚĀK. XI. fgg.</ls>
pA : <ls n="ŚĀK.">2,488,21.</ls>
laB : <ls>ŚĀK. 59,15. 85,7. ad 54.</ls>
vizkamBa : <ls>ŚĀK. XII. fg.</ls>
vfTA	<ls>ŚĀK. 72,10. 172. ad 54.</ls>
satkAra	<ls n="ŚĀK.">97,10. ad 160.</ls>  verse 160 has satkriya (the ref?)
iti	<ls>ŚĀK. 3,9. 10</ls>   can't find iti at 3,9 or 3,10

10418 : izwa : ŚĀK. 64,16. 16,28. : ?  16,28 is wrong (no line 28)

</ls> <ls n="ŚĀK.">

python lsfix2.py pwg temp_pwg_1.txt lsfix2_pwg_1.txt
(None,4),(True,2613),(True,2620),(fixed,188),(fixed,252),(all,5677) lsfix2_pwg_1.txt

--------------------
# generate temp_pwg_2.txt from temp_pwg_0.txt and the 'fixed' elements

python dict_replace2.py temp_pwg_1.txt lsfix2_pwg_1.txt temp_pwg_2.txt
apply_repls: 428 lines changed


-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue125fix
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue125fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pwg temp_pwg_2.txt lsfix2_pwg_2.txt
(None,4),(True,3042),(True,3530),(all,6576) lsfix2_pwg_2.txt

True: (+ 3042 3530)  6572

Additional lins: (- 6572 4905)  1667
---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
223 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
428 changes written to change_pwg_2.txt

