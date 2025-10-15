
10-10-2025 begun ejf
fix references t Ramayana (Bombay edition - prakshipta)

sanskrit-lexicon-scans/

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue75fix
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue75fix

-------------------------------------
# get temporary local copy of koshas
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw_0.txt

--------------------------------------
link target sample: https://sanskrit-lexicon-scans.github.io/ramayanabom/app1?N,N,N,N
or app1?N,N,N

-------------------------------------------------
link reference forms
pwg, pw, pwkvn, sch
"R. ed. Bomb. N,N,N,N" or "R. ed. Bomb. N,N,N" or "R. 7,N,N,N" or "R. 7,N,N"
Also 2 parameters (basicadjust inserts '1' as 3rd parameter)

-----
mw  
Same, except 1st parameter is roman

-------------------------------------------------
We use lsfix2.py, with parmfile lsfix2_parm.py
to examine splitting

For each kosha, try to resolve non-standard references by
splitting multiple references into sequences of standard references,
and making manual changes to the kosha.

See the readme files for these koshas:

readme_pwg.txt 19 links added.  temp_pwg_1.txt

readme_pw.txt  132 additional links  temp_pw_2.txt
     Revise pwbib_input.txt  (pywork repo)
     
readme_pwkvn.txt 17 additional links temp_pwkvn_1.txt
     
readme_sch.txt  69 additional links  temp_sch_1.txt
 Revise basicadjust (csl-websanlexicon repo) for R. N,N,N
 
  
readme_mw.txt x additional links

================================================
INSTALLATION
sync to github:

------------------
# csl-orig 
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue75fix
diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
diff temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt | wc -l
# diff temp_pwkvn_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt | wc -l
diff temp_sch_1a.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt | wc -l
diff temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt | wc -l
#0  as expected
# xxx
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue75fix  splitting 'RĀJAT.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue75fix

------------------------
# csl-corrections 
# print changes: pwg 1
cd /c/xampp/htdocs/cologne/csl-corrections
git pull
git add .
git commit -m "issue75fix  splitting 'RĀJAT.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue75fix

------------------------
# csl-websanlexicon
cd /c/xampp/htdocs/cologne/csl-websanlexicon
git pull
git add .
git commit -m "issue75fix  splitting 'RĀJAT.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue75fix

------------------------
# csl-apidev
cd /c/xampp/htdocs/cologne/csl-apidev
git pull
git add .
git commit -m "issue75fix  splitting 'RĀJAT.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue75fix

---------------------------------------------------
# sync to Cologne, pull changed repos, redo displays for
pwg, pw, sch, mw

---------------
csl-orig #pull
csl-websanlexicon #pull
csl-apidev #pull
csl-corrections #pull
# csl-pywork #pull
---------------
# update displays for pwg, pw, pwkvn, sch, mw
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/
sh generate_dict.sh pw  ../../PWScan/2020/
sh generate_dict.sh pwkvn  ../../PWKVNScan/2020/
sh generate_dict.sh sch  ../../SCHScan/2020/ 
sh generate_dict.sh mw  ../../MWScan/2020/

-----------------------------------------------------
# sync issue75fix to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue75fix
git pull
git add .
git commit -m "issue75fix 'RĀJAT.' link splitting
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
