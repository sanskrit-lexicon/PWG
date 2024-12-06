11-26-2024.  Version below begun 11-30-2024

Ref: https://github.com/sanskrit-lexicon/PWG/issues/81
   BHĀGAVATAPURĀṆA link target

   standardization of pwg links for 'Bhāg. P.'


This directory:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue81

----
Start with pwg.txt from csl-orig at latest commit
  dcad583bad36280f82123bd07ddfd74be2f0505f


cd /c/xampp/htdocs/cologne/csl-orig
git show dcad583ba:v02/pwg/pwg.txt > /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue81/temp_pwg_0.txt


-----------------------------------------------
baseline: all links
python link_prelim2.py temp_pwg_0.txt link_prelim2_0.txt

19054 <ls>BHĀG. P..*?</ls>
 3102 <ls n="BHĀG. P..*?</ls>
22156 Total

22156 cases written to link_prelim2_0.txt

-----------------------------------------------
TODO: sch.txt revise markup.
Example:
 <ls>Bhāg. P.</ls> 11, 8, 31.

***********************************************
temp_pwg_0a.txt  manual cleanup
cp temp_pwg_0.txt temp_pwg_0a.txt

----- step1
29 matches for "None"
Remove all of these.

----- step2
<ls n="BHĀG. P.">[0-9]\.?  [space at end]
8 matches
---
old: <ls n="BHĀG. P.">2. 3.</ls> sg. {#kar#}
new: 2. 3. sg. {#kar#}

--- kaSa
old: <ls n="BHĀG. P.">3. 30,23.</ls>
new: <ls n="BHĀG. P.">3,30,23.</ls>

--- DA pc=3-0919 (bottom)
old: <ls n="BHĀG. P.">7. 8.</ls>
new: <ls n="BHĀG. P. 5,">7,8.</ls>

--- nizWa
old: <ls n="BHĀG. P.">3. 32,32.</ls>
new: <ls n="BHĀG. P.">3,32,32.</ls>

---
old: <ls n="BHĀG. P.">3. 16,33.</ls>
new: <ls n="BHĀG. P.">3,16,33.</ls>

---
old: <ls n="BHĀG. P.">8. act.</ls> 
new: <ls n="BHĀG. P. 5,22,">8.</ls> act.

--- pfTuka
old: <ls n="BHĀG. P.">8. 9. 80,14.</ls>
new: <ls n="BHĀG. P. 10,81,">8.</ls> <ls n="BHĀG. P. 10,81,">9.</ls> <ls n="BHĀG. P. 10,">80,14.</ls>

---
old: <ls n="BHĀG. P.">8. 26,7.</ls>
new: <ls n="BHĀG. P. 10,9,">8.</ls> n="BHĀG. P. 10,26,7.</ls>

----- step3
<ls n="BHĀG. P.">[0-9]\.?</ls>    27 cases

27 matches for "<ls n="BHĀG. P.">[0-9]\.?</ls>" in buffer: temp_pwg_0a.txt

 114872:old:<ls n="BHĀG. P.">7</ls> <is>Ṛṣi</is> im 3ten <is>Manvantara</is>
 114872:new:7 <is>Ṛṣi</is> im 3ten <is>Manvantara</is>

 115597:old:<ls n="BHĀG. P.">7</ls> <is>Ṛṣi</is> des Südens.
 115597:new:7 <is>Ṛṣi</is> des Südens.

 116246:old:<ls n="BHĀG. P.">2</ls>; vgl. unten u. — {#vi#}
 116246:new:2; vgl. unten u. — {#vi#}

 116247:old:<ls n="BHĀG. P.">7.</ls>
 116247:new:7.

 128924:old:<ls n="BHĀG. P.">4.</ls>
 128924:new:4.

 132712:old:<ls n="BHĀG. P.">3.</ls> {#ka#}) erklärt
 132712:new:3. {#ka#}) erklärt

 137964:old:<ls n="BHĀG. P.">5.</ls>) <ls>KUMĀRAS. 4,29.</ls> {#yastu tatkArayet — anyayA#}
 137964:new:5.) <ls>KUMĀRAS. 4,29.</ls> {#yastu tatkArayet — anyayA#}

 163191:old:<ls n="BHĀG. P.">8.</ls>
 163191:new:8.

 231365:old:<ls n="BHĀG. P.">3.</ls> {#acakAt#}
 231365:new:3. {#acakAt#}

 278639:old:<ls n="BHĀG. P.">4.</ls> und vgl.
 278639:new:4. und vgl.

 292676:old:<ls n="BHĀG. P.">7.</ls>
 292676:new:7.

 295657:old:<ls n="BHĀG. P.">5.</ls> {#vyasanezu ca sarvezu piteva Bavati duHKitaH . utsavezu ca sarvezu piteva parituzyati ..#}
 295657:new:<ls n="BHĀG. P. 1,5,">5.</ls> {#vyasanezu ca sarvezu piteva Bavati duHKitaH . utsavezu ca sarvezu piteva parituzyati ..#}

 335779:old:<ls n="BHĀG. P.">7.</ls> Dem nom. pr. vorangesetzt: {#°caRqamahAsena#}
 335779:new:<ls n="BHĀG. P. 3,1,">7.</ls> Dem nom. pr. vorangesetzt: {#°caRqamahAsena#}

 354894:old:<ls n="BHĀG. P.">6.</ls>
 354894:new:6.

 356183:old:<ls n="BHĀG. P.">9.</ls> <ls>RĀJA-TAR. 2,102.</ls> {#yAni tu puzpamUlaPalErudakena saMDIyante tAni ca BakzaRIyAni#}
 356183:new:<ls n="BHĀG. P. 4,7">9.</ls> <ls>RĀJA-TAR. 2,102.</ls> {#yAni tu puzpamUlaPalErudakena saMDIyante tAni ca BakzaRIyAni#}

 356680: old:<ls n="BHĀG. P.">10</ls> <is>Dhātu</is> werden zu denzuerst genannten
 356680: new:10 <is>Dhātu</is> werden zu denzuerst genannten

 356681:old:<ls n="BHĀG. P.">7</ls> noch {%Haare, Haut%} und {%Sehnen%} hinzugerechnet,
 356681:new:7 noch {%Haare, Haut%} und {%Sehnen%} hinzugerechnet,

 638021:old:<ls n="BHĀG. P.">1</ls>): {#mudA ramaRamanvItam — kartum#} {%mit Wonne zu erfüllen%}
 638021:new:1): {#mudA ramaRamanvItam — kartum#} {%mit Wonne zu erfüllen%}

 648274:old:<ls n="BHĀG. P.">6</ls>).
 648274:new:6).

 657655:old:<ls n="BHĀG. P.">8.</ls>
 657655:new:<ls n="BHĀG. P. 10,45">8.</ls>

 693791:old:<ls n="BHĀG. P.">2</ls>).
 693791:new:2).

 716054:old:<ls n="BHĀG. P.">2</ls>).
 716054:new:2).

 722547:old:<ls n="BHĀG. P.">4.</ls> Z. 4 {#aniBftakara#}
 722547:new:<ls n="BHĀG. P. 12,10,">4.</ls> Z. 4 {#aniBftakara#}

 729850:old:<ls n="BHĀG. P.">8.</ls>
 729850:new:<ls n="BHĀG. P. 5,26,">8.</ls>

 755956:old:<ls n="BHĀG. P.">3.</ls> <ls>PRAVARĀDHY.</ls> in <ls>Verz. d. B. H. 56,18. 60,36.</ls>
 755956:new:<ls n="BHĀG. P. 9,6,">3.</ls> <ls>PRAVARĀDHY.</ls> in <ls>Verz. d. B. H. 56,18. 60,36.</ls>

 796943:old:<ls n="BHĀG. P.">2</ls> aus <ls>SIDDH. K.</ls> zu <ls>P. 7,2,10.</ls> {#vakzyate, avakzyat#}
 796943:new:2 aus <ls>SIDDH. K.</ls> zu <ls>P. 7,2,10.</ls> {#vakzyate, avakzyat#}

 854687:old:<ls n="BHĀG. P.">6</ls> in der Unterschr. {#manasaH#}
 854687:new:6 in der Unterschr. {#manasaH#}

 896912:old:<ls n="BHĀG. P.">4.</ls> <ls>PAÑCAT. 63,15.</ls> <ls>VET. in LA. (III) 20,8.</ls> {#padByAm#}
 896912:new:<ls n="BHĀG. P. 5,10,">4.</ls> <ls>PAÑCAT. 63,15.</ls> <ls>VET. in LA. (III) 20,8.</ls> {#padByAm#}

----- step4
96 matches for '<ls n="BHĀG. P.">[0-9]+\.?</ls>'

----- step5
19 matches for '<ls n="BHĀG. P.">[0-9]+\.? '

----- step 6
110 matches for '<ls n="BHĀG. P.">[0-9]+,[0-9]+\.?

----- step 7
4 matches for <ls>BHĀG. P.)

----- step 8
<ls n="BHĀG. P.">16,6.</ls>
496 matches for '<ls n="BHĀG. P.">[0-9]+,[0-9]+\.?</ls>'
Too many to do manually!


temp_pwg_0a.txt finished

# check for errors in xml
sh redo_pwg.sh 0a
# ok!

python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_0a.txt change_0a.txt
551 changes written to change_0a.txt

-----------------------------------------------
We should now be able to 'expand' lses sequences
whose first element is 'complete' (i.e. no previous ls needs to be examined)

Example:
<ls>X 1,2,3. 4. 5,6,7. 8,9.</ls>
<ls n="X 1,2,">3. 4. 5,6,7. 8,9.</ls>
<ls n="X 1,">2,3. 4. 5,6,7. 8,9.</ls>

ls_expand_0a_todo.txt will contain ls where the expansion could not be done;
These may be 'corrected' by further changes to temp_pwg_0a.txt

# extract all 'BHĀG. P.' literary sources.
# each line of output has tab-delimited fields:
#  entryid (L) of entry
#  headword (k1) of entry
#  linenumber in pwg.txt
#  the ls element

python link_prelim2.py temp_pwg_0a.txt link_prelim2_0a.txt
19052 <ls>BHĀG. P..*?</ls>
 3114 <ls n="BHĀG. P..*?</ls>
22166 Total

python link_expand.py link_prelim2_0a.txt link_expand_0a.txt link_change_0a_todo.txt
test2 nok1=17186, ntodo1=0
test2 nok2=4399, ntodo2=0, nomatch2=581,
581 lines written to link_expand_0a_nomatch2.txt

python make_change1.py temp_pwg_0a.txt link_expand_0a.txt change_1.txt

python updateByLine.py temp_pwg_0a.txt change_1.txt temp_pwg_1.txt
4385 change transactions from change_1.txt

--------------------------
# 
python make_change1.py temp_pwg_1.txt link_change_0a_todo.txt tempchange_1atodo.txt
581 cases written to tempchange_1atodo.txt

python updateByLine.py temp_pwg_1.txt tempchange_1atodo.txt temp_pwg_1atodo.txt

Manual edit of temp_pwg_1atodo.txt 


sh redo_pwg.sh  1atodo
# ok
python link_prelim2.py temp_pwg_1atodo.txt temp_prelim2_1atodo.txt
19052 <ls>BHĀG. P..*?</ls>
11512 <ls n="BHĀG. P..*?</ls>
30564 Total

python link_expand.py temp_prelim2_1atodo.txt temp_link_expand_1atodo.txt temp_link_change_1atodo_todo.txt
30564 ALL
30461 STANDARD
00103 CANTDO

0 lines written to temp_link_expand_1atodo.txt  # as expected
103 lines written to temp_link_change_1atodo_todo.txt

--------------------
# check links against index for bhagp_bur
python check_bur.py temp_prelim2_1atodo.txt Burnouf.BhP.index.txt temp_check_bur.txt
18 links incompatible with index

# See readme_check_bur.txt

---------------------
# change_2.txt
python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_1atodo.txt change_2.txt
620 changes written to change_2.txt

# temp_pwg_2.txt
python updateByLine.py temp_pwg_1.txt change_2.txt temp_pwg_2.txt
620 change transactions from change_2.txt

diff temp_pwg_2.txt temp_pwg_1atodo.txt | wc -l
# 0 -- these two files are identical

--------------------------------------------
Summary

# summary by book order
python summary.py 1 temp_pwg_2.txt bhagp_standard_2.txt bhagp_nonstandard_2.txt
30461 cases written to bhagp_standard_2.txt
103 cases written to bhagp_nonstandard_2.txt

# summary by skandha, adhyaya, verse  # only standard
python summary.py 2 temp_pwg_2.txt bhagp_verse_2.txt

--------------------------------------------
Installation version 2
--------------------------------------------
# local installation
sh redo_pwg.sh 2

-----------------------------------
sync csl-orig to Github
(using temp_pwg_2.txt)
cd /c/xampp/htdocs/cologne/csl-orig

git add . # pwg.txt
git commit -m "PWG: standardization of links for 'Bhāg. P.'
Ref: https://github.com/sanskrit-lexicon/PWG/issues/81"
# 5257 lines changed.
git push

-----------------------------------
sync this PWG repo to github.
============================================================
12-06-2024
Andhrabharati found solutions for unsolved problems of readme_check_bur.txt.
AB's file: readme_check_bur---.Unsolved.Problems.txt

cp temp_pwg_2.txt temp_pwg_3.txt
Manual edit temp_pwg_3.txt

Process version 3

sh redo_pwg.sh  3

python link_prelim2.py temp_pwg_3.txt temp_prelim2_3.txt
19052 <ls>BHĀG. P..*?</ls>
11510 <ls n="BHĀG. P..*?</ls>
30562 Total

python link_expand.py temp_prelim2_3.txt temp_link_expand_3.txt temp_link_change_3_todo.txt
30562 ALL
30459 STANDARD
00103 CANTDO
103 lines written to temp_link_change_3_todo.txt

python check_bur.py temp_prelim2_3.txt Burnouf.BhP.index.txt temp_check_bur.txt
0 links incompatible with index

-----------------------------
change file
python diff_to_changes_dict.py temp_pwg_2.txt temp_pwg_3.txt change_3.txt
19 changes written to change_3.txt

-----------------------------
pwg_printchange.txt  gathers the print changes
from readme_check_bur.txt and readme_check_bur---.Unsolved.Problems.txt

Add these to
 /c/xampp/htdocs/cologne/csl-corrections/dictionaries/pwg/pwg_printchange.txt

----------------------------
prepare summaries for version 3

# summary by book order
python summary.py 1 temp_pwg_3.txt bhagp_standard_3.txt bhagp_nonstandard_3.txt
30459 cases written to bhagp_standard_3.txt
103 cases written to bhagp_nonstandard_3.txt

# summary by skandha, adhyaya, verse  # only standard
python summary.py 2 temp_pwg_3.txt bhagp_verse_3.txt
30562 instances of ls
10493 cases written to bhagp_verse_3.txt


----------------------------
ready to install
--------------------------------------------
Installation version 3
--------------------------------------------
# local installation
sh redo_pwg.sh 3

-----------------------------------
sync csl-orig to Github
(using temp_pwg_3.txt)
cd /c/xampp/htdocs/cologne/csl-orig

git add . # pwg.txt
git commit -m "PWG: standardization of links for 'Bhāg. P.', version 3 
Ref: https://github.com/sanskrit-lexicon/PWG/issues/81"
# 19 insertions(+), 19 deletions(-)
git push

-----------------------------------
sync csl-corrections to Github
cd /c/xampp/htdocs/cologne/csl-corrections/
git add . # dictionaries/pwg/pwg_printchange.txt
git commit -m "PWG: print changes
Ref: https://github.com/sanskrit-lexicon/PWG/issues/81"

git push

-----------------------------------
Sync Cologne server to github
1. csl-orig repo
2. csl-pywork/v02  pwg  make displays
3. csl-corrections

-----------------------------------
sync this PWG repo to github.

-----------------------------------------------------------------
sync to github (minor correction to temp_pwg_3.txt for sarj)
-----------------------------------
sh redo_pwg.sh 3

sync csl-orig to Github
(using temp_pwg_3.txt)
cd /c/xampp/htdocs/cologne/csl-orig

git add . # pwg.txt
git commit -m "PWG:sarj  Revise previous correction.
Ref: https://github.com/sanskrit-lexicon/PWG/issues/81"
# 1 insertions(+), 1 deletions(-)
git push

-----------------------------------
sync csl-corrections to Github
cd /c/xampp/htdocs/cologne/csl-corrections/
git add . # dictionaries/pwg/pwg_printchange.txt
git commit -m "PWG: print change revision under sarj.
Ref: https://github.com/sanskrit-lexicon/PWG/issues/81"

git push

-----------------------------------
Sync Cologne server to github
1. csl-orig repo
2. csl-pywork/v02  pwg  make displays
3. csl-corrections

-----------------------------------
sync this PWG repo to github.



