
issue134fix

---------------------------------------------
# TS. corresponds to linktarget
sch TS. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)

Other refs starting with 'TS.' (these excluded in further analysis)

11 matches for "TS. Prāt."
 
These are excluded in lsfix2 analysis.

python lsfix2.py sch temp_sch_0.txt lsfix2_sch_0.txt
(None,16),(True,129),(fixed,3),(all,148) lsfix2_sch_0.txt

cp temp_sch_0.txt temp_sch_1.txt
# edit changes to temp_sch_1.txt

python lsfix2.py sch temp_sch_1.txt lsfix2_sch_1.txt
(None,8),(True,143),(fixed,3),(all,154) lsfix2_sch_1.txt

</ls>; <ls n="TS.">

17496 : paYcadaSavartani : TS. 4,3; 3,1. : TS. 4,3,3,1. : print change
====================================

None info:
6157	anadanIya	<ls>TS. 2,738,4.</ls>	
20803	AjiSiras	<ls>TS. 1,1024,3</ls>	
32136	kAmyayAjyA	<ls>TS. 1,1062,1.</ls>	
32142	kAmyezwi	<ls>TS. 1,1062,2</ls>	
44249	tapana	<ls>TS. 1,67,1.</ls>	
48225	dUreheti	<ls>TS. 1,1008,8. 12.</ls>	
55750	parihArasU	<ls>TS. 2,287,14.</ls>	
69961	rAzwraBft	<ls>TS. 3,4,7,</ls>	

---------------------------

# generate temp_sch_2.txt from temp_sch_1.txt and the 'fixed' elements

python dict_replace2.py temp_sch_1.txt lsfix2_sch_1.txt temp_sch_2.txt
apply_repls: 3 lines changed

-----------------------------------------------------------
# remake xml from temp_sch_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue134fix
cp temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh sch  ../../sch
sh xmlchk_xampp.sh sch
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue134fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py sch temp_sch_2.txt lsfix2_sch_2.txt
(None,8),(True,149),(all,157) lsfix2_sch_2.txt

Additional links: (- 149 129) 20
---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_sch_0.txt temp_sch_1.txt change_sch_1.txt
9 changes written to change_sch_1.txt

python diff_to_changes_dict.py temp_sch_1.txt temp_sch_2.txt change_sch_2.txt
3 changes written to change_sch_2.txt

===========================================

chkidx compares the kosha references and the link target index.

lsfix3.py is variation of lsfix2.py.  It prepares the input to chkidx.

python lsfix3.py sch temp_sch_2.txt lsfix3_sch_2.txt
(True,149),(all,149) lsfix3_sch_2.txt


( see readme_pwg.txt )

python chkidx.py lsfix3_sch_2.txt index.txt lsfix3_chkidx_sch_2.txt

48 instances find ipage out of 149
1 references NOT FOUND in index:
5075    aDaIza  <ls>TS. 6,3,3,7.</ls>   6,3,3,7


