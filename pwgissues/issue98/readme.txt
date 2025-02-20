issue98/readme.txt
02-19-2025 begun ejf
YĀJÑ.	YĀJÑAVALKYA'S Gesetzbuch.

Ref: https://github.com/sanskrit-lexicon/PWG/issues/98

This issue98 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue98

याज्ञवल्क्यधर्मशास्त्रम् 
pdf: Yajnavalkya_s_Gesetzbuch.pdf
https://en.wikipedia.org/wiki/Yajnavalkya#Scriptural_references
where the work is named Yajnavalkya Smriti

-----------------
yajn_index_v1.txt  (
format observations:
format 4 fields tab-separated values
page
adhyaya
from_verse
to_verse

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

