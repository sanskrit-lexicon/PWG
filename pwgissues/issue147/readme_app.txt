apps for meghasrnga repo

https://sanskrit-lexicon-scans.github.io/meghasrnga/
shows README.md  (with markdown converted to html)
----------------
edit meghasrnga/README.md

apps:
app0 ipage   Applies to both indexes.  All pages

 epage 1-5  
 ipage epage
  i  6
  ii 7
  iii 8 main title page
  iv 9
  v 10  Praefatio
  vi 11
  vii 12
  viii 13 end Praefatio
  1  14 meghadUta title
  2  15 blank
  3  16 first verse of meghadhuta  begin index_megha.txt
  ...
  31 44  last of meGadUta 
  32 45  ?
  33 46  SfNgAratilaka title
  34 47  blank
  35 48  first verse of SfNgAratilaka begin index_srnga.txt
  ...
  40 53  last verse of SfNgAratilaka
  
  41 54  annotatio critica begin
  42 55  blank
  43 56  Varietas lectionis in meGadUta
  44 57   ...
  ...
  53 66  end Varietas lectionis in meGadUta, begin Varietas lectionis in SfNgAratilaka
  56 69  end Varietas lectionis in SfNgAratilaka  end annotatio
  
  57 70  Glossarium
  58 71  blank
  59 72  Begin kosha! (glossarium)
  60 73  continue glossarium
  ...
  135 148 end glossarium
  136 149 addenda et emendenda
  [ blank epages 150-153]
=================================================
app0 for meghasrnga repo : a parameter, N internal page number
NNN = external page number
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/meghasrnga
local url:
localhost/sanskrit-lexicon-scans/meghasrnga/app0/?N
 
Github url:
https://sanskrit-lexicon-scans.github.io/meghasrnga/app0/?N

----------------
# app0 is similar to that of /malavikagni/app0
cd /c/xampp/htdocs/sanskrit-lexicon-scans/meghasrnga
cp -r ../malavikagni/app0 .

index.txt not needed.
# revise make_js_index.py so
- only page, ipage and vp, title

# generate index.js
cd app0/pywork
python make_js_index.py index.js

# copy index.js to app0 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/meghasrnga/app0
title = Meghadūta and Śṛṅgāratilaka, J. Gildemeister, 1841
# Edit index.html
--- head/title: Meghadūta
--- body/title: {title}

# Edit info.html
--- head/title: meghasrnga info
--- body/title: {title}
--- app0 

# Edit main.js
# pdfpages:  bhat1-001.pdf, bhat2-001.pdf, 

=================================================
app1 for meghasrnga repo  1 parameter (verse)  meghaduta verses
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/meghasrnga
local url:
localhost/sanskrit-lexicon-scans/meghasrnga/app1/?N
 
Github url:
https://sanskrit-lexicon-scans.github.io/meghasrnga/app1/?N

----------------

# app1 is similar to that of /bchrest1/app3
cd /c/xampp/htdocs/sanskrit-lexicon-scans/meghasrnga
cp -r ../bchrest1/app3 app1

# get the index for meghaduta

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue147/index_megha.txt app1/pywork/index.txt
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue147/make_js_index.py app1/pywork/

# generate index.js
cd app1/pywork
python make_js_index.py index.txt index.js

# copy index.js to app1 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/meghasrnga/app1
titles = 
# Edit index.html
--- head/title: meghasrnga
--- body/title: {titles}

# Edit info.html
--- head/title: meghasrnga info
--- body/title: {titles}
--- app1 

# Edit main.js
# pdfpages:  meghasrnga-001.pdf, bhat2-001.pdf

=================================================
app2 for meghasrnga repo  1 parameter (verse)  Śṛṅgāratilaka verses
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/meghasrnga
local url:
localhost/sanskrit-lexicon-scans/meghasrnga/app2/?N
 
Github url:
https://sanskrit-lexicon-scans.github.io/meghasrnga/app2/?N

----------------

# app2 is similar to app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/meghasrnga
cp -r app1 app2

# get the index for Śṛṅgāratilaka

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue147/index_srnga.txt app2/pywork/index.txt
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue147/make_js_index.py app2/pywork/

# generate index.js
cd app2/pywork
python make_js_index.py index.txt index.js

# copy index.js to app2 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/meghasrnga/app2
titles = 
# Edit index.html
--- head/title: meghasrnga
--- body/title: {titles}

# Edit info.html
--- head/title: meghasrnga info
--- body/title: {titles}
--- app2 

# Edit main.js
# pdfpages:  meghasrnga-001.pdf, bhat2-001.pdf

# --------------------
When local debugging done, upload to github

