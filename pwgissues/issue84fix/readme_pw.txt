
issue84fix

pw link forms:
ŚAT. BR. 4 parms

python lsfix2.py pw temp_pw_0.txt lsfix2_pw_0.txt
(None,33),(True,917),(fixed,162),(all,1112) lsfix2_pw_0.txt


cp temp_pw_0.txt temp_pw_1.txt
# edit temp_pw_1.txt for manual changes

python lsfix2.py pw temp_pw_1.txt lsfix2_pw_1.txt
(None,19),(True,935),(fixed,163),(all,1117) lsfix2_pw_1.txt

None  cases:
17 matches for "<ls>ŚAT. BR. 14</ls>"
prAcInAvavItin	<ls>ŚAT. BR. (KĀṆVA-Rec.) 2,4,2,2. 9</ls>	
mEtreyIbrAhmaRa	<ls>ŚAT. BR. 14,5. fgg.</ls>	


--------------------
# generate temp_pw_2.txt from temp_pw_1.txt and the 'fixed' elements

python dict_replace2.py temp_pw_1.txt lsfix2_pw_1.txt temp_pw_2.txt
apply_repls: 160 lines changed

-----------------------------------------------------------
# remake xml from temp_pw_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue84fix
cp temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue84fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pw temp_pw_2.txt lsfix2_pw_2.txt
(None,19),(True,1331),(all,1350) lsfix2_pw_2.txt

Additional links: (- 1331 917)  414 additional links

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pw_0.txt temp_pw_1.txt change_pw_1.txt
17 changes written to change_pw_1.txt

python diff_to_changes_dict.py temp_pw_1.txt temp_pw_2.txt change_pw_2.txt
160 changes written to change_pw_2.txt

===========================================
 Find some invalid references

python lsfix3.py pw temp_pw_2.txt lsfix3_pw_2.txt
(True,1331),(all,1331) lsfix3_pw_2.txt

example output line:
1917    agnikarman      <ls n="ŚAT. BR. 7,">4,1,42.</ls>        7,4,1,42


python chkidx.py lsfix3_pw_2.txt SAT.index_edit.txt lsfix3_chkidx_pw_2.txt
1302 instances find ipage out of 1331
 (- 1331 1302) 29 inconstent refs
Example of index-consistent reference:  248 = ipage
248     360     akarRa  <ls>ŚAT. BR. 3,3,1,16</ls>      3,3,1,16
Example of index-INCONSISTENT reference
None    3842    aNgArAvakzayaRa <ls>ŚAT. BR. 14,9,6,19</ls>     14,9,6,19

