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
# There are two modes of reference in pwg:
#  verse
#  linenum,ipage

# nparm = 1
python generate_random.py 10 1 temp_pwg.txt sahd_index_v1.txt temp_check_v1_1parm.txt
cp temp_check_v1_1parm.txt readme_checkindex_v1_1parm.txt

All checks succeed.

# nparm = 2
python generate_random.py 10 2 temp_pwg.txt sahd_index_v1.txt temp_check_v1_2parm.txt
cp temp_check_v1_2parm.txt readme_checkindex_v1_2parm.txt

All checks succeed.

Ready for repo.

Use repo name sahityadarpana


=================================================
mw <ls>Sāh. [0-9]    Not sure how to interpret

29 matches for "<ls>Sāh. [0-9]" in buffer: mw.txt
 page?
M
? mw    <L>24354<pc>139,3<k1>Ananda      <ls>Sāh. 399</ls>
? mw    <L>46857<pc>266,1<k1>kazwArTatva <ls>Sāh. 227, 18.</ls>
   only one other like 46857

================================================
03-07-2025  References by MW use a different pdf
150 matches for "<ls>Sāh. [ivx]+, *[0-9]+" in buffer: mw.txt
 (pariccheda, kārikā) mode of referencing, in MW
 Sah_D_Index-v3_MW.txt  from Andhrabharati

2015.495375.Sahithya-Darpana.pdf
Ref: https://archive.org/details/in.ernet.dli.2015.495375/page/n7/mode/2up
Ref: https://github.com/sanskrit-lexicon/PWG/issues/101

<ls>Sāh. 

see readme_examples_v3_pk.txt
With one exception, (guRIBAva vii,25)
the MW headword IS FOUND 'near' the ls reference.

================================================
03-11-2025
A new pdf for mw references:
https://archive.org/details/PWtu_sahitya-darpan-by-vishvanath-kaviraj-with-commentary-of-ramchandra-tarkavagish-b/page/n3/mode/2up


---------------
temporary copy of mw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt

---------------
preliminary check of mw against this pdf


regex: <ls>Sāh. [ixvclm]+, *[0-9]+\.?</ls>
83 matches for "<ls>Sāh. [ixvclm]+, *[0-9]+\.?</ls>" in buffer: temp_mw.txt
150 matches for "<ls>Sāh. [ixvclm]+, *[0-9]+" in buffer: temp_mw.txt

