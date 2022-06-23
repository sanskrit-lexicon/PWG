PWG/pwg_ls2/ramayana0

preliminary examination of correspondence between
* pwg 'R. GORR.' and 'R.'  and 'R. SCHL.' ls references and
* pdfs of Ramayana from Goressio and Schlegel.
  Note there are only 2 'volumes' of R. SCHL. pdf
  but 7 'volumes' of 'R. GORR.'
Important note: R. x,y,z  seems to refer to
 Schlegel if x = 1 or 2
 Goressio if x = 3,4,5,6,7
 This distinction can be implemented in basicadjust.php
  when generating the href.

# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------
Refer:
 https://github.com/sanskrit-lexicon/PWG/issues/54

Start with a copy of csl-orig/v02/pwg/pwg.txt at commit
  4d7cb57c0b845a3c59e14bcd37c01a3dd33949f9

# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_pwg_0 .txt in this spruch directory
  git show 4d7cb57c:v02/pwg/pwg.txt > /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/ramayana0/temp_pwg_0 .txt
# return to this ramayan0 directory
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/ramayana0/
# -------------------------------------------------------------
# -------------------------------------------------------------
# R. SCHL.  to be added as a pwg tooltip
# It is NOT in temp_pwgbib_input.txt
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pwg/pywork/pwgauth/pwgbib_input.txt temp_pwgbib_input.txt

python ../RV/lsextract.py 'R.' temp_pwg_0.txt temp_pwgbib_input.txt temp_lsextract_R_0.txt
2701 tooltips from temp_pwgbib_input.txt
9725 entries with ls for  R.
23287 = number of R. ls references

python ../RV/lsextract.py 'R. GORR.' temp_pwg_0.txt temp_pwgbib_input.txt temp_lsextract_RGORR_0.txt
2701 tooltips from temp_pwgbib_input.txt
2273 entries with ls for  R. GORR.
4023 = number of R. GORR. ls references

python ../RV/lsextract.py 'R. SCHL.' temp_pwg_0.txt temp_pwgbib_input.txt temp_lsextract_SCHL_0.txt
2701 tooltips from temp_pwgbib_input.txt
144 entries with ls for  R. SCHL.
194 = number of R. SCHL. ls references

# -------------------------------------------------------------
temp_pwg_1.txt. Manual changes 
1.  787 changes
<ls>R. A, B, C. D, E.</ls> -> <ls>R. A, B, C.</ls> <ls n="R. A,">D, E.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R. \1,">\4, \5.</ls>
----
1a. 44 changes
<ls>R. A, B, C. D, E</ls> -> <ls>R. A, B, C.</ls> <ls n="R. A,">D, E</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\)</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R. \1,">\4, \5</ls>
----
2. 1379 changes
<ls>R. A, B, C. D, E, F.</ls> -> <ls>R. A, B, C.</ls> <ls n="R.">D, E, F.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R.">\4, \5, \6.</ls>

2a. 24  changes (same redone at later time)
<ls>R. A, B, C. D, E, F.</ls> -> <ls>R. A, B, C.</ls> <ls n="R.">D, E, F.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R.">\4, \5, \6.</ls>

3. 299  changes
<ls>R. A, B, C. D.</ls> -> <ls>R. A, B, C.</ls> <ls n="R. A, B,">D.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R. \1, \2,">\4.</ls>

3a. 16  changes
<ls>R. A, B, C. D</ls> -> <ls>R. A, B, C.</ls> <ls n="R. A, B,">D</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\)</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R. \1, \2,">\4</ls>


4. 226 changes
 R. 2, 3, 12. 76, 13. 5, 32, 36.
<ls>R. A, B, C. D, E. F, G, H.</ls> ->
<ls>R. A, B, C.</ls> <ls n="R. A,">D, E.</ls> <ls n="R.">F, G, H.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R. \1,">\4, \5.</ls> <ls n="R.">\6, \7, \8.</ls>

5. 159 changes
R. 1, 1, 73. 5, 41, 4. 43, 7.
<ls>R. A, B, C. D, E, F. G, H.</ls> ->
<ls>R. A, B, C.</ls> <ls n="R.">D, E, F.</ls> <ls n="R. D,">G, H.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R.">\4, \5, \6</ls> <ls n="R. \4,">\7, \8.</ls>

7. 220  changes
R. R. 2, 26, 30. 3, 69, 3. 5, 89, 72.
<ls>R. A, B, C. D, E, F. G, H, I.</ls> ->
<ls>R. A, B, C.</ls> <ls n="R.">D, E, F.</ls> <ls n="R.">G, H, I.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R.">\4, \5, \6</ls> <ls n="R.">\7, \8, \9.</ls>

----
8. 2 changes
<ls>R. A, B, C. D, E, F,</ls> -> <ls>R. A, B, C.</ls> <ls n="R.">D, E, F</ls>,

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\,</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R.">\4, \5, \6</ls>,

----
9. 25 changes
<ls>R. A, B, C. D, E. F.</ls> -> <ls>R. A, B, C.</ls> <ls n="R. A, D,">F.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\)\. \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R. \1">\4, \5</ls> <ls n="R. \1, \4,">\6.</ls>

----
10. 335  changes
<ls>R. A, B, C. D. E, F.</ls> -> <ls>R. A, B, C.</ls> <ls n="R. A, B,">D.</ls> <ls> n="R. A,">E, F.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\)\. \([0-9]+\)\, \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R. \1, \2,">\4. </ls> <ls n="R. \1,">\5, \6.</ls>

