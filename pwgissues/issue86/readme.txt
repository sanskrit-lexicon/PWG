issue86/readme.txt
03-04-2025 begun ejf
08170	PAÑCAT.	PAÑCATANTRA. Pantschatantrum sive quinqu


Ref: https://github.com/sanskrit-lexicon/PWG/issues/86

This issue86 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue86

-----------------
pdf: pantschatantrums00kose.pdf  Kosegarten
This pdf is flawed (missing 2 pages)
See readme_pantschatantrums00kose.txt

-----------------
pdf: Pancatantra.1848.Kosegarten.pdf
  source https://github.com/sanskrit-lexicon/PWG/issues/86#issuecomment-2701596296
This source is pretty good, byt @grigoriyt1 decided to use another source

------------------
pdf: pancatantra.pdf
This is the one used in sanskrit-lexicon-scans/pantankose repository
ref: https://github.com/sanskrit-lexicon/PWG/issues/86#issuecomment-2760647446
 289 pages
source: https://www.digitale-sammlungen.de/en/view/bsb10219704
rights: https://rightsstatements.org/page/NoC-NC/1.0/

----------------------------------------
index:
index_panc.xlsx
  Ref: https://github.com/sanskrit-lexicon/PWG/issues/86#issuecomment-2760647446
index_panc.txt converted to text file, tab-separators
# copy to index.txt
  Some adjustments for typos and for purposes of app1
  See readme_index.txt  for details of changes.

-------------------------------------------
format
pdf p.	tantra	from V.	To V.	ipage
20	0	1	4	3
21	0	5	10	4
22	0	11	11	5
23	I	1	8a	6

 
tantra is in roman numerals: 0, I, II, III, IV, V
0 is the prasTAva
-------------------------------------------
# construct index.js, and check for internal consistencies
python make_js_index.py index.txt index.js

----------------------------------------
app construction.
2 apps are needed:
app1 -- (tantra,shloka) see readme_app1.txt
app2 -- (ipage,line-number)  see readme_app2.txt


----------------------------------------
local copies of dictionaries with links
----------------------------------------
# get temporary local copy of dictionaries for checking
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt


-------------------------------------------
7041 matches in 7033 lines for "<ls>PAÑCAT. " in buffer: temp_pwg.txt
3 types of references in pwg:
1767 matches for "<ls>PAÑCAT. [IV]+,[0-9]+" tantra,shloka

4870 matches for "<ls>PAÑCAT. [0-9]+,[0-9]+ ipage,line-number
49 matches for "<ls>PAÑCAT. Pr. [0-9]+  prastava,shloka

(+ 1767 4870 49) 6686  : expected 7041 !
(- 7041 6686) = 355 not accounted for.

Pañcat.
-------
PWG: PAÑCAT. [0-9]+,[0-9]+\.
+ <L>7563<pc>1-0565<k1>asmadviDa   <ls>PAÑCAT. 99,13.</ls> 99 + 14 = 113
+ <L>19928<pc>2-0509<k1>krUrAkza   <ls>PAÑCAT. 173,21.</ls> 173 + 14 = 187
+ <L>28543<pc>3-0214<k1>tadrUpa      <ls>PAÑCAT. 38,20.</ls>  38  + 14 =  52
+ <L>1054<pc>1-0078<k1>aYjana  <ls>PAÑCAT. 10,7   10 + 14 = 24
+ <L>42003<pc>4-0445<k1>pada  <ls>PAÑCAT. 103,3.</ls> sAcivyapada 103 + 14 = 117
+ <L>1303<pc>1-0096<k1>atidUra   <ls>PAÑCAT. 105,4.</ls>  105 + 14 = 119

------
PWG: "PAÑCAT. [IV]+,[0-9]+\.
+ <L>795<pc>1-0060<k1>acakzus    <ls>PAÑCAT. I,393.</ls> (ipage=83)
+ <L>15472<pc>2-0134<k1>karpUra  <ls>PAÑCAT. II,58. (ipage = 115)
+ <L>22050<pc>2-0710<k1>gala     <ls>PAÑCAT. III,265
+ <L>1282<pc>1-0094<k1>atiTi  <ls>PAÑCAT. IV,2 — 5.</ls>
+ <L>33454<pc>3-0670<k1>durAkranda  <ls>PAÑCAT. IV,31.</ls> (ipage 213)
+ <L>32156<pc>3-0541<k1>darSanIya <ls>PAÑCAT. IV,40.</ls>  (ipage 218)
+ <L>2724<pc>1-0199<k1>anukAlam   <ls>PAÑCAT. V,51.</ls>

