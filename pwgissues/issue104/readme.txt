issue104/readme.txt
03-08-2025 begun Dhaval
03-08-2025 end Dhaval

16151 : H. [HEMACANDRA'S ABHIDHĀNACINTĀMAṆI] Bohtlingk: pp. 18-305
01303 :	H. ś.	die Śeṣa's zu HEMACANDRA'S ABHIDHĀNACINTAMAṆI pp. 438-460

Ref: https://github.com/sanskrit-lexicon/PWG/issues/104

This issue105 directory in local file system:
cd /srv/http/cologne-extra/PWG/pwgissues/issue105


-----------------------------
indexes into Hemacandra's Abhidhānacintāmaṇi and Abhidhānacintāmaṇipariśiṣṭa (Also known as śeṣa)
H.    abch_index.txt    verse
H. ś.  acph_index.txt  verse

-----------------------------
pdf: Hemachandra_Abhidhanachintamani_1847_Bohtlingk.pdf
1847 Bohtlingk edition

----------------------------------------
# get temporary local copy of pwg.txt
cp /srv/http/sanskrit-lexicon/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt

-----------------------------
mkdir abch
cp abch_index.txt abch/abch_index_v1.txt

-----------------------------
mkdir acph 
cp  acph_index.txt acph/acph_index_v1.txt

-----------------------------
03-08-2025  indexes checked. 
-----------------------------
03-08-2025  sanskrit-lexicon-scans/abch2
app1 for abch
app2 for acph
-----------------------------
03-08-2025
csl-websanlexicon
 basicadjust.php
/srv/http/sanskrit-lexicon/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php

-----
abch app1
pwg, pw, pwkvn
<ls>H. ([0-9]+)[.]</ls>  verse
https://sanskrit-lexicon-scans.github.io/abch2/app1?$s

# checks against display
pwg test: akarRa
pw  test: sarvasaMjYA
pwkvn test: nAtivilambin
sch test : No example

-----
acph app2
pwg, pw, pwkvn
<ls>H. ś. ([0-9]+).</ls> verse
https://sanskrit-lexicon-scans.github.io/abch2/app2?$s
# checks against display
pwg test: yatIyasa
pw  test: citrANgasAdana
pwkvn test: akzata
sch test: No example

------------------------
sh generate_web.sh pwg  ../../pwg
cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
sh generate_web.sh pwg  ../../pwg
sh generate_web.sh pw  ../../pw
sh generate_web.sh pwkvn  ../../pwkvn

