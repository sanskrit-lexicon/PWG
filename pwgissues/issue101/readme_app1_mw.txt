
=================================================
app1   for sahityadarpana_mw 
=================================================

https://sanskrit-lexicon-scans.github.io/sahityadarpana_mw/

# local version
cd /c/xampp/htdocs/sanskrit-lexicon-scans/
git clone git@github.com:sanskrit-lexicon-scans/sahityadarpana_mw.git

/c/xampp/htdocs/sanskrit-lexicon-scans/sahityadarpana_mw
local url:
localhost/sanskrit-lexicon-scans/sahityadarpana_mw/app1/?N,N
 (paricCeda,kArikA)

Github url:
https://sanskrit-lexicon-scans.github.io/sahityadarpana_mw/app1/?N,N

https://sanskrit-lexicon-scans.github.io/sahityadarpana_mw/
shows README.md  (with markdown converted to html)

----------------
# app1 is similar to that of /markandeyapurana/app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/sahityadarpana_mw
cp -r ../markandeyapurana/app1 app1

# get the index

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue101/index_v4.txt app1/pywork/index.txt

# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue101/make_js_index_v4.py app1/pywork/make_js_index.py
# revise make_js_index.py to include ipage
# generate index.js
cd app1/pywork
python make_js_index.py index.txt index.js

# copy index.js to app1 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/sahityadarpana_mw/app1

# Edit index.html
--- head/title: sahityadarpana_mw
--- body/title: Sāhityadarpaṇa of Viśvanātha, (1936 edition)

# Edit info.html
--- head/title: sahityadarpana_mw info
--- body/title: [same as above]
--- app1 

# Edit main.js
# pdfpages:  sah-001.pdf

# vp is of form NNN
--- get_pdfpage_from_index
 let vp = indexobj['vp'];
 let pdf = `sah-${vp}.pdf`;
--- display_ipage_id
 let ipage = indexcur['ipage']; // an int

--- appipage
 This provides access by internal page number.
 It is used for the next page, previous page UI elements of app1.
 
# --------------------
When local debugging done, sync sahityadarpana_mw to github
# --------------------
modify basicadjust.php in csl-websanlexicon.
sh apidev_copy.sh
When done, sync csl-websanlexicon and csl-apidev to Github.

