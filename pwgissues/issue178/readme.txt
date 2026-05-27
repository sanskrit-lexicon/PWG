
05-24-2026 begun ejf

enhance PWG markup for common abbreviations, continuation of issue174

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issues/178


this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue178

* gather files to start analysis
-------------------------------------
# get temporary local copy of kosha (at commit b877f8411)
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt

-------------------------------------
programs from issue174
# count_ab.py  counts of <ab>X</ab> from a given version of pwg.txt
python count_ab.py <PWG> <count_ab_X.txt>
# abdiff.py  merges two count_ab files
python abdiff.py <count_ab_X.txt> <count_ab_Y.txt> <abdiff_X_Y.txt>
 X is (typically) from cdsl version of pwg
 Y is (typically) from Andhrabharati version of pwg
 output file has lines with 4 tab-delimited fields:
 - abbrev
 - count_X of abbrev from count_ab_X.txt, or -1 if abbrev not in X
 - count_Y of abbrev from count_ab_Y.txt, or -1 if abbrev not in Y
 - count_X - count_y for this abbrev if 
-------------------------------------
* count_ab_0.txt, count_ab_A0.txt, abdiff_0_0.txt

python count_ab.py temp_pwg_0.txt count_ab_0.txt
1129105 read from temp_pwg_0.txt
782 lines written to count_ab_0.txt
178317 = total number of <ab>X</ab>
# from Andhrabharati markcount_a_3b.txt renamed count_ab_A0.txt
python abdiff.py count_ab_0.txt count_ab_A0.txt abdiff_0_A0.txt
* temp_pwg_0a.txt_
cp temp_pwg_0.txt temp_pwg_0a.txt
# manaul changes to temp_pwg_0a.txt -- These awkward to do by program

* temp_pwg_1.txt
# many replacements in function change_one if change1.py
python change1.py temp_pwg_0a.txt temp_pwg_1.txt
892 lines changed
* change_0_0a.txt,  change_0a_1.txt
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_0a.txt change_0_0a.txt
235 changes written to change_0_0a.txt

python diff_to_changes_dict.py temp_pwg_0a.txt temp_pwg_1.txt change_0a_1.txt
892 changes written to change_0a_1.txt

* count_ab_1.txt, abdiff_1_A0.txt
python count_ab.py temp_pwg_1.txt count_ab_1.txt
782 lines written to count_ab_1.txt
177972 = total number of <ab>X</ab>

python abdiff.py count_ab_1.txt count_ab_A0.txt abdiff_1_A0.txt
782 read from count_ab_1.txt
788 read from count_ab_A0.txt
792 total distinct abbreviations
792 lines written to abdiff_1_A0.txt

* temp_pwg_2.txt, input_2.txt  
additional abbreviations in input_2.txt
N.N.
s.
ved.
ebend.

# mark these
python mark_ab.py temp_pwg_1.txt input_2.txt temp_pwg_2.txt # markcount_2.txt
1129105 lines read from temp_pwg_1.txt
7516 lines changed
1129105 lines written to temp_pwg_2.txt

* change_1_2.txt, change_0_2.txt
python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_1_2.txt
7516 changes written to change_1_2.txt

python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_2.txt change_0_2.txt
8605 changes written to change_0_2.txt
* count_ab_2.txt, abdiff_2_A0.txt
python count_ab.py temp_pwg_2.txt count_ab_2.txt
1129105 read from temp_pwg_2.txt
785 lines written to count_ab_2.txt
185563 = total number of <ab>X</ab>

python abdiff.py count_ab_2.txt count_ab_A0.txt abdiff_2_A0.txt
785 read from count_ab_2.txt
788 read from count_ab_A0.txt
795 total distinct abbreviations
795 lines written to abdiff_2_A0.txt

* pwgab_input_new_2.txt
# tooltips file from issue174/tips
cp ../issue174/tips/pwgab_input_new.txt pwgab_input_new_0.txt

python update_tips.py pwgab_input_new_0.txt count_ab_2.txt pwgab_input_new_2.txt
786 lines read from pwgab_input_new_0.txt
785 lines read from count_ab_2.txt
LEX: <id>adj.</id> <disp>adjectivisch - adjective</disp>  <N>0</N> CHECKED
LEX: <id>adv.</id> <disp>Adverb adverb</disp>  <N>0</N> CHECKED
LEX: <id>f.</id> <disp>femininum - feminine</disp>  <N>0</N> CHECKED
LEX: <id>interj.</id> <disp>Interjection - interjection </disp>  <N>0</N> CHECKED
LEX: <id>m.</id> <disp>masculinum - masculine</disp>  <N>0</N> CHECKED
LEX: <id>n.</id> <disp>neutrum - neuter</disp>  <N>0</N> CHECKED
791 lines written to pwgab_input_new_2.txt

* pwgab_input_new.txt
cp pwgab_input_new_2.txt pwgab_input_new.txt
# manual edit of pwgab_input_new.txt
# Search for '?'  and correct
# *  ' -> &#39;  in pwgab_input_new.txt

* install pwgab_input_new.txt into csl-pywork
cp pwgab_input_new.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pwg/pywork/pwgab/pwgab_input.txt

sh redo_new.sh 2
* install to Github: csl-orig, csl-pywork\
* unresolved
<ls>PAT. a. a. O. 1,223,a.</ls>  700+, 
223 matches for "<ls n="PAT. a. a. O."
---
Vp. (2te Aufl.)  pwgauth:  ?Vishnu purana, 2nd edition? VP^2 in pwk?
---
<ab>d.</ab> <lex>f.</lex> <ab>W.</ab> (2)  
---
Mark as <ab>X</ab>
ebend.   (~ 2600)
     Tooltip exists: "ebenda - ibid. (ibidem) - in the same source"
ved. (~550) Tooltip =  vedisch - Vedic

---

* INSTALLATION
* sync to github:

------------------
# csl-orig temp_pwg_2
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue178/
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt 
cd /c/xampp/htdocs/cologne/csl-orig/
git add .
git commit -m "PWG abbreviations
Ref: https://github.com/sanskrit-lexicon/pwg/issues/178 temp_pwg_2"
#  1 file changed, 8605 insertions(+), 8605 deletions(-)
git push
# remote: warning: File v02/pwg/pwg.txt is 50.88 MB; 
# this is larger than GitHub's recommended maximum file size of 50.00 MB

-------------------
# csl-pywork  pwgab_input_new.txt
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue178/

cp pwgab_input_new.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pwg/pywork/pwgab/pwgab_input.txt
cd /c/xampp/htdocs/cologne/csl-pywork/
git add .
git commit -m "PWG abbreviations - tooltips
Ref: https://github.com/sanskrit-lexicon/pwg/issues/178 pwgab_input_new.txt"
git push

cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue178/

---------------------------------------------------
* sync to Cologne, pull changed repos, redo display
---------------
csl-orig #pull
csl-corrections #pull

---------------
# update displays for pwg
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/

-----------------------------------------------------
* sync issue178/ to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue178/
git pull
git add .
git commit -m "issue178 PWG abbreviations. #178"
git push

------------------------------------------------------------
************************************************************
* THE END
