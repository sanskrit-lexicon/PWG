
CHange markup to split lsrefs for nir or naigh
Using lsfix2

=================================
# the 'NIR.' references of pwg
python lsfix2.py pwgnir temp_pwg_1.txt splits_nir/lsfix2_pwg_1.txt

3152 lines written to splits_nir/lsfix2_pwg_1.txt
(True, 2) 2683
(None, 2) 102
('fixed', 2) 360
(False, 2) 7

# make changes to temp_pwg_1.txt, then rerun:
python lsfix2.py pwgnir temp_pwg_1.txt splits_nir/lsfix2_pwg_1.txt

3136 lines written to splits_nir/lsfix2_pwg_1.txt
(True, 2) 2712
(None, 2) 55
('fixed', 2) 373

The 'None' are in 3 parts:
--------------------
11 '<ls>NIR. S. '
29 '<ls>NIR. [IVXL]+'  link via app0
 3 '<ls n="NIR.">[XIVL]+'  link via app0
12 miscellany


=================================
# the 'NAIGH.' references of pwg
python lsfix2.py pwgnaigh temp_pwg_1.txt splits_naigh/lsfix2_pwg_1.txt

1399 lines written to splits_naigh/lsfix2_pwg_1.txt
(True, 2) 1337
('fixed', 2) 27
(False, 2) 3
(None, 2) 32

# Further edits of temp_pwg_1.txt to resolve False and None
# redo lsfix2

python lsfix2.py pwgnaigh temp_pwg_1.txt splits_naigh/lsfix2_pwg_1.txt

1390 lines written to splits_naigh/lsfix2_pwg_1.txt
(True, 2) 1361
('fixed', 2) 27
(None, 2) 2

Remaining None in pwg
284612	<ls>NAIGH. x.</ls>
112939	<ls>NAIGH. LVII.</ls>

======================================
# the 'NIR.' references of pw
python lsfix2.py pwnir temp_pw_1.txt splits_nir/lsfix2_pw_1.txt

106 lines written to splits_nir/lsfix2_pw_1.txt
(True, 2) 102
('fixed', 2) 2
(None, 2) 2

# correct the error(s) in temp_pw_1.txt
# rerurn lsfix2
python lsfix2.py pwnir temp_pw_1.txt splits_nir/lsfix2_pw_1.txt

105 lines written to splits_nir/lsfix2_pw_1.txt
(True, 2) 103
('fixed', 2) 2

All ok with NIR pw

======================================
# the 'NAIGH.' references of pw
python lsfix2.py pwnaigh temp_pw_1.txt splits_naigh/lsfix2_pw_1.txt

0 lines written to splits_naigh/lsfix2_pw_1.txt
(True, 2) 10

All ok with naigh pw

======================================
# the 'NIR.' references of pwkvn
python lsfix2.py pwkvnnir temp_pwkvn_0.txt splits_nir/lsfix2_pwkvn_0.txt

24 lines written to splits_nir/lsfix2_pwkvn_0.txt
(None, 2) 2
(True, 2) 22

cp temp_pwkvn_0.txt temp_pwkvn_1.txt

# Correct temp_pwkvn_1.txt for the 2 None
# rerun lsfix2 on temp_pwkvn_1

python lsfix2.py pwkvnnir temp_pwkvn_1.txt splits_nir/lsfix2_pwkvn_1.txt

23 lines written to splits_nir/lsfix2_pwkvn_1.txt
(True, 2) 23

All done with pwkvn, nir

======================================
# the 'NAIGH.' references of pwkvn
python lsfix2.py pwkvnnaigh temp_pwkvn_1.txt splits_naigh/lsfix2_pwkvn_1.txt

No examples

Done with pwkvn

======================================
# the 'Nir.' references of sch
python lsfix2.py schnir temp_sch_0.txt splits_nir/lsfix2_sch_0.txt

19 lines written to splits_nir/lsfix2_sch_0.txt
(True, 2) 16
('fixed', 2) 1
(None, 2) 2

cp temp_sch_0.txt temp_sch_1.txt

# Correct the 2 'None'
# rerun lsfix2 on temp_sch_1

python lsfix2.py schnir temp_sch_1.txt splits_nir/lsfix2_sch_1.txt

22 lines written to splits_nir/lsfix2_sch_1.txt
(True, 2) 21
('fixed', 2) 1

Done with Nir. sch

======================================
# the 'Nigh.' references of sch
python lsfix2.py schnaigh temp_sch_1.txt splits_naigh/lsfix2_sch_1.txt

2 lines written to splits_naigh/lsfix2_sch_1.txt
(True, 2) 1
(None, 2) 1

The 1 None example not changed. No link

16486 ः navAlAbu ः <ls>Nigh. Pr.</ls> : cannot find in link target

Done with Nigh. in sch

======================================
# the 'Nir.' references of mw
python lsfix2.py mwnir temp_mw_1.txt splits_nir/lsfix2_mw_1.txt

506 lines written to splits_nir/lsfix2_mw_1.txt
(None, 2) 506


lsfix2 does not handle mw since first parm is roman for mw.

473 <ls>Nir. [ivxl]+, [0-9]+\.?</ls>
  9 <ls n="Nir. [ivxl]+,">[0-9]+\.?</ls>
  9 <ls n="Nir.">[ivxl]+, [0-9]+\.?</ls>
  3 <ls>Nir. [ivxl]+, [0-9]+ f.</ls>
(+ 473 9 9 3) 494

There remain 12 'None' cases to examine and correct if possible
No changes made. These are all 1-parameter references
 8 <ls>Nir. [ivxl]+\.?</ls>
 4 <ls n="Nir.">[ivxl]+\.?</ls>

