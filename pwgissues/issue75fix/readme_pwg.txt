
issue75fix

pwg link forms:
2 parameters.

332  "R. ed. Bomb." 
474  "R\. 7,[0-9]+,[0-9]+,[0-9]+"
1553 "R\. 7,[0-9]+,[0-9]+[^0-9,]"  (3 parameters)
  2  "R\. 7,[0-9]+[^0-9,]"  (2 parameters)  [basic adjust inserts 1 as param-3]
========================================
pwga "R. ed. Bomb."  
python lsfix2.py pwga temp_pwg_0.txt lsfix2_pwg_0_a.txt
(None,1),(True,320),(True,7),(all,328) lsfix2_pwg_0_a.txt

cp temp_pwg_0.txt temp_pwg_1.txt 

Make changes to temp_pwg_1 for the 1 None/

========================================
pwgb: "R. ..."  EXCLUDES "R. ed. Bomb." and several other forms
========================================
R. 2,3, or 4 parms.
  
python lsfix2.py pwgb temp_pwg_0.txt lsfix2_pwg_0_b.txt
(None,44),(True,135),(True,230),(True,37272),(fixed,2),(all,37683) lsfix2_pwg_0_b.txt
 True (+ 135 230 37272) 37637
------------------------------------
Further changes to temp_pwg_1, including

80595 : maheSa : R. ed. SCHL. I, XXXI. : R. ed. SCHL. 1,31. : maheSa not found! : print change
48502 : pratirAjan : 119,16 GORR. : R. GORR. 2,119,16 : print change


python lsfix2.py pwgb temp_pwg_1.txt lsfix2_pwg_1_b.txt
(None,22),(True,133),(True,233),(True,37290),(all,37678) lsfix2_pwg_1_b.txt

True  (+ 133 233 37290) 37656

(- 37656 37637) 19 additional links.
-----------------------------------------
classification of the 22 None

None	2	69357	AjIva	<ls>R. 2,56,13,a.</ls>
None	2	288015	tAvant	<ls>R. 2,56,13,b.</ls>	
None	2	559272	manojYa	<ls n="R.">2,56,13,a.</ls>	
Link: https://sanskrit-lexicon-scans.github.io/ramayanaschl/?2,56,13
 basicadjust ignores the ',a' and ',b'
 
1 parameter  references to kandas
None	2	329257	durvAsas	<ls>R. 7</ls>	
None	2	343911	dvAtriMSa	<ls>R. 3</ls>	
None	2	344081	dvAdaSaSata	<ls>R. 6</ls>	
None	2	344238	dvApaYcASa	<ls>R. 4</ls>	
None	2	344642	dvAviMSatitama	<ls>R. 3.</ls>	
None	2	344642	dvAviMSatitama	<ls n="R.">4</ls>	
None	2	344671	dvAzazwitama	<ls>R. 4</ls>	
None	2	345640	dvipaYcASa	<ls>R. 3</ls>	
None	2	370934	navacatvAriMSa	<ls>R. 6</ls>	
None	2	371025	navatriMSa	<ls>R. 6</ls>	
None	2	371127	navanavati	<ls>R. 6</ls>	
None	2	371159	navapaYcASa	<ls>R. 6</ls>	
None	2	371356	navaviMSa	<ls>R. 6</ls>	
None	2	371384	navaSata	<ls>R. 6</ls>	
None	2	371410	navazazwi	<ls>R. 6</ls>	
None	2	371420	navasaptati	<ls>R. 6</ls>	
None	2	371506	navASIti	<ls>R. 6</ls>	

-----
  Not sure how these resolve
None	2	393283	nI	<ls>R. III, S. 465.</ls>	
None	2	404093	paYcaviMSaka	<ls>R. III, S. 469.</ls>	


-----------------------------------------

# NO need generate temp_pwg_2.txt from temp_pwg_1.txt and the 'fixed' elements
# Change the original 2 fixed cases in temp_pwg_1.txt
##python dict_replace2.py temp_pwg_1.txt lsfix2_pwg_1.txt temp_pwg_2.txt


-----------------------------------------------------------
# remake xml from temp_pwg_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue75fix
cp temp_pwg_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue75fix
-- end of 'remake xml ...'

---------------------------------------------------


---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
30 changes written to change_pwg_1.txt
