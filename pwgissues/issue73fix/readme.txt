
09-13-2025 begun ejf
fix references to M.

sanskrit-lexicon-scans/

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue73fix
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue73fix

-------------------------------------
# get temporary local copy of koshas
----------------------------------------
# get temporary local copy of dictionaries for checking
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw_0.txt

--------------------------------------
link target sample: https://sanskrit-lexicon-scans.github.io/kumaras/app1?N,N


--------------------------------------
links from pwg, pw, pwkvn

<ls>M. ([0-9]+),([0-9]+)

---- links from sch
<ls>M. ([0-9]+),([0-9]+)

---- links from mw
<ls>Mn. ([vixlc]+), *([0-9]+)

-------------------------------------------------
We use lsfix2.py, with parmfile lsfix2_parm.py
to examine splitting

For each kosha, try to resolve non-standard references by
splitting multiple references into sequences of standard references,
and making manual changes to the kosha.

See the readme files for these koshas:

readme_pwg.txt 1 additional standard links (temp_pwg_1.txt)
 
readme_pw.txt  70 new links added. 
  
  [Correction to pwbib_input.txt in pywork]
  
readme_pwkvn.txt  1 change (temp_pwkvn_1.txt)  
 
readme_sch.txt  no changes.
  
readme_mw.txt  30+ links added.  (temp_mw_1.txt)
  Question regarding 11 links like <ls>Mn. i, 6/7</ls> under hw jayAditya
  
================================================
INSTALLATION
sync to github:

------------------
# csl-orig 
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue73fix
diff temp_pwg_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
diff temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt | wc -l
diff temp_pwkvn_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt | wc -l
#diff temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt | wc -l
diff temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue73fix  splitting 'M.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue73fix

---------------------------------------------------
# sync to Cologne, pull changed repos, redo displays for
pwg, pw, pwkvn,  mw

---------------
csl-orig #pull
#csl-pywork #pull
# csl-websanlexicon #pull
# csl-apidev #pull
# csl-corrections #pull

---------------
# update displays for pwg, pw, pwkvn, sch
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/
sh generate_dict.sh pw  ../../PWScan/2020/
sh generate_dict.sh pwkvn  ../../PWKVNScan/2020/
# sh generate_dict.sh sch  ../../SCHScan/2020/ 
sh generate_dict.sh mw  ../../MWScan/2020/

-----------------------------------------------------
# sync issue73fix to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue73fix
git pull
git add .
git commit -m "issue73fix 'M.' link splitting
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
