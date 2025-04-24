

----------------------------------------
# get temporary local copy of dictionaries for checking
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt

=====================================================
preliminary manual checks (before basicadjust updated)

BHAṬṬ. BHAṬṬIKĀVYA
In pwgbib_input.txt there are 3 forms of reference:

BHAṬṬ. = BHAṬṬIKĀVYA, ed. Calc. (GILD. Bibl. 137).

possible other abbreviations for BHAṬṬIKĀVYA
BHAṬṬI	Bhaṭṭi	BHAṬṬI = ? [Cologne Addition] 
BHAṬṬIK	Bhaṭṭik	BHAṬṬIK = ? [Cologne Addition] 

2195 matches for "<ls>BHAṬṬ\. " in buffer: temp_pwg.txt

3 matches for "<ls>BHAṬṬI" in buffer: temp_pwg.txt

The checks will be made for "<ls>BHAṬṬ. " in pwg, pw, pwkvn

PRELIMINARY MANUAL CHECK 
python generate_random.py 5 pwg temp_pwg.txt index.txt check_pwg_man.txt
regex_raw = <ls>BHAṬṬ. ([0-9]+),([0-9]+)
found 2183 instances in kosha
5 written to check_pwg_man.txt

These 5 random checks OK.

End of preliminary manual check.

=====================================================
Checks for all dictionaries after basicadjust updated.

----------------------------------------------------
First, pwg

pwg1
python generate_random.py 5 pwg1 temp_pwg.txt index.txt check_pwg1.txt
regex_raw = <ls>RAGH. ed. Calc. ([0-9]+),([0-9]+)
found 116 instances in kosha
All in this random sample checked.

pwg2
python generate_random.py 5 pwg2 temp_pwg.txt index.txt check_pwg2.txt
regex_raw = <ls>RAGH. (ed. Calc.) ([0-9]+),([0-9]+)
found 15 instances in kosha
All in this random sample checked.

pwg3 
python generate_random.py 5 pwg3 temp_pwg.txt index.txt check_pwg3.txt
regex_raw = <ls>RAGH. (Calc.) ([0-9]+),([0-9]+)
found 1 instance in kosha
All in this random sample checked.

-----------------------------------
Random checks between pw , the pdf and index
Just one form known
python generate_random.py 5 pw temp_pw.txt index.txt check_pw.txt
regex_raw = <ls>RAGH. ed. Calc. ([0-9]+),([0-9]+)
found 9 instances in kosha

All in this random sample checked.

-----------------------------------
Random checks between pwkvn , the pdf and index

Just 1 form found
python generate_random.py 5 pwkvn temp_pwkvn.txt index.txt check_pwkvn.txt
regex_raw = <ls>RAGH. ed. Calc. ([0-9]+),([0-9]+)
found 2 instances in kosha
f
All in this random sample checked.


-----------------------------------
Random checks between sch , the pdf and index
xxxx
# sch.txt markup change 
python generate_random.py 5 sch temp_sch.txt index.txt check_sch.txt
regex_raw = <ls>Ragh. ed. Calc. ([0-9]+),([0-9]+)
found 2 instances in kosha

All in this random sample checked.


-----------------------------------
Random checks between mw , the pdf and index

Only 1 form seen
python generate_random.py 5 mw temp_mw.txt index.txt check_mw.txt
regex_raw = <ls>Ragh. \(C\) ([vix]+), *([0-9]+)
found 2 instances in kosha

All in this random sample checked.
---------------------------------
All checks favorable.
Ready to install:
 csl-websanlexicon
 csl-apidev
 csl-orig
