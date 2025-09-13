
09-13-2025 begun ejf
fix references to 01077	MĀLAV.	MĀLAVIKĀGNIMITRA, ed. TULLBERG

sanskrit-lexicon-scans/

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue149fix
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue149fix

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
 2 parms: page, line-number
  https://sanskrit-lexicon-scans.github.io/malavikagni/app2?N,N
 1 parm: verse (1-95)
  https://sanskrit-lexicon-scans.github.io/malavikagni/app1?N


--------------------------------------
links from pwg, pw, pwkvn

<ls>MĀLAV. ([0-9]+),([0-9]+)
<ls>MĀLAV. ([0-9]+)

---- links from sch
<ls>Mālav. ([0-9]+),([0-9]+)
<ls>Mālav. ([0-9]+)

---- links from mw
<ls>Mālav. ([vixlc]+), *([0-9]+)  # uses app3, peculiar to mw. 

-------------------------------------------------
We use lsfix2.py, with parmfile lsfix2_parm.py
to examine splitting

For each kosha, try to resolve non-standard references by
splitting multiple references into sequences of standard references,
and making manual changes to the kosha.

See the readme files for these koshas:

readme_pwg.txt 174 additional standard links;  2 print change.
  10 `MĀLAV. ed. Bomb.  (not linked)
 
readme_pw.txt  no change. 16 non-standard refs remain.
  
readme_pwkvn.txt  no change. 3 non-standard refs remain.
 
readme_sch.txt  no change. 1 non-standard ref remains.

readme_mw.txt  no change.
   These references use app3.
     Example: Calika  <ls n="Mālav. i,">18/19</ls>
   update basicadjust.php -- repos csl-websanlexicon, csl-apidev.
  
================================================
INSTALLATION
sync to github:

------------------
# csl-orig    (just pwg)
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue149fix
diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
#diff temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt | wc -l
#diff temp_pwkvn_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt | wc -l
#diff temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt | wc -l
# diff temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue149fix  splitting 'MĀLAV.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue149fix

------------------------
# csl-websanlexicon
# print changes: pwg 1, pw 2, sch 2
cd /c/xampp/htdocs/cologne/csl-websanlexicon
git pull
git add .
git commit -m "issue149fix  'MĀLAV.' refs in mw
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue149fix

------------------------
# csl-apidev
# print changes: pwg 1, pw 2, sch 2
cd /c/xampp/htdocs/cologne/csl-apidev
git pull
git add .
git commit -m "issue149fix  'MĀLAV.' refs in mw
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue149fix

------------------------
# csl-corrections
# print changes: pwg 1, pw 2, sch 2
cd /c/xampp/htdocs/cologne/csl-corrections
git pull
git add .
git commit -m "issue149fix  splitting 'MĀLAV.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue149fix

---------------------------------------------------
# sync to Cologne, pull changed repos, redo displays for
pwg

---------------
csl-orig #pull
csl-websanlexicon #pull
csl-apidev #pull
csl-corrections #pull

---------------
# update displays for pwg
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/
# sh generate_dict.sh pw  ../../PWScan/2020/
# sh generate_dict.sh pwkvn  ../../PWKVNScan/2020/
# sh generate_dict.sh sch  ../../SCHScan/2020/ 
# sh generate_dict.sh mw  ../../MWScan/2020/

-----------------

-----------------------------------------------------
# sync issue149fix to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue149fix
git pull
git add .
git commit -m "issue149fix 'MĀLAV.' link splitting
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
