
=================================================
activating links from koshas to vikramor app1 and app2

koshas: pwg, pw, pwkvn
app1 VIKR. N   --- OR -- VIKRAM. N  
app2 VIKR. N,N --- OR -- VIKRAM. N,N

kosha: sch
app1 Vikr. N   --- OR -- Vikram. N  
app2 Vikr. N,N --- OR -- Vikram. N,N

=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/vikramor
local urls:
localhost/sanskrit-lexicon-scans/vikramor/app1/?N
localhost/sanskrit-lexicon-scans/vikramor/app2/?N


Github url:
https://sanskrit-lexicon-scans.github.io/vikramor/app1/?N
https://sanskrit-lexicon-scans.github.io/vikramor/app2/?N,N

https://sanskrit-lexicon-scans.github.io/vikramor/
shows README.md  (with markdown converted to html)


# -------------------
# edit local csl-websanlexicon ... basicadjust.php


cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
sh generate_web.sh pwg  ../../pwg
sh generate_web.sh pw  ../../pw
sh generate_web.sh pwkvn  ../../pwkvn
sh generate_web.sh sch  ../../sch

sh apidev_copy.sh  # simple search gets new basicadjust.php

Push csl-websanlexicon, csl-apidev to github

