issue75/readme.txt
03-27-2025 begun ejf



Ref: https://github.com/sanskrit-lexicon/PWG/issues/75

This issue75 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue75

-----------------
pdf: 'BHAGAVADGĪTĀ (1823) SCHLEGEL.pdf'

/e/pdfwork/bhagavadgita_shlegel/'BHAGAVADGĪTĀ (1823) SCHLEGEL.pdf'

-----------------
Index file
  
  index śak..xlsx
  Hemacandra.Anekarthasangraha.1807.xlsx
  convert to tsv (Google) BHAGAVADGITA.1823.SCHLEGEL.txt
  # 
  cp BHAGAVADGITA.1823.SCHLEGEL.txt index.txt

---------------------
see readme_prakshipta.txt  "What is the prakshipta of the Ramayana?"
---------------------
index_txt format observations for
 Ramayana.Bomb.-Vol.I-Index.1.1.txt and
 Ramayana.Bomb.-Vol.III-Index.txt
 
format 7+ fields tab-separated values
vol.
page
kāṇḍa
sarga
from v.
to v.
ipage

Further fields are remarks
remark(s)

----------------------------------------
# Begin checking consistency with dictionaries
# get temporary local copy of pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt

see readme_check_prakshipta.txt


--------------------
--  NOT DONE
# Prepare index.js
python make_js_index.py index.txt index.js
88 Success: Page records read from index.txt
json data written to index.js


----------------------------------------
Make misc checks between pwg , the pdf and index

'pwg':r'<ls>BHAG. ([0-9]+),([0-9]+)  (adhyAya, shloka)
python generate_random.py 5 pwg temp_pwg.txt index.txt check0_pwg.txt
found 2120 instances in kosha
found 656 distinct in kosha
5 written to check0_pwg.txt

All cases OK

-----------------------------
# get temporary local copy of mw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt

116 matches for "<ls>Bhag\. " in buffer: temp_mw.txt
108 matches for "<ls>Bhag\. [ivx]+, *[0-9]+" in buffer: temp_mw.txt

'mw':r'<ls>BHag. ([ivx]+), *([0-9]+)  (adhyAya, shloka)
python generate_random.py 5 mw temp_mw.txt index.txt check0_mw.txt
found 108 instances in kosha
5 written to check0_mw.txt

4 found, one NOT FOUND

Since one not found, check another batch
python generate_random.py 5 mw temp_mw.txt index.txt check0_mw_a.txt


----------------------------------------
Ready for bhagavadgita repo
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
start



edit check0_pwg.txt and manually check comparison
All in this random sample checked.


----------------------------------
# get temporary local copy of pw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt

63 matches for "<ls>BHAG. [0-9]+,[0-9]+" in buffer: temp_pw.txt
83 matches for "<ls>BHAG. [0-9]+[^0-9,]" in buffer: temp_pw.txt

Random check of links:

# Variant 1
'pw1':r'<ls>BHAG. ([0-9]+)[^,])  (verse,)

python generate_random.py 5 pw1 temp_pw.txt index.txt check_pw1.txt

One NOT FOUND
<ls>BHAG. 20</ls>
key (20,): 27	1	18	20	10
L= 72764, hw= pramARADika, pc=4-164-a

# Variant 2
'pw2':r'<ls>BHAG. ([0-9]+),([0-9]+)  (ipage,linenum)
python generate_random.py 5 pw2 temp_pw.txt index.txt check_pw2.txt

All checks ok.

----------------------------------------
# get temporary local copy of pwkvn.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn.txt

8 matches for "<ls>BHAG. [0-9]+[^0-9,]" in buffer: temp_pwkvn.txt
3 matches for "<ls>BHAG. [0-9]+,[0-9]+" in buffer: temp_pwkvn.txt


Random check of links:

# Variant 1
'pwkvn1':r'<ls>BHAG. ([0-9]+)[^,])  (verse,)

python generate_random.py 5 pwkvn1 temp_pwkvn.txt index.txt check_pwkvn1.txt

All are ok -- two are 'variant readings'

# Variant 2
'pwkvn2':r'<ls>BHAG. ([0-9]+),([0-9]+)  (ipage,linenum)
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

