
=================================================
activating links to bhattikavya app0 and app1
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/bhattikavya
local urls:
localhost/sanskrit-lexicon-scans/bhattikavya/app1/?N,N
localhost/sanskrit-lexicon-scans/bhattikavya/app0/?VNNN

Github url:
https://sanskrit-lexicon-scans.github.io/bhattikavya/app1/?N,N
https://sanskrit-lexicon-scans.github.io/bhattikavya/app0/?VNNN

https://sanskrit-lexicon-scans.github.io/bhattikavya/
shows README.md  (with markdown converted to html)

# link abbreviations in xxxauth.txt
pwg: "BHAṬṬI" in buffer: pwgbib_input.txt
 BHAṬṬ. BHAṬṬIKĀVYA, ed. Calc. (GILD. Bibl. 137).
   2195 matches for "<ls>BHAṬṬ\. " in buffer: temp_pwg.txt
 BHAṬṬI	Bhaṭṭi
   no parms
 BHAṬṬIK
   no parms

pw:
126 matches in 125 lines for "<ls>BHAṬṬ\. " in buffer: temp_pw.txt
pwkvn
15 matches for "<ls>BHAṬṬ\. " in buffer: temp_pwkvn.txt

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

