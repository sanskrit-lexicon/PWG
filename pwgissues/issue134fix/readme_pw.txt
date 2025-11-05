
issue134fix

---------------------------------------------
# TS. corresponds to linktarget
pw TS. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)

Other refs starting with 'TS.' (these excluded in further analysis)
112 matches for "TS. PRĀT."
  3 matches for "TS. <ab>Comm.</ab>"
  
These are excluded in lsfix2 analysis.
python lsfix2.py pw temp_pw_0.txt lsfix2_pw_0.txt
(None,23),(True,510),(fixed,41),(all,574) lsfix2_pw_0.txt

cp temp_pw_0.txt temp_pw_1.txt
# edit changes to temp_pw_1.txt

44677 : tapyatu : TS. (ed. WEBER) 1,4,35,1: TS. 1,4,35,1 : print change

11 matches for "<ls>TS\. [0-9]+,[0-9]+,[0-9]+\.?</ls>"  not linkable with index

python lsfix2.py pw temp_pw_1.txt lsfix2_pw_1.txt
(None,11),(True,520),(fixed,42),(all,573) lsfix2_pw_1.txt


====================================
Problem with images for pw pages 3-257 ... 3-265  (last page in pw.txt)
https://www.sanskrit-lexicon.uni-koeln.de/scans/csl-apidev/servepdf.php?dict=pw&page=3-257
====================================
None info:
28159	aBivAsa	<ls>TS. 1,142,12</ls>	
177668	jyotizya	<ls n="TS.">1,554,8. fgg.</ls>	
365122	mfgArezwi	<ls>TS. 4,7,15</ls>	
424517	vikarza	<ls>TS. 4,6,1-5</ls>	
441340	vizRvatikrama	<ls>TS. 3,5,3</ls>	
508164	sarparAjYI	<ls>TS. 1,5,4</ls>	
508275	sarpAhuti	<ls>TS. 5,5,10</ls>	
544238	stomaBAga	<ls>TS. 4,4,1. fgg.</ls>	
582361	kAmyezwi	<ls n="TS.">2,374</ls>	
583709	dUreheti	<ls n="TS. 1,1008,">12</ls>	
637462	rAzwraBft	<ls>TS. 3,4,7</ls>	

---------------------------
MISC COMMENTS

END MISC COMMENTS

--------------------------------

# generate temp_pw_2.txt from temp_pw_1.txt and the 'fixed' elements

python dict_replace2.py temp_pw_1.txt lsfix2_pw_1.txt temp_pw_2.txt
apply_repls: 41 lines changed

-----------------------------------------------------------
# remake xml from temp_pw_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue134fix
cp temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue134fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pw temp_pw_2.txt lsfix2_pw_2.txt
(None,11),(True,607),(all,618) lsfix2_pw_2.txt

Additional links: (- 607 510) 97
---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pw_0.txt temp_pw_1.txt change_pw_1.txt
19 changes written to change_pw_1.txt

python diff_to_changes_dict.py temp_pw_1.txt temp_pw_2.txt change_pw_2.txt
41 changes written to change_pw_2.txt

===========================================

chkidx compares the kosha references and the link target index.

lsfix3.py is variation of lsfix2.py.  It prepares the input to chkidx.

python lsfix3.py pw temp_pw_2.txt lsfix3_pw_2.txt
(True,607),(all,607) lsfix3_pw_2.txt

( see readme_pwg.txt )

python chkidx.py lsfix3_pw_2.txt index.txt lsfix3_chkidx_pw_2.txt
599 instances find ipage out of 607
8 references NOT FOUND in index
6