-------
PWG: <ls>PAÑCAT. Pr. [1-9]+
+  <L>4493<pc>1-0330<k1>aBigamana  <ls>PAÑCAT. Pr. 8.</ls> (ipage 4)
+ <L>9085<pc>1-0680<k1>Ayus  <ls>PAÑCAT. Pr. 10.</ls>  (ipage 4) taTAyur


---------------------
format observations: ???
format 5 fields tab-separated values
page
tantram   0=Pr.,1,2,3,4,5
fromv
tov
ipage

first lines of index
page	tantram	fromv	tov	ipage
17	0	1	4	3
18	0	5	10	4
19	0	11	11	5
20	1	1	8a	6
21	1	8b	16	7


------
# construct index.js, and check for internal consistencies
python make_js_index.py index.txt index.js



----------------------------------------
Random checks between pwg , the pdf and index

python generate_random.py 5 pw1 temp_pw.txt index.txt check_pwg1.txt
regex_raw = <ls>PAÑCAT. ([0-9]+),([0-9]+)
found 4870 instances in kosha
All in this random sample checked.

python generate_random.py 5 pwg2 temp_pwg.txt index.txt check_pwg2.txt
regex_raw = <ls>PAÑCAT. ([VI]+),([0-9]+)
found 1767 instances in kosha
All in this random sample checked.

python generate_random.py 5 pwg3 temp_pwg.txt index.txt check_pwg3.txt
regex_raw = <ls>PAÑCAT. (Pr\.) ([0-9]+)
found 49 instances in kosha
All in this random sample checked.

-----------------------------------
Random checks between pw , the pdf and index

python generate_random.py 5 pw1 temp_pw.txt index.txt check_pw1.txt
regex_raw = <ls>PAÑCAT. ([0-9]+),([0-9]+)
found 241 instances in kosha
All in this random sample checked.

python generate_random.py 5 pw2 temp_pw.txt index.txt check_pw2.txt
regex_raw = <ls>PAÑCAT. ([VI]+),([0-9]+)
found 17 instances in kosha
one NOT FOUND:
key (3, 193): 198	III	192b	197	181
L= 2987, hw= aDfzwa, pc=1-035-b
The other 4 in this random sample checked.

python generate_random.py 5 pw3 temp_pw.txt index.txt check_pw3.txt
regex_raw = <ls>PAÑCAT. (Pr\.) ([0-9]+)
found 0 instances in kosha

-----------------------------------
Random checks between pwkvn , the pdf and index

python generate_random.py 5 pwkvn1 temp_pwkvn.txt index.txt check_pwkvn1.txt
regex_raw = <ls>PAÑCAT. ([0-9]+),([0-9]+)
found 26 instances in kosha
All in this random sample checked.

python generate_random.py 5 pwkvn2 temp_pwkvn.txt index.txt check_pwkvn2.txt
regex_raw = <ls>PAÑCAT. ([VI]+),([0-9]+)
found 0 instances in kosha

python generate_random.py 5 pwkvn3 temp_pwkvn.txt index.txt check_pwkvn3.txt
regex_raw = <ls>PAÑCAT. (Pr\.) ([0-9]+)
found 0 instances in kosha

-----------------------------------
Random checks between sch , the pdf and index

python generate_random.py 5 sch1 temp_sch.txt index.txt check_sch1.txt
regex_raw = <ls>Pañcat. ([0-9]+),([0-9]+)
found 26 instances in kosha
All in this random sample checked.

python generate_random.py 5 sch2 temp_sch.txt index.txt check_sch2.txt
regex_raw = <ls>Pañcat. ([vi]+),([0-9]+)
found 0 instances in kosha

python generate_random.py 5 sch3 temp_sch.txt index.txt check_sch3.txt
regex_raw = <ls>Pañcat. (Pr\.) ([0-9]+)
found 0 instances in kosha

python generate_random.py 5 sch3 temp_sch.txt index.txt check_sch3.txt

-----------------------------------
Random checks between mw , the pdf and index

python generate_random.py 5 mw1 temp_mw.txt index.txt check_mw1.txt
regex_raw = <ls>Pañcat. ([0-9]+),([0-9]+)
found 2 instances in kosha
All in this random sample checked.

python generate_random.py 5 mw2 temp_mw.txt index.txt check_mw2.txt
regex_raw = <ls>Pañcat. ([vi]+),([0-9]+)
found 205 instances in kosha
  All NOT FOUND.  pantankose is not right source !
python generate_random.py 5 mw3 temp_mw.txt index.txt check_mw3.txt
regex_raw = <ls>Pañcat. (Pr\.) ([0-9]+)
found 0 instances in kosha

=============================================================
sync to github:  csl-websanlexicon, csl-apidev
