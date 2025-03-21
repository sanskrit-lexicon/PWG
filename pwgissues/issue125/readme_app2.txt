
=================================================
app2
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/shakuntala
local url:
localhost/sanskrit-lexicon-scans/shakuntala/app2/N,N
 (ipage,linenum)

Github url:
https://sanskrit-lexicon-scans.github.io/shakuntala/app2/?N,N

https://sanskrit-lexicon-scans.github.io/shakuntala/
shows README.md  (with markdown converted to html)

----------------
# app2 is similar to that of /markandeyapurana/app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/shakuntala
cp -r ../markandeyapurana/app1 app2

# get the index

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue125/index.txt app2/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue125/make_js_index.py app2/pywork/
# revise make_js_index.py to include ipage
# generate index.js
cd app2/pywork
python make_js_index.py index.txt index.js

# copy index.js to app2 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/shakuntala/app2

# Edit index.html
--- head/title: shakuntala
--- body/title: Abhijñānaśakuntala, Böhtlingk, Otto von, 1842

# Edit info.html
--- head/title: shakuntala info
--- body/title: Abhijñānaśakuntala, Böhtlingk, Otto von, 1842
--- app2 

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

