

----------------------------------------
# get temporary local copy of dictionaries for checking
#  meghadUta links

cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt


kosha abbreviations for meghaduta
PWG: MEGH.
PW:  MEGH.
PWKVN: MEGH.
sch: Megh.
mw:  Megh.

kosha abbreviations for
PWG: ŚṚṄGĀRAT.
PW:  ŚṚṄGĀRAT.  none
PWKVN: ŚṚṄGĀRAT. none
sch: Śṛṅgārat.  none
mw:  Śṛṅgārat. none numbered
mw:  Śṛṅgār.  1 instance with verse.

*************************
`35 matches for "<ls>RUDRAṬA, ŚṚṄGĀRAT. [0-9]+,[0-9]+" in buffer: temp_pw.txt`
(and one more `<ls n="RUDRAṬA, ŚṚṄGĀRAT. 3,">82</ls>`).

in PW, PWKVN aSruleSa MEGH. 103   NOT FOUND

These are all in pwkvn.txt !

pwbib_input.txt has no abbreviation tooltip for `RUDRAṬA, ŚṚṄGĀRAT.`

There are no `<ls>ŚṚṄGĀRAT. </ls>`.
***********************
one parameter
=====================================================

PRELIMINARY MANUAL CHECK for pwg MEGH.

python generate_random_megha.py 5 pwg temp_pwg.txt index_megha.txt check_pwg_megha_man.txt
regex_raw = <ls>KUMĀRAS. ([0-9]+),([0-9]+)
found 2451 instances in kosha

5 written to check_pwg_man.txt

These 5 random checks OK.

End of preliminary manual check for MEGH. in pwg

=====================================================
Checks for all dictionaries after basicadjust updated.

edit generate_random_megha.py
  function get_dict_regex:
      make consistent with basicadjust.php; see
     readme_websanlexicon.txt
  function get_dict_key
  function set_pagerec_key
----------------------------------------------------
pwg
python generate_random_megha.py 5 pwg temp_pwg.txt index_megha.txt check_megha_pwg.txt
regex_raw = <ls>MEGH. ([0-9]+)
found 1917 instances in kosha

All in this random sample checked.  BrAjin  is interesting.

----------------------------------------------------
pw
python generate_random_megha.py 5 pw temp_pw.txt index_megha.txt check_megha_pw.txt
found 119 instances in kosha
found 69 distinct in kosha

All in this random sample checked, after corrections to pw.txt

----------------------------------------------------
pwkvn
python generate_random_megha.py 5 pwkvn temp_pwkvn.txt index_megha.txt check_megha_pwkvn.txt
regex_raw = <ls>MEGH. ([0-9]+)
found 4 instances in kosha

Two NOT FOUND, but they are commentary references

----------------------------------------------------
sch
python generate_random_megha.py 5 sch temp_sch.txt index_megha.txt check_megha_sch.txt
regex_raw = <ls>Megh. ([0-9]+)
found 5 instances in kosha

3 NOT FOUND (2 commentary refs, one different edition).

----------------------------------------------------
---------------------------------
All (almost) checks favorable.
Ready to install:
 csl-websanlexicon
 csl-apidev
