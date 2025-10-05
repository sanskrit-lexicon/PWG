
issue109fix

pwg link forms:
2 parameters.
3 reference forms in pwg:
121  "RAGH. ed. Calc."   
 16  "RAGH. (ed. Calc.)" 
  1 "RAGH. (Calc.)"     

cp temp_pwg_0.txt temp_pwg_1.txt

Make changes
 "RAGH. (ed. Calc.)"  -> "RAGH. ed. Calc." and "RAGH. (Calc.)" 
2454 : anasUya : RAGH. (ed. Calc.): RAGH. ed. Calc. : print change
2915 : anumAna : RAGH. (ed. Calc.): RAGH. ed. Calc. : print change
4098 : apAya : RAGH. (ed. Calc.): RAGH. ed. Calc. : print change
4187 : apekzA : RAGH. (ed. Calc.): RAGH. ed. Calc. : print change
7257 : as : RAGH. (ed. Calc.): RAGH. ed. Calc. : print change
7257 : as : RAGH. (ed. Calc.): RAGH. ed. Calc. : print change
7365 : asahya : RAGH. (ed. Calc.): RAGH. ed. Calc. : print change
10503 : Ir : RAGH. (ed. Calc.): RAGH. ed. Calc. : print change
13432 : ekAntara : RAGH. (ed. Calc.): RAGH. ed. Calc. : print change
15071 : kar : RAGH. (Calc.) : RAGH. ed. Calc. : print change
15776 : kalpya : RAGH. (ed. Calc.): RAGH. ed. Calc. : print change
16363 : kAma : RAGH. (ed. Calc.): RAGH. ed. Calc. : print change
19326 : kopa : RAGH. (ed. Calc.): RAGH. ed. Calc. : print change
36705 : DAv : RAGH. (ed. Calc.): RAGH. ed. Calc. : print change
36831 : DU : RAGH. (ed. Calc.): RAGH. ed. Calc. : print change
37924 : nava : RAGH. (ed. Calc.): RAGH. ed. Calc. : print change
37935 : navagraha : RAGH. (ed. Calc.): RAGH. ed. Calc. : print change

Also 3 other minor changes

python lsfix2.py pwg temp_pwg_1.txt lsfix2_pwg_1.txt
(True,136),(fixed,2),(all,138) lsfix2_pwg_1.txt


--------------------
# generate temp_pwg_2.txt from temp_pwg_1.txt and the 'fixed' elements
python dict_replace2.py temp_pwg_1.txt lsfix2_pwg_1.txt temp_pwg_2.txt
apply_repls: 2 lines changed

-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue109fix
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue109fix
-- end of 'remake xml ...'

---------------------------------------------------
---- lsfix2 file with pwg_2

python lsfix2.py pwg temp_pwg_2.txt lsfix2_pwg_2.txt
(True,140),(all,140) lsfix2_pwg_2.txt

4 additional links.

---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
20 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
2 changes written to change_pwg_2.txt

