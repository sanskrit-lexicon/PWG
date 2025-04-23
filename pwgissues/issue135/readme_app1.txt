
=================================================
app1  
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/pantankose
local url:
localhost/sanskrit-lexicon-scans/pantankose/app1/N,N


Github url:
https://sanskrit-lexicon-scans.github.io/pantankose/app1/?N,N

https://sanskrit-lexicon-scans.github.io/pantankose/
shows README.md  (with markdown converted to html)

----------------
# app1 is similar to that of /shakuntala/app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/pantankose
cp -r ../shakuntala/app1 .

# get the index

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue86/index.txt app1/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue86/make_js_index.py app1/pywork/
# revise make_js_index.py to include ipage
# generate index.js
cd app1/pywork
python make_js_index.py index.txt index.js

# copy index.js to app1 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/pantankose/app1

# Edit index.html
--- head/title: pantankose
--- body/title: Pañcatantra, Kosegarten, 1848

# Edit info.html
--- head/title: pantankose info
--- body/title: Pañcatantra, Kosegarten, 1848
--- app1 

# Edit main.js
# pdfpages:  panc-001.pdf

# vp is of form NNN
--- get_pdfpage_from_index
 let vp = indexobj['vp'];
 let pdf = `panc-${vp}.pdf`;
--- display_ipage_id
 let ipage = indexcur['ipage']; // an int
 
# --------------------
When local debugging done, upload to github

