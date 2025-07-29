issue93fix/dash/readme.txt
07-29-2025 begun ejf
fix references to 'DAŚ. N,N'

sanskrit-lexicon-scans/bchrest1

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue93fix/dash
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93fix/dash

-------------------------------------
# get temporary local copy of pwg
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93fix/dash
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt

# generate a copy for manual changes
cp temp_pwg_0.txt temp_pwg_1.txt
--------------------------------------
Preliminary changes in temp_pwg_1.txt  re issue104fixa
Ref: https://github.com/sanskrit-lexicon/PWG/issues/160#issuecomment-3130710016

15237 : karuRa : H. 369,2 : H. 369,b : PRINT CHANGE  <ls>H. 369,b</ls>
52042 : ballAlasena : <ls>H. 124.</ls>,a : <ls>H. 124,a.</ls>  : markup change
8070 : AcArya : <ls>H. p. 15</ls> : NO CHANGE. Inaccessible in abch2 apps
10027 : itas : H. 7,149. 150 : H. an. 7,49. 50 : print change
     <ls>H. an. 7,49.</ls> <ls n="H. an. 7,">50</ls>  revised markup


--------------------------------------
# edit lsfix_parm.py
targetobj = {
 'dummy': 
   {'dictcode': 'pwg',
    'lscode': 'DAŚ.',
    'nparm': 2,
    }
 }

----------------------------------------
python lsfix.py dummy temp_pwg_0.txt lsfix_0.txt
411 lines written to lsfix_0.txt
True 372
fixed 33
None 5
False 1
----------------------------------------
Resolve None and False by changes to temp_pwg_1.txt

----------------------------

python lsfix.py dummy temp_pwg_1.txt lsfix_1.txt
411 lines written to lsfix_1.txt
True 377
fixed 34

No more False/None !
----------
No unresolved:


-------------------------------
# create temp_pwg_2.txt with the 'fixed' items
# 
python dict_replace.py temp_pwg_1.txt lsfix_1.txt temp_pwg_2.txt
34 lines to change
apply_repls: 34 lines changed

-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93fix/dash
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93fix/dash
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

python lsfix.py dummy temp_pwg_2.txt lsfix_2.txt
447 lines written to lsfix_2.txt
True 447

-------------------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
9 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
34 changes written to change_pwg_2.txt

============================================================
sync to github:
------------------
# csl-orig # git pull
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93fix/dash
diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue93fix/dash  'DAŚ. N,N' 
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93fix/dash

----------------
csl-corrections
 2 print change items above

cd /c/xampp/htdocs/cologne/csl-corrections/
git pull
git add .
git commit -m "issue93fix/dash  'DAŚ. N,N' 
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93fix/dash

---------------------------------------------------
sync to Cologne, pull changed repos, redo the pwg displays

---------------
csl-orig #pull
csl-corrections # pull
---------------
# update pwg display
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/

-----------------

# sync issue93fix/dash
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93fix/dash
git pull
git add .
git commit -m "issue93fix/dash 'DAŚ. N,N' DAŚARATHA'S Death, in bchrest1
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
