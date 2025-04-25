

----------------------------------------
# get temporary local copy of dictionaries for checking
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt

=====================================================
preliminary manual checks (before basicadjust updated)

In pwgbib_input.txt there are 3 forms of reference:
RĀJA-TAR.  = RĀJATARAṄGIṆĪ, ed. TROYER (GILD. Bibl. 148)
                für die 6&#13;&#10;ersten Taram̃ga's;
		für die folgenden die Calc. Ausg. (GILD. Bibl. 147).
RĀJA-TARAṄGIṆĪ  = RĀJATARAṄGIṆĪ ? [Cologne Addition]
RĀJA-TAR. ed. Calc. = RĀJATARAṄGIṆĪ,  Calc. Ausg. (GILD. Bibl. 147). [Cologne Addition]

Refer to these as number 1,2,3

7123 matches in 7118 lines for "<ls>RĀJA-TAR. " in buffer: temp_pwg.txt

1 match for "<ls>RĀJA-TARAṄGIṆĪ" in buffer: temp_pwg.txt
   <ls>RĀJA-TARAṄGIṆĪ</ls> (titular)

11 matches for "<ls>RĀJA-TAR. ed. Calc." in buffer: temp_pwg.txt

The checks will be made for "<ls>RĀJA-TAR. " in pwg, pw, pwkvn

-----------------------------------------------------
PRELIMINARY MANUAL CHECK 
python generate_random.py 5 pwg temp_pwg.txt index.txt check_pwg_man.txt
regex_raw = <ls>RĀJA-TAR. ([0-9]+),([0-9]+)
found 7051 instances in kosha
found 2969 distinct in kosha
5 written to check_pwg_man.txt

These 5 random checks OK.

End of preliminary manual check.

=====================================================
Checks for all dictionaries after basicadjust updated.

----------------------------------------------------
First, pwg
From pwgbib_input.txt

7130 matches in 7125 lines for "<ls>RĀJA-TAR\."

1 match for "<ls>RĀJA-TARAṄGIṆĪ"
11 matches for "<ls>RĀJA-TAR. ed. Calc."

The check is based on "<ls>RĀJA-TAR\."

python generate_random.py 5 pwg temp_pwg.txt index.txt check_pwg.txt
regex_raw = <ls>RĀJA-TAR. ([0-9]+),([0-9]+)
found 7051 instances in kosha

4/5 in this random sample checked.
  The one NOT FOUND:
  key (1, 162): 29	1	155b	164	18
  L= 35481, hw= drohin, pc=3-0817


-----------------------------------
Random checks between pw , the pdf and index
In this cse the PW abbreviation differs from the PWG abbreviation

444 matches in 442 lines for "<ls>RĀJAT\. [0-9] in buffer: temp_pw.txt
1 match for "<ls>RĀJAT. ed. Calc." in buffer: temp_pw.txt

1231	RĀJAT.	Rājat.	RĀJATARAṂGIṆĪ. Die 6 ersten Bücher nach der Ausg. von TROYER. Die Beträge aus dem 7ten und 8ten Buche von KERN. 
X066	RĀJAT. ed. Calc.	Rājat. ed. Calc.	[unknown literary source]

python generate_random.py 5 pw temp_pw.txt index.txt check_pw.txt
regex_raw = <ls>RĀJAT. ([0-9]+),([0-9]+)
found 438 instances in kosha

All in this random sample checked.

-----------------------------------
Random checks between pwkvn , the pdf and index

python generate_random.py 5 pwkvn temp_pwkvn.txt index.txt check_pwkvn.txt
regex_raw = <ls>RĀJAT. ([0-9]+),([0-9]+)
found 49 instances in kosha

All in this random sample checked.

-----------------------------------
Random checks between sch , the pdf and index

python generate_random.py 5 sch temp_sch.txt index.txt check_sch.txt
regex_raw = <ls>Rājat. ([0-9]+),([0-9]+)
found 73 instances in kosha

All in this random sample checked.

-----------------------------------
Random checks between mw , the pdf and index

Only 1 form seen
python generate_random.py 5 mw temp_mw.txt index.txt check_mw.txt
regex_raw = <ls>Rājat. ([vix]+), *([0-9]+)
found 513 instances in kosha

All in this random sample checked.

NOTE:
key (1, 46): 17	1	43b	50	6
L= 77923, hw= jalaDiraSana, pc=415,1
check: ok jalaDirasanA   MW typo in copying from PW ?

---------------------------------
All checks favorable (with one exception - see NOT FOUND above)
Ready to install:
 csl-websanlexicon
 csl-apidev
