
issue101fix

sch link forms:
 1 or 2 parameters

  "SĀH. D."
  
</ls> <ls n="SĀH. D.">

python lsfix2.py sch temp_sch_0.txt lsfix2_sch_0.txt
(None,2),(True,15),(True,20),(all,37) lsfix2_sch_0.txt

Total True: (+ 15 20) = 37

cp temp_sch_0.txt temp_sch_1.txt

Make changes to temp_sch_1 and 2 to correct None

6080 : asakO : Sāh. D. 49, ult. f. : SĀH. D. 49,21. f. : print change

python lsfix2.py sch temp_sch_1.txt lsfix2_sch_1.txt
(None,1),(True,15),(True,22),(all,38) lsfix2_sch_1.txt

True (+ 15 22) 37

The None item:
  asakO	<ls>Sāh. D. 49,21. f.</ls>  Actually ok, Called None because of
  'f.' instead of PW 'fg.'


--------------------
# no 'fixed' elements
# generate temp_sch_2.txt from temp_sch_1.txt and the 'fixed' elements
# python dict_replace2.py temp_sch_1.txt lsfix2_sch_1.txt temp_sch_2.txt

-----------------------------------------------------------
# remake xml from temp_sch_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue101fix
cp temp_sch_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh sch  ../../sch
sh xmlchk_xampp.sh sch
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue101fix
-- end of 'remake xml ...'

---------------------------------------------------

---- documentation in change files
python diff_to_changes_dict.py temp_sch_0.txt temp_sch_1.txt change_sch_1.txt
2 changes written to change_sch_1.txt

==============================================================
THE END
