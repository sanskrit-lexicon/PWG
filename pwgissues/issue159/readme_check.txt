
generate_random checks for aitbr
----
  'pwg2':r'<ls>AIT. BR. ([0-9]+),([0-9]+)[^0-9,]',


python generate_random.py ALL pwg2 temp_pwg_0.txt index.txt check_pwg2_ALL.txt check_pwg2_nopagerec.txt
regex_raw = <ls>AIT. BR. ([0-9]+),([0-9]+)[^0-9,]
found 3726 instances in kosha
found 285 distinct in kosha
write_examples: 3726 written to check_pwg2_ALL.txt
6 instances of 'pagerec not found'
write_examples: 6 written to check_pwg2_nopagerec.txt

NOTE: All the 3-parameter forms will be linked to aitbr_auf.

--------------------------
  'pwg3':r'<ls>AIT. BR. ([0-9]+),([0-9]+),([0-9]+)',

python generate_random.py ALL pwg3 temp_pwg_0.txt index.txt check_pwg3_ALL.txt check_pwg3_nopagerec.txt
regex_raw = <ls>AIT. BR. ([0-9]+),([0-9]+),([0-9]+)
found 4 instances in kosha
found 4 distinct in kosha
write_examples: 4 written to check_pwg3_ALL.txt
4 instances of 'pagerec not found'
write_examples: 4 written to check_pwg3_nopagerec.txt

Note: 08-13-2025  these print changes rescinded in temp_pwg_1.txt
   3-parameter references Haug's pdf may be wrong print target
97002 : SaMsa :  AIT. BR. 2,2,4 :  AIT. BR. 2,4 :  NOT CHANGED
12865 : UvaDya : AIT. BR. 2,6,11 : AIT. BR. 2,6. 11 : PRINT CHANGE (Andhrabharati)
46014 : purastAt : AIT. BR. 2,6,33 : AIT. BR. 2,6. 33. : TYPO (Andhrabharati)

After changes to temp_pwg_1.txt
python generate_random.py ALL pwg3 temp_pwg_1.txt index.txt check_pwg3_ALL_1.txt check_pwg3_nopagerec_1.txt
regex_raw = <ls>AIT. BR. ([0-9]+),([0-9]+),([0-9]+)
found 1 instances in kosha
found 1 distinct in kosha
write_examples: 1 written to check_pwg3_ALL_1.txt
1 instances of 'pagerec not found'
write_examples: 1 written to check_pwg3_nopagerec_1.txt

The instance:
key (2, 2, 4): pagerec not found
97002 : SaMsa : AIT. BR. 2,2,4 :

--------------------------
  'pw3':r'<ls>AIT. BR. ([0-9]+),([0-9]+),([0-9]+)',

python generate_random.py ALL pw3 temp_pw_0.txt index.txt check_pw3_ALL.txt check_pw3_nopagerec.txt
regex_raw = <ls>AIT. BR. ([0-9]+),([0-9]+),([0-9]+)
found 127 instances in kosha
found 111 distinct in kosha
write_examples: 127 written to check_pw3_ALL.txt
118 instances of 'pagerec not found'
write_examples: 118 written to check_pw3_nopagerec.txt


python generate_random.py ALL pw2 temp_pw_0.txt index.txt check_pw2_ALL.txt check_pw2_nopagerec.txt
regex_raw = <ls>AIT. BR. ([0-9]+),([0-9]+)[^0-9,]
found 95 instances in kosha
found 69 distinct in kosha
write_examples: 95 written to check_pw2_ALL.txt
1 instances of 'pagerec not found'
write_examples: 1 written to check_pw2_nopagerec.txt

64451 : parihAram : AIT. BR. 2,278 : 
parihAra not found at page 278 of volume 2

--------------------------
'pwkvn3':r'<ls>AIT. BR. ([0-9]+),([0-9]+),([0-9]+)',

