
mw  
python lsfix2.py mw temp_mw_0.txt lsfix2_mw_0.txt

6184 lines written to lsfix2_mw_0.txt
(None, 2) 6184

lsfix2 does not handle fixes to mw, since first parm is in roman.
Identify problems by sequence of manual regexes

cp temp_mw_0.txt temp_mw_1.txt

100775 : DAneya : MBh. 13, 5468 : MBh. xiii, 5468 : print change


python lsfix2.py mw temp_mw_1.txt lsfix2_mw_1.txt

(None, 2) 6189

---------
LINKED
4024 <ls>MBh. [ivxlc]+, [0-9]+\.?</ls> 
 462 <ls n="MBh.">[ivxlc]+, [0-9]+\.?</ls>
 212 <ls n="MBh. [ivxlc]+,">[0-9]+\.?</ls>
  78 <ls>MBh. [ivxlc]+, [0-9]+ f+\.?</ls>
  15 <ls n="MBh. [ivxlc]+,">[0-9]+ f+\.?</ls>
  17 <ls n="MBh.">[ivxlc]+, [0-9]+ f+\.?</ls>
 221 <ls>MBh. [ivxlc]+, [0-9]+, [0-9]+\.?</ls>
  19 <ls n="MBh.">[ivxlc]+, [0-9]+, [0-9]+\.?</ls>
   8 <ls n="MBh. [ivxlc]+,">[0-9]+, [0-9]+\.?</ls>
   2 <ls n="MBh. [ivxlc]+, [0-9]+,">[0-9]+\.?</ls>
  
 (+ 4024 462 212 78 15 17 221 19 8 2)  5058
 
NOT LINKED
 657 <ls>MBh. [ivxlc]+\.?</ls> 
 351 <ls n="MBh.">[ivxlc]+\.?</ls>
  31 <ls n="MBh.">[ivxlc]+ f+\.?</ls>
  48 <ls>MBh. [ivxlc]+ f+\.?</ls>
  11 ch\.
  15 <ls>MBh. (B.)</ls>
   1 <ls>MBh. [B.]</ls>
   4 <ls>MBh. [0-9]+\.?</ls>
   7 Bomb  (some may be linked -- depending on basicadjust coding)
   5 Calc  (some may be linked -- depending on basicadjust coding)
   1 misc.
(+ 656 350 31 48 11 15 1 4 7 5 1) 1129

(+ 5058 1129) 6187   approx.  latest read gives 6189


-----------------------------------------------------------
# remake xml from temp_mw_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue48fix
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue48fix
-- end of 'remake xml ...'

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_mw_0.txt temp_mw_1.txt change_mw_1.txt
21 changes written to change_mw_1.txt

-------------------------------------------------
