issue159auf/readme.txt
08-10-2025 begun ejf
AITAREYABRĀHMAṆA  Aufrecht ed. 1879

Ref: https://github.com/sanskrit-lexicon/PWG/issues/159

This issue159 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159

-----------------
pdf: /e/pdfwork/aitbr_auf.pdf

The final version of index will be named index.txt

----------------------------------------
# get temporary local copy of koshas
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw_0.txt

----------------------------------------
All the 5 koshas (pwg, pw, pwkvn, sch, mw) have references
to AITAREYABRĀHMAṆA  with either 2 or three parameters.
There are also slight variations in the lscode


We learned that the 3-parameter references are referring
to the Aufrecht edition.  pancika, kandika, khanda  Where khanda is a
sequence number (within kandika) provided by Aufrecht.
We will make a separate link target (aitbr_auf); the work on
this aufrecht edition will be in a separate directory
In local file system, 
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159/auf
See readme.txt in this directory.


Reference forms in koshas
--- pwg  AIT. BR.
3726  nparm=2
   4  nparg=3

** (4055) AIT. BR. with 2 numeric parameters 
** (7) AIT. BR. with 3 numeric parameters 

--- pw AIT. BR.
 127 with nparm=3
  95 nparm=2
 
--- pwkvn AIT. BR.
  39 nparm=3
   3 nparm=2
   
--- sch Ait. Br.
   3 nparm=2
  38 nparm=3
  
--- mw  AitBr.
 168 R,N
 116 R,N,N

--------------------------------------
index.txt format observations
format 7 fields tab-separated values
vol  (=I)
page N
pancika
adhyaya  not used in apps
fromv == kandika
tov   == kandika
ipage
remarks  # optional.

-----------------------------------
# Prepare index.js
python make_js_index.py index.txt index.js
266 Success: Page records read from index.txt
json data written to index.js
pagerecs passes check1_pancika
pagerecs passes check1_kandika

==========================================
apps in sanskrit-lexicon-scans

https://github.com/sanskrit-lexicon-scans/aitbr_auf
# initialize local repo, where the link target apps will be installed.
cd /c/xampp/htdocs/sanskrit-lexicon-scans/
git clone git@github.com:sanskrit-lexicon-scans/aitbr_auf.git

# edit README.md 

# Install apps in aitbr_auf repo
readme_app0.txt  internal page
readme_app1.txt  pancika,kandika  or pancika,kandika,kanda

========================================
--- links from koshas to app
pwg, pw, pwkv, sch, mw
see readme_websanlexicon.txt

========================================
See readme_changes_mw.txt regarding corrections in temp_mw_1.txt
----------------------------
Make one correction to pwg that Jim missed in issue159

cp temp_pwg_0.txt temp_pwg_1.txt
See 'pwg change' below

python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
1 changes written to change_pwg_1.txt

## regenerate pwg displays locally
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159auf
cp temp_pwg_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159auf


'pwg change':
97002 : SaMsa : AIT. BR. 2,2,4 :  AIT. BR. 2,4,6  : print change 

Print changes from readme_changes_mw.txt
37011 : upodAsfp : AitBr. i, 6, 1; 3. : AitBr. vi, 1, 1; 3.  : print change
71518 : canasita : AitBr. i, 6, 8; Sāy. : Sāy. on AitBr. i, 6, 8.  : print change
39426 : ekapAta : Sāy. on AitBr. ii, 19, 9 : Sāy. on AitBr. i, 19, 9  : print change
22727 : AgranTam : AitBr. v, 15, 10 : AitBr. v, 15, 9 : print change
29398 : ilava : AitBr. v, 25, 5 : AitBr. v, 3, 5 : print change Note: yadelavā 
34967 : upanivft : AitBr. vii, 5, 5 : AitBr. vii, 5, 6 : print change

==================================================
Documentation
See the check_*3_ALL.txt files  in directory issue159
Only 3-parameter kosha links use 
---------------------------------------------------

===========================================================
sync to github:
  csl-orig
  csl-corrections (see above 'print change'
  csl-websanlexicon
  csl-apidev
  csl-pywork

------------------
# csl-orig # git pull
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159
diff temp_pwg_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
diff temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt | wc -l
#0  as expected

cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "AITAREYABRĀHMAṆA (Aufrecht) link target correction
Ref: https://github.com/sanskrit-lexicon/PWG/issues/159"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159auf

------------------
# csl-websanlexicon
cd /c/xampp/htdocs/cologne/csl-websanlexicon/
git pull
git add .
git commit -m "AITAREYABRĀHMAṆA (Aufrecht) link target aitbr_auf. 
Ref: https://github.com/sanskrit-lexicon/pwg/issues/159"
git push
----
sh apidev_copy.sh
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159auf

------------------
# csl-apidev
cd /c/xampp/htdocs/cologne/csl-apidev/
git pull
git add .
git commit -m "AITAREYABRĀHMAṆA (Aufrecht) link target aitbr_auf. 
Ref: https://github.com/sanskrit-lexicon/pwg/issues/159"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159auf

------------------
# csl-pywork   TODO TODO
cd /c/xampp/htdocs/cologne/csl-pywork/
git pull
git add .
git commit -m "AITAREYABRĀHMAṆA (Aufrecht) link target aitbr_auf. 
Ref: https://github.com/sanskrit-lexicon/pwg/issues/159"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159auf

------------------
# csl-corrections
cd /c/xampp/htdocs/cologne/csl-corrections/
git pull
git add .
git commit -m "AITAREYABRĀHMAṆA (Aufrecht) link target aitbr_auf. 
Ref: https://github.com/sanskrit-lexicon/pwg/issues/159"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159auf

---------------------------------------------------
sync Cologne to Github, pull changed repos
---------------
csl-orig # pull
csl-corrections # pull
csl-websanlexicon # pull
csl-apidev # pull
csl-pywork # pull
-------------------------------------
# regenerate displays for pwg, pw, pwkvn, mw, [mw not required]

cd csl-pywork/v02

sh generate_dict.sh pwg  ../../PWGScan/2020/
sh generate_dict.sh pw  ../../PWScan/2020/
sh generate_dict.sh pwkvn  ../../PWKVNScan/2020/
sh generate_dict.sh sch  ../../SCHScan/2020/
sh generate_dict.sh mw  ../../MWScan/2020/

--------------------------------------------

# sync this repo PWG (issue159) to github
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue159auf
git pull
git add .
git commit -m "issue159auf #159"
git push

====================================
THE END

