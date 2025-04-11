issue124/readme.txt
03-08-2025 begun ejf
06078 VS. VĀJASANEYISAM̃HITĀ

Ref: https://github.com/sanskrit-lexicon/PWG/issues/124

This issue124 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue124

-----------------
pdf: VS.pdf  
---------------------------------------
index.VS.xlsx
  Ref: https://github.com/sanskrit-lexicon/PWG/issues/124#issuecomment-2760647446
index.VS.txt converted to text file, tab-separators

pdf p.	adh.	from v.	to v.	i. p.
103	---	---	---	1
104	1	1a	1a	2

--------------------------------------
index.txt
Some adjustments:
1. Replace '---' as needed
2. For pages 1080-1090, change adhy. from 39 to 40.

python make_index.py index.VS.txt index.txt
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

These all passed.  See first part of readme_checks.txt

-----------------------------------
app construction. see readme_app.txt
2 apps are needed: 

app1 -- (adhyAya,shloka) 
app0 -- (ipage,) 

---------------------------------------
Change to basicadjust to activate links.
see readme_websanlexicon.txt

---------------------------------------
Random checks between dictionary and the pdf and index
 for dictionaries pwg, pw, pkwvn, sch, mw.
 see readme_checks.txt

check_pwg.txt has two cases where Jim classified as NOT FOUND.

=============================================================
sync to github:  csl-websanlexicon, csl-apidev
sync to Cologne, and redo the 5 dictionaries.

-------------------------------------------------------------

738 matches in 737 lines for "<ls>VS. PRĀT. [0-9]+,[0-9]+" in buffer: temp_pwg.txt

from pwgbib-input.txt:
PRĀTIŚĀKHYA zur VĀJASANEYISAM̃HITĀ, citirt nach Adhyāya
   und Sūtra. Hdschr. S. ROTH in der Einl. z. NIR. S. XLVI.
------------------------------------------------------------
THE END
