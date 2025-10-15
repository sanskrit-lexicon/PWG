
issue75fix

pwkvn link forms:

========================================
pwkvna "R. ed. Bomb."  
python lsfix2.py pwkvna temp_pwkvn_0.txt lsfix2_pwkvn_0_a.txt
(None,1),(True,352),(fixed,5),(all,358) lsfix2_pwkvn_0_a.txt

cp temp_pwkvn_0.txt temp_pwkvn_1.txt 

Make changes to temp_pwkvn_1 for the 1 None/
Also, apply the 'fixed' items manually

python lsfix2.py pwkvna temp_pwkvn_1.txt lsfix2_pwkvn_1_a.txt
(True,368),(all,368) lsfix2_pwkvn_1_a.txt

========================================
pwkvnb: "R. ..."  EXCLUDES "R. ed. Bomb." and several other forms
========================================
R. 2,3, or 4 parms.

python lsfix2.py pwkvnb temp_pwkvn_0.txt lsfix2_pwkvn_0_b.txt
(None,4),(True,177),(True,3),(True,5),(all,189) lsfix2_pwkvn_0_b.txt

True (+ 177 3 5) 185

python lsfix2.py pwkvnb temp_pwkvn_1.txt lsfix2_pwkvn_1_b.txt
(None,2),(True,178),(True,3),(True,5),(all,188) lsfix2_pwkvn_1_b.txt

True (+ 178 3 5) 186

The 2 None are
13403	aSvapfzWa	<ls>R. PISCHEL</ls>	
13562	asma	<ls>R. PISCHEL</ls>	

-----------------------------------

# Nothing to  generate temp_pwkvn_2.txt from temp_pwkvn_1.txt and the 'fixed' elements

# python dict_replace2.py temp_pwkvn_1.txt lsfix2_pwkvn_1_b.txt temp_pwkvn_2.txt
# apply_repls: 42 lines changed

-----------------------------------------------------------
# remake xml from temp_pwkvn_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue75fix
cp temp_pwkvn_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwkvn  ../../pwkvn
sh xmlchk_xampp.sh pwkvn
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue75fix
-- end of 'remake xml ...'

---------------------------------------------------

pwkvna:  (- 368 352)  16 additional

pwkvnb:  (- 186 185)  1 additional

Total additional 17

---- documentation in change files
python diff_to_changes_dict.py temp_pwkvn_0.txt temp_pwkvn_1.txt change_pwkvn_1.txt
8 changes written to change_pwkvn_1.txt

