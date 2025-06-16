
=================================================
app1  
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/hitopadesha
local url:
localhost/sanskrit-lexicon-scans/hitopadesha/app1/N,N


Github url:
https://sanskrit-lexicon-scans.github.io/hitopadesha/app1/?N,N

https://sanskrit-lexicon-scans.github.io/hitopadesha/
shows README.md  (with markdown converted to html)

----------------
# app1 is similar to that of /pantakose/app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/hitopadesha
cp -r ../pantakose/app1 .

# get the index

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue152/index.txt app1/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue152/make_js_index.py app1/pywork/
# revise make_js_index.py to include ipage
# generate index.js
cd app1/pywork
python make_js_index.py index.txt index.js

# copy index.js to app1 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/hitopadesha/app1

# Edit index.html
--- head/title: hitopadesha
--- body/title: Hitopadeśa, ed. Schlegel und Lassen, 1829

# Edit info.html
--- head/title: hitopadesha info
--- body/title: Hitopadeśa, ed. Schlegel und Lassen, 1829
--- app1 

# Edit main.js
# pdfpages:  hit-001.pdf

# vp is of form NNN
--- get_pdfpage_from_index
 let vp = indexobj['vp'];
 let pdf = `panc-${vp}.pdf`;
--- display_ipage_id
 let ipage = indexcur['ipage']; // an int
 
# --------------------
When local debugging done, upload to github

