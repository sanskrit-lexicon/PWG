PWG/pwg_ls2/lsnum1

markup improvement.
Ref: https://github.com/sanskrit-lexicon/PWG/issues/65

--------------------------------------------------------------
Start with a copy of csl-orig/v02/pwg/pwg.txt at commit
  0057893421337a290458f667286e18a9488fc093

# change to csl-orig repository on local installation
# generate temp_pwg_0.txt in this lsnum1 directory
cd /c/xampp/htdocs/cologne/csl-orig/
git show 005789:v02/pwg/pwg.txt > /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/temp_pwg_0.txt
# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
--------------------------------------------------------------
Start with a copy of pwgbib_input.txt in csl-pywork at commit
  c67f58fddca18bce6f63d9a5b4bdcb178d85bdc7

cd /c/xampp/htdocs/cologne/csl-pywork/
# generate temp_pwg_0.txt in this lsnum1 directory
  git show c67f58fd:v02/distinctfiles/pwg/pywork/pwgauth/pwgbib_input.txt > /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/temp_pwg_tooltip_0.txt
  
# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/

===============================================================
# revise lsextract_all.py (starting with version in ../lsunknown)
python lsextract_all.py temp_pwg_0.txt temp_pwg_tooltip_0.txt temp_lsextract_pwg_0.txt temp_lsnum1_0.txt
2803 tooltips from temp_pwg_tooltip_0.txt
32089 lsnums written to temp_lsnum1_0.txt
write_tips Output in  lsextract_pwg_0.txt

***************************************************************************
Step 1: first 10%
===============================================================
temp_pwg_1.txt
 identify with '<ls n="">' markup the ls instances starting with a digit.
 Plan then to manually edit this version to correct
Also  make needed revisions to tooltip file
python mark_lsnum1.py temp_pwg_0.txt temp_lsnum1_0.txt temp_pwg_1.txt

cp temp_pwg_tooltip_0.txt temp_pwg_tooltip_1.txt

Manually change temp_pwg_1.txt (preserve number of lines)
Make changes at locations marked by '**...**'
Also, make changes to temp_pwg_tooltip_1.txt

===============================================================
NOTE holdover print changes from lsunknown
--------------------------------------------
print changes
<L>2471<pc>1-0181<k1>anAkASa BHṚ. -> BṚH.
<L>44051<pc>4-0628<k1>pAYcAlaka
 P. 7, 9148. -> MBH. 7, 9148.
 P. 4, 1224. -> MBH. 4, 1224.
<L>44055<pc>4-0629<k1>pAYcAlya
 P. 1, 3728. -> MBH. 1, 3728.
--------------------------------------------
2553 matches in 2542 lines for ")\.</ls>"
 ).</ls>   ==>  </ls>).
--------------------------------------------
editing pastes
</ls> <ls n="ŚAT. BR.">  </ls> <ls n="KĀTY. ŚR.">  </ls> <ls n="BṚH. ĀR. UP.">
</ls> <ls n="PAÑCAT."> </ls> <ls n="PRAB.">  </ls> <ls n="P.">
</ls> <ls n="M.">   </ls> <ls n="H.">
</ls> <ls n="ŚĀK.">  </ls> <ls n="SUŚR.">
</ls> <ls n="ṚV.">   </ls> <ls n="HIT.">  </ls> <ls n="KATHĀS.">
</ls> <ls n="Verz. d. B. H.">  </ls> <ls n="LIA. II">  </ls> <ls n="PAÑCAT.">
</ls> <ls n="">  </ls> <ls n="P."> n="TRIK."
 http://localhost/cologne/csl-apidev/simple-search/v1.1/list-0.2s_rw.php
 http://localhost/cologne/simple/
 n="" X n="COLEBR. Misc. Ess."
<ls n="HARIV.">  <ls n="Verz. d. Oxf. H.">
<ls n="Spr.">  <ls n="Spr. (II)">
<ls n="SIDDH. K.">  </ls> <ls>
-----------------------------------------------

-----------------------------------------------
regex change pairs of 3
<ls>\(X\.\) \([0-9]+, [0-9]+, [0-9]+\.\) \([0-9]+, [0-9]+, [0-9]+\.\)</ls>
<ls>\1 \2</ls> <ls n="\1">\3</ls>

