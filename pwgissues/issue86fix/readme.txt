issue86fix/readme.txt
09-29-2025 begun ejf
fix references to  Pañcatantra, Kosegarten, 1848  

sanskrit-lexicon-scans/

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue86fix
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue86fix

-------------------------------------
# get temporary local copy of koshas
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue86fix
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw_0.txt

=====================================================
split work for pwg

see readme_pwg.txt 

Add about 1165 additional links to target
 about 500 references to 'PAÑCAT. ed. orn.'  -- a different link target
    Some marked as 'ed. orn.'
 From Google Gemini:
    Meaning: 'Ed. orn.' is an abbreviation for ēditiō ōrnātior (Latin for "more ornamented edition") or textus ornatior ("more ornamented text").

The Text: This refers to the version of the Pañcatantra finalized by the Jaina monk Pūrṇabhadra in 1199 CE.
https://archive.org/details/panchatantracoll00purnuoft/page/n1/mode/2up
  Harvard Oriental Series: Johannes Hertel  1908.
  
 about 20 to 'PAÑCAT. ed. Bomb.' -- a different target

temp_pwg_2.txt
=====================================================
split work for pw

see readme_pw.txt 
52 additional standard links
temp_pw_2.txt
print changes

=====================================================
split work for pwkvn
see readme_pwkvn.txt
No changes made

=====================================================
Split work for sch

see readme_sch.txt
4 additional standard links  temp_sch_2.txt

=====================================================
split work for mw

See readme_mw.txt
Several print changes and typo changes.
use temp_mw_1.txt
python lsfix2.py mw2 temp_mw_0.txt lsfix2_mw2_0.txt

Changes to csl-websanlexicon (basicadjust) and csl-apidev
About 100 instances with 3 parameters -- basicadjust does
 not link to pantankose for these. These are probably Bombay edition.
 
============================================================
Ready
============================================================
sync to github:
------------------
# csl-orig 
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue86fix
diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
#0  expected
diff temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt | wc -l
#0  expected
diff temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt | wc -l
#0  expected
diff temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt | wc -l
#0  expected

cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue86fix  splitting 'PAÑCAT. ' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
# 4 files changed, 890 insertions(+), 890 deletions(-)
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue86fix

------------------
# csl-websanlexicon DONE
cd /c/xampp/htdocs/cologne/csl-websanlexicon
git pull
git add .
git commit -m "issue86fix  splitting 'PAÑCAT. ' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue86fix

------------------
# csl-apidev DONE
cd /c/xampp/htdocs/cologne/csl-apidev
git pull
git add .
git commit -m "issue86fix  splitting 'PAÑCAT. ' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue86fix

------------------
# csl-pywork

------------------
# csl-corrections  DONE
cd /c/xampp/htdocs/cologne/csl-corrections
git pull
git add .
git commit -m "issue86fix  'PAÑCAT. '
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue86fix

---------------------------------------------------
sync to Cologne
# connect to cologne server via ssh
---------------
# pull changed repos
csl-orig # pull
csl-websanlexicon # pull
csl-apidev # pull
$ csl-pywork # pull
csl-corrections # pull
---------------
# redo the displays for pwg, pw, sch
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/
sh generate_dict.sh pw  ../../PWScan/2020/
sh generate_dict.sh sch  ../../SCHScan/2020/

sh generate_dict.sh pwkvn  ../../PWKVNScan/2020/
sh generate_dict.sh mw  ../../MWScan/2020/

-----------------------------------------------------
# sync issue86fix to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue86fix
git pull
git add .
git commit -m "issue86fix 'PAÑCAT. ' link splitting
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
