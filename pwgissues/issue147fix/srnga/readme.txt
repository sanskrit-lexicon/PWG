
09-16-2025 begun ejf
fix references to ŚṚṄGĀRAT. = ŚṚṄGĀRATILAKA

sanskrit-lexicon-scans/

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue147fix/srnga/
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue147fix/srnga/

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
link target sample: https://sanskrit-lexicon-scans.github.io/meghasrnga/app2?N

--------------------------------------
pwg, pw,pwkvn  ŚṚṄGĀRAT. 
links from 
<ls>ŚṚṄGĀRAT. ([0-9]+) pwg, pw, pwkvn
<ls>Śṛṅgt. ([0-9]+) sch
<ls>Śṛṅgār. ([ivxlc]+) mw  (also Śṛṅgārat.)

-------------------------------------------------
We use lsfix2.py, with parmfile lsfix2_parm.py
to examine splitting

For each kosha, try to resolve non-standard references by
splitting multiple references into sequences of standard references,
and making manual changes to the kosha.

See the readme files for these koshas:

readme_pwg.txt  19 additional standard links  (temp_pwg_1.txt)

readme_pw.txt   No instances of ls = ŚṚṄGĀRAT. 
  
readme_pwkvn.txt  No instances of ls = ŚṚṄGĀRAT. 
 
readme_sch.txt  Our meghasrnga link target is NOT
  the target for 'Śṛṅgt.' references in sch.
  The target for sch is Śṛṅgāratilakabhāṇa ed. Kāvyamālā Nr. 44.
  changes made to basicadjust in csl-websanlexicon to deactivate
  'Śṛṅgt.' references
  163 references, half with 1 parameter, half with 2 parameters.
  
readme_mw.txt  0 new links. No changes.
  
================================================
INSTALLATION
sync to github:

------------------
# csl-orig 
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue147fix/srnga/
diff temp_pwg_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
#diff temp_pw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt | wc -l
#diff temp_pwkvn_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt | wc -l
#diff temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt | wc -l
#diff temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue147fix/srnga/  splitting 'ŚṚṄGĀRAT.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue147fix/srnga/

------------------------
# csl-websanlexicon
# basicadjust
cd /c/xampp/htdocs/cologne/csl-websanlexicon
git pull
git add .
git commit -m "issue147fix/srnga/  splitting 'ŚṚṄGĀRAT.' refs (sch) basicadjust
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue147fix/srnga/

------------------------
# csl-apidev
# basicadjust
cd /c/xampp/htdocs/cologne/csl-apidev
git pull
git add .
git commit -m "issue147fix/srnga/  splitting 'ŚṚṄGĀRAT.' refs (sch) basicadjust
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue147fix/srnga/

---------------------------------------------------
# sync to Cologne, pull changed repos, redo displays for
pwg, pw, sch

---------------
csl-orig #pull
csl-websanlexicon #pull
csl-apidev #pull
# csl-corrections #pull
# csl-pywork # pull

---------------
# update displays 
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/
sh generate_dict.sh pw  ../../PWScan/2020/
sh generate_dict.sh pwkvn  ../../PWKVNScan/2020/
sh generate_dict.sh sch  ../../SCHScan/2020/ 
sh generate_dict.sh mw  ../../MWScan/2020/


-----------------------------------------------------
# sync issue147fix/srnga/ to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue147fix/srnga/
git pull
git add .
git commit -m "issue147fix/srnga/ 'ŚṚṄGĀRAT.' link splitting
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
