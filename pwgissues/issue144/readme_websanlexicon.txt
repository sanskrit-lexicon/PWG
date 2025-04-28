
=================================================
activating links to taittiriyas app1
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/taittiriyas
local urls:
localhost/sanskrit-lexicon-scans/taittiriyas/app1?N,N,N,N
l

Github url:
https://sanskrit-lexicon-scans.github.io/taittiriyas/app1/?N,N,N,N

https://sanskrit-lexicon-scans.github.io/taittiriyas/
shows README.md  (with markdown converted to html)

# -------------------
# edit local csl-websanlexicon ... basicadjust.php

 /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php
# edit function ls_callback_pwg_href
---- links from pwg, pw, pwkvn, sch
taittiriyas  app1  adhyaya,verse
<ls>VS. ([0-9]+),([0-9]+)

---- links from mw
taittiriyas  app1
<ls>VS. ([vix]+),([0-9]+) 


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


