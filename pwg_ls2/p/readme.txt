PWG/pwg_ls2/p


Similar to pwg_ls2/av, but for Panini azwADyAyI


Refer:
 https://github.com/sanskrit-lexicon/PWG/issues/51

Start with a copy of csl-orig/v02/pwg/pwg.txt at commit
  199aa0ddc8e4960d78be30cde80b2cbaf77c035c
  
# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_pwg_00.txt in this spruch directory
  git show 199aa0d:v02/pwg/pwg.txt > /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/p/temp_pwg_00.txt
# return to this av directory
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/p/
# -------------------------------------------------------------
Focus on ls of form '<ls>P...</ls>'
Also handle those such as '<ls n="P."'
21567 matches in 21341 lines for "<ls>P\." in buffer: temp_pwg_00.txt

190 matches in 123 lines for "<ls n="P\." in buffer: temp_pwg_00.txt
121 matches in 77 lines for "<ls n="P\." in buffer: temp_pwg_00.txt

# -------------------------------------------------------------
cp temp_pwg_00.txt temp_pwg_01.txt
We will manually add changes contained in change_01.txt to update
 temp_pwg_01.txt.

# -------------------------------------------------------------

python listls3_abnormal.py 'P.' temp_pwg_00.txt temp_abnormal_av_00.txt temp_change_abnormal.txt

2643 abnormal ls written to temp_abnormal_av_00.txt
2643 change transactions temp_change_abnormal.txt
    98 <ls n="P. PRĀT. #, ">#.</ls>
    65 <ls n="P. PRĀT.">#, #.</ls>
     2 <ls n="P[.] #, #,">#.</ls>
     3 <ls n="P[.] #,">#, #.</ls>
    19 <ls n="P[.]">#, #, #.</ls>
     3 <ls>P. ANUKR. #, #.</ls>
     5 <ls>P. ANUKR.</ls>
   516 <ls>P. PRĀT\. #, #.</ls>
    11 <ls>P. PRĀT\.</ls>
    52 <ls>P[.] #, #, #. fgg.</ls>
     4 <ls>P[.] #, #, #. v. l.</ls>
  6559 <ls>P[.] #, #, #.</ls>
   171 <ls>P[.]</ls>
totals= 7508


regex replace
6332 matches for ",</ls> 
<ls>" in buffer: temp_pwg_00.txt

-----------------------------------------------------
Manual changes in temp_pwg_01.txt
To insert a newline interactively in emacs, use C-q C-j
Character shows as red-underlined ^J

Manual change 1:
Let X be this newline. Replace-regex
,</ls>\( *\)X\(<ls>Sch\.</ls> *$\) → ,</ls>\1 \2X
Replaced 2806 occurrences

Manual change 2:
# Remove double spaces:
Replace '</ls>  <ls>' with '</ls> <ls>'
Replace 2807 occurrences.

Manual change 3:
Let X be this newline. Replace-regex
,</ls>\( \)X\(<ls>Sch\.</ls>\)  → ,</ls>\1 \2X
Replaced 1456 occurrences

Manual change 4:
# Remove double spaces:
Replace '</ls>  <ls>' with '</ls> <ls>'
Replace 2807 occurrences.

Manual change 5:
Let X be this newline. Replace-regex
,</ls>\( \)X\(<ls>Sch\..*?</ls>\)  → ,</ls>\1 \2X
Replaced 205 occurrences
 EXAMPLE
OLD:
<ls>P. 7, 1, 76,</ls> 
<ls>Sch. 8, 2, 16,</ls> <ls>Sch.</ls>
NEW:
<ls>P. 7, 1, 76,</ls>  <ls>Sch. 8, 2, 16,</ls>
<ls>Sch.</ls>

Manual change 6:
# Remove double spaces:
Replace '</ls>  <ls>' with '</ls> <ls>'
Replace 205 occurrences.

Manual change 7:
Let X be this newline. Replace-regex
,</ls>\( \)X\(<ls>Sch\..*?</ls>\) → ,</ls>\1 \2X
Replaced 149 occurrences

