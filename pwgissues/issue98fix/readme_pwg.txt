
issue98fix

cp temp_pwg_0.txt temp_pwg_1.txt

---------------------------------------------
# YĀJÑ. corresponds to linktarget
pwg YĀJÑ. ([0-9]+),([0-9]+),

python lsfix2.py pwg temp_pwg_0.txt lsfix2_pwg_0.txt
(False,3),(None,88),(True,3511),(fixed,182),(all,3784) lsfix2_pwg_0.txt

cp temp_pwg_0.txt temp_pwg_1.txt
# edit changes to temp_pwg_1.txt

python lsfix2.py pwg temp_pwg_1.txt lsfix2_pwg_1.txt
(None,9),(True,3586),(fixed,183),(all,3778) lsfix2_pwg_1.txt


None instances:  references to preface
32291	aparArka	<ls>YĀJÑ. Vorrede V.</ls>	
366779	nandapaRqita	<ls>YĀJÑ. VI.</ls>	
436694	pArASara	<ls>YĀJÑ. VII.</ls>	
474110	pratItAkzarA	<ls>YĀJÑ. S. VI.</ls>	
509089	bAlaMBawwa	<ls>YĀJÑ. VI.</ls>	
581617	mAnava	<ls>YĀJÑ. S. VII.</ls>	
586900	mitAkzara	<ls>YĀJÑ. V. fg.</ls>	
882480	vEjayanta	<ls>YĀJÑ. S. VI.</ls>	
912118	SANKaliKita	<ls>YĀJÑ. S. VII.</ls>	

---------------------------
MISC COMMENTS

END MISC COMMENTS

--------------------------------

# generate temp_pwg_2.txt from temp_pwg_1.txt and the 'fixed' elements

python dict_replace2.py temp_pwg_1.txt lsfix2_pwg_1.txt temp_pwg_2.txt
apply_repls: 183 lines changed

-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue98fix
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue98fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pwg temp_pwg_2.txt lsfix2_pwg_2.txt
(None,9),(True,3995),(all,4004) lsfix2_pwg_2.txt


Additional links: (- 3995 3511) 484

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
102 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
183 changes written to change_pwg_2.txt

===========================================

chkidx compares the kosha references and the link target index.

lsfix3.py is variation of lsfix2.py.  It prepares the input to chkidx.

python lsfix3.py pwg temp_pwg_2.txt lsfix3_pwg_2.txt
(True,3995),(all,3995) lsfix3_pwg_2.txt

example output line:
216     aMSahara        <ls n="YĀJÑ. 2,">133.</ls>      2,133

cp ../issue98/yajn_index_v1_edit.txt  index.txt
# modify chkidx.py (Pagerec) for this kosha
 <<<  remove vol field
 <<<  THere is no ipage in index.txt, use epage 

python chkidx.py lsfix3_pwg_2.txt index.txt lsfix3_chkidx_pwg_2.txt
3993 instances find ipage out of 3995
2 references NOT FOUND in index

116886 : hi : YĀJÑ. 2,190. 8,283. : YĀJÑ. 2,190. 3,283. : print change
