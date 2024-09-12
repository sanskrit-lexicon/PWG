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
# 4 ls unknowns
Ref: https://github.com/sanskrit-lexicon/PWG/issues/74#issuecomment-2345495387
cp temp_pwg_3.txt temp_pwg_4.txt
manual edit temp_pwg_4.txt

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

----------------------------------
----------------------------------
----------------------------------
----------------------------------
THE END