11. 144 changes
R. 6, 29, 19. 31, 17. 73, 37.
<ls>R. A, B, C. D, E. F, G.</ls> ->
<ls>R. A, B, C.</ls> <ls n="R. A,">D, E.</ls> <ls n="R. A,">F, G.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R. \1,">\4, \5.</ls> <ls n="R. \1,">\6, \7.</ls>

12. 25 changes
R. 1, 40, 13. 5, 7, 39. 47.
<ls>R. A, B, C. D, E, F. G.</ls> ->
<ls>R. A, B, C.</ls> <ls n="R.">D, E, F.</ls> <ls n="R. E, F,"> G.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R.">\4, \5, \6.</ls> <ls n="R. \4, \5,">\7.</ls>

---------------------------
13. 43 changes
R. 1, 63, 2. 2, 64, 21
<ls>R. A, B, C. D, E, F</ls> -> <ls>R. A, B, C.</ls> <ls n="R.">D, E, F</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R.">\4, \5, \6</ls>

---------------------------
14. 3 changes
R. 5, 40, 12. 13.
<ls>R. A, B, C. D.</ls> ->
<ls>R. A, B, C.</ls> <ls n="R. A, B,">D.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R. \1, \2,">\4.</ls>

---------------------------
15. 39 changes
R. 5, 33, 34. 38. 1, 51, 4.
<ls>R. A, B, C. D. E, F, G.</ls> ->
<ls>R. A, B, C.</ls> <ls n="R. A, B,">D.</ls> <ls n="R.">E, F, G.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R. \1, \2,">\4.</ls> <ls n="R.">\5, \6, \7.</ls>

----
16. 4 changes
<ls>R. A, B, C. D, E, F. G, H, I.</ls> ->
<ls>R. A, B, C.</ls> <ls n="R.">D, E, F.</ls> <ls n="R.">G, H, I.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R.">\4, \5, \6.</ls> <ls n="R.">\7, \8, \9.</ls>
----
17.  changes
R. 2, 72, 8. 12. 3, 22, 35.
<ls>R. A, B, C. D. E, F, G.</ls> ->
<ls>R. A, B, C.</ls> <ls n="R. A, B,">D.</ls> <ls n="R.">E, F, G.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R. \1, \2,">\4.</ls> <ls n="R.">\5, \6, \7.</ls>

# -------------------------------------------------------------
temp_pwg_2.txt   More manual changes.


1. 
R. 3, 20, 37. 5, 38, 30. 6, 30, 39. 37, 65.
<ls>R. A, B, C. D, E, F. G, H, I. J, K.</ls> ->
<ls>R. A, B, C.</ls> <ls n="R">D, E, F.</ls> <ls n="R.">G, H, I.</ls> <ls n="R. G,">J, K.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R.">\4, \5, \6.</ls> <ls n="R.">\7, \8, \9.</ls> <ls n="R. \7,">\10, \11.</ls> X10 = \10

# -------------------------------------------------------------
python ../RV/lsextract.py 'R.' temp_pwg_1.txt temp_pwgbib_input.txt temp_lsextract_R_1.txt
2701 tooltips from temp_pwgbib_input.txt
9710 entries with ls for  R.
27756 = number of R. ls references

install temp_pwg_1.txt into csl-orig. (temporary - to catch xml errors)
make corrections to change_01.txt

cp temp_pwg_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg ' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/ramayana0



# -------------------------------------------------------------
# temp_pwg_2.txt   constructed iteratively
# not used
#python ../p/listls3_abnormal.py 'R.' temp_pwg_1.txt temp_abnormal_r_00.txt temp_change_abnormal.txt

python ../p/make_change3_abnormal.py 'R.' temp_pwg_1.txt temp_change3_abnormal.txt
1231 records written to temp_change3_abnormal.txt

# insert temp_change3_abnormal.txt into (new file) change_2.txt

python updateByLine.py temp_pwg_1.txt change_2.txt temp_pwg_2.txt
1231 of type new
----

python ../p/make_change3_ls.py 'R.' temp_pwg_2.txt temp_change3_01.txt
291 changes not yet done. See tempdbg.txt
10 changes deferred
4451 records written to temp_change3_01.txt
# insert temp_change3_01.txt into bottom of change_2.txt

python updateByLine.py temp_pwg_1.txt change_2.txt temp_pwg_2.txt
5682 change transactions from change_2.txt

----
python ../p/make_change3_ls.py 'R.' temp_pwg_2.txt temp_change3_02.txt
334 changes not yet done. See tempdbg.txt
4 changes deferred
1569 records written to temp_change3_02.txt

# insert temp_change3_02.txt into bottom of change_2.txt

python updateByLine.py temp_pwg_1.txt change_2.txt temp_pwg_2.txt
7251 change transactions from change_2.txt

----
python ../p/make_change3_ls.py 'R.' temp_pwg_2.txt temp_change3_03.txt
351 changes not yet done. See tempdbg.txt
3 changes deferred
1137 records written to temp_change3_03.txt
# insert temp_change3_03.txt into bottom of change_2.txt
python updateByLine.py temp_pwg_1.txt change_2.txt temp_pwg_2.txt
8388 change transactions from change_2.txt

