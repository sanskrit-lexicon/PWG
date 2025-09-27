
09-18-2025 begun ejf
fix references to 

sanskrit-lexicon-scans/

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue69fix
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue69fix

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
link target sample: https://sanskrit-lexicon-scans.github.io/meghasrnga/app1?N

--------------------------------------
pwg, pw,pwkvn   
links from
pwgbib_input.txt

<ls>Verz. d. Oxf. H. ([0-9]+)

? <ls>Verz. der. Oxf. H.
? <ls>d. Oxf. H.
? <ls>Verz. d. Oxf.
? <ls>Verz. der Oxf. H.

pwbib_input.txt, pwkvnbib_input.txt

<ls>Verz. d. Oxf. H. ([0-9]+)

schauth/tooltip.txt

<ls>Verz. d. Oxf. H. ([0-9]+)

mwauth/tooltip.txt
  Found no references to this work

-------------------------------------------------
We use lsfix2_alt.py, with parmfile lsfix2_parm.py
to examine splitting

For each kosha, try to resolve non-standard references by
splitting multiple references into sequences of standard references,
and making manual changes to the kosha.

See the readme files for these koshas:

readme_pwg.txt 9851 additional standard links;
  
readme_pw.txt  16 additional standard links
  
readme_pwkvn.txt  0 new links.  No changes.
 
readme_sch.txt  0 new links. No changes.
   
================================================
INSTALLATION
sync to github:

------------------
# csl-orig 
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue69fix
diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
diff temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt | wc -l

#diff temp_pwkvn_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt | wc -l
#diff temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt | wc -l
#diff temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt | wc -l

#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue69fix  splitting 'Verz. d. Oxf. H.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue69fix

------------------------
# csl-corrections
cd /c/xampp/htdocs/cologne/csl-corrections
git pull
git add .
git commit -m "issue69fix  splitting 'Verz. d. Oxf. H.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue69fix

---------------------------------------------------
# sync to Cologne, pull changed repos, redo displays for
pwg, pw

---------------
csl-orig #pull
# csl-websanlexicon #pull
# csl-apidev #pull
csl-corrections #pull
# csl-pywork # pull

---------------
# update displays 
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/
sh generate_dict.sh pw  ../../PWScan/2020/
# sh generate_dict.sh pwkvn  ../../PWKVNScan/2020/
# sh generate_dict.sh sch  ../../SCHScan/2020/ 
# sh generate_dict.sh mw  ../../MWScan/2020/

-----------------------------------------------------
# sync issue69fix to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue69fix
git pull
git add .
git commit -m "issue69fix 'Verz. d. Oxf. H.' link splitting
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
