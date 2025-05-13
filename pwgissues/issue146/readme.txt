issue146/readme.txt
05-08-2025 begun ejf
02512	KUMĀRAS.	KUMĀRASAM̃BHAVA, ed. STENZLER (GILD. Bib

Ref: https://github.com/sanskrit-lexicon/PWG/issues/146

This issue146 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue146

-----------------
pdfs: /e/pdfwork/kumaras/

----------------------------------------
index prepared by github user OFar0101
cp /e/pdfwork/kumaras/index_orig.txt .

----------------------------------------
Format observations:
page    sarga   vers from       vers to int page
16      1       1       3       3

----------------------------------------
index.txt minor changes
1. Remove 'remarks' field at end
2. discard last 3 lines:
122	==	==	==	109	The title page Comments
123	==	==	==	110	
124-152	==	==	==	111-139	Comments

python make_index.py index_orig.txt index.txt

107 cases written to index.txt

----------------------------------------
# construct index.js, and check for internal consistencies

python make_js_index.py index.txt index.js

----------------------------------------
 preliminary check of pwg links
 5 Checks succeeded.  See readme_checks.txt

----------------------------------------
'ready for repo' message in https://github.com/sanskrit-lexicon/PWG/issues/146
----------------------------------------
repo ready  kumaras

app construction.
2 apps needed:  see readme_app.txt
app1 -- (sarga,shloka)
app0 -- ipage

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

