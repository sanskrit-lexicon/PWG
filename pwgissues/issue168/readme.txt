issue168/readme.txt
10-06-2025 begun ejf
0500	PAÑCAT. ed. orn.	PAÑCATANTRA Kosegarten ed. orn.


Ref: https://github.com/sanskrit-lexicon/PWG/issues/86

This issue168 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue168

-----------------
pdf: /e/pdfwork/pantanorn/pantankoseorn.pdf
   source link provided by Andhrabharati
     https://github.com/sanskrit-lexicon/PWG/issues/160#issuecomment-3368736024
     
----------------------------------------
index: prepared by funderburkjim

# prepare preliminary form of index, for all ipages 1-64
python prep_index.py index.txt
# manually add the tantra (always 1) and fromv, tov

-------------------------------------------
format
epage   tantra  fromv   tov     ipage
8       0       1       4       1
9       0       5       5       2
10      1       1       3a      3
11      1       3b      4       4

A separate 'app0' is needed for page navigation,
  since a couple of pages have no verses.
  
 
-------------------------------------------
# construct index.js, and check for internal consistencies
python make_js_index.py index.txt index.js

----------------------------------------
app construction.
3 apps are needed:
app2 -- (tantra,shloka) see 
app1 -- (ipage,line-number)  
app0 -- ipage

See sanskrit-lexicon-scans/pantankoseorn/ for the apps.
index.txt, index.js and make_js_index.py are used

----------------------------------------
local copies of dictionaries with links
----------------------------------------
# get temporary local copy of dictionaries for checking
# only pwg has links to Kosegarten ed. orn.
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt


-------------------------------------------

Pañcat.
-------
PWG: PAÑCAT. [0-9]+,[0-9]+\.


first lines of index
page	tantram	fromv	tov	ipage
17	0	1	4	3
18	0	5	10	4
19	0	11	11	5
20	1	1	8a	6
21	1	8b	16	7


------
# construct index.js, and check for internal consistencies
python make_js_index.py index.txt index.js

#
-----------------------------------------------------
check for fixes.

lsfix2.py is modified:
old: a1 = '([0-9]+)'
new: a1 = '([0-9I]+)' (twice)

# option 'pwga' uses 'PAÑCAT. ed. orn.'
python lsfix2.py pwga temp_pwg_0.txt lsfix2_pwg_0_a.txt
(None,2),(True,284),(fixed,16),(all,302) lsfix2_pwg_0_a.txt

# option 'pwgb' uses 'ed. orn.'
python lsfix2.py pwgb temp_pwg_0.txt lsfix2_pwg_0_b.txt
(False,1),(None,2),(True,149),(fixed,4),(all,156) lsfix2_pwg_0_b.txt


cp temp_pwg_0.txt temp_pwg_1.txt

edit temp_pwg_1.txt to resolve None in lsfix2_pwg_0_a.txt
  Also resolve the False, None, and fixed in lsfix2_pwg_0_b.txt

# rerun lsfix2 with pwg_1

python lsfix2.py pwga temp_pwg_1.txt lsfix2_pwg_1_a.txt
(True,286),(fixed,16),(all,302) lsfix2_pwg_1_a.txt

python lsfix2.py pwgb temp_pwg_1.txt lsfix2_pwg_1_b.txt
(True,161),(all,161) lsfix2_pwg_1_b.txt

----------------------
temp_pwg_2.txt from the 'fixed' in lsfix2_pwg_1_a.txt

python dict_replace2.py temp_pwg_1.txt lsfix2_pwg_1_a.txt temp_pwg_2.txt

apply_repls: 16 lines changed
----------------------
remake local displays using temp_pwg_2.txt

cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue168
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue168

---------------------------------------------------
@lsfix2 file with pwg_2

# 'PAÑCAT. ed. orn.'
python lsfix2.py pwga temp_pwg_2.txt lsfix2_pwg_2_a.txt
(True,321),(all,321) lsfix2_pwg_2_a.txt

 (- 321 284) 37 additional links
 
# 'ed. orn.'
python lsfix2.py pwgb temp_pwg_2.txt lsfix2_pwg_2_b.txt
(True,161),(all,161) lsfix2_pwg_2_b.txt

(- 161 149)  12 additional links

---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
9 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
16 changes written to change_pwg_2.txt

=====================================================

INSTALLATION
sync to github:

------------------
# csl-orig 
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue168
diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue168  splitting 'PAÑCAT. ed. orn.'
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------
# csl-websanlexicon
cd /c/xampp/htdocs/cologne/csl-websanlexicon
git pull
git add .
git commit -m "issue168  splitting 'PAÑCAT. ed. orn.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue168

------------------------
# csl-apidev
cd /c/xampp/htdocs/cologne/csl-apidev
git pull
git add .
git commit -m "issue168  splitting 'PAÑCAT. ed. orn.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue168

------------------------
# csl-pywork
cd /c/xampp/htdocs/cologne/csl-pywork
git pull
git add .
git commit -m "issue168   'PAÑCAT. ed. orn.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue168

---------------------------------------------------
# sync to Cologne, pull changed repos, redo displays for
pwg

---------------
csl-orig #pull
csl-websanlexicon #pull
csl-apidev #pull
# csl-corrections #pull
csl-pywork #pull
---------------
# update displays for pwg
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/

-----------------------------------------------------
# sync issue168 to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue168
git pull
git add .
git commit -m "issue168 'PAÑCAT. ed. orn.' 
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
