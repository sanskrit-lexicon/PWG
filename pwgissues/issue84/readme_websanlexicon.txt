
=================================================
activating links to shatapathabr app1
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/shatapathabr
local urls:
localhost/sanskrit-lexicon-scans/shatapathabr/app1/N,N,N,N


Github url:
https://sanskrit-lexicon-scans.github.io/shatapathabr/app1/?N,N,N,N

https://sanskrit-lexicon-scans.github.io/shatapathabr/
shows README.md  (with markdown converted to html)


# -------------------
# edit local csl-websanlexicon ... basicadjust.php

 /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php
# edit function ls_callback_pwg_href
---- links from pwg, pw, pwkvn
shatapathabr  app1
<ls>ŚAT. BR. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)  

---- links from sch
shatapathabr  app2
<ls>ŚAT. BR. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)  


cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
sh generate_web.sh pwg  ../../pwg
sh generate_web.sh pw  ../../pw
sh generate_web.sh pwkvn  ../../pwkvn
sh generate_web.sh sch  ../../sch
sh apidev_copy.sh  # simple search gets new basicadjust.php


csl-websanlexicon ok.
sh apidev_copy.sh  # so now simple search ok.

This step finished locally.
--------------------------------------------
checks for pwg
'pwg': r'<ls>ŚAT. BR. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)'
python generate_random1.py 5 pwg temp_pwg.txt SAT.Index_edit.txt check_pwg.txt
 OK

checks for pw
'pw': r'<ls>ŚAT. BR. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)'
python generate_random1.py 5 pw temp_pw.txt SAT.Index_edit.txt check_pw.txt

4 found, 1 NOT FOUND

checks for pwkvn
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn.txt

'pwkvn': r'<ls>ŚAT. BR. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)'
python generate_random1.py 5 pwkvn temp_pwkvn.txt SAT.Index_edit.txt check_pwkvn.txt
 OK

checks for sch
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch.txt

'sch': r'<ls>Śat. Br. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)'
python generate_random1.py 5 sch temp_sch.txt SAT.Index_edit.txt check_sch.txt
 
checks for mw
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt

'mw': r'<ls>ŚBr. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)'
python generate_random1.py 5 mw temp_mw.txt SAT.Index_edit.txt check_mw.txt
 OK


Push csl-websanlexicon, csl-apidev to github

