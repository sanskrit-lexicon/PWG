
readme_changes_mw.txt

references in mw to AitBr. with 3-parameters
 where mw headword not found in aitbr_auf (main) reference.

cf. Andhrabharati's analysis at
  https://github.com/sanskrit-lexicon/PWG/issues/159#issuecomment-3193463177
  
----------------------------------------------
There remain 8 instances marked 'check: not found'

cp temp_mw_0.txt temp_mw_1.txt

----------------------------------------------
 
++key (1, 6, 1): pagerec not found
37011 : upodAsfp : AitBr. 1,6,1 : 
check: not found

old: <ls>AitBr. i, 6, 1</ls>; <ls n="AitBr. i, 6,">3.</ls>
new: <ls>AitBr. vi, 1, 1</ls>; <ls n="AitBr. vi, 1,">3.</ls>

37011 : upodAsfp : AitBr. i, 6, 1; 3. : AitBr. vi, 1, 1; 3. : print change

----------------------------------------------

++key (1, 6, 8): pagerec not found
71518 : canasita : AitBr. 1,6,8 : 
check: not found

old: <ls>AitBr. i, 6, 8</ls>; <ls>Sāy.</ls>
new: <ls>Sāy. on AitBr. i, 6, 8.</ls>  # markup change
 AB: <ls>AitBr. i, 6, 8, <ab>Sāy.</ab></ls>

71518 : canasita : AitBr. 1,6,8; Sāy. : Sāy. on AitBr. i, 6, 8. : print change
----------------------------------------------

key (1, 16, 40): pagerec not found
68918 : grAmayAjin : AitBr. 1,16,40 : 
check: not found


old: <ls>Sāy.</ls> on <ls>AitBr. i, 16, 40.</ls>
new: <ls>Sāy. on AitBr. i, 16, 40.</ls>
----------------------------------------------

++key (2, 19, 9): pagerec not found
39426 : ekapAta : AitBr. 2,19,9 : 
check: not found (Auf 2,19 has only 8 sentences)

old: <ls>Sāy.</ls> on <ls>AitBr. ii, 19, 9.</ls>
new: <ls>Sāy. on AitBr. i, 19, 9.</ls>

39426 : ekapAta : Sāy. on AitBr. ii, 19, 9 : Sāy. on AitBr. i, 19, 9 :  print change
----------------------------------------------

++key (3, 37, 6): pagerec not found
36346 : upasTapadA : AitBr. 3,37,6 : 
check: not found

old: <ls>Sāy.</ls> on <ls>AitBr. iii, 37, 6.</ls>
new: <ls>Sāy. on AitBr. iii, 37, 6.</ls> 
----------------------------------------------

++key (5, 15, 10): pagerec not found
22727 : AgranTam : AitBr. 5,15,10 : 
check: not found; in Auf under 5,15,9

old: <ls>AitBr. v, 15, 10.</ls>
new: <ls>AitBr. v, 15, 9.</ls>  

22727 : AgranTam : AitBr. 5, 15, 10 : AitBr. 5, 15, 9 : print change
----------------------------------------------

++key (5, 25, 5): pagerec not found
29398 : ilava : AitBr. 5,25,5 : 
check: not found

old: <ls>AitBr. v, 25, 5.</ls>
new: <ls>AitBr. v, 3, 5</ls>   
 AB: <ls>AitBr. v, 3, 5,  <ab>Sāy.</ab></ls>
 
29398 : ilava : AitBr. 5, 25, 5 : AitBr. 5, 3, 5 : print change Note: yadelavā 
----------------------------------------------

++key (7, 5, 5): pagerec not found
34967 : upanivft : AitBr. 7,5,5 : 
check: not found, in Auf  at 7,5,6

old: <ls>AitBr. vii, 5, 5.</ls>
new: <ls>AitBr. vii, 5, 6.</ls>

34967 : upanivft : AitBr. vii, 5, 5 : AitBr. vii, 5, 6 : print change


## regenerate mw displays locally
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159auf
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159auf

python diff_to_changes_dict.py temp_mw_0.txt temp_mw_1.txt change_mw_1.txt
---------------------------------------

Add new ls abbrev for mw
csl-pywork/v02/distinctfiles/mw/pywork/mwauth/tooltip.txt

Aitareyabrāhmaṇa, ed. Aufrecht, 1879, Sāyaṇa commentary

137 matches for "<ls>Sāy.</ls> on <ls>" in buffer: temp_mw_1.txt
