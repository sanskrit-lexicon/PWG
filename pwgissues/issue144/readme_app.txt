apps for taittiriyabr repo

https://sanskrit-lexicon-scans.github.io/taittiriyabr/
shows README.md  (with markdown converted to html)
----------------
edit taittiriyabr/README.md

=================================================
app0 for taittiriyabr repo : internal page number
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/taittiriyabr
local url:
localhost/sanskrit-lexicon-scans/taittiriyabr/app0/N
 
Github url:
https://sanskrit-lexicon-scans.github.io/taittiriyabr/app0/?N

----------------
# app0 is similar to that of /taittiriyas/app0
cd /c/xampp/htdocs/sanskrit-lexicon-scans/taittiriyabr
cp -r ../taittiriyas/app0 .

cp app0/pywork/make_js_index.py app0/pywork/tempwork_make_js_index.py

# get the index for app1 (we'll change this next)

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue144/index.txt app0/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue144/make_js_index.py app0/pywork/

# revise make_js_index.py so
- only  vp, vip in each record of index.js
- remove duplicate vp records

# generate index.js
cd app0/pywork
python make_js_index.py index.txt index.js

# copy index.js to app0 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/taittiriyabr/app0

# Edit index.html
--- head/title: taittiriyabr
--- body/title: Taittirīya-Brāhmaṇa, Rājendralāla Mitra, 1859-1872

# Edit info.html
--- head/title: taittiriyabr info
--- body/title: Taittirīya-Brāhmaṇa, Rājendralāla Mitra, 1859-1872
--- app0 

# Edit main.js
# pdfpages:  tai-1001.pdf

# vp is of form NNNN
--- get_pdfpage_from_index
 let vp = indexobj['vp'];
 let pdf = `taij-${vp}.pdf`;
--- display_ipage_id
 let ipage = indexcur['ipage']; // an int
 

=================================================
app1 for taittiriyabr repo  (4-parameters)
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/taittiriyabr
local url:
localhost/sanskrit-lexicon-scans/taittiriyabr/app1/N,N,N,N
 
Github url:
https://sanskrit-lexicon-scans.github.io/taittiriyabr/app1/?N,N,N,N

https://sanskrit-lexicon-scans.github.io/taittiriyabr/
shows README.md  (with markdown converted to html)
----------------

# app1 is similar to that of /shatapathabr/app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/taittiriyabr
cp -r ../shatapathabr/app1 .

# get the index

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue144/index.txt app1/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue144/make_js_index.py app1/pywork/
# revise make_js_index.py to include ipage
# generate index.js
cd app1/pywork
python make_js_index.py index.txt index.js

# copy index.js to app1 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/taittiriyabr/app1

# Edit index.html
--- head/title: taittiriyabr
--- body/title: Taittirīya-Sam̃hitā, A. Weber, 1871-2

# Edit info.html
--- head/title: taittiriyabr info
--- body/title: Taittirīya-Sam̃hitā, A. Weber, 1871-2
--- app1 

# Edit main.js
# pdfpages:  tai1-001.pdf, tai2-001.pdf

# --------------------
When local debugging done, upload to github

