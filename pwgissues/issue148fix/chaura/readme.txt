issue148fix/chaura/readme.txt
08-02-2025 begun ejf
fix references to Caurapañcāśikā

sanskrit-lexicon-scans/

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue148fix/chaura
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue148fix/chaura

-------------------------------------
# get temporary local copy of pwg
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue148fix/chaura
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt

# generate a copy for manual changes
cp temp_pwg_0.txt temp_pwg_1.txt
--------------------------------------
3 forms of reference:
lscode:  CAURAP. 
1 parameter

We use lsfix2.py, with parmfile lsfix2_parm.py
to examine splitting

-------------------------------------------------
python lsfix2.py dummy temp_pwg_0.txt lsfix2_0.txt
377 lines written to lsfix2_0.txt
(True, 1) 361
(None, 1) 3
('fixed', 1) 12
(False, 1) 1


Resolve the None and False  by edits to temp_pwg_1.txt

---------------
python lsfix2.py dummy temp_pwg_1.txt lsfix2_1.txt
378 lines written to lsfix2_1.txt
(True, 1) 364
('fixed', 1) 14

All ok.

----------------------------
generate temp_pwg_2.txt from temp_pwg_1.txt and the 'fixed' elements

python dict_replace2.py temp_pwg_1.txt lsfix2_1.txt temp_pwg_2.txt
378 kept.
378 lines read from lsfix2_1.txt
14 lines to change
apply_repls: 14 lines changed
1

-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue148fix/chaura
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue148fix/chaura
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

python lsfix2.py dummy temp_pwg_2.txt lsfix2_2.txt
393 lines written to lsfix2_2.txt
(True, 1) 393

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
4 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
14 changes written to change_pwg_2.txt


============================================================
sync to github:
------------------
# csl-orig 
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue148fix/chaura
diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue148fix/chaura  splitting 'CAURAP.' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue148fix/chaura

------------------

---------------------------------------------------
sync to Cologne, pull changed repos, redo the pwg displays

---------------
csl-orig #pull
---------------
# update pwg display and pw display and pwkvn display
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/

-----------------

# sync issue148fix/chaura
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue148fix/chaura
git pull
git add .
git commit -m "issue148fix/chaura links to CAURAP.
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

-----------------------------------------------------
# sync issue148fix/chaura to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue148fix/chaura
git pull
git add .
git commit -m "issue148fix/chaura links to CAURAP.
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
