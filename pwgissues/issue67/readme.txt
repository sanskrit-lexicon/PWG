
PWG/pwgissues/issue67
German word corrections provided by Thomas.
  pre_change.txt 134
Separate into 'regular' and 'irregular'
  pre_change_regular.txt  120  
  pre_change_irregular.txt 14  (for manual corrections)
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue67

Start with pwg.txt
at commit 6678da906d50216059cfa2728cd8ec581e0da97d of csl-orig:

cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt


Try borrow code from
 /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue101

cp /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue101/german1/make_change_regular.py .
cp /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue101/german1/digentry.py .

# programmatic changes for regular
python make_change_regular.py  pre_change_regular.txt temp_pwg_0.txt change_regular.txt
120 records read from pre_change_regular.txt
1149413 lines read from temp_pwg_0.txt
122736 entries found
120 cases written to change_regular.txt

# Apply the regular changes
python updateByLine.py temp_pwg_0.txt change_regular.txt temp_pwg_1.txt
1149413 records written to temp_pwg_1.txt
120 change transactions from change_regular.txt

# make the 'irregular' changes
cp temp_pwg_1.txt temp_pwg_2.txt

# manual changes to temp_pwg_2.txt from pre_change_irregular.txt

# generate changes
python python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_irregular.txt
14 changes written to change_irregular.txt

# print changes
-----
<L>98274<pc>7-0107<k1>SalAka
Durchboren -> Durchbohren ;; print error
-----
<L>20580<pc>2-0571<k1>kzetra
Eheman -> Ehemann ;; print error
-----
<L>18181<pc>2-0361<k1>kulya
condolance -> condolence [misprint]
-----
<L>102803<pc>7-0462<k1>saMlakzya
wahrnembar ->  wahrnehmbar ;;misprint corrected
-----
<L>102803<pc>7-0462<k1>saMlakzya
wahrnembarer -> wahrnehmbarer ;;misprint corrected
-----
<L>14199<pc>2-0010<k1>kakza
wight -> weight ;; misprint corrected

=====================================================================

# do local install
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt

# check local installation
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue67/

# push repositories to GitHub
----- csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git pull # check for other revisions. 
git status  # v02/pwg/pwg.txt
git add .
git commit -m "PWG: German word corrections
  Ref: https://github.com/sanskrit-lexicon/PWG/issues/67"
# 134 lines changed
git push

--------------------------------------------
# update cologne displays
# login to cologne
---- csl-orig
git pull
#161 lines changed

---- csl-pywork
cd v02
git pull # no change
sh generate_dict.sh pwg  ../../PWGScan/2020/


******************************************************
prepare temp_pwg_2_hk.txt for Thomas
-------------------------------------------
12-08-2023
Regenerate temp_pwg_2_hk.txt from temp_pwg_2.txt
(refer c:/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue95/pwtranscode/)

cp temp_pwg_2.txt /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue95/pwtranscode/temphk/temp_pwg_2.txt
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue95/pwtranscode/

python pw_transcode.py slp1 hk temphk/temp_pwg_2.txt temphk/temp_pwg_2_hk.txt
# check invertibility
python pw_transcode.py hk slp1 temphk/temp_pwg_2_hk.txt temphk/temp_pwg_2_hk_slp1.txt
diff temphk/temp_pwg_2.txt temphk/temp_pwg_2_hk_slp1.txt | wc -l
# 92  - known differences
# mv temp_pwg_2_hk.txt back to german1 directory
mv temphk/temp_pwg_2_hk.txt /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue67/
# remove unneeded
rm temphk/temp_pwg_2.txt
rm temphk/temp_pwg_2_hk_slp1.txt

# return to this german1 directory
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue67

zip temp_pwg_2_hk.zip temp_pwg_2_hk.txt change_regular.txt change_irregular.txt
Send temp_pw_2_hk.zip to thomas

-----------------------------------------------------
--------------------------------------------
# sync this repository to Github
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue67

git add .
git commit -m "#67"
git push

make comment in https://github.com/sanskrit-lexicon/PWG/issues/67
