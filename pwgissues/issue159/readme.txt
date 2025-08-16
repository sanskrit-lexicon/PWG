issue159/readme.txt
08-10-2025 begun ejf
AITAREYABRĀHMAṆA

Ref: https://github.com/sanskrit-lexicon/PWG/issues/159

This issue159 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159

-----------------
pdf: /e/pdfwork/aitbr/aitbr_1.pdf
     /e/pdfwork/aitbr/aitbr_2.pdf

Index file: pertains only to vol. 1.
Vol 2 is for translation, notes.  Currently not indexed.

The final version of index will be named index.txt

There were several revisons resulting in final version of index.txt .
----------------------------------------
# get temporary local copy of koshas
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw_0.txt

----------------------------------------
All the 5 koshas (pwg, pw, pwkvn, sch, mw) have references
to AITAREYABRĀHMAṆA  with either 2 or three parameters.
There are also slight variations in the lscode

We learned that the 3-parameter references are referring
to the Aufrecht edition.  pancika, kandika, khanda  Where khanda is a
sequence number (within kandika) provided by Aufrecht.
We will make a separate link target (aitbr_auf); the work on
this aufrecht edition will be in a separate directory
In local file system, 
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159/auf
See readme.txt in this directory.

The rest of this discussion is primarily based on the Haug edition.


Reference forms in koshas
--- pwg  AIT. BR.
3726  nparm=2
   4  nparg=3

** (4055) AIT. BR. with 2 numeric parameters 
** (7) AIT. BR. with 3 numeric parameters 

--- pw AIT. BR.
 127 with nparm=3
  95 nparm=2
 
--- pwkvn AIT. BR.
  39 nparm=3
   3 nparm=2
   
--- sch Ait. Br.
   3 nparm=2
  38 nparm=3
  
--- mw  AitBr.
 168 R,N
 116 R,N,N

--------------------------------------
index.txt format observations
format 7 fields tab-separated values
vol  (=I)
page N
pancika
adhyaya  not used in apps
fromv == kandika
tov   == kandika
ipage
remarks  # optional.

-----------------------------------
# Prepare index.js
# Note that the verses are continuous through pancika.
python make_js_index.py index.txt index.j
252 Success: Page records read from index.txt
json data written to index.js
pagerecs passes check1_pancika
pagerecs passes check1_kandika

==========================================
apps in sanskrit-lexicon-scans

https://github.com/sanskrit-lexicon-scans/aitbr
# initialize local repo, where the link target apps will be installed.
cd /c/xampp/htdocs/sanskrit-lexicon-scans/
git clone git@github.com:sanskrit-lexicon-scans/aitbr.git

# edit README.md 

# Install apps in aitbr repo
readme_app0.txt  internal page
readme_app1.txt  pancika,kandika
readme_app2.txt  3-parameter.  Not used in kosha references to Haug edition

========================================
--- links from koshas to app
pwg, pw, pwkv, sch, mw
see readme_websanlexicon.txt

========================================
----------------------------------------
# Begin checking consistency with dictionaries
# using (a) generate_random.py and (b) lsfix2.py (with lsfix2_parm.py)

see readme_check.txt

-------------
print changes (to document in csl-corrections)
pwg
12865 : UvaDya : AIT. BR. 2,6,11 : AIT. BR. 2,6. 11 : PRINT CHANGE (Andhrabharati)

------------
pwg 'other' references (prob. to commentary in volume 2 of Haug edition)
None	2	505611	<ls>AIT. BR. S. 120</ls>	
None	2	505612	<ls n="AIT. BR.">S. 347, Anm.</ls>	
None	2	1008048	<ls>AIT. BR. Comm. 1,1.</ls>	

==================================================
Documentation 
---------------------------------------------------
pwg
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
113 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
386 changes written to change_pwg_2.txt

python lsfix2.py pwg temp_pwg_2.txt lsfix2_pwg_2.txt
5176 lines written to lsfix2_pwg_2.txt
(True, 2) 5172
(None, 2) 3
(True, 3) 1

---------------------------------------------------
pw
python diff_to_changes_dict.py temp_pw_0.txt temp_pw_1.txt change_pw_1.txt
1 change written to change_pw_1.txt

python diff_to_changes_dict.py temp_pw_1.txt temp_pw_2.txt change_pw_2.txt
11 changes written to change_pw_2.txt

python lsfix2.py pw temp_pw_2.txt lsfix2_pw_2.txt
241 lines written to lsfix2_pw_2.txt
(True, 2) 104
(True, 3) 137

---------------------------------------------------
pwkvn  no changes

---------------------------------------------------
sch
python diff_to_changes_dict.py temp_sch_0.txt temp_sch_1.txt change_sch_1.txt
3 change written to change_sch_1.txt

python diff_to_changes_dict.py temp_sch_1.txt temp_sch_2.txt change_sch_2.txt
1 changes written to change_sch_2.txt

python lsfix2.py sch temp_sch_2.txt lsfix2_sch_2.txt
45 lines written to lsfix2_sch_2.txt
(True, 3) 42
(True, 2) 3

---------------------------------------------------
mw
python diff_to_changes_dict.py temp_mw_0.txt temp_mw_1.txt change_mw_1.txt
2 change written to change_mw_1.txt

No temp_mw_2.txt since lsfix2 doesn't work since it can't handle roman first parameter

===========================================================
sync to github:
  csl-orig
  csl-corrections (pwg see above PRINT CHANGE)
  csl-websanlexicon
  csl-apidev

------------------
# csl-orig # git pull
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159
diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
diff temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt | wc -l
diff temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt | wc -l
diff temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt | wc -l
#0  as expected

cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "AITAREYABRĀHMAṆA (Haug) link target correction
Ref: https://github.com/sanskrit-lexicon/PWG/issues/159"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159

------------------
# csl-websanlexicon
cd /c/xampp/htdocs/cologne/csl-websanlexicon/
git pull
git add .
git commit -m "AITAREYABRĀHMAṆA (Haug) link target aitbr. 
Ref: https://github.com/sanskrit-lexicon/pwg/issues/159"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159

sh apidev_copy.sh

------------------
# csl-apidev
cd /c/xampp/htdocs/cologne/csl-apidev/
git pull
git add .
git commit -m "AITAREYABRĀHMAṆA (Haug) link target aitbr. 
Ref: https://github.com/sanskrit-lexicon/pwg/issues/159"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159

------------------
# csl-corrections
cd /c/xampp/htdocs/cologne/csl-corrections/
git pull
git add .
git commit -m "AITAREYABRĀHMAṆA (Haug) link target aitbr. 
Ref: https://github.com/sanskrit-lexicon/pwg/issues/159"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159

---------------------------------------------------
sync Cologne to Github, pull changed repos
---------------
csl-orig # pull
csl-corrections # pull
csl-websanlexicon # pull
csl-apidev # pull
-------------------------------------
# regenerate displays for pwg, pw, pwkvn, mw, [mw not required]

cd csl-pywork/v02

sh generate_dict.sh pwg  ../../PWGScan/2020/
sh generate_dict.sh pw  ../../PWScan/2020/
sh generate_dict.sh pwkvn  ../../PWKVNScan/2020/
sh generate_dict.sh sch  ../../SCHScan/2020/
sh generate_dict.sh mw  ../../MWScan/2020/

--------------------------------------------

# sync this repo PWG (issue159) to github
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159
git pull
git add .
git commit -m "issue159 #159"
git push

====================================
THE END

