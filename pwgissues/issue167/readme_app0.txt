
=================================================
app0
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/nirukta
local url:
localhost/sanskrit-lexicon-scans/nirukta/app0/N


Github url:
https://sanskrit-lexicon-scans.github.io/nirukta/app0/?N

https://sanskrit-lexicon-scans.github.io/nirukta/
shows README.md  (with markdown converted to html)

----------------
# app0 is similar to that of /aitbr_auf/app0
cd /c/xampp/htdocs/sanskrit-lexicon-scans/nirukta
cp -r ../aitbr_auf/app0 .


# get the index (before revision)

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue167/index.txt app0/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue167/make_js_index.py app0/pywork/

Use an alternate:  ipage 1-608, epage = ipage + 21
# generate index.js
cd app0/pywork
python make_js_index1.py index.js

# copy index.js to app0
cp index.js ../

-------------------------------------
TITLE = Yāska's Nirukta with Nighaṇṭavas, ed. Roth, 1852
cd /c/xampp/htdocs/sanskrit-lexicon-scans/nirukta/app0

# Edit index.html
--- head/title: nirukta
--- body/title: TITLE

# Edit info.html
--- head/title: nirukta info
--- body/title: TITLE
--- app0 

# Edit main.js
# pdfpages:  nirukta_001.pdf

# vp is of form NNN
--- get_pdfpage_from_index
 let vp = indexobj['vp'];
 let pdf = `nirukta_${vp}.pdf`;
--- display_ipage_id
 let ipage = indexcur['ipage']; // an int
 
# --------------------
When local debugging done, upload to github

