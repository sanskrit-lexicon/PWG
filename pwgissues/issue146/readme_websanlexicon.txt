
=================================================
activating links to kumaras app1
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/kumaras
local urls:
localhost/sanskrit-lexicon-scans/kumaras/app1/?N,N

Github url:
https://sanskrit-lexicon-scans.github.io/kumaras/app1/?N,N

https://sanskrit-lexicon-scans.github.io/kumaras/
shows README.md  (with markdown converted to html)
# link abbreviations in xxxauth.txt
pwg KUMĀRAS.
pw  KUMĀRAS.
pwkvn KUMĀRAS.
sch Kumāras.
mw  Kum.

# -------------------


# edit local csl-websanlexicon ... basicadjust.php

 /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php
 

cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
sh generate_web.sh pwg  ../../pwg
sh generate_web.sh pw  ../../pw
sh generate_web.sh pwkvn  ../../pwkvn
sh generate_web.sh sch  ../../sch
sh generate_web.sh mw  ../../mw

sh apidev_copy.sh  # simple search gets new basicadjust.php

Proceed to readme_checks.txt 
When these checks are finished,
this csl-websanlexicon step is finished locally.

Push csl-websanlexicon, csl-apidev to github

