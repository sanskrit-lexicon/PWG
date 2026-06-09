
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

* --------------------------------------------
* 06-04-2026 change_0e_0f.py, temp_pwg_0f_base1.txt 
Freeze temp_pwg_0e_base1.txt and change_0d_0e.py.
Initialze change_0e_0f.py,
which is used to generate temp_pwg_0f_base1.txt

# changes to AB version: v1d
python change_ab_v1c_v1d.py ../temp_ab_files/'pwg_(AB)_v1c.txt' temp_ab_pwg_v1d.txt
# 55 lines changed

# changes to temp_pwg_0f.txt
python change_0e_0f.py temp_pwg_0e_base1.txt temp_pwg_0f_base1.txt
# 
# use compare_ab.py to identify first difference in <ab>X</ab>

# Find first difference in abbreviation sequences from 0f and v1d
python compare_ab.py temp_pwg_0f_base1.txt temp_ab_pwg_v1d.txt compare_ab_0f_v1d.txt

---------------------------
* 06-05-2026 change_0f_0g.py, temp_pwg_0g_base1.txt 
Freeze temp_pwg_0f_base1.txt and change_0e_0f.py.
Initialze change_0f_0g.py, which is used to generate temp_pwg_0g_base1.txt
cp change_0e_0f.py change_0f_0g.py a
# changes to AB version: v1d
python change_ab_v1c_v1d.py ../temp_ab_files/'pwg_(AB)_v1c.txt' temp_ab_pwg_v1d.txt
# 71 lines changed

# changes to temp_pwg_0g.txt
python change_0f_0g.py temp_pwg_0f_base1.txt temp_pwg_0g_base1.txt
# 
# use compare_ab.py to identify first difference in <ab>X</ab>

# Find first difference in abbreviation sequences from 0g and v1d
python compare_ab.py temp_pwg_0g_base1.txt temp_ab_pwg_v1d.txt compare_ab_0g_v1d.txt

---------------------------
* 06-06-2026 change_0g_0h.py, temp_pwg_0h_base1.txt 
Freeze temp_pwg_0g_base1.txt and change_0f_0g.py.
Initialze change_0g_0h.py, which is used to generate temp_pwg_0h_base1.txt
#copy change_0e_0f.py change_0g_0h.py 
# changes to AB version: v1d
python change_ab_v1c_v1d.py ../temp_ab_files/'pwg_(AB)_v1c.txt' temp_ab_pwg_v1d.txt
# 87 lines changed

# changes to temp_pwg_0h.txt
python change_0g_0h.py temp_pwg_0g_base1.txt temp_pwg_0h_base1.txt
# 
# use compare_ab.py to identify first difference in <ab>X</ab>

# Find first difference in abbreviation sequences from 0h and v1d
python compare_ab.py temp_pwg_0h_base1.txt temp_ab_pwg_v1d.txt compare_ab_0h_v1d.txt

---------------------------
* 06-08-2026 change_0h_0i.py, temp_pwg_0i_base1.txt 
Freeze temp_pwg_0h_base1.txt and change_0g_0h.py.
Initialze change_0h_0i.py, which is used to generate temp_pwg_0i_base1.txt
#copy change_0g_oh.py change_0h_0i.py 
# changes to AB version: v1d
python change_ab_v1c_v1d.py ../temp_ab_files/'pwg_(AB)_v1c.txt' temp_ab_pwg_v1d.txt
# 87 lines changed

# changes to temp_pwg_0i.txt
python change_0h_0i.py temp_pwg_0h_base1.txt temp_pwg_0i_base1.txt
# 
# use compare_ab.py to identify first difference in <ab>X</ab>

# Find first difference in abbreviation sequences from 0h and v1d
python compare_ab.py temp_pwg_0i_base1.txt temp_ab_pwg_v1d.txt compare_ab_0i_v1d.txt

python make_change_01.py temp_pwg_0i_base1.txt make_change_01.txt
111 changes
python make_change_02.py temp_pwg_0i_base1.txt make_change_02.txt
53 changes
python make_change_03.py temp_pwg_0i_base1.txt make_change_03.txt
75 changes
---------------------------
* 06-08-2026 change_0h_0j.py, temp_pwg_0j_base1.txt 
Freeze temp_pwg_0i_base1.txt and change_0h_0i.py.
Initialze change_0i_0j.py, which is used to generate temp_pwg_0j_base1.txt
#copy change_0h_oi.py change_0i_0j.py 
# changes to AB version: v1d
python change_ab_v1c_v1d.py ../temp_ab_files/'pwg_(AB)_v1c.txt' temp_ab_pwg_v1d.txt
# 90 lines changed

# changes to temp_pwg_0j.txt
python change_0i_0j.py temp_pwg_0i_base1.txt temp_pwg_0j_base1.txt
# 
# use compare_ab.py to identify first difference in <ab>X</ab>

# Find first difference in abbreviation sequences from 0h and v1d
python compare_ab.py temp_pwg_0j_base1.txt temp_ab_pwg_v1d.txt compare_ab_0j_v1d.txt

python make_change_04.py temp_pwg_0j_base1.txt make_change_04.txt
26 changes

python make_change_05.py temp_pwg_0j_base1.txt make_change_05.txt
17 changes

python make_change_06.py temp_pwg_0j_base1.txt make_change_06.txt
27=8 changes
---------------------------
* additional notes
--------------
85 matches for "<ab>u.</ab> <ab n="dem">d.</ab>" v1d
 9 matches for "<ab>u. d.</ab>"
104 matches for "<ab>u. d.</ab>" in 0f
2 matches for "<ms>" in buffer: temp_ab_pwg_v1d.txt 
----
what's the diff?
 ('(<ab>vgl.</ab> <ab>S.</ab> 370)',
   '(<ab>vgl.</ab> <ab n="Seite">S.</ab> 370)'),
----