python generate_random.py ALL pwkvn3 temp_pwkvn_0.txt index.txt check_pwkvn3_ALL.txt check_pwkvn3_nopagerec.txt

regex_raw = <ls>AIT. BR. ([0-9]+),([0-9]+),([0-9]+)
found 39 instances in kosha
found 36 distinct in kosha
write_examples: 39 written to check_pwkvn3_ALL.txt
36 instances of 'pagerec not found'
write_examples: 36 written to check_pwkvn3_nopagerec.txt

--------------------------
'pwkvn2':r'<ls>AIT. BR. ([0-9]+),([0-9]+)[^0-9,]',

python generate_random.py ALL pwkvn2 temp_pwkvn_0.txt index.txt check_pwkvn2_ALL.txt check_pwkvn2_nopagerec.txt

regex_raw = <ls>AIT. BR. ([0-9]+),([0-9]+)[^0-9,]
found 3 instances in kosha
found 3 distinct in kosha
write_examples: 3 written to check_pwkvn2_ALL.txt
0 instances of 'pagerec not found'

--------------------------
'sch3':r'<ls>Ait. Br. ([0-9]+),([0-9]+),([0-9]+)',

python generate_random.py ALL sch3 temp_sch_0.txt index.txt check_sch3_ALL.txt check_sch3_nopagerec.txt

found 38 instances in kosha
found 35 distinct in kosha
write_examples: 38 written to check_sch3_ALL.txt
35 instances of 'pagerec not found'
write_examples: 35 written to check_sch3_nopagerec.txt

--------------------------
'sch2':r'<ls>Ait. Br. ([0-9]+),([0-9]+)[^0-9,]',

python generate_random.py ALL sch2 temp_sch_0.txt index.txt check_sch2_ALL.txt check_sch2_nopagerec.txt
regex_raw = <ls>Ait. Br. ([0-9]+),([0-9]+)[^0-9,]
found 3 instances in kosha
found 3 distinct in kosha
write_examples: 3 written to check_sch2_ALL.txt
0 instances of 'pagerec not found'

--------------------------
'mw3':r'<ls>AitBr. ([iv]+), *([0-9]+), *([0-9]+)',

python generate_random.py ALL mw3 temp_mw_0.txt index.txt check_mw3_ALL.txt check_mw3_nopagerec.txt

found 116 instances in kosha
found 106 distinct in kosha
write_examples: 116 written to check_mw3_ALL.txt
111 instances of 'pagerec not found'
write_examples: 111 written to check_mw3_nopagerec.txt

--------------------------
'mw2':r'<ls>AitBr. ([iv]+), *([0-9]+)[^0-9,]',

python generate_random.py ALL mw2 temp_mw_0.txt index.txt check_mw2_ALL.txt check_mw2_nopagerec.txt

regex_raw = <ls>AitBr. ([iv]+), *([0-9]+)[^0-9,]
found 168 instances in kosha
found 96 distinct in kosha
write_examples: 168 written to check_mw2_ALL.txt
0 instances of 'pagerec not found'

==================================================

lsfix2 pwg
--------------------------
python lsfix2.py pwg temp_pwg_0.txt lsfix2_pwg_0.txt

4514 lines written to lsfix2_pwg_0.txt
(True, 2) 4054
('fixed', 2) 350
(None, 2) 94
(False, 2) 8
(True, 3) 7
('fixed', 3) 1

edit temp_pwg_1.txt and edit the 'False' and 'None' items

Also, check the ('fixed', 3) item

Questions:
---
96220 : vyac L AIT. BR. 4,12. ĀRAṆS. 1,6. #  Only instance of ĀRAṆS. Treat as separate lscode?
---
52117 : bahizpavamAna :
<ls>HAUG</ls>, <ls>AIT. BR. S. 120</ls>, Anm.; über andere Formen
<ls n="AIT. BR.">S. 347, Anm.</ls>
---
108383 : sAptadaSya : <ls>AIT. BR. Comm. 1,1.</ls> : ?

