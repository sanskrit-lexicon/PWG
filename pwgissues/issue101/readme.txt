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

================================================
03-24-2025
sahityadarpana app1 has been made.
Ref: https://github.com/sanskrit-lexicon-scans/sahityadarpana/tree/main/app1
# check pwg, pw, pwkvn, sch with both 1 and 2 parms
# index file: sahd_index_v1.txt
# pdf file  : "Sahitya Darpana Visvanatha Translation James Ballantyne R. Asiatic Society 1851.pdf"
https://sanskrit-lexicon-scans.github.io/sahityadarpana/app1/?V
https://sanskrit-lexicon-scans.github.io/sahityadarpana/app1/?P,L

cp ../issue125/generate_random.py generate_random1.py
# edit generate_random1.py  (modify get_dict_regex)

# check of pwg 1-parm
'pwg1':r'<ls>SĀH. D. ([0-9]+)[^0-9,]'    verse

python generate_random1.py 5 pwg1 temp_pwg.txt sahd_index_v1.txt check_pwg1.txt
found 1292 instances in kosha

OK!

# check of pwg 2-parm
'pwg1':r'<ls>SĀH. D. ([0-9]+),([0-9]+)'    page,line

python generate_random1.py 5 pwg2 temp_pwg.txt sahd_index_v1.txt check_pwg2.txt
found 2200 instances in kosha

OK!

# check of pw 1-parm
'pw1':r'<ls>SĀH. D. ([0-9]+)[^0-9,]'    verse
# get temporary local copy of pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt

python generate_random1.py 5 pw1 temp_pw.txt sahd_index_v1.txt check_pw1.txt
found 70 instances in kosha

OK!

# check of pw 2-parm
'pw2':r'<ls>SĀH. D. ([0-9]+),([0-9]+)'    page,line

python generate_random1.py 5 pw2 temp_pw.txt sahd_index_v1.txt check_pw2.txt
found 119 instances in kosha

OK!

# check of pwkvn 1-parm
'pwkvn1':r'<ls>SĀH. D. ([0-9]+)[^0-9,]'    verse
# get temporary local copy of pwkvng.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn.txt

python generate_random1.py 5 pwkvn1 temp_pwkvn.txt sahd_index_v1.txt check_pwkvn1.txt
found 14 instances in kosha

 1 questionable, 4 OK

# check of pwkvn 2-parm
'pwkvn2':r'<ls>SĀH. D. ([0-9]+),([0-9]+)'    page,line

python generate_random1.py 5 pwkvn2 temp_pwkvn.txt sahd_index_v1.txt check_pwkvn2.txt
found 21 instances in kosha

OK!

# check of sch 1-parm
'sch1':r'<ls>Sāh. D. ([0-9]+)[^0-9,]'    verse
# get temporary local copy of schg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch.txt

python generate_random1.py 5 sch1 temp_sch.txt sahd_index_v1.txt check_sch1.txt
found 15 instances in kosha

OK

# check of sch 2-parms
'sch2':r'<ls>Sāh. D. ([0-9]+),([0-9]+)'    ipage,line

python generate_random1.py 5 sch2 temp_sch.txt sahd_index_v1.txt check_sch2.txt
found 21 instances in kosha

OK

# check of mw 1-parm
'mw1':r'<ls>Sāh. ([0-9]+)[^0-9,]'    verse
# get temporary local copy of mw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt

python generate_random1.py 5 mw1 temp_mw.txt sahd_index_v1.txt check_mw1.txt
found 27 instances in kosha

OK

# check of mw 2-parms
'mw2':r'<ls>Sāh. ([0-9]+),([0-9]+)'    ipage,line

python generate_random1.py 5 mw2 temp_mw.txt sahd_index_v1.txt check_mw2.txt
found 2 instances in kosha

=================================================================
OK
# check of mw 2-parms,  first parm in roman.  Presume ipage,line?

150 matches for "<ls>Sāh. [ivxlcm]+, *[0-9]+" in buffer: mw.txt
 (pariccheda, kārikā) mode of referencing, in MW

----- This requires a different pdf and repo.

'mw3':r'<ls>Sāh. ([ivxlcm]+),([0-9]+)'    section,verse

and different Sah_D_Index-v4_MW.txt
# make index file for link target
# Sah_D_Index-v4_MW.txt has more information than is
# needed for the app index.
# make index_v4.txt of same form as sahd_index_v1.txt.
python make_index_v4.py Sah_D_Index-v4_MW.txt index_v4.txt

# construct index_v4.js
# the use of letters in fromv, tov is non-standard.
# But this is not important. Use a variant of make_js_index.py
# make_js_index_v4.py
python make_js_index_v4.py index_v4.txt index_v4.js

# generate random examples.  note minor change in
# gen__v4 program, to use make_js_index_v4.py
python generate_random1_v4.py 5 mwv4 temp_mw.txt index_v4.txt check_mwv4.txt
found 150 instances in kosha
4 written to check_mwv4.txt

3 ok, one NOT FOUND

# do another batch
python generate_random1_v4.py 8 mwv4 temp_mw.txt index_v4.txt check_mwv4_a.txt

8 written to check_mwv4_a.txt

6 ok, 2 NOT FOUND.

What to make of the occasional 'NOT FOUND' ?

================================================
03-25-2025  sahityadarpana_mw
see readme_app1_mw.txt for how the app1 was made.
================================================
repos updated, cologne updated.
THE END
