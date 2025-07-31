issue62fix/readme.txt
07-31-2025 begun ejf
fix references to Deslongchamps edition of amarakosha.

sanskrit-lexicon-scans/amara_dlc

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue62fix
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue62fix

-------------------------------------
# get temporary local copy of pwg
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue62fix
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt

# generate a copy for manual changes
cp temp_pwg_0.txt temp_pwg_1.txt
--------------------------------------
3 forms of reference to amara_dlc link target:
lscode:  AK.
3 or 4 parameters

We use lsfix2.py, with parmfile lsfix2_parm.py
to examine splitting



======================================
# lsfix2 option colebr for lsfix2_parm.py, 
  uses lscode COLEBR. with 3 or 4 parameters
  
python lsfix2.py dummy temp_pwg_0.txt lsfix2_0.txt
15017 lines written to lsfix2_0.txt
(True, 3) 5392
(True, 4) 9625

Nothing to do!
No changes or splitting required.

# sync issue62fix to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue62fix
git pull
git add .
git commit -m "issue62fix links to amara_dlc 
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
