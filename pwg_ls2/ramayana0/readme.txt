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
 https://github.com/sanskrit-lexicon/PWG/issues/57

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
further work on 'ed. Bomb.'
----------------------------------------------------------------
revision to pwgbib_input.txt regarding tooltips.
 (new version of csl-pywork)
# revise local copy
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pwg/pywork/pwgauth/pwgbib_input.txt temp_pwgbib_input.txt 

----------------------------------------------------------------
# markup for 'ed. Bomb.'
cp temp_pwg_3.txt temp_pwg_4.txt
manual changes from temp_pwg_3.txt
touch change_4.txt

(<ls>ed. Bomb.)
python lsextract_v1.py 'ed. Bomb.' temp_pwg_4.txt temp_pwgbib_input.txt lsextract_v1_edbomb.txt temp_changes_edbomb.txt
# manual change to temp_changes_edbomb.txt
# insert temp_changes_edbomb.txt into change_4.txt
python updateByLine.py temp_pwg_3.txt change_4.txt temp_pwg_4.txt
python lsextract_v1.py 'ed. Bomb.' temp_pwg_4.txt temp_pwgbib_input.txt lsextract_v1_edbomb.txt temp_changes_edbomb.txt
2702 tooltips from temp_pwgbib_input.txt
24 entries with ls for  ed. Bomb.
29 = number of ed. Bomb. ls references
1 marked as abnormal for ed. Bomb.   THIS IS AN MBH REFERENCE
1 abnormal change forms written to temp_changes_edbomb.txt

# some further manual changes to change_4.
python updateByLine.py temp_pwg_3.txt change_4.txt temp_pwg_4.txt
24 change transactions from change_4.txt

---  adding markup to ed. Bomb.
3053 matches in 2998 lines for "ed\. Bomb\." in buffer: temp_pwg_4.txt
  27 matches for "<ls>ed\. Bomb\."  no action 
  27 matches for ">ed\. Bomb\." (same list as prev.) no action
   8 matches for "^ed\. Bomb\."  (lines starting with ed. Bomb.) marked
   3018 matches in 2967 lines for "[^>]ed\. Bomb\."  info, no action
   2 matches of [ed. Bomb.]  marked
  51 matches for "[(]ed\. Bomb\."  marked
   2965 matches in 2916 lines for "[^>]ed\. Bomb\."
     88 matches for "[^ ]ed\. Bomb\."
   2965 matches in 2916 lines for "[ ]ed\. Bomb\."
     88 matches for "<ls>ed\. Bomb\."
   So now, the unmarked 'ed. Bomb.' coincide with those with ' ed. Bomb' (preceding space)
-------------------------------------------------------------------------
   There are some of these (such as "<ls>R. ed. Bomb.") that we don't want to mark.
   Two examples: <ls>R. ed. Bomb.   AND "<ls n="R. ed. Bomb."
     temporarily change these to <ls>R._ed._Bomb. (271)  AND "<ls n="R._ed._Bomb." (44)
     Now 70 matches for "\. ed\. Bomb\."  
       <ls>BHĀG. P. ed. Bomb. (14) temporary: <ls>BHĀG._P._ed._Bomb.
       <ls>ŚUK. ed. Bomb.  (8) temporary: <ls>ŚUK._ed._Bomb.
       <ls>MBH. ed. Bomb.  (9) temporary: <ls>MBH._ed._Bomb.
       <ls>PAÑCAT. ed. Bomb. (18) temporary: <ls>PAÑCAT._ed._Bomb.
       <ls>MĀLAV. ed. Bomb. (8) temporary: <ls>MĀLAV._ed._Bomb.
       misc. others changed by adding ls markup (13)
       Now, there are no remaining matches of ". ed. Bomb."

    2 matches for " ed\. Bomb\. [0-9]".  Add <ls> markup to these
    247 matches for " ed\. Bomb\.$"   Change these to "<ls>ed. Bomb.</ls>"
    1081 matches in 1080 lines for " ed\. Bomb\. " Since none of these 
        is followed by a digit, we may safely add ls markup

    1049 matches in 1040 lines for " ed\. Bomb\.)"
        we may safely add ls markup to these
     128 matches for " ed\. Bomb\.,
        we may safely add ls markup to these
      51 matches for " ed\. Bomb\.;"
        we may safely add ls markup to these
       6 matches for " ed\. Bomb\.:"
        we may safely add ls markup to these
    There remain 16 matches for " ed\. Bomb\.</ls>"
      These are remarked manually.
