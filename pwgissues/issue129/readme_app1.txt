
=================================================
app1
=================================================
https://sanskrit-lexicon-scans.github.io/bhagavadgita/
# Initialize README.md 
# Activate Pages hosting at githubb  (settings/pages ...)

# clone locally
cd /c/xampp/htdocs/sanskrit-lexicon-scans/
git clone git@github.com:sanskrit-lexicon-scans/bhagavadgita.git


# 
/c/xampp/htdocs/sanskrit-lexicon-scans/bhagavadgita
local url:
localhost/sanskrit-lexicon-scans/bhagavadgita/app1/?N,N


Github url:
https://sanskrit-lexicon-scans.github.io/bhagavadgita/app1/?N,N

https://sanskrit-lexicon-scans.github.io/bhagavadgita/
shows README.md  (with markdown converted to html)

----------------
# app1 is similar to that of /markandeyapurana/app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/bhagavadgita
cp -r ../markandeyapurana/app1 .

# get the index

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue129/index.txt app1/pywork/index.txt
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue129/make_js_index.py app1/pywork/make_js_index.py
# revise make_js_index.py to include ipage
# generate index.js
cd app1/pywork
python make_js_index.py index.txt index.js

# copy index.js to app1 
cp index.js ../

-------------------------------------
cd /c/xampp/htdocs/sanskrit-lexicon-scans/bhagavadgita/
edit README.md


cd /c/xampp/htdocs/sanskrit-lexicon-scans/bhagavadgita/app1


# Edit index.html
--- head/title: bhagavadgita
--- body/title: Bhagavadgītā,  A. W. Schlegel, 1823

# Edit info.html
--- head/title: bhagavadgita info
--- body/title: Bhagavadgītā,  A. W. Schlegel, 1823
--- app1 

# Edit main.js
# pdfpages:  bhag-001.pdf

# vp is of form NNN
--- get_pdfpage_from_index
 let vp = indexobj['vp'];
 let pdf = `bhag-${vp}.pdf`;
--- display_ipage_id
 let ipage = indexcur['ipage']; // an int
 
# --------------------
When local debugging done, upload to github