----
python ../p/make_change3_ls.py 'R.' temp_pwg_2.txt temp_change3_04.txt
359 changes not yet done. See tempdbg.txt
2 changes deferred
595 records written to temp_change3_04.txt

# insert temp_change3_04.txt into bottom of change_2.txt
python updateByLine.py temp_pwg_1.txt change_2.txt temp_pwg_2.txt
8983 change transactions from change_2.txt

----
python ../p/make_change3_ls.py 'R.' temp_pwg_2.txt temp_change3_05.txt
360 changes not yet done. See tempdbg.txt
1 changes deferred
308 records written to temp_change3_05.txt

# insert temp_change3_05.txt into bottom of change_2.txt
python updateByLine.py temp_pwg_1.txt change_2.txt temp_pwg_2.txt
9291 change transactions from change_2.txt

----
python ../p/make_change3_ls.py 'R.' temp_pwg_2.txt temp_change3_06.txt
363 changes not yet done. See tempdbg.txt
0 changes deferred
169 records written to temp_change3_06.txt

# insert temp_change3_06.txt into bottom of change_2.txt
python updateByLine.py temp_pwg_1.txt change_2.txt temp_pwg_2.txt
9460 change transactions from change_2.txt

----
python ../p/make_change3_ls.py 'R.' temp_pwg_2.txt temp_change3_07.txt
365 changes not yet done. See tempdbg.txt
0 changes deferred
93 records written to temp_change3_07.txt
# insert temp_change3_07.txt into bottom of change_2.txt

python updateByLine.py temp_pwg_1.txt change_2.txt temp_pwg_2.txt
9553 change transactions from change_2.txt

----
python ../p/make_change3_ls.py 'R.' temp_pwg_2.txt temp_change3_08.txt
365 changes not yet done. See tempdbg.txt
0 changes deferred
58 records written to temp_change3_08.txt

# insert temp_change3_08.txt into bottom of change_2.txt

python updateByLine.py temp_pwg_1.txt change_2.txt temp_pwg_2.txt
9611 change transactions from change_2.txt

----
python ../p/make_change3_ls.py 'R.' temp_pwg_2.txt temp_change3_09.txt
365 changes not yet done. See tempdbg.txt
0 changes deferred
31 records written to temp_change3_09.txt

# insert temp_change3_09.txt into bottom of change_2.txt
python updateByLine.py temp_pwg_1.txt change_2.txt temp_pwg_2.txt
9642 change transactions from change_2.txt

2701 tooltips from temp_pwgbib_input.txt
9710 entries with ls for  R.
36167 = number of R. ls references

python ../RV/lsextract.py 'R.' temp_pwg_2.txt temp_pwgbib_input.txt temp_lsextract_R_2.txt
2701 tooltips from temp_pwgbib_input.txt
9710 entries with ls for  R.
36167 = number of R. ls references

# -------------------------------------------------------------
Now manually handle the tempdbg.txt (call it temp_change_09_dbg.txt)
<lsg1> -> <ls n="GORR. 1,"> 
<lsg2> -> <ls n="GORR. 2,">

QUESTION: <L>115535<pc>7-1463<k1>svasTa
  <ls n="R.">7, 18, 17.</ls> and following not found in ramayanaschl
QUESTION: <L>117897<pc>7-1677<k1>hlAd
  <ls n="R. GORR.">7, 97, 11.</ls> not found in ramayangorr
What is meaning of R. with 4 parameters? (100+ instances. first parm is '7')

#insert revised temp_change_09_dbg.txt at bottom of change_2.txt
python updateByLine.py temp_pwg_1.txt change_2.txt temp_pwg_2.txt
10015 change transactions from change_2.txt

-----
python ../p/make_change3_ls.py 'R.' temp_pwg_2.txt temp_change3_10.txt
6 changes not yet done. See tempdbg.txt
0 changes deferred
31 records written to temp_change3_10.txt


# insert temp_change3_10.txt into bottom of change_2.txt
python updateByLine.py temp_pwg_1.txt change_2.txt temp_pwg_2.txt

python ../RV/lsextract.py 'R.' temp_pwg_2.txt temp_pwgbib_input.txt temp_lsextract_R_2.txt
2701 tooltips from temp_pwgbib_input.txt
9710 entries with ls for  R.
36747 = number of R. ls references


-------------------------------------------------------------
# local install temp_pwg_2.txt and check for xml validity

cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg ' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/ramayana0

-------------------------------------------------------------
temp_pwg_3.txt
1142 matches in 1079 lines for "GORR" in buffer: temp_lsextract_R_2.txt
These need further work.
Initially, cp temp_pwg_2.txt temp_pwg_3.txt

--- option 1
python make_change_3a.py 1 temp_pwg_3.txt temp_change3a_01.txt
498 records written to temp_change3a_01.txt
insert temp_change3a_01.txt into change_3.txt

python updateByLine.py temp_pwg_2.txt change_3.txt temp_pwg_3.txt

python ../RV/lsextract.py 'R.' temp_pwg_3.txt temp_pwgbib_input.txt temp_lsextract_R_3.txt
36747 = number of R. ls references

--- option 2
python make_change_3a.py 2 temp_pwg_3.txt temp_change3a_02.txt
168 records written to temp_change3a_01.txt
insert temp_change3a_02.txt into change_3.txt

python updateByLine.py temp_pwg_2.txt change_3.txt temp_pwg_3.txt

