
10-03-2025 begun ejf
fix references to RAGHUVAṂŚA, ed. STENZLER, 1832 

sanskrit-lexicon-scans/

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue100fix
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue100fix

-------------------------------------
# get temporary local copy of koshas
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw_0.txt

--------------------------------------
link target sample: https://sanskrit-lexicon-scans.github.io/raghuvamsa/app1?N,N


-------------------------------------------------
We use lsfix2.py, with parmfile lsfix2_parm.py
to examine splitting

For each kosha, try to resolve non-standard references by
splitting multiple references into sequences of standard references,
and making manual changes to the kosha.

See the readme files for these koshas:
Only a few changes.

readme_pwg.txt 7 new links added.

readme_pw.txt  19 new links added.  
  
readme_pwkvn.txt  no changes.  
 
readme_sch.txt  2 links added.  (temp_sch_1.txt)

readme_mw.txt  1 new link; 2 changes (temp_mw_1.txt)

  
================================================
INSTALLATION
sync to github:

------------------
# csl-orig 
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue100fix
diff temp_pwg_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
diff temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt | wc -l
#diff temp_pwkvn_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt | wc -l
diff temp_sch_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt | wc -l
diff temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue100fix  splitting 'RAGH.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue100fix

------------------------
# csl-corrections 
# print changes: pwg 1
cd /c/xampp/htdocs/cologne/csl-corrections
git pull
git add .
git commit -m "issue100fix  splitting 'RAGH.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue100fix

------------------------
# csl-websanlexicon
cd /c/xampp/htdocs/cologne/csl-websanlexicon
git pull
git add .
git commit -m "issue100fix  splitting 'RAGH.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue100fix

------------------------
# csl-apidev
cd /c/xampp/htdocs/cologne/csl-apidev
git pull
git add .
git commit -m "issue100fix  splitting 'RAGH.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue100fix

------------------------
# csl-pywork
cd /c/xampp/htdocs/cologne/csl-pywork
git pull
git add .
git commit -m "issue100fix  splitting 'RAGH.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue100fix

---------------------------------------------------
# sync to Cologne, pull changed repos, redo displays for
pwg, pw, sch, mw

---------------
csl-orig #pull
csl-websanlexicon #pull
csl-apidev #pull
csl-corrections #pull
csl-pywork #pull
---------------
# update displays for pwg, pw, pwkvn, sch
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/
sh generate_dict.sh pw  ../../PWScan/2020/
# sh generate_dict.sh pwkvn  ../../PWKVNScan/2020/
sh generate_dict.sh sch  ../../SCHScan/2020/ 
sh generate_dict.sh mw  ../../MWScan/2020/

-----------------

-----------------------------------------------------
# sync issue100fix to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue100fix
git pull
git add .
git commit -m "issue100fix 'RAGH.' link splitting
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
