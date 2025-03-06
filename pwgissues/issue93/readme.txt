issue93/readme.txt
03-01-2025 begun ejf

03446	N.	NALOPĀKHYĀNA in BÖHTLINGK'S Chrestomathi
01127	VID.	Geschichte des VIDŪṢAKA in BÖHTLINGK'S C
00413	DAŚ.	DAŚARATHA'S Tod in BÖHTLINGK'S Chrestoma
00370	VIŚV.	VIŚVĀMITRA'S Kampf in BÖHTLINGK'S Chrest

Ref: https://github.com/sanskrit-lexicon/PWG/issues/93

This issue93 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93


-----------------------------
indexes into BÖHTLINGK'S Chrestomathi
N.    Nalopakhyana_index.txt    adhy,verse
VID.  Geschichte_des_Vidushaka_Index.txt  verse
DAŚ.  Dasharathas_Tod_Index.txt   sarga,verse
VIŚV. Vishvamitras_kampf_Index.txt

-----------------------------
pdf: Chrestomathie 1st ed. 1845.pdf
/e/pdfwork/chr1/Chrestomathie 1st ed. 1845.pdf

----------------------------------------
# get temporary local copy of pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt

-----------------------------
mkdir nala
cp Nalopakhyana_index.txt nala/index.txt
# refer nala/readme.txt

-----------------------------
mkdir vid 
cp  Geschichte_des_Vidushaka_Index.txt vid/index.txt
# refer vid/readme.txt

-----------------------------
mkdir dash
cp Dasharathas_Tod_Index.txt dash/index.txt
# refer dash/readme.txt

adhy,verse
(Dasharatha's Death)

-----------------------------
VIŚV.	VIŚVĀMITRA'S Kampf  (battle)
sarga,verse

cp -r dash vishva
cp Vishvamitras_kampf_Index.txt vishva/index.txt
see vishva/readme.txt

-----------------------------
03-02-2025  indexes checked. 
-----------------------------
03-04-2025  sanskrit-lexicon-scans/bchrest1
app1 for nala
app2 for dash
app3 for vid
app4 for vishva
-----------------------------
03-05-2025
csl-websanlexicon
 basicadjust.php
/c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php

-----
nala app1
pwg, pw, pwkvn
<ls>N. ([0-9]+),([0-9]+.</ls>  adhyaya,verse
https://sanskrit-lexicon-scans.github.io/bchrest1/app1?$t,$s

# checks against display
pwg test: kasmAt
pw  test: NONE suMsamAra  only example! mal-formed
pwkvn test: NONE
mw test: NONE
-----
dash app2 Daś
pwg, pw, pwkvn
<ls>DAŚ. ([0-9]+),([0-9]+.</ls>  sarga,verse
https://sanskrit-lexicon-scans.github.io/bchrest1/app2?$t,$s
# checks against display
pwg test: karmacezwA
pw  test: NONE
pwkvn test: NONE
sch test: NONE
mw test: None
-----
vid app3
pwg, pw, pwkvn
<ls>VID. ([0-9]+).</ls>  verse
https://sanskrit-lexicon-scans.github.io/bchrest1/app3?$t
# checks against display
pwg test: pratyAgama 
pw  test: NONE
pwkvn test: NONE
sch test: NONE
mw test: NONE
-----
vishva   Viśv
pwg, pw, pwkvn
<ls>VIŚV. ([0-9]+),([0-9]+.</ls>  sarga,verse
https://sanskrit-lexicon-scans.github.io/bchrest1/app4?$t
# checks against display
pwg test: aKilena
pw  test: NONE
pwkvn test: NONE
sch test: NONE
mw test: NONE
------------------------
sh generate_web.sh pwg  ../../pwg
cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
sh generate_web.sh pwg  ../../pwg
sh generate_web.sh pw  ../../pw
sh generate_web.sh pwkvn  ../../pwkvn


sh generate_web.sh sch  ../../sch
sh generate_web.sh mw  ../../mw
