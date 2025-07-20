
=================================================
activating links to pancar app1
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/pancar
local urls:
localhost/sanskrit-lexicon-scans/pancar/app1?N,N,N
l

Github url:
https://sanskrit-lexicon-scans.github.io/pancar/app1/?N,N,N


# -------------------
# edit local csl-websanlexicon ... basicadjust.php

 /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php
# edit function ls_callback_pwg_href
---- links from pwg, pw, pwkvn
pancar  app1  ratra,adhyaya,verse
<ls>PAÑCAR. ([0-9]+),([0-9]+),([0-9]+)

pancar app0  S. page  [only found in PWG]

<ls>PAÑCAR. S. ([0-9]+)

---- links from sch   <<< ratra = 4??
pancar app1
<ls>Pañcar. ([0-9]+),([0-9]+),([0-9]+)

---- links from mw
pancar  app1
<ls>Pañcar. ([vix]+), *([0-9]+), *([0-9]+)


cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
sh generate_web.sh pwg  ../../pwg
sh generate_web.sh pw  ../../pw
sh generate_web.sh pwkvn  ../../pwkvn
sh generate_web.sh sch  ../../sch
sh generate_web.sh mw  ../../mw

sh apidev_copy.sh  # simple search gets new basicadjust.php

cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue137

This step finished locally.


