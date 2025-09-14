
mw  
python lsfix2.py mw temp_mw_0.txt lsfix2_mw_0.txt

3874 lines written to lsfix2_mw_0.txt
(None, 2) 3874

lsfix2 does not handle fixes to mw, since first parm is in roman.
Identify problems by sequence of manual regexes

cp temp_mw_0.txt temp_mw_1.txt
After changes to temp_mw_1, rerun lsfix2

python lsfix2.py mw temp_mw_1.txt lsfix2_mw_1.txt
3908 lines written to lsfix2_mw_1.txt
(None, 2) 3908

Redo analysis:
---------
LINKED
3366 <ls>Mn. [ivxlc]+, [0-9]+\.?</ls> 
 168 <ls n="Mn.">[ivxlc]+, [0-9]+\.?</ls>
 191 <ls n="Mn. [ivxlc]+,">[0-9]+\.?</ls>
  18 <ls>Mn. [ivxlc]+, [0-9]+ f+\.?</ls>
   3 <ls n="Mn. [ivxlc]+,">[0-9]+ f+\.?</ls>
   5 <ls n="Mn.">[ivxlc]+, [0-9]+ f+\.?</ls>
(157 remain)


NOT LINKED
  76 <ls>Mn. [ivxlc]+\.?</ls> 
  47 <ls n="Mn.">[ivxlc]+\.?</ls>
   8 <ls n="Mn.">[ivxlc]+ f+\.?</ls>
  10 <ls>Mn. [ivxlc]+, [0-9]+/[0-9]+\.?</ls> 
   1 <ls n="Mn.">[ivxlc]+, [0-9]+/[0-9]+\.?</ls>
   2 misc.
     <ls>Mn. ii vi f.</ls>
     <ls>Mn. 89</ls>

-----------------------------------
Emacs global change to temp_mw_1.txt

<ls>Mn. x, 41, 46</ls>

<ls>Mn. \([ivxlc]+\), \([0-9]+\), \([0-9]+\.?\)</ls>
 ->
 <ls>Mn. \1, \2</ls>, <ls n="Mn. \1,">\3</ls>

29
-----------------------------------

-------------------------------------------------
Example: <ls>Mn. i, 6/7</ls>jayAditya
  11 instances
  No change.
  These links are to an unknown edition.
  Displays link to Mn. i,6
    but the mw headword (jayAditya)- not found at link. i,6 or i,7
  Headwords:
   jayAditya (2), jAta, jAbAlaSruti, jAbAli, jAraja,
   jIrRavAwikA, tAtkAlika, tAntrika, tAmra, tAla
  
-------------------------------------------------

# remake xml from temp_mw_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue73fix
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue73fix
