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
---- 1. volume colume
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


========================================
----------------------------------------
The preferred column separator is 'tab' (tab-separated-values).
  Indische_Spr_v1_Index.txt uses spaces.
  Change to tabs
# save the 'space' version under another name
cp Indische_Spr_v1_Index.txt Indische_Spr_v1_Index_space.txt
# manually edit Indische_Spr_v1_Index.txt and change '  +' to '\t' (TAB)
# revise make_js_index.py to use tab-separator
#
cp index_1.js temp_index_1_space.js

# remake index_1.js
python make_js_index.py I Indische_Spr_v1_Index.txt index_1.js
# expect no change in index_1.js
diff temp_index_1_space.js index_1.js | wc -l
0  # no difference, as expected
rm temp_index_1_space.js  # discard temporary file

----------------------------------------------
Volume 3 index file = IndischeSprueche_Vol3_index.txt
# This is a tsv file.
# Problem:  many extra columns!
# Solution: manual edit. Remove tabs at end of lines

-------
# make index_3.js
python make_js_index.py III IndischeSprueche_Vol3_index.txt index_3.js
Skipping column title line: volume      page    from v.         to v.   ipage

356 Success: Page records read from IndischeSprueche_Vol3_index.txt
json data written to index_3.js
check1 finds 0 errors

Good so far.

vol 3 has verses 3360 - 5419
# Generate a few random instances from pwg for detail checking

# get temporary local copy of pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt
 (commit 9dfc1998a78962ef82cec37184024e01353351b7 in csl-orig)
   
# generate 10 examples for manual checking. write file temp.txt
python generate_random.py 10 temp_pwg_0.txt III IndischeSprueche_Vol3_index.txt temp_check_3.txt

# make readme file for the checks
cp temp_check_3.txt readme_checkindex_vol3.txt
# manually check the examples -  edit readme_checkindex_vol3.txt
#  use the pdf in checking
# Results of check:
  All ok with index.

----------------------------
In course of the check, two pwg.txt typos noticed:
  L=76434 "Danda" (धन्द॒) -> Danada धनद  typo 
  L=76435  Dandeva -> Danadeva
  (Ref: https://github.com/sanskrit-lexicon/csl-orig/issues/1775)

install the corrections Danda, Dandeva into csl-orig
cp temp_pwg_0.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt

cd /c/xampp/htdocs/cologne/csl-orig
git pull
git add v02/pwg/pwg.txt
git commit -m "PWG Danda, Dandeva. #1775"
git push

Also update csl-orig and pwg displays at Cologne

# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue98

----------------------------
check index for volume 2
Indische_Spr_v2_Index.txt
  Ref: https://github.com/sanskrit-lexicon/PWG/issues/98#issuecomment-2659012762

The format of lines is space-separated values
Manually edit and change to tab-separated values
global regex replacement lines: "  +" -> \t

# make index_2.js
python make_js_index.py II Indische_Spr_v2_Index.txt  index_2.js

322 Success: Page records read from Indische_Spr_v2_Index.txt
json data written to index_2.js

# get temp copy of pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt

# generate 10 examples for manual checking of v2 index. write file temp.txt
python generate_random.py 10 temp_pwg.txt II Indische_Spr_v2_Index.txt temp_check_2.txt

# make readme file for the checks
cp temp_check_2.txt readme_checkindex_vol2.txt
# manually check the examples -  edit readme_checkindex_vol2.txt
#  use the volume 2 pdf in checking
# Results of check:
  All ok with index.

rm temp_pwg.txt

----------------------------
