
=================================================
activating links to ramayanabom app1
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/ramayanabom
local urls:
localhost/sanskrit-lexicon-scans/ramayanabom/app1/?N,N

Github url:
https://sanskrit-lexicon-scans.github.io/ramayanabom/app1/?N,N

https://sanskrit-lexicon-scans.github.io/ramayanabom/
shows README.md  (with markdown converted to html)


# -------------------
# edit local csl-websanlexicon ... basicadjust.php

 /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php
# edit function ls_callback_pwg_href
---- links from pwg, pw, pwkvn
ramayanabom  app1
# only for kanda = 7 (uttara kanda)
<ls>R. 7,([0-9]+),([0-9]+),([0-9])   # prakshipta
<ls>R. 7,([0-9]+),([0-9]+)  # normal


---- links from sch
ramayanabom  app1
same as pwg

---- links from mw
ramayanabom  app1
<ls>R. ([ivx]+),([0-9]+)  


cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
sh generate_web.sh pwg  ../../pwg
sh generate_web.sh pw  ../../pw
sh generate_web.sh pwkvn  ../../pwkvn
sh generate_web.sh sch  ../../sch

sh apidev_copy.sh  # simple search gets new basicadjust.php


===================================
checks of links for dictionaries

# get temporary local copy of pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt


----------------------------------------
checks for "R. ed. Bomb.
Make misc checks between pwg , the pdf and index

268 matches for "<ls>R. ed. Bomb. " in buffer: temp_pwg.txt

'pwg3':r'<ls>R. ed. Bomb. ([0-9]+),([0-9]+),([0-9]+)[^,]
python generate_random.py 5 pwg3 temp_pwg.txt index.js check_pwg3.txt
found 268 instances in kosha
5 written to check_pwg3.txt

one NOT FOUND hw = sAmaYjasya. Correction: found sAmaMjasya in commentary

# Check another 5 from pwg
python generate_random.py 5 pwg3 temp_pwg.txt index.js check_pwg3_a.txt

All are ok.

----------------------------------
# get temporary local copy of pw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt

555 matches in 554 lines for "<ls>R. ed. Bomb. " in buffer: temp_pw.txt

Random check of links:

'pw3':r'<ls>R. ed. Bomb. ([0-9]+),([0-9]+),([0-9]+)[^,]
python generate_random.py 5 pw3 temp_pw.txt index.js check_pw3.txt
found 549 instances in kosha
5 written to check_pw3.txt

All checks ok  Note 4 corrections to pw.txt.
----------------------------------
# get temporary local copy of pwkvn.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn.txt

339 matches in 335 lines for "<ls>R. ed. Bomb. " in buffer: temp_pwkvn.txt

Random check of links:

'pwkvn3':r'<ls>R. ed. Bomb. ([0-9]+),([0-9]+),([0-9]+)[^,]

python generate_random.py 5 pwkvn3 temp_pwkvn.txt index.js check_pwkvn3.txt
found 338 instances in kosha
5 written to check_pwkvn3.txt


All checks  ok

----------------------------------------
# get temporary local copy of sch.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch.txt

335 matches in 330 lines for "<ls>R. ed. Bomb. " in buffer: temp_sch.txt

Random check of links:

'sch3':r'<ls>R. ed. Bomb. ([0-9]+),([0-9]+),([0-9]+)[^,]

python generate_random.py 5 sch3 temp_sch.txt index.js check_sch3.txt
found 333 instances in kosha
5 written to check_sch3.txt

All checks OK

-----------------------------
# get temporary local copy of mw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt

2 matches for "<ls>R. ed. Bomb. " in buffer: temp_mw.txt


'mw':r'<ls>R. ed. Bomb. ([ivx]+), *([0-9]+), *([0-9]+)
python generate_random.py 5 mw3 temp_mw.txt index.js check_mw3.txt
found 2 instances in kosha
2 written to check_mw3.txt

1 is OK.  1 is uncertain:
 key (1, 61, 7): 1	61	4	17	1204
L= 13487, hw= aByAhf, pc=78,1
 

END OF CHECKS for R. ed. Bomb. All ok.

========================================================
Ref: https://github.com/sanskrit-lexicon/PWK/issues/83#issuecomment-1030888319_
  RĀMĀYAṆA. The 1st and 2nd Kāṇḍa after the output of SCHLEGEL, 
  the 3rd--6th after that of GORRESIO, 
  the 7th after the bomb. Edition unless another edition is explicitly mentioned. 
  A number in parentheses refers to ed. Bomb.
---------------------------
checks for "R. 7,N,N,N" pwg

182 matches for "<ls>R. [0-9]+,[0-9]+,[0-9]+,[0-9]+" in buffer: temp_pwg.txt
The first parameter is always 7. Proof:
182 matches for "<ls>R. 7,[0-9]+,[0-9]+,[0-9]+" in buffer: temp_pwg.txt

'pwg4':r'<ls>R. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)'
python generate_random.py 5 pwg4 temp_pwg.txt index.js check_pwg4.txt
found 182 instances in kosha
5 written to check_pwg4.txt

All are ok.

---------------------------
checks for "R. 7,N,N,N" pw

5 matches for "<ls>R. 7,[0-9]+,[0-9]+,[0-9]+" in buffer: temp_pw.txt
8 matches for "<ls>R. [0-9]+,[0-9]+,[0-9]+,[0-9]+" in buffer: temp_pw.txt
 3 cases where kanda is not 7!

'pw4':r'<ls>R. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)'
python generate_random.py 10 pw4 temp_pw.txt index.js check_pw4.txt
found 8 instances in kosha
5 written to check_pw4.txt


