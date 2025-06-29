
=================================================
app1  
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/amara_col
local url:
localhost/sanskrit-lexicon-scans/amara_col/app1/N,N,N,N or N,N,N


Github url:
https://sanskrit-lexicon-scans.github.io/amara_col/app1/?N,N,N,N

https://sanskrit-lexicon-scans.github.io/amara_col/
shows README.md  (with markdown converted to html)

----------------
# app1 is similar to that of /amara_dlc/app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/amara_col
cp -r ../amara_dlc/app1 .

# get the index

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue154/index.txt app1/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue154/make_js_index.py app1/pywork/
# generate index.js
cd app1/pywork
python make_js_index.py index.txt index.js

# copy index.js to app1 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/amara_col/app1

TITLE = Amarakosha, ed. Colebrooke, 1808.
# Edit index.html
--- head/title: amara_col
--- body/title: {TITLE}

# Edit info.html
--- head/title: amara_col info
--- body/title: {TITLE}
--- app1 

# Edit main.js
# pdfpages:  amara_col-001.pdf

# vp is of form NNN
--- get_pdfpage_from_index
 let vp = indexobj['vp'];
 let pdf = `amar1-${vp}.pdf`;
--- display_ipage_id
 let ipage = indexcur['ipage']; // an int
 
# --------------------
When local debugging done, upload to github

