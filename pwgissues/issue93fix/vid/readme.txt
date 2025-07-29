issue93fix/vid/readme.txt
07-28-2025 begun ejf
fix references to 'VID. N'
Story of VIDŪṢAKA
sanskrit-lexicon-scans/bchrest1

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue93fix/vid
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93fix/vid

-------------------------------------
# get temporary local copy of pwg
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93fix/vid
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt

# generate a copy for manual changes
cp temp_pwg_0.txt temp_pwg_1.txt

--------------------------------------
# edit lsfix_parm.py
targetobj = {
 'dummy': 
   {'dictcode': 'pwg',
    'lscode': 'VID.',
    'nparm': 1,
    }
 }

----------------------------------------
python lsfix.py dummy temp_pwg_0.txt lsfix_0.txt
1129 lines written to lsfix_0.txt
True 955
None 1
fixed 171
False 2

----------------------------------------
Resolve None and False by changes to temp_pwg_1.txt

--- 670 : aNga : hom=3
<ls>VID. 180,b.</ls> -> <ls>VID. 180</ls>,{%b%}.    (markup change)
  If 'b' means 'pada b (of abcd)', then this 'b' should be 'a'!

----------------------------

python lsfix.py dummy temp_pwg_1.txt lsfix_1.txt
1129 lines written to lsfix_1.txt
True 958
fixed 171

No more False/None !
----------
None are unresolved:


-------------------------------
# create temp_pwg_2.txt with the 'fixed' items
# 
python dict_replace.py temp_pwg_1.txt lsfix_1.txt temp_pwg_2.txt
1129 lines read from lsfix_1.txt
171 lines to change
apply_repls: 171 lines changed

-------------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93fix/vid
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93fix/vid
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
1395 lines written to lsfix_2.txt
True 1395

-------------------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
3 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
171 changes written to change_pwg_2.txt

============================================================
sync to github:
------------------
# csl-orig # git pull
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93fix/vid
diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue93fix/vid  'VID N' 
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93fix/vid

---------------------------------------------------
sync to Cologne, pull changed repos, redo the pwg displays

---------------
csl-orig #pull
---------------
# update pwg display
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/

-----------------

# sync issue93fix/vid
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93fix/vid
git pull
git add .
git commit -m "issue93fix/vid 'VID N' VIDŪṢAKA in bchrest1
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
