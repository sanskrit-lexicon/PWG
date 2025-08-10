issue157/readme.txt
08-05-2025 begun ejf
VIKRAMORVAŚĪ

Ref: https://github.com/sanskrit-lexicon/PWG/issues/125

This issue157 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue157

-----------------
pdf: /e/pdfwork/vikramor/Vikramorvaśī (1846).pdf

Index file

cp /e/pdfwork/vikramor/Vikramorvasi.Index.tsv index_orig.txt

cp index_orig.txt index.txt
--  edit index.txt to remove last 6 lines (epage >= 111)
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
647 matches for "<ls>VIKR. [0-9]+,[0-9]+"
1442 matches for "<ls>VIKR. [0-9]+[^,]

27 matches for "<ls>VIKRAM. [0-9]+,[0-9]+"
21 matches for "<ls>VIKRAM. [0-9]+[^0-9,]

--- pw
26 matches for "<ls>VIKR. [0-9]+,[0-9]+"
56 matches for "<ls>VIKR. [0-9]+[^,]

4 matches for "<ls>VIKRAM. [0-9]+,[0-9]+"
6 matches for "<ls>VIKRAM. [0-9]+[^0-9,]

1 instance <ls>VIKR. drāv. 654,24</ls>
  L=99767, vA  Not implemented
  (p. 654 not found in Bollensen pdf ?)
  
--- pwkvn
5 matches for "<ls>VIKR. [0-9]+,[0-9]+"
4 matches for "<ls>VIKR. [0-9]+[^,]

4 matches for "<ls>VIKRAM. [0-9]+,[0-9]+"
0 matches for "<ls>VIKRAM. [0-9]+[^0-9,]

--- sch
5 matches for "<ls>Vikr. [0-9]+,[0-9]+"
4 matches for "<ls>Vikr.  [0-9]+[^0-9,]

4 matches for "<ls>Vikram. [0-9]+,[0-9]+"
2 matches for "<ls>Vikram. [0-9]+[^0-9,]

--- mw
0 matches for "<ls>Vikr. [0-9]+,[0-9]+"
69 matches for "<ls>Vikr. [iv]+, *[0-9]+"
3 matches for "<ls>Vikr.  [0-9]+[^0-9,]

0 matches for "<ls>Vikram. [0-9]+,[0-9]+"
0 matches for "<ls>Vikram. [0-9]+[^0-9,]

--------------------------------------
parameters:  
1:  verse  (continuous across anka).
2:  ipage,line-number

---------------------
index_orig.txt format observations
format 5 fields tab-separated values
page
anka
fromv
tov
ipage
remarks  # optional.

Note: '---' changed to '0' .
such lines will never be used in the apps
-----------------------------------
# Prepare index.js
# Note that the verses are continuous through all adhyAyas.
python make_js_index.py index.txt index.j

==========================================
apps in sanskrit-lexicon-scans

https://github.com/sanskrit-lexicon-scans/vikramor
# initialize local repo, where the link target apps will be installed.
cd /c/xampp/htdocs/sanskrit-lexicon-scans/
git clone git@github.com:sanskrit-lexicon-scans/vikramor.git

# edit README.md 

# Install apps in vikramor repo
readme_app0.txt  internal page
readme_app1.txt  verse
readme_app2.txt  internal page,line number


# Install app1 as target for Variant 1 
see readme_app1.txt

# Install app2 as target for Variant 2
see readme_app2.txt