regex change pairs of 2
<ls>\(X\.\) \([0-9]+, [0-9]+\.\) \([0-9]+, [0-9]+\.\)</ls> 
<ls>\1 \2</ls> <ls n="\1">\3</ls>

regex change triples of 2
<ls>\(X\.\) \([0-9]+, [0-9]+\.\) \([0-9]+, [0-9]+\.\) \([0-9]+, [0-9]+\.\)</ls>
<ls>\1 \2</ls> <ls n="\1">\3</ls> <ls n="\1">\4</ls>

regex change triples of 3
<ls>\(X\.\) \([0-9]+, [0-9]+, [0-9]+\.\) \([0-9]+, [0-9]+, [0-9]+\.\) \([0-9]+, [0-9]+, [0-9]+\.\)</ls>
<ls>\1 \2</ls> <ls n="\1">\3</ls> <ls n="\1">\4</ls>
https://github.com/sanskrit-lexicon/COLOGNE/tree/master/localinstall/xampp
regex change triples of 4
<ls>\(X\.\) \([0-9]+, [0-9]+, [0-9]+, [0-9]+\.\) \([0-9]+, [0-9]+, [0-9]+, [0-9]+\.\) \([0-9]+, [0-9]+, [0-9]+, [0-9]+\.\)</ls>
<ls>\1 \2</ls> <ls n="\1">\3</ls> <ls n="\1">\4</ls>

-----------------------------------------------
-----------------------------------------------

bib YĀJAÑ.  (circumflex added)
pwg YĀJAÑ.  (preformed)  <<  revised temp_pwg_1.txt and tooltip to use preformed


---------------------------------------------------------------------------
temp_pwg_1a.txt remove unresolved <ls n="">
cp temp_pwg_1.txt temp_pwg_1a.txt
Manually change (via emacs) <ls n=""> → <ls>  29000 changes

---------------------------------------------------------------------------
install  temp_pwg_1a.txt to check xml
cp temp_pwg_1a.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg ' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/

python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1a.txt change_pwg_1.txt

---------------------------------------------------------------------------
About 10% done. Commit csl-orig, and update at Cologne.
cd /c/xampp/htdocs/cologne/csl-orig/
git pull  # to handle other changes, if any
git add .
git commit -m "PWG: numeric orphans, 1
Ref: https://github.com/sanskrit-lexicon/PWG/issues/65"
git push
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
-------------------------------------------------
# do the necessary at cologne:
# login via ssh.
cd csl-orig
git pull
cd ../csl-pywork/v02
grep 'pwg' redo_cologne_all.sh
# etc.

---------------------------------------------------------------------------
update pwg repository
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/

***************************************************************************
Step 2.
cp temp_pwg_1a.txt temp_pwg_2.txt

Continue with the <ls n=""> instances. in temp_pwg_2.txt.
Now 29000+ to go.


touch change_pwg_2.txt
# option 1
python make_change_b.py 1 temp_pwg_2.txt temp_change_2_1.txt
8115 change transactions written to temp_change_2_1.txt# insert temp_change_2_1.txt into change_pwg_2.txt

python updateByLine.py temp_pwg_1a.txt change_pwg_2.txt temp_pwg_2.txt
1149413 lines read from temp_pwg_1a.txt
1149413 records written to temp_pwg_2.txt
8115 change transactions from change_pwg_2.txt

---------------------------------------------------------------------------
install  temp_pwg_2.txt to check xml
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg ' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/

---------------------------------------------------------------------------
Commit csl-orig, and update at Cologne.
cd /c/xampp/htdocs/cologne/csl-orig/
git pull  # to handle other changes, if any
git add .
git commit -m "PWG: numeric orphans, 2
Ref: https://github.com/sanskrit-lexicon/PWG/issues/65"
git push
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
-------------------------------------------------
# do the necessary at cologne:
# login via ssh.
cd csl-orig
git pull
cd ../csl-pywork/v02
grep 'pwg' redo_cologne_all.sh
# etc.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
---------------------------------------------------------------------------
update pwg repository
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
add and push.
Add issue comment

***************************************************************************
Step 3.

cp temp_pwg_2.txt temp_pwg_3.txt

touch change_pwg_3.txt
------------------------
# option 3a
python make_change_b.py 3a temp_pwg_3.txt temp_change_3_3a.txt
1982 change transactions written to temp_change_3_3a.txt

