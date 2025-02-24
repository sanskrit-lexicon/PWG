issue100/readme.txt
02-24-2025 begun dkp
RAGH. 	RAGHUVAṂŚA, ed. STENZLER (GILD. Bibl. 13)

Ref: https://github.com/sanskrit-lexicon/PWG/issues/100

This issue100 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue100

रघुवंशम्
pdf: Ragh.pdf

-----------------
ragh_index_v1.txt  (
format observations:
format 5 fields tab-separated values
volume
page
adhyaya
from_verse
to_verse
ipage

-----------------
cp yajn_index_v1.txt  yajn_index_v1_edit.txt
# some adjustments to yajn_index_v1_edit.txt
There were two observations by the indexer @grigoriyt1.
Page 53 (book page) has oblique scan. It is not harming the text.
Page 93 (book page) has numbering error. It ends at 87, but erroneously marked 89 in book. Kept 87.

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
python generate_random.py 10 temp_pwg.txt I ragh_index_v1_edit.txt temp_check_1.txt
cp temp_check_1.txt readme_checkindex_1.txt
Checking this against Yajnavalkya_s_Gesetzbuch.pdf
___ found NO problems ___




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

