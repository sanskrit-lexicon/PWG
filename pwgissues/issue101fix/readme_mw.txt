
issue101fix

mw link forms:
"Sāh.",  1 or 2 parameters
  

python lsfix2.py mw temp_mw_0.txt lsfix2_mw_0.txt
(None,188),(True,27),(all,215) lsfix2_mw_0.txt

The 'True' items are 1-parameter (section)
25 matches for "<ls>Sāh. [0-9]+\.?</ls>"
2 matches for "<ls n="Sāh.">[0-9]+\.?</ls>"

The None items
 2 matches for "<ls>Sāh. [0-9]+, [0-9]+\.?</ls>"     link to sahityadarpana
84 matches for "<ls>Sāh. [ivx]+, [0-9]+\( f\)?\.?</ls>"     link to sahityadarpana_mw
 3 matches for "<ls n="Sāh.">[ivx]+, [0-9]+\.?</ls>" link to sahityadarpana_mw
13 matches for "<ls n="Sāh. [ivx]+,">[0-9]+\.?</ls>" link to sahityadarpana_mw
20 matches for "<ls>Sāh. [ivx]+, [0-9]+ a/b\.?</ls>" link to sahityadarpana_mw
32 matches for "<ls>Sāh. [ivx]+, [0-9]+/[0-9]+\.?</ls>" link to sahityadarpana_mw
 3 matches for "<ls n="Sāh. [ivx]+,">[0-9]+/[0-9]+\.?</ls>" link to sahityadarpana_mw
 3 matches for "<ls n="Sāh.">[ivx]+, [0-9]+/[0-9]+\.?</ls>" link to sahityadarpana_mw
 8 matches for "<ls>Sāh. [ivx]+\.?</ls>" do not link
 7 matches for "<ls>Sāh. [ivx]+, [0-9]+/[0-9]+, [0-9]+\.?</ls>" these link (to X, Y)  what is last parm?
    example: gamakatva	<ls>Sāh. v, 4/5, 12.</ls>


gamakatva <ls>Sāh. v, 4/5, 12.</ls>
   This links to 5,4  and word is found following the verse.
   app1 fails at https://sanskrit-lexicon-scans.github.io/sahityadarpana_mw/app1?5,5
      which is on page 271;  Also. there is no v,12  (app1?5,12)
See readme_mw_unusual.txt  for some further examples

cp temp_mw_0.txt temp_mw_1.txt

Make changes to temp_mw_1 and 2 to correct None

13529 : asakO : SĀH. D. 49, ult. fg. : SĀH. D. 49,21. fg. : print change

python lsfix2.py mw temp_mw_1.txt lsfix2_mw_1.txt
True  (+ 14 24) 38

--------------------
# no 'fixed' elements
# generate temp_mw_2.txt from temp_mw_1.txt and the 'fixed' elements
# python dict_replace2.py temp_mw_1.txt lsfix2_mw_1.txt temp_mw_2.txt

-----------------------------------------------------------
# remake xml from temp_mw_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue101fix
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue101fix
-- end of 'remake xml ...'

---------------------------------------------------

---- documentation in change files
python diff_to_changes_dict.py temp_mw_0.txt temp_mw_1.txt change_mw_1.txt
2 changes written to change_mw_1.txt

==============================================================
THE END
