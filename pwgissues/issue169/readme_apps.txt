rajatarcalc repo

https://github.com/sanskrit-lexicon-scans
new repo
 Owner: sanskrit-lexicon-scans
 repo name: rajatarcalc
 "Rājataraṅgiṇī, Calcutta edition"
 visibility: Public
 add README: On
 CLICK: Create repository
---
Pages
https://github.com/sanskrit-lexicon-scans/rajatarcalc/settings/pages
  Source: 'Depploy from a branch'
  Branch: main
click 'Save'  [This takes a few minutes]

---
Local version:
cd /c/xampp/htdocs/sanskrit-lexicon-scans/
git clone git@github.com:sanskrit-lexicon-scans/rajatarcalc.git
cp rajatar/.gitignore rajatarcalc/

---
pdfpages
cd /c/xampp/htdocs/sanskrit-lexicon-scans/rajatarcalc

cp -r /e/pdfwork/rajatarcalc/pdfpages .

git add .
git commit -m "create pdfpages"
git push  # takes several minutes, depending on upload bandwidth

===============================================================
apps for rajatarcalc repo

Note rajatarcalc is similar to rajatar

https://sanskrit-lexicon-scans.github.io/rajatarcalc/
shows README.md  (with markdown converted to html)
----------------
edit rajatarcalc/README.md

=================================================
app0 for rajatarcalc repo : internal page number
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/rajatarcalc
local url:
localhost/sanskrit-lexicon-scans/rajatarcalc/app0/?N
 
Github url:
https://sanskrit-lexicon-scans.github.io/rajatarcalc/app0/?N

----------------
# app0 is similar to /rajatar/app0
cd /c/xampp/htdocs/sanskrit-lexicon-scans/rajatarcalc
cp -r ../rajatar/app0 .

# get the index for app1 (we'll change this next)

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue169/index.txt app0/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue169/make_js_index.py app0/pywork/

# revise make_js_index.py so
- only page, ipage and vp in each record of index.js
- remove duplicate ipage records

# generate index.js
cd app0/pywork
python make_js_index.py index.txt index.js

# copy index.js to app0 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/rajatarcalc/app0

# Edit index.html
--- head/title: rajatarcalc
--- body/title: Rājataraṅgiṇī, Calcutta edition, 1835

# Edit info.html
--- head/title: rajatarcalc info
--- body/title: Rājataraṅgiṇī, Calcutta edition, 1835
--- app0 

# Edit main.js
# pdfpages:  rajatarcalc_001.pdf

# vp is of form NNN
--- get_pdfpage_from_index
 let vp = indexobj['vp'];
 let pdf = `rajatarcalc_${vp}.pdf`;


=================================================
app1 for rajatarcalc repo  (2-parameters)
=================================================
# app1 is similar to /rajatar/app0
cd /c/xampp/htdocs/sanskrit-lexicon-scans/rajatarcalc
cp -r ../rajatar/app1 .

# get the index for rajatarcalc/app1 

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue169/index.txt app1/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue169/make_js_index.py app1/pywork/

local url:
localhost/sanskrit-lexicon-scans/rajatarcalc/app1/?N,N
 
Github url:
https://sanskrit-lexicon-scans.github.io/rajatarcalc/app1/?N,N

https://sanskrit-lexicon-scans.github.io/rajatarcalc/
shows README.md  (with markdown converted to html)

cd app1/pywork
python make_js_index.py index.txt index.js

# copy index.js to app1 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/rajatarcalc/app1

# Edit index.html
--- head/title: rajatarcalc
--- body/title: Rājataraṅgiṇī, Calcutta edition, 1835

# Edit info.html
--- head/title: rajatarcalc info
--- body/title: Rājataraṅgiṇī, Calcutta edition, 1835
--- app1 

# Edit main.js
# pdfpages:  rajatarcalc_NNN.pdf

# --------------------
When local debugging done, upload to github

cd /c/xampp/htdocs/sanskrit-lexicon-scans/rajatarcalc/
git add app0
git commit -m "create app0"
git add app1
git commit -m "create app1"
git push
