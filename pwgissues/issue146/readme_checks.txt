

----------------------------------------
# get temporary local copy of dictionaries for checking
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt


2512 KUMĀRAS.	KUMĀRASAM̃BHAVA
In pwgbib_input.txt there are no other forms of reference.


2459 matches for "<ls>KUMĀRAS\. " in buffer: temp_pwg.txt

The checks will be made for "<ls>KUMĀRAS. " in pwg, pw, pwkvn
For sch: Kumāras
For mw: Kum.

=====================================================

PRELIMINARY MANUAL CHECK for pwg

modify generate_random.py as needed:
  
python generate_random.py 5 pwg temp_pwg.txt index.txt check_pwg_man.txt
regex_raw = <ls>KUMĀRAS. ([0-9]+),([0-9]+)
found 2451 instances in kosha

5 written to check_pwg_man.txt

These 5 random checks OK.

End of preliminary manual check.

=====================================================
Checks for all dictionaries after basicadjust updated.

edit generate_random.py
  function get_dict_regex:
      make consistent with basicadjust.php; see
     readme_websanlexicon.txt
  function get_dict_key
  function set_pagerec_key
----------------------------------------------------
pwg
python generate_random.py 5 pwg temp_pwg.txt index.txt check_pwg.txt
regex_raw = <ls>KUMĀRAS. ([0-9]+),([0-9]+)
found 2451 instances in kosha

All in this random sample checked.

-----------------------------------
Random checks between pw , the pdf and index

python generate_random.py 5 pw temp_pw.txt index.txt check_pw.txt
regex_raw = <ls>KUMĀRAS. ([0-9]+),([0-9]+)
found 124 instances in kosha

All in this random sample checked.

-----------------------------------
Random checks between pwkvn , the pdf and index

python generate_random.py 5 pwkvn temp_pwkvn.txt index.txt check_pwkvn.txt
regex_raw = <ls>KUMĀRAS. ([0-9]+),([0-9]+)
found 35 instances in kosha

All in this random sample checked.

-----------------------------------
Random checks between sch , the pdf and index

# sch.txt markup change 
python generate_random.py 5 sch temp_sch.txt index.txt check_sch.txt
regex_raw = <ls>Kumāras. ([0-9]+),([0-9]+)
found 39 instances in kosha

All in this random sample checked.

-----------------------------------
Random checks between mw , the pdf and index

python generate_random.py 5 mw temp_mw.txt index.txt check_mw.txt
regex_raw = <ls>Kum. ([vix]+), *([0-9]+)
found 264 instances in kosha

One NOT FOUND:
key (3, 39): 48	3	35	39	35
L= 74050, hw= cetanatva, pc=397,3
check: NOT FOUND

---------------------------------
All (almost) checks favorable.
Ready to install:
 csl-websanlexicon
 csl-apidev