Done with Nir. mw

======================================
# the 'Naigh.' references of mw
python lsfix2.py mwnaigh temp_mw_1.txt splits_naigh/lsfix2_mw_1.txt

464 lines written to splits_naigh/lsfix2_mw_1.txt
(None, 2) 464

lsfix2 does not handle mw since first parm is roman for mw.

439 <ls>Naigh. [ivxl]+, [0-9]+\.?</ls>
  4 <ls n="Naigh. [ivxl]+,">[0-9]+\.?</ls>
 17 <ls n="Naigh.">[ivxl]+, [0-9]+\.?</ls>
  3 <ls>Naigh. [i]+\.?</ls>
One correction

Done with corrections for mw
======================================

**************************************
Get version 2 of pwg   
**************************************

cat splits_nir/lsfix2_pwg_1.txt splits_naigh/lsfix2_pwg_1.txt > lsfix2_pwg_1.txt

# apply the nir and naigh 'fixed' instances
python dict_replace2.py temp_pwg_1.txt lsfix2_pwg_1.txt temp_pwg_2.txt

4530 kept.
4530 lines read from lsfix2_pwg_1.txt
398 lines to change
apply_repls: 398 lines changed

-------------------------------
check validity of temp_pwg_2.txt

# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue167
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue167

-------------------------------
lsfix2 files for pwg, nir and naigh

python lsfix2.py pwgnir temp_pwg_2.txt splits_nir/lsfix2_pwg_2.txt

3703 lines written to splits_nir/lsfix2_pwg_2.txt
(True, 2) 3648  # compare 2683 
(None, 2) 55

python lsfix2.py pwgnaigh temp_pwg_2.txt splits_naigh/lsfix2_pwg_2.txt

1419 lines written to splits_naigh/lsfix2_pwg_2.txt
(True, 2) 1417  # compare 1337
(None, 2) 2

**************************************
Get version 2 of pw   
**************************************

cat splits_nir/lsfix2_pw_1.txt splits_naigh/lsfix2_pw_1.txt > lsfix2_pw_1.txt

# apply the nir and naigh 'fixed' instances
python dict_replace2.py temp_pw_1.txt lsfix2_pw_1.txt temp_pw_2.txt

115 lines read from lsfix2_pw_1.txt
2 lines to change
apply_repls: 2 lines changed


-------------------------------
check validity of temp_pw_2.txt

# remake xml from temp_pw_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue167
cp temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue167

-------------------------------
lsfix2 files for pw, nir and naigh

python lsfix2.py pwnir temp_pw_2.txt splits_nir/lsfix2_pw_2.txt

108 lines written to splits_nir/lsfix2_pw_2.txt
(True, 2) 108

python lsfix2.py pwnaigh temp_pw_2.txt splits_naigh/lsfix2_pw_2.txt

10 lines written to splits_naigh/lsfix2_pw_2.txt
(True, 2) 10

**************************************
Get version 2 of pwkvn 
**************************************

cat splits_nir/lsfix2_pwkvn_1.txt splits_naigh/lsfix2_pwkvn_1.txt > lsfix2_pwkvn_1.txt

# apply the nir and naigh 'fixed' instances
python dict_replace2.py temp_pwkvn_1.txt lsfix2_pwkvn_1.txt temp_pwkvn_2.txt

23 kept.
23 lines read from lsfix2_pwkvn_1.txt
0 lines to change
# so temp_pwkvn_1.txt == temp_pwkvn_2.txt
-------------------------------
check validity of temp_pwkvn_2.txt

# remake xml from temp_pwkvn_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue167
cp temp_pwkvn_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwkvn  ../../pwkvn
sh xmlchk_xampp.sh pwkvn
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue167

-------------------------------
# lsfix2 files for pwkvn, nir and naigh

python lsfix2.py pwkvnnir temp_pwkvn_2.txt splits_nir/lsfix2_pwkvn_2.txt

23 lines written to splits_nir/lsfix2_pwkvn_2.txt
(True, 2) 23


python lsfix2.py pwkvnnaigh temp_pwkvn_2.txt splits_naigh/lsfix2_pwkvn_2.txt

0 lines written to splits_naigh/lsfix2_pwkvn_2.txt


**************************************
Get version 2 of sch 
**************************************

cat splits_nir/lsfix2_sch_1.txt splits_naigh/lsfix2_sch_1.txt > lsfix2_sch_1.txt

# apply the nir and naigh 'fixed' instances
python dict_replace2.py temp_sch_1.txt lsfix2_sch_1.txt temp_sch_2.txt

24 lines read from lsfix2_sch_1.txt
1 lines to change
apply_repls: 1 lines changed

-------------------------------
check validity of temp_sch_2.txt

# remake xml from temp_sch_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue167
cp temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh sch  ../../sch
sh xmlchk_xampp.sh sch
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue167

-------------------------------
# lsfix2 files for sch, nir and naigh

python lsfix2.py schnir temp_sch_2.txt splits_nir/lsfix2_sch_2.txt

23 lines written to splits_nir/lsfix2_sch_2.txt
(True, 2) 23

python lsfix2.py schnaigh temp_sch_2.txt splits_naigh/lsfix2_sch_2.txt

(True, 2) 1
(None, 2) 1


**************************************
Install version 1 of mw   (no 'fixing')
**************************************


-------------------------------
check validity of temp_mw_1.txt

# remake xml from temp_mw_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue167
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue167

-------------------------------
# lsfix2 files for mw, nir and naigh
Not applicable for mw
