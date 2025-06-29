06-26-2025
amarakosha Colebrook 1808 edition
cd /e/pdfwork/amara_cole
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue154

--------------------------------------------------------
Initial pdf and index
From https://github.com/sanskrit-lexicon/PWG/issues/62#issuecomment-3004712126
amar.index.xlsx
Amarakosha (1808) Colebrooke.pdf
  This is digitized by Google, original from University of California.

TITLE: Dictionary of the Sanskrit Language by AmaraSinha
 With an English Interpretation, and Annotations,
 by H. T. Colebrooke,
 printed at Serampoor, 1808

--------------------------------------------------------
index_amar.tsv
 Google docs convert amar.index.xlsx  to index_amar.tsv
 This is a 'complete index' of all pages.
 This was edited to
 1. remove first (blank) line
 2. remove initial tab in each line
--------------------------------------------------------
index_orig.txt
For our link-target work, we include only pdfpages 29-421
---------------
index.txt will be the final form.  Initialize:
cp index_orig.txt index.txt
=======================================

Allow manual changes to index.txt

-------------------------------------
Format of index.txt

pdfpage	book	chapter 	section	fromv	tov	ipage
29	I	1	1	1	2	1
93	II	1	--	1	4a	65

Jim Changes to index.txt
old:
132	II	4	4	4	7(1)	104
133	II	4	4	7(2)	10a	105
new:
132	II	4	4	4	7a	104
133	II	4	4	7b	10a	105
-----
Three changes so 'next-page' in app1 will function properly
---
old: 65       I       1       5       19b     22a     37
new: 65       I       1       5       19b     21     37
---
old: 66       I       1       6       1       4a      38
new: 66       I       1       6       1       3      38
---
old: 394      III     4       28      14      18a     36
new: 394      III     4       28      14      17     36
======================================================
# get temporary local copy of dictionaries for checking
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt
Just pwg for now

cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt

======================================================
# adapt make_js_index.py
python make_js_index.py index.txt index.js

419 Page records read from index.txt
json data written to index.js
pagerecs passes check1_key
67 records written to bcs.txt
check_nextpage finds 0 problems


======================================================
AKother.txt  125 AK references with 'embedded' colebrook references

======================================================
preliminary checks with temp_pwg.txt


------------------------------------
<ls n="AK. 3,4,32 (28),">16.</ls>
<L>106247<pc>7-0757<k1>saMBAvya
394	III	4	28	14	17	366
ok
------------------------------------
<ls n="AK. 3,4,32 (COL. 28),">16.</ls>
<L>2818<pc>1-0206<k1>anunaya
394	III	4	28	14	17	366
ok
------------------------------------
<ls n="AK.">3,4,32 (COL. 28),5.</ls>
<L>2705<pc>1-0198<k1>anukampA
391	III	4	28	3b	6	363
ok
------------------------------------
<ls>AK. 3,3,38 (37).</ls>
<L>92764<pc>6-1150<k1>virati
314	III	3	--	37	40a	286
ok  virataya
------------------------------------
<ls>AK. 3,4,32 (28),10.</ls>
<L>97288<pc>7-0030<k1>SaNkA
392	III	4	28	7	10a	364
ok
------------------------------------
<ls>AK. 3,4,32 (COL. 28),1.</ls>
<L>7766<pc>1-0581<k1>A
390	III	4	28	1	3a	362
ok
------------------------------------
<ls>AK. 3,4,32 (COLEBR. 28),15.</ls>
<L>46024<pc>4-0783<k1>purA
394	III	4	28	14	17	366
ok
------------------------------------
<ls>AK. 3,4,32, [COL. 28,] 10.</ls>
<L>4120<pc>1-0303<k1>api
392	III	4	28	7	10a	364

------------------------------------
------------------------------------
------------------------------------
============================================================
Misc. other references to be changed

2 matches for "<ls>COL. [0-9]" in buffer: temp_pwg.txt
  22570:<ls>AK. 3,3,42.</ls> [<ls>COL. 41.</ls>])
  54334:<ls>AK. 3,3,39.</ls>, (<ls>COL. 38</ls>,) <ls>Sch.</ls>

