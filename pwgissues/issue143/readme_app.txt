apps for bhattikavya repo

Note bhattikavya is similar to vajasasa

https://sanskrit-lexicon-scans.github.io/bhattikavya/
shows README.md  (with markdown converted to html)
----------------
edit bhattikavya/README.md

=================================================
app0 for bhattikavya repo : VNNN
V = Volume (1 or 2), NNN = external page number
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/bhattikavya
local url:
localhost/sanskrit-lexicon-scans/bhattikavya/app0/VNNN
 
Github url:
https://sanskrit-lexicon-scans.github.io/bhattikavya/app0/?VNNN

----------------
# app0 is similar to that of /taittiriyas/app0
cd /c/xampp/htdocs/sanskrit-lexicon-scans/bhattikavya
cp -r ../taittiriyas/app0 .

# 
cp app0/pywork/make_js_index.py app0/pywork/tempwork_make_js_index.py

# get the index for app1

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue143/index.txt app0/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue143/make_js_index.py app0/pywork/

# revise make_js_index.py so
- only page, ipage and vp in each record of index.js
- remove duplicate ipage records

# generate index.js
cd app0/pywork
python make_js_index.py index.txt index.js

# copy index.js to app0 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/bhattikavya/app0

# Edit index.html
--- head/title: bhattikavya
--- body/title: Bhaṭṭikāvya with commentaries, 1828

# Edit info.html
--- head/title: bhattikavya info
--- body/title: Bhaṭṭikāvya with commentaries, 1828
--- app0 

# Edit main.js
# pdfpages:  bhat1-001.pdf, bhat2-001.pdf, 

=================================================
app1 for bhattikavya repo  (2-parameters)
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/bhattikavya
local url:
localhost/sanskrit-lexicon-scans/bhattikavya/app1/N,N
 
Github url:
https://sanskrit-lexicon-scans.github.io/bhattikavya/app1/?N,N

https://sanskrit-lexicon-scans.github.io/bhattikavya/
shows README.md  (with markdown converted to html)
----------------

# app1 is similar to that of /taittiriyas/app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/bhattikavya
cp -r ../taittiriyas/app1 .

# get the index for bhattikavya

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue143/index.txt app1/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue143/make_js_index.py app1/pywork/

# generate index.js
cd app1/pywork
python make_js_index.py index.txt index.js

# copy index.js to app1 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/bhattikavya/app1

# Edit index.html
--- head/title: bhattikavya
--- body/title: Bhaṭṭikāvya with commentaries, 1828

# Edit info.html
--- head/title: bhattikavya info
--- body/title: Bhaṭṭikāvya with commentaries, 1828
--- app1 

# Edit main.js
# pdfpages:  bhat1-001.pdf, bhat2-001.pdf

# --------------------
When local debugging done, upload to github

