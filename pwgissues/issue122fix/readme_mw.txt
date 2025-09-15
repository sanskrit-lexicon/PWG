
mw link forms:
<ls>MārkP. ([vixlc]+), *([0-9]+)

python lsfix2.py mw temp_mw_0.txt lsfix2_mw_0.txt

109 lines written to lsfix2_mw_0.txt
(None, 2) 109

lsfix2 does not handle fixes to mw, since first parm is in roman.
Identify problems by sequence of manual regexes

cp temp_mw_0.txt temp_mw_1.txt

---------
LINKED
 78 <ls>MārkP. [ivxlc]+, [0-9]+\.?</ls> 
  2 <ls n="MārkP.">[ivxlc]+, [0-9]+\.?</ls>
  4 <ls n="MārkP. [ivxlc]+,">[0-9]+\.?</ls>
  2 <ls>MārkP. [ivxlc]+, [0-9]+ f+\.?</ls>
  0 <ls n="MārkP. [ivxlc]+,">[0-9]+ f+\.?</ls>
  0 <ls n="MārkP.">[ivxlc]+, [0-9]+ f+\.?</ls>

NOT LINKED
 20 <ls>MārkP. [ivxlc]+\.?</ls> 
  1 <ls n="MārkP.">[ivxlc]+\.?</ls>
  0 <ls n="MārkP.">[ivxlc]+ f+\.?</ls>
  1 <ls>MārkP. [ivxlc]+ f+\.?</ls>
  1 <ls>MārkP. iii l</ls>    typo iiil
total = 272, as expected

1 change to mw. in temp_mw_1.txt
-------------------------------------------------

# remake xml from temp_mw_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue122fix
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue122fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py mw temp_mw_1.txt lsfix2_mw_1.txt

2686 lines written to lsfix2_mw_2.txt

109 lines written to lsfix2_mw_1.txt
(None, 2) 109

---- documentation in change files
python diff_to_changes_dict.py temp_mw_0.txt temp_mw_1.txt change_mw_1.txt
1 changes written to change_mw_1.txt
