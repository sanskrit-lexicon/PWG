
=================================================
app2
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/nirukta
local url:
localhost/sanskrit-lexicon-scans/nirukta/app2/?N,N


Github url:
https://sanskrit-lexicon-scans.github.io/nirukta/app2/?N,N

https://sanskrit-lexicon-scans.github.io/nirukta/
shows README.md  (with markdown converted to html)

----------------
# app2 is similar to app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/nirukta
cp -r app1 app2

# get the index (naighantuka)
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue167/index_naigh.txt app2/pywork/index.txt

# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue167/make_js_index_naigh.py app2/pywork/make_js_index.py


# generate index.js
cd app1/pywork
python make_js_index_nir.py index.txt index.js

# copy index.js to app1
cp index.js ../

-------------------------------------
TITLE = Yāska's Nirukta with Nighaṇṭavas, ed. Roth, 1852
cd /c/xampp/htdocs/sanskrit-lexicon-scans/nirukta/app2

# Edit index.html
--- head/title: nirukta
--- body/title: TITLE

# Edit info.html
--- head/title: nirukta info
--- body/title: TITLE
--- app2

# Edit main.js
# pdfpages:  nirukta_001.pdf

# vp is of form NNN

# --------------------
When local debugging done, upload to github

