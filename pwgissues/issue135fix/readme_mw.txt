
issue135fix

mw link forms:
2 parameters.

3523 matches in 3455 lines for "Rājat\." in temp_mw_0.txt
  2837 matches in 2835 lines for "<ls>Rājat\.</ls>"
   573 matches for "<ls>Rājat\. "
   113 matches in 89 lines for "<ls n="Rājat\."

python lsfix2.py mw temp_mw_0.txt lsfix2_mw_0.txt
(None,686),(all,686) lsfix2_mw_0.txt
  Note: (+ 573 113) = 686

498 <ls>Rājat. [iv]+, [0-9]+\.?</ls>
 45 <ls n="Rājat. [iv]+,">[0-9]+\.?</ls>
 43 <ls n="Rājat.">[iv]+, [0-9]+\.?</ls>
  2 <ls n="Rājat.">[iv]+, [0-9]+ [f]+\.?</ls>
 14 <ls>Rājat. [iv]+, [0-9]+ [f]+\.?</ls>
  5 <ls n="Rājat. [iv]+,">[0-9]+ [f]+\.?</ls>

 59 <ls>Rājat. [iv]+\( [f]+\)?\.?</ls>
 15 <ls n="Rājat.">[iv]+\( [f]+\)?\.?</ls>

(+ 498 45 43 2 14 5 59 15) 681
 5 others
 
cp temp_mw_0.txt temp_mw_1.txt

Make changes to temp_mw_1 
 
python lsfix2.py mw temp_mw_1.txt lsfix2_mw_1.txt
(None,685),(all,685) lsfix2_mw_1.txt

Similar analysis using temp_mw_1.txt
498 <ls>Rājat. [iv]+, [0-9]+\.?</ls>
 46 <ls n="Rājat. [iv]+,">[0-9]+\.?</ls>
 44 <ls n="Rājat.">[iv]+, [0-9]+\.?</ls>
  2 <ls n="Rājat.">[iv]+, [0-9]+ [f]+\.?</ls>
 14 <ls>Rājat. [iv]+, [0-9]+ [f]+\.?</ls>
  5 <ls n="Rājat. [iv]+,">[0-9]+ [f]+\.?</ls>

 59 <ls>Rājat. [iv]+\( [f]+\)?\.?</ls>
 15 <ls n="Rājat.">[iv]+\( [f]+\)?\.?</ls>

(+ 498 46 44 2 14 5 59 15) 683

2 others
jagat   <ls>Rājat. (C) iii, 494</ls>	
tipya   <ls>Rājat. viii, 15, 5.</ls>	


--------------------
# generate temp_mw_2.txt from temp_mw_1.txt and the 'fixed' elements
python dict_replace2.py temp_mw_1.txt lsfix2_mw_1.txt temp_mw_2.txt
apply_repls: 32 lines changed

-----------------------------------------------------------
# remake xml from temp_mw_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue135fix
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue135fix
-- end of 'remake xml ...'


---- documentation in change files
python diff_to_changes_dict.py temp_mw_0.txt temp_mw_1.txt change_mw_1.txt
3 changes written to change_mw_1.txt
