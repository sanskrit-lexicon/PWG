
=================================================
activating links to meghasrnga app1 and app2
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/meghasrnga
local urls:
localhost/sanskrit-lexicon-scans/meghasrnga/app1/?N,N
localhost/sanskrit-lexicon-scans/meghasrnga/app0/?VNNN

Github url:
https://sanskrit-lexicon-scans.github.io/meghasrnga/app1/?N,N
https://sanskrit-lexicon-scans.github.io/meghasrnga/app0/?VNNN

https://sanskrit-lexicon-scans.github.io/meghasrnga/
shows README.md  (with markdown converted to html)

------------------------------------------------
kosha abbreviations for meghaduta
meghasrnga/app1/?N
PWG: MEGH.
PW:  MEGH.
PWKVN: MEGH.
sch: Megh.
mw:  Megh.

meghasrnga/app2/?N
PWG: ŚṚṄGĀRAT.
PW:  ŚṚṄGĀRAT.  none
PWKVN: ŚṚṄGĀRAT. none
sch: Śṛṅgārat.  none
mw:  Śṛṅgārat. none numbered
mw:  Śṛṅgār.  1 instance with verse.


pw:
126 matches in 125 lines for "<ls>MEGH\. " in buffer: temp_pw.txt
pwkvn
15 matches for "<ls>MEGH\. " in buffer: temp_pwkvn.txt

sch:
15 matches for "<ls>Bhaṭṭ\." in buffer: temp_sch.txt

mw: first parameter roman
150 matches for "<ls>Bhaṭṭ\. " in buffer: temp_mw.txt
# -------------------


# edit local csl-websanlexicon ... basicadjust.php

 /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php
 

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

This step finished locally.

Push csl-websanlexicon, csl-apidev to github

