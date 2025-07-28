issue104fix/readme.txt
07-27-2025 begun ejf
fix references to 'H. ś.'

Abhidhānacintāmaṇipariśiṣṭa
sanskrit-lexicon-scans/abch2

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue104fix
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue104fix

-------------------------------------
# get temporary local copy of pwg
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue104fix
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt

# generate a copy for manual changes
cp temp_pwg_0.txt temp_pwg_1.txt

--------------------------------------
# edit lsfix_parm.py
targetobj = {
 'dummy': 
   {'dictcode': 'pwg',
    'lscode': 'H. ś.',
    'nparm': 1,
    }
 }
----------------------------------------

python lsfix.py dummy temp_pwg_0.txt lsfix_0.txt

1318 lines written to lsfix_0.txt
True 1308
None 6
False 4

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

Edut tenp_pwg_1.txt to resolve the 'False' cases
4 done

Edut tenp_pwg_1.txt to resolve the 'None' cases

Several None are like:
<ls>H. 204.</ls> <ls n="H. ś.">ś. 55.</ls> <ls>an. 3,523.</ls> <ls>MED. r. 117.</ls>
Since there are no `<ls>ś\.` matches,  We may change
 basicadjust.php so `<ls>ś. N</ls>` is a variant of `<ls>H. ś. N</ls>`
pwg text changed as
  <ls n="H. ś.">ś. 55.</ls> -> <ls>ś. 55.</ls>
  Also revise pwgbib_input.txt by adding line
1.123a	ś.	ś.	ś. = die Śeṣa's zu HEMACANDRA'S ABHIDHĀNACINTĀMAṆI (s. unter H.),&#13;&#10;S. 421--443.

# run lsfix.py with temp_pwg_1.txt
python lsfix.py dummy temp_pwg_1.txt lsfix_1.txt
1313 lines written to lsfix_1.txt
True 1313

# No False/None cases remain!

# Also no 'fixed' cases.
-------------------------------------------------------------
# create temp_pwg_2.txt with the 'fixed' items
# 
python dict_replace.py temp_pwg_1.txt lsfix_1.txt temp_pwg_2.txt
1313 kept.
1313 lines read from lsfix_1.txt
0 lines to change
apply_repls: 0 lines changed

This is as expected -- since no 'fixed' cases.
i.e., temp_pwg_1.txt and temp_pwg_2.txt are identical
diff temp_pwg_1.txt temp_pwg_2.txt | wc -l

47 lines to change
apply_repls: 47 lines changed
1129105 lines written to temp_pwg_2.txt
# 0  as expected.

-------------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue104fix
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue104fix
-- end of 'remake xml ...'
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue104fix

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
lsfix_2.txt for documentation

python lsfix.py dummy temp_pwg_2.txt lsfix_2.txt
1313 lines written to lsfix_2.txt
True 1313

diff lsfix_1.txt lsfix_2.txt | wc -l
#0  files are identical, as expected.
-------------------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
10 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
0 changes written to change_pwg_2.txt
 # as expected

============================================================
sync to github:
------------------
# csl-orig # git pull xxxx
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue104fix  'H. ś.' Abhidhānacintāmaṇipariśiṣṭa
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue104fix

-----------------
# csl-pywork   # change to pwgbib_input.txt
cd /c/xampp/htdocs/cologne/csl-pywork
git add .
git commit -m "issue104fix  'H. ś.' Abhidhānacintāmaṇipariśiṣṭa
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue104fix

-----------------
# csl-websanlexicon  # change to basicadjust.php
cd /c/xampp/htdocs/cologne/csl-websanlexicon
git add .
git commit -m "issue104fix  'H. ś.', 'ś.',  Abhidhānacintāmaṇipariśiṣṭa
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue104fix

-----------------
# csl-apidev         # change to basicadjust.php
cd /c/xampp/htdocs/cologne/csl-apidev
git add .
git commit -m "issue104fix  'H. ś.', 'ś.',  Abhidhānacintāmaṇipariśiṣṭa
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue104fix
-----------------
csl-corrections
 NONE
 
---------------------------------------------------
sync to Cologne, pull changed repos, redo the pwg displays
csl-orig #pull
csl-websanlexicon # pull
csl-pywork # pull
csl-apidev # pull

cd csl-pywork/v02
# update pwg display
sh generate_dict.sh pwg  ../../PWGScan/2020/

-----------------

# sync issue104fix
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue104fix
git add .
git commit -m "issue104fix 'H. ś.' Abhidhānacintāmaṇipariśiṣṭa
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
