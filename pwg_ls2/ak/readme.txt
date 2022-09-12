PWG/pwg_ls2/ak

markup improvement.

AK. = AMARAKOṢA nach der Ausgabe von COLEBROOKE und LOISELEUR&#13;&#10;DESLONGCHAMPS (GILD. Bibl. 251. 253).

cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pwg/pywork/pwgauth/pwgbib_input.txt temp_bib.txt

Also, http://amara.aupasana.com/sloka?sloka_number=1.1.53
Links added in basicadjust
http://amara.aupasana.com/search?term=purocita
   (itrans or devanagari)
1. https://archive.org/details/ColebrookeAmarakosha1891_201809/page/n37/mode/2up
 Other versions of Colebrooke, 3rd ed.
1a. https://idoc.pub/documents/amarakosha-sanskrit-dictionary-colebrooke-1891-3rded-19n08k85954v
  (downloaded - somewhat clearer than 1.)
2. https://sanskritdocuments.org/sanskrit/amarakosha/

----------------------------------------------------------
The numbering is similar between aupasana and Colebrooke,
but slightly different.
Colebrook's 1.1.42  corresponds to sloka_number=1.1.46

------------------
but some references seem incomparable
e.g. under <L>166<pc>1-0013<k1>akza,
  <ls>AK. 2, 10, 45. 3, 4, 224.</ls>   There is no sloka 3,4,224 in aupasana.
  Also, 'akza' is not found in Colebrooke at 3,4,224.

------------------
<L>15593<pc>2-0148<k1>karzaka
<ls>AK. 2, 9, 6. 3, 4, 28, 217.</ls>
In Colebrooke, 217 is found in Book #, Chap. 4, Section 24.
--------------------------------------------------------------
Start with a copy of csl-orig/v02/pwg/pwg.txt at commit
  dc533ea2d59092faae2536f23b3da23fb960e43e
  
# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_pwg_0.txt in this spruch directory
  git show dc533ea2:v02/pwg/pwg.txt > /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/ak/temp_pwg_0.txt
# return to this mbh directory
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/ak/
===============================================================
14471 matches in 14460 lines for "<ls>AK\."
The 'standard form' for a specific reference has 4 numeric parameters
e.g. <ls>AK. 1, 1, 2, 34.</ls>
7130 matches for "<ls>AK\. [0-9]+, [0-9]+, [0-9]+, [0-9]+\.?</ls>"
# Some have just 3 parameters
4418 matches in 4416 lines for "<ls>AK\. [0-9]+, [0-9]+, [0-9]+\.?</ls>"
1 match for "<ls>AK\. [0-9]+, [0-9]+\.?</ls>"
1 match for "<ls>AK\. [0-9]+\.?</ls>"
1125 matches in 1123 lines for "<ls>AK\.</ls>"
  example: <ls>RAMĀN.</ls> zu <ls>AK.</ls> im <ls>ŚKDR.</ls>
5 or more numbers
1198 matches for "<ls>AK\.\( [0-9]+[,.]\)\{5,\}"

(+ 7130 4418 1125 1198) 13871
(- 14471 13871) = 600 of some other type.

Some end with <ab>v.l.</ab>, and perhaps

There also may be some <ls>#</ls>  (without the AK.)
======================================================

python lsextract_all.py temp_pwg_0.txt temp_bib.txt lsextract_pwg_0.txt
717763	ALL	As of 2022-08-29
32354	NUMBER	ls starts with number
02085	UNKNOWN	ls is unknown
14467	AK.	AMARAKOṢA

-----------------------------------------------------
python classify.py temp_pwg_0.txt temp_classify_0_done.txt temp_classify_0_todo.txt

159 parameter types found
12726 instances in 8 categories written to temp_classify_0_done.txt
1745 instances in 151 categories written to temp_classify_0_todo.txt

-----------------------------------------------------
cp temp_pwg_0.txt temp_pwg_1.txt
touch change_1.txt

