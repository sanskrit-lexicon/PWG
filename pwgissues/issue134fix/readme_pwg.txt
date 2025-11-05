
issue134fix

cp temp_pwg_0.txt temp_pwg_1.txt

---------------------------------------------
# TS. corresponds to linktarget
pwg TS. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)

Other refs starting with 'TS.' (these excluded in further analysis)
589 matches for "TS. PRĀT."
 35 matches for "TS. Comm."
  2 matches for "TS. ANUKR."

python lsfix2.py pwg temp_pwg_0.txt lsfix2_pwg_0.txt
(False,17),(None,244),(True,4514),(fixed,512),(all,5287) lsfix2_pwg_0.txt

cp temp_pwg_0.txt temp_pwg_1.txt
# edit changes to temp_pwg_1.txt

python lsfix2.py pwg temp_pwg_1.txt lsfix2_pwg_1.txt
(None,58),(True,4644),(fixed,556),(all,5258) lsfix2_pwg_1.txt


None info:

---------------------------
MISC COMMENTS
These 10  likely refer to a commentary
625931	aSanihata	<ls>TS. 1,785,12.</ls>	
653330	karRa	<ls>TS. 1,427,5.</ls>	
661357	kumba	<ls>TS. 1,538,12.</ls>	
950504	zaRRavati	<ls>TS. 7,2,15.</ls>	
952218	saMyoga	<ls>TS. 2,109,5.</ls>	
963919	saYj	<ls>TS. 2,109,6.</ls>	
985424	saMpAdana	<ls>TS. 1,914,4.</ls>	
1005253	sAtyadUta	<ls>TS. 2,194,11.</ls>	
1070066	svagA	<ls>TS. 1,233,20.</ls>	
1100240	homa	<ls>TS. 1,538,10.</ls>	
These 9 likely refer to commentary
632556	Ara	<ls>TS. 1,394.</ls>	
697853	DizRya	<ls>TS. 1,227,16</ls>	
985031	saMpad	<ls>TS. 1,914.</ls>	
991754	sarj	<ls>TS. 2,296</ls>	
1104703	apagoraRa	<ls>TS. 2,796.</ls>	
1108296	uddrAva	<ls>TS. 2,254, Anm.</ls>	
1108767	upastaraRa	<ls>TS. 1,898. 2,719.</ls>	
1119588	pratiSaraRa	<ls>TS. 2,738.</ls>	
1119928	pravarta	<ls>TS. 2,453. fg.</ls>	
-
427160	palAyana	<ls>TS. 880,7. 10.</ls>
END MISC COMMENTS

41963 : patman :  8,6,3. 8,23. : 8,8,23. : cf. 120717 patman : print change
13402 : ekahAyana : {#eka^hAyanA  ... vadanti#} 6 : {#eka^hAyanA  ... vadanti#} 7 : print change
54342 : Bavya : TS. 3,12,8,3 : TBR. 3,12,8,3 : print change
17726 : kunaKin : TS. 2,5,17. : TS. 2,5,1,7. : print change

</ls> <ls n="TS.">
</ls> <ls n="AV.">

</ls> <ls n="ṚV.">
--------------------------------

# generate temp_pwg_2.txt from temp_pwg_1.txt and the 'fixed' elements

python dict_replace2.py temp_pwg_1.txt lsfix2_pwg_1.txt temp_pwg_2.txt
apply_repls: 555 lines changed

-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue134fix
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue134fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pwg temp_pwg_2.txt lsfix2_pwg_2.txt
(None,58),(True,6013),(all,6071) lsfix2_pwg_2.txt
Note: TS. ANUKR. references skipped at this point - from lsfix2_parm.py


Additional links: (- 6013 4514) 1499
---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
223 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
555 changes written to change_pwg_2.txt

===========================================

chkidx compares the kosha references and the link target index.

lsfix3.py is variation of lsfix2.py.  It prepares the input to chkidx.

python lsfix3.py pwg temp_pwg_2.txt lsfix3_pwg_2.txt
(True,6013),(all,6013) lsfix3_pwg_2.txt

example output line:
68407   AGAra   <ls n="TS. 3,1,9,">3.</ls>      3,1,9,3

cp ../issue134/index.txt  index.txt

# modify chkidx.py (Pagerec)

python chkidx.py lsfix3_pwg_2.txt index.txt lsfix3_chkidx_pwg_2.txt
3163 instances find ipage out of 3210
5892 instances find ipage out of 6013
121 references NOT FOUND in index

