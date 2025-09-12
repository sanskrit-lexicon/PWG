
mw  
python lsfix2.py mw temp_mw_0.txt lsfix2_mw_0.txt

272 lines written to lsfix2_mw_0.txt
(None, 2) 272


lsfix2 does not handle fixes to mw, since first parm is in roman.
Identify problems by sequence of manual regexes

cp temp_mw_0.txt temp_mw_1.txt

---------
LINKED
264 <ls>Kum. [ivxlc]+, [0-9]+\.?</ls> 
  3 <ls n="Kum.">[ivxlc]+, [0-9]+\.?</ls>
  3 <ls n="Kum. [ivxlc]+,">[0-9]+\.?</ls>
  0 <ls>Kum. [ivxlc]+, [0-9]+ f+\.?</ls>
  0 <ls n="Kum. [ivxlc]+,">[0-9]+ f+\.?</ls>
  0 <ls n="Kum.">[ivxlc]+, [0-9]+ f+\.?</ls>

NOT LINKED
  2 <ls>Kum. [ivxlc]+\.?</ls> 
  0 <ls n="Kum.">[ivxlc]+\.?</ls>
  0 <ls n="Kum.">[ivxlc]+ f+\.?</ls>
  0 <ls>Kum. [ivxlc]+ f+\.?</ls>
total = 272, as expected

first parm out of range (i.e., > 7)
1  viii  (8)
14 x     (> 8)

NO changes to mw
-------------------------------------------------
