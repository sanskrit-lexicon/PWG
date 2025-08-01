issue129fix/chr/readme.txt
07-31-2025 begun ejf
fix references to 'BHAG. N,N'

sanskrit-lexicon-scans/bhagavadgita

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue129fix
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue129fix

-------------------------------------
# get temporary local copy of pwg
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue129fix
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt

# generate a copy for manual changes
cp temp_pwg_0.txt temp_pwg_1.txt

--------------------------------------
# edit lsfix_parm.py
targetobj = {
 'dummy': 
   {'dictcode': 'pwg',
    'lscode': 'BHAG.',
    'nparm': 2,
    }
 }

----------------------------------------
python lsfix.py dummy temp_pwg_0.txt lsfix_0.txt
True 1994
fixed 232
None 45
False 2

----
15523 : karman : <ls n="BHAG.">II,506.</ls>  : how to code???
 AB (with better print):  <ls>H. 506</ls>
 ----
63323 : aDyuzwa : <ls>WEBER, BHAG. 425.</ls> : tooltip ?
https://www.deutsche-digitale-bibliothek.de/item/PKCDI6263WKTKWP7W7RTUM44QCRTMQKL
https://www.digitale-sammlungen.de/en/view/bsb10219646?page=,1
This download has only 96 pages,  BUT
 p. 425 is at download page 76, and our word aDyuzwa is 10 lines from bottom
Über ein Fragment der Bhagavatî, A. Weber, 1865

ADDED to pwgbib_input.txt in csl-pywork

-----
49721 : praloBana : BHAG. 8,20,5 : BHAG. P. 8,20,5  print change

<ls>BHAG. 8,20,5</ls>
----------------------------------------
Resolve None and False by changes to temp_pwg_1.txt
----------------------------

python lsfix.py dummy temp_pwg_1.txt lsfix_1.txt
2265 lines written to lsfix_1.txt
True 2026
fixed 237
None 2

Unresolved:
 
57095 : maDusUdana : <ls>BHAG. Einl. XVI. fgg.</ls> : 
57096 : maDusUdanasarasvatI : <ls>BHAG. Einl. XVI. fgg.</ls> : 

Ref: https://github.com/sanskrit-lexicon/PWG/issues/160#issuecomment-3142195400
These believed to be references to p. XVI of the Introduction to
  the Schlegel version of BHAGAVADGITA.  But,
  How does p. XVI relate to the pwg entries?
 XVI: https://sanskrit-lexicon-scans.github.io/bhagavadgita/pdfpages/bhag-021.pdf
 
-------------------------------
# create temp_pwg_2.txt with the 'fixed' items
# 
python dict_replace.py temp_pwg_1.txt lsfix_1.txt temp_pwg_2.txt
2265 lines read from lsfix_1.txt
237 lines to change
apply_repls: 237 lines changed

-------------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue129fix
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue129fix
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
2580 lines written to lsfix_2.txt
True 2578
None 2


-------------------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
46 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
237 changes written to change_pwg_2.txt

============================================================
sync to github:
------------------
# csl-orig # git pull
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue129fix
diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue129fix  'BHAG. N,N'
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue129fix

----------------
# csl-pywork
cd /c/xampp/htdocs/cologne/csl-pywork/
git pull
git add .
git commit -m "issue129fix  'BHAG. N,N'
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue129fix

----------------
# csl-corrections
cd /c/xampp/htdocs/cologne/csl-corrections/
git pull
git add .
git commit -m "pwg printchange issue129fix  'BHAG. N,N'
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue129fix

---------------------------------------------------
sync to Cologne, pull changed repos, redo the pwg displays

---------------
csl-orig #pull
csl-corrections # pull
csl-pywork # pull

---------------
# update pwg display
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/

-----------------

# sync issue129fix
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue129fix
git pull
git add .
git commit -m "issue129fix BHAG. N,N bhagavadgita ls split
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