python make_change.py 0 temp_pwg_1.txt temp_bib.txt temp_change_1.txt
186 have some irregularity.  Ignore these for now.
Note 1:  Allow ending to contain 'v\. ?l\.' or 'fgg?\.'
Note 2: Many parenthetical numbers, not sure how to code.

-----------------------------------------------------:
<ls>AK.)</ls> and similar

python make_change.py 1a temp_pwg_1.txt temp_bib.txt temp_change_1a.txt
4 lines in temp_change_1a.txt
# manual correction
# insert temp_change_1a.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
4 change transactions from temp_change_1a.txt

-----------------------------------------------------:
<ls>AK. X...</ls>  X not a digit

python make_change.py 1b temp_pwg_1.txt temp_bib.txt temp_change_1b.txt
11 lines in temp_change_1b.txt
# manual correction
# insert temp_change_1b.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
8 change transactions from temp_change_1b.txt

NOTE:
1. Some remain unsolved.
  <ls>AK. (1, 1, 7, 6. 7)</ls>
  'AK. ed. COLEBR.' 3
  <ls>AK. S. IX.</ls>
-----------------------------------------------------
missing spaces between numbers:
<ls>AK. 2,7,18.</ls> -> <ls>AK. 2, 7, 18.</ls>

python make_change.py 1c temp_pwg_1.txt temp_bib.txt temp_change_1c.txt
290 lines in temp_change_1c.txt
# insert temp_change_1c.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
298 change transactions from change_1.txt

-----------------------------------------------------
ady. -> adj.  (Usual PWG confusion between 'j' and 'y'.)
This applies to all records of PWG, not just AK references

python make_change.py 1d temp_pwg_1.txt temp_bib.txt temp_change_1d.txt
36 lines in temp_change_1d.txt
# manual adjustment
# insert temp_change_1d.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
338 change transactions from change_1.txt

NOTE:  There are a couple like <ls>MED. ady. N</ls>
  Not sure.  Think 'ady.' is like a section heading. Not changed.

-----------------------------------------------------

python classify.py temp_pwg_1.txt temp_classify_1_done.txt temp_classify_1_todo.txt
140 parameter types found
12990 instances in 8 categories written to temp_classify_1_done.txt
1481 instances in 132 categories written to temp_classify_1_todo.txt

BEGIN Parameter refactoring
-----------------------------------------------------
<ls>AK. N, N, N, N. N, N, N, N.</ls> ->
<ls>AK. N, N, N, N.</ls> <ls n="AK.">N, N, N, N.</ls>

python make_change.py 1e temp_pwg_1.txt temp_bib.txt temp_change_1e.txt
459 lines in temp_change_1e.txt
# insert temp_change_1e.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
797 change transactions from change_1.txt

-----------------------------------------------------
<ls>AK. N, N, N. N, N, N, N.</ls> ->
<ls>AK. N, N, N.</ls> <ls n="AK.">N, N, N, N.</ls>

python make_change.py 1f temp_pwg_1.txt temp_bib.txt temp_change_1f.txt
246 lines in temp_change_1f.txt
# insert temp_change_1f.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1043 change transactions from change_1.txt

-----------------------------------------------------
<ls>AK. N, N, N. N, N, N.</ls> ->
<ls>AK. N, N, N.</ls> <ls n="AK.">N, N, N.</ls>

python make_change.py 1g temp_pwg_1.txt temp_bib.txt temp_change_1g.txt
47 lines in temp_change_1g.txt
# insert temp_change_1g.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1090 change transactions from change_1.txt

-----------------------------------------------------
<ls>AK. N, N, N, N. N, N, N.</ls> ->
<ls>AK. N, N, N, N.</ls> <ls n="AK.">N, N, N.</ls>

python make_change.py 1h temp_pwg_1.txt temp_bib.txt temp_change_1h.txt
88 lines in temp_change_1h.txt
# insert temp_change_1h.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1178 change transactions from change_1.txt

