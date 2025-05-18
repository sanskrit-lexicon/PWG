

----------------------------------------
# get temporary local copy of dictionaries for checking
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt


pwgbib_input.txt
1.202	MĀLAV.	Mālav.	*MĀLAV. = MĀLAVIKĀGNIMITRA, ed. TULLBERG (GILD. Bibl. 209).
1.202a	MĀLAV. ed. Bomb.	Mālav ed. Bomb.	 MĀLAVIKĀGNIMITRA, Bombay edition [Cologne Addition]
pwbib_input.txt
1181	MĀLAV.	Mālav.	MĀLAVIKĀGNIMITRA, Ausg. von TULLIBERG. 
pwkvn_input.txt
1181	MĀLAV.	Mālav.	MĀLAVIKĀGNIMITRA, Ausg. von TULLIBERG. 
schauth/tooltip.txt
Mālav.	(PW) MĀLAVIKĀGNIMITRA, Ausg. von TULLIBERG. 
Mālavik.	(CSL) MĀLAVIKĀGNIMITRA, Ausg. von TULLIBERG. 
mwauth/tooltip.txt
05:06	Mālav.	Mālavikāgnimitra	Title

85 matches for "<ls>Mālav\. " in buffer: temp_mw.txt
80 matches for "<ls>Mālav\. [iv]+, *[0-9]+"
  Example <ls>Mālav. ii, 26/27</ls>  cArutA  'between' veses 26 and 27 epage 36
1 match for "<ls>Mālav\. [0-9]+" in buffer: temp_mw.txt
   <ls>Mālav. 13/14</ls>  pIWamarda
=====================================================

PRELIMINARY MANUAL CHECK for pwg

modify generate_random.py as needed:
 Only 1-parameter example understood.
 
python generate_random.py 5 pwg1 temp_pwg.txt index.txt check_pwg1_man.txt
regex_raw = <ls>MĀLAV. ([0-9]+)[^0-9,]
found 469 instances in kosha

5 written to check_pwg1_man.txt

One NOT FOUND.

--- Do another small batch


End of preliminary manual check.


1056 matches in 1055 lines for "<ls>MĀLAV. " in buffer: temp_pwg.txt
2-parameter
575 matches for "<ls>MĀLAV. [0-9]+,[0-9]+" in buffer: temp_pwg.txt

1-parameter
469 matches for "<ls>MĀLAV. [0-9]+[^0-9,]" in buffer: temp_pwg.txt

REST OF THIS README NOT YET PROCESSED !

=====================================================
Checks for all dictionaries after basicadjust updated.

edit generate_random.py
  function get_dict_regex:
      make consistent with basicadjust.php; see
     readme_websanlexicon.txt
  function get_dict_key
  function set_pagerec_key
----------------------------------------------------
pwg1 1 parameter (verse)
python generate_random.py 5 pwg1 temp_pwg.txt index.txt check_pwg1.txt
regex_raw = <ls>MĀLAV. ([0-9]+)[^0-9,]
found 469 instances in kosha

All in this random sample checked.

----------------------------------------------------
pwg2 2 parameters (ipage, linenumber)
python generate_random.py 5 pwg2 temp_pwg.txt index.txt check_pwg2.txt
regex_raw = <ls>MĀLAV. ([0-9]+),([0-9]+)
found 575 instances in kosha

All in this random sample checked.

-----------------------------------
pw1 1 parameter (verse)
python generate_random.py 5 pw1 temp_pw.txt index.txt check_pw1.txt
regex_raw = <ls>MĀLAV. ([0-9]+)[^0-9,]
found 36 instances in kosha

All in this random sample checked, after a print change

----------------------------------------------------
pw2 2 parameters (ipage, linenumber)
python generate_random.py 5 pw2 temp_pw.txt index.txt check_pw2.txt
regex_raw = <ls>MĀLAV. ([0-9]+),([0-9]+)
found 40 instances in kosha

All in this random sample checked.

-----------------------------------
pwkvn1 1 parameter (verse)
python generate_random.py 5 pwkvn1 temp_pwkvn.txt index.txt check_pwkvn1.txt
regex_raw = <ls>MĀLAV. ([0-9]+)[^0-9,]
found 36 instances in kosha

All in this random sample checked

----------------------------------------------------
pwkvn2 2 parameters (ipage, linenumber)
python generate_random.py 5 pwkvn2 temp_pwkvn.txt index.txt check_pwkvn2.txt
regex_raw = <ls>MĀLAV. ([0-9]+),([0-9]+)
found 2 instances in kosha
found 2 distinct in kosha
WARNING Can only get 2 examples

All in this random sample checked.

-----------------------------------
sch1 1 parameter (verse)
python generate_random.py 5 sch1 temp_sch.txt index.txt check_sch1.txt
regex_raw = <ls>Mālav. ([0-9]+)[^0-9,]
found 5 instances in kosha
found 4 distinct in kosha
WARNING Can only get 4 examples

All in this random sample checked

----------------------------------------------------
sch2 2 parameters (ipage, linenumber)
python generate_random.py 5 sch2 temp_sch.txt index.txt check_sch2.txt
regex_raw = <ls>Mālav. ([0-9]+),([0-9]+)
found 2 instances in kosha
found 2 distinct in kosha
WARNING Can only get 2 examples


All in this random sample checked.

-----------------------------------
mw1 1 parameter (verse)
python generate_random.py 5 mw1 temp_mw.txt index.txt check_mw1.txt
regex_raw = <ls>Mālav. ([0-9]+)[^0-9,]
found 0 instances in kosha

No examples to check.

----------------------------------------------------
mw2 2 parameters (anka_roman, verse_in_anka)
python generate_random_mw.py 4 mw2 temp_mw.txt index.txt check_mw2.txt
regex_raw = <ls>Mālav. ([vix]+), *([0-9]+)
found 81 instances in kosha

All in this random sample checked.
  One ? (Calika) may be a prakrit variant
mw2 2 parameters (anka_roman, verse_in_anka)

-----------------------------------
Examine all mw2
85 matches for "<ls>Mālav. [iv]" in buffer: temp_mw.txt
81 matches for "<ls>Mālav. [iv]+, *[0-9]" in buffer: temp_mw.txt

python generate_random_mw.py ALL mw2 temp_mw.txt index.txt check_mw2_all.txt


---------------------------------
All (almost) checks favorable.
Ready to install:
 csl-websanlexicon
 csl-apidev
