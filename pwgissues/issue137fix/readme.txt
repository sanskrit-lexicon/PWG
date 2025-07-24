issuexxx/readme.txt
07-20-2025 begun ejf

Ref: https://github.com/sanskrit-lexicon/PWG/issues/xxx

This issue137 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issuexxx

-----------------
# get temporary local copy of pwg
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt

----------------------------------------

ratra, adhy, verse

pwg: PAÑCAR. N,N,N  OR PAÑCAR. S. N  (page)

python lsfix.py pancar temp_pwg_0.txt lsfix_0.txt

changes with 21 None
cp temp_pwg_0.txt temp_pwg_1.txt
manual changes to temp_pwg_1.txt for these 21. Changes are typos except for
107197 : sarveSa : PAÑCAR. 1,1,1,5. : PAÑCAR. 1,1,5.  : print chg pwg

TODO anomaly: <ls>PAÑCAR. 1,7,58,d.</ls>  under 'mA'
 changed to <ls>PAÑCAR. 1,7,58</ls>,d.

python lsfix.py pancar temp_pwg_1.txt lsfix_1.txt 
Now only 5 'None'
5 matches for "None" in buffer: lsfix_all1.txt
   1083:None	<ls n="PAÑCAR.">S. 238.</ls>	
   1084:None	<ls n="PAÑCAR. S.">278.</ls>	
   1297:None	<ls>PAÑCAR. S. 245.</ls>	
   1668:None	<ls n="PAÑCAR.">S. 249</ls>	
   1669:None	<ls>PAÑCAR. S. 280. fg.</ls>	

7 matches for "False" in buffer: lsfix_all1.txt
    317:False	<ls>PAÑCAR. 4,3,81. <is>Śiva</is></ls>	<ls>PAÑCAR. 4,3,81.</ls>
    321:False	<ls>PAÑCAR. 4,3,25. <is>Śiva's</is></ls>	<ls>PAÑCAR. 4,3,25.</ls>
    959:False	<ls>PAÑCAR. 4,3,53 (<is>Viṣṇu</is>). 6,17.</ls>	<ls>PAÑCAR. 4,3,53</ls>
   1120:False	<ls>PAÑCAR. 4,8,43. <is>Śiva's</is></ls>	<ls>PAÑCAR. 4,8,43.</ls>
   1246:False	<ls>PAÑCAR. 1,5,30. fg. 2,2,85. 4,3,36 (S. 249). 8,38.</ls>	<ls>PAÑCAR. 1,5,30. fg.</ls> <ls n="PAÑCAR.">2,2,85.</ls> <ls n="PAÑCAR.">4,3,36</ls>
   1964:False	<ls>PAÑCAR. 2,4,46 (?).</ls>	<ls>PAÑCAR. 2,4,46</ls>
   2188:False	<ls>PAÑCAR. 4,3,117. n.</ls>	<ls>PAÑCAR. 4,3,117.</ls>

Make changes to temp_pwg_1.txt for these, then rerun lsfix

python lsfix.py pancar temp_pwg_1.txt lsfix_1.txt
2282 lines written to lsfix_1.txt 

-------------------------------------------------------------
apply corrections to the 'fixed' items
python dict_replace.py temp_pwg_1.txt lsfix_1.txt temp_pwg_2.txt


---- remake xml from temp_pwg_2.txt and check
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issuexxx

---- make change files for possible future reference
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
23 changes

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
300 changes

--------------------------------------------
# check for invalid links for pancar
(pancar work in issue137)

python ../issue137/generate_random.py ALL pwg3 temp_pwg_2.txt ../issue137/index.txt temp_check_all_2.txt temp_check_all_2_nopagerec.txt

write_examples: 2104 written to temp_check_all_2.txt
0 instances of 'pagerec not found'

=============================================================
sync to github:
csl-orig 
csl-corrections
 107197 : sarveSa : PAÑCAR. 1,1,1,5. : PAÑCAR. 1,1,5.  : print chg pwg
# this issue
sync to Cologne, and redo the pwg displays

-------------------------------------------------------------
------------------------------------------------------------
THE END
