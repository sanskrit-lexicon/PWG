issue136/readme.txt
03-28-2025 begun ejf
KĀTYĀYANA'S ŚRAUTASŪTRĀṆI

Ref: https://github.com/sanskrit-lexicon/PWG/issues/136

This issue136 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue136

-----------------
pdf:
/e/pdfwork/katyasr/katyasr.pdf
-----------------
Anna's comments
KATY.SR._Comments.docx.pdf

---------------------------------------
KATY.SR._Index.xlsx  From Anna
index_orig.txt converted to text file, tab-separators

7 fields per line
page	adhy	kaṇḍ	fromv	tov	ipage	remark(s)
23	1	1	 -	 --	1	
24	1	1	1	1	2	

--------------------------------------
index.txt
Some adjustments:
1. remove remarks
2. replace - -- cases
3. remove last 2 lines (corrections)
4. Remove (1) and (2) at page = 742,743,883,884
python make_index.py index_orig.txt index.txt
dropping line # 1253: 1137       -       --      -       --     1111    Correcti
ons
dropping line # 1254: 1138       -       --      -       --     1112    continue

1252 cases written to index.txt

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
