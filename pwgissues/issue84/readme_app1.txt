
=================================================
app1
=================================================
https://github.com/sanskrit-lexicon-scans/shatapathabr
# token README.md
# Pages

cd /c/xampp/htdocs/sanskrit-lexicon-scans/shatapathabr

git clone git@github.com:sanskrit-lexicon-scans/shatapathabr.git

Improve README.md
-------------------------------------------------
/c/xampp/htdocs/sanskrit-lexicon-scans/shatapathabr
local url:
localhost/sanskrit-lexicon-scans/shatapathabr/app1/N,N,N,N


Github url:
https://sanskrit-lexicon-scans.github.io/shatapathabr/app1/?N,N,N,N

https://sanskrit-lexicon-scans.github.io/shatapathabr/
shows README.md  (with markdown converted to html)

----------------
# base app1 on /markandeyapurana/app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/shatapathabr
cp -r ../markandeyapurana/app1 .

# get the index

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue84/SAT.index_edit.txt app1/pywork/index.txt
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue84/make_js_index.py app1/pywork/
# revise make_js_index.py to include ipage
# generate index.js
cd app1/pywork
python make_js_index.py index.txt index.js

# copy index.js to app1 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/shatapathabr/app1

# Edit index.html
--- head/title: shatapathabr
--- body/title: Śatapatha-Brāhmaṇa, ed. by Albrecht Weber, 1855

# Edit info.html
--- head/title: shatapathabr info
--- body/title: Śatapatha-Brāhmaṇa, ed. by Albrecht Weber, 1855
--- app1 

# Edit main.js
# pdfpages:  shat-0001.pdf

# vp is of form NNNN
--- get_pdfpage_from_index
 let vp = indexobj['vp'];
 let pdf = `shat-${vp}.pdf`;
--- display_ipage_id
 let ipage = indexcur['ipage']; // an int
 
# --------------------
When local debugging done, upload to github

