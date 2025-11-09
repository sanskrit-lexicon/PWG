
issue98fix

cp temp_mw_0.txt temp_mw_1.txt

---------------------------------------------
# Yājñ. corresponds to linktarget
mw Yājñ. ([0-9]+),([0-9]+),

python lsfix2.py mw temp_mw_0.txt lsfix2_mw_0.txt
(None,714),(all,714) lsfix2_mw_0.txt

python lsfix2.py mw temp_mw_1.txt lsfix2_mw_1.txt
(None,715),(all,715) lsfix2_mw_1.txt

lsfix2.py does not handle mw.txt properly.
As a partial substitute,  classify the instances in lsfix2_mw_0.txt

--------------------------------

linked
651 matches for "<ls>Yājñ. [ivxl]+, [0-9]+\( f+\)?\.?</ls>"
  8 matches for "<ls n="Yājñ.">[ivxl]+, [0-9]+\( f+\)?\.?</ls>"
 18 matches for "<ls n="Yājñ. [ivxl]+,">[0-9]+\( f+\)?\.?</ls>"

(+ 651 8 18) 677

unlinked
 18 matches for "<ls>Yājñ. [ivxl]+\( f+\)?\.?</ls>"    
  1 matches for "<ls n="Yājñ.">[ivxl]+\( f+\)?\.?</ls>"
 19 matches for "/[^l]"   # linkable, see 'wrong links' list below
 
(+ 18 1 19) 38

(+ 677 38) 715  as expected
wrong links: headword not found in reference.
221598	girISa	<ls>Yājñ. ii, 102/103, 34</ls>	
224008	gurukArya	<ls>Yājñ. ii, 5/6, 31</ls>	
225714	gfhaja	<ls>Yājñ. ii, 181/182</ls>	
225720	gfhajAta	<ls>Yājñ. ii, 181/182</ls>	
227348	gocaraya	<ls>Yājñ. ii, 96 a/b.</ls>	
240597	catuHsaMkara	<ls>Yājñ. ii, 7 a/b, 49.</ls>	
241422	caturviMSatimata	<ls>Yājñ. iii, 327/328, 9</ls>	
247067	cAracakzus	<ls>Yājñ. ii, 3/4.</ls>	
265835	jAbAlaSruti	<ls>Yājñ. iii, 57/58</ls>	
268239	jIva	<ls>Yājñ. ii, 102/103, 39</ls>	
270624	jYAtipraBuka	<ls>Yājñ. ii, 5/6, 28.</ls>	
275792	tattvABiyoga	<ls>Yājñ. ii, 5/6, 4 ff.</ls>	
275948	tatsaMKyAka	<ls>Yājñ. ii, 6/7.</ls>	
289485	tulADAra	<ls>Yājñ. ii, 102/103</ls>	
295238	tripaYcaka	<ls>Yājñ. ii, 181/182, 11.</ls>	
301230	daRqaBAj	<ls>Yājñ. ii, 5/6, 35.</ls>	
301869	dattApradAnika	<ls n="Yājñ. ii,">174/175.</ls>	
306360	dahara	<ls>Yājñ. iii, 279/271</ls>	
306500	dA	<ls>Yājñ. ii, 6/7</ls>	

-----------------------------------------------------------
# remake xml from temp_mw_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue98fix
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue98fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py mw temp_mw_2.txt lsfix2_mw_2.txt

Additional links: (- 61 58) 3

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_mw_0.txt temp_mw_1.txt change_mw_1.txt
1 changes written to change_mw_1.txt

python diff_to_changes_dict.py temp_mw_1.txt temp_mw_2.txt change_mw_2.txt
1 changes written to change_mw_2.txt

===========================================

chkidx compares the kosha references and the link target index.

lsfix3.py is variation of lsfix2.py.  It prepares the input to chkidx.

python lsfix3.py mw temp_mw_2.txt lsfix3_mw_2.txt

python chkidx.py lsfix3_mw_2.txt index.txt lsfix3_chkidx_mw_2.txt
61 instances find ipage out of 61
0 references NOT FOUND in index
6
