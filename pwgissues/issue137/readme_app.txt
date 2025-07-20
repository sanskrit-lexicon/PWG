apps for pancar repo

https://sanskrit-lexicon-scans.github.io/pancar/
shows README.md  (with markdown converted to html)
----------------
edit pancar/README.md

=================================================
app0 for pancar repo : internal page number
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/pancar
local url:
localhost/sanskrit-lexicon-scans/pancar/app0/?N
 
Github url:
https://sanskrit-lexicon-scans.github.io/pancar/app0/?N

----------------
# app0 is similar to that of /katyasr/app0
cd /c/xampp/htdocs/sanskrit-lexicon-scans/pancar
cp -r ../katyasr/app0 .

# get the index for app1:  

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue137/index.txt app0/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue137/make_js_index.py app0/pywork/

# revise make_js_index.py so
- only page, ipage and vp in each record of index.js

# generate index.js
cd app0/pywork
python make_js_index.py index.txt index.js

# copy index.js to app0 
cp index.js ../


-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/pancar/app0

# Edit index.html
--- head/title: pancar
--- body/title: Nārada Pañcarātra, Banerjea, 1865

# Edit info.html
--- head/title: pancar info
--- body/title: Nārada Pañcarātra, Banerjea, 1865
--- app0 

# Edit main.js
# pdfpages:  pancar-001.pdf


=================================================
app1 for pancar repo  (ratr, adhy, verse)
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/pancar
local url:
localhost/sanskrit-lexicon-scans/pancar/app1/N,N,N
 
Github url:
https://sanskrit-lexicon-scans.github.io/pancar/app1/?N,N,N

# app1 is similar to that of /rajatar/app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/pancar
cp -r ../katysr/app1 .

# get the index for pancar

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue137/index.txt app1/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue137/make_js_index.py app1/pywork/
# revise make_js_index.py to include ipage
# generate index.js
cd app1/pywork
python make_js_index.py index.txt index.js

# copy index.js to app1 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/pancar/app1

# Edit index.html
--- head/title: pancar
--- body/title:  Nārada Pañcarātra, Banerjea, 1865

# Edit info.html
--- head/title: pancar info
--- body/title:  Nārada Pañcarātra, Banerjea, 1865
--- app1 

# Edit main.js
# pdfpages:   pancar-001.pdf

# --------------------
When local debugging done, upload to github

