
=================================================
app0
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/vikramor
local url:
localhost/sanskrit-lexicon-scans/vikramor/app0/N


Github url:
https://sanskrit-lexicon-scans.github.io/vikramor/app0/?N

https://sanskrit-lexicon-scans.github.io/vikramor/
shows README.md  (with markdown converted to html)

----------------
# app1 is similar to that of /bhattikavya/app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/vikramor
cp -r ../bhattikavya/app1 .


# get the index (before revision)

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue157/index.txt app1/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue157/make_js_index.py app1/pywork/

Use an alternate:  ipage 1-608, epage = ipage + 21
# generate index.js
cd app1/pywork
python make_js_index1.py index.js

# copy index.js to app0
cp index.js ../

-------------------------------------
TITLE = Vikramorvasī by Kālidāsa, ed. F. Bollensen, 1846
cd /c/xampp/htdocs/sanskrit-lexicon-scans/vikramor/app0

# Edit index.html
--- head/title: vikramor
--- body/title: TITLE

# Edit info.html
--- head/title: vikramor info
--- body/title: TITLE
--- app1 

# Edit main.js
# pdfpages:  vikramor_001.pdf

# vp is of form NNN
--- get_pdfpage_from_index
 let vp = indexobj['vp'];
 let pdf = `vikram_${vp}.pdf`;
--- display_ipage_id
 let ipage = indexcur['ipage']; // an int
 
# --------------------
When local debugging done, upload to github

