issue93/nala/readme.txt
03-01-2025 begun ejf

03446	N.	NALOPĀKHYĀNA in BÖHTLINGK'S Chrestomathi

Ref: https://github.com/sanskrit-lexicon/PWG/issues/93

This issue93 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93

index.txt BÖHTLINGK'S Chrestomathi
pdf: Chrestomathie 1st ed. 1845.pdf
/e/pdfwork/chr1/Chrestomathie 1st ed. 1845.pdf

-----------------------------

format observations:
format 5 fields tab-separated values
page	adhy.	from v.	to v.	ipage
19	1	1	8	1

page
adhyaya
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
Skipping column title line: page        adhy.   from v. to v.   ipage

103 Success: Page records read from index.txt
json data written to index.js
pagerecs passes check1_adhy
check1 finds no problems


-----------------------------
# Generate a few random instances from pwg for detail checking
python generate_random.py 10 ../temp_pwg.txt index.txt temp_check.txt
103 Success: Page records read from index.txt
1132566 lines read from ../temp_pwg.txt
123366 entries found
regex_raw = <ls>N. ([1-3]),([0-9]+)
found 283 instances adhy,verse in kosha
found 87 distinct adhy,verse in kosha
10 examples found
10 written to temp_check.txt


cp temp_check.txt readme_checkindex.txt

pdf: Chrestomathie 1st ed. 1845.pdf
/e/pdfwork/chr1/Chrestomathie 1st ed. 1845.pdf

All checks passed. Ready

