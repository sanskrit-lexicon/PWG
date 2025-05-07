apps for katyasr repo

https://sanskrit-lexicon-scans.github.io/katyasr/
shows README.md  (with markdown converted to html)
----------------
edit katyasr/README.md

=================================================
app0 for katyasr repo : internal page number
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/katyasr
local url:
localhost/sanskrit-lexicon-scans/katyasr/app0/?N
 
Github url:
https://sanskrit-lexicon-scans.github.io/katyasr/app0/?N

----------------
# app0 is similar to that of /bhattikavya/app0
cd /c/xampp/htdocs/sanskrit-lexicon-scans/katyasr
cp -r ../bhattikavya/app0 .

# get the index for app1:  

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue136/index.txt app0/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue136/make_js_index.py app0/pywork/

# revise make_js_index.py so
- only page, ipage and vp in each record of index.js
- remove duplicate ipage records

# generate index.js
cd app0/pywork
python make_js_index.py index.txt index.js

# copy index.js to app0 
cp index.js ../

# Now index.js has 988 records, from ipage = 1 to ipage = 988

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/katyasr/app0

# Edit index.html
--- head/title: katyasr
--- body/title: The Śrautasūtra of Kātyāyana, A. Weber, 1859

# Edit info.html
--- head/title: katyasr info
--- body/title: The Śrautasūtra of Kātyāyana, A. Weber, 1859
--- app0 

# Edit main.js
# pdfpages:  katyasr-0001.pdf



=================================================
app1 for katyasr repo  (adhyAya, kanda, verse)
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/katyasr
local url:
localhost/sanskrit-lexicon-scans/katyasr/app1/N,N,N
 
Github url:
https://sanskrit-lexicon-scans.github.io/katyasr/app1/?N,N,N

# app1 is similar to that of /rajatar/app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/katyasr
cp -r ../rajatar/app1 .

# get the index for katyasr

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue136/index.txt app1/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue136/make_js_index.py app1/pywork/
# revise make_js_index.py to include ipage
# generate index.js
cd app1/pywork
python make_js_index.py index.txt index.js

# copy index.js to app1 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/katyasr/app1

# Edit index.html
--- head/title: katyasr
--- body/title: The Śrautasūtra of Kātyāyana, A. Weber, 1859

# Edit info.html
--- head/title: katyasr info
--- body/title: The Śrautasūtra of Kātyāyana, A. Weber, 1859
--- app1 

# Edit main.js
# pdfpages:   katyasr-0001.pdf

# --------------------
When local debugging done, upload to github

