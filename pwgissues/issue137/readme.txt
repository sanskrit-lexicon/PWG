issue137/readme.txt
07-17-2025 begun ejf
NĀRADA PAÑCARĀTRA

Ref: https://github.com/sanskrit-lexicon/PWG/issues/137

This issue137 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue137

-----------------
pdf:
/e/pdfwork/pancar/'Nárada Pañcarātra (1865).pdf'
-----------------


---------------------------------------
Narada.Pancaratra.1865.xlsx from IrinaKonstant

index_orig.txt converted to text file, tab-separators

7 fields per line
page	ratra	adhy.	from v.	to v.	ipage	remark(s)
18	1	1	1	6	1	
19	1	1	7	16	2	
20	1	1	17	27a	3	

--------------------------------------
cp index_orig.txt index.txt
Some adjustments:
1. verse 3,4,16 appears on two pages -- which is 'right'?
  removoing (1) -- this means page 194 will match 3,4,16
old:
194	3	4	11	16	177	
195	3	4	16(1)	22a	178	renumber the repeated v.16
new:
194	3	4	11	16	177	
195	3	4	16	22a	178	renumber the repeated v.16
2.
v.30 to v.39 occur two times! But, it is seen that except at two places, the PWG cited these conflicting repeats along with page numbers.
old:
265	4	3	28	37	248	
266	4	3	38	37	249	
267	4	3	38	48	250	

265 28,...,37
266 38,39   then  30,...,37
267 38,39   then  40,...,48
new: (effectively skip page 266)
266	4	3	37	37	249	


-------------------------------------------
# construct index.js, and check for internal consistencies
python make_js_index.py index.txt index.js

----------------------------------------
# get temporary local copy of dictionaries for checking
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt

----------------------------------------
csl-pywork/v02/distinctfiles/pwg/pywork/pwgauth/pwgbib_input.txt
pwgbib_input.txt  correction
PAÑCAR. = NĀRADA PAÑCARĀTRA
   (per https://github.com/sanskrit-lexicon/PWG/issues/137#issuecomment-2784691655)

ratra, adhy, verse

pwg: PAÑCAR. N,N,N  OR PAÑCAR. S. N  (page)
pw : PAÑCAR. N,N,N
pwkvn : PAÑCAR. N,N,N
sch: Pañcar. N,N,N     <<< sch has ratra = 4 sometimes?
mw: Pañcar.  R,N,N

----------------------------------------
# preliminary check of temp_pwg.txt and index and pdf
 random selection of <ls>PAÑCAR

115 matches for "n="PAÑCAR." in buffer: temp_pwg.txt
  There are several errors noticed (2 or 1 parameter)

2110 matches in 2108 lines for "<ls>PAÑCAR." in buffer: temp_pwg.txt
2077 matches in 2076 lines for "<ls>PAÑCAR. [0-9]+,[0-9]+,[0-9]+[.<]" in buffer: temp_pwg.txt

2077 matches in 2076 lines for "<ls>PAÑCAR. [0-9]+,[0-9]+,[0-9]+[^.<]" in buffer: temp_pwg.txt

-------------------------------------------------
python generate_random.py ALL pwg3 temp_pwg.txt index.txt check_pwg3_ALL.txt check_pwg3_ALL_nopagerec.txt

regex_raw = <ls>PAÑCAR. ([0-9]+),([0-9]+),([0-9]+)
found 2091 instances in kosha
found 1207 distinct in kosha
write_examples: 2091 written to check_pwg3_ALL.txt
4 instances of 'pagerec not found'
write_examples: 4 written to check_pwg3_ALL_nopagerec.txt

 Checked one or two in each ratra (1-5). OK.

-------------------------------------------------------
cp temp_pwg.txt temp_pwg1.txt
manual edits of temp_pwg1.txt

Resolve the 4 nopagerec cases:
110048 : sugopya : PAÑCAR. 1,4,105 : PAÑCAR. 1,14,105 : print change (jim)
121217 : bawu : PAÑCAR. 2,4,65 : PAÑCAR. 2,4,45 : print change (ab)
89364 : vAgISatva : PAÑCAR. 3,8,56 : PAÑCAR. 3,15,56 : print change
82375 : yoga : PAÑCAR. 3,20,30 : PAÑCAR. 3,2,30 : print change

Two cases with 2 parms (from issue94/lsexamine2)
54266 : Bava : PAÑCAR. 12,45 : PAÑCAR. 1,2,45 : print change jim
55050 : Buj  : PAÑCAR. 36,22. : PAÑCAR. 3,4,24. : typo

Also, changed 120+ 'incomplete' references.

There still remain 300+ 'incomplete' references.

---- remake xml and check
cp temp_pwg1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue137

-------------------------------------------------------
# rerun generate_random with temp_pwg1
python generate_random.py ALL pwg3 temp_pwg1.txt index.txt check_pwg3_ALL_1.txt check_pwg3_ALL_1_nopagerec.txt

regex_raw = <ls>PAÑCAR. ([0-9]+),([0-9]+),([0-9]+)
found 2091 instances in kosha
found 1205 distinct in kosha
write_examples: 2091 written to check_pwg3_ALL_1.txt
0 instances of 'pagerec not found'

READY FOR REPO!

-------------------------------------------------------
app construction. see readme_app.txt

app1 -- (adhyAya,kanda,shloka) 
app0 -- (ipage,) 
app2 -- ipage,line See https://github.com/sanskrit-lexicon/PWG/issues/145

---------------------------------------
Change to basicadjust to activate links.
see readme_websanlexicon.txt

---------------------------------------
Random checks between dictionary and the pdf and index
 for dictionaries pwg, pw, pkwvn, sch, mw.
 see readme_checks.txt

=============================================================
sync to github:
csl-websanlexicon  # git pull
csl-apidev  # git pull
csl-pywork # git pull
csl-orig # git pull
csl-corrections

sync to Cologne, and redo the 5 dictionaries.

-------------------------------------------------------------
------------------------------------------------------------
THE END