========================================
--- links from koshas to app
pwg, pw, pwkv, sch.  (MW doesn't work with this Bollensen pdf.
see readme_csl-websanlexicon.txt
 basicadjust.php

========================================
----------------------------------------
# Begin checking consistency with dictionaries


----------------------------------------
Make misc checks between pwg , the pdf and index

----------------------
 'pwg1a':r'<ls>VIKR. ([0-9]+)[^0-9,]',

python generate_random.py ALL pwg1a temp_pwg_0.txt index.txt check_pwg1a_ALL.txt check_pwg1a_nopagerec.txt
regex_raw = <ls>VIKR. ([0-9]+)[^0-9,]
found 871 instances in kosha
found 133 distinct in kosha
write_examples: 871 written to check_pwg1a_ALL.txt
0 instances of 'pagerec not found'

----------------------
 'pwg1b':r'<ls>VIKRAM. ([0-9]+)[^0-9,]',

python generate_random.py ALL pwg1b temp_pwg_0.txt index.txt check_pwg1b_ALL.txt check_pwg1b_nopagerec.txt
regex_raw = <ls>VIKRAM. ([0-9]+)[^0-9,]
found 21 instances in kosha
found 20 distinct in kosha
write_examples: 21 written to check_pwg1b_ALL.txt
0 instances of 'pagerec not found'

----------------------
 'pwg2a':r'<ls>VIKR. ([0-9]+),([0-9]+)'

python generate_random.py ALL pwg2a temp_pwg_0.txt index.txt check_pwg2a_ALL.txt check_pwg2a_nopagerec.txt

regex_raw = <ls>VIKR. ([0-9]+),([0-9]+)
found 647 instances in kosha
found 364 distinct in kosha
write_examples: 647 written to check_pwg2a_ALL.txt
1 instances of 'pagerec not found'
write_examples: 1 written to check_pwg2a_nopagerec.txt

PRINT CHANGE
101446 : Sram : <ls>VIKR. 18,113.</ls> : <ls>VIKR. 98,13.</ls> :
Ref: https://github.com/sanskrit-lexicon/PWG/issues/157#issuecomment-3163863095
In प्राकृतभाषाव्याख्या  section.
Note app0 and app2 would need to change to include ipage from 90-130
The internal page-numbering actually extends to ipage = 608.
  epage = ipage + 21
----------------------
 'pwg2b':r'<ls>VIKRAM. ([0-9]+),([0-9]+)'

python generate_random.py ALL pwg2b temp_pwg_0.txt index.txt check_pwg2b_ALL.txt check_pwg2b_nopagerec.txt
regex_raw = <ls>VIKRAM. ([0-9]+),([0-9]+)
found 27 instances in kosha
found 27 distinct in kosha
write_examples: 27 written to check_pwg2b_ALL.txt
0 instances of 'pagerec not found'


==================================================
splitting kosha refs for pwg

# lsfix2 option colebr for lsfix2_parm.py, 

# checks with lscode='VIKR.', 1 or 2 paramters
python lsfix2.py vikr temp_pwg_0.txt lsfix2_vikr_0.txt
1561 lines written to lsfix2_vikr_0.txt
(True, 1) 862
(True, 2) 615
('fixed', 2) 47
('fixed', 1) 17
(None, 1) 9
(False, 1) 11

edit temp_pwg_1.txt
These excluded as 'skip' in lsfix2_parm
None	1	66379	<ls>VIKR. (LENZ) 93,16.</ls>	
None	1	112357	<ls>VIKR. XV. fg.</ls>	  ref. to preface

print change
24427 : caccapuwa :
old: <ls>VIKR. ed.</ls> <ls>BOLL. S. 513.</ls>
new: <ls>VIKR. 513,21</ls>
---
from pwg2a above
101446 : Sram : <ls>VIKR. 18,113.</ls> : <ls>VIKR. 98,13.</ls> :
----
print change
<ls>VIKR. 64,3.</ls> <ls n="">6.</l S. 519.</ls>
24551 : caturasra :
old: VIKR. 64,3. 6. S. 519.
new: VIKR. 64,3. 6. 519,12.
----
print change
64206 : apahastay :
old: <ls>VIKR. ed.</ls> <ls>BOLL. S. 253.</ls>
new: <ls>VIKR. 253,27.</ls>
---- 
print change
93946 : vizkamBa :
old: <ls>VIKR. S. 369.fg.</ls>
new: <ls>VIKR. 369,24. fg.</ls>

---------------------------
rerun with temp_pwg_1.txt

python lsfix2.py vikr temp_pwg_1.txt lsfix2_vikr_1.txt
1569 lines written to lsfix2_vikr_1.txt
(True, 1) 871
(True, 2) 633
('fixed', 2) 48
('fixed', 1) 17

------------------------------------------
Splitting with lscode 'VIKRAM.'
python lsfix2.py vikram temp_pwg_1.txt lsfix2_vikram_1.txt
50 lines written to lsfix2_vikram_1.txt
('fixed', 2) 4
(True, 2) 24
(True, 1) 21
('fixed', 1) 1

Nothing more to fix!

==========================================
# concatenate the lsfix2 files
cat lsfix2_vikr_1.txt  lsfix2_vikram_1.txt > lsfix2_1_all.txt

# apply the 'fixed' cases to pwg
python dict_replace2.py temp_pwg_1.txt lsfix2_1_all.txt temp_pwg_2.txt
1619 kept.
1619 lines read from lsfix2_1_all.txt
70 lines to change
apply_repls: 70 lines changed

======================================


-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue157
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue157
-- end of 'remake xml ...'

---------------------------
How to handle xmlchk error (documentation)
1. Open /c/xampp/htdocs/cologne/pwg/pywork/pwg.xml in Emacs
 use C-cC-n to find xml errors.
 Make correction in temp_pwg_1.txt
 When done
2. rerun next two
python lsfix.py dummy temp_pwg_1.txt lsfix_1.txt 
python dict_replace.py temp_pwg_1.txt lsfix_1.txt temp_pwg_2.txt
3. Redo the 'remake xml ...' steps.
   continue these steps until xmlchk  says 'ok'.
---- end of 'How to handle xmlchk error'
-------------------------------------------------------------
Create Some documentation files

python lsfix2.py vikr temp_pwg_2.txt lsfix2_vikr_2.txt
1657 lines written to lsfix2_vikr_2.txt
(True, 1) 907
(True, 2) 750

python lsfix2.py vikram temp_pwg_2.txt lsfix2_vikram_2.txt
55 lines written to lsfix2_vikram_2.txt
(True, 2) 32
(True, 1) 23

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
18 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
70 changes written to change_pwg_2.txt

============================================================
sync to github:
------------------
# csl-orig # git pull
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue157
diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue157 VIKRAMORVAŚĪ link target correction #157"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue157

------------------
# csl-websanlexicon
cd /c/xampp/htdocs/cologne/csl-websanlexicon/
git pull
git add .
git commit -m "issue157 VIKRAMORVAŚĪ link target. 
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue157

sh apidev_copy.sh

------------------
# csl-apidev
cd /c/xampp/htdocs/cologne/csl-apidev/
git pull
git add .
git commit -m "issue157 VIKRAMORVAŚĪ link target. 
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue157

------------------
# csl-corrections
cd /c/xampp/htdocs/cologne/csl-corrections/
git pull
git add .
git commit -m "issue157 VIKRAMORVAŚĪ link target. 
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue157

---------------------------------------------------
sync Cologne to Github, pull changed repos
redo the pwg displays

---------------
csl-orig # pull
csl-corrections # pull
csl-websanlexicon # pull
csl-apidev # pull
-------------------------------------
# sync Cologne to github
# sync to cologne
# regenerate displays for pwg, pw, pwkvn, sch, [mw not required]

cd csl-pywork/v02

sh generate_dict.sh pwg  ../../PWGScan/2020/
sh generate_dict.sh pw  ../../PWScan/2020/
sh generate_dict.sh pwkvn  ../../PWKVNScan/2020/
sh generate_dict.sh sch  ../../SCHScan/2020/

--------------------------------------------

# sync this PWG (issue157)
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue157
git pull
git add .
git commit -m "issue157 #157 #160"
git push

-------------------------------------
# sync this repo to github
====================================
THE END

