
issue84fix

pwg link forms:
ŚAT. BR. 4 parms

python lsfix2.py pwg temp_pwg_0.txt lsfix2_pwg_0.txt
(False,35),(None,498),(True,12288),(fixed,2518),(all,15339) lsfix2_pwg_0.txt

cp temp_pwg_0.txt temp_pwg_1.txt
# edit temp_pwg_1.txt for manual changes

python lsfix2.py pwg temp_pwg_1.txt lsfix2_pwg_1.txt
(None,8),(True,12664),(fixed,2702),(all,15374) lsfix2_pwg_1.txt

See readme_pwg_unlinked.txt for 8 references that are unlinked.


---------------------------
MISC COMMENTS
jalpa (1141,7)  ?
aDipati 2,34 :: no link to 14,7,2,34
87302 : vac : ŚAT. BR. 1,5,1,16. fcam 6,2,27. : ŚAT. BR. 1,5,1,16. fcam 6,3,27. : print change
2653 : anila : ŚAT. BR. 14,8,31 : ŚAT. BR. 14,8,3,1 : print change

88288  iqA <ls>ŚAT. BR. 1,8,1.</ls>  ??

203781	gam	<ls n="ŚAT. BR. ">30.</ls>
 https://www.sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpdf/pwg2-0669.pdf
   2nd col, "असतो मा सद्गमय तमसो मा ज्योतिर्गमय"
   Should occur at
     https://sanskrit-lexicon-scans.github.io/shatapathabr/app1/?14,9,1,30
   But 14,9,1,19 is the last verse of 14,9,1

   Phrase Occurs at 14,4,1,30.

21814 : gam : {#asato mA sadgamaya tamaso mA jyotirgamaya#} 30 : ... ŚAT. BR. 14,4,1,30 : print change

   
   Where is this famous quotation in shatapathabr ?

51057 : priyavrata : ŚAT. BR. 4,4,3,5,20 : ŚAT. BR. 4,3,5,20 : print change
87675 : vaD : {#mA no\ hArdi^ tvi\zA va^DIH#} 8,68,8 : ... 8,79,8 : ṚV : print change
98939 : SArIra : {#Atman#} 11,4 : 14,6,11,4 : 14,7,11,4 does not exist : print change 
anAraByavAda   <ls>ŚAT. BR. 809,10</ls>
  The reference is to ipage=809, line-number 10
  "Extracts from the commentary of sAyanAcArya"

lokAloka   <ls>ŚAT. BR. S. 1132.</ls>
https://sanskrit-lexicon-scans.github.io/shatapathabr/pdfpages/shat-1153.pdf
 5th line from bottom. "Extracts ..."

END MISC COMMENTS

--------------------------------

# generate temp_pwg_2.txt from temp_pwg_1.txt and the 'fixed' elements

python dict_replace2.py temp_pwg_1.txt lsfix2_pwg_1.txt temp_pwg_2.txt
apply_repls: 2695 lines changed

-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue84fix
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue84fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pwg temp_pwg_2.txt lsfix2_pwg_2.txt
(None,8),(True,20676),(all,20684) lsfix2_pwg_2.txt

Additional links: (- 20676 12288)  8388 
---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
538 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
2695 changes written to change_pwg_2.txt

===========================================

chkidx compares the kosha references and the link target index.

lsfix3.py is variation of lsfix2.py.  It prepares the input to chkidx.

python lsfix3.py pwg temp_pwg_2.txt lsfix3_pwg_2.txt

example output line:
1215    akna    <ls>ŚAT. BR. 3,2,1,5.</ls>      3,2,1,5


python chkidx.py lsfix3_pwg_2.txt SAT.index_edit.txt lsfix3_chkidx_pwg_2.txt
20439 instances find ipage out of 20676
 (- 20676 20439)  237 references NOT FOUND in index

