
10-23-2025 begun ejf

fix references to ŚAT. BR. = ŚATAPATHABRĀHMAṆA

sanskrit-lexicon-scans/

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue84fix
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue84fix

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
ŚAT. BR. N,N,N,N
  (Kāṇḍa 1-14, Adhyāya, Brāhmaṇa, Kaṇḍikā)

--------------------------------------
links from pwg, pw, pwkvn

<ls>ŚAT. BR. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)

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

readme_pwg.txt 8388  additional standard links
  revise pwgbib_input.txt in csl-pywork
  237 references inconsistent with index. see lsfix3_chkidx_pwg_2.txt
  
readme_pw.txt x additional standard links
  29 references inconsistent with index. see lsfix3_chkidx_pw_2.txt
  
readme_pwkvn.txt  0 additional standard links
  no changes
  
readme_sch.txt 31 additional standard links 
  1 index-inconsistent reference, corrected by print change (aRupriyaNgu)

readme_mw.txt  0 additional standard links 
  a few changes (temp_mw_1.txt)
  
================================================
INSTALLATION
sync to github:

------------------
# csl-orig    (just pwg)
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue84fix
diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
diff temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt | wc -l
# diff temp_pwkvn_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt | wc -l
diff temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt | wc -l
diff temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue84fix  splitting 'ŚAT. BR.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue84fix

------------------------
# csl-pywork
cd /c/xampp/htdocs/cologne/csl-pywork
git pull
git add .
git commit -m "issue84fix  splitting 'ŚAT. BR.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue84fix

------------------------
# csl-corrections
cd /c/xampp/htdocs/cologne/csl-corrections
git pull
git add .
git commit -m "issue84fix  splitting 'ŚAT. BR.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue84fix

---------------------------------------------------
# sync to Cologne, pull changed repos, redo displays for
pwg

---------------
csl-orig #pull
# csl-websanlexicon #pull
# csl-apidev #pull
csl-pywork #pull
csl-corrections #pull


---------------
# update displays for pwg
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/
sh generate_dict.sh pw  ../../PWScan/2020/
sh generate_dict.sh pwkvn  ../../PWKVNScan/2020/
sh generate_dict.sh sch  ../../SCHScan/2020/ 
sh generate_dict.sh mw  ../../MWScan/2020/

-----------------------------------------------------
# sync issue84fix to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue84fix
git pull
git add .
git commit -m "issue84fix 'ŚAT. BR.' link splitting
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