python ../RV/lsextract.py 'R.' temp_pwg_3.txt temp_pwgbib_input.txt temp_lsextract_R_3.txt
36747 = number of R. ls references

--- option 3
python make_change_3a.py 3 temp_pwg_3.txt temp_change3a_03.txt
203 records written to temp_change3a_01.txt

# insert temp_change3a_03.txt into change_3.txt

python updateByLine.py temp_pwg_2.txt change_3.txt temp_pwg_3.txt
869 change transactions from change_3.txt

python ../RV/lsextract.py 'R.' temp_pwg_3.txt temp_pwgbib_input.txt temp_lsextract_R_3.txt
36950 = number of R. ls references

--- option 2a
python make_change_3a.py 2a temp_pwg_3.txt temp_change3a_02a.txt
4 records written to temp_change3a_02a.txt
insert temp_change3a_02a.txt into change_3.txt

python updateByLine.py temp_pwg_2.txt change_3.txt temp_pwg_3.txt
875 changes

python ../RV/lsextract.py 'R.' temp_pwg_3.txt temp_pwgbib_input.txt temp_lsextract_R_3.txt
36950 = number of R. ls references

--- option 1a
python make_change_3a.py 1a temp_pwg_3.txt temp_change3a_01a.txt
14 records written to temp_change3a_01a.txt
insert temp_change3a_01a.txt into change_3.txt

python updateByLine.py temp_pwg_2.txt change_3.txt temp_pwg_3.txt
887 changes

python ../RV/lsextract.py 'R.' temp_pwg_3.txt temp_pwgbib_input.txt temp_lsextract_R_3.txt
36950 = number of R. ls references

--- option 4
python make_change_3a.py 4 temp_pwg_3.txt temp_change3a_04.txt
63 records written to temp_change3a_04.txt
insert temp_change3a_04.txt into change_3.txt

python updateByLine.py temp_pwg_2.txt change_3.txt temp_pwg_3.txt
887 changes

python ../RV/lsextract.py 'R.' temp_pwg_3.txt temp_pwgbib_input.txt temp_lsextract_R_3.txt
36977 = number of R. ls references

python lsextract_v1.py 'R.' temp_pwg_3.txt temp_pwgbib_input.txt lsextract_v1_R_3.txt temp_changes_gorr.txt
224 GORR change forms written to temp_changes_gorr.txt

# Manually edit temp_changes_gorr_edit.txt.
</ls> <ls n="R. ed. Bomb.">
<ls n="R. GORR.">
</ls> <ls n="R. GORR.">
</ls> <ls n="R.">
<ls n="GORR.">
</ls> <ls n="GORR.">
</ls> <ls n="SCHL.">
</ls> <ls n="SCHL.">
</ls> <ls>
insert temp_changes_gorr_edit.txt into change_3.txt

python updateByLine.py temp_pwg_2.txt change_3.txt temp_pwg_3.txt
1163 change transactions from change_3.txt

python ../RV/lsextract.py 'R.' temp_pwg_3.txt temp_pwgbib_input.txt temp_lsextract_R_3.txt

python ../RV/lsextract.py 'R. GORR.' temp_pwg_3.txt temp_pwgbib_input.txt temp_lsextract_Rgorr_4.txt
2294 entries with ls for  R. GORR.
4341 = number of R. GORR. ls references

python ../p/make_change3_ls.py 'R. GORR.' temp_pwg_3.txt temp_change3_11.txt
32 changes not yet done. See tempdbg.txt
2 changes deferred
503 records written to temp_change3_11.txt
# insert temp_change3_11.txt into change_3.txt. 
python updateByLine.py temp_pwg_2.txt change_3.txt temp_pwg_3.txt
1700

python ../RV/lsextract.py 'R. GORR.' temp_pwg_3.txt temp_pwgbib_input.txt temp_lsextract_Rgorr_4.txt
2701 tooltips from temp_pwgbib_input.txt
2294 entries with ls for  R. GORR.
4875 = number of R. GORR. ls references

python ../p/make_change3_ls.py 'R. GORR.' temp_pwg_3.txt temp_change3_12.txt
3 changes not yet done. See tempdbg.txt
1 changes deferred
92 records written to temp_change3_12.txt
# insert temp_change3_12.txt into change_3.txt. 
python updateByLine.py temp_pwg_2.txt change_3.txt temp_pwg_3.txt
1792 change transactions from change_3.txt

python ../p/make_change3_ls.py 'R. GORR.' temp_pwg_3.txt temp_change3_13.txt
3 changes not yet done. See tempdbg.txt
0 changes deferred
29 records written to temp_change3_13.txt
# insert temp_change3_13.txt into change_3.txt. 
python updateByLine.py temp_pwg_2.txt change_3.txt temp_pwg_3.txt
1821 change transactions from change_3.txt

python ../p/make_change3_ls.py 'R. GORR.' temp_pwg_3.txt temp_change3_14.txt
3 changes not yet done. See tempdbg.txt
0 changes deferred
13 records written to temp_change3_14.txt
# insert temp_change3_14.txt into change_3.txt. 
python updateByLine.py temp_pwg_2.txt change_3.txt temp_pwg_3.txt
1834 change transactions from change_3.txt

python lsextract_v2.py 'R. GORR.' temp_pwg_3.txt temp_pwgbib_input.txt lsextract_v2_R_GORR_3.txt temp_changes_gorr.txt
# insert temp_changes_gorr.txt into change_3.txt
python updateByLine.py temp_pwg_2.txt change_3.txt temp_pwg_3.txt
2388 change transactions from change_3.txt

