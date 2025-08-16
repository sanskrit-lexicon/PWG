
=================================================
app0
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/aitbr
local url:
localhost/sanskrit-lexicon-scans/aitbr/app0/N


Github url:
https://sanskrit-lexicon-scans.github.io/aitbr/app0/?N

https://sanskrit-lexicon-scans.github.io/aitbr/
shows README.md  (with markdown converted to html)

----------------
# app0 is similar to that of /vikramor/app0
cd /c/xampp/htdocs/sanskrit-lexicon-scans/aitbr
cp -r ../vikramor/app0 .

# get the index

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159/index.txt app0/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159/make_js_index.py app0/pywork/

Revise to only print ipage, vp attributes

# copy index.js to app0
cp index.js ../

-------------------------------------
TITLE = Aitareyabrāhmaṇa, ed. Haug, 1863
cd /c/xampp/htdocs/sanskrit-lexicon-scans/aitbr/app0

# Edit index.html
--- head/title: aitbr
--- body/title: TITLE

# Edit info.html
--- head/title: aitbr info
--- body/title: TITLE
--- app1 

# Edit main.js
# pdfpages:  aitbr1_001.pdf

# vp is of form VNNN
--- get_pdfpage_from_index
 
# --------------------
When local debugging done, upload to github

