issue92/readme.txt
03-06-2025 begun ejf
09176 VARĀH. BṚH. S. : VARĀHAMIHIRA'S BṚHATSAM̃HITĀ

Ref: https://github.com/sanskrit-lexicon/PWG/issues/92

This issue92 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue92

-----------------
pdf: Br.pdf
/e/pdfwork/brhatsamhita/Br.pdf

----------------------------------------
Index file
Brihatsamhita_v2.Index.xlsx
  convert to tsv (Google)
  rename index.txt  (save copy as index_orig.txt)
  remove comment at top
  remove and extra tabs at end of each line
Note comment at page 81
81	2	5b	6a	6		6 - нет ?
 нет = no   There is no verse 6 here !
 Also, pwg has no reference to this verse.
 


Brihatsamhita.Notes.docx   mentions some questions hard to understand

---------------------
format observations:
format 5 fields tab-separated values
page
adhy
fromv
tov
ipage

first lines of index
page	adhy.	fromv.	tov.	ipage
76	1	1	4	1
77	1	5	10a	2
78	1	10b	11	3

last lines of index
581	107	2	7a	506
582	107	7b	12	507
583	107	13	13	508

----------------------------------------
misc checks between pwg and Br.pdf
first verse:
+ <L>27412<pc>3-0095<k1>ji  <ls>VARĀH. BṚH. S. 1,1.</ls> (jayati — savitA) 
+ <L>71841<pc>5-1337<k1>kram   <ls>VARĀH. BṚH. S. 107,13.</ls>  (anukrAntam)

+ <L>41013<pc>4-0328<k1>nEzWika  <L>41013<pc>4-0328<k1>nEzWika
    {#kftsnANgopANgakuSalaM horAgaRitanEzWikam#}
----------------------------------------
page, ipage

8 - Bṛhatsam̃hitā of Varāhamihira, KERN, 1865
9 - blank
10 - Devanagari title page
11 - blank
12 1 preface Hindu astronomer and astrologer
...
75 64 end of preface
76 १  श्रीगणॅशाय नमः   <<< index starts here   upanayana (introduction)
--------------
------

# apply the program to the index
python make_js_index.py index.txt index.js

----------------------------------------
# get temporary local copy of pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt

# Generate a few random instances from pwg for detail checking
python generate_random.py 10 temp_pwg.txt I yajn_index_v1a.txt temp_check_1.txt
cp temp_check_1.txt readme_checkindex_1.txt
Checking this against Yajnavalkya_s_Gesetzbuch.pdf
___ found problems ___




----------------------------------------
Checking yajn_index_v1_edit.txt against
   yjnavalkyasgese00yjgoog.pdf

python make_js_index.py I yajn_index_v1_edit.txt index_1.js
115 Success: Page records read from yajn_index_v1_edit.txt
json data written to index_1.js
pagerecs passes check1_adhy
check1 finds no problems

python generate_random.py 10 temp_pwg.txt I yajn_index_v1_edit.txt temp_check_1.txt

cp temp_check_1.txt readme_check_index_v1_edit.txt

manually edit readme_check_index_v1_edit.txt
for consistency of
  yajn_index_v1_edit.txt
  yjnavalkyasgese00yjgoog.pdf

ALL IS WELL!

