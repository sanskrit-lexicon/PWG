issue154fix/readme.txt
07-30-2025 begun ejf
fix references to colebrooke edition of amarakosha.
'VIŚV. N,N'

sanskrit-lexicon-scans/amara_col

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue154fix
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue154fix

-------------------------------------
# get temporary local copy of pwg
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue154fix
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt

# generate a copy for manual changes
cp temp_pwg_0.txt temp_pwg_1.txt
--------------------------------------
3 forms of reference to amara_col link target:
lscode:
 COL.
 COLEBR.
 AK. ed. COLEBR.

And each lscode can take 3 or 4 paramenters
 lscode is COL., COLEBR., 

We use lsfix2.py, with parmfile lsfix2_parm.py
to examine splitting
This is applied for the 3 cases



======================================
# lsfix2 option colebr for lsfix2_parm.py, 
  uses lscode COLEBR. with 3 or 4 parameters
  
python lsfix2.py colebr temp_pwg_0.txt lsfix2_colebr_0.txt
31 lines written to lsfix2_colebr_0.txt
(True, 3) 3   3 parameters, no splitting required
(True, 4) 26  4 parameters, no splitting required
(None, 4) 2   2 items not resolved:


corrections to temp_pwg_1.txt for:
---
None	4	376514	<ls>COLEBR. a. a. O.</ls>
<ls>COLEBR. a. a. O.</ls> -> <ls>COLEBR.</ls> a. a. O.  

---
None	4	385483	<ls>COLEBR. (28),2.</ls>	
nirBartsana <ls>AK. 3,4,32</ls> <ls>COLEBR. (28),2.</ls>
Andhrabharati solution
 Ref: https://github.com/sanskrit-lexicon/PWG/issues/160#issuecomment-3137576648
 
39521 : nirBartsana : AK. 3,4,32 COLEBR. (28),2. : AK. 3,4,32,2 (COLEBR. 3,4,28,2.)  : PRINT CHANGE

--------------------------------------
python lsfix2.py colebr temp_pwg_1.txt lsfix2_colebr_1.txt
30 lines written to lsfix2_colebr_1.txt
(True, 3) 3
(True, 4) 27

--------------------------------------
Now, examine the 'COL.' examples, with 3 or 4 parameters

python lsfix2.py col temp_pwg_1.txt lsfix2_col_1.txt
100 lines written to lsfix2_col_1.txt
(True, 4) 92
(True, 3) 8

No further changes

--------------------------------------
Now, examine the 'AK. ed. COLEBR.' examples, with 3 or 4 parameters

python lsfix2.py akcol temp_pwg_1.txt lsfix2_akcol_1.txt
3 lines written to lsfix2_akcol_1.txt
(True, 3) 2
(True, 4) 1

--------------------------------------
## variant dict_replace2.py  to generate temp_pwg_2.txt
There are no splitting fixes required.
We'll upload the revised temp_pwg_1.txt to csl-orig

# concatenate the lsfix2 files
cat lsfix2_colebr_1.txt lsfix2_col_1.txt lsfix2_akcol_1.txt > lsfix2_1_all.txt

# apply the 'fixed' cases to pwg
python dict_replace2.py temp_pwg_1.txt lsfix2_1_all.txt temp_pwg_2.txt
apply_repls: 0 lines changed

Note in this case
diff temp_pwg_1.txt temp_pwg_2.txt | wc -l
# 0   files are identical
======================================


-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue154fix
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue154fix
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
These will be identical to the lsfix2_X_1 files, since temp_pwg1 = temp_pwg2

python lsfix2.py colebr temp_pwg_2.txt lsfix2_colebr_2.txt
30 lines written to lsfix2_colebr_2.txt
(True, 3) 3
(True, 4) 27


python lsfix2.py col temp_pwg_2.txt lsfix2_col_2.txt
100 lines written to lsfix2_col_2.txt
(True, 4) 92
(True, 3) 8

python lsfix2.py akcol temp_pwg_2.txt lsfix2_akcol_2.txt
3 lines written to lsfix2_akcol_2.txt
(True, 3) 2
(True, 4) 1

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
3 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
0 changes written to change_pwg_2.txt

============================================================
sync to github:
------------------
# csl-orig # git pull
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue154fix
diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue154fix  splitting refs to amara_col' 
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue154fix

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

# sync issue154fix
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue154fix
git pull
git add .
git commit -m "issue154fix links to amara_col 
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