Insert temp_change_3_3a into change_pwg_3
python updateByLine.py temp_pwg_2.txt change_pwg_3.txt temp_pwg_3.txt

-----------------------
# option 3b
python make_change_b.py 3b temp_pwg_3.txt temp_change_3_3b.txt
3020 change transactions written to temp_change_3_3a.txt

Insert temp_change_3_3b into bottom of change_pwg_3
python updateByLine.py temp_pwg_2.txt change_pwg_3.txt temp_pwg_3.txt
5002 change transactions from change_pwg_3.txt

---------------------------------------------------------------------------
install  temp_pwg_3.txt to check xml
cp temp_pwg_3.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg ' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/

---------------------------------------------------------------------------
Commit csl-orig, and update at Cologne.
cd /c/xampp/htdocs/cologne/csl-orig/
git pull  # to handle other changes, if any
git add .
git commit -m "PWG: numeric orphans, 3
Ref: https://github.com/sanskrit-lexicon/PWG/issues/65"
git push
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
-------------------------------------------------
# do the necessary at cologne:
# login via ssh.
cd csl-orig
git pull
cd ../csl-pywork/v02
grep 'pwg' redo_cologne_all.sh
# etc.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
---------------------------------------------------------------------------
update pwg repository
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
add .
git commit -m "PWG: numeric orphans, 3
Ref: https://github.com/sanskrit-lexicon/PWG/issues/65"
git push
update issue comment

***************************************************************************
Step 4.

cp temp_pwg_3.txt temp_pwg_4.txt

touch change_pwg_4.txt
------------------------
# option 4a
python make_change_b.py 4a temp_pwg_4.txt temp_change_4_4a.txt
752 change transactions written to temp_change_4_4a.txt
# edit 4_4a, to remove/correct many false positives under Verz. d. Oxf. H.
# Insert temp_change_4_4a into change_pwg_4
python updateByLine.py temp_pwg_3.txt change_pwg_4.txt temp_pwg_4.txt
1071 change transactions from change_pwg_4.txt

------------------------
# option 4b
python make_change_b.py 4b temp_pwg_4.txt temp_change_4_4b.txt
2620 change transactions written to temp_change_4_4b.txt

# Insert temp_change_4_4b into change_pwg_4
python updateByLine.py temp_pwg_3.txt change_pwg_4.txt temp_pwg_4.txt
3691 change transactions from change_pwg_4.txt

------------------------
# option 4c
python make_change_b.py 4c temp_pwg_4.txt temp_change_4_4c.txt
2170 change transactions written to temp_change_4_4c.txt

# Insert temp_change_4_4c into change_pwg_4
python updateByLine.py temp_pwg_3.txt change_pwg_4.txt temp_pwg_4.txt
5861 change transactions from change_pwg_4.txt

------------------------
89 matches for "<ls>[0-9, ]+</ls>, <ls>Sch.</ls>
cp temp_pwg_4.txt temp_pwg_4_work.txt
# manually edit temp_pwg_4_work.txt
python diff_to_changes_dict.py temp_pwg_4.txt temp_pwg_4_work.txt temp_change_4_x1.txt
103 changes written to temp_change_4_x1.txt

insert temp_change_4_x1.txt into change_pwg_4.txt
python updateByLine.py temp_pwg_3.txt change_pwg_4.txt temp_pwg_4.txt
5964 change transactions from change_pwg_4.txt
# temp_pwg_4_work.txt no longer needed
rm temp_pwg_4_work.txt

------------------------
 a two-line pattern
