
mw  
python lsfix2.py mw temp_mw_0.txt lsfix2_mw_0.txt

976 lines written to lsfix2_mw_0.txt
(None, 2) 976

lsfix2 does not handle fixes to mw, since first parm is in roman.
Identify problems by sequence of manual regexes

cp temp_mw_0.txt temp_mw_1.txt

---------
LINKED
600 <ls>Kathās. [ivxlc]+, [0-9]+\.?</ls> 
 68 <ls n="Kathās.">[ivxlc]+, [0-9]+\.?</ls>
 15 <ls n="Kathās. [ivxlc]+,">[0-9]+\.?</ls>
 18 <ls>Kathās. [ivxlc]+, [0-9]+ f+\.?</ls>
  2 <ls n="Kathās. [ivxlc]+,">[0-9]+ f+\.?</ls>
  1  <ls n="Kathās.">[ivxlc]+, [0-9]+ f+\.?</ls>

NOT LINKED
181 <ls>Kathās. [ivxlc]+\.?</ls> 
 57 <ls n="Kathās.">[ivxlc]+\.?</ls>
  ;; not linked
  1 <ls n="Kathās.">[ivxlc]+ f+\.?</ls>
  6 <ls>Kathās. [ivxlc]+ f+\.?</ls>

  9 remaining -- examine
92326	<ls>Kathās. 52, 123.</ls>	
94376	<ls>Kathās. 57, 136</ls>	
97012	<ls>Kathās. 90, 18.</ls>	
110841	<ls>Kathās. 123, 196</ls>	
238771	<ls>Kathās. liv, III.</ls>	
241053	<ls>Kathās. xxiv-xxvi.</ls>	
306447	<ls n="Kathās.">222 f.</ls>	

print changes:
26060 : Arawi : Kathās. 52, 123. : Kathās. vii, 123. : print change
26667 : Ala : Kathās.   57, 136 : Kathās. vvii, 136 :  print change
27433 : ASarIram : Kathās. 90, 18. : Kathās. xc, 18. : print change
31381 : uttaraMga : Kathās. 123, 196 : Kathās. cxxiii, 196 :  print change
70539 : cakrasenA : Kathās. liv, III. :  Kathās. liv, 111. : print change

91212 : dA : <ls n="Kathās.">222 f.</ls> : <ls n="Mn. viii,">222 f.</ls> : markup change

-------------------------------------------------
python lsfix2.py mw temp_mw_1.txt lsfix2_mw_1.txt

975 lines written to lsfix2_mw_1.txt
(None, 2) 975


repeate analysis
LINKED
625 <ls>Kathās. [ivxlc]+, [0-9]+\.?</ls>
 68 <ls n="Kathās.">[ivxlc]+, [0-9]+\.?</ls>
 15 <ls n="Kathās. [ivxlc]+,">[0-9]+\.?</ls> 
 18 <ls>Kathās. [ivxlc]+, [0-9]+ f+\.?</ls> 
  2 <ls n="Kathās. [ivxlc]+,">[0-9]+ f+\.?</ls>
  1 <ls n="Kathās.">[ivxlc]+, [0-9]+ f+\.?</ls>
     
NOT LINKED
181 <ls>Kathās. [ivxlc]+\.?</ls>
 57 <ls n="Kathās.">[ivxlc]+\.?</ls>
  1 <ls n="Kathās.">[ivxlc]+ f+\.?</ls>
  6 <ls>Kathās. [ivxlc]+ f+\.?</ls>

1  variant

---------------------------------------

# remake xml from temp_mw_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue70fix
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue70fix
-- end of 'remake xml ...'

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_mw_0.txt temp_mw_1.txt change_mw_1.txt
