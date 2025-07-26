issue123fix/readme.txt
07-25-2025 begun ejf
fix references to 'N.'
sanskrit-lexicon-scans/bchrest1


Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue93fix/nala
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93fix/nala

-------------------------------------
# get temporary local copy of pwg
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93fix/nala
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt

# generate a copy for manual changes
cp temp_pwg_0.txt temp_pwg_1.txt

--------------------------------------
# edit lsfix_parm.py
targetobj = {
 'dummy': 
   {'dictcode': 'pwg',
    'lscode': 'N.',
    'nparm': 2,
    }
 }
----------------------------------------

Necessary to revise lsfix.py.
For lscode 'N.', there are many unwanted regular-expression matches
  becuase the the period.  
python lsfix.py dummy temp_pwg_0.txt lsfix_0.txt

3293 lines written to lsfix_0.txt
True 2189
None 951
fixed 149
False 4

Resolve False by changes to temp_pwg_1.txt

H. ś. = die Śeṣa's zu HEMACANDRA'S ABHIDHĀNACINTĀMAṆI

# rerun lsfix on temp_pwg_1.txt
python lsfix.py dummy temp_pwg_1.txt lsfix_1.txt 
3297 lines written to lsfix_1.txt
True 2197
None 951
fixed 149

------------------------------------------------

Many of  None cases are believed to be 'Notes' associated with preceding ls codes.


------------------------------------
# Generate temp_pwg_1a.txt

python make_1a.py temp_pwg_1.txt temp_pwg_1a.txt

python lsfix.py dummy temp_pwg_1a.txt lsfix_1a.txt 
2463 lines written to lsfix_1a.txt
True 2214
None 92
fixed 156

The None lines are refs to two other editions of Nala story:
88 of the None lines are 'BOPP'
4 of the None lnes are 'BRUCE'



Since there are no None/False items, we are ready to
install the 'fixed' changes

-------------------------------------------------------------
create version of kosha with the 'fixed' items

python dict_replace.py temp_pwg_1a.txt lsfix_1a.txt temp_pwg_2.txt
47 lines to change
apply_repls: 47 lines changed
1129105 lines written to temp_pwg_2.txt

# apply lsfix.py to temp_pwg_2.txt
python lsfix.py dummy temp_pwg_2.txt lsfix_2.txt
2817 lines written to lsfix_2.txt
True 2725
None 92

88 of the None lines are 'BOPP'
4 of the None lnes are 'BRUCE'

82 matches for "<span>" in buffer: temp_pwg_2.txt
 These to be changed sometime in future.
 
-------------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93fix/nala
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# expect 'ok'
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93fix/nala
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
# documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
496 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_1a.txt change_pwg_1a.txt
1437 changes written to change_pwg_1a.txt

python diff_to_changes_dict.py temp_pwg_1a.txt temp_pwg_2.txt change_pwg_2.txt
156 changes written to change_pwg_2.txt

============================================================
sync to github:
------------------
csl-orig # git pull
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "PWG: issue93fix/nala
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93fix/nala
-----------------
csl-corrections
 NONE
-----------------

# issue93fix
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93fix
git add .
git commit -m "issue93fix/nala
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
---------------------------------------------------
sync to Cologne, pull changed repos, redo the pwg displays


------------------------------------------------------------
THE END
