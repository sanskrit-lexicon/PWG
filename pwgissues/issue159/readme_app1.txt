
=================================================
app1
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/aitbr
local url:
localhost/sanskrit-lexicon-scans/aitbr/app1/?N,N 


Github url:
https://sanskrit-lexicon-scans.github.io/aitbr/app0/?N,N

https://sanskrit-lexicon-scans.github.io/aitbr/
shows README.md  (with markdown converted to html)

----------------
# app1 is similar to that of /vikramor/app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/aitbr
cp -r ../vikramor/app1 app1

# get the index

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159/index.txt app1/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159/make_js_index.py app1/pywork/

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

 
# --------------------
When local debugging done, upload to github

