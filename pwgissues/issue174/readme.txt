
05-14-2026 begun ejf

enhance PWG markup for common abbreviations

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issues/174


this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue174

* gather files to start analysis
-------------------------------------
# get temporary local copy of kosha
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt

# local copy of pwgab_input.txt
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pwg/pywork/pwgab/pwgab_input.txt pwgab_input.txt
pwgab_input.txt 54 
-------------------------------------
# Files from Andhrabharati
PWG_abbr_global.txt   787
PWG_abbr_local.txt

Ref: https://github.com/sanskrit-lexicon/PWG/issues/174#issuecomment-4462624587
-------------------------------------
* xmltag_pwg_0.txt, xmltag_pwg_0_edit.txt
python xmltag.py temp_pwg_0.txt xmltag_pwg_0.txt
12 distinct tags written to xmltag_pwg_0.txt

-------------------------------------
* count_ab_0.txt
# stats on <ab>X</ab>
python count_ab.py temp_pwg_0.txt count_ab_0.txt
1129105 read from temp_pwg_0.txt
59 lines written to count_ab_0.txt
1755 = total number of <ab>X</ab>

* count_ab_local_0.txt
# stats on <ab n="Y">X</ab>
python count_ab_local.py temp_pwg_0.txt count_ab_local_0.txt
1129105 read from temp_pwg_0.txt
27 lines written to count_ab_local_0.txt

-------------------------------------
* temp_pwg_1.txt
# remove all 'ab' markup in pwg, for both local and global
python remove_ab.py temp_pwg_0.txt temp_pwg_1.txt
# additionally, manual changes to temp_pwg_1.txt
v.l. -> v. l.   (782)   # correction
s.u. -> s. u.   (2)     # correction
<lex>n</lex> -> <lex>n.</lex>  (1)  # correction

-------------------------------------
* pwgab_input_1.txt
 cp pwgab_input.txt pwgab_input_1.txt
# manual changes
 in particular, lower case versions added for many abbreviations.
Question re 'Mpt'
-------------------------------------
* temp_pwg_2.txt, markcount_a_2.txt
python mark_ab.py temp_pwg_1.txt pwgab_input_1.txt temp_pwg_2.txt markcount_a_2.txt

86 lines read from pwgab_input_1.txt
1129105 lines read from temp_pwg_1.txt
99485 lines changed
1129105 lines written to temp_pwg_2.txt
86 lines written to markcount_a_2.txt
111590 = total number of <ab>X</ab>

-------------------------------------
* pwgab_input_2.txt
  Reformatting of Andhrabharati's file PWG_abbr_global.txt
-------------------------------------
* pwgab_input_1b.txt,  pwgab_input_2b.txt

cp pwgab_input_1.txt pwgab_input_1b.txt  # (cdsl)
cp pwgab_input_2.txt pwgab_input_2b.txt  # (AB)

edit based on abdiff_count_2_3.txt
** (1) abbrev in cdsl (0), in AB (0): remove in both
** (7) abbrev not in cdsl, in AB (0): Remove in AB
adj. Comp.	-1	0
ANUKR.	-1	0
Chr.	-1	0
d. f. W.	-1	0
excl.	-1	0
MBH.	-1	0
v. Chr.	-1	0

** (4) abbrev in cdsl (0), not in AB: Remove in cdsl
Adv.	0	-1
Metron.	0	-1
N. ag.	0	-1
Nomin.	0	-1

** (2) abbrev in cdsl (>0), not in AB, not lex: Add to AB
Med.	20	-1
Vgl.	18301	-1

** (6) abbrev in cdsl (>0), not in AB, lex
Recall from temp_pwg_2.txt
Adj.	1	-1   lex
adv.	2887	-1   lex 
interj.	90	-1   lex
f.	2555	-1   lex
m.	1040	-1   lex
n.	1169	-1   lex

