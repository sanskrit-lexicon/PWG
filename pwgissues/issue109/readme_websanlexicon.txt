
=================================================
activating links to raghuvamsacalc app1
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/raghuvamsacalc
local urls:
localhost/sanskrit-lexicon-scans/raghuvamsacalc/app1?N,N
l

Github url:
https://sanskrit-lexicon-scans.github.io/raghuvamsacalc/app1/?N,N

https://sanskrit-lexicon-scans.github.io/raghuvamsacalc/
shows README.md  (with markdown converted to html)

# -------------------
# edit local csl-websanlexicon ... basicadjust.php

 /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php
# edit function ls_callback_pwg_href
---- links from pwg, pw, pwkvn, sch
raghuvamsacalc  app1  sarga,verse

preliminary checks temp_pwg.txt consistent with pdf.
 Manually took one or two from each form of link.
 conclusion: This pdf consistent with these links in pwg
 
15 matches for "<ls>RAGH. (ed. Calc.) [0-9]+,[0-9]+"  ok pdf
116 matches for "<ls>RAGH. ed. Calc. [0-9]+,[0-9]+"  ok pdf
1 match for "<ls>RAGH. (Calc.) [0-9]+,[0-9]+"  ? pdf  not sure

These two cannot be handled in basicadjust.php.
Maybe do print change 
1 match for "<ls>RAGH. [0-9]+,[0-9]+\.?</ls> <ls>ed. Calc.</ls>"  ok pdf
2 matches for "<ls>RAGH. [0-9]+,[0-9]+\.?</ls> (<ls>ed. Calc.</ls>)"  ok pdf

<ls>XXX ([0-9]+),([0-9]+)

---- links from mw
raghuvamsacalc  app1
<ls>XXX ([vix]+),([0-9]+) 


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