5 matches for "<ls>COLEBR. [0-9]" in buffer: temp_pwg.txt
  26435:<ls>AK. 3,3,40.</ls> (<ls>COLEBR. 39.</ls>) {#adanta#} {%auf ein kurzes a auslautend%}
 114124:<ls>AK. 3,3,39</ls> (<ls>COLEBR. 38).</ls>
 282541:<ls>AK. 3,4,32</ls> (<ls>COLEBR. 28),12.</ls> {#tarkayukta#} viell. {%in blossem Verdacht stehend%}
 357558:<ls>AK. 3,4,32</ls> (<ls>COLEBR. 28),2.</ls> <ls>H. an. 7,9.</ls> <ls>MED. avy. 11.</ls> {#DikSabdapatitaScEva jIvite tasya kA dayA#}
 374819:<ls>AK. 3,4,32</ls> (<ls>COLEBR. 28),9.</ls> <ls>H. an. 7,32.</ls> <ls>MED. avy. 45.</ls> {#nAnA\ hi tvA\ hava^mAnA\ janA^ i\me#}

========================================
prepare transformed string.
There is considerable regularity to the changes needed to expose Colebrook refs.
python prepare_change.py AKother.txt Akother1.txt
78 unique strings found
47 duplicates noticed

# apply the replacements of Akother1.txt to temp_pwg.txt
# result is temp_pwg1.txt
python replace.py temp_pwg.txt Akother1.txt temp_pwg1.txt

# install pwg1, regenerate local displays
cp temp_pwg1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt

cd /c/xampp/htdocs/cologne/csl-pywork/v02/
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok

# make change file
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue154
python diff_to_changes_dict.py temp_pwg.txt temp_pwg1.txt change_pwg_pwg1.txt
126 changes written to change_pwg_pwg1.txt

----------------------------------------
regenerate lsexamine files in issue94
cd ../issue94
sh redo_lsexamine.sh


----------------------------------------
Three ls tags 
COL. 
AK. ed. COLEBR. 
COLEBR.


----------------------------------------
check all variations  for pagerec not found.

4 numeric parameters
python generate_random.py ALL pwg4a temp_pwg1.txt index.txt check_pwg4a_ALL.txt check_pwg4a_ALL_nopagerec.txt

regex_raw = <ls>COL. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)
found 92 instances in kosha
found 22 distinct in kosha
write_examples: 92 written to check_pwg4a_ALL.txt
4 instances of 'pagerec not found'
write_examples: 4 written to check_pwg4a_ALL_nopagerec.txt

This will uncover additional changes to kosha
cp temp_pwg1.txt temp_pwg2.txt
Manual changes to temp_pwg2.txt

# make changes to temp_pwg2.txt
# rerun with pwg2
python generate_random.py ALL pwg4a temp_pwg2.txt index.txt check_pwg4a_ALL_1.txt check_pwg4a_ALL_1_nopagerec.txt

0 instances of 'pagerec not found'

--------------------------
pwg3a COL. with 3 parms

python generate_random.py ALL pwg3a temp_pwg2.txt index.txt check_pwg3a_ALL.txt check_pwg3a_ALL_nopagerec.txt

regex_raw = <ls>COL. ([0-9]+),([0-9]+),([0-9]+)[^0-9,]
found 8 instances in kosha
found 4 distinct in kosha
write_examples: 8 written to check_pwg3a_ALL.txt
0 instances of 'pagerec not found'

--------------------------
pwg4b COLEBR. with 4 parms

python generate_random.py ALL pwg4b temp_pwg2.txt index.txt check_pwg4b_ALL.txt check_pwg4b_ALL_nopagerec.txt

regex_raw = <ls>COLEBR. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)
found 26 instances in kosha
found 11 distinct in kosha
write_examples: 26 written to check_pwg4b_ALL.txt
0 instances of 'pagerec not found'

--------------------------
pwg4b COLEBR. with 3 parms

python generate_random.py ALL pwg3b temp_pwg2.txt index.txt check_pwg3b_ALL.txt check_pwg3b_ALL_nopagerec.txt

regex_raw = <ls>COLEBR. ([0-9]+),([0-9]+),([0-9]+)[^0-9,]
found 3 instances in kosha
found 3 distinct in kosha
write_examples: 3 written to check_pwg3b_ALL.txt
0 instances of 'pagerec not found'

--------------------------
pwg4c AK. ed. COLEBR. with 4 parms

python generate_random.py ALL pwg4c temp_pwg2.txt index.txt check_pwg4c_ALL.txt check_pwg4c_ALL_nopagerec.txt

regex_raw = <ls>AK. ed. COLEBR. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)
found 1 instances in kosha
found 1 distinct in kosha
write_examples: 1 written to check_pwg4c_ALL.txt
0 instances of 'pagerec not found'

--------------------------
pwg3c AK. ed. COLEBR. with 3 parms

python generate_random.py ALL pwg3c temp_pwg2.txt index.txt check_pwg3c_ALL.txt check_pwg3c_ALL_nopagerec.txt

regex_raw = <ls>AK. ed. COLEBR. ([0-9]+),([0-9]+),([0-9]+)[^0-9,]
found 2 instances in kosha
found 2 distinct in kosha
write_examples: 2 written to check_pwg3c_ALL.txt
0 instances of 'pagerec not found'

python generate_random.py ALL pwg3 temp_pwg1.txt index.txt check_pwg3_ALL_1.txt check_pwg3_ALL_1_nopagerec.txt

0 instances of 'pagerec not found'


===================================================

#generate change file for pwg2
python diff_to_changes_dict.py  temp_pwg1.txt temp_pwg2.txt change_pwg1_pwg2.txt

4 changes written to change_pwg1_pwg2.txt

# install temp_pwg2.txt  to csl-orig

cp temp_pwg2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt

cd /c/xampp/htdocs/cologne/csl-pywork/v02/
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok
----------------------------------------
regenerate lsexamine files in issue94
cd ../issue94
sh redo_lsexamine.sh

----------------------------------

----------------------------------

prepare printchanges records for csl-corrections pwg_printchange.txt

python prepare_printchange.py temp_pwg.txt Akother1.txt pwg_printchange.txt

manual adjust pwg_printchange.txt
----
Remove non-printchange lines:
10779 : uta : <ls n="AK.">3,5,2 5.</ls> : <ls n="AK.">3,5,2</ls> <ls n="AK. 3,5,">5.</ls>
48877 : pratyaYc : <ls n="AK.">II. 167.</ls> : <ls>H. 167.</ls>
55695 : BfS : <ls>AK. 2,8,2</ls>, <ls n="AK.">67.H. 366.</ls> : <ls>AK. 2,8,2,67.</ls> <ls>H. 366.</ls>
----
4 changed as per check_pwg4a_ALL_nopagerec.txt

==================================

app1  see readme_app1.txt

==================================
basicadjust.php  csl-websanlexicon
Three ls tags for pwg
COL. 
AK. ed. COLEBR. 
COLEBR.

cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
sh generate_web.sh pwg  ../../pwg
sh apidev_copy.sh


==================================
sync local repos to github
csl-orig
csl-websanlexicon
csl-apidev

==================================
sync github to cologne
csl-orig, csl-websanlexicon, csl-apidev

regenerate displays at cologne
----------------------------------
sync csl-corrections

=================================
sync  issue154