Assume that AB has marked these as <lex>X</lex> (see count_lex_1.txt)
in temp_pwg_1.txt there are 4 abbreviations
 marked as <lex>X</lex>:  
adj.	35690
f.	23728
m.	43731
n.	21346

* ******************************************
* temp_pwg_3.txt -> temp_pwg_3a.txt ->temp_pwg_4.txt -> temp_pwg_5.txt
* ******************************************
* temp_pwg_3.txt, markcount_a_3.txt
python mark_ab.py temp_pwg_1.txt pwgab_input_2.txt temp_pwg_3.txt markcount_a_3.txt

787 lines read from pwgab_input_2.txt
1129105 lines read from temp_pwg_1.txt
119390 lines changed
1129105 lines written to temp_pwg_3.txt
787 lines written to markcount_a_3.txt
143949 = total number of <ab>X</ab>

-------------------------------------
* abdiff_count_2_3.txt
python count_ab.py temp_pwg_2.txt count_ab_2.txt
python count_ab.py temp_pwg_3.txt count_ab_3.txt

python abdiff.py count_ab_2.txt count_ab_3.txt abdiff_count_2_3.txt
81 read from count_ab_2.txt
778 read from count_ab_3.txt
786 total distinct abbreviations
786 lines written to abdiff_count_2_3.txt


python abdiff.py 
* temp_pwg_3a.txt  masc.
cp temp_pwg_3.txt temp_pwg_3a.txt
<lex>masc.</lex> -> <ab>masc.</ab> (2)
* temp_pwg_4.txt, input_lex.txt
cat input_lex.txt
adj.    blah
adv.    blah
interj. blah
f.      blah
m.      blah
n.      blah
---------
python mark_lex.py temp_pwg_3a.txt input_lex.txt temp_pwg_4.txt markcount_lex_4.txt

cat markcount_lex_4.txt
adj.    35690
adv.    2885
f.      26283
interj. 90
m.      44771
n.      22473

* temp_pwg_5.txt  <ab>adj.</ab> -> <lex>adj.</lex>
cp temp_pwg_4.txt temp_pwg_5.txt
manual change temp_pwg_5.txt
<ab>adj.</ab> -> <lex>adj.</lex>  (387)
* count_ab_5.txt and count_lex_5.txt 
python count_ab.py temp_pwg_5.txt count_ab_5.txt
777 lines written to count_ab_5.txt
143564 = total number of <ab>X</ab>

python count_lex.py temp_pwg_5.txt count_lex_5.txt
6 lines written to count_lex_5.txt
132579 = total number of <lex>X</lex>

* temp_pwg_6.txt further changes
cp temp_pwg_5.txt temp_pwg_6.txt
u.s.<ab>w.</ab> -> <ab>u. s. w.</ab>  (2394)
u.s.w -> <ab>u. s. w.</ab>  (31 - in italics)
Vgl. -> <ab>Vgl.</ab>  (18304)
V. l. -> <ab>v. l.</ab> (1)
, v. l.</ls> -> </ls>, <ab>v. l.</ab>  (2248)
 v. l.</ls> -> </ls> <ab>v. l.</ab>    (77)
<lex>adj.</lex> <ab>comp.</ab> -> <ab>adj. comp.</ab>    (1381, noted by AB)
<lex>adj.</lex> <ab>Comp.</ab> -> <ab>adj. comp.</ab>    (7)
<ls>Schol.</ls> -> <ab>Schol.</ab>  (2997)
REGEX: <ls>Schol\.\( [0-9]\)</ls> → <ab>Schol.</ab>\1    (25)
manual: <ls>Schol.X> -> <ab>Schol.</ab> Y                (32)
<ls>Sch.</ls> -> <ab>Sch.</ab>  
? <ls>Schol. in der Calc.</ls> <ab>Ausg.</ab>

python count_ab.py temp_pwg_6.txt count_ab_6.txt
778 lines written to count_ab_6.txt
167281 = total number of <ab>X</ab>
# Compare AB 171175   (- 171175 167281)  3944

