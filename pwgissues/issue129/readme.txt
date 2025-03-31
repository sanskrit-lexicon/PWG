issue129/readme.txt
03-27-2025 begun ejf
02278	BHAG.	BHAGAVADGĪTĀ


Ref: https://github.com/sanskrit-lexicon/PWG/issues/129

This issue129 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue129

-----------------
pdf: 'BHAGAVADGĪTĀ (1823) SCHLEGEL.pdf'

/e/pdfwork/bhagavadgita_shlegel/'BHAGAVADGĪTĀ (1823) SCHLEGEL.pdf'

-----------------
Index file
  
  BHAGAVADGITA.1823.SCHLEGE.xlsx
  convert to tsv (Google) BHAGAVADGITA.1823.SCHLEGEL.txt
  # 
  cp BHAGAVADGITA.1823.SCHLEGEL.txt index.txt
 
---------------------
index_txt format observations
format 5 fields tab-separated values
page
adhy
fromv
tov
ipage
--------------------
--
# Prepare index.js
python make_js_index.py index.txt index.js
88 Success: Page records read from index.txt
json data written to index.js

----------------------------------------
construct app1 in sanskrit-lexicon-scans/bhagavadgita.
See readme_app1.txt

----------------------------------------
Activate links from CDSL dictionaries for bhagavadgita
Do checks of consistency of links for pwg, pw, pwkvn, sch, mw dictionaries
see readme_websanlexicon.txt


==========================================
index checks complete.  All is GO for pwg, pw, pwkvn, sch, mw


==========================================

-------------------------------------
# sync to github
sync csl-websanlexicon
sync csl-apidev
# sync to cologne
# regenerate displays for pwg, pw, pwkvn, sch, [mw not required]
-------------------------------------
# sync this repo to github
====================================
THE END

