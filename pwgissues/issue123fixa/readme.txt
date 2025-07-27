issue123fixa/readme.txt
07-26-2025 begun ejf
fix references to 'an.' 
sanskrit-lexicon-scans/anekārthasaṃgraha


Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue123fixa
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue123fixa

-------------------------------------
# get temporary local copy of pwg
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue123fixa
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt

# generate a copy for manual changes
cp temp_pwg_0.txt temp_pwg_1.txt


--------------------------------------
# edit lsfix_parm.py
targetobj = {
 'dummy': 
   {'dictcode': 'pwg',
    'lscode': 'an.',
    'nparm': 2,
    }
 }
----------------------------------------

python lsfix.py dummy temp_pwg_0.txt lsfix_0.txt

1942 lines written to lsfix_0.txt
True 1910
None 9
fixed 23

----------------------------------------

Resolve None and False by changes to temp_pwg_1.txt
From  Ref: https://github.com/sanskrit-lexicon/PWG/issues/160#issuecomment-3121512678

2 cases of <ls>H. <is>an</is>. which need to be corrected as <ls>H. an.;
(<ls>H. an.).</ls> -> (<ls>H. an.</ls>)

python lsfix.py dummy temp_pwg_1.txt lsfix_1.txt
1942 lines written to lsfix_1.txt
True 1910
None 9
fixed 23

Edut tenp_pwg_1.txt to resolve the 'None' cases

# rerun lsfix
python lsfix.py dummy temp_pwg_1.txt lsfix_1.txt
1941 lines written to lsfix_1.txt
True 1917
None 1
fixed 23

----
Not solved:
<L>2054<pc>1-0155<k1>aDunA
None	17295	<ls>an. 57.</ls>	

-------------------------------------------------------------
# create temp_pwg_2.txt with the 'fixed' items

python dict_replace.py temp_pwg_1.txt lsfix_1.txt temp_pwg_2.txt
47 lines to change
apply_repls: 47 lines changed
1129105 lines written to temp_pwg_2.txt


-------------------------------------------------------------
-- remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue123fixa
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue123fixa
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
Create Some documentation files
lsfix_2.txt for documentation

python lsfix.py dummy temp_pwg_2.txt lsfix_2.txt
1967 lines written to lsfix_2.txt
True 1966
None 1

-------------------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
11 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
23 changes written to change_pwg_2.txt

============================================================
sync to github:
------------------
csl-orig # git pull
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue123fixa
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
-----------------
csl-corrections
 NONE
 
---------------------------------------------------
sync to Cologne, pull changed repos, redo the pwg displays
csl-orig pull
-----------------

# sync issue123fixa
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue123fixa
git add .
git commit -m "issue123fixa
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