-----------------------------------------------------
<ls>AK. N1, N2, N3, N4. N5, N6.</ls> ->
<ls>AK. N1, N2, N3, N4.</ls> <ls n="AK. N1, N2,">N5, N6.</ls>

<ls>AK. 2, 8, 1, 10. 2, 63.</ls>           <L>5658<pc>1-0411<k1>ari
Both verses 2, 8, 1, 10. and 2, 8, 2, 63. refer to 'ari'

python make_change.py 1i temp_pwg_1.txt temp_bib.txt temp_change_1i.txt
87 lines in temp_change_1i.txt
# insert temp_change_1i.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1265 change transactions from change_1.txt

NOTE:  Using the 3rd edition (1891) of Colebrook:
  <L>47817<pc>4-0916<k1>pragraha
  <ls>AK. 3, 4, 23, 140. 29, 221.</ls>
  Book III, Chapter IV, Sect. XXIII starts with number 208
    i.e., there is no 140!
  Also, the last section in Book III, CHapter IV is XXXVIII (28).
  So, there is no Section 29!
HOWEVER:  There is a verse 221, which happens to be in
  section XXV (25). And this verse has 'pragraha'
  Also, there is mention of pragraha in verse 140 which occurs in section 19.
THUS: in this example, the section number IS IRRELEVANT!


-----------------------------------------------------
<ls>AK. N1, N2, N3. N4.</ls> ->
<ls>AK. N1, N2, N3.</ls> <ls n="AK. N1, N2,">N4.</ls>


python make_change.py 1j temp_pwg_1.txt temp_bib.txt temp_change_1j.txt
62 lines in temp_change_1j.txt
# insert temp_change_1j.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1327 change transactions from change_1.txt

-----------------------------------------------------
<ls>AK. N1, N2, N3, N4. N5.</ls> ->
<ls>AK. N1, N2, N3, N4.</ls> <ls n="AK. N1, N2, N3,">N5.</ls>


python make_change.py 1k temp_pwg_1.txt temp_bib.txt temp_change_1k.txt
52 lines in temp_change_1k.txt
# insert temp_change_1k.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1379 change transactions from change_1.txt

-----------------------------------------------------
<ls>AK. N1, N2, N3, N4. N5, N6, N7, N8. N9, N10.</ls> ->
<ls>AK. N1, N2, N3, N4.</ls> <ls n="AK.">N5, N6, N7, N8.</ls> <ls n="AK. N5, N6,">N9, N10.</ls>

python make_change.py 1l temp_pwg_1.txt temp_bib.txt temp_change_1l.txt
36 lines in temp_change_1l.txt
# insert temp_change_1l.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1415 change transactions from change_1.txt

-----------------------------------------------------
<ls>AK. N1, N2, N3. N4, N5.</ls> ->
<ls>AK. N1, N2, N3.</ls> <ls n="AK. N1,">N4, N5.</ls>

python make_change.py 1m temp_pwg_1.txt temp_bib.txt temp_change_1m.txt
31 lines in temp_change_1m.txt
# insert temp_change_1m.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1446 change transactions from change_1.txt

PROBLEM:
<ls>AK. 3, 1, 51. 4, 32.</ls>              <L>1176<pc>1-0086<k1>aRqaja
Can file aRqaja in 3,1,51. BUT cannot find aRqaja in 3,4,32 ?? NOT SURE
  poor print, possibly viprARqajA.

-----------------------------------------------------
<ls>AK. N1, N2, N3,</ls> 
 These are errors in markup to correct

python make_change.py 1n temp_pwg_1.txt temp_bib.txt temp_change_1n.txt
21 lines in temp_change_1n.txt
# manually correct markup in temp_change_1n.txt
# insert temp_change_1n.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1467 change transactions from change_1.txt

Note: Example: <ls>AK. 3, 4, 32, (COL. 28,) 15.</ls>
  The 'COL. 28' is probably from the 1891 edition.
  Don't currently have pdf of the edition that shows '3, 4, 32'.

