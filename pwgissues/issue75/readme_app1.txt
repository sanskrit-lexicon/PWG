
=================================================
app1
=================================================
https://sanskrit-lexicon-scans.github.io/ramayanabom/
# Initialize README.md 
# Activate Pages hosting at github (settings/pages ...)

# clone locally
cd /c/xampp/htdocs/sanskrit-lexicon-scans/
git clone git@github.com:sanskrit-lexicon-scans/ramayanabom.git


# 
/c/xampp/htdocs/sanskrit-lexicon-scans/ramayanabom
local url:
localhost/sanskrit-lexicon-scans/ramayanabom/app1/?N,N,N
or ?N,N,N,N (prakshipta)


Github url:
https://sanskrit-lexicon-scans.github.io/ramayanabom/app1/

https://sanskrit-lexicon-scans.github.io/ramayanabom/
shows README.md  (with markdown converted to html)

----------------
# app1 is similar to that of ŚATAPATHABRĀHMAṆA /shatapathabr/app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/ramayanabom
cp -r ../shatapathabr/app1 .

# get the index
  (in three parts for volumes 1,2,3  indexv1.txt, indexv2.txt indexv3.txt

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue75/indexv1.txt app1/pywork/indexv1.txt
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue75/indexv2.txt app1/pywork/indexv2.txt
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue75/indexv3.txt app1/pywork/indexv3.txt

# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue75/make_js_index.py app1/pywork/make_js_index.py

# generate index.js
cd app1/pywork
python make_js_index.py indexv1.txt indexv2.txt indexv3.txt index.js

# copy index.js to app1 
cp index.js ../

-------------------------------------
cd /c/xampp/htdocs/sanskrit-lexicon-scans/ramayanabom/
edit README.md


cd /c/xampp/htdocs/sanskrit-lexicon-scans/ramayanabom/app1


# Edit index.html
--- head/title: ramayanabom
--- body/title: Rāmāyaṇa, Bombay edition, 1859

# Edit info.html
--- head/title: ramayanabom info
--- body/title: Rāmāyaṇa, Bombay edition, 1859
--- app1 

# Edit main.js
# pdfpages are in three sections
pdfpages1:  ram-I-NNN.pdf   
pdfpages2:  ram-II-NNN.pdf
pdfpages3:  ram-III-NNN.pdf
 
# --------------------
When local debugging done, upload to github

