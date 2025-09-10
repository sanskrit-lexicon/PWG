issue136fix/bhartr/readme.txt
09-08-2025 begun ejf
fix references to KĀTYĀYANA'S ŚRAUTASŪTRĀṆI

sanskrit-lexicon-scans/

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue136fix
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue136fix

-------------------------------------
# get temporary local copy of koshas
----------------------------------------
# get temporary local copy of dictionaries for checking
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw_0.txt


For each kosha, try to resolve non-standard references by
splitting multiple references into sequences of standard references,
and making manual changes to the kosha.

See the readme files for these koshas:
readme_pwg.txt
  3-parameters:  2516 additional links
  2-parameters:   427 additional links (page,linenum)
  discovered 2-parameter links 
  (- (+ 7877 732) (+ 5361 305))
readme_pw.txt 139 links added. some 2-parameter links
readme_pwkvn.txt  no changes 
readme_sch.txt  5 links added
readme_mw.txt  no changes

The main tool is lsfix2.py, parameterized by lsfix2_parm.py

--------------------------------------
---- links from pwg, pw, pwkvn
katysr  app1  adhyaya,kanda,verse
<ls>KĀTY. ŚR. ([0-9]+),([0-9]+),([0-9]+)

---- links from sch
katysr app1
<ls>Kāty. Śr. ([0-9]+),([0-9]+),([0-9]+)

---- links from mw
katysr  app1
<ls>KātyŚr. ([vix]+), *([0-9]+), *([0-9]+), *([0-9]+)

-------------------------------------------------
We use lsfix2.py, with parmfile lsfix2_parm.py
to examine splitting

================================================
INSTALLATION
sync to github:

------------------
# csl-orig 
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue136fix
diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
diff temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt | wc -l
diff temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue136fix  splitting 'KĀTY. ŚR.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue136fix

------------------------
# csl-websanlexicon
cd /c/xampp/htdocs/cologne/csl-websanlexicon
git pull
git add .
git commit -m "issue136fix  splitting 'KĀTY. ŚR.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue136fix


------------------------
# csl-apidev
cd /c/xampp/htdocs/cologne/csl-apidev
git pull
git add .
git commit -m "issue136fix  splitting 'KĀTY. ŚR.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue136fix

------------------------
# csl-corrections (for print changes to pwg)
cd /c/xampp/htdocs/cologne/csl-corrections
git pull
git add .
git commit -m "issue136fix  splitting 'KĀTY. ŚR.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue136fix

---------------------------------------------------
# sync to Cologne, pull changed repos, redo the pwg displays

---------------
csl-orig #pull
csl-websanlexicon #pull
csl-apidev #pull
csl-corrections #pull

---------------
# update displays for pwg, pw, sch
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/
sh generate_dict.sh pw  ../../PWScan/2020/
sh generate_dict.sh sch  ../../SCHScan/2020/

-----------------

-----------------------------------------------------
# sync issue136fix to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue136fix
git pull
git add .
git commit -m "issue136fix 'KĀTY. ŚR.' link splitting
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
