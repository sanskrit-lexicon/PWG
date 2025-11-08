
11-06-2025 begun ejf

fix references to VĀJASANEYISAM̃HITĀ

sanskrit-lexicon-scans/

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue124fix
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue124fix

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

link target vajasasa

index fields  2 parameters
adhyāya 1-40, verse

--------------------------------------
links from pwg, pw, pwkvn, sch, mw

<ls>VS. ([0-9]+),([0-9]+)

-------------------------------------------------
We use lsfix2.py, with parmfile lsfix2_parm.py
to examine splitting

For each kosha, try to resolve non-standard references by
splitting multiple references into sequences of standard references,
and making manual changes to the kosha.

See the readme files for these koshas:

readme_pwg.txt 1357 additional standard links 
  19 references NOT FOUND in index
      See None items in lsfix3_chkidx_pwg_2.txt
  Note:  2 changes to index.txt ---
    TODO:  install into vajasasa link target app1
 1048 matches for "VS. PRĀT." not linked
   2 matches for "VS. ANUKR." not linked

readme_pw.txt 22 additional standard links
  0 references inconsistent with index. see lsfix3_chkidx_pw_2.txt
  Note: inconsistency found and corrected by print change (hw = sabva)
  
readme_pwkvn.txt  0 additional standard links  
  0 references inconsistent with index.
  no changes to temp_pwkvn_0.txt
  
  
readme_sch.txt 0 additional standard links 
  0 reference inconsistent with index. 
  no changes to temp_sch_0.txt
  
readme_mw.txt  5 changes (temp_mw_1.txt)
 
================================================
INSTALLATION
sync to github:

------------------
# csl-orig  
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue124fix
 diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
 diff temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt | wc -l
# diff temp_pwkvn_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt | wc -l
# diff temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt | wc -l
 diff temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue124fix  splitting 'VĀJASANEYISAM̃HITĀ' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue124fix

------------------------
# csl-corrections
cd /c/xampp/htdocs/cologne/csl-corrections
git pull
git add .
git commit -m "issue124fix  splitting 'VĀJASANEYISAM̃HITĀ' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue124fix

---------------------------------------------------
# sync to Cologne, pull changed repos, redo displays 

---------------
csl-orig #pull
# csl-websanlexicon #pull
# csl-apidev #pull
# csl-pywork #pull
csl-corrections #pull

---------------
# update displays for pwg, etc.
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/
sh generate_dict.sh pw  ../../PWScan/2020/
sh generate_dict.sh pwkvn  ../../PWKVNScan/2020/
sh generate_dict.sh sch  ../../SCHScan/2020/ 
sh generate_dict.sh mw  ../../MWScan/2020/

-----------------------------------------------------
# sync issue124fix to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue124fix
git pull
git add .
git commit -m "issue124fix 'VĀJASANEYISAM̃HITĀ' link splitting
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
