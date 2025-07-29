issue104fixa/readme.txt
07-28-2025 begun ejf
fix references to 'H. N'

Abhidhānacintāmaṇi
sanskrit-lexicon-scans/abch2

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue104fixa
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue104fixa

-------------------------------------
# get temporary local copy of pwg
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue104fixa
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt

# generate a copy for manual changes
cp temp_pwg_0.txt temp_pwg_1.txt

--------------------------------------
To avoid false negatives 'H. ś.' and 'H. an.',
add an additional field 'skip' to the parm
# edit lsfix_parm.py
targetobj = {
 'dummy': 
   {'dictcode': 'pwg',
    'lscode': 'H.',
    'nparm': 1,
    'skip': ['H. ś.' , 'H. an.'],
    }
 }
and make comparable upgrade to lsfix.py.
----------------------------------------

python lsfix.py dummy temp_pwg_0.txt lsfix_0.txt
16580 lines written to lsfix_0.txt
True 16537
None 32
fixed 2
False 9


----------------------------------------

Resolve None and False by changes to temp_pwg_1.txt


From  Ref: https://github.com/sanskrit-lexicon/PWG/issues/160#issuecomment-3124667886

2054 : aDunA : an. 57. : an. 7,57. : PRINT CHANGE
167  : akza  : H. 2,556. : H. an. 2,556. : PRINT CHANGE
4959 : aByAsa   : H. Pr. 36. : HIT. Pr. 36 : PRINT CHANGE
12413 : uraga : H. 1 03. : H. 1303. : PRINT CHANGE (AB pls. chk)
84835 : ru : Verz. d. B. H. H. No. 896. fg. : Verz. d. B. H. No. 896. fg. : PRINT CHANGE

2948 : anurakti : <ls>H. I,89.</ls>   : <span>H. I,89.</span> : This is Wilson Theatre of the Hindus  
15237 : karuRa : <ls>H. 369,2.</ls> : <ls>H. 369</ls>,2.  : odd usage. Markup
----------------------------

python lsfix.py dummy temp_pwg_1.txt lsfix_1.txt

True 16551
None 2  
fixed 2

Unresolved
8070 : AcArya   : <ls>H. p. 15</ls> : ?
10027 : itas : <ls>H. 7,149. 150</ls> : ?

-------------------------------
# create temp_pwg_2.txt with the 'fixed' items
# 
python dict_replace.py temp_pwg_1.txt lsfix_1.txt temp_pwg_2.txt
1129105 lines read from temp_pwg_1.txt
16555 kept.
16555 lines read from lsfix_1.txt
2 lines to change
apply_repls: 2 lines changed
1129105 lines written to temp_pwg_2.txt

-------------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue104fixa
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue104fixa
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
lsfix_2.txt for documentation

python lsfix.py dummy temp_pwg_2.txt lsfix_2.txt
16557 lines written to lsfix_2.txt
True 16555
None 2

-------------------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
43 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
2 changes written to change_pwg_2.txt
 # as expected

============================================================
sync to github:
------------------
# csl-orig # git pull xxxx
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue104fixa  'H.' Abhidhānacintāmaṇi
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue104fixa


-----------------
# csl-apidev         # change to basicadjust.php
-----------------
csl-corrections
cd /c/xampp/htdocs/cologne/csl-corrections
git pull  # in case Dhaval has modified csl-corrections.
git add .
git commit -m "issue104fixa  'H.'  Abhidhānacintāmaṇi
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue104fixa

 
---------------------------------------------------
sync to Cologne, pull changed repos, redo the pwg displays
csl-corrections  # pull

---------------
csl-orig #pull
---------------
cd csl-pywork/v02
# update pwg display
sh generate_dict.sh pwg  ../../PWGScan/2020/

-----------------

# sync issue104fixa
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue104fixa
git pull
git add .
git commit -m "issue104fixa 'H.' Abhidhānacintāmaṇi
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
