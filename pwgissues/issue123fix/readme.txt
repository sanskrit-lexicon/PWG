issue123fix/readme.txt
07-24-2025 begun ejf
fix references to 'H. an.'
sanskrit-lexicon-scans/anekārthasaṃgraha

Ref: https://github.com/sanskrit-lexicon/PWG/issues123fix

this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue123fix

-------------------------------------
# get temporary local copy of pwg
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue123fix
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt

# generate a copy for manual changes
cp temp_pwg_0.txt temp_pwg_1.txt

--------------------------------------
# edit lsfix_parm.py
targetobj = {
 'dummy': 
   {'dictcode': 'pwg',
    'lscode': 'H. an.',
    'nparm': 2,
    }
 }
----------------------------------------

python lsfix.py dummy temp_pwg_0.txt lsfix_0.txt

3160 lines written to lsfix_0.txt
True 3090
fixed 47
None 20
False 3


Resolve None and False by changes to temp_pwg_1.txt

H. ś. = die Śeṣa's zu HEMACANDRA'S ABHIDHĀNACINTĀMAṆI

# rerun lsfix on temp_pwg_1.txt
python lsfix.py dummy temp_pwg_1.txt lsfix_1.txt 
3153 lines written to lsfix_1.txt
True 3106
fixed 47

Since there are no None/False items, we are ready to install changes

-------------------------------------------------------------
create version of kosha with the 'fixed' items

python dict_replace.py temp_pwg_1.txt lsfix_1.txt temp_pwg_2.txt
47 lines to change
apply_repls: 47 lines changed
1129105 lines written to temp_pwg_2.txt


-------------------------------------------------------------
-- remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue123fix
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue123fix
-- end of 'remake xml ...'

---------------------------
How to handle xmlchk error;
1. Open /c/xampp/htdocs/cologne/pwg/pywork/pwg.xml in Emacs
 use C-cC-n to find xml errors.
 Make correction in temp_pwg_1.txt
 When done
2. rerun next two
python lsfix.py dummy temp_pwg_1.txt lsfix_1.txt 
python dict_replace.py temp_pwg_1.txt lsfix_1.txt temp_pwg_2.txt

3. Redo the 'remake xml ...' steps.
   continue these steps until xmlchk  says 'ok'.

-------------------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
23 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
47 changes written to change_pwg_2.txt

============================================================
sync to github:
------------------
csl-orig # git pull
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue123fix
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
-----------------
csl-corrections
 NONE
-----------------

# issue123fix
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue123fix
git add .
git commit -m "issue123fix
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
---------------------------------------------------
sync to Cologne, pull changed repos, redo the pwg displays

-------------------------------------------------------------
------------------------------------------------------------
THE END
