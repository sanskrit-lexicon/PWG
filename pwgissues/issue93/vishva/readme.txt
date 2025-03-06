issue93/vishva/readme.txt
03-01-2025 begun ejf


VIŚV.	VIŚVĀMITRA'S Kampf   sarga,verse
Ref: https://github.com/sanskrit-lexicon/PWG/issues/93
 Kampf = battle
This issue93 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93

index.txt BÖHTLINGK'S Chrestomathi
pdf: Chrestomathie 1st ed. 1845.pdf
/e/pdfwork/chr1/Chrestomathie 1st ed. 1845.pdf

-----------------------------

format 5 fields tab-separated values
page	sarga	from v.	to v.	ipage
99	1	1	9	81

page
sarga   --- for convenience, this referred to as adhy (aDyAya)
from_verse
to_verse
ipage

Note: no 'a,b', etc.

-----------------------------
make_js_index.py makes index into a javascript module.
It does several validity checks.
This program will be part of the 'app4' in the sanskrit-lexicon-scans
repo for this link source.


# apply the program to the index
python make_js_index.py index.txt index.js

Skipping column title line: page        sarga   from v. to v.   ipage

45 Success: Page records read from index.txt
json data written to index.js
pagerecs passes check1_adhy
check1 finds no problems

-----------------------------
# Generate a few random instances from pwg for detail checking
python generate_random.py 10 ../temp_pwg.txt index.txt temp_check.txt

Skipping column title line: page        sarga   from v. to v.   ipage

45 Success: Page records read from index.txt
1132566 lines read from ../temp_pwg.txt
123366 entries found
regex_raw = <ls>VIŚV. ([0-9]+),([0-9]+)
found 326 instances adhy,verse in kosha
found 200 distinct adhy,verse in kosha
10 examples found
10 written to temp_check.txt
---

cp temp_check.txt readme_checkindex.txt

pdf: Chrestomathie 1st ed. 1845.pdf
/e/pdfwork/chr1/Chrestomathie 1st ed. 1845.pdf

All checks passed. Ready
