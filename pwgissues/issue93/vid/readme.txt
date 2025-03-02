issue93/vid/readme.txt
03-01-2025 begun ejf

01127   VID.	Geschichte des VIDŪṢAKA in BÖHTLINGK'S
Ref: https://github.com/sanskrit-lexicon/PWG/issues/93

Geschichte des = story of 

pdf: Chrestomathie 1st ed. 1845.pdf
/e/pdfwork/chr1/Chrestomathie 1st ed. 1845.pdf

-----------------------------

format 5 fields tab-separated values
page	from v.	to v.	ipage
232	1	9	214

page
from_verse
to_verse
ipage

Note: no 'a,b', etc.

-----------------------------
make_js_index.py makes index into a javascript module.
It does several validity checks.
This program will be part of the 'app1' in the sanskrit-lexicon-scans
repo for this link source.


# apply the program to the index
python make_js_index.py index.txt index.js

Skipping column title line: page        from v. to v.   ipage

29 Success: Page records read from index.txt
json data written to index.js
check1 finds no problems

-----------------------------
# Generate a few random instances from pwg for detail checking
python generate_random.py 10 ../temp_pwg.txt index.txt temp_check.txt
1132566 lines read from ../temp_pwg.txt
123366 entries found
regex_raw = <ls>VID. ([0-9]+)
found 1109 instances verse in kosha
found 325 distinct verse in kosha
10 examples found
10 written to temp_check.txt

cp temp_check.txt readme_checkindex.txt

pdf: Chrestomathie 1st ed. 1845.pdf
/e/pdfwork/chr1/Chrestomathie 1st ed. 1845.pdf

All checks passed. Ready


-----------------------------
-----------------------------
-----------------------------
-----------------------------
-----------------------------


===============================================
old notes re yajnavalkya

-----------------
cp yajn_index_v1.txt  yajn_index_v1_edit.txt
# some adjustments to yajn_index_v1_edit.txt
---- 1. volume column
By the file name, apparently there is more than 1 volume.
Insert 'volume' column into ('I') into yajn_index_v1_edit.txt

---- 2. subtract 3 from page. result yajn_index_v1a.txt
For some reason, the page values in index are 3 too great,
when compared to pdf.
python change_page.py yajn_index_v1_edit.txt yajn_index_v1a.txt
--------
make_js_index.py makes index into a javascript module.
It does several validity checks.
This program will be part of the 'app1' in the sanskrit-lexicon-scans
repo for this link source.

------

------
# apply the program to the index for volume I
python make_js_index.py I yajn_index_v1a.txt index_1.js


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

