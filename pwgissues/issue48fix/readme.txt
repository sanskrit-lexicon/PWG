
09-15-2025 begun ejf
fix references to MBH Calcutta edition;  also MBH Bombay edition

sanskrit-lexicon-scans/

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue48fix
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue48fix

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

<ls>MBH. ([0-9]+),([0-9]+)   mbhcalc
<ls>MBH. ([0-9]+),([0-9]+),([0-9]+)   mbhbomb


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

readme_pwg.txt 111 additional standard links;  7 print changes
  84 unlinked 'MBH.'
  Almost all links are to mbhcalc (MBH. with 2 parms).
  
  add basicadjust 'MBH. ed. Calc. N,N' csl-websanlexicon
  
readme_pw.txt  510 new links added.  1 print change
  
readme_pwkvn.txt  8 new links.  1 print change
 
readme_sch.txt  118 new links added. 

readme_mw.txt  a few changes. 1 print change.  temp_mw_1.txt
 A few spellings not linked
   (such as <ls>MBh. (ed. Calc.) xii, 2307</ls>
  
================================================
INSTALLATION
sync to github:

------------------
# csl-orig 
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue48fix
diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
diff temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt | wc -l
diff temp_pwkvn_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt | wc -l
diff temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt | wc -l
diff temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue48fix  splitting 'MBH.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue48fix

------------------------
# csl-websanlexicon
# basicadjust
cd /c/xampp/htdocs/cologne/csl-websanlexicon
git pull
git add .
git commit -m "issue48fix  splitting 'MBH.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue48fix

------------------------
# csl-apidev
# basicadjust
cd /c/xampp/htdocs/cologne/csl-apidev
git pull
git add .
git commit -m "issue48fix  splitting 'MBH.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue48fix

------------------------
# csl-corrections
# print changes: mw, pw, pwg, pwkvn
cd /c/xampp/htdocs/cologne/csl-corrections
git pull
git add .
git commit -m "issue48fix  splitting 'MBH.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue48fix

---------------------------------------------------
# sync to Cologne, pull changed repos, redo displays for
pwg, pw, pwkvn, sch, mw

---------------
csl-orig #pull
csl-websanlexicon #pull
csl-apidev #pull
csl-corrections #pull

---------------
# update displays 
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/
sh generate_dict.sh pw  ../../PWScan/2020/
sh generate_dict.sh pwkvn  ../../PWKVNScan/2020/
sh generate_dict.sh sch  ../../SCHScan/2020/ 
sh generate_dict.sh mw  ../../MWScan/2020/

-----------------

-----------------------------------------------------
# sync issue48fix to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue48fix
git pull
git add .
git commit -m "issue48fix 'MBH.' link splitting
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