Example:
OLD:
<ls>P. 1, 1, 14,</ls> 
<ls>Sch.</ls>; vgl. <is>gaṇa</is> {#cAdi#} und 
NEW:
<ls>P. 1, 1, 14,</ls>  <ls>Sch.</ls>; 
vgl. <is>gaṇa</is> {#cAdi#} und 

Manual change 8:
# Remove double spaces:
Replace '</ls>  <ls>' with '</ls> <ls>'
Replace 149 occurrences.

Manual change 9:
',</ls> <ls>' -> '</ls>, <ls>

Manual change 10:
\(<ls>P\. [0-9]+, [0-9]+, [0-9]+\), \(<is>Vārtt</is>\. [0-9]+\)</ls> → \1</ls>, \2
Example:
OLD:
<ls>P. 1, 1, 68, <is>Vārtt</is>. 4</ls>
NEW:
<ls>P. 1, 1, 68</ls>, <is>Vārtt</is>. 4
338 replacements

Manual change 11:
 \(<ls>P\. [0-9]+, [0-9]+, [0-9]+\), \(<is>Vārtt</is>\. [0-9]+\.\)</ls> → \1</ls>, \2

Example:
OLD:
<ls>P. 6, 3, 3, <is>Vārtt</is>. 1.</ls>
NEW:
<ls>P. 6, 3, 3</ls>, <is>Vārtt</is>. 1.

755 replacements

Manual change 12:
, <is>Vārtt</is>.</ls> → </ls>, <is>Vārtt</is>.
Replace 366 occurrences

Manual change 13:
, \(<is>Vārtt</is>\. [0-9]\.\)</ls> → </ls>, \1
Replaced 97 occurrences

Manual change 14:
' \(<is>Vārtt</is>\.\)</ls> → </ls> \1'
Replaced 24 occurrences
Example
218009
<ls>P. 1, 4, 24. <is>Vārtt</is>.</ls> {#aDarmAcca jugupseta#} 
<ls>P. 1, 4, 24.</ls> <is>Vārtt</is>. {#aDarmAcca jugupseta#} 

Manual change 15:
Replaced 120 occurrences
Example: line 340661
<ls>P. 5, 3, 83, <is>Vārtt</is>. 2, Schol.</ls>
<ls>P. 5, 3, 83</ls>, <is>Vārtt</is>. 2, Schol.

Manual change 16:
', <is>Vārtt</is>., Schol.</ls> → </ls>, <is>Vārtt</is>., Schol.''
Replaced 36

Manual change 17:
', Schol.</ls> → </ls>, Schol.'
Replace 1172 occurrences

Manual change 18:
', Sch.</ls> → </ls>, Sch.'
Replaced 72 occurrences

Manual change 19:
'. Schol.</ls> → .</ls> Schol.'
Replaced 162 occurrences

Manual change 20:
'. Sch.</ls> → .</ls> Sch.'
Replaced 22 occurrences

67279
<ls>SAUN. <is>Vārtt</is>. 3.</ls> Schei
<ls>SAUN.</ls> <is>Vārtt</is>. 3.

Manual change 21:
' \. \(<is>Vārtt</is>\. [0-9]+\.\)</ls> → .</ls> \1'
Replaced 13

Manual change 22:
' \. \(<is>Vārtt</is>\. [0-9]+\.\)</ls> → .</ls> \1'
Replaced 13

Manual change 23:
1003671
<ls>1, 1, 23, <is>Vārtt</is>. 1.</ls>
<ls>1, 1, 23</ls>, <is>Vārtt</is>. 1. 
Replaced 5

Manual change 24:
', <is>Kār</is>.</ls> → </ls>, <is>Kār</is>.'
Replace 24

Manual change 25:
', \(<is>Kār</is>. [0-9]+[.]?\)</ls> → </ls>, \1'
line 12397
Replace 4

Manual change 26:
'\. \(<is>Kār</is>. [0-9]+[.]?\)</ls> → .</ls> \1'
Replace 14
145548
<ls>P. 6, 1, 59. <is>Kār</is>. 5</ls> aus
<ls>P. 6, 1, 59.</ls> <is>Kār</is>. 5 aus

Manual change 27:
'. <is>Kār</is>.</ls> → .</ls> <is>Kār</is>.'
228547
<is>Vārtt</is>. <is>Kār</is>.</ls>
<is>Vārtt</is>.</ls> <is>Kār</is>.
13 Replace

Manual change 28:
', \(<is>Vārtt</is>\. [0-9]+[.]?\)</ls> → </ls>, \1'
25543
<ls>P. 1, 1, 46. 47, <is>Vārtt</is>. 1</ls>; vgl.
<ls>P. 1, 1, 46. 47</ls>, <is>Vārtt</is>. 1; vgl. 
33 Replace

Manual change 29:
'. \(<is>Vārtt</is>\. [0-9]+[.]?\)</ls> → .</ls> \1'
21 Replace
98656
<ls>P. 1, 4, 1. <is>Vārtt</is>. 3</ls>, <ls>Sch.</ls>
<ls>P. 1, 4, 1.</ls> <is>Vārtt</is>. 3, <ls>Sch.</ls>

Manual change 30:
24  Replace
4756
<ls>P. 6, 4, 40, <is>Vārtt</is>. 2. 3.</ls>
<ls>P. 6, 4, 40</ls>, <is>Vārtt</is>. 2. 3.

Manual change 31
', \(<is>Vārtt</is>\. [0-9][.]\) \([0-9]+, [0-9]+, [0-9]+[.]?\)</ls> → </ls>, \1 <ls>\2</ls>'
21 Replace
 11346
<ls>P. 7, 4, 93, <is>Vārtt</is>. 3. 1, 2, 48</ls>, <is>Vārtt</is>., <ls>Sch.</ls>
<ls>P. 7, 4, 93</ls>, <is>Vārtt</is>. 3. <ls>1, 2, 48</ls>, <is>Vārtt</is>., <ls>Sch.</ls>

Manual change 32
 ', \(<is>Vārtt</is>\.\) \([0-9]+, [0-9]+, [0-9]+[.]?\)</ls> → </ls>, \1 <ls>\2</ls>'
9 Replace
 28253
<ls>P.</ls> (<ls>ed. Calc.) 1, 4, 65, <is>Vārtt</is>. 3, 3, 106</ls>, Sch.
<ls>P.</ls> (<ls>ed. Calc.) 1, 4, 65</ls>, <is>Vārtt</is>. <ls>3, 3, 106</ls>, Sch. 

Manual change 33:
', <is>Vārtt</is>.)</ls> → </ls>, <is>Vārtt</is>.)'
6 Replace

END of manual changes

---------------------------------------------------------
generate change_01.txt (which has all the manual changes)
Initialize change_01
python diff_to_changes.py temp_pwg_00.txt temp_pwg_01.txt change_01.txt
13132 changes written to change_01.txt

---------------------------------------------------------
 python listls3_abnormal.py 'P.' temp_pwg_01.txt temp_abnormal_p_01.txt temp_change_abnormal.txt
1149413 lines read from temp_pwg_01.txt
122736 entries found
2200 abnormal ls written to temp_abnormal_p_01.txt
2200 change transactions temp_change_abnormal.txt
    10 <ls n="P[.] #, #,">#.</ls>
    14 <ls n="P[.] #,">#, #.</ls>
     1 <ls n="P[.]">#, #, #. fgg.</ls>
    92 <ls n="P[.]">#, #, #.</ls>
   119 <ls>P[.] #, #, #. fgg.</ls>
    21 <ls>P[.] #, #, #. v. l.</ls>
 18992 <ls>P[.] #, #, #.</ls>
   239 <ls>P[.]</ls>
totals= 19488


------------------------------------------------

------------------------------------------------
python make_change3_abnormal.py 'P.' temp_pwg_01.txt temp_change3_abnormal.txt
1291 records written to temp_change3_abnormal.txt

# insert temp_change3_abnormal.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt

15317 change transactions from change_01.txt

------------------------------------------------
python listls3_abnormal.py 'P.' temp_pwg_01.txt temp_abnormal_p_02.txt temp_change_abnormal_02.txt
397 abnormal ls written to temp_abnormal_p_02.txt

temp_change_abnormal_02_edit.txt manual changes.
# Manual changes from temp_change_abnormal_02_edit.txt inserted into change_01

python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
15702 change transactions from change_01.txt


------------------------------------------------
python listls3_abnormal.py 'P.' temp_pwg_01.txt temp_abnormal_p_03.txt temp_change_abnormal_03.txt

29 abnormal ls written to temp_abnormal_p_03.txt
29 change transactions temp_change_abnormal_03.txt
    10 <ls n="P[.] #, #,">#.</ls>
    15 <ls n="P[.] #,">#, #.</ls>
     1 <ls n="P[.]">#, #, #. fgg.</ls>
    95 <ls n="P[.]">#, #, #.</ls>
   154 <ls>P[.] #, #, #. fgg.</ls>
    22 <ls>P[.] #, #, #. v. l.</ls>
 21094 <ls>P[.] #, #, #.</ls>
   251 <ls>P[.]</ls>
totals= 21642

# --------------------------------------------------------
Now begin to add markup for ca
------------------------------------------------

python make_change3_ls.py 'P.' temp_pwg_01.txt temp_change3_01.txt
38 changes not yet done. See tempdbg.txt
63 changes deferred
2449 records written to temp_change3_01.txt


# insert temp_change3_01.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
18151 change transactions from change_01.txt

Add changes from tempdbg
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
18195 change transactions from change_01.txt

Also
28 '<ls>BHĀG.</ls> <ls>P. -> <ls>BHĀG. P.'
 2 '<ls>BRAHMAVAIV.</ls> <ls>P. -> <ls>BRAHMAVAIV. P.'
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
18224 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'P.' temp_pwg_01.txt temp_change3_02.txt
2 changes not yet done. See tempdbg.txt
28 changes deferred
446 records written to temp_change3_02.txt

# insert temp_change3_02.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
18671 change transactions from change_01.txt

------------------------------------------------

python make_change3_ls.py 'P.' temp_pwg_01.txt temp_change3_03.txt
1 changes not yet done. See tempdbg.txt
12 changes deferred
166 records written to temp_change3_03.txt

#insert temp_change3_03 into change_01.
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
18838 change transactions from change_01.txt

------------------------------------------------

python make_change3_ls.py 'P.' temp_pwg_01.txt temp_change3_04.txt
0 changes not yet done. See tempdbg.txt
11 changes deferred
90 records written to temp_change3_04.txt

#insert temp_change3_04 into change_01.
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
18928 change transactions from change_01.txt

------------------------------------------------

python make_change3_ls.py 'P.' temp_pwg_01.txt temp_change3_05.txt
1 changes not yet done. See tempdbg.txt
8 changes deferred
58 records written to temp_change3_05.txt

#insert temp_change3_05 into change_01.
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
18987 change transactions from change_01.txt

------------------------------------------------

python make_change3_ls.py 'P.' temp_pwg_01.txt temp_change3_06.txt
0 changes not yet done. See tempdbg.txt
5 changes deferred
39 records written to temp_change3_06.txt

# insert temp_change3_06.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
19026 change transactions from change_01.txt

------------------------------------------------

python make_change3_ls.py 'P.' temp_pwg_01.txt temp_change3_07.txt
0 changes not yet done. See tempdbg.txt
3 changes deferred
22 records written to temp_change3_07.txt

# insert temp_change3_07.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
19048 change transactions from change_01.txt

------------------------------------------------

python make_change3_ls.py 'P.' temp_pwg_01.txt temp_change3_08.txt
0 changes not yet done. See tempdbg.txt
3 changes deferred
15 records written to temp_change3_08.txt

# insert temp_change3_08.txt into change_01.txt
; manual correction of one BHAG. P. 
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
19053 change transactions from change_01.txt

------------------------------------------------

python make_change3_ls.py 'P.' temp_pwg_01.txt temp_change3_09.txt
0 changes not yet done. See tempdbg.txt
2 changes deferred
9 records written to temp_change3_09.txt

# insert temp_change3_09.txt into change_01.txt
Corrected:
; <ls n="P. 3,">14, 27.</ls>   <L>115585<pc>7-1466<k1>svAtman
1095689  BHAG. P. problem removed in this line.  There are no <ls>P.</ls> here.

python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
19051 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'P.' temp_pwg_01.txt temp_change3_10.txt
0 changes not yet done. See tempdbg.txt
1 changes deferred
6 records written to temp_change3_10.txt

# insert temp_change3_10.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
10957 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'P.' temp_pwg_01.txt temp_change3_11.txt
0 changes not yet done. See tempdbg.txt
0 changes deferred
5 records written to temp_change3_11.txt

# insert temp_change3_11.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
19062 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'P.' temp_pwg_01.txt temp_change3_12.txt
0 changes not yet done. See tempdbg.txt
0 changes deferred
4 records written to temp_change3_12.txt

# insert temp_change3_12.txt into change_01.txt
# remove 31 transactions that have an error in handling of 'fg.'
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
19066 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'P.' temp_pwg_01.txt temp_change3_13.txt
0 changes not yet done. See tempdbg.txt
0 changes deferred
2 records written to temp_change3_13.txt

# insert temp_change3_13.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
19068 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'P.' temp_pwg_01.txt temp_change3_14.txt
0 changes not yet done. See tempdbg.txt
0 changes deferred
1 records written to temp_change3_14.txt


# insert temp_change3_14.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
19069 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'P.' temp_pwg_01.txt temp_change3_15.txt
0 changes not yet done. See tempdbg.txt
0 changes deferred
0 records written to temp_change3_15.txt

DONE!!

------------------------------------------------
Checks of change_abnormal.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
19125 about 70 new changes

# -------------------------------------------------------------
install temp_pwg_01.txt into csl-orig.
make corrections to change_01.txt

cp temp_pwg_01.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg ' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/p

------------------------------------------------
python listls3_abnormal.py 'P.' temp_pwg_01.txt abnormal_p_01.txt change_abnormal.txt
28 abnormal ls written to abnormal_p_01.txt
28 change transactions change_abnormal.txt
    17 <ls n="P[.] #, #,">#. fgg.</ls>
   994 <ls n="P[.] #, #,">#.</ls>
     2 <ls n="P[.] #,">#, #. fgg.</ls>
   467 <ls n="P[.] #,">#, #.</ls>
    14 <ls n="P[.]">#, #, #. fgg.</ls>
     2 <ls n="P[.]">#, #, #. v. l.</ls>
  1932 <ls n="P[.]">#, #, #.</ls>
   154 <ls>P[.] #, #, #. fgg.</ls>
    22 <ls>P[.] #, #, #. v. l.</ls>
 21068 <ls>P[.] #, #, #.</ls>
   212 <ls>P[.]</ls>
totals= 24884


python ../mbh1/lsextract_all.py temp_pwg_01.txt ../mbh1/pwg_tooltip.txt lsextract_pwg.txt
Before: 19829	P.	PĀṆINI'S acht Bücher grammatischer Regel
After : 24914	P.	PĀṆINI'S acht Bücher grammatischer Regel

# -------------------------------------------------------------
install temp_pwg_01.txt into csl-orig.

cp temp_pwg_01.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg ' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/p

# -------------------------------------------------------------


; -----------------------------------------------
misc text for copy/paste manual changes
</ls> <ls>
</ls> <ls n="P.">
</ls> <ls n="P.">
<ls n="P. ,">
<ls n="R.">
</ls> <ls n="P.">
</ls> <ls n="P.">
</ls> <ls n="P.">
</ls> <ls n="M.">

</ls> <ls n="P.">

<ls\([^>]*>[^<]*\)</ls> → LSBEG\1LSEND

\(\(<ls n="P..*?">.*?</ls>\)\|\(<ls>P..*?</ls>\)\) +\(\(<ls n="P..*?">.*?</ls>\)\|\(<ls>P..*?</ls>\)\)

\(\(\(<ls n="P.[^"]*">[^<]*</ls>\)\|\(<ls>P.[^<]*</ls>\)\) *\)\{2,99\}