-----------------------------------------------------
<ls>AK. N1, N2, N3. N4, N5, N6, N7. N8, N9.</ls> ->
<ls>AK. N1, N2, N3.</ls> <ls n="AK.">N4, N5, N6, N7.</ls>
   <ls n="AK. N4, N5,">N8, N9.</ls>

python make_change.py 1o temp_pwg_1.txt temp_bib.txt temp_change_1o.txt
20 lines in temp_change_1o.txt
# insert temp_change_1o.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1487 change transactions from change_1.txt

-----------------------------------------------------
<ls>AK. N1. N2, N3, N4.</ls> -> <ls>AK. N1, N2, N3, N4.</ls>
consider these to be typographical (not print) errors.
Have confirmed <ls>AK. 2. 6, 1, 12.</ls>  -> <ls>AK. 2, 6, 1, 12.</ls>
 for <L>36772<pc>3-0966<k1>DImant

python make_change.py 1p temp_pwg_1.txt temp_bib.txt temp_change_1p.txt
17 lines in temp_change_1p.txt
# insert temp_change_1p.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1504 change transactions from change_1.txt

-----------------------------------------------------
<ls>AK. N1, N2. N3, N4.</ls> -> <ls>AK. N1, N2, N3, N4.</ls>
consider these to be typographical (not print) errors.
Confirmed: <ls>AK. 2, 4. 2, 13.</ls> -> <ls>AK. 2, 4, 2, 13.</ls>
  for <L>22348<pc>2-0740<k1>gAlava

python make_change.py 1q temp_pwg_1.txt temp_bib.txt temp_change_1q.txt
15 lines in temp_change_1q.txt
# insert temp_change_1q.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1519 change transactions from change_1.txt

-----------------------------------------------------
<ls>AK. N1, N2. N3.</ls> -> <ls>AK. N1, N2, N3.</ls>
consider these to be typographical (not print) errors.
Confirmed: <ls>AK. 2, 10. 22.</ls> -> <ls>AK. 2, 10, 22.</ls>
  for <L>17450<pc>2-0306<k1>kukkura

python make_change.py 1r temp_pwg_1.txt temp_bib.txt temp_change_1r.txt
11 lines in temp_change_1r.txt
# insert temp_change_1r.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1530 change transactions from change_1.txt

-----------------------------------------------------
<ls>AK. N1, N2, N3, N4. N5, N6, N7. N8, N9, N10, N11.</ls> ->
<ls>AK. N1, N2. N3, N4</ls> <ls n="AK. N1,">N5, N6, N7.</ls>
  <ls n="AK.">N8, N9, N10, N11.</ls>
  
Confirmed: <ls>AK. 1, 1, 1, 63. 2, 2, 4. 3, 6, 8, 44.</ls> ->
  <ls>AK. 1, 1, 1, 63.</ls> <ls n="AK. 1,">2, 2, 4.</ls>
  <ls n="AK.">2, 2, 4.</ls> 
  for <L>22278<pc>2-0735<k1>gAmin

python make_change.py 1s temp_pwg_1.txt temp_bib.txt temp_change_1s.txt
9 lines in temp_change_1s.txt
# insert temp_change_1s.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1539 change transactions from change_1.txt

-----------------------------------------------------
<ls>AK. N1, N2, N3. N4. N5, N6, N7, N8.</ls> ->
<ls>AK. N1, N2, N3, N4</ls> <ls n="AK.">N5, N6, N7, N8.</ls>
  
Confirmed: 
python make_change.py 1t temp_pwg_1.txt temp_bib.txt temp_change_1t.txt
 lines in temp_change_1t.txt
# insert temp_change_1t.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
 change transactions from change_1.txt

-----------------------------------------------------

python classify.py temp_pwg_1.txt temp_classify_1_done.txt temp_classify_1_todo.txt
129 parameter types found
15347 instances in 8 categories written to temp_classify_1_done.txt
310 instances in 121 categories written to temp_classify_1_todo.txt

