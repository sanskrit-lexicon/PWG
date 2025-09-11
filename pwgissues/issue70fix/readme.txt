issue70fix/bhartr/readme.txt
09-10-2025 begun ejf
fix references to 

sanskrit-lexicon-scans/

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue70fix
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue70fix

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
link target sample: https://sanskrit-lexicon-scans.github.io/kss/?20,216
This is an 'early' display, and does not have a page-navigation component.
--------------------------------------
---- links from pwg, pw, pwkvn
kss  taraṃga,śloka 
<ls>KATHĀS. ([0-9]+),([0-9]+)

---- links from sch
kss 
<ls>Kathās ([0-9]+),([0-9]+)

---- links from mw
kss  
<ls>Kathās. ([vixlc]+), *([0-9]+)
Two instances of 
Kath. ([vixlc]+), *([0-9]+)

-------------------------------------------------
We use lsfix2.py, with parmfile lsfix2_parm.py
to examine splitting

For each kosha, try to resolve non-standard references by
splitting multiple references into sequences of standard references,
and making manual changes to the kosha.

See the readme files for these koshas:
readme_pwg.txt only 5 additional links added (out of 25000!)
  
readme_pw.txt  About 120 new links added.

readme_pwkvn.txt  no changes

readme_sch.txt  11 new links added.

readme_mw.txt  temp_mw_1.txt print changes


================================================
INSTALLATION
sync to github:

------------------
# csl-orig 
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue70fix
diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
diff temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt | wc -l
diff temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt | wc -l
diff temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue70fix  splitting 'KATHĀS.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue70fix


------------------------
# csl-corrections (for print changes to mw)
cd /c/xampp/htdocs/cologne/csl-corrections
git pull
git add .
git commit -m "issue70fix  splitting 'KATHĀS.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue70fix

---------------------------------------------------
# sync to Cologne, pull changed repos, redo displays for pwg, pw, sch, mw

---------------
csl-orig #pull
#csl-websanlexicon #pull
# csl-apidev #pull
csl-corrections #pull

---------------
# update displays for pwg, pw, sch, mw
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/
sh generate_dict.sh pw  ../../PWScan/2020/
sh generate_dict.sh sch  ../../SCHScan/2020/  # done
sh generate_dict.sh mw  ../../MWScan/2020/

-----------------

-----------------------------------------------------
# sync issue70fix to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue70fix
git pull
git add .
git commit -m "issue70fix 'KATHĀS.' link splitting
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
