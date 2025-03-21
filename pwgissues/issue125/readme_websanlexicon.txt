
=================================================
activating links to shakuntala app1 and app2
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/shakuntala
local urls:
localhost/sanskrit-lexicon-scans/shakuntala/app1/N
localhost/sanskrit-lexicon-scans/shakuntala/app2/N


Github url:
https://sanskrit-lexicon-scans.github.io/shakuntala/app1/?N
https://sanskrit-lexicon-scans.github.io/shakuntala/app2/?N,N

https://sanskrit-lexicon-scans.github.io/shakuntala/
shows README.md  (with markdown converted to html)


# -------------------
# edit local csl-websanlexicon ... basicadjust.php

 /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php
# edit function ls_callback_pwg_href
---- links from pwg, pw, pwkvn
shakuntala  app2
<ls>ŚĀK. ([0-9]+),([0-9]+)  
shakuntala  app1
<ls>ŚĀK. ([0-9]+)  

---- links from sch
shakuntala  app2
<ls>Śāk. ([0-9]+),([0-9]+)  
shakuntala  app1
<ls>Śāk. ([0-9]+)  


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

