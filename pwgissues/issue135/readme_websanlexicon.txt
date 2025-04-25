
=================================================
activate links to rajatar/app1?N,N for koshas
see read
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/rajatar
local urls:
localhost/sanskrit-lexicon-scans/rajatar/app1/N

Github url:
https://sanskrit-lexicon-scans.github.io/rajatar/app1/?N,N

https://sanskrit-lexicon-scans.github.io/rajatar/
shows README.md  (with markdown converted to html)


# -------------------
# edit local csl-websanlexicon ... basicadjust.php

 /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php

mw
07:03	Rājat.	Rājataraṃgiṇī	Title
07:03a	Rājat. (C)	Rājataraṃgiṇī, Calcutta edition [Cologne Addition]	Title
07:03x	Rāj.	Rājataraṃgiṇī	Title

# edit function ls_callback_pwg_href
---- links from pwg, pw, pwkvn
---- links from sch
rajatar  app2
<ls>Śāk. ([0-9]+),([0-9]+)  
rajatar  app1
<ls>Śāk. ([vi]+),([0-9]+) 


cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
sh generate_web.sh pwg  ../../pwg
sh generate_web.sh pw  ../../pw
sh generate_web.sh pwkvn  ../../pwkvn
sh generate_web.sh sch  ../../sch

sh apidev_copy.sh  # simple search gets new basicadjust.php


csl-websanlexicon ok.
sh apidev_copy.sh  # so now simple search ok.

This step finished locally.

Push csl-websanlexicon, csl-apidev to github

