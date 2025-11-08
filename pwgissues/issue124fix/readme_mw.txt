
issue124fix

cp temp_mw_0.txt temp_mw_1.txt

---------------------------------------------
# VS. corresponds to linktarget
mw VS. ([xivlc]+),([0-9]+),


python lsfix2.py mw temp_mw_0.txt lsfix2_mw_0.txt
(None,755),(all,755) lsfix2_mw_0.txt

lsfix2.py does not handle mw.txt properly.
As a partial substitute,  classify the instances in lsfix2_mw_0.txt

cp temp_mw_0.txt temp_mw_1.txt
# edit changes to temp_mw_1.txt

91592: dAtyOha : VS. xxiv, 25, 39 : VS. xxiv, 25. 39 : print change
151108 : BImala : VS. 30, 6 : VS. xxx, 6 : print change
219021 : Sukriya : VS. 36-40 : VS. xxxvi — xxxx : print change

python lsfix2.py mw temp_mw_1.txt lsfix2_mw_1.txt
(None,755),(all,755) lsfix2_mw_1.txt

not linked
 43 matches for "<ls>VS. [ivxl]+\( f+\)?\.?</ls>"    
 10 matches for "<ls n="VS.">[ivxl]+\( f+\)?\.?</ls>"
  2 misc:
    112297	utpruz	<ls>VS. p. 58, l. 18</ls>	
    236084	Gasi	<ls>VS. (Kāṇv.) ii, 24</ls>	
(+ 43 10 2) 55

linked
652 matches for "<ls>VS. [ivxl]+, [0-9]+\( f+\)?\.?</ls>"
 23 matches for "<ls n="VS.">[ivxl]+, [0-9]+\( f+\)?\.?</ls>"
 24 matches for "<ls n="VS. [ivxl]+,">[0-9]+\( f+\)?\.?</ls>"
  1 misc:
    279937	tarikA	<ls>VS. xxxix, 5/6</ls>
(+ 652 23 24 1) 700

(+ 55 700) 755 as expected

--------------------------------

# generate temp_mw_2.txt from temp_mw_1.txt and the 'fixed' elements
# no fixed elements
# python dict_replace2.py temp_mw_1.txt lsfix2_mw_1.txt temp_mw_2.txt
# apply_repls: 5 lines changed

-----------------------------------------------------------
# remake xml from temp_mw_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue124fix
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue124fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

---- documentation in change files
python diff_to_changes_dict.py temp_mw_0.txt temp_mw_1.txt change_mw_1.txt
5 changes written to change_mw_1.txt

===========================================

chkidx compares the kosha references and the link target index.

This code (see readme_pwg.txt) doesn't work for mw.


