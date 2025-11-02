
11-02-2025 begun ejf

fix references
 ŚAT. BR. = ŚATAPATHABRĀHMAṆA
 pw
 
sanskrit-lexicon-scans/

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue84fix

this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue170/issue84pw


-------------------------------------
# get temporary local copy of kosha
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw_0.txt
--------------------------------------
# Andhrabharati's solution file
lsfix3_chkidx_pw_3_ab.txt 
--------------------------------------
Generate a change file from AB's solution file and kosha

python prepare.py temp_pw_0.txt lsfix3_chkidx_pw_3_ab.txt change_pw_1.txt

1020 : aNgArAvakzayaRa : ŚAT. BR. 14,9,6,19 : ŚAT. BR. 14,6,9,19 : print change
74782 : priyavrata : ŚAT. BR. 4,5,3,20 : ŚAT. BR. 4,3,5,20 : print change

--------------------------------------
# Generate temp_pw_1.txt from change file
python updateByLine.py temp_pw_0.txt change_pw_1.txt temp_pw_1.txt
28 change transactions from change_pw_1.txt

--------------------------------------
# check again for invalid references in temp_pw_1.txt
python lsfix3.py pw temp_pw_1.txt lsfix3_pw_1_ab.txt

python chkidx.py lsfix3_pw_1_ab.txt SAT.index_edit.txt lsfix3_chkidx_pw_1_ab.txt
1333 instances find ipage out of 1333
ALL SOLVED!

# if there are any None elements, revise change_pw_1.txt , etc.

-----------------------------------------------------------
# remake xml from temp_pw_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue170/issue84pw/
cp temp_pw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue170/issue84pw/


================================================
INSTALLATION
sync to github:

------------------
# csl-orig 
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue170/issue84pw/
diff temp_pw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
# git commit -m "issue84pw  #170"   wrong commit message!

git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue170/issue84pw/
The actual commit.
https://github.com/sanskrit-lexicon/csl-orig/commit/891097589f0072ce6be52e5059340548153b9df7
------------------------
# csl-corrections
cd /c/xampp/htdocs/cologne/csl-corrections
git pull
git add .
git commit -m "Ref: https://github.com/sanskrit-lexicon/PWG/issues/170 (issue84pw)"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue170/issue84pw/

---------------------------------------------------
# sync to Cologne, pull changed repos, redo display
---------------
csl-orig #pull
csl-corrections #pull

---------------
# update displays 
cd csl-pywork/v02
sh generate_dict.sh pw  ../../PWScan/2020/

-----------------------------------------------------
# sync issue170/issue84pw/ to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue170/issue84pw/
git pull
git add .
git commit -m "#170 issue84pw"
git push

------------------------------------------------------------
THE END
