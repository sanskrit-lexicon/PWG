

----------------------------------------
# get temporary local copy of dictionaries for checking
#   links

cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt
bhartṛ
In pwg:
01291	BHARTṚ.	BHARTṚHARI, Ausg. von BOHLEN (GILD. Bibl
PWG: BHARTṚ.
sch: Bhartṛ.
mw:  Bhartṛ.

two parameter
=====================================================

PRELIMINARY MANUAL CHECK for pwg BHARTṚ.

python generate_random_bhart.py 5 pwg temp_pwg.txt index_bhart.txt check_pwg_man_bhart.txt
regex_raw = <ls>BHARTṚ. ([0-9]+),([0-9]+)
found 1180 instances in kosha

5 written to check_pwg_man_bhart.txt

One of these checks failed in pwg:
key (2, 13): 76	2	12	17a	39
L= 30736, hw= tyaj, pc=3-0408
check: NOT FOUND  << no tyaj form found in 2,13 on page 76.

=====================================================

PRELIMINARY MANUAL CHECK for pwg CAURAP.

python generate_random_caurap.py 5 pwg temp_pwg.txt index_caurap.txt check_pwg_man_caurap.txt

regex_raw = <ls>CAURAP. ([0-9]+)
found 376 instances in kosha
5 written to check_pwg_man_caurap.txt

All 5 random checks succeed.

=====================================================

End of preliminary manual check for BHARTṚ., CAURAP. in pwg

=====================================================
Checks for all dictionaries after basicadjust updated.

edit generate_random.py
  function get_dict_regex:
      make consistent with basicadjust.php; see
     readme_websanlexicon.txt
  function get_dict_key
  function set_pagerec_key

====================================================
check 5 dictionaries re Bhartṛhariśataka
====================================================
----------------------------------------------------
pwg  bhart
python generate_random_bhart.py 5 pwg temp_pwg.txt index_bhart.txt check_bhart_pwg.txt
regex_raw = <ls>BHARTṚ. ([0-9]+),([0-9]+)
found 1180 instances in kosha

All in this random sample checked.

----------------------------------------------------
pw  bhart
python generate_random_bhart.py 5 pwg temp_pw.txt index_bhart.txt check_bhart_pw.txt
regex_raw = <ls>BHARTṚ. ([0-9]+),([0-9]+)
found 0 instances in kosha

----------------------------------------------------
pwkvn  bhart
python generate_random_bhart.py 5 pwkvn temp_pwkvn.txt index_bhart.txt check_bhart_pwkvn.txt
regex_raw = <ls>BHARTṚ. ([0-9]+),([0-9]+)
found 0 instances in kosha

----------------------------------------------------
sch  bhart
python generate_random_bhart.py 5 sch temp_sch.txt index_bhart.txt check_bhart_sch.txt
regex_raw = <ls>Bhartṛ. ([0-9]+)
found 0 instances in kosha

----------------------------------------------------
mw  bhart
python generate_random_bhart.py 5 mw temp_mw.txt index_bhart.txt check_bhart_mw.txt
regex_raw = <ls>Bhartṛ. ([iv]+), *([0-9]+)
found 129 instances in kosha

All instances check.

====================================================
check 5 dictionaries re Caurapañcāśikā
====================================================
----------------------------------------------------
pwg  caurap
python generate_random_caurap.py 5 pwg temp_pwg.txt index_caurap.txt check_caurap_pwg.txt
regex_raw = <ls>CAURAP. ([0-9]+)
found 376 instances in kosha

2 not found -- comments in other publications.

----------------------------------------------------
pw  caurap
python generate_random_caurap.py 5 pwg temp_pw.txt index_caurap.txt check_caurap_pw.txt
regex_raw = <ls>CAURAP. ([0-9]+)
found 6 instances in kosha

All random cases checked.

----------------------------------------------------
pwkvn  caurap
python generate_random_caurap.py 5 pwkvn temp_pwkvn.txt index_caurap.txt check_caurap_pwkvn.txt
regex_raw = <ls>CAURAP. .A.. ([0-9]+)
found 16 instances in kosha


----------------------------------------------------
sch  caurap
python generate_random_caurap.py 5 sch temp_sch.txt index_caurap.txt check_caurap_sch.txt
regex_raw = <ls>Caurapṛ. ([0-9]+)
found 0 instances in kosha

----------------------------------------------------
mw  caurap
python generate_random_caurap.py 5 mw temp_mw.txt index_caurap.txt check_caurap_mw.txt
regex_raw = <ls>Caurap. ([0-9]+)
found 2 instances in kosha

1 checked, another not checked (this refers to Caurap. (A.))

repos updated:
csl-orig
csl-websanlexicon
csl-apidev
csl-pywork
csl-corrections

