
=================================================
app1
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/shakuntala
local url:
localhost/sanskrit-lexicon-scans/shakuntala/app1/N


Github url:
https://sanskrit-lexicon-scans.github.io/shakuntala/app1/?N

https://sanskrit-lexicon-scans.github.io/shakuntala/
shows README.md  (with markdown converted to html)

----------------
# app1 is similar to that of /markandeyapurana/app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/shakuntala
cp -r ../markandeyapurana/app1 .

# get the index

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue125/index.txt app1/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue125/make_js_index.py app1/pywork/
# revise make_js_index.py to include ipage
# generate index.js
cd app1/pywork
python make_js_index.py index.txt index.js

# copy index.js to app1 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/shakuntala/app1

# Edit index.html
--- head/title: shakuntala
--- body/title: Abhijñānaśakuntala, Böhtlingk, Otto von, 1842

# Edit info.html
--- head/title: shakuntala info
--- body/title: Abhijñānaśakuntala, Böhtlingk, Otto von, 1842
--- app1 

# Edit main.js
# pdfpages:  Sak-001.pdf

# vp is of form NNN
--- get_pdfpage_from_index
 let vp = indexobj['vp'];
 let pdf = `Sak-${vp}.pdf`;
--- display_ipage_id
 let ipage = indexcur['ipage']; // an int
 
# --------------------
When local debugging done, upload to github

