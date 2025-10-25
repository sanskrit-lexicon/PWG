
10-23-2025 begun ejf

fix references to ŚĀK. ŚĀKUNTALA

sanskrit-lexicon-scans/

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue125fix
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue125fix

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
link target sample:
 2 parms: page (3-113), line-number
  https://sanskrit-lexicon-scans.github.io/shakuntala/app2?N,N
 1 parm: verse (1-194)
  https://sanskrit-lexicon-scans.github.io/shakuntala/app1?N


--------------------------------------
links from pwg, pw, pwkvn

<ls>ŚĀK. ([0-9]+),([0-9]+)
<ls>ŚĀK. ([0-9]+)

---- links from sch
<ls>Śāk. ([0-9]+),([0-9]+)
<ls>Śāk. ([0-9]+)

---- links from mw
<ls>Śāk. ([vixlc]+), *([0-9]+)  # uses app3, peculiar to mw. 

-------------------------------------------------
We use lsfix2.py, with parmfile lsfix2_parm.py
to examine splitting

For each kosha, try to resolve non-standard references by
splitting multiple references into sequences of standard references,
and making manual changes to the kosha.

See the readme files for these koshas:

readme_pwg.txt 1667 additional standard links
  approx. (+ 223 428) 651 changes
  269 refs to "ŚĀK. CH." not linked
  9 refs to other editions or spellings
  see 'other references' in readme_pwg.txt
  
 
readme_pw.txt 23 additional standard links
  modify pwbib_input.txt in csl-pywork
  38 'excludes other references'
  
readme_pwkvn.txt  0 additional standard links
  11 'excludes other references'  no changes
  
readme_sch.txt  3 or 4 additional standard links temp_sch_1.txt
  revised schauth/tooltip.txt in pywork
  
readme_mw.txt  0 additional standard links
 There is only one reference to Śāk. with parameters,
 and this does not link to our shakuntala link target.

  
================================================
INSTALLATION
sync to github:

------------------
# csl-orig    (just pwg)
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue125fix
diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
diff temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt | wc -l
# diff temp_pwkvn_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt | wc -l
diff temp_sch_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt | wc -l
# diff temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue125fix  splitting 'ŚĀK.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue125fix

------------------------
# csl-pywork
cd /c/xampp/htdocs/cologne/csl-pywork
git pull
git add .
git commit -m "issue125fix  splitting 'ŚĀK.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue125fix

---------------------------------------------------
# sync to Cologne, pull changed repos, redo displays for
pwg

---------------
csl-orig #pull
# csl-websanlexicon #pull
# csl-apidev #pull
csl-pywork #pull

---------------
# update displays for pwg
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/
sh generate_dict.sh pw  ../../PWScan/2020/
sh generate_dict.sh pwkvn  ../../PWKVNScan/2020/
sh generate_dict.sh sch  ../../SCHScan/2020/ 
sh generate_dict.sh mw  ../../MWScan/2020/

-----------------------------------------------------
# sync issue125fix to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue125fix
git pull
git add .
git commit -m "issue125fix 'ŚĀK.' link splitting
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
