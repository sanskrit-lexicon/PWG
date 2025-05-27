issue148/readme.txt
05-09-2025 begun ejf

BHARTṚHARI  CAURAPAÑCĀŚIKĀ  two works in same pdf

Ref: https://github.com/sanskrit-lexicon/PWG/issues/148

This issue148 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue148

-----------------
pdf: /e/pdfwork/bhartrhari

----------------------------------------
indexes prepared by github user OFar0101
These are misnamed by OFar0101
cp /e/pdfwork/bhartrhari/index_bhart_orig.txt index_caurap_orig.txt
cp /e/pdfwork/bhartrhari/index_caurap_orig.txt index_bhart_orig.txt



----------------------------------------
Format observations:
index_caurap_orig.txt

page	vers from	vers to	int page
38	1	1	1


index_bhart_orig.txt
page	śataka	vers from	vers to	int page
58	1	1	4	21


----------------------------------------
index_bhart.txt  no changes needed
cp index_bhart_orig.txt index_bhart.txt

----------------------------------------
index_caurap.txt no changes needed
cp index_caurap_orig.txt index_caurap.txt

----------------------------------------
# construct index_bhart.js, and check for internal consistencies

python make_js_index_bhart.py index_bhart.txt index_bhart.js
56 Success: Page records read from index_bhart.txt
json data written to index_bhart.js

----------------------------------------
# construct index_caurap.js, and check for internal consistencies

python make_js_index_caurap.py index_caurap.txt index_caurap.js
19 Success: Page records read from index_caurap.txt


----------------------------------------
 preliminary check of pwg links for bhart
 5 Checks succeeded.  See readme_checks_bhart.txt

----------------------------------------
'ready for repo' message in https://github.com/sanskrit-lexicon/PWG/issues/148
----------------------------------------
app construction.
2 apps are needed:  see readme_app.txt
app1 -- (sarga,shloka)
app0 -- VNNN  

----------------------------------------
modify basicadjust.php for pwg, pw, pwkvn, sch, mw
see readme_websanlexicon.txt

----------------------------------------
checks of links from dictionaries
see readme_checks.txt

sync to github:  csl-websanlexicon, csl-apidev
pull github to cologne server
regenerate displays for pwg, pw, pwkvn, sch, mw
=============================================================
THE END

