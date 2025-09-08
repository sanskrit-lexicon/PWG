
=================================================
app1  nirukta by adhy,verse
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/nirukta
local url:
localhost/sanskrit-lexicon-scans/nirukta/app1/?N

Github url:
https://sanskrit-lexicon-scans.github.io/nirukta/app1/?N

https://sanskrit-lexicon-scans.github.io/nirukta/
shows README.md  (with markdown converted to html)

----------------
# app1 is similar to vikramor/app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/nirukta
cp -r ../vikramor/app1 app1

# get the index (naighantuka)
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue167/index_nir.txt app1/pywork/index.txt

# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue167/make_js_index_nir.py app1/pywork/make_js_index.py

# generate index.js
cd app1/pywork
python make_js_index_nir.py index.txt index.js

# copy index.js to app1
cp index.js ../

-------------------------------------
TITLE = Yāska's Nirukta with Nighaṇṭavas, ed. Roth, 1852
cd /c/xampp/htdocs/sanskrit-lexicon-scans/nirukta/app1

# Edit index.html
--- head/title: nirukta
--- body/title: TITLE

# Edit info.html
--- head/title: nirukta info
--- body/title: TITLE
--- app1

# Edit main.js
# pdfpages:  nirukta_001.pdf

# vp is of form NNN
--- get_pdfpage_from_index
 let vp = indexobj['vp'];
 let pdf = `nirukta_${vp}.pdf`;
--- display_ipage_id
 let ipage = indexcur['ipage']; // an int
 
# --------------------
When local debugging done, upload to github

