apps for raghuvamsacalc repo

https://sanskrit-lexicon-scans.github.io/raghuvamsacalc/
shows README.md  (with markdown converted to html)
----------------
edit raghuvamsacalc/README.md

=================================================
app0 for raghuvamsacalc repo : internal page number   NOT USED
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/raghuvamsacalc
local url:
localhost/sanskrit-lexicon-scans/raghuvamsacalc/app0/N
 
Github url:
https://sanskrit-lexicon-scans.github.io/raghuvamsacalc/app0/?N

----------------
# app0 is similar to that of /vajasasa/app0
cd /c/xampp/htdocs/sanskrit-lexicon-scans/raghuvamsacalc
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

cd /c/xampp/htdocs/sanskrit-lexicon-scans/raghuvamsacalc/app0

# Edit index.html
--- head/title: raghuvamsacalc
--- body/title: Taittirīya-Sam̃hitā, A. Weber, 1871-2

# Edit info.html
--- head/title: raghuvamsacalc info
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
app1 for raghuvamsacalc repo  (2-parameters)
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/raghuvamsacalc
local url:
localhost/sanskrit-lexicon-scans/raghuvamsacalc/app1/N,N
 
Github url:
https://sanskrit-lexicon-scans.github.io/raghuvamsacalc/app1/?N,N

----------------

# app1 is similar to that of /bchrest1/app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/raghuvamsacalc
cp -r ../bchrest1/app1 .

# get the index

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue109/index.txt app1/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue109/make_js_index.py app1/pywork/
# generate index.js
cd app1/pywork
python make_js_index.py index.txt index.js

# copy index.js to app1 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/raghuvamsacalc/app1

# Edit index.html
--- head/title: raghuvamsacalc
--- body/title: Raghuvaṃśa, Kālidāsa, Calcutta, 1832

# Edit info.html
--- head/title: raghuvamsacalc info
--- body/title: Raghuvaṃśa, Kālidāsa, Calcutta, 1832
--- app1 

# Edit main.js
# pdfpages:  ragh-001.pdf

# --------------------
When local debugging done, upload to github

