
issue75fix

pw link forms:
2 parameters.

620  "R. ed. Bomb."
168  "R. GORR."
  2  "R. ed. SCHL."
989  "<ls>R\. [0-9]+,"

========================================
pwa "R. ed. Bomb."  
python lsfix2.py pwa temp_pw_0.txt lsfix2_pw_0_a.txt
(None,9),(True,1),(True,560),(fixed,9),(all,579) lsfix2_pw_0_a.txt

cp temp_pw_0.txt temp_pw_1.txt 

Make changes to temp_pw_1 for the 9 None/
Also, apply the 'fixed' items manually
128367 : susaMprahfzwa : R. ed. Bomb. 354,30 : R. ed. Bomb. 3,54,30 : print change

python lsfix2.py pwa temp_pw_1.txt lsfix2_pw_1_a.txt
(None,8),(True,1),(True,588),(all,597) lsfix2_pw_1_a.txt

The 8 unresolved
117549	kUj	<ls>R. ed. Bomb. Śl. 13</ls>	
117549	kUj	<ls n="R. ed. Bomb.">2,96</ls>	
229291	DfzwamAna	<ls>R. ed. Bomb. 43</ls>	
229291	DfzwamAna	<ls n="R. ed. Bomb.">2,95</ls>	
303222	praseka	<ls>R. ed. Bomb. Śl. 2</ls>	
303222	praseka	<ls n="R. ed. Bomb.">2,95</ls>	
63936	mUla	<ls>R. ed. Bomb. I,179,a, Z. 1</ls>	
561992	hArAntara	<ls n="R. ed. Bomb.">2,95</ls>	


========================================
pwb: "R. ..."  EXCLUDES "R. ed. Bomb." and several other forms
========================================
R. 2,3, or 4 parms.

python lsfix2.py pwb temp_pw_0.txt lsfix2_pw_0_b.txt
(None,7),(True,5),(True,6),(True,978),(fixed,43),(all,1039) lsfix2_pw_0_b.txt
True (+ 5 6 978) = 989
209148 : pratyupaveSana : 120,17 GORR. : R. ed. GORR. 2,120,17 : print change


python lsfix2.py pwb temp_pw_1.txt lsfix2_pw_1_b.txt
(None,2),(True,5),(True,6),(True,982),(fixed,43),(all,1038) lsfix2_pw_1_b.txt

The two remaining mention another reference
580985	aSvapfzWa	<ls>R. PISCHEL</ls>	
581146	asma	<ls>R. PISCHEL</ls>	

-----------------------------------

# generate temp_pw_2.txt from temp_pw_1.txt and the 'fixed' elements

python dict_replace2.py temp_pw_1.txt lsfix2_pw_1_b.txt temp_pw_2.txt
apply_repls: 42 lines changed

-----------------------------------------------------------
# remake xml from temp_pw_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue75fix
cp temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue75fix
-- end of 'remake xml ...'

---------------------------------------------------
python lsfix2.py pwa temp_pw_2.txt lsfix2_pw_2_a.txt
(None,8),(True,1),(True,588),(all,597) lsfix2_pw_2_a.txt

True (- 589 561) 28 additional

python lsfix2.py pwb temp_pw_2.txt lsfix2_pw_2_b.txt
(None,2),(True,1082),(True,5),(True,6),(all,1095) lsfix2_pw_2_b.txt

True: (+ 1082 5 6)  1093
(- 1093 989)  104 additional

Total additions (+ 28 104) 132

---- documentation in change files
python diff_to_changes_dict.py temp_pw_0.txt temp_pw_1.txt change_pw_1.txt
15 changes written to change_pw_1.txt

python diff_to_changes_dict.py temp_pw_1.txt temp_pw_2.txt change_pw_2.txt
42 changes written to change_pw_2.txt

