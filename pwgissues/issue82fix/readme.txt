issue82fix/readme.txt
08-01-2025 begun ejf
fix references to bhagavata purana

sanskrit-lexicon-scans/

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue82fix
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue82fix

-------------------------------------
# get temporary local copy of pwg
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue82fix
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt

# generate a copy for manual changes
cp temp_pwg_0.txt temp_pwg_1.txt
--------------------------------------
3 forms of reference:
lscode:  BHĀG. P.
3 parameters.

Note: There are 16 instances of `BHĀG. P. N,N`.
basicadjust.php previously had (experimental) code to link
 these as `BHĀG. P. N,N,1`
However, this now viewed as suspect, and the basicadjust code is
commente out.
We use lsfix2.py, with parmfile lsfix2_parm.py
to examine splitting

-------------------------------------------------
bhagp:  
python lsfix2.py bhagp temp_pwg_0.txt lsfix2_0.txt
30290 lines written to lsfix2_0.txt
(True, 3) 30267
(None, 3) 22
(False, 3) 1

Resolve the None and False  by edits to temp_pwg_1.txt

bhagp_einl_pwg.txt   # references to Preface of burnouf vol 1 of 'BHĀG. P.'
 (bhag

python lsfix2.py bhagp temp_pwg_1.txt lsfix2_1.txt
30286 lines written to lsfix2_1.txt
(True, 3) 30270
(None, 3) 16

The 16 'None' cases are 2-parameter references 'BHĀG. P. N,N',
whose links are currently unresolved.
bhagp_2parm.txt  extracts these 16 cases.

----------------------------
There are also several references (in pwg and pw)
'BHĀG. P. ed. Bomb. N,N,N'
Change to basicadjust.php to handle this form for pw, pwg.
-
python lsfix2.py bhagpbom temp_pwg_1.txt lsfix2_bom_1.txt
15 lines written to lsfix2_bom_1.txt
(True, 3) 11
('fixed', 3) 4

----------------------------
generate temp_pwg_2.txt from temp_pwg_1.txt and the 'fixed' elements

cat lsfix2_1.txt lsfix2_bom_1.txt > lsfix2_all_1.txt

python dict_replace2.py temp_pwg_1.txt lsfix2_all_1.txt temp_pwg_2.txt

Apply the fixed changes.


-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue82fix
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue82fix
-- end of 'remake xml ...'

---------------------------
How to handle xmlchk error (documentation)
1. Open /c/xampp/htdocs/cologne/pwg/pywork/pwg.xml in Emacs
 use C-cC-n to find xml errors.
 Make correction in temp_pwg_1.txt
 When done
2. rerun next two
python lsfix.py dummy temp_pwg_1.txt lsfix_1.txt 
python dict_replace.py temp_pwg_1.txt lsfix_1.txt temp_pwg_2.txt
3. Redo the 'remake xml ...' steps.
   continue these steps until xmlchk  says 'ok'.
---- end of 'How to handle xmlchk error'
-------------------------------------------------------------
Create Some documentation files

python lsfix2.py bhagp temp_pwg_2.txt lsfix2_2.txt
30286 lines written to lsfix2_2.txt
(True, 3) 30270
(None, 3) 16

python lsfix2.py bhagpbom temp_pwg_2.txt lsfix2_bom_2.txt
19 lines written to lsfix2_bom_2.txt
(True, 3) 19


---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
15 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
4 changes written to change_pwg_2.txt


============================================================
sync to github:
------------------
# csl-orig 
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue82fix
diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue82fix  splitting 'BHĀG. P.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue82fix

------------------
# csl-websanlexicon (basicadjust.php)
cd /c/xampp/htdocs/cologne/csl-websanlexicon/
git pull
git add .
git commit -m "issue82fix  splitting 'BHĀG. P.' refs
cd Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue82fix

------------------
# csl-apidev (basicadjust.php)
cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
sh apidev_copy.sh
cd /c/xampp/htdocs/cologne/csl-apidev/
git pull
git add .
git commit -m "issue82fix  splitting 'BHĀG. P.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue82fix

------------------
# csl-pywork ()
cd /c/xampp/htdocs/cologne/csl-pywork/
git pull
git add .
git commit -m "pwgbig_input.txt  edit"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue82fix

---------------------------------------------------
sync to Cologne, pull changed repos, redo the pwg displays

---------------
csl-orig #pull
csl-websanlexicon # pull
csl-apidev # pull
csl-pywork # pull
---------------
# update pwg display and pw display and pwkvn display
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/
sh generate_dict.sh pw  ../../PWScan/2020/
sh generate_dict.sh pwkvn  ../../PWKVNScan/2020/

-----------------

# sync issue82fix
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue82fix
git pull
git add .
git commit -m "issue82fix links to bhagavatapurana
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

-----------------------------------------------------
# sync issue82fix to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue82fix
git pull
git add .
git commit -m "issue82fix links to amara_dlc 
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
