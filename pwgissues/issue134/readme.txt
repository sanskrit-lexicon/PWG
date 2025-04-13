issue134/readme.txt
04-11-2025 begun ejf
05387 TS. TAITTIRĪYASAM̃HITĀ

Ref: https://github.com/sanskrit-lexicon/PWG/issues/134

This issue134 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue134

-----------------
pdf: in two parts:
taittiriya_1.pdf, taittiriya_2.pdf

---------------------------------------
Taittiriya.Samhita.Index.xlsx
  Ref: https://github.com/sanskrit-lexicon/PWG/issues/134
  index_orig.txt  converted to text file, tab-separators

Vol     page    kaṇḍa   prapāṭhaka      anuvāka vers from       vers to int page
I       14      I       1       1       1       1       1
I       14      I       1       2       1a      1a      1
I       15      I       1       2       1b      2       2
I       15      I       1       3       1a      1a      2
I       16      I       1       3       1b      1b      3
I       16      I       1       4       1       2       3
I       17      ---     ---     ---     ---     ---     ---     ipage 2 repeated
I       18      ---     ---     ---     ---     ---     ---     ipage 3 repeated
I       19      I       1       5       1       2       4

--------------------------------------
4369 matches in 4365 lines for "<ls>TS. [0-9]+,[0-9]+,[0-9]+,[0-9]+" in buffer: temp_pwg.txt

Preliminary check of consistency of index with the two pdfs for pwg.
Ready for repo.
File names in pdfpages directory of repo:
tai-1001.pdf through tai-1433.pdf for volume 1
tai-2001.pdf through tai-2415.pdf for volume 2

---------------------------------------
index.txt some edits of index_orig.txt
 # remove lines whose 4th parameter contains '-' or 'X'
 # drop the last (9th) parameter (remark)

python make_index.py index_orig.txt  index.txt
70 lines dropped
1202 cases written to index.txt


-------------------------------------------
# construct index.js, and check for internal consistencies
python make_js_index.py index.txt index.js

----------------------------------------
# get temporary local copy of dictionaries for checking
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt

----------------------------------------
# preliminary check of temp_pwg.txt and index and pdf

These all passed.

repo sanskrit-lexicon-scans/taittiriyas constructed

-----------------------------------
app construction. see readme_app.txt
2 apps are needed: 

app1 -- (kaṇḍa, prapāṭhaka, anuvāka, verse)
app0 -- (external page)

---------------------------------------
Change to basicadjust to activate links.
see readme_websanlexicon.txt

---------------------------------------
Random checks between dictionary and the pdf and index
 for dictionaries pwg, pw, pkwvn, sch, mw.
 see readme_checks.txt

check_mw.txt has one case classified as NOT FOUND.

=============================================================
sync to github:  csl-websanlexicon, csl-apidev
sync to Cologne, and redo the 5 dictionaries.

-------------------------------------------------------------

THE END

