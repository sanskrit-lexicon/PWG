09-08-2024 begin

Ref: https://github.com/sanskrit-lexicon/PWG/issues/74
   standardization of pwg links for M. (MAnava DharmashAstra


This directory:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue74

----
Start with pwg.txt from csl-orig at commit
  afabed1faabbd2696008d8837b521b966f7f7eb7

cd /c/xampp/htdocs/cologne/csl-orig
git show afabed1fa:v02/pwg/pwg.txt > /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue74/temp_pwg_0.txt


***********************************************
improve markup pwg
-----------------------------------------------
Examine temp_pwg_0.txt
17188 matches in 15341 lines for "\bM\." in buffer: temp_pwg_0.txt
Emacs: occur 
  Save *OCCUR* buffer to M_all_0.txt

# All "M." link references
Regex matches to one of these two regexes:
 regex1raw = r'<ls>M\..*?<?ls>'
 regex2raw = r'<ls n="M\..*?">.*?</ls>'
Then sort the matches.

python linksort.py 1 temp_pwg_0.txt linksort1_0.txt

1149413 lines read from temp_pwg_0.txt
122736 entries found
16891 cases written to linksort1_0.txt

# Non-standard links.
Standard:
<ls>M\. [0-9]+, [0-9]+\.?</ls>
<ls n="M\. [0-9]+,">[0-9]+\.?</ls>
<ls n="M\.">([0-9]+), ([0-9])+\.?</ls>
<ls>M\.</ls>
<ls>M\. ([0-9]+), ([0-9]+)\. fgg?\.</ls>
<ls n="M\. ([0-9]+),">([0-9])+\. fgg?\.</ls>
<ls n="M\.">([0-9]+), ([0-9])+\. fgg?\.</ls>

# show the standard links, sorted with subcounts of multiplicity
python linksort.py 2 temp_pwg_0.txt linksort2_0.txt

1149413 lines read from temp_pwg_0.txt
122736 entries found
13979 total number of 'regular' links
2607 cases written to linksort2_0.txt

Note: 
First:
  (0,0) (25)  No parameters: <ls>M\.</ls>
    A few: <ls>M.</ls> <ls>MÜLLER</ls>  to be recoded
  (1,1) (3)
Last few
  124,251 (3)
  148,135 (1)
  190,90 (1)
  561,7 (1)   IS this correct?


------------------------------------------------
Begin work to 'correct' the non-standard links
(- 16891 13979) 2912 non-standard.
First step is to list the non-standard:

python linksort.py 3 temp_pwg_0.txt linksort3_0.txt

1149413 lines read from temp_pwg_0.txt
122736 entries found
1920 non-standard of type1
992 non-standard of type2
2912 cases written to linksort3_0.txt

---- 
------------------------------------------------
 for each line of linksort3, if possible generate an
   array of links, and write the original line and these links.
 Some link-rewrites will fail.
 Successes written to the ok file, others written to the todo file

python link_change.py linksort3_0.txt link_change_0_ok.txt link_change_0_todo.txt

2104 marked OK written to link_change_0_ok.txt
808 marked TODO written to link_change_0_todo.txt

(+ 2104 806) = 2910  Should be 2912!  

This analysis also identified several 'test2 wrong form' messages, such as
 <ls>M.).</ls>.
Put these into link_change_0_wrongform.txt for reference.
There are 23 such items.

Let's correct this wrong forms manually
-------------------
cp temp_pwg_0.txt temp_pwg_0a.txt
Manual correct temp_pwg_0a.txt, with notes in the ..wrongform.. file.

-------------------
rerun several programs using version 0a

# All "M." link references
python linksort.py 1 temp_pwg_0a.txt linksort1_0a.txt
16897 cases written to linksort1_0a.txt

# show the standard links, sorted with subcounts of multiplicity
python linksort.py 2 temp_pwg_0a.txt linksort2_0a.txt
14010 total number of 'regular' links
2607 cases written to linksort2_0a.txt

# Begin work to 'correct' the non-standard links
python linksort.py 3 temp_pwg_0a.txt linksort3_0a.txt
1911 non-standard of type1
976 non-standard of type2
2887 cases written to linksort3_0a.txt

#  for each line of linksort3, if possible generate an
   array of links, and write the original line and these links.
 Some link-rewrites will fail.
 Successes written to the ok file, others written to the todo file

