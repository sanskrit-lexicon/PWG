issue148fix/bhartr/readme.txt
08-03-2025 begun ejf
fix references to BHAṬṬIKĀVYA

sanskrit-lexicon-scans/

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue143fix
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue143fix

-------------------------------------
# get temporary local copy of pwg
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue143fix
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt

# generate a copy for manual changes
cp temp_pwg_0.txt temp_pwg_1.txt
--------------------------------------
3 forms of reference:
lscode:  BHAṬṬ.
2 parameters

We use lsfix2.py, with parmfile lsfix2_parm.py
to examine splitting

-------------------------------------------------

python lsfix2.py dummy temp_pwg_0.txt lsfix2_0.txt
2550 lines written to lsfix2_0.txt
(True, 2) 2300
('fixed', 2) 178
(None, 2) 70
(False, 2) 2


Resolve the None and False  by edits to temp_pwg_1.txt

------------------------------------------------
# 
python lsfix2.py dummy temp_pwg_1.txt lsfix2_1.txt
2548 lines written to lsfix2_1.txt
(True, 2) 2367
('fixed', 2) 181

All None and False now corrected in temp_pwg_1.txt

----------------------------
# generate temp_pwg_2.txt from temp_pwg_1.txt and the 'fixed' elements

python dict_replace2.py temp_pwg_1.txt lsfix2_1.txt temp_pwg_2.txt
2548 kept.
2548 lines read from lsfix2_1.txt
181 lines to change
apply_repls: 181 lines changed

-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue143fix
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue143fix
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
2773 lines written to lsfix2_2.txt
(True, 2) 2773

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
74 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
181 changes written to change_pwg_2.txt

============================================================
sync to github:
------------------
# csl-orig 
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue143fix
diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue143fix  splitting 'BHAṬṬ. N,N' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue143fix

---------------------------------------------------
sync to Cologne, pull changed repos, redo the pwg displays

---------------
csl-orig #pull

---------------
# update pwg display and pw display and pwkvn display
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/

-----------------

-----------------------------------------------------
# sync issue143fix to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue143fix
git pull
git add .
git commit -m "issue143fix 'BHARTṚ. N,N' link splitting
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
