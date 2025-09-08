issue167/readme.txt
09-06-2025 begun ejf
NIRUKTA

Ref: https://github.com/sanskrit-lexicon/PWG/issues/167

This issue167 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue167

-----------------
pdf: /e/pdfwork/nirukta/nirukta.pdf

Two Index files

cp /e/pdfwork/nirukta/nirukta.txt nirukta.txt
cp /e/pdfwork/nirukta/Naighantuka.txt naighantuka.txt

cp nirukta.txt index_nir.txt

cp naighantuka.txt index_naigh.txt
----------------------------------------
# get temporary local copy of koshas
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw_0.txt

----------------------------------------
Reference forms in koshas
--- pwg
NIR. Nirukta
2954 matches in 2952 lines for "<ls>NIR\. [0-9]+,[0-9]+  <<< index_nir app1
Preface forms
29 matches for "<ls>NIR\. [IVXL]+"   # preface  app0
7 matches for "<ls>NIR. S\. [0-9]+
4 matches for "<ls>NIR. S\. [IVXL]+
4 matches for "<ls>NIR. Einl\. [IVXL]+"

NAIGH.
1366 matches for "<ls>NAIGH\. "
1356 matches for "<ls>NAIGH\. [0-9]+,[0-9]+"  index_naigh  app2

--- pw
100 matches for "<ls>NIR\. [0-9]+,[0-9]+" in buffer: temp_pw_0.txt
10 matches for "<ls>NAIGH\. [0-9]+,[0-9]+"

  
--- pwkvn
18 matches for "<ls>NIR\. [0-9]+,[0-9]+" in buffer: temp_pwkvn_0.txt
0 matches for "<ls>NAIGH\. [0-9]+,[0-9]+"

--- sch
19 matches for "<ls>Nir\. [0-9]+,[0-9]+" in buffer: temp_sch_0.txt
1 matches for "<ls>Nigh\. [0-9]+,[0-9]+"

--- mw
476 matches for "<ls>Nir\. [ivxl]+, *[0-9]+" in buffer: temp_mw_0.txt
439 matches for "<ls>Naigh\. [ivxl]+, *[0-9]+"


=============================================
index_nir.txt
page
kanda   # not used in links, a string
adhy
fromv
tov
ipage
Remarks
Note: remove 6 lines with no references

links use adhy,verse

---------------------

# Prepare index_nir.js

python make_js_index_nir.py index_nir.txt index_nir.js

=============================================
index_naigh.txt
page
adhy
fromv
tov
ipage
Remarks
Note: remove 4 lines with no references

links use adhy,verse

---------------------
# Prepare index_naigh.js
python make_js_index_naigh.py index_naigh.txt index_naigh.js

==========================================
apps in sanskrit-lexicon-scans

https://github.com/sanskrit-lexicon-scans/nirukta
# initialize local repo, where the link target apps will be installed.
cd /c/xampp/htdocs/sanskrit-lexicon-scans/
git clone git@github.com:sanskrit-lexicon-scans/nirukta.git

# edit README.md 

# Install apps in nirukta repo
readme_app0.txt  internal page
readme_app1.txt  adhy,verse  nirukta
readme_app2.txt  adhy,verse  naighantuka


# Install app1 as target for NIR. N,N
see readme_app1.txt

# Install app2 as target for NAIGH. N,N
see readme_app2.txt

========================================
--- links from koshas to app
pwg, pw, pwkv, sch,mw
see readme_csl-websanlexicon.txt
 basicadjust.php
START
========================================
----------------------------------------
# Begin checking consistency with dictionaries

See readme_check.txt

----------------------

==================================================
splitting kosha refs to activate more links.

See readme_split.txt


---------------------------------------------------
---- documentation in change files
--- pwg
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
104 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
398 changes written to change_pwg_2.txt

--- pw
python diff_to_changes_dict.py temp_pw_0.txt temp_pw_1.txt change_pw_1.txt
2 changes written to change_pw_1.txt

python diff_to_changes_dict.py temp_pw_1.txt temp_pw_2.txt change_pw_2.txt
2 changes written to change_pw_2.txt

--- pwkvn
python diff_to_changes_dict.py temp_pwkvn_0.txt temp_pwkvn_1.txt change_pwkvn_1.txt
1 changes written to change_pwkvn_1.txt

python diff_to_changes_dict.py temp_pwkvn_1.txt temp_pwkvn_2.txt change_pwkvn_2.txt
0 changes written to change_pwkvn_2.txt

--- sch
python diff_to_changes_dict.py temp_sch_0.txt temp_sch_1.txt change_sch_1.txt
2 changes written to change_sch_1.txt

python diff_to_changes_dict.py temp_sch_1.txt temp_sch_2.txt change_sch_2.txt
1 changes written to change_sch_2.txt

--- mw
python diff_to_changes_dict.py temp_mw_0.txt temp_mw_1.txt change_mw_1.txt
4 changes written to change_mw_1.txt

# no temp_mw_2.txt
#python diff_to_changes_dict.py temp_mw_1.txt temp_mw_2.txt change_mw_2.txt
# changes written to change_mw_2.txt


============================================================
sync to github:
------------------
# csl-orig # git pull
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue167
diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
diff temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt | wc -l
diff temp_pwkvn_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt | wc -l
diff temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt | wc -l
diff temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt | wc -l
#0  as expected

cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "nirukta link target, revisions to pwg, pw, pwkvn, sch, mw
Ref: https://github.com/sanskrit-lexicon/pwg/issues/167"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue167

------------------
# csl-websanlexicon
cd /c/xampp/htdocs/cologne/csl-websanlexicon/
git pull
git add .
git commit -m "nirukta link target, revisions to pwg, pw, pwkvn, sch, mw
Ref: https://github.com/sanskrit-lexicon/pwg/issues/167"

git push
cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
sh apidev_copy.sh

cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue167


------------------
# csl-apidev
cd /c/xampp/htdocs/cologne/csl-apidev/
git pull
git add .
git commit -m "nirukta link target, revisions for  pwg, pw, pwkvn, sch, mw
Ref: https://github.com/sanskrit-lexicon/pwg/issues/167"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue167



---------------------------------------------------
sync Cologne to Github, pull changed repos
redo the pwg displays

---------------
csl-orig # pull
csl-websanlexicon # pull
csl-apidev # pull

# regenerate displays for pwg, pw, pwkvn, sch, mw

cd csl-pywork/v02

sh generate_dict.sh pwg  ../../PWGScan/2020/
sh generate_dict.sh pw  ../../PWScan/2020/
sh generate_dict.sh pwkvn  ../../PWKVNScan/2020/
sh generate_dict.sh sch  ../../SCHScan/2020/
sh generate_dict.sh MW  ../../MWScan/2020/

--------------------------------------------

# sync this PWG (issue167)
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue167
git pull
git add .
git commit -m "#167 #160"
git push

-------------------------------------
# sync this repo to github
====================================
THE END

