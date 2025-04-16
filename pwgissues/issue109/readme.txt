issue109/readme.txt
04-07-2025 begun ejf

Ref: https://github.com/sanskrit-lexicon/PWG/issues/109

This issue109 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue109


----------------
# citation forms in pwg
RAGH. (ed. Calc.) x,y
RAGH. ed. Calc. x,y
RAGH. (Calc.) x,y
RAGH. x,y ed. Calc.
---------------

pdf: raghuvamsacalc.pdf
/e/pdfwork/raghuvamsacalc

repo
https://github.com/sanskrit-lexicon-scans/raghuvamsacalc

pdfpages directory
ragh-001.pdf
ragh-002.pdf
...
ragh-654.pdf
ragh-655.pdf

-----------------
Kalidasa.Raghuvamsa-Comments.txt comments by github user angalinde
-----------------

Kalidasa Raghuvamsa-Index.txt from line in issue109
renamed index_orig.txt
remove trailing tabs at end of lines
cp index_orig.txt index.txt

------------------
# some editing of index.txt in preparation for app
---
Remove lines 2,3 (title, introduction)
---
old: 117	---	---	---	104	comments
new: 117	4	89	89	104	comments Jim invents verse 89
---
old: 156	---	---	---	143	comments
new: 156	5	77	77	143	comments  Jim invents 77
---
old: 413	---	---	---	400	sarga ending
new: 156	5	77	77	143	comments  Jim invents 77
---
old: 651	---	---	---	638
new: 651	19	58	58	638	Jim invents 58


==============================

-----------------
index.txt format
format 5 fields tab-separated values (optional comments)
page
sarga
from_verse
to_verse
ipage

-----------------
make_js_index.py makes index into a javascript module.
It does several validity checks.
This program will be part of the 'app1' in the sanskrit-lexicon-scans
repo for this link source.

python make_js_index.py index.txt index.js

json data written to index.js
pagerecs passes check1_sarga
fromv problem A
lnum=288, line=302      9       55      56      289     Nr. 55 is repeated
fromv problem A
lnum=304, line=318      10      6       8       305     Nr. 6 is repeated
fromv problem A
lnum=311, line=325      10      28      30      312     Nr. 27 is skipped
fromv problem A
lnum=459, line=473      14      54      55      460     Nr. 53 is skipped
fromv problem A
lnum=460, line=474      14      55      57      461     Nr. 55 is repeated
fromv problem A
lnum=488, line=502      15      44      46      489     Nr. 43 is skipped
fromv problem A
lnum=494, line=508      15      62      64      495     Nr. 61 is skipped
check1 finds 7 anomalies

Don't think these anomalies are 'serious' -- they were noted by angalinde

----------------------------------------
construction of app1 in sanskrit-lexicon-scans/raghuvamsacalc
see readme_app.txt

----------------------------------------
dictionary links
see readme_websanlexicon.txt

----------------------------------------
checks of consistency among koshas and links.
See readme_checks.txt

----------------------------------------
repos csl-websanlexicon, csl-apidev, csl-orig (shc)
push local to github
pull github to cologne
regenerate displays for pwg, pw, pwkvn, sch, mw
----------------------------------------
push this repo to github
THE END

 