479 matches for "{#[a-zA-Z]+#} *
<ls>[1-9]\.</ls>"
cp temp_pwg_4.txt temp_pwg_4_work.txt
Emacs change the 479 in temp_pwg_4_work.txt
\({#[a-zA-Z]+#}\) *
<ls>\([1-9]\.\)</ls>\( *\) → \1 _\2 

python diff_to_changes_dict.py temp_pwg_4.txt temp_pwg_4_work.txt temp_change_4_x2.txt
961 changes written to temp_change_4_x2.txt
insert temp_change_4_x2 into change_pwg_4.txt

python updateByLine.py temp_pwg_3.txt change_pwg_4.txt temp_pwg_4.txt
6925 change transactions from change_pwg_4.txt
# temp_pwg_4_work.txt no longer needed
rm temp_pwg_4_work.txt

That's enough for this batch of changes. ready to install temp_pwg_4
---------------------------------------------------------------------------
install  temp_pwg_4.txt to check xml
cp temp_pwg_4.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg ' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
 
---------------------------------------------------------------------------
Commit csl-orig, and update at Cologne.
cd /c/xampp/htdocs/cologne/csl-orig/
git pull  # to handle other changes, if any
git add .
git commit -m "PWG: numeric orphans, 4
Ref: https://github.com/sanskrit-lexicon/PWG/issues/65"
git push
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
-------------------------------------------------
# do the necessary at cologne:
# login via ssh.
cd csl-orig
git pull
cd ../csl-pywork/v02
grep 'pwg' redo_cologne_all.sh
# etc.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
---------------------------------------------------------------------------
update pwg repository
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
add .
git commit -m "PWG: numeric orphans, 4
Ref: https://github.com/sanskrit-lexicon/PWG/issues/65"
git push
update issue comment

***************************************************************************
Step 5.

cp temp_pwg_5.txt temp_pwg_5.txt

touch change_pwg_5.txt
------------------------
# option 5a
# get 'parent' lsname from previous 3 lines
python make_change_b.py 5a temp_pwg_5.txt temp_change_5_5a.txt
731 change transactions written to temp_change_5_5a.txt

# brief look suggests 5_5a ok.
# Insert temp_change_5_5a into change_pwg_5
python updateByLine.py temp_pwg_4.txt change_pwg_5.txt temp_pwg_5.txt
731 change transactions from change_pwg_5.txt

------------------------
#  5_5x1
cp temp_pwg_5.txt temp_pwg_5_work.txt
# manual edit of temp_pwg_5_work.txt
python diff_to_changes_dict.py temp_pwg_5.txt temp_pwg_5_work.txt change_pwg_5_x1.txt
insert change_pwg_5_x1.txt into change_pwg_5.txt

python updateByLine.py temp_pwg_4.txt change_pwg_5.txt temp_pwg_5.txt
840 change transactions from change_pwg_5.txt

# temp_pwg_5_work.txt not needed
rm temp_pwg_5_work.txt

------------------------
#  5_5x2
cp temp_pwg_5.txt temp_pwg_5_work.txt
# manual edit of temp_pwg_5_work.txt,
# 596 matches for "^<ls>[0-9]+</ls>"matching
python diff_to_changes_dict.py temp_pwg_5.txt temp_pwg_5_work.txt temp_change_pwg_5_x2.txt
1380 changes written to change_pwg_5_x2.txt
#insert temp_change_pwg_5_x2.txt into change_pwg_5.txt

python updateByLine.py temp_pwg_4.txt change_pwg_5.txt temp_pwg_5.txt
2220 change transactions from change_pwg_5.txt

# temp_pwg_5_work.txt not needed
rm temp_pwg_5_work.txt

------------------------
# option 5b
# get 'parent' lsname from previous 3 lines
# add Spr. to list of approved codes
python make_change_b.py 5b temp_pwg_5.txt temp_change_5_5b.txt
731 change transactions written to temp_change_5_5b.txt

# brief look suggests 5_5b ok.
# Insert temp_change_5_5b into change_pwg_5
2220 python updateByLine.py temp_pwg_4.txt change_pwg_5.txt temp_pwg_5.txt

------------------------
# option 5b1
# get 'parent' lsname from previous 3 lines
# cases 'Spr. (II)'
python make_change_b.py 5b1 temp_pwg_5.txt temp_change_5_5b1.txt
732 change transactions written to temp_change_5_5b1.txt

# brief look suggests 5_5b1 ok.
# Insert temp_change_5_5b1 into change_pwg_5
python updateByLine.py temp_pwg_4.txt change_pwg_5.txt temp_pwg_5.txt
2952 change transactions from change_pwg_5.txt

------------------------
# option 5b2
# get 'parent' lsname from previous 3 lines
# cases 'Spr.'
python make_change_b.py 5b2 temp_pwg_5.txt temp_change_5_5b2.txt
1118 change transactions written to temp_change_5_5b2.txt

# brief look suggests 5_5b2 ok.
# Insert temp_change_5_5b2 into change_pwg_5
python updateByLine.py temp_pwg_4.txt change_pwg_5.txt temp_pwg_5.txt
4274 change transactions from change_pwg_5.txt

------------------------
# option 5b3
# get 'parent' lsname from previous 3 lines
# cases 'HALL'
python make_change_b.py 5b3 temp_pwg_5.txt temp_change_5_5b3.txt
204 change transactions written to temp_change_5_5b3.txt

# brief look suggests 5_5b3 ok.
# Insert temp_change_5_5b3 into change_pwg_5
python updateByLine.py temp_pwg_4.txt change_pwg_5.txt temp_pwg_5.txt
 change transactions from change_pwg_5.txt

------------------------
# option 5b4
# get 'parent' lsname from previous 3 lines
# most lsnames approved. Previous reference has no numbers.
python make_change_b.py 5b4 temp_pwg_5.txt temp_change_5_5b4.txt
123 hange transactions written to temp_change_5_5b4.txt

# brief look suggests 5_5b4 ok.
# Insert temp_change_5_5b4 into change_pwg_5
python updateByLine.py temp_pwg_4.txt change_pwg_5.txt temp_pwg_5.txt
4397 change transactions from change_pwg_5.txt


That's enough for this batch of changes. ready to install temp_pwg_5
---------------------------------------------------------------------------
install  temp_pwg_5.txt to check xml
cp temp_pwg_5.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg ' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
 
---------------------------------------------------------------------------
Commit csl-orig, and update at Cologne.
cd /c/xampp/htdocs/cologne/csl-orig/
git pull  # to handle other changes, if any
git add .
git commit -m "PWG: numeric orphans, 5
Ref: https://github.com/sanskrit-lexicon/PWG/issues/65"
git push
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
-------------------------------------------------
# do the necessary at cologne:
# login via ssh.
cd csl-orig
git pull
cd ../csl-pywork/v02
grep 'pwg' redo_cologne_all.sh
# etc.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
---------------------------------------------------------------------------
update pwg repository
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
add .
git commit -m "PWG: numeric orphans, 5
Ref: https://github.com/sanskrit-lexicon/PWG/issues/65"
git push
update issue comment

***************************************************************************
Step 6.

cp temp_pwg_5.txt temp_pwg_6.txt

touch change_pwg_6.txt
------------------------

------------------------
#  6_x1
cp temp_pwg_6.txt temp_pwg_6_work.txt
# 415 matches for ",a,</ls>"
# manual edit of temp_pwg_6_work.txt,

python diff_to_changes_dict.py temp_pwg_6.txt temp_pwg_6_work.txt temp_change_pwg_6_x1.txt

#insert temp_change_pwg_6_x2.txt into change_pwg_6.txt

python updateByLine.py temp_pwg_5.txt change_pwg_6.txt temp_pwg_6.txt
920 lines changed

# temp_pwg_6_work.txt not needed
rm temp_pwg_6_work.txt

------------------------
#  6_x2
cp temp_pwg_6.txt temp_pwg_6_work.txt
# 287 matches for ",b,<"
# manual edit of temp_pwg_6_work.txt,

python diff_to_changes_dict.py temp_pwg_6.txt temp_pwg_6_work.txt temp_change_pwg_6_x2.txt
592 changes written to temp_change_pwg_6_x2.txt

#insert temp_change_pwg_6_x2.txt into change_pwg_6.txt

python updateByLine.py temp_pwg_5.txt change_pwg_6.txt temp_pwg_6.txt
1532 lines changed

# now temp_pwg_6 = temp_pwg_6_work
# temp_pwg_6_work.txt not needed
rm temp_pwg_6_work.txt

------------------------
#  6_x3
cp temp_pwg_6.txt temp_pwg_6_work.txt
# 200+ matches for "</ls>,a."
# 193 matches for "</ls>,b\."
# 42 matches for "zu <ls>[1-8], [0-9]+, [0-9]+\.</ls>
# manual edit of temp_pwg_6_work.txt,

python diff_to_changes_dict.py temp_pwg_6.txt temp_pwg_6_work.txt temp_change_pwg_6_x3.txt
450 changes written to temp_change_pwg_6_x3.txt

#insert temp_change_pwg_6_x3.txt into change_pwg_6.txt

python updateByLine.py temp_pwg_5.txt change_pwg_6.txt temp_pwg_6.txt
1982 lines changed

# now temp_pwg_6 = temp_pwg_6_work
# temp_pwg_6_work.txt not needed
rm temp_pwg_6_work.txt

------------------------
#  6_x4
cp temp_pwg_6.txt temp_pwg_6_work.txt
# 5252 matches in 5172 lines for "<ls>[0-9]"
# 
# manual edit of temp_pwg_6_work.txt,
# <is>Kār</is>. -> <is>Kār.</is> (281 instances)

python diff_to_changes_dict.py temp_pwg_6.txt temp_pwg_6_work.txt temp_change_pwg_6_x4.txt
769 changes written to temp_change_pwg_6_x4.txt

#insert temp_change_pwg_6_x4.txt into change_pwg_6.txt

python updateByLine.py temp_pwg_5.txt change_pwg_6.txt temp_pwg_6.txt
2751 lines changed

# now temp_pwg_6 = temp_pwg_6_work
# temp_pwg_6_work.txt not needed
rm temp_pwg_6_work.txt

---------------------------------------------------------------------------
python make_change_b.py 6a temp_pwg_6.txt temp_change_6a.txt
220 change transactions written to temp_change_6a.txt

#insert temp_change_6a.txt into change_pwg_6.txt.
python updateByLine.py temp_pwg_5.txt change_pwg_6.txt temp_pwg_6.txt
2971 change transactions from change_pwg_6.txt

##cp temp_pwg_6.txt temptemp_pwg_6.txt

------------------------
#  6_x5
cp temp_pwg_6.txt temp_pwg_6_work.txt
# 4686 matches in 4610 lines for "<ls>[0-9]" 

# back to manual changes.

python diff_to_changes_dict.py temp_pwg_6.txt temp_pwg_6_work.txt temp_change_pwg_6_x5.txt
1186 changes written to temp_change_pwg_6_x5.txt

#insert temp_change_6_x5.txt into change_pwg_6.txt.
python updateByLine.py temp_pwg_5.txt change_pwg_6.txt temp_pwg_6.txt
4157 change transactions from change_pwg_6.txt


# temp_pwg_6_work.txt not needed
rm temp_pwg_6_work.txt


--------------
install  temp_pwg_6.txt to check xml
cp temp_pwg_6.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg ' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
 

---------------------------------------------------------------------------
That's enough for this batch of changes. ready to install temp_pwg_6
---------------------------------------------------------------------------
---------------------------------------------------------------------------
Commit csl-orig, and update at Cologne.
cd /c/xampp/htdocs/cologne/csl-orig/
git pull  # to handle other changes, if any
git add .
git commit -m "PWG: numeric orphans, 6
Ref: https://github.com/sanskrit-lexicon/PWG/issues/65"
git push
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
-------------------------------------------------
# do the necessary at cologne:
# login via ssh.
cd csl-orig
git pull
cd ../csl-pywork/v02
grep 'pwg' redo_cologne_all.sh
# etc.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
---------------------------------------------------------------------------
update pwg repository
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
add .
git commit -m "PWG: numeric orphans, 6
Ref: https://github.com/sanskrit-lexicon/PWG/issues/65"
git push
update issue comment

---------------------------------------------------------------------------
------------------------
#  7
cp temp_pwg_6.txt  temp_pwg_7.txt 
touch change_pwg_7.txt

# 3942 matches in 3873 lines for "<ls>[0-9]"

# back to manual changes.
cp temp_pwg_7.txt temp_pwg_7_work.txt

python diff_to_changes_dict.py temp_pwg_7.txt temp_pwg_7_work.txt temp_change_pwg_7_x1.txt
51 changes written to temp_change_pwg_7_x1.txt

#insert temp_change_7_x1.txt into change_pwg_7.txt.
python updateByLine.py temp_pwg_6.txt change_pwg_7.txt temp_pwg_7.txt
# now temp_pwg_7.txt == temp_pwg_7_work.txt

# temp_pwg_7_work.txt not needed
rm temp_pwg_7_work.txt

--------------------------------------------------------
python make_change_b.py 7b temp_pwg_7.txt temp_change_7_7b.txt
11 change transactions
# insert temp_change_7_7b.txt into change_pwg_7.txt
python updateByLine.py temp_pwg_6.txt change_pwg_7.txt temp_pwg_7.txt
534 change transactions

--------------------------------------------------------
# back to manual changes. 7_x2  START
cp temp_pwg_7.txt temp_pwg_7_work.txt
# Manual changes to temp_pwg_7_work.txt
python diff_to_changes_dict.py temp_pwg_7.txt temp_pwg_7_work.txt temp_change_pwg_7_x2.txt


#insert temp_change_7_x2.txt into change_pwg_7.txt.
python updateByLine.py temp_pwg_6.txt change_pwg_7.txt temp_pwg_7.txt
change transactions from change_pwg_7.txt

--------------------------------------------------------
python make_change_b.py 7b temp_pwg_7.txt temp_change_7_7b.txt
change transactions
# insert temp_change_7_7a.txt into change_pwg_7.txt
python updateByLine.py temp_pwg_6.txt change_pwg_7.txt temp_pwg_7.txt
11 change transactions

--------------------------------------------------------
# back to manual changes.
cp temp_pwg_7.txt temp_pwg_7_work.txt
# Manual changes to temp_pwg_7_work.txt
python diff_to_changes_dict.py temp_pwg_7.txt temp_pwg_7_work.txt temp_change_pwg_7_x2.txt
460 changes written to temp_change_pwg_7_x2.txt

#insert temp_change_7_x2.txt into change_pwg_7.txt.
python updateByLine.py temp_pwg_6.txt change_pwg_7.txt temp_pwg_7.txt
523 change transactions from change_pwg_7.txt

# now temp_pwg_7.txt == temp_pwg_7_work.txt

# temp_pwg_7_work.txt not needed
rm temp_pwg_7_work.txt

--------------------------------------------------------
# back to manual changes. 7_x3
cp temp_pwg_7.txt temp_pwg_7_work.txt
# Manual changes to temp_pwg_7_work.txt
python diff_to_changes_dict.py temp_pwg_7.txt temp_pwg_7_work.txt temp_change_pwg_7_x3.txt
3083 changes written to temp_change_pwg_7_x3.txt

#insert temp_change_7_x3.txt into change_pwg_7.txt.
python updateByLine.py temp_pwg_6.txt change_pwg_7.txt temp_pwg_7.txt
3617 change transactions from change_pwg_7.txt

# now temp_pwg_7.txt == temp_pwg_7_work.txt

# temp_pwg_7_work.txt not needed
rm temp_pwg_7_work.txt

--------------

--------------
install  temp_pwg_7.txt to check xml
cp temp_pwg_7.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg ' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
 

---------------------------------------------------------------------------
That's enough for this batch of changes. ready to install temp_pwg_7
---------------------------------------------------------------------------

Commit csl-orig, and update at Cologne.
cd /c/xampp/htdocs/cologne/csl-orig/
git pull  # to handle other changes, if any
git add .
git commit -m "PWG: numeric orphans, 7
Ref: https://github.com/sanskrit-lexicon/PWG/issues/65"
git push
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
-------------------------------------------------
# do the necessary at cologne:
# login via ssh.
cd csl-orig
git pull
cd ../csl-pywork/v02
grep 'pwg' redo_cologne_all.sh
# etc.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
---------------------------------------------------------------------------
update pwg repository
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
add .
git commit -m "PWG: numeric orphans, 7
Ref: https://github.com/sanskrit-lexicon/PWG/issues/65"
git push
update issue comment

#install temp_pwg_tooltip_2.txt in csl-pywork
cp temp_pwg_tooltip_2.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pwg/pywork/pwgauth/pwgbib_input.txt

--------------------------------------------------------
---------------------------------------------------------------------------
#  8
cp temp_pwg_7.txt  temp_pwg_8.txt 
touch change_pwg_8.txt

# 3942 matches in 3873 lines for "<ls>[0-9]"

# back to manual changes.
cp temp_pwg_8.txt temp_pwg_8_work.txt

cp temp_pwg_8.txt temp_pwg_8_work.txt
# Manual changes to temp_pwg_8_work.txt
python diff_to_changes_dict.py temp_pwg_8.txt temp_pwg_8_work.txt temp_change_pwg_8.txt
2016 changes written to temp_change_pwg_8.txt

#insert temp_change_8.txt into change_pwg_8.txt.
python updateByLine.py temp_pwg_7.txt change_pwg_8.txt temp_pwg_8.txt
2016 change transactions from change_pwg_8.txt

# now temp_pwg_8.txt == temp_pwg_8_work.txt

# temp_pwg_8_work.txt not needed
rm temp_pwg_8_work.txt

# some introduced errors identified by rerunning lextract
# revise lsextract_all.py 
python lsextract_all.py temp_pwg_8.txt temp_pwg_tooltip_1.txt temp_lsextract_pwg_8a.txt temp_lsnum1_8a.txt
File temp_lsnum1_1.txt shows 81 items
- 59 are unresolved <ls>{number} -- nothing more to do with these
- the rest (22) are errors in ls

cp temp_pwg_8.txt temp_pwg_8_work.txt
# manually correct those 22 items in temp_pwg_8_work.txt
# A couple of changes also to temp_pwg_tooltip_1.txt
python diff_to_changes_dict.py temp_pwg_8.txt temp_pwg_8_work.txt temp_change_pwg_8x.txt
21 changes written to temp_change_pwg_8x.txt

# insert temp_change_pwg_8x.txt into change_pwg_8.txt
python updateByLine.py temp_pwg_7.txt change_pwg_8.txt temp_pwg_8.txt
2037 change transactions from change_pwg_8.txt

# more cleanup
python diff_to_changes_dict.py temp_pwg_8.txt temp_pwg_8_work.txt temp_change_pwg_8x1.txt
3 changes written to temp_change_pwg_8x1.txt

# insert temp_change_pwg_8x1.txt into change_pwg_8.txt
python updateByLine.py temp_pwg_7.txt change_pwg_8.txt temp_pwg_8.txt
2040 change transactions from change_pwg_8.txt

# one more time for lsextract
python lsextract_all.py temp_pwg_8.txt temp_pwg_tooltip_1.txt temp_lsextract_pwg_8b.txt temp_lsnum1_8b.txt
# Now there are 58 'number' ls, and 0 'unknown' ls.
# Good!
# ready to install

--------------
# Several changes were made to tooltips, in coordination with
# the above changes to pwg.txt.
# install temp_pwg_tooltip_1.txt in csl-pywork
cp temp_pwg_tooltip_1.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pwg/pywork/pwgauth/pwgbib_input.txt


--------------
# install  temp_pwg_8.txt to check xml
cp temp_pwg_8.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg ' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
 

---------------------------------------------------------------------------
That's enough for this batch of changes. ready to install temp_pwg_8
---------------------------------------------------------------------------
Commit csl-pywork (for tooltips)
cd /c/xampp/htdocs/cologne/csl-pywork/v02
git add .
git commit -m "PWG: numeric orphans, 8.  Tooltip changes. minor rev.
Ref: https://github.com/sanskrit-lexicon/PWG/issues/65"
git push

---------------------------------------------------------------------------
Commit csl-orig, and update at Cologne.
cd /c/xampp/htdocs/cologne/csl-orig/
git pull  # to handle other changes, if any
git add .
git commit -m "PWG: numeric orphans, 8. minor rev.
Ref: https://github.com/sanskrit-lexicon/PWG/issues/65"
git push
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
-------------------------------------------------
# do the necessary at cologne:
# login via ssh.
cd csl-orig
git pull
cd ../csl-pywork/v02
git pull # for the new tooltips
grep 'pwg' redo_cologne_all.sh
# etc.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/

---------------------------------------------------------------------------
update pwg repository
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
add .
git commit -m "PWG: numeric orphans, 8
Ref: https://github.com/sanskrit-lexicon/PWG/issues/65"
git push
update issue comment


---------------------------------------------------------------------------
# regenerate dictionary displays,  a way to check for errors in new tooltips

---------------------------------------------------------------------------
push repositories to Github:
csl-orig
csl-pywork
PWG repository (repository containing this file)

---------------------------------------------------------------------------
pull repositories from Github to Cologne.
csl-orig
csl-pywork

---------------------------------------------------------------------------
{Ç} end of entry preceding <L>52710<pc>5-0088<k1>bimbaka<k2>bimbaka
 should be 'long-short' .
---------------------------------------------------------------------------
# revise lsextract_all.py 
python lsextract_all.py temp_pwg_8.txt temp_pwg_tooltip_1.txt temp_lsextract_pwg_1.txt temp_lsnum1_1.txt

2834 tooltips from temp_pwg_tooltip_1.txt
81 lsnums written to temp_lsnum1_1.txt
write_tips Output in  temp_lsextract_pwg_1.txt
---------------------------------------------------------------------------
---------------------------------------------------------------------------
