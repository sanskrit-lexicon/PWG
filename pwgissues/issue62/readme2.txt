issue62 readme2.txt
06-26-2025
From ../issue94/lsexamine2.txt
 - extract the AK. references with 1 or 2 numerical parms
 and place in file AK1or2parm.txt.
 there are (20 + 16) = 36 instances

cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue62

diff /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg2.txt | wc -l
0  # so temp_pwg2.txt is current as of this time.
# make temp_pwg3.txt to mark the 36 examples -- they are all erroneous!
python prepare_pwg3.py temp_pwg2.txt AK1or2parm.txt temp_pwg3.txt
34 unique strings found
marking strings with "@"
36 lines marked

# manually edit temp_pwg3.txt
# copy pwg3 to csl-orig
cp  temp_pwg3.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
/c/xampp/htdocs/cologne/csl-pywork/v02

# generate local pwg displays
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
# check xml validity
sh xmlchk_xampp.sh pwg
# ok

cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue62   # return home
------------------------------------------
# generate change file 
python diff_to_changes_dict.py temp_pwg2.txt temp_pwg3.txt change_pwg2_pwg3.txt

37 changes written to change_pwg2_pwg3.txt

------------------------------------------
redo issue94 lsexamine files with revised pwg3
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue94 
sh redo_lsexamine.sh
Check lsexamine2.txt -
  There are now 0 instances of 1-parm and 2-parm AK references
  Good!
==========================================
syncing
--------------------------
sync csl-orig
cd /c/xampp/htdocs/cologne/csl-orig

# git commit -m "PWG:  AK. corrections. Ref readme2.txt.
> Ref: https://github.com/sanskrit-lexicon/pwg/issues/62"
push

--------------------------
# sync issue94 to github
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue94
git add .
git commit -m "issue94:  rerun redo_lsexamine.sh for AK. changes. #94"
git push

--------------------------
# sync issue62 to github

cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue62 


#
--------------------------


