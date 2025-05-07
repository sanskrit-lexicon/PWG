
=================================================
activating links to taittiriyabr app1
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/taittiriyabr
local urls:
localhost/sanskrit-lexicon-scans/taittiriyabr/app1?N,N,N,N
l

Github url:
https://sanskrit-lexicon-scans.github.io/taittiriyabr/app1/?N,N,N,N

pwg, pw, pwkvn
<ls>TBR. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)
sch
<ls>TBr. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)
mw
<ls>TBr. ([i]+),([0-9]+),([0-9]+),([0-9]+)

# -------------------
# edit local csl-websanlexicon ... basicadjust.php

 /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php
# edit function ls_callback_pwg_href
---- links from pwg, pw, pwkvn, sch
taittiriyabr  app1  adhyaya,verse
<ls>VS. ([0-9]+),([0-9]+)

---- links from mw
taittiriyabr  app1
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


