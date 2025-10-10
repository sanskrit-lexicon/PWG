
issue135fix

pw link forms:
2 parameters.

457  "RĀJAT."   
  1  "RĀJAT. ed. Calc."   a different edition

python lsfix2.py pw temp_pw_0.txt lsfix2_pw_0.txt
(None,12),(True,413),(fixed,30),(all,455) lsfix2_pw_0.txt


cp temp_pw_0.txt temp_pw_1.txt

Make changes to temp_pw_1 to correct False and None
 
python lsfix2.py pw temp_pw_1.txt lsfix2_pw_1.txt
(None,5),(True,418),(fixed,32),(all,455) lsfix2_pw_1.txt

----------------  The 5 None
BizAyaka	<ls>RĀJAT. 44. 46. 50</ls>	
BizAyakapura	<ls>RĀJAT. 109</ls>	
mahAmArgapati	<ls>RĀJAT. 92</ls>	
ledarI	<ls>RĀJAT. 106</ls>	
sajAni	<ls>RĀJAT. ed. Calc. 1,258</ls>	

--------------------
# generate temp_pw_2.txt from temp_pw_1.txt and the 'fixed' elements
python dict_replace2.py temp_pw_1.txt lsfix2_pw_1.txt temp_pw_2.txt
apply_repls: 32 lines changed

-----------------------------------------------------------
# remake xml from temp_pw_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue135fix
cp temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue135fix
-- end of 'remake xml ...'

---------------------------------------------------
---- lsfix2 file with pw_2

python lsfix2.py pw temp_pw_2.txt lsfix2_pw_2.txt
(None,5),(True,491),(all,496) lsfix2_pw_2.txt

(- 491 413)  78 additional links

---- documentation in change files
python diff_to_changes_dict.py temp_pw_0.txt temp_pw_1.txt change_pw_1.txt
7 changes written to change_pw_1.txt

python diff_to_changes_dict.py temp_pw_1.txt temp_pw_2.txt change_pw_2.txt
32 changes written to change_pw_2.txt

==============================================================
The remaining 5 'None' cases are listed above.
==============================================================
