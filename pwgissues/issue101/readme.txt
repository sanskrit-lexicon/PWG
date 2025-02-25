issue101/readme.txt
02-25-2025 begun ejf
SĀH. D. SĀHITYADARPAṆA

Ref: https://github.com/sanskrit-lexicon/PWG/issues/101

This issue101 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue101

pdf: 'Sahitya Darpana Visvanatha Translation James Ballantyne R. Asiatic Society 1851.pdf'

https://en.wikipedia.org/wiki/Viswanatha_Kaviraja

-----------------

sahd_index.txt
 # Note: renamed and reformatted from Sah_D_Index.xlsx
comment from @Azanuka2412
  "typo with numbers of shlokas - after 742 shloka comes 744"
comment from pwgbib_input.txt :
1.267	SĀH. D.	Sāh. D.	SĀH. D. = SĀHITYADARPAṆA, auf den 10 ersten Bogen nach der Ausgabe&#13;&#10;von 1828 (GILD. Bibl. 264), auf den folgenden Bogen, wenn nicht&#13;&#10;die Yahreszahl 1828 ausdrücklich bemerkt wird, nach der Ausgabe&#13;&#10;von RÖER in der Bibliotheca indica. Eine einfache Zahl verweist auf&#13;&#10;die Kārikā, eine doppelte auf Seite und Zeile.

pwgbib_input.txt For "SĀH. D.":
"On the first 10 sheets according to the edition of 1828 (GILD. Bibl. 264), on the following sheets, unless the year number 1828 is expressly noted, according to the edition of RÖER in the Bibliotheca indica. A single number refers to the Kārikā, a double number to the page and line."


format observations of sahd_index.txt.
format 5 fields tab-separated values
page	adhy.	from v.	to v.	ipage
128	1	1	2	1
133	1	3	3	6

page
adhyaya
from_verse
to_verse
internal page number

make_js_index.py makes index into a javascript module.
It does several validity checks.
This program will be part of the 'app1' in the sanskrit-lexicon-scans
repo for this link source.
------
# apply the program to the index 
python make_js_index.py sahd_index.txt index.js

line 93 change:
old: 225	3	248c	249	98
old: 225	3	248b	249	98

line 192 change:
old: 334       6       559a    559a    207
new: 334       6       559    559a    207

----------------------------------------
# insert missing pages into index
python index_version1.py sahd_index.txt sahd_index_v1.txt

python make_js_index.py sahd_index_v1.txt index_v1.js

128 first page
470 = last page

(- 470 128) 342

(- 343 1)  342
----------------------------------------
# get temporary local copy of pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt

# Generate a few random instances from pwg for detail checking
python generate_random.py 10 temp_pwg.txt I sahd_index_v1a.txt temp_check_1.txt
cp temp_check_1.txt readme_checkindex_1.txt
Checking this against Sahdavalkya_s_Gesetzbuch.pdf
___ found problems ___




----------------------------------------
Checking sahd_index_v1_edit.txt against
   yjnavalkyasgese00yjgoog.pdf

python make_js_index.py I sahd_index_v1_edit.txt index_1.js
115 Success: Page records read from sahd_index_v1_edit.txt
json data written to index_1.js
pagerecs passes check1_adhy
check1 finds no problems

python generate_random.py 10 temp_pwg.txt I sahd_index_v1_edit.txt temp_check_1.txt

cp temp_check_1.txt readme_check_index_v1_edit.txt

manually edit readme_check_index_v1_edit.txt
for consistency of
  sahd_index_v1_edit.txt
  yjnavalkyasgese00yjgoog.pdf

ALL IS WELL!

