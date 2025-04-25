apps for rajatar repo

Note rajatar is similar to vajasasa

https://sanskrit-lexicon-scans.github.io/rajatar/
shows README.md  (with markdown converted to html)
----------------
edit rajatar/README.md

=================================================
app0 for rajatar repo : internal page number
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/rajatar
local url:
localhost/sanskrit-lexicon-scans/rajatar/app0/N
 
Github url:
https://sanskrit-lexicon-scans.github.io/rajatar/app0/?N

----------------
# app0 is similar to that of /vajasasa/app0
cd /c/xampp/htdocs/sanskrit-lexicon-scans/rajatar
cp -r ../vajasasa/app0 .

# 
cp app0/pywork/make_js_index.py app0/pywork/tempwork_make_js_index.py

# get the index for app1 (we'll change this next)

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue135/index.txt app0/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue135/make_js_index.py app0/pywork/

# revise make_js_index.py so
- only page, ipage and vp in each record of index.js
- remove duplicate ipage records

# generate index.js
cd app0/pywork
python make_js_index.py index.txt index.js

# copy index.js to app0 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/rajatar/app0

# Edit index.html
--- head/title: rajatar
--- body/title: Rājataraṅgiṇī, M. A. Troyer, 1840

# Edit info.html
--- head/title: rajatar info
--- body/title: Rājataraṅgiṇī, M. A. Troyer, 1840
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
app1 for rajatar repo  (2-parameters)
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/rajatar
local url:
localhost/sanskrit-lexicon-scans/rajatar/app1/N,N
 
Github url:
https://sanskrit-lexicon-scans.github.io/rajatar/app1/?N,N

https://sanskrit-lexicon-scans.github.io/rajatar/
shows README.md  (with markdown converted to html)
----------------

# app1 is similar to that of /vajasasa/app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/rajatar
cp -r ../vajasasa/app1 .

# get the index for rajatar

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue135/index.txt app1/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue135/make_js_index.py app1/pywork/
# revise make_js_index.py to include ipage
# generate index.js
cd app1/pywork
python make_js_index.py index.txt index.js

# copy index.js to app1 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/rajatar/app1

# Edit index.html
--- head/title: rajatar
--- body/title: Rājataraṅgiṇī, M. A. Troyer, 1840

# Edit info.html
--- head/title: rajatar info
--- body/title: Rājataraṅgiṇī, M. A. Troyer, 1840
--- app1 

# Edit main.js
# pdfpages:  tai1-001.pdf, tai2-001.pdf

# --------------------
When local debugging done, upload to github

