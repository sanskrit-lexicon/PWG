
10-31-2025 begun ejf

fix references to TAITTIRĪYABRĀHMAṆA

sanskrit-lexicon-scans/

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue144fix
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue144fix

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
TAITT. BR. N,N,N,N

index fields
kāṇḍa 1-3, prapāṭhaka, anuvāka, śloka

--------------------------------------
links from pwg, pw, pwkvn

<ls>TAITT. BR. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)
TBR.
TAITTIRĪYA

---- links from sch
<ls>TAITT. BR. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)
TBr.	(PW) TAITTIRĪYA BRĀHMAṆA (ROTH). 

---- links from mw
<ls>TBr. ([vixlc]+), ([0-9]+), ([0-9]+), ([0-9]+). 
TBr.
TB.  no parms

-------------------------------------------------
We use lsfix2.py, with parmfile lsfix2_parm.py
to examine splitting

For each kosha, try to resolve non-standard references by
splitting multiple references into sequences of standard references,
and making manual changes to the kosha.

See the readme files for these koshas:

readme_pwg.txt 921  additional standard links (TBR. N,N,N,N)
  revise pwgbib_input.txt in csl-pywork
  TAITT. BR. has 70 refs.  But this is not our link target
  47 references NOT FOUND in index
  
readme_pw.txt 49 additional standard links
  2 references inconsistent with index. see lsfix3_chkidx_pw_2.txt
  
readme_pwkvn.txt  1 additional standard links  (temp_pwkvn_1.txt)
  1 reference inconsistent with index. see None in lsfix3_chkidx_pwkvn_1.txt
  
readme_sch.txt 8 additional standard links 
  1 reference inconsistent with index. see None in lsfix3_chkidx_sch_2.txt


readme_mw.txt  0 additional standard links (temp_mw_1.txt)
 1 change
  
================================================
INSTALLATION
sync to github:

------------------
# csl-orig    (just pwg)
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue144fix
 diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
 diff temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt | wc -l
 diff temp_pwkvn_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt | wc -l
 diff temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt | wc -l
 diff temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue144fix  splitting 'TAITTIRĪYABRĀHMAṆA' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue144fix

------------------------
# csl-pywork
cd /c/xampp/htdocs/cologne/csl-pywork
git pull
git add .
git commit -m "issue144fix  splitting 'TAITTIRĪYABRĀHMAṆA' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue144fix

---------------------------------------------------
# sync to Cologne, pull changed repos, redo displays for
pwg

---------------
csl-orig #pull
# csl-websanlexicon #pull
# csl-apidev #pull
csl-pywork #pull
# csl-corrections #pull


---------------
# update displays for pwg, etc.
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/
sh generate_dict.sh pw  ../../PWScan/2020/
sh generate_dict.sh pwkvn  ../../PWKVNScan/2020/
sh generate_dict.sh sch  ../../SCHScan/2020/ 
sh generate_dict.sh mw  ../../MWScan/2020/

-----------------------------------------------------
# sync issue144fix to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue144fix
git pull
git add .
git commit -m "issue144fix 'TAITTIRĪYABRĀHMAṆA' link splitting
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
