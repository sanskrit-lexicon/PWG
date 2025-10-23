
issue101fix

pw link forms:
 1 or 2 parameters

  "SĀH. D."
  

python lsfix2.py pw temp_pw_0.txt lsfix2_pw_0.txt
(False,3),(None,2),(True,117),(True,64),(fixed,4),(fixed,4),(all,194) lsfix2_pw_0.txt

Total True: (+ 117 65) = 182

cp temp_pw_0.txt temp_pw_1.txt

Make changes to temp_pw_1 and 2 to correct False and None

13529 : asaMkO : asaMkO SĀH. D. 49, ult. fg. : asakO SĀH. D. 49,21. fg. : print change


python lsfix2.py pw temp_pw_1.txt lsfix2_pw_1.txt
(None,1),(True,119),(True,67),(fixed,4),(fixed,6),(all,197) lsfix2_pw_1.txt

The None item:
tulyalakzman	<ls>SĀH. D. (1828) 360,7</ls>

--------------------
# generate temp_pw_2.txt from temp_pw_1.txt and the 'fixed' elements
python dict_replace2.py temp_pw_1.txt lsfix2_pw_1.txt temp_pw_2.txt

apply_repls: 10 lines changed

-----------------------------------------------------------
# remake xml from temp_pw_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue101fix
cp temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue101fix
-- end of 'remake xml ...'

---------------------------------------------------
---- lsfix2 file with pw_2

python lsfix2.py pw temp_pw_2.txt lsfix2_pw_2.txt
(None,1),(True,131),(True,75),(all,207) lsfix2_pw_2.txt

Total True: (+ 131 75) 206

(- 206 182) 24  additional links

---- documentation in change files
python diff_to_changes_dict.py temp_pw_0.txt temp_pw_1.txt change_pw_1.txt
5 changes written to change_pw_1.txt

python diff_to_changes_dict.py temp_pw_1.txt temp_pw_2.txt change_pw_2.txt
10 changes written to change_pw_2.txt

==============================================================
THE END
