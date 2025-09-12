
09-11-2025 begun ejf
fix references to 02512	KUMĀRAS.	KUMĀRASAM̃BHAVA, ed. STENZLER

sanskrit-lexicon-scans/

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue146fix
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue146fix

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

<ls>KUMĀRAS. ([0-9]+),([0-9]+)

---- links from sch
<ls>Kumāras. ([0-9]+),([0-9]+)

---- links from mw
<ls>Kum. ([vixlc]+), *([0-9]+)

-------------------------------------------------
We use lsfix2.py, with parmfile lsfix2_parm.py
to examine splitting

For each kosha, try to resolve non-standard references by
splitting multiple references into sequences of standard references,
and making manual changes to the kosha.

See the readme files for these koshas:

readme_pwg.txt 356 additional standard links;  1 print change.
  6 matches for "[0-9][0-9]," in buffer: lsfix2_pwg_2.txt
  5 matches for "[89],"
 So, 11 cases parm1>7 -- 1868 edition?
 
readme_pw.txt  10 new links added.  2 print change;  parm1>7 1838 edition?
  33 cases parm1>7 --  1868 edition?
  
readme_pwkvn.txt  1 change (temp_pwkvn_1.txt)  
 
readme_sch.txt  8 new links added. print changes
   13 cases parm1>7 -- 1868 edition?

readme_mw.txt  no changes.
   15 cases parm1>7 -- 1868 edition?
  
================================================
INSTALLATION
sync to github:

------------------
# csl-orig 
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue146fix
diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
diff temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt | wc -l
diff temp_pwkvn_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt | wc -l
diff temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt | wc -l
# diff temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue146fix  splitting 'KUMĀRAS.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue146fix

------------------------
# csl-corrections
# print changes: pwg 1, pw 2, sch 2
cd /c/xampp/htdocs/cologne/csl-corrections
git pull
git add .
git commit -m "issue146fix  splitting 'KUMĀRAS.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue146fix

---------------------------------------------------
# sync to Cologne, pull changed repos, redo displays for
pwg, pw, pwkvn, sch, mw

---------------
csl-orig #pull
#csl-websanlexicon #pull
# csl-apidev #pull
csl-corrections #pull

---------------
# update displays for pwg, pw, pwkvn, sch
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/
sh generate_dict.sh pw  ../../PWScan/2020/
sh generate_dict.sh pwkvn  ../../PWKVNScan/2020/
sh generate_dict.sh sch  ../../SCHScan/2020/ 
# sh generate_dict.sh mw  ../../MWScan/2020/

-----------------

-----------------------------------------------------
# sync issue146fix to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue146fix
git pull
git add .
git commit -m "issue146fix 'KUMĀRAS.' link splitting
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