python link_change.py linksort3_0a.txt link_change_0a_ok.txt link_change_0a_todo.txt

2104 marked OK written to link_change_0a_ok.txt
783 marked TODO written to link_change_0a_todo.txt

NOTE: there are no 'test2 wrong form' messages using version 0a!

------------------------------------------------
change_1.txt
generate a standard change file

python make_change.py temp_pwg_0a.txt link_change_0a_ok.txt change_1.txt
2100 lines changes
2104 count of replacements
2100 cases written to change_1.txt

Note: Why 2104 instead of 2100?

# apply the changes: temp_pwg_1.txt
python updateByLine.py temp_pwg_0a.txt change_1.txt temp_pwg_1.txt

2100 change transactions from change_1.txt
2100 of type new

----
# regenerate local displays from temp_pwg_1
# This to check xml validity.

cp temp_pwg_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok  No problems noticed
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue74

-------------------------------------------------------
-------------------------------------------------------
What about the items in link_change_0a_todo.txt ?

python linksort.py 4 temp_pwg_1.txt linksort4_1.txt
816 non-standard records
816 cases written to linksort4_1.txt

Not sure why there are 816 here -- expected 783 (as records in 
link_change_0a_todo.txt).
Structure of linksort4_1.txt record.
3 tab-delimited fields:
1. ls elt (M.) which is non-standard
2. the first parameter of previous ls (M) in the entry (or -1 if no 
3. previous ls (M.) in the entry

<ls n="M.">101.</ls>	1	<ls>M. 1, 100.</ls>

<ls>M. 1, 100.</ls> {#svameva brAhmaRo BuNkte svaM vaste svaM dadAti sa#} 
<ls n="M.">101.</ls> {#svAdAna#}    THE PROBLEM

This example can be resolved by a prior ls:
<ls n="M.">101.</ls> -> <ls n="M. 1,">101.</ls>

---------------------------
Write a variant of link_change.py to apply the method of this example.

python link_change_a.py linksort4_1.txt link_changea_1_ok.txt link_changea_1_todo.txt

197 cases with status OK written to link_changea_1_ok.txt
619 cases with status TODO written to link_changea_1_todo.txt

=========================================================
debug link_change_a.py  ???
temp_debug_input.txt 1:
  line from linksort4_1.txt that should be resolved but was missed.
<ls n="M.">101.</ls>	1	<ls>M. 1, 100.</ls>

python link_change_a.py temp_debug_input.txt temp_debug_ok.txt temp_debug_todo.txt

linksort4_1.txt link_changea_1_ok.txt link_changea_1_todo.txt

debug end
=========================================================
#generate a standard change file from link_changea_1_ok.txt

python make_change_a.py temp_pwg_1.txt link_changea_1_ok.txt change_2.txt
197 cases written to change_2.txt

# apply the changes: temp_pwg_1.txt
python updateByLine.py temp_pwg_1.txt change_2.txt temp_pwg_2.txt
197 change transactions from change_2.txt

regenerate local displays from temp_pwg_1

cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue74

-------------------------------------------------------


Write an intermediate temp_pwg_3_work.txt
  for these 619 remaining cases.

python linksort.py 5 temp_pwg_2.txt temp_pwg_3_work.txt

1149413 lines read from temp_pwg_2.txt
122736 entries found
619 non-standard records
1149413 lines written to temp_pwg_3_work.txt

This file has emacs org-mode markup:
- '** <ls'  identifies problematic ls -  619 of them
- the entry metaline is '* TODO <L>...'
- the entry lend is '* <LEND>'
- '* D <L>'  '* DONE <L>'  * T <L>

So we can edit in org-mode
 When an entry is changed, change '* TODO ' to '* D '
Manual edit of temp_pwg_3_work.txt

</ls> <ls n="M.">
</ls> <ls n="M. ,">

[ ...  much time passes ... ]
NOTES:
---
<L>1289<pc>1-0095<k1>atiTin
 has M. 12,917   but there is no such shloka in our 'manu'!
---
<L>33327<pc>3-0662<k1>duHKa
{#duHKamupayanti#} not found at M. 1,26 or 1,49
---
<L>40002<pc>4-0237<k1>niHSreyasa
 print change
old: <ls>M. 12, 83.</ls> etc.
new: <ls>M. 12, 83.</ls> <ls n="M. 12,">104.</ls> <ls n="M. 12,">116.</ls> - <ls n="M.">1, 117.</ls>
---

--------------------------
cp temp_pwg_3_work.txt temp_pwg_3.txt

Manually remove temporary markup from temp_pwg_3.txt

** <ls -> <ls
* TODO <L> -> <L>
* DONE <L> -> <L>
* <L> -> <L>
** -> (empty-string)

</ls> <ls n="M.">


-----------------------
regenerate local displays from temp_pwg_3.txt
 
cp temp_pwg_3.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok !
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue74

------------------------
# generate change_3 file:
python diff_to_changes_dict.py temp_pwg_2.txt temp_pwg_3.txt change_3.txt

601 line changes written to change_3.txt

-----------------------
Regenerate all "M." link references in temp_pwg_3.txt

python linksort.py 1 temp_pwg_3.txt linksort1_3.txt
22566 cases written to linksort1_3.txt
------------
generate the non-standard links
python linksort.py 3 temp_pwg_3.txt linksort3_3.txt
9 cases written to linksort3_3.txt




-----------------------------------
sync csl-orig to Github
(using temp_pwg_3.txt)
cd /c/xampp/htdocs/cologne/csl-orig

git add . # pwg.txt
git commit -m "PWG link standardization for M. (Manava dharmashastra)
Ref: https://github.com/sanskrit-lexicon/PWG/issues/74"
# 2916 insertions(+), 2916 deletions(-)

git push

-------------------------
sync cologne for csl-orig
and regenerate pwg displays.

----------------------------------
Some summary info using version 3 of pwg
python linksort.py 2 temp_pwg_3.txt linksort2_3.txt
22557 total number of 'regular' links
2659 cases written to linksort2_3.txt

Compare 22557 links for version 3 to
        13979 for version -

python linksort.py 3 temp_pwg_3.txt linksort3_3.txt
9 non-standard links

----------------------------------
link count summary for pwg
Refer: https://github.com/sanskrit-lexicon/PWG/tree/master/pwg_ls2/ak
lsextract_all.py

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/ak/lsextract_all.py .
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pwg/pywork/pwgauth/pwgbib_input.txt  .

python lsextract_all.py temp_pwg_3.txt pwgbib_input.txt lsextract_all.txt
compare to https://github.com/sanskrit-lexicon/PWG/blob/master/pwg_ls2/ak/lsextract_pwg_1.txt done exactly 2 years ago.

----------------------------------
sync this repo to github

----------------------------------
09-12-2024 reopen for a few changes

------------------------
# generate change_0a file:
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_0a.txt change_0a.txt
27 changes written to change_0a.txt

----------------------------------
# remove un-needed work file
rm temp_pwg_3_work.txt


----------------------------------
# discover bug in linksort.py (in get_standard_regexes)
# linksorta.py corrects the bug
# 
python linksorta.py 2 temp_pwg_3.txt linksorta2_3.txt
22557 total number of 'regular' links
2723 cases written to linksorta2_3.txt

The correction does not affect the total number of regular links.
It does increase the number of cases, from 2659 to 2723.
-------------------------------------------------------

----------------------------------
compare linksort2_3.txt with
c:/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue73/Manu.Deslongchamps.index.txt
Based on the index, there are 37 invalid adhyAya,shlokas.
  These are identified in file ls_M_invalid.txt

Note: program used to find some info (metaline, <ls>) of invalid items.
python linksort_debug.py 2 temp_pwg_3.txt ls_M_invalid.txt

----------------------------------
----------------------------------
# 4 ls unknowns
Ref: https://github.com/sanskrit-lexicon/PWG/issues/74#issuecomment-2345495387
cp temp_pwg_3.txt temp_pwg_4.txt
manual edit temp_pwg_4.txt

resolving.ls_M_invalid.cases.AB_pwg.txt  AB's solutions to
 ls_M_invalid.txt.  Solves all but 2.
 Note: jim edits resolving.ls_M_invalid.cases.AB_pwg.txt
 
 Further corrections made to temp_pwg_4.txt

# generate change_4.txt
python diff_to_changes_dict.py temp_pwg_3.txt temp_pwg_4.txt change_4.txt
39 changes written to change_4.txt

----------------------------------

ls-entries.to.split.further_pwg.txt
From AB.
About 50.

# generate formal change file --
python make_change_split.py temp_pwg_4.txt ls-entries.to.split.further_pwg.txt temp_change_5.txt

cp temp_change_5.txt change_5.txt
# edit change_5.txt

</ls> <ls n="R.">
</ls> <ls n="ṚV.">
</ls> <ls n="AV.">
</ls> <ls n="GORR.">
</ls> <ls n="R. GORR.">

https://sanskrit-lexicon-scans.github.io/ramayanagorr/?4,2,25
https://sanskrit-lexicon-scans.github.io/ramayanaschl/?2,25,73
https://sanskrit-lexicon.github.io/avlinks/avhymns/av08.010.html
https://sanskrit-lexicon.github.io/rvlinks/rvhymns/rv01.175.html
https://sanskrit-lexicon-scans.github.io/manu/index.html?5,162
https://sanskrit-lexicon-scans.github.io/mbhcalc/?13.4283

# then apply changes to get temp_pwg_5.txt
python updateByLine.py temp_pwg_4.txt change_5.txt temp_pwg_5.txt
48 change transactions from change_5.txt

----------------------------------
# regenerate local displays from temp_pwg_5
# check for errors

cp temp_pwg_5.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue74

------------------------------------------------------------
Corrections from issue66
Ref: https://github.com/sanskrit-lexicon/PWG/issues/66

cp temp_pwg_5.txt temp_pwg_6.txt
# manual edit

6 cases  working ....
done 204440: <div n="2">— g) {%ein best. Metrum%} (4 Mal {Ç}{?} {Ç}{?}) 
---
done 277743: <ls>HIT. 98, 11.</ls> — In den beiden letzten Bedd. offenbar = {?}
<L>28175<pc>3-0177<k1>waNka
 <pic name='rajatamudra.png'/>
 changes to
   csl-websanlexicon/v02/inventory.txt
   csl-websanlexicon/v02/makotemplates/web/webtc/basicdisplay.php
 NOTE: The image does NOT show up in simple-search.
 
277749: {#waNkaka#}¦ <lex>m.</lex> {%gestempeltes%} {?} {%Silber, Silbergeld%} ({#rajatamudrA#})
<L>28176<pc>3-0178<k1>waNkaka
---
done 533545: <ls>KUMĀRAS. 3, 42.</ls> {#cOrajArarnif{?}BatEreva sTAtavyam#}
old:
{#cOrajArarnif{?}BatEreva sTAtavyam#}
new:
{#cOrajArErniBftEreva sTAtavyam#}
print change
Ref: https://github.com/sanskrit-lexicon/PWG/issues/66#issue-1570786740

---
done 613960:
old:
<ls>H. 633.</ls> {#nAgnO mehaM#} {%(Urin%} oder {?} {%Urinlassen)%} {#kurvIta#}
new: from AB:  Note paren imbalance:
<ls>H. 633.</ls> {#nAgnO mehaM#} {%(Urin%} oder {%das Urinlassen)%} {#kurvIta#}
new: jim adjust
<ls>H. 633.</ls> {#nAgnO mehaM#} ({%Urin%} oder {%das Urinlassen%}) {#kurvIta#}

---
651213: 1. {#utpulaka#}¦ ({#ud + pu°#}) <lex>n.</lex> {%das Sträuben der Härchen am Körper%} (vor Auf{?}sung): {#biBratyutpulakAni#} 

<L>67734<pc>5-1166<k1>utpulaka
old:
1. {#utpulaka#}¦ ({#ud + pu°#}) <lex>n.</lex> {%das Sträuben der Härchen am Körper%} (vor Auf{?}sung): {#biBratyutpulakAni#}

new:
1. {#utpulaka#}¦ ({#1. ud + pu°#}) <lex>n.</lex> {%das Sträuben der Härchen am Körper%} (vor Aufregung): {#biBratyutpulakAni#}
-------------
TODO:
1.   print change (see above)
2. scan page replacement:
  https://www.sanskrit-lexicon.uni-koeln.de/scans/csl-apidev/servepdf.php?dict=PWG&page=5-0908
  original-url=
  "https://www.sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpdf/pwg5-0907.pdf"
3. scan page replacement
original-url="https://www.sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpdf/pwg5-1165.pdf" 
----------------------------------
# generate change_6
python diff_to_changes_dict.py temp_pwg_5.txt temp_pwg_6.txt change_6.txt
7 changes written to change_6.txt 
----------------------------------
# regenerate local displays from temp_pwg_6
# check for errors

cp temp_pwg_6.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue74
(* 5 126) 630
----------------------------------
C.lines.filled.or.corrected.-.wiki.style.txt
  from issue29.

python make_change_prosody.py temp_pwg_6.txt C.lines.filled.or.corrected.-.wiki.style.txt temp_change_7.txt

cp temp_change_7.txt change_7.txt
# manual edit of change_7.txt
'; ?' (31 of these) where other (non-prosody) differences noticed:
1. {#(X)#} - I used ({#X#})
2. <ls>Z. 2</ls> --  I kept this but 99 of these found in cdsl
   Jim thinks all should be re-written as Z. 2  (no ls markup)
3. d. i. -> <ab>d. i.</ab>
4. linenum difference
   1098078 -> 1098076
   1098113 -> 1098111
   1104666 -> 1104663
   1104667 -> 1104664

--------------------
# apply change_7
python updateByLine.py temp_pwg_6.txt change_7.txt temp_pwg_7.txt
1149413 lines read from temp_pwg_6.txt
1149413 records written to temp_pwg_7.txt
126 change transactions from change_7.txt

----------------------------------
# regenerate local displays from temp_pwg_7
# check for errors

cp temp_pwg_7.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue74

----------------------------------
¯ -> –  2004 matches in 322 lines for "¯" in buffer: temp_pwg_7.txt
˘ -> ⏑  2438 matches in 312 lines for "˘" in buffer: temp_pwg_7.txt

python make_change_prosody1.py temp_pwg_7.txt change_8.txt
1149413 lines read from temp_pwg_7.txt
122736 entries found
326 cases written to change_8.txt

python updateByLine.py temp_pwg_7.txt change_8.txt temp_pwg_8.txt
1149413 lines read from temp_pwg_7.txt
1149413 records written to temp_pwg_8.txt
326 change transactions from change_8.txt

2743 matches in 446 lines for "–" in buffer: temp_pwg_8.txt
3354 matches in 437 lines for " ⏑" in buffer: temp_pwg_8.txt

----------------------------------
# regenerate local displays from temp_pwg_8
# check for errors

cp temp_pwg_8.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue74


----------------------------------
Andhrabharati's resolution of the 7 unresolved from change_5.txt
 Ref: https://github.com/sanskrit-lexicon/PWG/issues/74#issuecomment-2351900537

make new file change_9.txt

# apply the changes: temp_pwg_9.txt
python updateByLine.py temp_pwg_8.txt change_9.txt temp_pwg_9.txt
5 change transactions from change_9.txt

----------------------------------
# regenerate local displays from temp_pwg_9
# check for errors

cp temp_pwg_9.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue74


-------------------------------------------------------------
notes re some of AB's observations in above comment
32 matches for "<ls>AV. [0-9]+, [0-9]+\.?</ls>"
4 matches in 1 line for "<ls n="AV.">[0-9]+, [0-9]+\.?</ls>"

365 matches in 364 lines for "<ls>ṚV. [0-9]+, [0-9]+\.?</ls>" in buffer: temp_pwg_8.txt
79 matches in 63 lines for "<ls n="ṚV.">[0-9]+, [0-9]+\.?</ls>" in buffer: temp_pwg_8.txt

180 matches for "<ls>R. [0-9]+, [0-9]+, [0-9]+, [0-9]+\.?</ls>"
 (प्रक्षिप्त)
 Three subsets:
 7, 59, x, y
 7, 23, x, y
 7, 37, x, y
 
----------------------------------
----------------------------------------------------------------
install version 9 of pwg
cd /c/xampp/htdocs/cologne/csl-orig

cd /c/xampp/htdocs/cologne/csl-websanlexicon
git add .
git commit -m "PWG: Ref. https://github.com/sanskrit-lexicon/PWG/issues/74"
git push
----
sh apidev_copy.sh  # for basicdisplay.php

cd /c/xampp/htdocs/cologne/csl-apidev
git add .
git commit -m "PWG: Ref. https://github.com/sanskrit-lexicon/PWG/issues/74"
git push

----------------------------------------------------------------
update cologne server

cd scans/csl-orig
git pull
cd scans/csl-websanlexicon
git pull
cd scans/csl-apidev
git pull
cd scans/csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/

----------------------------------------------------------------
THE END
