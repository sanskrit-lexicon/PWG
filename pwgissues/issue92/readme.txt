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



