
alignab/readme.txt
06-02-2026 begin

local directory:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue180/alignab

work to align cdsl with ab. (re <ab>, <lex>, and other similar tags)
start with 
cdsl: alignv1c/temp_pwg_0d_base1.txt
  AB: temp_ab_files/'pwg_(AB)_v1c.txt'

* temp_ab_pwg_v1d.txt, temp_pwg_0e_base1.txt

python change_ab_v1c_v1d.py ../temp_ab_files/'pwg_(AB)_v1c.txt' temp_ab_pwg_v1d.txt
29 lines changed

python change_0d_0e.py ../alignv1c/temp_pwg_0d_base1.txt temp_pwg_0e_base1.txt
# 3467
# use compare_ab.py to identify first difference in <ab>X</ab>

#Find first difference in <ab>X</ab> or <ab n="Y">X</ab>

python compare_ab.py temp_pwg_0e_base1.txt temp_ab_pwg_v1d.txt compare_ab.txt


* Notes
<ls>Sch. ', '<ab>Sch.</ab> <ls n="">  
<ls>ebend.</ls>  followed (perhaps on next line) by "<ls"

462 matches in 461 lines for "<ls>ŚKDR.</ls> <ab>u.</ab>" in v1c
391 matches in 390 lines for "<ls>ŚKDR.</ls> <ab>u.</ab>" in 0e

-------------
# Andhrabharati version has <bot> markup
cdsl: {%Morinda tinctoria%} 
  ab: <bot>Morinda tinctoria</bot>
AB:  <abot>Roxb.</abot>
-------------
AB  16 <lang>pers.</lang> For ab comparisons, change these to <ab>pers.</ab>
    27 <ab>pers.</ab>
cdsl: 34 <ab>pers.</ab>
-------------
AB: <ls>ŚAṂK.</ls>_zu_<ls>  "_zu_" unique to AB version
-------------
AB: <ed>2ten Aufl.</ed>
----------------
AB: <ab>d.</ab> 0
    114 matches for "<ab[^>]*?>d.</ab>
    97 matches for "<ab n="dem">d.</ab>
     6 matches for "<ab n="die">d.</ab>
     9 matches for "<ab n="der">d.</ab>
     1 match   for "<ab n="des">d.</ab>
     1 match   for "<ab n="das">d.</ab>
cdsl: <ab>d.</ab> 72
  Consider all AB forms as cdsl forms.

---------------------
cdsl: 14 matches for "<ab>d.</ab> <ab>folg.</ab>"
  ab: 14 <ab>d. folg.</ab>
---------------------
ab: 9 matches in 8 lines for "n="Süd"  NOTE: Süd = South in German.
  These need to be checked.
-------------------
<is n="Devadatta">D.</is>   one.dtd  Basicdisplay ?
3393 matches in 3065 lines for "<is n" in buffer: temp_ab_pwg_v1d.txt
