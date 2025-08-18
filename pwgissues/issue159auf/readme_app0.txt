
=================================================
app0  index full book
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/aitbr_auf
local url:
localhost/sanskrit-lexicon-scans/aitbr_auf/app0/N

Github url:
https://sanskrit-lexicon-scans.github.io/aitbr_auf/app0/?N

https://sanskrit-lexicon-scans.github.io/aitbr_auf/
shows README.md  (with markdown converted to html)

----------------
# app0 is similar to that of /bhartrhari/app0
cd /c/xampp/htdocs/sanskrit-lexicon-scans/aitbr_auf
cp -r ../bhartrhari/app0 .

# get the program to convert index.txt to index.js
# revise app0/pywork/make_js_index.py for aitbr_auf
cd app0/pywork
python make_js_index.py index.js
cp index.js ../

-------------------------------------
TITLE = Aitareyabrāhmaṇa, ed. Aufrecht, 1879
cd /c/xampp/htdocs/sanskrit-lexicon-scans/aitbr_auf/app0

# Edit index.html
--- head/title: aitbr_auf
--- body/title: TITLE

# Edit info.html
--- head/title: aitbr_auf info
--- body/title: TITLE
--- app1 

# Edit main.js
# pdfpages:  aitbrauf_001.pdf

# vp is of form NNN
--- get_pdfpage_from_index
 
# --------------------
When local debugging done, upload to github

