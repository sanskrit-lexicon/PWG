
issue101fix

pwkvn link forms:
 1 or 2 parameters

  "SĀH. D."
  
</ls> <ls n="SĀH. D.">

python lsfix2.py pwkvn temp_pwkvn_0.txt lsfix2_pwkvn_0.txt
(None,1),(True,14),(True,23),(all,38) lsfix2_pwkvn_0.txt

Total True: (+ 14 23) = 37

cp temp_pwkvn_0.txt temp_pwkvn_1.txt

Make changes to temp_pwkvn_1 and 2 to correct None

13529 : asakO : SĀH. D. 49, ult. fg. : SĀH. D. 49,21. fg. : print change

python lsfix2.py pwkvn temp_pwkvn_1.txt lsfix2_pwkvn_1.txt
(True,14),(True,24),(all,38) lsfix2_pwkvn_1.txt
True  (+ 14 24) 38

--------------------
# no 'fixed' elements
# generate temp_pwkvn_2.txt from temp_pwkvn_1.txt and the 'fixed' elements
# python dict_replace2.py temp_pwkvn_1.txt lsfix2_pwkvn_1.txt temp_pwkvn_2.txt

-----------------------------------------------------------
# remake xml from temp_pwkvn_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue101fix
cp temp_pwkvn_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwkvn  ../../pwkvn
sh xmlchk_xampp.sh pwkvn
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue101fix
-- end of 'remake xml ...'

---------------------------------------------------

---- documentation in change files
python diff_to_changes_dict.py temp_pwkvn_0.txt temp_pwkvn_1.txt change_pwkvn_1.txt
2 changes written to change_pwkvn_1.txt

==============================================================
THE END
