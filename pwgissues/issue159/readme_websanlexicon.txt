
=================================================
activating links from koshas to aitbr for  app1 and app2
START
-- pwg, pw, pwkvn
app1 AIT. BR.  nparm = 2
app2 AIT. BR.  nparm = 3
-- sch
app1 Ait. Br.  nparm = 2
app2 Ait. Br.  nparm = 3
-- mw
app1 AitBr.  nparm = 2
app2 AitBr.  nparm = 3



=================================================

Github url:
https://sanskrit-lexicon-scans.github.io/aitbr/app1/?N,N
https://sanskrit-lexicon-scans.github.io/aitbr/app2/?N,N,N

# -------------------
# edit local csl-websanlexicon ... basicadjust.php

# -------------------

cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
sh generate_web.sh pwg  ../../pwg
sh generate_web.sh pw  ../../pw
sh generate_web.sh pwkvn  ../../pwkvn
sh generate_web.sh sch  ../../sch
sh generate_web.sh mw  ../../mw


sh apidev_copy.sh  # simple search gets new basicadjust.php

Push csl-websanlexicon, csl-apidev to github