16 matches for " ed\. Bomb\.</ls>" in buffer: temp_pwg_4work.txt
 517081:<ls>BHĀG. P. 3, 19, 4. 8, 5, 15 ed. Bomb.</ls> (<ls>BURNOUF</ls>None {#baDyamAna#} für {#baDyamAna)#} . 
 525579:<ls>MBH. 3, 12729 ed. Bomb.</ls> und bei <ls>KULL.</ls> zu <ls>M. 3, 185</ls> {#brAhmadeyA#}, welche Form wohl die richtigere ist.
 532350:<ls>25 ed. Bomb.</ls> 
 554549:<ls>MBH. 11, 97, ed. Bomb.</ls> {#(pariBujyantaM#} ed. Calc.). {#varAhavasApariBfzwa#} 
 564983:<ls>MBH. 6, 360 ed. Bomb.</ls> {#(maDumatta#} ed. Calc.). sg. N. pr. eines Landes <is>gaṇa</is> {#kacCAdi#} zu 
 598267:<ls>MBH. 9, 2437 ed. Bomb.</ls> {#mitrahana#} ed. Calc. mit Weglassung eines {#Bo#} .
 620638:<ls>MBH. 12, 1509, ed. Bomb.</ls> {#(aBiBU#} ed. Calc.); nach dem Schol. = {#aSarIra#} .
 622912:<ls>MBH. 6, 342, ed. Bomb.</ls> {#(maniNgA#} ed. Calc.).
 628802:<ls>MBH. 7, 1487, ed. Bomb.</ls> {#(aprati°#} ed. Calc.).
 645824:<ls>MBH. 3, 16111 ed. Bomb.</ls> St. {#apASrayavant#} der ed. Calc.
 645858:<ls>MBH. 13, 3262 ed. Bomb.</ls> st. {#a°#} der ed. Calc. 
 657396:<ls>MBH. 1, 2988, ed. Bomb.</ls> <ls>Z. 17</ls> lies {#nAganAsoru#} st. {#nagna°#} . 
 665475:<ls>MBH. 3, 11383, ed. Bomb.</ls>
 701637:<ls>MBH. 5, 68 ed. Bomb.</ls>
1138062:<ls>Z. 6. 7 ed. Bomb.</ls> {#tasya kAlaH parAyaRam#}; vgl. 
1144538:<ls>MBH. 1, 7051. 7019 ed. Bomb.</ls>

# -------------------------------------------------------------
# install temp_pwg_4.txt and check xml
cp temp_pwg_4.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg ' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
 #prints 'ok'

*******************************************************************************************
# markup for 'ed. Calc.'
cp temp_pwg_4.txt temp_pwg_5.txt
# manual changes from temp_pwg_4.txt
touch change_5.txt

Add tooltip for ed. Calc.  : "Calcutta edition of various works [Cologne addition]"
# revise local copy
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pwg/pywork/pwgauth/pwgbib_input.txt temp_pwgbib_input.txt 

1350 matches in 1348 lines for "ed\. Calc\.(<ls>ed. Calc."
32 matches for "<ls>ed\. Calc\."
  manually revise
 No lines starting with 'ed. Calc.'
1318 matches in 1317 lines for "[^>]ed\. Calc\."

 5 Matches with "<ls>RAGH. (ed. Calc.)"  temporary change to "<ls>RAGH. (ed._Calc.)"
 6 matches for "P. (ed. Calc.)" temporary change to "P. (<ls>ed._Calc.</ls>)"
 Finally change all "(ed. Calc.)" to "(<ls>ed._Calc.</ls>)"

118 matches for "<ls>RAGH. ed. Calc." temporary change to "<ls>RAGH. ed._Calc."
475 matches for "<ls>LALIT. ed. Calc." temporary change to "<ls>LALIT. ed._Calc."
  9 matches for "<ls>RĀJA-TAR. ed. Calc." temporary change to "<ls>RĀJA-TAR. ed._Calc."
  2 matches for "<ls>MṚCCH. ed. Calc." temporary change to "<ls>MṚCCH. ed._Calc."
  2 matches for "<ls>M. ed. Calc." temporary change to "<ls>M. ed._Calc."

All instances of "<ls>ed. Calc." temporary change to "<ls>ed._Calc."
No instances of "ed. Calc." within an <ls>X</ls> (all temporarily changed to "ed._Calc.")
656 matches in 655 lines for "ed. Calc."  These remain to be marked.
Have marked all "(ed. Calc." instances to "(ed._Calc."
624 matches in 623 lines for "ed. Calc." These remain to be marked.
** break point 1** (change_5.txt updated)
110 changes of "ed. Calc.$" to "<ls>ed._Calc.</ls>".

45 matches for "ed. Calc. $"  temporarily marked as "<ls>ed._Calc. "
287 matches for " ed. Calc.)" temporarily marked as " <ls>ed._Calc.</ls>)"
 43 matches for " ed. Calc. {#" temporarily marked as " <ls>ed._Calc.</ls> {#"
 15 matches for " ed. Calc.;" temporarily marked as " <ls>ed._Calc.</ls>;
 21 matches for " ed. Calc. zu" temporarily marked as " <ls>ed._Calc.</ls> zu"
 24 matches for " ed. Calc.,"  temporarily marked as " <ls>ed._Calc.</ls>,"
 27 matches for " der ed. Calc. "  temporarily marked as " der <ls>ed._Calc.</ls> "
 23 matches for "die ed. Calc. " temporarily marked as "die <ls>ed._Calc.</ls> "
 21 matches for "ed. Calc."  are all that remain. temporarily marked as "<ls>ed._Calc.</ls>"

Now there are no "ed. Calc." -- all have been marked.
Remove temporary markup:  "ed._Calc." -> "ed. Calc."
python updateByLine.py temp_pwg_4.txt change_5.txt temp_pwg_5.txt
# consolidate change_4.txt and change_5.txt
mv change_4.txt tempprev_change_4.txt
mv change_5.txt tempprev_change_5.txt
python diff_to_changes.py temp_pwg_3.txt temp_pwg_4.txt change_4.txt
# 2680 changes written to change_4.txt
python diff_to_changes.py temp_pwg_4.txt temp_pwg_5.txt change_5.txt
762 changes written to change_5.txt


# -------------------------------------------------------------

# install temp_pwg_5.txt and check xml
cp temp_pwg_5.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg ' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
 #prints 'ok'

# redo the summary
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pwg/pywork/pwgauth/pwgbib_input.txt temp_pwgbib_input.txt
python ../mbh1/lsextract_all.py temp_pwg_5.txt temp_pwgbib_input.txt lsextract_pwg.txt