All are ok, after the following 4 corrections to pw.txt.
Note csl-orig is updated

corrections to temp_pw.txt

----
<L>32414<pc>2-123-b<k1>kzAnta
old: <ls>R. 1,34,32,33</ls>
new: <ls>R. 1,34,32.</ls> <ls n="R. 1,34,33</ls>
----
<L>67796<pc>4-095-a<k1>punaHpratinivartana
old: <ls>R. 5,1,8,1</ls>
new: <ls>R. 5,1,81</ls>
---
<L>7329<pc>1-086-a<k1>aBijYAna
old: <ls>R. 5,68,1,4</ls>
new: <ls>R. 5,68,1.</ls> <ls n="R. 5,68,">43</ls>
---
<L>221287<pc>7-376-a<k1>vIRApaRavatURavant
old: <ls>R. 7,23,1,39</ls>
new: <ls>R. 7,23,4,39</ls

cp temp_pw.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw

----------------------------------
---------------------------
checks for "R. 7,N,N,N" pkwvn

3 matches for "<ls>R. 7,[0-9]+,[0-9]+,[0-9]+" in buffer: temp_pwkvn.txt

'pwkvn4':r'<ls>R. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)'
python generate_random.py 10 pwkvn4 temp_pwkvn.txt index.js check_pwkvn4.txt
found 3 instances in kosha
3 written to check_pkwvn4.txt

All checks  ok after corrections

correction to pwkvn
<L>21287<pc>7-376-a<k1>vIRApaRavatURavant
old: <ls>R. 7,23,1,39</ls>
new: <ls>R. 7,23,4,39</ls>

cp temp_pwkvn.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwkvn  ../../pwkvn

----------------------------------------
checks for "R. 7,N,N,N" sch

0 matches for "<ls>R. [0-9]+,[0-9]+,[0-9]+,[0-9]+" in buffer: temp_sch.txt

Nothing to check
# 'sch4':r'<ls>R. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)'
# python generate_random.py 10 sch4 temp_sch.txt index.js check_sch4.txt

All checks OK

----------------------------------------
checks for "R. 7,N,N,N" mw

3 matches for "<ls>R. vii, *[0-9]+, *[0-9]+, [0-9]+" in buffer: temp_mw.txt

'mw4':r'<ls>R. (vii), *([0-9]+), *([0-9]+), *([0-9]+)'
python generate_random.py 10 mw4 temp_mw.txt index.js check_mw4.txt
found 3 instances in kosha

All checks OK

Possible MW print error:
key (3, 20, 17, 18): no index for (3,20,17,18)
L= 91516, hw= dAkzeyI, pc=475,1  

END OF CHECKS for R. N,N,N,N
All ok.

========================================================
Ref: https://github.com/sanskrit-lexicon/PWK/issues/83#issuecomment-1030888319_
  RĀMĀYAṆA. The 1st and 2nd Kāṇḍa after the output of SCHLEGEL, 
  the 3rd--6th after that of GORRESIO, 
  the 7th after the bomb. Edition unless another edition is explicitly mentioned. 
  A number in parentheses refers to ed. Bomb.
---------------------------
checks for "R. 7,N,N" pwg

1098 matches for "<ls>R. 7,[0-9]+,[0-9]+[^,]" in buffer: temp_pwg.txt

'pwg37':r'<ls>R. (7),([0-9]+),([0-9]+),[^,]'
python generate_random.py 5 pwg37 temp_pwg.txt index.js check_pwg37.txt
found 1098 instances in kosha
5 written to check_pwg37.txt

All are ok.

---------------------------
checks for "R. 7,N,N" pw

54 matches for "<ls>R. 7+,[0-9]+,[0-9]+[^,]" in buffer: temp_pw.txt

'pw37':r'<ls>R. (7),([0-9]+),([0-9]+),[^,]'
python generate_random.py 5 pw37 temp_pw.txt index.js check_pw37.txt
found 54 instances in kosha
5 written to check_pw37.txt

All are ok.

---------------------------
checks for "R. 7,N,N" pwkvn

15 matches for "<ls>R. 7+,[0-9]+,[0-9]+[^,]" in buffer: temp_pwkvn.txt

'pwkvn37':r'<ls>R. (7),([0-9]+),([0-9]+),[^,]'
python generate_random.py 5 pwkvn37 temp_pwkvn.txt index.js check_pwkvn37.txt
found 15 instances in kosha
5 written to check_pwkvn37.txt

All are ok.

---------------------------
checks for "R. 7,N,N" sch

19 matches for "<ls>R. 7+,[0-9]+,[0-9]+[^,]" in buffer: temp_sch.txt

'sch37':r'<ls>R. (7),([0-9]+),([0-9]+),[^,]'
python generate_random.py 5 sch37 temp_sch.txt index.js check_sch37.txt
found 15 instances in kosha
5 written to check_sch37.txt

All are ok.
One is questionable:
key (7, 84, 15): 7	84	15	18	3754
L= 19846, hw= prItisaMgoya, pc=273-3
check: ? prItisaMyoga  found.   Is prItisaMgoya a print error in sch?


---------------------------
checks for "R. 7,N,N" mw

122 matches for "<ls>R. vii, *[0-9]+, *[0-9]+[^,]" in buffer: temp_mw.txt

'mw37':r'<ls>R. (vii), *([0-9]+), *([0-9]+),[^,]'
python generate_random.py 5 mw37 temp_mw.txt index.js check_mw37.txt
found 122 instances in kosha
5 written to check_mw37.txt

All are ok.

END OF CHECKS for R. 7,N,N

===================================

This step finished locally.

===================================

Push csl-websanlexicon, csl-apidev to github
also csl-orig

===================================

