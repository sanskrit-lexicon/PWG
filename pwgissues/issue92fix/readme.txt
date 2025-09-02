issue92fix/readme.txt
08-28-2025 begun ejf
fix references to Bṛhatsam̃hitā of Varāhamihira, KERN, 1865

sanskrit-lexicon-scans/

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue92fix
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue92fix

-------------------------------------
# get temporary local copy of koshas
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue92fix
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw_0.txt

# generate a copy for manual changes
--------------------------------------
forms of reference:
  VARĀH. BṚH. S. N,N : pwg, pw, pwkvn
  Varāh. Bṛh. S. N,N : sch
  VarBṛS. N,N         : mw


We use lsfix2.py, with parmfile lsfix2_parm.py
to examine splitting

============================================================
split work for pwg
python lsfix2.py pwg2 temp_pwg_0.txt lsfix2_pwg2_0.txt
9125 lines written to lsfix2_0.txt
(None, 2) 594
(True, 2) 6138
('fixed', 2) 2256
(False, 2) 137

cp temp_pwg_0.txt temp_pwg_1.txt

Resolve the None and False  by edits to temp_pwg_1.txt

 problems noted:
--- 21814 : gam (lnum 204627) :
  {#nIcopagatA#} <ls n="VARĀH. BṚH. S.">32,15.   nIcopagatA not found in 32,15
--- 40842 : nemi :
<ls>VARĀH. BṚH. S. 42 (43),22. 86,22 (103).</ls>
  42,22 not indexed
  43,22 indexed and contains nemyAm ok
  86,22 indexed  nemyAm not found
  86,103 not indexed
--- 23053 : gocara
<ls n="VARĀH. BṚH. S.">40 (39),13.</ls>
  40,13 gocara not found
  39,13 not indexed
------------------------------------------------
</ls> <ls n="VARĀH. BṚH. S.">
cp temp_pwg_0.txt temp_pwg_1.txt
Manually edit temp_pwg_1.txt
-- pre-split cases where a '(nnn)' is in scope.

# run lsfix2 on temp_pwg_1.txt
python lsfix2.py pwg2 temp_pwg_1.txt lsfix2_pwg_1.txt
9308 lines written to lsfix2_pwg_1.txt
(None, 2) 477
(True, 2) 6388
('fixed', 2) 2379
(False, 2) 64

----------------------------
# generate temp_pwg_2.txt from temp_pwg_1.txt and the 'fixed' elements

python dict_replace2.py temp_pwg_1.txt lsfix2_pwg_1.txt temp_pwg_2.txt
9308 kept.
9308 lines read from lsfix2_pwg_1.txt
2361 lines to change
apply_repls: 2361 lines changed

-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue92fix
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue92fix
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

python lsfix2.py pwg2 temp_pwg_2.txt lsfix2_pwg_2.txt
14249 lines written to lsfix2_pwg_2.txt
(None, 2) 477
(True, 2) 13708
(False, 2) 64


---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
400 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
2361 changes written to change_pwg_2.txt

============================================================
Split work for pw
============================================================
python lsfix2.py pw2 temp_pw_0.txt lsfix2_pw2_0.txt
337 lines written to lsfix2_pw2_0.txt
(True, 2) 305
('fixed', 2) 17
(None, 2) 15

cp temp_pw_0.txt temp_pw_1.txt
edit temp_pw_1.txt : try to solve the None cases.
1 case solved

# run lsfix2 on temp_pw_1.txt
python lsfix2.py pw2 temp_pw_1.txt lsfix2_pw_1.txt
337 lines written to lsfix2_pw_1.txt
(True, 2) 305
('fixed', 2) 18
(None, 2) 14

----------------------------
# generate temp_pw_2.txt from temp_pw_1.txt and the 'fixed' elements

python dict_replace2.py temp_pw_1.txt lsfix2_pw_1.txt temp_pw_2.txt
337 lines read from lsfix2_pw_1.txt
18 lines to change
apply_repls: 18 lines changed

# remake xml from temp_pw_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue92fix
cp temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue92fix

cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue92fix
cp temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue92fix

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pw2 temp_pw_2.txt lsfix2_pw_2.txt
365 lines written to lsfix2_pw_2.txt
(True, 2) 351
(None, 2) 14

---- documentation in change files
python diff_to_changes_dict.py temp_pw_0.txt temp_pw_1.txt change_pw_1.txt
1 changes written to change_pw_1.txt

python diff_to_changes_dict.py temp_pw_1.txt temp_pw_2.txt change_pw_2.txt
18 changes written to change_pw_2.txt

=====================================================
Split work for pwkvn
=====================================================
python lsfix2.py pwkvn2 temp_pwkvn_0.txt lsfix2_pwkvn2_0.txt
40 lines written to lsfix2_pwkvn2_0.txt
(True, 2) 39
(None, 2) 1

The 'None' item is not amenable to correction.
Nothing else to do with pwkvn

=====================================================
Split work for sch
=====================================================
python lsfix2.py sch2 temp_sch_0.txt lsfix2_sch2_0.txt
42 lines written to lsfix2_sch2_0.txt
(True, 2) 38
(None, 2) 3
('fixed', 2) 1

cp temp_sch_0.txt temp_sch_1.txt
edit temp_sch_1.txt : try to solve the None cases.

# run lsfix2 on temp_sch_1.txt
python lsfix2.py sch2 temp_sch_1.txt lsfix2_sch_1.txt
49 lines written to lsfix2_sch_1.txt
(True, 2) 48
('fixed', 2) 1

----------------------------
# generate temp_sch_2.txt from temp_sch_1.txt and the 'fixed' elements

python dict_replace2.py temp_sch_1.txt lsfix2_sch_1.txt temp_sch_2.txt
49 lines read from lsfix2_sch_1.txt
1 lines to change
apply_repls: 1 lines changed

-------------------------------------------------------------
# Create Some documentation files

python lsfix2.py sch2 temp_sch_2.txt lsfix2_sch_2.txt
51 lines written to lsfix2_sch_2.txt

# ---- documentation in change files
python diff_to_changes_dict.py temp_sch_0.txt temp_sch_1.txt change_sch_1.txt
3 changes written to change_sch_1.txt
python diff_to_changes_dict.py temp_sch_1.txt temp_sch_2.txt change_sch_2.txt
1 changes written to change_sch_2.txt

plit work for mw
=====================================================
python lsfix2.py mw2 temp_mw_0.txt lsfix2_mw2_0.txt
607 lines written to lsfix2_mw2_0.txt
(None, 2) 606
(True, 2) 1

lsfix2 doesn't fully work for MW, since MW writes
 1st parameter in roman numerals.
However, it does list the instances of VarBṛS. with parameters
 <ls>VarBṛS. X</ls> and <ls n="VarBṛS.Y">Z</ls>
 which it classifies as None.

Manually examine lsfix2_mw2_0.txt and correct anomalies
in temp_mw_1.txt.
cp temp_mw_0.txt temp_mw_1.txt

First anomaly is that in 8 instances, the first parameter
is digit sequence (not roman!).
Change these to Roman
Also a few other problems, such as
-----
caradala 
https://sanskrit-lexicon-scans.github.io/brihatsam/pdfpages/Br-079.pdf
 is inaccessible via
 https://sanskrit-lexicon-scans.github.io/brihatsam/app1/?2,1

The 'next page' link stalls.
This solved by modifications to brihatsam apps:
 - app0 added based on aitbr/app0
 - app1 modified to use app0 for next page links
---
 None	2	250192	<ls>VarBṛS. lxxvii, 4/5, 6</ls>	citrin - not found!
 None	2	280778	<ls>VarBṛS. xliv, 9/10</ls>	tarkArI - not found
-----

# run lsfix2 on temp_mw_1.txt
python lsfix2.py mw2 temp_mw_1.txt lsfix2_mw_1.txt
613 lines written to lsfix2_mw_1.txt
(None, 2) 613


# remake xml from temp_mw_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue92fix
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue92fix

-------------------------------------------------------------
# Create Some documentation files

# ---- documentation in change files
python diff_to_changes_dict.py temp_mw_0.txt temp_mw_1.txt change_mw_1.txt
21 changes written to change_mw_1.txt


============================================================
Ready
============================================================
sync to github:
------------------
# csl-orig 
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue92fix
diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
#0  as expected
diff temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt | wc -l
#0  as expected
diff temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt | wc -l
#0  as expected 
diff temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt | wc -l
#0  as expected 
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue92fix  splitting 'VARĀH. BṚH. S. N,N' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue92fix

---------------------------------------------------
sync to Cologne
# connect to cologne server via ssh
---------------
# pull changed repos
csl-orig #pull

---------------
# redo the displays for pwg, pw, sch, mw
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/
sh generate_dict.sh pw  ../../PWScan/2020/
sh generate_dict.sh sch  ../../SCHScan/2020/
sh generate_dict.sh mw  ../../MWScan/2020/

-----------------------------------------------------
# sync issue92fix to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue92fix
git pull
git add .
git commit -m "issue92fix 'VARĀH. BṚH. S. N,N' link splitting
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
