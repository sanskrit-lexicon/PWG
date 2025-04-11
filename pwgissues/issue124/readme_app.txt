apps for vajasasa repo

https://sanskrit-lexicon-scans.github.io/vajasasa/
shows README.md  (with markdown converted to html)
----------------
edit vajasasa/README.md

=================================================
app0 for vajasasa repo : internal page number
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/vajasasa
local url:
localhost/sanskrit-lexicon-scans/vajasasa/app0/N
 
Github url:
https://sanskrit-lexicon-scans.github.io/vajasasa/app0/?N

----------------
# app0 is similar to that of /pantankose/app0
cd /c/xampp/htdocs/sanskrit-lexicon-scans/vajasasa
cp -r ../pantankose/app0 .

# get the index for app1:  

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue124/index.txt app0/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue124/make_js_index.py app0/pywork/

# revise make_js_index.py so
- only page, ipage and vp in each record of index.js
- remove duplicate ipage records

Add two lines to index.txt, for missing pages
197	3	63	63	95
674	18	25b	26	572

# generate index.js
cd app0/pywork
python make_js_index.py index.txt index.js

# copy index.js to app0 
cp index.js ../

# Now index.js has 988 records, from ipage = 1 to ipage = 988

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/vajasasa/app0

# Edit index.html
--- head/title: vajasasa
--- body/title: 

# Edit info.html
--- head/title: vajasasa info
--- body/title: 
--- app0 

# Edit main.js
# pdfpages:  panc-001.pdf

# vp is of form NNNN
--- get_pdfpage_from_index
 let vp = indexobj['vp'];
 let pdf = `yaj-${vp}.pdf`;
--- display_ipage_id
 let ipage = indexcur['ipage']; // an int
 

=================================================
app1 for vajasasa repo  (adhyAya, verse)
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/vajasasa
local url:
localhost/sanskrit-lexicon-scans/vajasasa/app1/N,N
 
Github url:
https://sanskrit-lexicon-scans.github.io/vajasasa/app1/?N,N

https://sanskrit-lexicon-scans.github.io/vajasasa/
shows README.md  (with markdown converted to html)
----------------
edit vajasasa/README.md
----------------
# app1 is similar to that of /pantankose/app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/vajasasa
cp -r ../pantankose/app1 .

# get the index

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue124/index.txt app1/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue124/make_js_index.py app1/pywork/
# revise make_js_index.py to include ipage
# generate index.js
cd app1/pywork
python make_js_index.py index.txt index.js

# copy index.js to app1 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/vajasasa/app1

# Edit index.html
--- head/title: vajasasa
--- body/title: Pañcatantra, Kosegarten, 1848

# Edit info.html
--- head/title: vajasasa info
--- body/title: Pañcatantra, Kosegarten, 1848
--- app1 

# Edit main.js
# pdfpages:  panc-001.pdf

# vp is of form NNN
--- get_pdfpage_from_index
 let vp = indexobj['vp'];
 let pdf = `panc-${vp}.pdf`;
--- display_ipage_id
 let ipage = indexcur['ipage']; // an int
 
# --------------------
When local debugging done, upload to github

