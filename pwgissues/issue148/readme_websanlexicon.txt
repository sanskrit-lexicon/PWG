
=================================================
activating links to bhartrhari app1 and app2
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/bhartrhari
local urls:
localhost/sanskrit-lexicon-scans/bhartrhari/app1/?N
localhost/sanskrit-lexicon-scans/bhartrhari/app0/?N

Github url:
https://sanskrit-lexicon-scans.github.io/bhartrhari/app2/?N,N

https://sanskrit-lexicon-scans.github.io/bhartrhari/
shows README.md  (with markdown converted to html)

cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt


app1  Caurapañcāśikā 1 parameter
pwg CAURAP.  376
pw  CAURAP. N  6
pw 'CAURAP. (A.)' 31
pwkvn 'CAURAP. (A.)' 16
sch 'Caurap. (A.)' 14
mw  'Caurap.'  2


Corrections:

4422 : kARqavastra : CAURAP. (A.) 31 : CAURAP. (A.) 51 : pwkvn typo
204422 : kARqavastra : CAURAP. (A.) 31 : CAURAP. (A.) 51 : pw typo
100648 : vAmanayanA : CAURAP. (A.) 108 : CAURAP. (A.) 109 : pw printchange
85085 : tiraspawa : Caurap. 49. : Caurap. (A.) 49. : mw printchange

cp temp_pw.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cp  temp_pwkvn.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt
cp temp_mw.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt

app2 Bhartṛhariśataka  2 parameters
pwg BHARTṚ. 1238
pw  not found
pwkvn not found
sch  not found
mw Bhartṛ.  132 (2 parm)  and 705 with 0 parameters.

# edit local csl-websanlexicon ... basicadjust.php

 /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php
 

cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
sh generate_web.sh pwg  ../../pwg
sh generate_web.sh pw  ../../pw
sh generate_web.sh pwkvn  ../../pwkvn
sh generate_web.sh sch  ../../sch
sh generate_web.sh mw  ../../mw

sh apidev_copy.sh  # simple search gets new basicadjust.php

Use the check_X1.txt and check_X2.txt files (for X=pwg, pw, pwkvn, sch)
and local simple search to find several example links.
These work as expected.

csl-websanlexicon ok.
sh apidev_copy.sh  # so now simple search ok.

This step finished locally.

Push csl-websanlexicon, csl-apidev to github

