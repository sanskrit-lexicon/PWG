* *******************************************************
*  PREVIOUS WORK TO IGNORE FOR NOW
This work was not productive.  
* *******************************************************
* temp_pwg_A0.txt  
Ref: https://github.com/sanskrit-lexicon/PWG/issues/180#issuecomment-4565098273

 pwg_(AB)_v1b.txt
Ref: https://github.com/user-attachments/files/28350617/pwg_.AB._v1b.zip
Renamed to temp_pwg_A0.txt




* temp_pwg_0b_base1 and 
* programs from issue174, issue178
# count_lex_py counts of <lex>X</lex> from a given version of pwg.txt
python count_lex.py <PWG> <count_lex_X.txt>

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
* Align <lex> tags
python count_lex.py temp_pwg_0.txt count_lex_0.txt
1129105 read from temp_pwg_0.txt
7 lines written to count_lex_0.txt
131189 = total number of <lex>X</lex>


python count_lex.py temp_pwg_A0.txt count_lex_A0.txt
591087 read from temp_pwg_A0.txt
17 lines written to count_lex_A0.txt
130842 = total number of <lex>X</lex>


# adjustment of lex tags in cdsl version
python change_1.py temp_pwg_0.txt temp_pwg_1.txt
1129105 lines 
123366 metalines
669 lines changed

python change_A1.py temp_pwg_A0.txt temp_pwg_A1.txt
591087 lines read from temp_pwg_A0.txt
122738 metalines
921 lines changed

python count_lex.py temp_pwg_1.txt count_lex_1.txt
13 lines written to count_lex_1.txt

python count_lex.py temp_pwg_A1.txt count_lex_A1.txt
13 lines written to count_lex_A1.txt

python abdiff.py count_lex_1.txt count_lex_A1.txt lexdiff_1_A1.txt

* INSTALLATION
* sync to github:

------------------
# csl-orig temp_pwg_2
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue180/
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt 
cd /c/xampp/htdocs/cologne/csl-orig/
git add .
git commit -m "PWG abbreviations
Ref: https://github.com/sanskrit-lexicon/pwg/issues/180 temp_pwg_2"
#  1 file changed, 8605 insertions(+), 8605 deletions(-)
git push
# remote: warning: File v02/pwg/pwg.txt is 50.88 MB; 
# this is larger than GitHub's recommended maximum file size of 50.00 MB

-------------------
# csl-pywork  pwgab_input_new.txt
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue180/

cp pwgab_input_new.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pwg/pywork/pwgab/pwgab_input.txt
cd /c/xampp/htdocs/cologne/csl-pywork/
git add .
git commit -m "PWG abbreviations - tooltips
Ref: https://github.com/sanskrit-lexicon/pwg/issues/180 pwgab_input_new.txt"
git push

cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue180/

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
* sync issue180/ to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue180/
git pull
git add .
git commit -m "issue180 PWG abbreviations. #180"
git push

------------------------------------------------------------
************************************************************
