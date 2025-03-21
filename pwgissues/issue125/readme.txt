issue125/readme.txt
03-19-2025 begun ejf
05500 ŚĀK. ŚĀKUNTALA


Ref: https://github.com/sanskrit-lexicon/PWG/issues/125

This issue125 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue125

-----------------
pdf:
/e/pdfwork/shakuntala/ŚĀK.pdf
Index file
  index śak..xlsx
  Hemacandra.Anekarthasangraha.1807.xlsx
  convert to tsv (Google) (rename index_orig.txt)
 
---------------------
index_orig.txt format observations
format 5 fields tab-separated values
page
adhy
fromv
tov
ipage
--------------------
'---' notation  non-standard
cp index_orig.txt index_v1.txt
# manual changes to index_v1.txt
-----

page 18 is a title page, page 19 is a blank page
Remove these two pages.
Use adhy. 0 for the prastAva
OLD:
pdf p.	adh.	from v.	to v.	i. p.
18	---	---	---	1
19	---	---	---	2
20	prastavana	1	2	3
21	prastvana	3	5	4

NEW:
pdf p.	adh.	from v.	to v.	i. p.
20	0	1	2	3
21	0	3	5	4


---------------------------------
32 matches in 16 lines for "---" in buffer: index_v1.txt

These 16 lines have fromv and tov '---'
# change these as in this example.
Use of 'c' is arbitrary.
OLD:
29	1	23	24	12
30	1	---	---	13
31	1	---	---	14
NEW:
29	1	23	24	12
30	1	24c	24c	13
31	1	24c	24c	14

# do these changes with a program
python make_index.py index_v1.txt index.txt


----------------------------------------
changes to index.txt based on make_js_index.py
--- 1. change to-verse
OLD:
42	2	40	41	25
NEW:
42	2	40	42	25
--- 2. change from-verse
OLD:
54	3	64	65	37
NEW:
54	3	63	65	37

