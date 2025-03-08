issue105/readme.txt
03-05-2025 begun Dhaval
03-07-2025 end Dhaval

12990 : MED. [MEDINĪKOṢA], pp. 382-563 (pdf pages)
08426 : TRIK. [TRIKĀṆḌAŚEṢA], p. 252-333 (pdf pages)
01865 : HĀR. [HĀRĀVALĪ], pp. 350-372 (pdf pages)

Note - this PDF also has Amarakośa in case this is the edition used.

Ref: https://github.com/sanskrit-lexicon/PWG/issues/105

This issue105 directory in local file system:
cd /srv/http/cologne-extra/PWG/pwgissues/issue105


-----------------------------
indexes into BÖHTLINGK'S Chrestomathi
MED.    medini_index.txt    adhy,verse (with adhy being Sanskrit consonant).
TRIK.  trikandashesha_index.txt  adhy,verse
HĀR.  haravali_index.txt   verse

-----------------------------
pdf: Amarakosha_Medinikosha_Trikandashesha_Haravali.pdf
1807 Calcutta edition

----------------------------------------
# get temporary local copy of pwg.txt
cp /srv/http/sanskrit-lexicon/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt

-----------------------------
mkdir medini
cp medini_index.txt medini/medini_index_v1.txt
# refer medini/readme.txt

-----------------------------
mkdir trikandashesha 
cp  trikandashesha_index.txt trikandashesha/trikandashesha_index_v1.txt
# refer trikandashesha/readme.txt

-----------------------------
mkdir haravali
cp haravali_index.txt haravali/haravali_index.txt
# refer haravali/readme.txt

-----------------------------
03-06-2025  indexes checked. 
-----------------------------
03-07-2025  sanskrit-lexicon-scans/medini
app1 for medini
app2 for trikandashesha
app3 for haravali
-----------------------------
03-07-2025
csl-websanlexicon
 basicadjust.php
/srv/http/sanskrit-lexicon/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php

-----
medini app1
pwg, pw, pwkvn
<ls>MED. ([khgṅcjñṭḍṇtdnpbmyrlvśṣsao])[.] ([0-9]+)[.]</ls>  adhyaya,verse
https://sanskrit-lexicon-scans.github.io/medini/app1?$t,$s

# checks against display
pwg test: dfzwi
pw  test: puwita
pwkvn test: granTAvftti
sch test : Fail
  success (change schauth/tooltip.txt) Jim kulapAlaka <ls>Med. k. 109.</ls>
mw test: No example
-----
trikandashesha app2
pwg, pw, pwkvn
<ls>TRIK. ([0-9]+),([0-9]+),([0-9]+).</ls> kand, adhy, verse
https://sanskrit-lexicon-scans.github.io/medini/app2?$k,$t,$s
# checks against display
pwg test: pAdakawaka
pw  test: kunABi
pwkvn test: nApitaSAlikA
sch test: <L>1629<pc>022-3<k1>adva    <ls>Trik. 1,2,9.</ls>
           granTAvftti   <ls>Trik. 3,3,278</ls> 
mw test: No example
-----
haravali app3
pwg, pw, pwkvn
<ls>HĀR. ([0-9]+).</ls>  verse
https://sanskrit-lexicon-scans.github.io/bchrest1/app3?$t
# checks against display
pwg test: jalakaraNka
pw  test: SUkataru
pwkvn test: atfptikft
sch test: atfptikft  <ls>Hār. 220.</ls> 
mw test: No example

------------------------
sh generate_web.sh pwg  ../../pwg
cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
sh generate_web.sh pwg  ../../pwg
sh generate_web.sh pw  ../../pw
sh generate_web.sh pwkvn  ../../pwkvn


sh generate_web.sh sch  ../../sch
sh generate_web.sh mw  ../../mw
