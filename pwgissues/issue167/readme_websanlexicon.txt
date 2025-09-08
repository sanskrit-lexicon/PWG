
=================================================
activating links from koshas to nirukta app1 and app2

koshas: pwg, pw, pwkvn
app1 NIR. N,N
app2 NAIGH. N,N

kosha: sch
app1 Nir. N,N
app2 Nigh. N,N  one instance

kosha: mw
app1 Nir. R,N
app2 Naigh. R,N
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/nirukta
local urls:
localhost/sanskrit-lexicon-scans/nirukta/app1/?N,N
localhost/sanskrit-lexicon-scans/nirukta/app2/?N,N


Github url:
https://sanskrit-lexicon-scans.github.io/nirukta/app1/?N,N
https://sanskrit-lexicon-scans.github.io/nirukta/app2/?N,N

https://sanskrit-lexicon-scans.github.io/nirukta/
shows README.md  (with markdown converted to html)


# -------------------
# edit local csl-websanlexicon ... basicadjust.php
# install for local displays
cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
sh generate_web.sh pwg  ../../pwg
sh generate_web.sh pw  ../../pw
sh generate_web.sh pwkvn  ../../pwkvn
sh generate_web.sh sch  ../../sch
sh generate_web.sh mw  ../../mw

sh apidev_copy.sh  # simple search gets new basicadjust.php
# return home
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue167

Push csl-websanlexicon, csl-apidev to github

