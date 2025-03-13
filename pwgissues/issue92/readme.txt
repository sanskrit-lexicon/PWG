issue92/readme.txt
03-06-2025 begun ejf
09176 VARĀH. BṚH. S. : VARĀHAMIHIRA'S BṚHATSAM̃HITĀ

Ref: https://github.com/sanskrit-lexicon/PWG/issues/92

This issue92 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue92

-----------------
pdf: Br.pdf
/e/pdfwork/brhatsamhita/Br.pdf

----------------------------------------
Index file
Brihatsamhita_v2.Index.xlsx
  convert to tsv (Google)
  rename index.txt  (save copy as index_orig.txt)
  remove comment at top
  remove and extra tabs at end of each line
Note comment at page 81
81	2	5b	6a	6		6 - нет ?
 нет = no   There is no verse 6 here !
 Also, pwg has no reference to this verse.
 


Brihatsamhita.Notes.docx   mentions some questions hard to understand

---------------------
format observations:
format 5 fields tab-separated values
page
adhy
fromv
tov
ipage

first lines of index
page	adhy.	fromv.	tov.	ipage
76	1	1	4	1
77	1	5	10a	2
78	1	10b	11	3

last lines of index
581	107	2	7a	506
582	107	7b	12	507
583	107	13	13	508

----------------------------------------
# Prepare index.js
python make_js_index.py index.txt index.js
587 Success: Page records read from index.txt
json data written to index.js
pagerecs passes check1_adhy
check1 finds no problems

----------------------------------------
# get temporary local copy of pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt

----------------------------------------
Selected pages from Br.pdf.
8 - Bṛhatsam̃hitā of Varāhamihira, KERN, 1865
9 - blank
10 - Devanagari title page
11 - blank
12 1 preface Hindu astronomer and astrologer
...
75 64 end of preface
76 १  श्रीगणॅशाय नमः   <<< index starts here   upanayana (introduction)

----------------------------------------
Make misc checks between pwg , Br.pdf and index
Several anomalies noticed.
see readme_brihat_problems.txt

We conclude that, at least in part, pwg references
are from some other version of Brihat

Andhrabharati provided an interesting theory:
Ref: https://github.com/sanskrit-lexicon/PWG/issues/92#issuecomment-2708358312

Basic conclusions from AB's analysis related to PWG:
  There is no available alternative to Br.pdf, 
  Volumes 5-7 of PWG were published after Br.pdf, and
  references in these volumes should be consistent with Br.pdf

----------------------------------------
see byvol/readme.txt for further analysis of AB's theory.
Conclusion: Agree that it is 'safe' to generate links to Br.pdf
from pwg for volumes 5-7 of pwg.
Also, volume 1 should be safe.
Volumes 2-4 references are NOT safe.

basicadjust.php can handle this 'volume' distinction for PWG.

--------------------------------------------
No study has been made yet related to PW (and PWKVN), sch and MW(99).

--------------------------------------------
03-12-2025
----------------------------------------
# get temporary local copy of pw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt
Random check of links:  (~300 links)
+ pw <L>560<pc>1-007-b<k1>agnidevA  <ls>VARĀH. BṚH. S. 71,6</ls>
+ pw L>41788<pc>2-254-c<k1>jayada  <ls>VARĀH. BṚH. S. 17,7</ls>
+ pw <L>69566<pc>4-118-c<k1>pfTvIDara <ls>VARĀH. BṚH. S. 53,47</ls>
+ pw <L>4553<pc>1-053-c<k1>anuparipAwikrama <ls>VARĀH. BṚH. S. 107,13</ls>
+ pw <L>104532<pc>6-123-b<k1>viSalaBamarut  <ls>VARĀH. BṚH. S. 84,1</ls>

Links check for pw

----------------------------------------
# get temporary local copy of pwkvn.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn.txt
Random check of links: (37)
+ pwkvn <L>245<pc>1-284-b<k1>aRqa <ls>VARĀH. BṚH. S. 56,22</ls>
+ pwkvn <L>2157<pc>2-289-a<k1>anAditya  <ls>VARĀH. BṚH. S. 2,9</ls>
+ pwkvn <L>4524<pc>3-260-b<k1>kzatajapAta  <ls>VARĀH. BṚH. S. 95,48</ls>

----------------------------------------
# get temporary local copy of mw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt
Random check of links: ()
511 matches for "<ls>VarBṛS. " in buffer: temp_mw.txt
435 matches for "<ls>VarBṛS. [ivxclm]+, [0-9]"
7 matches for "<ls>VarBṛS. [0-9]+, [0-9]
3 matches for "<ls>VarBṛS. [ivxclm]+, [0-9]+, [0-9]+"

+ mw <L>32621.1<pc>186,1<k1>udayarkza  <L>32621.1<pc>186,1<k1>udayarkza
+ mw <L>50523<pc>283,3<k1>kirAta   <ls>VarBṛS. xi, 60</ls>
+ mw <L>65178<pc>355,2<k1>girinagara   <ls>VarBṛS. xiv, 11.</ls>

----------------------------------------
# get temporary local copy of sch.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch.txt
Random check of links: (42)    Varāh. Bṛh. S.
+ sch sch <L>65<pc>002-1<k1>akaluza  <ls>Varāh. Bṛh. S. 8,53.</ls>
+ sch <L>12107<pc>166-2<k1>ganDamAMsi  <ls>Varāh. Bṛh. S. 51,15.</ls>
+ sch <L>17949<pc>248-1<k1>paripluta  <ls>Varāh. Bṛh. S. 68,115.</ls>

---------------------------------
index correction 2,9  starts on previous page
---------------------------------
THE END 03-12-2025.
