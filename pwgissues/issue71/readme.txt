
Ref: https://github.com/sanskrit-lexicon/PWG/issues/71
   standardization of pwg links for KATHĀS.
katha sarit sagara

This directory:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue71

----
Start with pwg.txt from csl-orig at commit
  0c4d0e81f65b80414ef27a595fa63b7f9a075586

cd /c/xampp/htdocs/cologne/csl-orig
git show 0c4d0e81f6:v02/pwg/pwg.txt > /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue71/temp_pwg_0.txt


***********************************************
improve markup pwg
-----------------------------------------------
Examine temp_pwg_0.txt
Emacs: occur 
 19504 matches in 17191 lines for "KATHĀS\."
  Save *OCCUR* buffer to kathas_all_0.txt

# All "KATHĀS." link references
Regex matches to one of these two regexes:
 regex1raw = r'<ls>KATHĀS\..*?<?ls>'
 regex2raw = r'<ls n="KATHĀS\..*?">.*?</ls>'
Then sort the matches.
python linksort.py 1 temp_pwg_0.txt linksort1_0.txt
19502 cases written to linksort1_0.txt

# Non-standard links.
Standard:
<ls>KATHĀS\. [0-9]+, [0-9]+\.?</ls>
<ls n="KATHĀS\. [0-9]+,">[0-9]+\.?</ls>
<ls n="KATHĀS\.">([0-9]+), ([0-9])+\.?</ls>
<ls>KATHĀS\.</ls>
<ls>KATHĀS\. ([0-9]+), ([0-9]+)\. fgg?\.</ls>
<ls n="KATHĀS\. ([0-9]+),">([0-9])+\. fgg?\.</ls>
<ls n="KATHĀS\.">([0-9]+), ([0-9])+\. fgg?\.</ls>

# show the standard links, sorted with subcounts of multiplicity
python linksort.py 2 temp_pwg_0.txt linksort2_0.txt
16955 total number of 'regular' links
9207 cases written to linksort2_0.txt
Note: 
First:
  (0,0) (7)  No parameters: <ls>KATHĀS\.</ls>
  (1,1) (3)
Last few
  124,251 (3)
  148,135 (1)
  190,90 (1)
  561,7 (1)   IS this correct?


------------------------------------------------
Begin work to 'correct' the non-standard links
(- 19502 16955) 2547 non-standard.
First step is to list the non-standard:

python linksort.py 3 temp_pwg_0.txt linksort3_0.txt
1891 non-standard of type1
656 non-standard of type2
2547 cases written to linksort3_0.txt  (2547 as expected)

----
------------------------------------------------
 for each line of linksort3, if possible generate an
   array of links, and write the original line and these links.
 Some link-rewrites will fail.
 Successes written to the ok file, others written to the todo file

python link_change.py linksort3_0.txt link_change_0_ok.txt link_change_0_todo.txt

2174 marked OK written to link_change_0_ok.txt
373 marked TODO written to link_change_0_todo.txt

------------------------------------------------
generate a standard change file

python make_change.py temp_pwg_0.txt link_change_0_ok.txt change_1.txt
2167 lines changes
2174 count of replacements
2167 cases written to change_1.txt

# apply the changes: temp_pwg_1.txt
python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt

2167 change transactions from change_1.txt
2167 of type new

----
regenerate local displays from temp_pwg_1

cp temp_pwg_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
ok
-------------------------------------------------------
What about the items in link_change_0_todo.txt ?

python linksort.py 4 temp_pwg_1.txt linksort4_1.txt
380 non-standard records
380 cases written to linksort4_1.txt


Note linksort3_1.txt has  the same 373 lines as in link_change_0_todo.txt


Some of these can be resolved by a prior ls.
Example:

<ls>KATHĀS. 101, 135.</ls> {#kAlam#} dass. 
<ls n="KATHĀS.">134.</ls> <ls>HARIV. 10270.</ls> {#dUtikAgamanakAlamapArayantI soQum#} {%erwarten%}

Here <ls n="KATHĀS.">134.</ls> -> <ls n="KATHĀS.">101, 134.</ls>

---------------------------
Write a variant of link_change.py to apply the method of this example.

python link_change_a.py linksort3_1.txt link_change_1_ok.txt link_change_1_todo.txt


---------------------------
python link_change_a.py linksort4_1.txt link_change_1_ok.txt link_change_1_todo.txt

146 cases with status OK written to link_change_1_ok.txt
234 cases with status TODO written to link_change_1_todo.txt

#generate a standard change file from link_change_1_ok.txt

python make_change_a.py temp_pwg_1.txt link_change_1_ok.txt change_2.txt
146 cases written to change_2.txt

# apply the changes: temp_pwg_1.txt
python updateByLine.py temp_pwg_1.txt change_2.txt temp_pwg_2.txt
146 change transactions from change_2.txt

regenerate local displays from temp_pwg_1

cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue71

-------------------------------------------------------
234 cases with status TODO written to link_change_1_todo.txt

Can we do some of them?

python linksort.py 4 temp_pwg_2.txt linksort4_2.txt
234 cases written to linksort4_2.txt

Write an intermediate temp_pwg_3_work.txt
  for these 234 cases.

python linksort.py 5 temp_pwg_2.txt temp_pwg_3_work.txt

Manual edit of temp_pwg_3_work.txt

cp temp_pwg_3_work.txt temp_pwg_3.txt

Manually remove temporary markup from temp_pwg_3.txt

** <ls -> <ls
* TODO <L> -> <L>
* DONE <L> -> <L>
* <L> -> <L>
** -> (empty-string)

</ls> <ls n="KATHĀS.">

------------------------
# generate change_3 file:
python diff_to_changes_dict.py temp_pwg_2.txt temp_pwg_3.txt change_3.txt
230 line changes written to change_3.txt

-----------------------
regenerate local displays from temp_pwg_3.txt

cp temp_pwg_3.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok !
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue71
-----------------------
Regenerate all "KATHĀS." link references in temp_pwg_3.txt

python linksort.py 1 temp_pwg_3.txt linksort1_3.txt
25005 cases written to linksort1_3.txt
------------
generate the non-standard links
python linksort.py 3 temp_pwg_3.txt linksort3_3.txt
5 non-standard of type1
2 non-standard of type2
7 cases written to linksort3_3.txt

----
cat linksort3_3.txt
THESE ARE THE NON-STANDARD KATHĀS. links.
<ls>KATHĀS. 75. fgg.</ls>
<ls>KATHĀS. 9, Einl.</ls>  page before 9,1  Link logic does not reach!
<ls>KATHĀS. 9. fgg.</ls>
<ls>KATHĀS. 9</ls>
<ls>KATHĀS. S. 96.</ls>
<ls n="KATHĀS.">22,a.</ls>
<ls n="KATHĀS.">42.</ls>
-----------------------------------
sync csl-orig to Github
(using temp_pwg_3.txt)
cd csl-orig/v02
git add . # pwg.txt
git commit -m "PWG: KATHĀS. links.
Ref: https://github.com/sanskrit-lexicon/PWG/issues/71"
# 2538 insertions(+), 2538 deletions(-)

git push
----------------------------------
push this PWG repo.