python lsextract_v2.py 'R. GORR.' temp_pwg_3.txt temp_pwgbib_input.txt lsextract_v2_R_GORR_3.txt temp_changes_gorr.txt
499 GORR change forms written to temp_changes_gorr.txt
# insert temp_changes_gorr.txt into change_3.txt
python updateByLine.py temp_pwg_2.txt change_3.txt temp_pwg_3.txt
2887 change transactions from change_3.txt

python lsextract_v2.py 'R. GORR.' temp_pwg_3.txt temp_pwgbib_input.txt lsextract_v2_R_GORR_3.txt temp_changes_gorr.txt
301 GORR change forms written to temp_changes_gorr.txt
# insert temp_changes_gorr.txt into change_3.txt
python updateByLine.py temp_pwg_2.txt change_3.txt temp_pwg_3.txt
3188 change transactions from change_3.txt

python lsextract_v2.py 'R. GORR.' temp_pwg_3.txt temp_pwgbib_input.txt lsextract_v2_R_GORR_3.txt temp_changes_gorr.txt
2294 entries with ls for  R. GORR.
6319 = number of R. GORR. ls references
63 GORR change forms written to temp_changes_gorr.txt
# insert temp_changes_gorr.txt into change_3.txt
python updateByLine.py temp_pwg_2.txt change_3.txt temp_pwg_3.txt
3251 change transactions from change_3.txt

python lsextract_v3.py 'R. GORR.' temp_pwg_3.txt temp_pwgbib_input.txt lsextract_v3_R_GORR_3.txt temp_changes_gorr.txt
2294 entries with ls for  R. GORR.
6382 = number of R. GORR. ls references
469 GORR change forms written to temp_changes_gorr.txt

