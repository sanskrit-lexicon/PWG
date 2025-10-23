
issue101fix
10-21-2025 begun ejf
fix references to Sāhityadarpaṇa

sanskrit-lexicon-scans/

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue101fix
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue101fix

-------------------------------------
# get temporary local copy of koshas
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw_0.txt

--------------------------------------
app1
Provides access in two ways:
- by 'verse' (section)  V = 1 to 757
  - Example: https://sanskrit-lexicon-scans.github.io/sahityadarpana/app1/?200
- by 'internal page 1-343, line number within page
  - Example: https://sanskrit-lexicon-scans.github.io/sahityadarpana/app1/?100,1

-------------------------------------------------
We use lsfix2.py, with parmfile lsfix2_parm.py
to examine splitting

For each kosha, try to resolve non-standard references by
splitting multiple references into sequences of standard references,
and making manual changes to the kosha.

See the readme files for these koshas:

readme_pwg.txt 1330 additional links  temp_pwg_2
  11 refs to an 1828 edition
   1 print change
 
readme_pw.txt  24 additional links  temp_pw_2
  1 refs to an 1828 edition
  2 print changes

readme_pwkvn.txt  1 additional link  temp_kwkvn_1.txt
  1 print change
  
readme_sch.txt 2 additional links   temp_sch_1.txt
  1 print changes
  2 addition refs not linked
    - gotrasKalana : <ls>Sāhityadarpaṇa III,219</ls> actually matches section 219
    - vastUtTAna   : <ls>Sāhityad. VI,133</ls> ...  ed. Bombay 1902
    
readme_mw.txt 0 additional links  temp_mw_1.txt
 See readme_mw_unusual.txt .

================================================
INSTALLATION
sync to github:

------------------
# csl-orig 
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue101fix
diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
diff temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt | wc -l
diff temp_pwkvn_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt | wc -l
diff temp_sch_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt | wc -l
diff temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt | wc -l
#0  as expected
# xxx
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue101fix  splitting Sāhityadarpaṇa refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue101fix

------------------------
# csl-corrections 
# print changes: 
cd /c/xampp/htdocs/cologne/csl-corrections
git pull
git add .
git commit -m "issue101fix  splitting Sāhityadarpaṇa refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue101fix

------------------------
# csl-pywork
# print changes: 
cd /c/xampp/htdocs/cologne/csl-pywork
git pull
git add .
git commit -m "issue101fix  splitting Sāhityadarpaṇa refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue101fix

---------------------------------------------------
# sync to Cologne, pull changed repos, redo displays for
pwg, pw, sch, mw

---------------
csl-orig #pull
# csl-websanlexicon #pull
# csl-apidev #pull
csl-corrections #pull
csl-pywork #pull
---------------
# update displays for pwg, pw, pwkvn, sch, mw
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/
sh generate_dict.sh pw  ../../PWScan/2020/
sh generate_dict.sh pwkvn  ../../PWKVNScan/2020/
sh generate_dict.sh sch  ../../SCHScan/2020/ 
sh generate_dict.sh mw  ../../MWScan/2020/

-----------------------------------------------------
# sync issue101fix to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue101fix
git pull
git add .
git commit -m "issue101fix Sāhityadarpaṇa link splitting
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
