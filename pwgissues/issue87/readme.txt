issue87/readme.txt
02-05-2025 begun ejf
Indische SprÃ¼che 1st ed. link target

Ref: https://github.com/sanskrit-lexicon/PWG/issues/87

This issue87 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue87


https://github.com/sanskrit-lexicon/PWG/issues/87#issue-2820409982
link to 3 pdfs  (volumes 1-3).

Indische_Spr_v1_Index.txt
  Ref: https://github.com/sanskrit-lexicon/PWG/issues/87#issuecomment-2628934230

Check Indische_Spr_v1_Index.txt for 10 random verses.
No problems noticed !

See readme_checkindex_vol1.txt for details

Note:  the 'column separator' in v1_Index is [ ]+  (one or more spaces).

-----------------------
02-06-2025
make_js_index.py makes index into a javascript module.
It does several validity checks.
This program will be part of the 'app1' in the sanskrit-lexicon-scans
repo for this link source.

------
# apply the program to the index for volume I
python make_js_index.py I Indische_Spr_v1_Index.txt index_1.js
output:
Skipping column title line: volume      page    from v. to v.   ipage
305 Success: Page records read from Indische_Spr_v1_Index.txt
json data written to temp.txt
check1 finds 0 errors
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
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue87

----------------------------
