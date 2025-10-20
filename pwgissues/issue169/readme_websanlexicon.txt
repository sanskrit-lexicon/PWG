
=================================================
activate links to rajatarcalc/app1?N,N for koshas
see read
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/rajatarcalc
local urls:

Github url:
https://sanskrit-lexicon-scans.github.io/rajatarcalc/app1/?N,N

https://sanskrit-lexicon-scans.github.io/rajatarcalc/
shows README.md  (with markdown converted to html)


# -------------------
# edit local csl-websanlexicon ... basicadjust.php

 /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php

basicadjust.php is modified for 5 koshas: pwg, pw, pwkvn, sch, mw


--------------------------------------
pwg refs
pwg RĀJA-TAR. 7/8,N
pwga RĀJAT. ed. Calc N,N
pwgb RĀJAT. 7/8,N

python lsfix2.py pwg temp_pwg_0.txt lsfix2_pwg_0.txt

--------------------------------------

# revise local displays for changes to basicadjust.
cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
sh generate_web.sh pwg  ../../pwg
sh generate_web.sh pw  ../../pw
sh generate_web.sh pwkvn  ../../pwkvn
sh generate_web.sh sch  ../../sch
sh generate_web.sh mw  ../../mw

sh apidev_copy.sh  # simple search gets new basicadjust.php


csl-websanlexicon ok.
sh apidev_copy.sh  # so now simple search ok.

This step finished locally.

Push csl-websanlexicon, csl-apidev to github

