issue143/readme.txt
04-23-2025 begun ejf
02561 BHAṬṬ. BHAṬṬIKĀVYA

Ref: https://github.com/sanskrit-lexicon/PWG/issues/143

This issue143 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue143

-----------------
pdfs:
BHAṬṬI KĀVYA Vol. 1 (1828).pdf
BHAṬṬI KĀVYA Vol. 2 (1828).pdf

sources:
> (Vol.1): https://archive.org/download/b2874522x_0001/b2874522x_0001.pdf
> (Vol.2): https://archive.org/download/b2874522x_0002/b2874522x_0002.pdf

----------------------------------------
indexes prepared by github user angalinde
Bhattikavya_Vol_I_Index.txt
Bhattikavya_Vol_II_Index.txt

----------------------------------------
Format observations:
vol.	page	sarga	from v.	to v.	ipage	remark(s)
vol is I or II
For vol 1, sarga 1-11
For vol 2, sarga 12-22

----------------------------------------
index.txt  merge of the two indexes above,
 with some adjustments
1. in vol 1
  drop pages 5-10.
2. in vol II
  drop pages 5-8
  drop pages 520-521

In both volumes:
1. fields sarga, fromv, tov may be '---'
 Change these.
 Example:
old:
II	457	20	10	12	449	
II	458	---	---	---	450	
new:
II	457	20	10	12	449	
II	458	20	12	12	450	

2. drop last (remark) field

python make_index.py Bhattikavya_Vol_I_Index.txt Bhattikavya_Vol_II_Index.txt index.txt

1357 cases written to index.txt

----------------------------------------
# construct index.js, and check for internal consistencies

python make_js_index.py index.txt index.js

----------------------------------------
 preliminary check of pwg links
 5 Checks succeeded.  See readme_checks.txt

----------------------------------------
'ready for repo' message in https://github.com/sanskrit-lexicon/PWG/issues/143
----------------------------------------
app construction.
2 apps are needed:  see readme_app.txt
app1 -- (sarga,shloka)
app0 -- VNNN  

----------------------------------------
modify basicadjust.php for pwg, pw, pwkvn, sch, mw
see readme_websanlexicon.txt

----------------------------------------
checks of links from dictionaries
see readme_checks.txt

sync to github:  csl-websanlexicon, csl-apidev
pull github to cologne server
regenerate displays for pwg, pw, pwkvn, sch, mw
=============================================================
THE END

