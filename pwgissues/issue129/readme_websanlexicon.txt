
=================================================
activating links to bhagavadgita app1
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/bhagavadgita
local urls:
localhost/sanskrit-lexicon-scans/bhagavadgita/app1/?N,N

Github url:
https://sanskrit-lexicon-scans.github.io/bhagavadgita/app1/?N,N

https://sanskrit-lexicon-scans.github.io/bhagavadgita/
shows README.md  (with markdown converted to html)


# -------------------
# edit local csl-websanlexicon ... basicadjust.php

 /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php
# edit function ls_callback_pwg_href
---- links from pwg, pw, pwkvn
bhagavadgita  app1
<ls>BHAG. ([0-9]+),([0-9]+)  

---- links from sch
bhagavadgita  app1
<ls>Bhag. ([0-9]+),([0-9]+)  

---- links from mw
bhagavadgita  app1
<ls>Bhag. ([ivx]+),([0-9]+)  


cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
sh generate_web.sh pwg  ../../pwg
sh generate_web.sh pw  ../../pw
sh generate_web.sh pwkvn  ../../pwkvn
sh generate_web.sh sch  ../../sch

sh apidev_copy.sh  # simple search gets new basicadjust.php

Use the check_X1.txt and check_X2.txt files (for X=pwg, pw, pwkvn, sch)
and local simple search to find several example links.
These work as expected.

csl-websanlexicon ok.
sh apidev_copy.sh  # so now simple search ok.

===================================
checks of links for dictionaries

# get temporary local copy of pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt

# all instances of BHAG. with 1 or more parametegrs
2120 matches in 2119 lines for "<ls>BHAG. [0-9]+,[0-9]+" in buffer: temp_pwg.txt

----------------------------------------
Make misc checks between pwg , the pdf and index

'pwg':r'<ls>BHAG. ([0-9]+),([0-9]+)  (adhyAya, shloka)
python generate_random.py 5 pwg temp_pwg.txt index.txt check_pwg.txt
found 2120 instances in kosha
found 656 distinct in kosha
5 written to check_pwg.txt

All cases OK

----------------------------------
# get temporary local copy of pw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt

103 matches for "<ls>BHAG. [0-9]+,[0-9]+" in buffer: temp_pw.txt

Random check of links:

'pw':r'<ls>BHAG. ([0-9]+),([0-9]+)  (adhyaya,shloka)
python generate_random.py 5 pw temp_pw.txt index.txt check_pw.txt

All checks ok.
----------------------------------
# get temporary local copy of pwkvn.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn.txt

35 matches for "<ls>BHAG. [0-9]+,[0-9]+" in buffer: temp_pwkvn.txt

Random check of links:

'pwkvn':r'<ls>BHAG. ([0-9]+),([0-9]+)  (adhyaya,shloka)
python generate_random.py 5 pwkvn temp_pwkvn.txt index.txt check_pwkvn.txt

All checks ok.

----------------------------------------
# get temporary local copy of sch.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch.txt

36 matches for "<ls>Bhag. [0-9]+,[0-9]+" in buffer: temp_sch.txt

Random check of links:

'sch':r'<ls>Bhag. ([0-9]+),([0-9]+)  (adhyaya, shloka)
python generate_random.py 5 sch temp_sch.txt index.txt check_sch.txt

All checks OK

-----------------------------
# get temporary local copy of mw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt

116 matches for "<ls>Bhag\. " in buffer: temp_mw.txt
108 matches for "<ls>Bhag\. [ivx]+, *[0-9]+" in buffer: temp_mw.txt

'mw':r'<ls>BHag. ([ivx]+), *([0-9]+)  (adhyAya, shloka)
python generate_random.py 5 mw temp_mw.txt index.txt check_mw.txt
found 108 instances in kosha
5 written to check_mw.txt

All checks ok. 

END OF CHECKS. All ok.


This step finished locally.

Push csl-websanlexicon, csl-apidev to github

===================================

