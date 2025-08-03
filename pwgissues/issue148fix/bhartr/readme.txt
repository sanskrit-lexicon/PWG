issue148fix/bhartr/readme.txt
08-03-2025 begun ejf
fix references to Bhartṛhariśataka

sanskrit-lexicon-scans/

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue148fix/bhartr
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue148fix/bhartr

-------------------------------------
# get temporary local copy of pwg
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue148fix/bhartr
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt

# generate a copy for manual changes
cp temp_pwg_0.txt temp_pwg_1.txt
--------------------------------------
3 forms of reference:
lscode:  BHARTṚ. 
2 parameters

We use lsfix2.py, with parmfile lsfix2_parm.py
to examine splitting

-------------------------------------------------

python lsfix2.py dummy temp_pwg_1.txt lsfix2_0.txt
1286 lines written to lsfix2_0.txt
(None, 2) 84
(True, 2) 1123
('fixed', 2) 75
(False, 2) 4


Resolve the None and False  by edits to temp_pwg_1.txt

------------------------------------------------
Preliminary changes to temp_pwg_1.txt
--- L= 108217, 38637
Ref: https://github.com/sanskrit-lexicon/PWG/issues/160#issuecomment-3146943221
--- L=57095, 57096
Ref: https://github.com/sanskrit-lexicon/PWG/issues/160#issuecomment-3146707739
57095 : maDusUdana : BHAG. Einl. XVI. fgg. : BHĀG. P. Einl. I, LXIV. : print chg
57096 : maDusUdanasarasvatI : BHAG. Einl. XVI. fgg. :: text deleted : print chg
------------------------------------------------
# dummy1 -- skip 'BHARTṚ. Suppl.'
python lsfix2.py dummy1 temp_pwg_1.txt lsfix2_1.txt
1233 lines written to lsfix2_1.txt
(True, 2) 1158
('fixed', 2) 75

There are about 50 'BHARTṚ. Suppl. N';
the other uses of 'Suppl.' in pwg relate to SKDR. (Sabdakalpadruma)
L=26977 jalarASi  `BHARTṚ. Suppl. 17.'  Jim does not find jalarASi

358994  अथ अवधूतचर्या
36831 : DU : BHARTṚ. p. 69. : BHARTṚ. 3,92 : print change

BHARTṚ. ed. BOHL.  : tooltip?  1 instance L=100758, SfNgAraSata

----------------------------
generate temp_pwg_2.txt from temp_pwg_1.txt and the 'fixed' elements

python dict_replace2.py temp_pwg_1.txt lsfix2_1.txt temp_pwg_2.txt
1233 lines read from lsfix2_1.txt
apply_repls: 75 lines changed

-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue148fix/bhartr
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue148fix/bhartr
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

python lsfix2.py dummy1 temp_pwg_2.txt lsfix2_2.txt
1324 lines written to lsfix2_2.txt
(True, 2) 1324

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
43 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
74 changes written to change_pwg_2.txt


============================================================
sync to github:
------------------
# csl-orig 
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue148fix/bhartr
diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue148fix/bhartr  splitting 'BHARTṚ. N,N' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue148fix/bhartr

# csl-pywork  (pwgbib_input.txt)
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue148fix/bhartr
cd /c/xampp/htdocs/cologne/csl-pywork/
git pull
git add .
git commit -m "issue148fix/bhartr  'BHARTṚ. Suppl.' 
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue148fix/bhartr

------------------
# csl-corrections
cd /c/xampp/htdocs/cologne/csl-corrections/
git pull
git add .
git commit -m "pwg: PWG issue148fix/bhartr  
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue148fix/bhartr

---------------------------------------------------
sync to Cologne, pull changed repos, redo the pwg displays

---------------
csl-orig #pull
csl-pywork # pull
csl-corrections # pull
TODO ....
---------------
# update pwg display and pw display and pwkvn display
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/

-----------------

-----------------------------------------------------
# sync issue148fix/bhartr to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue148fix/bhartr
git pull
git add .
git commit -m "issue148fix/bhartr 'BHARTṚ. N,N' link splitting
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
