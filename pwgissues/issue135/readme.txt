issue135/readme.txt
04-22-2025 begun ejf
07784 RĀJA-TAR. RĀJATARAṄGIṆĪ

Ref: https://github.com/sanskrit-lexicon/PWG/issues/135

This issue135 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue135

-----------------
pdf: 
source https://download.digitale-sammlungen.de/BOOKS/download.pl?id=bsb10251152

https://www.digitale-sammlungen.de/en/view/bsb10251152

rights: https://rightsstatements.org/page/NoC-NC/1.0/

Rājataraṅgiṇī: histoire des rois du Kachmîr.
 Trad. et commentée par M. A. Troyer  1840
 

----------------------------------------
index:
Rajatarangini_index.revised.txt
 Ref: https://github.com/sanskrit-lexicon/PWG/issues/135#issuecomment-2772730419
 
# copy to index.txt
cp Rajatarangini_index.revised.txt index.txt
  Some adjustments for typos and for purposes of app1
--  remove trailing space in page fields: Example '100 ' -> '100'
--
old: 84	3	94b	102	73
new: 84	3	93b	102	73
--  next is error in pdf:
262	5	477	481*	251
263	5	483*	483	252
in pdf, There is no 482  on page 262/3
 Changing page 262, so 5,482 (which occurs in PWG) will link here
old: 262	5	477	481	251
new: 262	5	477	482	251

--------------
11 matches for "<ls>RĀJA-TAR. 5,482" in buffer: temp_pwg.txt
  some of these checked, and found on p 262/3 of pdf.
1 match for "<ls>RĀJA-TAR. 5,483" in buffer: temp_pwg.txt
  rAjaDama


-------------------------------------------
format
page taranga fromv tov ipage

12	1	1	5a	1
13	1	5b	14	2
14	1	15	24a	3
15	1	24b	33	4

 
taranga is a number: 1-6

-------------------------------------------
# construct index.js, and check for internal consistencies
This is similar to yajnavalkya  issue98
cp ../issue98/make_js_index.py .
# edits:  adhy -> taranga, etc.
python make_js_index.py index.txt index.js

----------------------------------------
 preliminary check of pwg links. for RĀJA-TAR
 5 Checks succeeded.  See readme_checks.txt

----------------------------------------
'ready for repo' message in https://github.com/sanskrit-lexicon/PWG/issues/135
----------------------------------------
app construction.
2 apps are needed:
app1 -- (taranga,shloka) 
app0 --  ipage internal page# 1-293
see readme_app.txt.

----------------------------------------
activate links to rajatar.
See readme_websanlexicon.txt


Random checks between koshas , the pdf and index
see readme_checks.txt

=============================================================
sync to github:  csl-websanlexicon, csl-apidev
sync cologne csl-websanlexicon, csl-apidev
 Regenerate displays for pwg, pw, pwkvn, sch, mw 
sync this PWG repo to github
