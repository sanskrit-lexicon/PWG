

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

edit generate_random.py
  function get_dict_regex:
      make consistent with basicadjust.php; see
     readme_websanlexicon.txt
  function get_dict_key
  function set_pagerec_key
----------------------------------------------------
pwg
python generate_random.py 5 pwg temp_pwg.txt index.txt check_pwg.txt
regex_raw = <ls>BHAṬṬ. ([0-9]+),([0-9]+)
found 2183 instances in kosha

All in this random sample checked.

-----------------------------------
Random checks between pw , the pdf and index
Just one form known
python generate_random.py 5 pw temp_pw.txt index.txt check_pw.txt
regex_raw = <ls>BHAṬṬ. ([0-9]+),([0-9]+)
found 125 instances in kosha

All in this random sample checked.

-----------------------------------
Random checks between pwkvn , the pdf and index

Just 1 form found
python generate_random.py 5 pwkvn temp_pwkvn.txt index.txt check_pwkvn.txt
regex_raw = <ls>BHAṬṬ. ([0-9]+),([0-9]+)
found 15 instances in kosha

In this random sample checked, one not found:
key (9, 64): I	673	9	64	64	665
L= 9379, hw= vizkanttar, pc=6-306-b


-----------------------------------
Random checks between sch , the pdf and index

# sch.txt markup change 
python generate_random.py 5 sch temp_sch.txt index.txt check_sch.txt
regex_raw = <ls>Bhaṭṭ. ([0-9]+),([0-9]+)
found 15 instances in kosha

One in this random sample NOT FOUND:
key (9, 64): I	673	9	64	64	665
L= 5688, hw= aviskanttar, pc=077-3

-----------------------------------
Random checks between mw , the pdf and index

python generate_random.py 5 mw temp_mw.txt index.txt check_mw.txt
regex_raw = <ls>Bhaṭṭ. ([vix]+), *([0-9]+)
found 140 instances in kosha

All in this random sample checked.

---------------------------------
All (almost) checks favorable.
Ready to install:
 csl-websanlexicon
 csl-apidev
