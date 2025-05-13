apps for kumaras repo

Note kumaras is similar to bhattikavya

https://sanskrit-lexicon-scans.github.io/kumaras/
shows README.md  (with markdown converted to html)
----------------
edit kumaras/README.md

=================================================
app0 for kumaras repo : ipage
internal page number
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/kumaras
local url:
localhost/sanskrit-lexicon-scans/kumaras/app0/N
  N 3 to 108
  
Github url:
https://sanskrit-lexicon-scans.github.io/kumaras/app0/?N

----------------
# app0 is similar to that of /rajatar/app0
cd /c/xampp/htdocs/sanskrit-lexicon-scans/kumaras
cp -r ../rajatar/app0 .

# 
cp app0/pywork/make_js_index.py app0/pywork/tempwork_make_js_index.py

# get the index for app1 (we'll use it for app0 also)

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue146/index.txt app0/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue146/make_js_index.py app0/pywork/

# revise make_js_index.py so
- only page, ipage and vp in each record of index.js
- remove duplicate ipage records

# generate index.js
cd app0/pywork
python make_js_index.py index.txt index.js

# copy index.js to app0 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/kumaras/app0

# Edit index.html
--- head/title: kumaras
--- body/title: Kumāra Sambhava,  ed. Adolph Stenzler, 1838

# Edit info.html
--- head/title: kumaras info
--- body/title: Kumāra Sambhava,  ed. Adolph Stenzler, 1838
--- app0 

# Edit main.js
# pdfpages:  kum-NNN.pdf,  where NNN is external page number

=================================================
app1 for kumaras repo  (2-parameters)
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/kumaras
local url:
localhost/sanskrit-lexicon-scans/kumaras/app1/N,N
 
Github url:
https://sanskrit-lexicon-scans.github.io/kumaras/app1/?N,N

https://sanskrit-lexicon-scans.github.io/kumaras/
shows README.md  (with markdown converted to html)
----------------

# app1 is similar to that of /rajatar/app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/kumaras
cp -r ../rajatar/app1 .

# get the index for kumaras

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue146/index.txt app1/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue146/make_js_index.py app1/pywork/

# generate index.js
cd app1/pywork
python make_js_index.py index.txt index.js

# copy index.js to app1 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/kumaras/app1

# Edit index.html
--- head/title: kumaras
--- body/title: Kumāra Sambhava,  ed. Adolph Stenzler, 1838

# Edit info.html
--- head/title: kumaras info
--- body/title: Kumāra Sambhava,  ed. Adolph Stenzler, 1838
--- app1 

# Edit main.js
# pdfpages:  kum-NNN.pdf

# --------------------
When local debugging done, upload to github

