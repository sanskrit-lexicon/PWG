issue123/readme.txt
03-14-2025 begun ejf
ANEKĀRTHASAM̃GRAHA

09781 : H. an. [HEMACANDRA'S ANEKĀRTHASAM̃GRAHA] 1807 Calc. ed. : pp. 226-365 (pdf pages)

Ref: https://github.com/sanskrit-lexicon/PWG/issues/123

This issue123 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue123

-----------------
pdf:
/e/pdfwork/Hemacandra Anekarthasangraha (1807).pdf


----------------------------------------
Selected pages from the pdf.
Bayerische StaatsBibliothek

Organization NOT UNDERSTOOD by Jim!

Calc. ed. : pp. 226-365 (pdf pages)  
----------------------------------------
Index file
  Hemacandra.Anekarthasangraha.1807.xlsx
  convert to tsv (Google) (rename index_orig.txt)
  cp index_orig.txt index_kanda.txt  

(Note:  See later for index.txt  

---------------------
index_kanda.txt format observations
format 6 fields tab-separated values
page
kanda
adhy
fromv
tov
ipage

sample:
page	kanda	adhy.	from v.	to v.	ipage
106	1	1	1	9a	1
107	1	1	9b	22a	2

Notes:
kanda is 1 or 2
 kanda = 1: page 106 - 225, adhy 1-6 ipage 1-120
 kanda = 2: page 226 - 365, adhy 1-7 ipage 1-140
 
---------------------
changes to index_kanda.txt
---- change 1
old
129	1	2	195b	208a	24
130	1	2	209b	221a	25
new
129	1	2	195b	208a	24
130	1	2	208b	221a	25


----------------------------------------
# Prepare index_kanda.js
python make_js_index_kanda.py index_kanda.txt index_kanda.js

----------------------------------------
# get temporary local copy of pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt

3153 matches in 3152 lines for "<ls>H. an. " in buffer: temp_pwg.txt

6610 matches in 6604 lines for "<ls>H. an.</ls>" in buffer: temp_pwg.txt

3143 matches in 3142 lines for "<ls>H. an. [1-7],[0-9]+" in buffer: temp_pwg.txt

----------------------------------------
Make misc checks between pwg , the pdf and index_kanda

"Calc. ed. : pp. 226-365 (pdf pages)"
 conjecture: all the 3153 references ref to kanda = 2

<L>16265<pc>2-0211<k1>kAdambara
<ls>H. an. 4,248.</ls>
349	2	4	245b	259a	124

provisional conclusion:  all references '<Ls>H. an. a,v</ls>
 match requires kanda = 2.
 kanda = 1 NOT used.


========================================
index.txt
1. remove kanda field
2. include only when kanda = 2
python make_index.py index_kanda.txt index.txt
146 cases written to index.txt

page	adhy.	from v.	to v.	ipage
226	1	1	9a	1
227	1	9b	16	2

----------------------------------------
index.js
python make_js_index.py index.txt index.js

145 Success: Page records read from index.txt
json data written to index.js
pagerecs passes check1_adhy
check1 finds no problems


----------------------------------------
Make misc checks between pwg , the pdf and index

python generate_random.py 10 pwg temp_pwg.txt index.txt check_pwg.txt

edit check_pwg.txt and manually check comparison
All in this random sample checked.

----------------------------------
# get temporary local copy of pw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt

69 matches for "<ls>H. an. " in buffer: temp_pw.txt

Random check of links:

python generate_random.py 5 pw temp_pw.txt index.txt check_pw.txt

Links check for pw

----------------------------------------
# get temporary local copy of pwkvn.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn.txt

11 matches for "<ls>H. an. " in buffer: temp_pwkvn.txt

Random check of links:

python generate_random.py 5 pwkvn temp_pwkvn.txt index.txt check_pwkvn.txt

Links check for pwkvn

----------------------------------------
# get temporary local copy of sch.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch.txt

11 matches for "<ls>H. an. " in buffer: temp_sch.txt

Random check of links: 
python generate_random.py 5 sch temp_sch.txt index.txt check_sch.txt

Links check for sch

----------------------------------------
# get temporary local copy of mw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt

No references to this work in mw !
Ref: c:/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwauth/

==========================================
index checks complete.  All is GO!

Ready for sanskrit-lexicon-scans