------------------
page 130 सप्तमः अङ्कः   end of 7th chapter
page 131 blank
page 132 अथ प्राकृतभाषाव्याख्या  (Bohtlingk's notes begin

Delete last two lines of index.txt
131	7	194c	194c	114
132	7	194c	194c	115

-----------------------------------
page 112  end of षष्ठः अङ्कः

------------------
# Prepare index.js
# Note that the verses are continuous through all adhyAyas.
python make_js_index.py index.txt index.js

----------------------------------------
# Begin checking consistency with dictionaries
# get temporary local copy of pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt

# all instances of ŚĀK. with 1 or more parameters
5177 matches in 5152 lines for "<ls>ŚĀK. " in buffer: temp_pwg.txt

#  ŚĀK. ipage,line-offset
2326 matches in 2318 lines for "<ls>ŚĀK. [0-9]+,[0-9]+"

#  ŚĀK. 
2326 matches in 2257 lines for "<ls>ŚĀK. [0-9]+[.<]"

259 matches for "<ls>ŚĀK. C[hH]\. [0-9]+,[0-9]+" 
  ŚĀK. CH. = CHEZY'S Ausgabe des ŚĀKUNTALA (GILD. Bibl. 187).
  This is another version! 

Many variations!

page 

----------------------------------------
Make misc checks between pwg , the pdf and index

# Variant 1
'pwg1':r'<ls>ŚĀK. ([0-9]+)[^,])  (verse,)
python generate_random.py 10 pwg1 temp_pwg.txt index.txt check_pwg1.txt

edit check_pwg.txt and manually check comparison
Two were NOT FOUND:
<ls>ŚĀK. 78.</ls>
key (78,): 63	4	77	78	46
L= 116165, hw= hariRa, pc=7-1547
---
<ls>ŚĀK. 191.</ls>
key (191,): 128	7	191	192a	111
L= 113928, hw= sTA, pc=7-1285

# Variant 2
'pwg2':r'<ls>ŚĀK. ([0-9]+),([0-9]+)  (ipage,linenum)
python generate_random.py 10 pwg2 temp_pwg.txt index.txt check_pwg2.txt

edit check_pwg.txt and manually check comparison
All in this random sample checked.


----------------------------------
# get temporary local copy of pw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt

63 matches for "<ls>ŚĀK. [0-9]+,[0-9]+" in buffer: temp_pw.txt
83 matches for "<ls>ŚĀK. [0-9]+[^0-9,]" in buffer: temp_pw.txt

Random check of links:

# Variant 1
'pw1':r'<ls>ŚĀK. ([0-9]+)[^,])  (verse,)

python generate_random.py 5 pw1 temp_pw.txt index.txt check_pw1.txt

One NOT FOUND
<ls>ŚĀK. 20</ls>
key (20,): 27	1	18	20	10
L= 72764, hw= pramARADika, pc=4-164-a

# Variant 2
'pw2':r'<ls>ŚĀK. ([0-9]+),([0-9]+)  (ipage,linenum)
python generate_random.py 5 pw2 temp_pw.txt index.txt check_pw2.txt

All checks ok.

----------------------------------------
# get temporary local copy of pwkvn.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn.txt

8 matches for "<ls>ŚĀK. [0-9]+[^0-9,]" in buffer: temp_pwkvn.txt
3 matches for "<ls>ŚĀK. [0-9]+,[0-9]+" in buffer: temp_pwkvn.txt


Random check of links:

# Variant 1
'pwkvn1':r'<ls>ŚĀK. ([0-9]+)[^,])  (verse,)

python generate_random.py 5 pwkvn1 temp_pwkvn.txt index.txt check_pwkvn1.txt

All are ok -- two are 'variant readings'

# Variant 2
'pwkvn2':r'<ls>ŚĀK. ([0-9]+),([0-9]+)  (ipage,linenum)
python generate_random.py 5 pwkvn2 temp_pwkvn.txt index.txt check_pwkvn2.txt

only 3 examples
All are ok

----------------------------------------
# get temporary local copy of sch.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch.txt

17 matches for "<ls>Śāk. " in buffer: temp_sch.txt
2 matches for "<ls>Śāk. [0-9]+,[0-9]+" in buffer: temp_sch.txt
8 matches for "<ls>Śāk. [0-9]+[^0-9,]" in buffer: temp_sch.txt

Random check of links:

# Variant 1
'sch1':r'<ls>Śāk. ([0-9]+)[^,])  (verse,)

python generate_random.py 5 sch1 temp_sch.txt index.txt check_sch1.txt

2 variant readings
1 NOT FOUND. also a variant reading
<ls>Śāk. 84</ls> v.l.
key (84,): 69	4	84	86	52
L= 6244, hw= asikta, pc=086-1  


# Variant 2
'sch2':r'<ls>Śāk. ([0-9]+),([0-9]+)  (ipage,linenum)
python generate_random.py 5 sch2 temp_sch.txt index.txt check_sch2.txt

Only 2 examples, both OK

----------------------------------------
# get temporary local copy of mw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt

no matches for "<ls>Śāk."

285 matches for "<ls>Śak. " in buffer: temp_mw.txt

32 matches for "<ls>Śak. [0-9]+[^0-9,]" in buffer: temp_mw.txt

30 matches for "<ls>Śak. [0-9]+, [0-9]+" in buffer: temp_mw.txt

207 matches for "<ls>Śak. [iv]+" in buffer: temp_mw.txt

194 matches for "<ls>Śak. \(i\|ii\|iii\|iv\|v\|vi\|vii\), [0-9]" in buffer: temp_mw.txt

The 'verse' numbers restart at new shloka

index question:  

# Variant 1
'mw1':r'<ls>Śak. ([0-9]+)[^,])  (verse,)

python generate_random.py 5 mw1 temp_mw.txt index.txt check_mw1.txt

NOT FOUND  ALL!   ---

# Variant 2
'mw2':r'<ls>Śāk. ([0-9]+), *([0-9]+)  (ipage,linenum)
python generate_random.py 5 mw2 temp_mw.txt index.txt check_mw2.txt

NOT FOUND ALL!

i\|ii\|iii\|iv\|v\|vi\|vii

<L>68445<pc>370,3<k1>graTita  <ls>Śak. i, 1/2</ls>

==========================================
index checks complete.  All is GO for pwg, pw, pwkvn, sch.
Ready for sanskrit-lexicon-scans

==========================================
MW requires different index --- probably can use same pdf

See lsmw/readme_mw.txt 
==========================================
Beginning apps in sanskrit-lexicon-scans

https://github.com/sanskrit-lexicon-scans/shakuntala
# initialize local repo, where the link target apps will be installed.
cd /c/xampp/htdocs/sanskrit-lexicon-scans/
git clone git@github.com:sanskrit-lexicon-scans/shakuntala.git

# edit README.md 

# Install app1 as target for Variant 1 
see readme_app1.txt

# Install app2 as target for Variant 2
see readme_app2.txt

--- links to shakuntala app1 and app2 for
pwg, pw, pwkv, sch.
see readme_csl-websanlexicon.txt


-------------------------------------
# sync to github
sync csl-websanlexicon
sync csl-apidev
# sync to cologne
 # regenerate displays for pwg, pw, pwkvn, sch, [mw not required]
-------------------------------------
# sync this repo to github
====================================
THE END