PRINT error: <L>44264<pc>4-0644<k1>pAtra  <ls n="R. GORR.">15, 6, 8 (9</ls>
  CORRECTED  1, 15, 6. 8.
4-num anomaly in R. GORR. <L>82519<pc>6-0193<k1>yogya
  <ls n="R. GORR.">7, 59, 1, 21.</ls>

# manual editing of temp_changes_gorr.txt.
# insert temp_changes_gorr.txt into change_3.txt
python updateByLine.py temp_pwg_2.txt change_3.txt temp_pwg_3.txt
3685 change transactions from change_3.txt

python lsextract_v3.py 'R. GORR.' temp_pwg_3.txt temp_pwgbib_input.txt lsextract_v3_R_GORR_3.txt temp_changes_gorr.txt
52 GORR changes written --- these all seem to be legitimate exceptions

python lsextract_v1.py 'R.' temp_pwg_3.txt temp_pwgbib_input.txt lsextract_v1_R_3.txt temp_changes_abnormal.txt
403 marked as abnormal for R.
403 abnormal change forms written to temp_changes_abnormal_R.txt
# manual corrections to temp_changes_abnormal_R.txt
 <xls> -> <ls>,  </xls> -> </ls>
 R. ed. Ser. still another (unknown) version of Ramayana

# insert temp_changes_abnormal_R.txt into change_3.txt
python updateByLine.py temp_pwg_2.txt change_3.txt temp_pwg_3.txt
4072 change transactions from change_3.txt

# How many are still abnormal for 'R.' ?
python lsextract_v1.py 'R.' temp_pwg_3.txt temp_pwgbib_input.txt lsextract_v1_R_3.txt temp_changes_abnormal.txt
90 abnormal change forms written to temp_changes_abnormal.txt

4119 change transactions from change_3.txt
python updateByLine.py temp_pwg_2.txt change_3.txt temp_pwg_3.txt

One final time:
python lsextract_v1.py 'R.' temp_pwg_3.txt temp_pwgbib_input.txt lsextract_v1_R_3.txt temp_changes_abnormal_R.txt
46 abnormal change forms written to temp_changes_abnormal.txt

Now try the same with R. GORR.
python lsextract_v1.py 'R. GORR.' temp_pwg_3.txt temp_pwgbib_input.txt lsextract_v1_Rgorr_3.txt temp_changes_abnormal_gorr.txt
47 abnormal change forms written to temp_changes_abnormal_gorr.txt
# manual adjust temp_changes_abnormal_gorr.txt
# insert into bottom of change_3.txt
python updateByLine.py temp_pwg_2.txt change_3.txt temp_pwg_3.txt
4135 change transactions from change_3.txt

# rerun 
python lsextract_v1.py 'R. GORR.' temp_pwg_3.txt temp_pwgbib_input.txt lsextract_v1_Rgorr_3.txt temp_changes_abnormal_gorr.txt
32 abnormal change forms written to temp_changes_abnormal_gorr.txt

[this version of temp_pwg_3.txt has been xml-checked.

Do similar analysis for 'R. SCHL'

python lsextract_v1.py 'R. SCHL.' temp_pwg_3.txt temp_pwgbib_input.txt lsextract_v1_Rschl_3.txt temp_changes_abnormal_schl.txt
149 entries with ls for  R. SCHL.
204 = number of R. SCHL. ls references
26 marked as abnormal for R. SCHL.
26 abnormal change forms written to temp_changes_abnormal_schl.txt

#examine temp_changes_abnormal_schl.txt
# insert temp_changes_abnormal_schl.txt into change_3.txt
python updateByLine.py temp_pwg_2.txt change_3.txt temp_pwg_3.txt
4162 change transactions from change_3.txt

# remaining R. SCHL. anomalies
python lsextract_v1.py 'R. SCHL.' temp_pwg_3.txt temp_pwgbib_input.txt lsextract_v1_Rschl_3.txt temp_changes_abnormal_rschl.txt
206 = number of R. SCHL. ls references
0 marked as abnormal for R. SCHL.
0 abnormal change forms written to temp_changes_abnormal_rschl.txt


python lsextract_v1.py 'SCHL.' temp_pwg_3.txt temp_pwgbib_input.txt lsextract_v1_schl_3.txt temp_changes_abnormal_schl.txt
# insert temp_changes_abnormal_schl.txt into change_3.txt
python updateByLine.py temp_pwg_2.txt change_3.txt temp_pwg_3.txt
4212 change transactions from change_3.txt

# <ls>adv.</ls> -> <ls> (9) inserted into change_3.txt
python updateByLine.py temp_pwg_2.txt change_3.txt temp_pwg_3.txt
4221 change transactions from change_3.txt

python lsextract_v1.py 'SCHL.' temp_pwg_3.txt temp_pwgbib_input.txt lsextract_v1_schl_3.txt temp_changes_abnormal_schl.txt
224 entries with ls for  SCHL.
328 = number of SCHL. ls references
2 marked as abnormal for SCHL.

python lsextract_v1.py 'R. SCHL.' temp_pwg_3.txt temp_pwgbib_input.txt lsextract_v1_rschl_3.txt temp_changes_abnormal_rschl.txt
149 entries with ls for  R. SCHL.
206 = number of R. SCHL. ls references
0 marked as abnormal for R. SCHL.
0 abnormal change forms written to temp_changes_abnormal_rschl.txt

python lsextract_v1.py 'R. ed. Bomb.' temp_pwg_3.txt temp_pwgbib_input.txt lsextract_v1_redbomb_3.txt temp_changes_abnormal_redbomb.txt
262 entries with ls for  R. ed. Bomb.
290 = number of R. ed. Bomb. ls references
28 marked as abnormal for R. ed. Bomb.
28 abnormal change forms written to temp_changes_abnormal_redbomb.txt

# manual changes to temp_changes_abnormal_redbomb.txt
# insert temp_changes_abnormal_redbomb.txt into change_3.txt TODO
python updateByLine.py temp_pwg_2.txt change_3.txt temp_pwg_3.txt
4250 change transactions from change_3.txt

python lsextract_v1.py 'R. ed. Bomb.' temp_pwg_3.txt temp_pwgbib_input.txt lsextract_v1_redbomb_3.txt temp_changes_abnormal_redbomb.txt
262 entries with ls for  R. ed. Bomb.
309 = number of R. ed. Bomb. ls references
0 marked as abnormal for R. ed. Bomb.

python lsextract_v1.py 'GORR.' temp_pwg_3.txt temp_pwgbib_input.txt lsextract_v1_gorr_3.txt temp_changes_abnormal_gorr.txt
3270 = number of GORR. ls references
171 marked as abnormal for GORR.

# Manually edit temp_changes_abnormal_gorr.txt
# insert temp_changes_abnormal_gorr.txt into change_3
python updateByLine.py temp_pwg_2.txt change_3.txt temp_pwg_3.txt
4403 change transactions from change_3.txt

# recompute abnormals
python lsextract_v1.py 'GORR.' temp_pwg_3.txt temp_pwgbib_input.txt lsextract_v1_gorr_3.txt temp_changes_abnormal_gorr.txt
1170 entries with ls for  GORR.
3285 = number of GORR. ls references
26 marked as abnormal for GORR.
26 abnormal change forms written to temp_changes_abnormal_gorr.txt

# manual adjustment of temp_changes_abnormal_gorr.txt and insert into change_3
$ python updateByLine.py temp_pwg_2.txt change_3.txt temp_pwg_3.txt             1149413 lines read from temp_pwg_2.txt
1149413 records written to temp_pwg_3.txt
4404 change transactions from change_3.txt
4404 of type new

# rerun
python lsextract_v1.py 'GORR.' temp_pwg_3.txt temp_pwgbib_input.txt lsextract_v1_gorr_3.txt temp_changes_abnormal_gorr.txt
1170 entries with ls for  GORR.
3286 = number of GORR. ls references
17 marked as abnormal for GORR.
17 abnormal change forms written to temp_changes_abnormal_gorr.txt


START HERE
sh redo_lsextract_v1.sh
This remakes these files:
lsextract_v1_r.txt
lsextract_v1_gorr.txt
lsextract_v1_schl.txt
lsextract_v1_rgorr.txt
lsextract_v1_rschl.txt
lsextract_v1_redbomb.txt

grep 'ABNORMAL' lsextract_v1_*.txt > lsextract_abnormal.txt
 (98 lines -- pwg Ramayana references considered as abnormal)

Summary of number of references with different abbreviations.
These are approximately the number of references with link targets.
The main purpose here is to identify the abnormal <ls> forms. The
exact references may be found by consulting the lsextract_v1_X.txt file(s).

abbrev     #entries  #references  #abnormal
R.          9705       37595       47
GORR.       1170        3287       17
SCHL.        224         328        2
R. GORR.    2295        7076       31
R. SCHL.     149         210        1
R. ed. Bomb. 263         310        0
R. ed. Ser.    4           4        0

# redo the summary of all ls references in pwg, using temp_pwg_3.txt
# note that ../mbh1/pwg_tooltip.txt is same as temp_pwgbib_input.txt
#  (as of this work)
python ../mbh1/lsextract_all.py temp_pwg_3.txt ../mbh1/pwg_tooltip.txt lsextract_pwg.txt

# do the summary BEFORE the changes, i.e., with temp_pwg_0.txt
python ../mbh1/lsextract_all.py temp_pwg_0.txt ../mbh1/pwg_tooltip.txt temp_lsextract_pwg_0.txt

# edited version of comparison of temp_lsextract_pwg_0.txt and lsextract_pwg.txt
# This quantifies the markup improvements.
 OLD     NEW    category      
698067  714437  ALL           As of 2022-06-22
 36524   32387  NUMBER        ls starts with number
 02170   02161  UNKNOWN       ls is unknown
 
                Ramayan 
                abbrev        Current tooltip
 23287   37595  R.            RĀMĀYAṆA. Ohne eine nähere Angabe ist be
 04023   07076  R. GORR.      RĀMĀYAṆA, translation by Gaspare Gorresi
 00343   03287  GORR.         GORRESIO.
 00217   00328  SCHL.*        ?  
 00194   00210  R. SCHL.      RĀMĀYAṆA. ? [Cologne addition]
 00269   00310  R. ed. Bomb.  RĀMĀYAṆA. ? [Cologne addition]

* SCHL.  This is a shorter abbreviation with same meaning as 'R. SCHL.', namely,
  the Schlegel version of Kandas 1 and 2 of Ramayana.
  It MAY be that some instances of SCHL. in pwg refer to other works by Schlegel.
   
# -------------------------------------------------------------
install temp_pwg_3.txt and check xml
cp temp_pwg_3.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg ' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/ramayana0

# *************************************************************
old notes follow

# -------------------------------------------------------------
; <L>9414<pc>1-0705<k1>AleKya {R. 1}
R. SCHL. 1, 5, 12.  Found in Schlegel, p. 29 (external 108)

Note: Gorresio 1,5,12 does not have AleKya

; <L>9367<pc>1-0701<k1>Alaya {R. 7}
R. 1, 2, 3. Found Alaya in Gorresio (p. 14, external 164) tridaSAlayaM
            Found Alaya in Schlegel (p. 15, external 94) tridaSAlayaM

; <L>393<pc>1-0031<k1>agnidAyaka {R. GORR. 1}
R. GORR. 2, 79, 19. Schlegel not found. last sarga is XX in Volume II
   Found verse in Bayer vol2.pdf,  p. 290, and agnidAyaka found there.
   dli_vol2.pdf does NOT have (missing pages)
   
; <L>85474<pc>6-0450<k1>roza {R. GORR. 2}
R. GORR. 1, 68, 20.  Schlegel caput LXVIII p. 246-7:
       verse 20 not found  (only 18 verses)

; <L>85374<pc>6-0443<k1>roDa {R. GORR. 1}
R. GORR. 1, 4, 27.


; <L>85715<pc>6-0475<k1>lag {R. GORR. 1}
R. GORR. 2, 8, 41.  dli_vol2: ayoDyAkARqa begins on p. 3 (external 52)
   and first sarga is X --- where are sargas 1-9?
   Bayer edition: Also starts at X  in volume 2. So where
289 matches for "GORR. 2, [1-9]," in buffer: temp_lsextract_RGORR_0.txt
 
; <L>88895<pc>6-0823<k1>vaSya {R. GORR. 3}
R. GORR. 2, 10, 24. Found in Bayer. Found in dli_vol2.

;-----------------------------------------------------------
; <L>1386<pc>1-0100<k1>atiyaSas {R. 1}
R. 2, 1, 6. in Schlegel p. 281; 

# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------
PROBABLY UNUSED, from ../p/readme.txt
# -------------------------------------------------------------
Focus on ls of form '<ls>P...</ls>'
Also handle those such as '<ls n="P."'
21567 matches in 21341 lines for "<ls>P\." in buffer: temp_pwg_0.txt

190 matches in 123 lines for "<ls n="P\." in buffer: temp_pwg_0.txt
121 matches in 77 lines for "<ls n="P\." in buffer: temp_pwg_0.txt

# -------------------------------------------------------------
cp temp_pwg_0.txt temp_pwg_01.txt
We will manually add changes contained in change_01.txt to update
 temp_pwg_01.txt.

# -------------------------------------------------------------

python listls3_abnormal.py 'P.' temp_pwg_0.txt temp_abnormal_av_0.txt temp_change_abnormal.txt

2643 abnormal ls written to temp_abnormal_av_0.txt
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
<ls>" in buffer: temp_pwg_0.txt

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
python diff_to_changes.py temp_pwg_0.txt temp_pwg_01.txt change_01.txt
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
python ../01/updateByLine.py temp_pwg_0.txt change_01.txt temp_pwg_01.txt

15317 change transactions from change_01.txt

------------------------------------------------
python listls3_abnormal.py 'P.' temp_pwg_01.txt temp_abnormal_p_02.txt temp_change_abnormal_02.txt
397 abnormal ls written to temp_abnormal_p_02.txt

temp_change_abnormal_02_edit.txt manual changes.
# Manual changes from temp_change_abnormal_02_edit.txt inserted into change_01

python ../01/updateByLine.py temp_pwg_0.txt change_01.txt temp_pwg_01.txt
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
python ../01/updateByLine.py temp_pwg_0.txt change_01.txt temp_pwg_01.txt
18151 change transactions from change_01.txt

Add changes from tempdbg
python ../01/updateByLine.py temp_pwg_0.txt change_01.txt temp_pwg_01.txt
18195 change transactions from change_01.txt

Also
28 '<ls>BHĀG.</ls> <ls>P. -> <ls>BHĀG. P.'
 2 '<ls>BRAHMAVAIV.</ls> <ls>P. -> <ls>BRAHMAVAIV. P.'
python ../01/updateByLine.py temp_pwg_0.txt change_01.txt temp_pwg_01.txt
18224 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'P.' temp_pwg_01.txt temp_change3_02.txt
2 changes not yet done. See tempdbg.txt
28 changes deferred
446 records written to temp_change3_02.txt

# insert temp_change3_02.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_0.txt change_01.txt temp_pwg_01.txt
18671 change transactions from change_01.txt

------------------------------------------------

python make_change3_ls.py 'P.' temp_pwg_01.txt temp_change3_03.txt
1 changes not yet done. See tempdbg.txt
12 changes deferred
166 records written to temp_change3_03.txt

#insert temp_change3_03 into change_01.
python ../01/updateByLine.py temp_pwg_0.txt change_01.txt temp_pwg_01.txt
18838 change transactions from change_01.txt

------------------------------------------------

python make_change3_ls.py 'P.' temp_pwg_01.txt temp_change3_04.txt
0 changes not yet done. See tempdbg.txt
11 changes deferred
90 records written to temp_change3_04.txt

#insert temp_change3_04 into change_01.
python ../01/updateByLine.py temp_pwg_0.txt change_01.txt temp_pwg_01.txt
18928 change transactions from change_01.txt

------------------------------------------------

python make_change3_ls.py 'P.' temp_pwg_01.txt temp_change3_05.txt
1 changes not yet done. See tempdbg.txt
8 changes deferred
58 records written to temp_change3_05.txt

#insert temp_change3_05 into change_01.
python ../01/updateByLine.py temp_pwg_0.txt change_01.txt temp_pwg_01.txt
18987 change transactions from change_01.txt

------------------------------------------------

python make_change3_ls.py 'P.' temp_pwg_01.txt temp_change3_06.txt
0 changes not yet done. See tempdbg.txt
5 changes deferred
39 records written to temp_change3_06.txt

# insert temp_change3_06.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_0.txt change_01.txt temp_pwg_01.txt
19026 change transactions from change_01.txt

------------------------------------------------

python make_change3_ls.py 'P.' temp_pwg_01.txt temp_change3_07.txt
0 changes not yet done. See tempdbg.txt
3 changes deferred
22 records written to temp_change3_07.txt

# insert temp_change3_07.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_0.txt change_01.txt temp_pwg_01.txt
19048 change transactions from change_01.txt

------------------------------------------------

python make_change3_ls.py 'P.' temp_pwg_01.txt temp_change3_08.txt
0 changes not yet done. See tempdbg.txt
3 changes deferred
15 records written to temp_change3_08.txt

# insert temp_change3_08.txt into change_01.txt
; manual correction of one BHAG. P. 
python ../01/updateByLine.py temp_pwg_0.txt change_01.txt temp_pwg_01.txt
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

python ../01/updateByLine.py temp_pwg_0.txt change_01.txt temp_pwg_01.txt
19051 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'P.' temp_pwg_01.txt temp_change3_10.txt
0 changes not yet done. See tempdbg.txt
1 changes deferred
6 records written to temp_change3_10.txt

# insert temp_change3_10.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_0.txt change_01.txt temp_pwg_01.txt
10957 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'P.' temp_pwg_01.txt temp_change3_11.txt
0 changes not yet done. See tempdbg.txt
0 changes deferred
5 records written to temp_change3_11.txt

# insert temp_change3_11.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_0.txt change_01.txt temp_pwg_01.txt
19062 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'P.' temp_pwg_01.txt temp_change3_12.txt
0 changes not yet done. See tempdbg.txt
0 changes deferred
4 records written to temp_change3_12.txt

# insert temp_change3_12.txt into change_01.txt
# remove 31 transactions that have an error in handling of 'fg.'
python ../01/updateByLine.py temp_pwg_0.txt change_01.txt temp_pwg_01.txt
19066 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'P.' temp_pwg_01.txt temp_change3_13.txt
0 changes not yet done. See tempdbg.txt
0 changes deferred
2 records written to temp_change3_13.txt

# insert temp_change3_13.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_0.txt change_01.txt temp_pwg_01.txt
19068 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'P.' temp_pwg_01.txt temp_change3_14.txt
0 changes not yet done. See tempdbg.txt
0 changes deferred
1 records written to temp_change3_14.txt


# insert temp_change3_14.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_0.txt change_01.txt temp_pwg_01.txt
19069 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'P.' temp_pwg_01.txt temp_change3_15.txt
0 changes not yet done. See tempdbg.txt
0 changes deferred
0 records written to temp_change3_15.txt

DONE!!

------------------------------------------------
Checks of change_abnormal.txt
python ../01/updateByLine.py temp_pwg_0.txt change_01.txt temp_pwg_01.txt
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
