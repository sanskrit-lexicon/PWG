
11-16-2025 begun ejf

fix references
 ŚAT. BR. = ŚATAPATHABRĀHMAṆA
 pwg
 
sanskrit-lexicon-scans/

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue84fix

this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue170/issue84pwg

-------------------------------------
# get temporary local copy of kosha
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt
--------------------------------------

# Andhrabharati's solution files
1. lsfix3_chkidx_pwg_3b2.txt : is this replaced by lsfix3_chkidx_pwg_3b.txt , NOT USED
  ref0 =  https://github.com/user-attachments/files/23324109/lsfix3_chkidx_pwg_3b2.txt
2. lsfix3_chkidx_pwg_3a.txt
   regular citations (type-a) [70 out of 71]
   Jim's old format
   ref1 = https://github.com/sanskrit-lexicon/PWG/issues/170#issuecomment-3538921474
3. lsfix3_chkidx_pwg_3b.txt
   padded citations (type-b) [157 out of 166]
   AB's new format
   ref1
4. lsfix3_todo_ab.txt
   ref1 is source. This file made by Jim to hold misc. cases from AB in ref1 comment.
   9 individual cases (+ 4 5)   [ first two cases (izwi) solved by
     adding cases 127, 128 to change_pwg_3b.txt
   The 'solution' status of these uncertain

--------------------------------------
# for context -- do this on temp_pwg_0.txt
# create lsfix3_pwg_0.txt and lsfix3_chkidx_pwg_0.txt

# check again for invalid references in temp_pwg_0.txt

python lsfix3.py pwg temp_pwg_0.txt lsfix3_pwg_0.txt
(True,20678),(all,20678) lsfix3_pwg_0.txt

python chkidx.py lsfix3_pwg_0.txt SAT.index_edit.txt lsfix3_chkidx_pwg_0.txt
20441 instances find ipage out of 20678
 (- 20678 20441)  = 237  

diff lsfix3_chkidx_pwg_0.txt /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue84fix/lsfix3_chkidx_pwg_2.txt | wc -l
# 13 lines in diff.
# Here is the diff  NOT sure what to do with this
1032c1032
< 731   35792   apsaras <ls>ŚAT. BR. 9,4,1,2. fgg.</ls> 9,4,1,2
---
> 731   35793   apsaras <ls>ŚAT. BR. 9,4,1,2. fgg.</ls> 9,4,1,2
12288,12289c12288,12289
< 348   496227  prEza   <ls>ŚAT. BR. 4,1,3,15.</ls>     4,1,3,15
< 992   496228  prEza   <ls n="ŚAT. BR.">13,5,2,23.</ls>        13,5,2,23
---
> 348   496227  prEpa   <ls>ŚAT. BR. 4,1,3,15.</ls>     4,1,3,15
> 992   496228  prEpa   <ls n="ŚAT. BR.">13,5,2,23.</ls>        13,5,2,23
13121,13122d13120
< 846   535274  Buvana  <ls n="ŚAT. BR.">11,3,1,6.</ls> 11,3,1,6
< 19    535274  Buvana  <ls n="ŚAT. BR.">1,2,5,1.</ls>  1,2,5,1

=======================================================================
lsfix3_chkidx_pwg_3a.txt  work

--------------------------------------
Generate a change file from temp_pwg_0.txt and  lsfix3_chkidx_pwg_3a.txt
This change file is a 'template'.
edit the change file and manually change the 'new' per the correction.

python prepare.py temp_pwg_0.txt lsfix3_chkidx_pwg_3a.txt change_pwg_3a.txt

Manually edit change_pwg_3a.txt
--------------------------------------
# Generate temp_pwg_3a.txt from change file
python updateByLine.py temp_pwg_0.txt change_pwg_3a.txt temp_pwg_3a.txt
# 69 lines changed

Nearly all the changes are marked as 'print error'.
Generate 'print change' lines for csl-corrections

# prepare a template print change line for each record
python prep_printchange.py change_pwg_3a.txt prep_printchange_pwg_3a.txt
edit this, filling in the blanks
# printchange_pwg_3a.txt is extracted from the prep file,
# and used to modify csl-corrections/dictionaries/pwg/pwg_printchange.txt
  (in csl-corrections repo)

x
=======================================================================
lsfix3_chkidx_pwg_3b.txt  work

--------------------------------------
Generate a change file template from temp_pwg_0.txt and  lsfix3_chkidx_pwg_3b.txt
This change file is a 'template'.
edit the change file and manually change the 'new' per the correction.

This 3b file has one extra field, the parameters.
Use variant prepare_3b.py to generate the template
Also makes a partial 'pc: ' line for documenting print errors.

python prepare_3b.py temp_pwg_3a.txt lsfix3_chkidx_pwg_3b.txt change_pwg_3b.txt

--------------------------------------
# Generate temp_pwg_3b.txt from change file
python updateByLine.py temp_pwg_3a.txt change_pwg_3b.txt temp_pwg_3b.txt
# 126 lines changed

-------------------------------------
# remake xml from temp_pwg_3b.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue170/issue84pwg/
cp temp_pwg_3b.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue170/issue84pwg/

--------------------------------------
# check again for invalid references in temp_pwg_3b.txt
python lsfix3.py pwg temp_pwg_3b.txt lsfix3_pwg_3b.txt
(True,20641),(all,20641) lsfix3_pwg_3b.txt

python chkidx.py lsfix3_pwg_3b.txt SAT.index_edit.txt lsfix3_chkidx_pwg_3b.txt
20630 instances find ipage out of 20641
(- 20641 20630) 11 unsolved.
put these 13 into file lsfix3_todo_jim.txt
compare

-------------------------------------
Nearly all the changes are marked as 'print error'.
in change_pwg_3b.txt there are lines starting with "; pc:" and ending with 'p'
Extract these lines for csl-corrections, as printchange_pwg_3b.txt

================================================
INSTALLATION
sync to github:

------------------
# csl-orig 
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue170/issue84pwg/
diff temp_pwg_3b.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue84pwg  #170  pwg refs inconsistent with index"

git push
#    3d3d805..14553c5  master -> master
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue170/issue84pwg/
------------------------

# csl-corrections
# use printchange_pwg_3a.txt  printchange_pwg_3b.txt to modify
# dictionaries/pwg/pwg_printchange.txt

cd /c/xampp/htdocs/cologne/csl-corrections
git pull
git add .
git commit -m "Ref: https://github.com/sanskrit-lexicon/PWG/issues/170 (issue84pwg)"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue170/issue84pwg/

---------------------------------------------------
# sync to Cologne, pull changed repos, redo display
---------------
csl-orig #pull
csl-corrections #pull

---------------
# update displays for pwg
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/

-----------------------------------------------------
# sync issue170/issue84pwg/ to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue170/issue84pwg/
git pull
git add .
git commit -m "#170 issue84pwg"
git push

------------------------------------------------------------
THE END