-----------------------------------------------------

python check_parms.py temp_pwg_1.txt temp_check_parms_1.txt

compare with ak_index.txt to search for errors.
temp_checkparms_1.txt has the items of difference (where PWG references
in Cologne digitization are outside the range of possibilities according
to the Colebrooke 1891 version of AK.

Construct prototype change_transactions for the items in temp_checkparms_1.txt.

python ak_index_verses.py ak_index.txt ak_index_verses_set.py
# all possible verses, expressed as a python set named
# 'ak_index_verses_set'.
# either a 3-tuple of cardinal numbers or a 4-tuple.

python ak_verse_change.py 1 temp_pwg_1.txt temp_checkparms_1.txt
# uses ak_index_verses_set.py.
# Consistent with check_parms.py

There are many systematic differences. (~ 2000).

------------------------------------------------------------
temp_checkparms_1s_extra
A few changes gleaned from preliminary study of temp_checkparms_1.txt
# insert temp_checkparms_1s_extra into change_1
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1547 change transactions from change_1.txt

------------------------------------------------------------
unmatched verses, within <ls n="AK.X">Y</ls>
Also, require X+Y NOT to start with "3, 4,"
  Reason. There are MANY mismatches of "3, 4, i, j",
python ak_verse_change.py 2 temp_pwg_1.txt temp_checkparms_1_2.txt
38 records written to temp_checkparms_1_2.txt
# manually examine temp_checkparms_1_2.txt
#  insert temp_checkparms_1_2.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1570 change transactions from change_1.txt

Note 1: (3, 6, 25) (PWG) == (3, 6, 3, 25) (AK Colebrooke)
  ? and similarly with (3, 6, X) ? I.e. the 'section' is not mentioned
  in PWG references to (3, 6, X) = ? (3, 6, S, X)
Note 2: (4, 18, 130) PWG.  There is no Book 4 in Colebrooke!

------------------------------------------------------------

python classify.py temp_pwg_1.txt temp_classify_1_done.txt temp_classify_1_todo.txt
301 instances in 120 categories written to temp_classify_1_todo.txt

------------------------------------------------------------
; N, N, N. N. N, N, N, N. (7)
python make_change.py 1t temp_pwg_1.txt temp_bib.txt temp_change_1t.txt
7 lines in temp_change_1t.txt
# manual adjustment
# insert temp_change_1t.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1577 change transactions from change_1.txt

------------------------------------------------------------
; N, N, N, N. N, N. N, N. (7)
python make_change.py 1u temp_pwg_1.txt temp_bib.txt temp_change_1u.txt
7 lines in temp_change_1u.txt
# manual adjustment
# insert temp_change_1u.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1584 change transactions from change_1.txt

------------------------------------------------------------
; N, N, N. N, N, N. N.
python make_change.py 1v temp_pwg_1.txt temp_bib.txt temp_change_1v.txt
6 lines in temp_change_1v.txt
# manual adjustment
# insert temp_change_1v.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1590 change transactions from change_1.txt

------------------------------------------------------------
; N, N, N, N. N, N, N. N. (6)
python make_change.py 1w temp_pwg_1.txt temp_bib.txt temp_change_1w.txt
6 lines in temp_change_1w.txt
# manual adjustment
# insert temp_change_1w.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1596 change transactions from change_1.txt

------------------------------------------------------------
; N, N, N, N. N, N, N, N. N, N, N. (6)

python make_change.py 1x temp_pwg_1.txt temp_bib.txt temp_change_1x.txt
6 lines in temp_change_1x.txt
# manual adjustment
# insert temp_change_1x.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1602 change transactions from change_1.txt

------------------------------------------------------------
; N, N, N, N. N, N, N. N, N, N, N. N, N. (6)

python make_change.py 1y temp_pwg_1.txt temp_bib.txt temp_change_1y.txt
6 lines in temp_change_1y.txt
# manual adjustment
# insert temp_change_1y.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1608 change transactions from change_1.txt

------------------------------------------------------------
; N, N, N, N. N, N, N, N. N, N. N, N. (6)

python make_change.py 1z temp_pwg_1.txt temp_bib.txt temp_change_1z.txt
 lines in temp_change_1z.txt
# manual adjustment
# insert temp_change_1z.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1614 change transactions from change_1.txt

------------------------------------------------------------
; N, N, N ? N. N, N, N. (6)  ? = (28),

python make_change.py 2a temp_pwg_1.txt temp_bib.txt temp_change_2a.txt
 lines in temp_change_2a.txt
# manual adjustment
# insert temp_change_2a.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1620 change transactions from change_1.txt

------------------------------------------------------------
;  N. N, N. (6)

python make_change.py 2b temp_pwg_1.txt temp_bib.txt temp_change_2b.txt
6 lines in temp_change_2b.txt
# manual adjustment
# insert temp_change_2b.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1626 change transactions from change_1.txt

------------------------------------------------------------
; N, N, N. N, N. N.

python make_change.py 2c temp_pwg_1.txt temp_bib.txt temp_change_2c.txt
5 lines in temp_change_2c.txt
# manual adjustment
# insert temp_change_2c.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1631 change transactions from change_1.txt

------------------------------------------------------------
; N, N, N. N (4)

python make_change.py 2d temp_pwg_1.txt temp_bib.txt temp_change_2d.txt
4 lines in temp_change_2d.txt
# manual adjustment
# insert temp_change_2d.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1635 change transactions from change_1.txt

------------------------------------------------------------
; N, N, N, N. ? (4)

python make_change.py 2f temp_pwg_1.txt temp_bib.txt temp_change_2f.txt
4 lines in temp_change_2f.txt
# manual adjustment
# insert temp_change_2f.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1639 change transactions from change_1.txt

------------------------------------------------------------
; N, N, N, N. N, N, N (4)

python make_change.py 2f temp_pwg_1.txt temp_bib.txt temp_change_2f.txt
4 lines in temp_change_2f.txt
# manual adjustment
# insert temp_change_2f.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1643 change transactions from change_1.txt

------------------------------------------------------------
28 COLEBR
need to be coded consistently

python make_change.py 2g temp_pwg_1.txt temp_bib.txt temp_change_2g.txt
2 lines in temp_change_2g.txt
# manual adjustment
# insert temp_change_2g.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1645 change transactions from change_1.txt

------------------------------------------------------------
N, N, N, N. N, N. N, N, N. (4)

python make_change.py 2h temp_pwg_1.txt temp_bib.txt temp_change_2h.txt
4 lines in temp_change_2h.txt
# manual adjustment
# insert temp_change_2h.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1649 change transactions from change_1.txt

------------------------------------------------------------
 N, N, N, N. N (4)

python make_change.py 2i temp_pwg_1.txt temp_bib.txt temp_change_2i.txt
4 lines in temp_change_2i.txt
# manual adjustment
# insert temp_change_2i.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1653 change transactions from change_1.txt

------------------------------------------------------------
 N, N. N. N. (4)

python make_change.py 2j temp_pwg_1.txt temp_bib.txt temp_change_2j.txt
4 lines in temp_change_2j.txt
# manual adjustment
# insert temp_change_2j.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1657 change transactions from change_1.txt

------------------------------------------------------------
 (COLEBR\.  Still some need re-arranging

python make_change.py 2k temp_pwg_1.txt temp_bib.txt temp_change_2k.txt
20 lines in temp_change_2k.txt
# manual adjustment. Several are unchanged, only 10 are changed
# insert temp_change_2k.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1667 change transactions from change_1.txt

------------------------------------------------------------
; N, N, N.  N, N, N, N.  N, N.  N, N. (4)

python make_change.py 2l temp_pwg_1.txt temp_bib.txt temp_change_2l.txt
4 lines in temp_change_2l.txt
# manual adjustment. 
# insert temp_change_2l.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1671 change transactions from change_1.txt

------------------------------------------------------------
; N, N, N, N. N. N, N, N, N. (3) 

python make_change.py 2m temp_pwg_1.txt temp_bib.txt temp_change_2m.txt
3 lines in temp_change_2m.txt
# manual adjustment. 
# insert temp_change_2m.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1674 change transactions from change_1.txt

------------------------------------------------------------
; N, N, N. N, N, N, N (3)
add period

python make_change.py 2n temp_pwg_1.txt temp_bib.txt temp_change_2n.txt
3 lines in temp_change_2n.txt
# manual adjustment. 
# insert temp_change_2n.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1677 change transactions from change_1.txt

------------------------------------------------------------
; N, N, N, N.  N, N.  N, N, N, N. (3)

python make_change.py 2o temp_pwg_1.txt temp_bib.txt temp_change_2o.txt
3 lines in temp_change_2o.txt
# manual adjustment. 
# insert temp_change_2o.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1680 change transactions from change_1.txt

------------------------------------------------------------
; N, N, N, N. N, N, N, N. N, N, N, N. (3)

python make_change.py 2p temp_pwg_1.txt temp_bib.txt temp_change_2p.txt
3 lines in temp_change_2p.txt
# manual adjustment. 
# insert temp_change_2p.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1683 change transactions from change_1.txt

------------------------------------------------------------
; N, N, N. N, N, N. N, N, N, N. (3)
various markup

python make_change.py 2q temp_pwg_1.txt temp_bib.txt temp_change_2q.txt
3 lines in temp_change_2q.txt
# manual adjustment. 
# insert temp_change_2q.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1686 change transactions from change_1.txt

------------------------------------------------------------
; <ls>AK. (

python make_change.py 2r temp_pwg_1.txt temp_bib.txt temp_change_2r.txt
3 lines in temp_change_2r.txt
# manual adjustment. 
# insert temp_change_2r.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1689 change transactions from change_1.txt

------------------------------------------------------------
; N, N, N. N, N. N, N. (2)

python make_change.py 2s temp_pwg_1.txt temp_bib.txt temp_change_2s.txt
2 lines in temp_change_2s.txt
# manual adjustment. 
# insert temp_change_2s.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1691 change transactions from change_1.txt

------------------------------------------------------------
; N, N, N N. (2)

python make_change.py 2t temp_pwg_1.txt temp_bib.txt temp_change_2t.txt
2 lines in temp_change_2t.txt
# manual adjustment. 
# insert temp_change_2t.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1693 change transactions from change_1.txt

------------------------------------------------------------
; N, N, N, N. N, N, N. N. N. (2)

python make_change.py 2u temp_pwg_1.txt temp_bib.txt temp_change_2u.txt
2 lines in temp_change_2u.txt
# manual adjustment. 
# insert temp_change_2u.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1695 change transactions from change_1.txt

------------------------------------------------------------
; N, N, N, N. N, N, N. N, N. (2)

python make_change.py 2v temp_pwg_1.txt temp_bib.txt temp_change_2v.txt
2 lines in temp_change_2v.txt
# manual adjustment. 
# insert temp_change_2v.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1697 change transactions from change_1.txt

------------------------------------------------------------
; Handle the rest of the cases from temp_classify_1_todo.txt

python make_change.py 2w temp_pwg_1.txt temp_bib.txt temp_change_2w.txt
98 lines in temp_change_2w.txt
# manual adjustment. 
# insert temp_change_2w.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1792 change transactions from change_1.txt

print changes:
1.
;<L>20142<pc>2-0530<k1>kzantar
190914 old <ls>AK. 3. 1. 3, 1.</ls> 
190914 new <ls>AK. 3. 1. 31.</ls> 
2.
;<L>42207<pc>4-0463<k1>padya
420991 old <ls>AK. 2, 16.</ls> 
420991 new <ls>AK. 2, 1, 15.</ls> 


------------------------------------------------------------
python classify.py temp_pwg_1.txt temp_classify_1_done.txt temp_classify_1_todo.txt
25 parameter types found
15899 instances in 8 categories written to temp_classify_1_done.txt
130 instances in 17 categories written to temp_classify_1_todo.txt

A few misc changes ('temp_change_2w_extra' in change_1.txt)
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1798 change transactions from change_1.txt
--------------------------------------------------
------------------------------------------------------------
; 32, (COL. 28,) -> 32 (COL. 28),  and also COLEBR.
These may be (minor) print changes, made for consistency

python make_change.py 2x temp_pwg_1.txt temp_bib.txt temp_change_2x.txt
11 lines in temp_change_2x.txt
# manual adjustment. 
# insert temp_change_2x.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
1810 change transactions from change_1.txt

--------------------------------------------------
python classify.py temp_pwg_1.txt temp_classify_1_done.txt temp_classify_1_todo.txt
14 parameter types found
15909 instances in 8 categories written to temp_classify_1_done.txt
125 instances in 6 categories written to temp_classify_1_todo.txt

------------------------------------------------------------
python check_parms.py temp_pwg_1.txt temp_check_parms_1_rev1.txt
------------------------------------------------------------
option = 1: all differences, including those that are symptomatic
For instance: (3, 4, ....
option = 2: Exclude systematic differences

 
python ak_verse_change.py 1 temp_pwg_1.txt temp_checkparms_1_opt1.txt
14 parameter types found
1801 keys found
2135 records written to temp_checkparms_1_opt1.txt

python ak_verse_change.py 2 temp_pwg_1.txt temp_checkparms_1_opt2.txt
25 records written to temp_checkparms_1_opt2.txt
# manual update most are unchanged
# insert  temp_checkparms_1_opt2.txt into change_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt

python ak_verse_change.py 2 temp_pwg_1.txt temp_checkparms_1_opt2a.txt
14 parameter types found
1793 keys found
17 records written to temp_checkparms_1_opt2a.txt

------------------------------------------------------------
# cp ak_verse_change.py ak_verse_list.py
python ak_verse_list.py temp_pwg_1.txt temp_ak_verse_list.txt

---------------------------------------------------------------------------
install  temp_pwg_1.txt to check xml
cp temp_pwg_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg ' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/ak/

------------------------------------------------------------
python lsextract_all.py temp_pwg_1.txt temp_bib.txt lsextract_pwg_1.txt
------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
https://archive.org/details/amarakochaouvoca01amaruoft/
LOISELEUR DESLONGCHAMPS
 This may be the 'nach der Ausgabe von COLEBROOKE und LOISELEUR' mentioned
 as the source for 'AK.'
VOCABULAIRE D'AMARASINHA, A. LOISELEUR DESLONGCHAMPS,
 PREMIERE PARTIE,
 M DCCC XXXIX (1839)

ak_index_ld.txt  like ak_index.txt, but for the LD version.
python ak_index_verses.py ak_index_ld.txt ak_index_ld_verses_set.py

# cp ak_verse_list.py ak_verse_ld_list.py
# ak_verse_ld uses ak_index_ld_verses_set.py
python ak_verse_ld_list.py temp_pwg_1.txt ak_verse_ld_list.txt

511 matches for "^-" in buffer: ak_verse_list.txt
306 matches for "^-" in buffer: ak_verse_ld_list.txt

This comparison provides support for contention that
the LD version should be preferred as a link target.
However, there are still 306 PWG references which
do not correspond to a verse in LD.

The next comparison is puzzling:
263 matches for "\+ (3, 4," in buffer: ak_verse_list.txt
262 matches for "\+ (3, 4," in buffer: ak_verse_ld_list.txt

442 matches for "\- (3, 4," in buffer: ak_verse_list.txt
234 matches for "\- (3, 4," in buffer: ak_verse_ld_list.txt
This shows that about 200 additional (3, 4, ...) of PWG are
 recognized by LD version.
 
*****************************************************