-------------------
# redo lsfix2 after corrections
python lsfix2.py pwg temp_pwg_1.txt lsfix2_pwg_1.txt
4510 lines written to lsfix2_pwg_1.txt
(True, 2) 4118
('fixed', 2) 388
(None, 2) 3
(True, 3) 1

None	2	505611	<ls>AIT. BR. S. 120</ls>	
None	2	505612	<ls n="AIT. BR.">S. 347, Anm.</ls>	
None	2	1008048	<ls>AIT. BR. Comm. 1,1.</ls>	

=======================================================
# apply the 'fixed' cases to pwg
python dict_replace2.py temp_pwg_1.txt lsfix2_pwg_1.txt temp_pwg_2.txt
4510 lines read from lsfix2_pwg_1.txt
386 lines to change
apply_repls: 386 lines changed

## regenerate pwg displays locally from temp_pwg_2.txt
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159

---------------------------
How to handle xmlchk error (documentation)
1. Open /c/xampp/htdocs/cologne/pwg/pywork/pwg.xml in Emacs
 use C-cC-n to find xml errors.
 Make correction in temp_pwg_1.txt
 When done
2. rerun next two
python lsfix.py dummy temp_pwg_1.txt lsfix_1.txt 
python dict_replace.py temp_pwg_1.txt lsfix_1.txt temp_pwg_2.txt
3. Redo the 'remake xml ...' steps.
   continue these steps until xmlchk  says 'ok'.
---- end of 'How to handle xmlchk error'

------------------------
==================================================

lsfix2 pw
--------------------------
python lsfix2.py pw temp_pw_0.txt lsfix2_pw_0.txt
227 lines written to lsfix2_pw_0.txt
(True, 2) 92
('fixed', 2) 4
('fixed', 3) 6
(None, 2) 1
(True, 3) 124

cp temp_pw_0.txt temp_pw_1.txt
Correct the 'None,2' instance.

python lsfix2.py pw temp_pw_1.txt lsfix2_pw_1.txt
227 lines written to lsfix2_pw_1.txt
(True, 2) 92
('fixed', 2) 5
('fixed', 3) 6
(True, 3) 124

python dict_replace2.py temp_pw_1.txt lsfix2_pw_1.txt temp_pw_2.txt
227 lines read from lsfix2_pw_1.txt
11 lines to change
apply_repls: 11 lines changed

## regenerate pw displays locally
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159
cp temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159

------------------------------------------------------
lsfix2 pwkvn
--------------------------
python lsfix2.py pwkvn temp_pwkvn_0.txt lsfix2_pwkvn_0.txt
46 lines written to lsfix2_pwkvn_0.txt
(True, 2) 3
(True, 3) 43

No changes needed to pwkvn

------------------------------------------------------
lsfix2 sch
--------------------------
python lsfix2.py sch temp_sch_0.txt lsfix2_sch_0.txt
41 lines written to lsfix2_sch_0.txt
(True, 3) 34
(None, 2) 3
(True, 2) 3
('fixed', 3) 1

Correct the 3 None,2 instances

cp temp_sch_0.txt temp_sch_1.txt

# 
python lsfix2.py sch temp_sch_1.txt lsfix2_sch_1.txt
44 lines written to lsfix2_sch_1.txt
(True, 3) 40
(True, 2) 3
('fixed', 3) 1

#
python dict_replace2.py temp_sch_1.txt lsfix2_sch_1.txt temp_sch_2.txt
44 lines read from lsfix2_sch_1.txt
1 lines to change
apply_repls: 1 lines changed


## regenerate sch displays locally
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159
cp temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh sch  ../../sch
sh xmlchk_xampp.sh sch
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159

===================================================
cp temp_mw_0.txt temp_mw_1.txt
manual changes to temp_mw_1.txt

## regenerate mw displays locally
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159
