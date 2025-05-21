

----------------------------------------
# get temporary local copy of dictionaries for checking
#  meghadUta links

cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt

PWG: ŚṚṄGĀRAT.
sch: Śṛṅgt.
mw:  Śṛṅgār.

one parameter
=====================================================

PRELIMINARY MANUAL CHECK for pwg ŚṚṄGĀRAT.

python generate_random_srnga.py 5 pwg temp_pwg.txt index_srnga.txt check_pwg_srnga_man.txt
regex_raw = <ls>ŚṚṄGĀRAT. ([0-9]+)
found 100 instances in kosha


5 written to check_pwg_srnga_man.txt

These 5 random checks OK.

End of preliminary manual check for ŚṚṄGĀRAT. in pwg

=====================================================
Checks for all dictionaries after basicadjust updated.

edit generate_random_srnga.py
  function get_dict_regex:
      make consistent with basicadjust.php; see
     readme_websanlexicon.txt
  function get_dict_key
  function set_pagerec_key
----------------------------------------------------
pwg
python generate_random_srnga.py 5 pwg temp_pwg.txt index_srnga.txt check_srnga_pwg.txt
found 100 instances in kosha
found 21 distinct in kosha

All in this random sample checked.

----------------------------------------------------
pw 
python generate_random_srnga.py 5 pw temp_pw.txt index_srnga.txt check_srnga_pw.txt
regex_raw = <ls>ŚṚṄGĀRAT. ([0-9]+)
found 0 instances in kosha

Nothing to check

----------------------------------------------------
pwkvn 
python generate_random_srnga.py 5 pwkvn temp_pwkvn.txt index_srnga.txt check_srnga_pwkvn.txt
regex_raw = <ls>ŚṚṄGĀRAT. ([0-9]+)
found 0 instances in kosha

Nothing to check

----------------------------------------------------
sch 
python generate_random_srnga.py 5 sch temp_sch.txt index_srnga.txt check_srnga_sch.txt
regex_raw = <ls>Śṛṅgt. ([0-9]+)
found 163 instances in kosha

Śṛṅgt. refers to a different edition
      Śṛṅgāratilakabhāṇa ed. Kāvyamālā Nr. 44.

Nothing to check

-----------------------------------
----------------------------------------------------
mw
python generate_random_srnga.py 5 mw temp_mw.txt index_srnga.txt check_srnga_mw.txt
regex_raw = <ls>Śṛṅgār. ([0-9]+)
found 1 instances in kosha

The sample checked.

---------------------------------
All (almost) checks favorable.
Ready to install:
 csl-websanlexicon
 csl-apidev
