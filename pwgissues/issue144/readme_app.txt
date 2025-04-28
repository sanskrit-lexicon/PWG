apps for taittiriyas repo

https://sanskrit-lexicon-scans.github.io/taittiriyas/
shows README.md  (with markdown converted to html)
----------------
edit taittiriyas/README.md

=================================================
app0 for taittiriyas repo : internal page number
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/taittiriyas
local url:
localhost/sanskrit-lexicon-scans/taittiriyas/app0/N
 
Github url:
https://sanskrit-lexicon-scans.github.io/taittiriyas/app0/?N

----------------
# app0 is similar to that of /vajasasa/app0
cd /c/xampp/htdocs/sanskrit-lexicon-scans/taittiriyas
cp -r ../vajasasa/app0 .

cp app0/pywork/make_js_index.py app0/pywork/tempwork_make_js_index.py

# get the index for app1 (we'll change this next)

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue134/index.txt app0/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue134/make_js_index.py app0/pywork/

# revise make_js_index.py so
- only page, ipage and vp in each record of index.js
- remove duplicate ipage records

# generate index.js
cd app0/pywork
python make_js_index.py index.txt index.js

# copy index.js to app0 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/taittiriyas/app0

# Edit index.html
--- head/title: taittiriyas
--- body/title: Taittirīya-Sam̃hitā, A. Weber, 1871-2

# Edit info.html
--- head/title: taittiriyas info
--- body/title: Taittirīya-Sam̃hitā, A. Weber, 1871-2
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
app1 for taittiriyas repo  (4-parameters)
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/taittiriyas
local url:
localhost/sanskrit-lexicon-scans/taittiriyas/app1/N,N,N,N
 
Github url:
https://sanskrit-lexicon-scans.github.io/taittiriyas/app1/?N,N,N,N

https://sanskrit-lexicon-scans.github.io/taittiriyas/
shows README.md  (with markdown converted to html)
----------------

# app1 is similar to that of /shatapathabr/app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/taittiriyas
cp -r ../shatapathabr/app1 .

# get the index

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue134/index.txt app1/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue134/make_js_index.py app1/pywork/
# revise make_js_index.py to include ipage
# generate index.js
cd app1/pywork
python make_js_index.py index.txt index.js

# copy index.js to app1 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/taittiriyas/app1

# Edit index.html
--- head/title: taittiriyas
--- body/title: Taittirīya-Sam̃hitā, A. Weber, 1871-2

# Edit info.html
--- head/title: taittiriyas info
--- body/title: Taittirīya-Sam̃hitā, A. Weber, 1871-2
--- app1 

# Edit main.js
# pdfpages:  tai1-001.pdf, tai2-001.pdf

# --------------------
When local debugging done, upload to github

