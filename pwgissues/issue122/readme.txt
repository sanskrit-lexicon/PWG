issue122/readme.txt
03-13-2025 begun ejf
05436 MĀRK. P. MĀRKĀṆḌEYAPURĀṆA


Ref: https://github.com/sanskrit-lexicon/PWG/issues/122

This issue122 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue122

-----------------
pdf:
/e/pdfwork/markandeyap/MarkandeyaPurana-KmBanerjee1862bis.pdf


----------------------------------------
Selected pages from the pdf.
page
1 = MĀRKĀṆḌEYAPURĀṆA, edited K. M. BANERJEA, Calcutta, 1862
2 = Introduction
...
33 = end of introduction
34 starts  ipage = 1
...


----------------------------------------
Index file
  MarkandeyaPurana-KmBanerjee1862bis.index.v1.xlsx
  convert to tsv (Google)
  rename index.txt  (save copy as index_orig.txt)
  remove extra tabs at end of each line


MarkandeyaPurana-KmBanerjee1862bis.Notes.docx
problems noted:
* Page 682 verse 36 followed by 40
* At page 602 finished chapter 115
It is expected that there will be a 116 chapter.
But at page 610 The link that ended section 117

---------------------
index.txt format observations
format 5 fields tab-separated values
page
adhy
fromv
tov
ipage

---------------------
changes to index.txt
1. remove first line: 34	0	1	2	1
  This is a prastAva   -- marked as adhyAya = 0
2. remove comment at line 740
  682	135	31	37	649	37 error numeration as 40
3. remove lines at end  Not sure here?
687	--	--	--	654	the beginning of application 1
688	--	--	--	655
689	--	--	--	656
690	--	--	--	657
691	--	--	--	658
692	--	--	--	659
693	--	--	--	660
NOTE:
 a. page 687: blank
 b. pages 688-693  'Different reading at the end'
4. lnum=658, line=610      118     1       5       577
   previous adhyAya 116.
   See docx comment above
602	116	1	5	569
5.  typo
old: 580	109	55b	63	547
new: 580	109	54b	63	547

----------------------------------------
# Prepare index.js
python make_js_index.py index.txt index.js
744 Success: Page records read from index.txt
json data written to index.js
check1_adhy known anomaly
prev line: 610  116     74b     76      577
 cur line: 610  118     1       5       577
pagerecs passes check1_adhy
check1 finds no problems

----------------------------------------
# get temporary local copy of pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt

----------------------------------------
Make misc checks between pwg , the pdf and index

python generate_random.py 10 pwg temp_pwg.txt index.txt check_pwg.txt
1132566 lines read from temp_pwg.txt
123366 entries found
regex_raw = <ls>MĀRK. P. ([0-9]+),([0-9]+)
found 5126 instances adhy,verse in kosha
found 3006 distinct adhy,verse in kosha
10 examples found
10 written to check_pwg.txt

edit check_pwg.txt and manually check comparison
All in this random sample checked.

--------------------------------------------
checks on adhyAya 116
36 matches for "<ls>MĀRK. P. 116,

python generate_random.py 5 pwg116 temp_pwg.txt index.txt check_pwg_116.txt
  All in this random sample checked

--------------------------------------------
checks on adhyAya 118
50 matches for "<ls>MĀRK. P. 118,

python generate_random.py 5 pwg118 temp_pwg.txt index.txt check_pwg_118.txt
  All in this random sample checked
  
--------------------------------------------
checks on aDyAya 117
 aDyAya 117 is missing in pdf.
 no matches for "<ls>MĀRK. P. 117," in temp_pwg.txt

 Neither pdf nor pwg have references to aDyAya 117 !

----------------------------------------
# get temporary local copy of pw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt

166 matches for "<ls>MĀRK. P. [0-9]+,[0-9]+" in buffer: temp_pw.txt

Random check of links:  (~160 links)

python generate_random.py 5 pw temp_pw.txt index.txt check_pw.txt

Links check for pw

----------------------------------------
# get temporary local copy of pwkvn.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn.txt

35 matches for "<ls>MĀRK. P. [0-9]+,[0-9]+" in buffer: temp_pwkvn.txt

Random check of links:

python generate_random.py 5 pwkvn temp_pwkvn.txt index.txt check_pwkvn.txt

Links check for pwkvn

----------------------------------------
# get temporary local copy of sch.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch.txt

35 matches for "<ls>Mārk. P. [0-9]+,[0-9]+" in buffer: temp_sch.txt

Random check of links: 
python generate_random.py 5 sch temp_sch.txt index.txt check_sch.txt

Links check for sch

----------------------------------------
# get temporary local copy of mw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt

80 matches for "<ls>MārkP. [ivxlcm]*, *[0-9]+" in buffer: temp_mw.txt

Random check of links: ()

python generate_random.py 5 mw temp_mw.txt index.txt check_mw.txt

Links check for sch
------------------------------------------
check for aDyAya 117 in koshas:
 None of (pwg, pw, pwkvn, sch, mw) have reference to aDyAya 117

==========================================
index checks complete.  All is GO!

==========================================
Beginning app1 in sanskrit-lexicon-scans

local repo
/c/xampp/htdocs/sanskrit-lexicon-scans/markandeyapurana
local url:
localhost/sanskrit-lexicon-scans/markandeyapurana/app1/N,N

Github url:
https://sanskrit-lexicon-scans.github.io/markandeyapurana/app1/N,N

https://sanskrit-lexicon-scans.github.io/markandeyapurana/
shows README.md  (with markdown converted to html)

----------------
# The app1 is similar to that of raghuvamsa/app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/markandeyapurana
cp -r ../raghuvamsa/app1 .

# get the index

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue122/index.txt app1/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue122/make_js_index.py app1/pywork/
# revise make_js_index.py to include ipage
# generate index.js
cd app1/python
python make_js_index.py index.txt index.js

# copy index.js to app1 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/markandeyapurana/app1

# Edit index.html
--- head/title: markandeyap
--- body/title: Mārkāṇḍeya Purāṇa, K.M. Banerjea, 1862

# Edit info.html
--- head/title: markandeyap info
--- body/title: Mārkāṇḍeya Purāṇa, K.M. Banerjea, 1862
--- app1 ...

# Edit main.js
# pdfpages:  mar-001.pdf
# vp is of form NNN
--- get_pdfpage_from_index
 let vp = indexobj['vp'];
 let pdf = `mar-${vp}.pdf`;
--- display_ipage_id
 let ipage = indexcur['ipage']; // an int
 
# --------------------
When local debugging done, upload to github

#  get temporary versions of repos for checking
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue122

cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt

# -------------------
# edit csl-websanlexicon
 /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php
--- links from pwg, pw, pwkvn
# edit function ls_callback_pwg_href

cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
sh generate_web.sh pwg  ../../pwg
sh apidev_copy.sh  # simple search gets new basicadjust.php

--- links from sch
# edit function ls_callback_mw_href
  'Mārk P.' => 'markandeyap', // sch
# edit function ls_callback_sch_href
  add section
--- links from mw
# edit function ls_callback_mw_href
   'MārkP.' => 'markandeyap', // mw
   add section 

-------------------------------------
# sync to github
sync csl-websanlexicon
sync csl-apidev
# sync to cologne
 # regenerate displays for pwg, pw, pwkvn, mw, sch
-------------------------------------
# sync this repo to github

