apps for bhartrhari repo

Note bhartrhari is similar to vajasasa

https://sanskrit-lexicon-scans.github.io/bhartrhari/
shows README.md  (with markdown converted to html)
----------------
edit bhartrhari/README.md

=================================================
app0 for bhartrhari repo 

=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/bhartrhari
local url:
localhost/sanskrit-lexicon-scans/bhartrhari/app0/N
 
Github url:
https://sanskrit-lexicon-scans.github.io/bhartrhari/app0/?N

----------------
# app0 is similar to that of /meghasrnga/app0
cd /c/xampp/htdocs/sanskrit-lexicon-scans/bhartrhari
cp -r ../meghasrnga/app0 .

# 
# This is a 'full' index -- no input files used.


# generate index.js
cd app0/pywork
python make_js_index.py index.js

# copy index.js to app0 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/bhartrhari/app0
title: Caurapañcāśikā and Bhartṛhariśataka, ed. Bohlen, 1833
# Edit index.html
--- head/title: bhartrhari
--- body/title: {title}

# Edit info.html
--- head/title: bhartrhari info
--- body/title: {title}
--- app0 

# Edit main.js
# pdfpages:  bhartrhari-001.pdf 001-293

=================================================
app1 for bhartrhari repo  caurap index (1-parameter)
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/bhartrhari
local url:
localhost/sanskrit-lexicon-scans/bhartrhari/app1/N
 
Github url:
https://sanskrit-lexicon-scans.github.io/bhartrhari/app1/?N,N

----------------

# app1 is similar to that of /meghasrnga/app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/bhartrhari
cp -r ../meghasrnga/app1 .

# get the index for cOrapaYcAsikA  (Caurapañcāśikā)

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue148/index_caurap.txt app1/pywork/index.txt

# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue148/make_js_index_caurap.py app1/pywork/make_js_index.py

# generate index.js
cd app1/pywork
python make_js_index.py index.txt index.js

# copy index.js to app1 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/bhartrhari/app1
title: Caurapañcāśikā, ed. Bohlen, 1833

# Edit index.html
--- head/title: bhartrhari
--- body/title: {title}

# Edit info.html
--- head/title: bhartrhari info
--- body/title: {title}
--- app1 

# Edit main.js
# pdfpages:  bhartrhari-NNN.pdf, NNN = 001-293

=================================================
app2 for bhartrhari repo  bhart_index (2-parameters)
 Sataka and verse
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/bhartrhari
local url:
localhost/sanskrit-lexicon-scans/bhartrhari/app2/?N,N
 
Github url:
https://sanskrit-lexicon-scans.github.io/bhartrhari/app2/?N,N

----------------

# app2 is similar to that of /rajatar/app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/bhartrhari
cp -r ../rajatar/app1 app2

# get the index for bhartṛhariśataka

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue148/index_bhart.txt app2/pywork/index.txt

# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue148/make_js_index_bhart.py app2/pywork/make_js_index.py

# generate index.js
cd app2/pywork
python make_js_index.py index.txt index.js

# copy index.js to app2
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/bhartrhari/app1
title: Bhartṛhariśataka, ed. Bohlen, 1833

# Edit index.html
--- head/title: bhartrhari
--- body/title: {title}

# Edit info.html
--- head/title: bhartrhari info
--- body/title: {title}
--- app1 

# Edit main.js
# pdfpages:  bhartrhari-NNN.pdf, NNN = 001-293

# --------------------
When local debugging done, upload to github

