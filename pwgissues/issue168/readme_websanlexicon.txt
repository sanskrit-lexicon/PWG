
=================================================
activating links to pantankoseorn app1 and app2
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/pantankoseorn
local urls:
localhost/sanskrit-lexicon-scans/pantankoseorn/app1/N
localhost/sanskrit-lexicon-scans/pantankoseorn/app2/N

Github url:
https://sanskrit-lexicon-scans.github.io/pantankoseorn/app1/?N,N
https://sanskrit-lexicon-scans.github.io/pantankoseorn/app2/?N,N

https://sanskrit-lexicon-scans.github.io/pantankoseorn/
shows README.md  (with markdown converted to html)


# -------------------
# edit local csl-websanlexicon ... basicadjust.php

 /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php
# edit function ls_callback_pwg_href
---- links from pwg, pw, pwkvn
pantankoseorn  app1  page,linenum
<ls>PAÑCAT. ed. orn. ([0-9]+),([0-9]+) 
pantankoseorn  app2  tantra,verse
<ls>PAÑCAT. ed. orn. ([0vi]+),([0-9]+)



cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
sh generate_web.sh pwg  ../../pwg

sh apidev_copy.sh  # simple search gets new basicadjust.php

Use the check_X1.txt and check_X2.txt files (for X=pwg, pw, pwkvn, sch)
and local simple search to find several example links.
These work as expected.

csl-websanlexicon ok.
sh apidev_copy.sh  # so now simple search ok.

This step finished locally.

Push csl-websanlexicon, csl-apidev to github
# return home
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue168

