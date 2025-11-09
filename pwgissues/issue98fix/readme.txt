
11-08-2025 begun ejf

fix references to  YĀJÑ. YĀJÑAVALKYA'S Gesetzbuch.

sanskrit-lexicon-scans/

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue98fix
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue98fix

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
adhyāya 1-3, verse
diff ../issue98/yajn_index_v1_edit.txt  /c/xampp/htdocs/sanskrit-lexicon-scans/yajnavalkya/app1/pywork/index.txt

../issue98/yajn_index_v1_edit.txt is the index file to use in chkidx.py


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

readme_pwg.txt 484 additional standard links 
  2 references NOT FOUND in index
      See None items in lsfix3_chkidx_pwg_2.txt
 
readme_pw.txt 5 additional standard links
  0 references inconsistent with index
   
readme_pwkvn.txt  3 additional standard links  
  0 references inconsistent with index.
  
readme_sch.txt 3 additional standard links 
  0 reference inconsistent with index. 
  no changes to temp_sch_0.txt
  
readme_mw.txt  a few changes changes (temp_mw_1.txt)
 Note: see 19 'wrong links' in readme_mw.txt
 
================================================
INSTALLATION
sync to github:

------------------
# csl-orig  
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue98fix
 diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
 diff temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt | wc -l
 diff temp_pwkvn_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt | wc -l
 diff temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt | wc -l
 diff temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue98fix  splitting 'YĀJÑ.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue98fix

------------------------
# csl-corrections
cd /c/xampp/htdocs/cologne/csl-corrections
git pull
git add .
git commit -m "issue98fix  splitting 'YĀJÑ.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue98fix

------------------------
# csl-pywork
cd /c/xampp/htdocs/cologne/csl-pywork
git pull
git add .
git commit -m "issue98fix  splitting 'YĀJÑ.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue98fix

---------------------------------------------------
# sync to Cologne, pull changed repos, redo displays 

---------------
csl-orig #pull
# csl-websanlexicon #pull
# csl-apidev #pull
csl-pywork #pull
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
# sync issue98fix to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue98fix
git pull
git add .
git commit -m "issue98fix 'YĀJÑ.' link splitting
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
