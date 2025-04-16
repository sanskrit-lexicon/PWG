

=====================================================
Checks for all dictionaries after basicadjust updated.

----------------------------------------
# get temporary local copy of dictionaries for checking
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt

----------------------------------------------------
First, pwg
There are 3 forms to check

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
