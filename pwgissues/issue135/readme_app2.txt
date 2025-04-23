
=================================================
app2  ipage,line-mu,ber
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/pantankose
local url:
localhost/sanskrit-lexicon-scans/pantankose/app2/N,N


Github url:
https://sanskrit-lexicon-scans.github.io/pantankose/app2/?N,N

https://sanskrit-lexicon-scans.github.io/pantankose/
shows README.md  (with markdown converted to html)

----------------
# app2 is similar to that of /shakuntala/app2
cd /c/xampp/htdocs/sanskrit-lexicon-scans/pantankose
cp -r ../shakuntala/app2 .

# get the index

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue86/index.txt app2/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue86/make_js_index.py app2/pywork/
# revise make_js_index.py to include ipage
# generate index.js
cd app2/pywork
python make_js_index.py index.txt index.js

# copy index.js to app2 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/pantankose/app2

# Edit index.html
--- head/title: pantankose
--- body/title: Pañcatantra, Kosegarten, 1848

# Edit info.html
--- head/title: pantankose info
--- body/title: Pañcatantra, Kosegarten, 1848
--- app2 

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