* temp_pwg_7.txt Sch.
cp temp_pwg_6.txt temp_pwg_7.txt

<ls>Sch.</ls> -> <ab>Sch.</ab>   (6677)

python count_ab.py temp_pwg_7.txt count_ab_7.txt
779 lines written to count_ab_7.txt
173958 = total number of <ab>X</ab>

# Compare AB 171175   (- 171175 173958)  -2783
* temp_pwg_8.txt S. Z. u.
cat input_8.txt
S.	?
Z.	?
u.	?

python mark_ab.py temp_pwg_7.txt input_8.txt temp_pwg_8.txt
# 4229 lines changed

python count_ab.py temp_pwg_8.txt count_ab_8.txt
782 lines written to count_ab_8.txt
178317 = total number of <ab>X</ab>
# Compare AB 171175   (- 171175 178317)  -7142

S.   422
u.  2270
Z.  1667


* more unresolved discussion
3225 for "<ab>Schol\.</ab>"
3054 matches in 3016 lines for "<ls>Schol\."
6287 matches for "Schol\."
----------------------------------
v. l.</ls> -> <ab>v. l.</ab></ls>  (2325 - NOT DONE)
   For display, v. l. needs to be outside ls

4965 matches for "<ab>v\. l\.</ab>"
4976 matches for "v\. l\."
  11 matches for "[^b][^/]v\. l\."  to be changed
-----
? <ls n="PAT. a. a. O.">1,122,a.</ls>
? u.
? Z.
? S.

* count_lex_0.txt
python count_lex.py temp_pwg_0.txt count_lex_0.txt
1129105 read from temp_pwg_0.txt
6 lines written to count_lex_0.txt
124497 = total number of <lex>X</lex>

adj.	35690
f.	23728
m.	43731
masc.	2
n	1
n.	21345

* count_lex_1.txt
python count_lex.py temp_pwg_1.txt count_lex_1.txt
1129105 read from temp_pwg_0.txt
5 lines written to count_lex_1.txt
124497 = total number of <lex>X</lex>

adj.	35690
f.	23728
m.	43731
masc.	2
n.	21346

temp_pwg_1.txt changed <lex>n</lex> to <lex>n.</lex>

* *****************************************************

* INSTALLATION
* sync to github:

------------------
# csl-orig temp_pwg_6
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue174/
cp temp_pwg_6.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt 
cd /c/xampp/htdocs/cologne/csl-orig/
git add .
git commit -m "PWG abbreviations, (temp_pwg_6) #174"
git push
FILE SIZE WARNING 
remote: warning: See https://gh.io/lfs for more information.
remote: warning: File v02/pwg/pwg.txt is 50.78 MB; this is larger than GitHub's recommended maximum file size of 50.00 MB
remote: warning: GH001: Large files detected. You may want to try Git Large File Storage - https://git-lfs.github.com.

cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue174/
------------------------
# csl-orig temp_pwg_7
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue174/
cp temp_pwg_7.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt 
cd /c/xampp/htdocs/cologne/csl-orig/
git add .
git commit -m "PWG abbreviations, (temp_pwg_7) #174"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue174/

# csl-orig temp_pwg_8
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue174/
cp temp_pwg_8.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt 
cd /c/xampp/htdocs/cologne/csl-orig/
git add .
git commit -m "PWG abbreviations, (temp_pwg_8) #174"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue174/


---------------------------------------------------
* sync to Cologne, pull changed repos, redo display
---------------
csl-orig #pull
csl-corrections #pull

---------------
# update displays for pwg
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/

-----------------------------------------------------
* sync issue174/ to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue174/
git pull
git add .
git commit -m "issue174 folder revised. #174"
git push

------------------------------------------------------------
************************************************************
* work on tooltips
  see tips/readme.txt
* THE END
