
=================================================
app1 for aitbr_auf  N,N  or N,N,N
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/aitbr_auf
local url:
localhost/sanskrit-lexicon-scans/aitbr_auf/app1/?N,N 
localhost/sanskrit-lexicon-scans/aitbr_auf/app1/?N,N,N


Github url:
https://sanskrit-lexicon-scans.github.io/aitbr_auf/app0/?N,N
https://sanskrit-lexicon-scans.github.io/aitbr_auf/app0/?N,N,N

https://sanskrit-lexicon-scans.github.io/aitbr_auf/
shows README.md  (with markdown converted to html)

----------------
# app1 is similar to that of /bhartrhari/app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/aitbr_auf
cp -r ../bhartrhari/app1 app1

# get the index
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159auf/index.txt app1/pywork/

cd app1/pywork
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159auf/make_js_index.py app1/pywork/

cd app1/pywork
python make_js_index.py index.txt index.js
# copy index.js to parent directory
cp index.js ../

-------------------------------------
TITLE = Aitareyabrāhmaṇa, ed. Aufrecht, 1879
cd /c/xampp/htdocs/sanskrit-lexicon-scans/aitbr_auf/app1

# Edit index.html
--- head/title: aitbr_auf
--- body/title: TITLE

# Edit info.html
--- head/title: aitbr_auf info
--- body/title: TITLE
--- app1 

# Edit main.js
# pdfpages:  aitbrauf_001.pdf

 
# --------------------
When local debugging done, upload to github

