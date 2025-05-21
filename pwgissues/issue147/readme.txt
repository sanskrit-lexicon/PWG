issue147/readme.txt
05-09-2025 begun ejf

MEGHADŪTA   ŚṚṄGĀRATILAKA  two works in same pdf

Ref: https://github.com/sanskrit-lexicon/PWG/issues/147

This issue147 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue147

-----------------
pdf: /e/pdfwork/meghaduta/


----------------------------------------
indexes prepared by github user OFar0101
cp /e/pdfwork/meghaduta/index_megha_orig.txt .
cp /e/pdfwork/meghaduta/index_srnga_orig.txt .

----------------------------------------
Format observations:
index_megha_orig.txt

page	vers from	vers to	int page	
14	==	==	1	The title page
15	==	==	2	
16	1	2	3	


index_srnga_orig.txt
page	vers from	vers to	int page	
46	==	==	33	The title page
47	==	==	34	
48	1	2	35	

----------------------------------------
index_megha.txt minor changes
1. Remove 'remarks' field at end of lines
2. discard first 2 lines:
14	==	==	1	The title page
15	==	==	2	
3. discard last line
45			32	

python make_index_megha.py index_megha_orig.txt index_megha.txt
30 cases written to index_megha.txt

----------------------------------------
index_srnga.txt minor changes
1. Remove 'remarks' field at end of lines
2. discard first 2 lines:
46	==	==	33	The title page
47	==	==	34	

python make_index_srnga.py index_srnga_orig.txt index_srnga.txt
7 cases written to index_srnga.txt

----------------------------------------
# construct index_megha.js, and check for internal consistencies

python make_js_index.py index_megha.txt index_megha.js
29 Success: Page records read from index_megha.txt
json data written to index_megha.js

----------------------------------------
# construct index_srnga.js, and check for internal consistencies

python make_js_index.py index_srnga.txt index_srnga.js
6 Success: Page records read from index_srnga.txt
json data written to index_srnga.js
c
----------------------------------------
 preliminary check of pwg links for megha
 5 Checks succeeded.  See readme_checks_megha.txt

----------------------------------------
'ready for repo' message in https://github.com/sanskrit-lexicon/PWG/issues/147
----------------------------------------
app construction.
2 apps are needed:  see readme_app.txt
app1 -- (sarga,shloka)
app0 -- VNNN  

----------------------------------------
modify basicadjust.php for pwg, pw, pwkvn, sch, mw
see readme_websanlexicon.txt

----------------------------------------
typo pw.txt (csl-orig)  TODO <<<<<<<<<<<<<<<<<
(temp_pw.txt changed)
typos
17813 : ucCilIDra : ucCilIDra : ucCilIMDra : typo, pw
17814 : ucCilIDra : ucCilIDra : ucCilIMDra : typo, pw
74866 : prekzaRa : MEGH. 7 : MEGH. 79 : typo, pw

6657 : aSruleSa : MEGH. 103 : MEGH. 105  : printchange, pwkvn
206657 : aSruleSa : MEGH. 103 : MEGH. 105 : printchange, pw
5905 : aSruleSa : Megh. 103 : Megh. 105 : printchange, sch
24104 : ADAna : Megh. iii : Megh. 3  : printchange, mw
60535 : nIcEs : MEGH. 42 : MEGH. 43  : printchange, pw  (cf. pwg)
62448 : pat : MEGH. 28 : MEGH. 29  : printchange, pw  (cf. pwg)
8670  : uc  : MEGH. 93 : MEGH. 94  : printchange, pwkvn
208670  : uc  : MEGH. 93 : MEGH. 94  : printchange, pw
7869   : uc  : MEGH. 93 : MEGH. 94  : printchange, sch

cp temp_pw.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cp temp_pwkvn.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt
cp temp_mw.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cp temp_sch.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt

----------------------------------------
checks of links from dictionaries
see readme_checks.txt

sync to github:  csl-websanlexicon, csl-apidev.
csl-orig  (pwg, pw, mw)  csl-corrections (print change)
pull github to cologne server
regenerate displays for pwg, pw, pwkvn, sch, mw
=============================================================
THE END

diff temp_pw.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt | wc -l
diff temp_pw.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt | wc -l
diff temp_pwkvn.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt | wc -l
diff temp_mw.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt | wc -l
diff temp_sch.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt | wc -l
