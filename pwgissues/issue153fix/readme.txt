issue153fix/readme.txt
09-01-2025 begun ejf
fix references to  Gitagovinda, ed. Lassen, 1836 

sanskrit-lexicon-scans/

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue153fix
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue153fix

-------------------------------------
# get temporary local copy of koshas
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue153fix
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw_0.txt

# generate a copy for manual changes
--------------------------------------
GĪT. 12,26.
forms of reference:
  GĪT. N,N  : pwg, pw, pwkvn
  Gīt. N,N  : sch
  Gīt. N,N  : mw


We use lsfix2.py, with parmfile lsfix2_parm.py
to examine splitting

============================================================
split work for pwg
python lsfix2.py pwg2 temp_pwg_0.txt lsfix2_pwg2_0.txt
1136 lines written to lsfix2_pwg2_0.txt
(True, 2) 1027
(None, 2) 36
('fixed', 2) 71
(False, 2) 2

cp temp_pwg_0.txt temp_pwg_1.txt

Resolve the None and False  by edits to temp_pwg_1.txt

 problems noted:
--- 
------------------------------------------------

python lsfix2.py pwg2 temp_pwg_1.txt lsfix2_pwg_1.txt
1140 lines written to lsfix2_pwg_1.txt
(True, 2) 1043
('fixed', 2) 72
(None, 2) 25

The None cases are using some other mode of reference than adhyaya,verse.
Cannot resolve now.

----------------------------
# generate temp_pwg_2.txt from temp_pwg_1.txt and the 'fixed' elements

python dict_replace2.py temp_pwg_1.txt lsfix2_pwg_1.txt temp_pwg_2.txt
1140 lines read from lsfix2_pwg_1.txt
72 lines to change
apply_repls: 72 lines changed

-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue153fix
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue153fix
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
(True, 2) 1197
(None, 2) 25

---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
20 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
72 changes written to change_pwg_2.txt

============================================================
Split work for pw
============================================================
python lsfix2.py pw2 temp_pw_0.txt lsfix2_pw2_0.txt
50 lines written to lsfix2_pw2_0.txt
(True, 2) 43
(None, 2) 7

None	2	45298	<ls>GĪT. S. 41</ls>	
The None cases can't be solved now.
Nothing more to do for pw!


=====================================================
Split work for pwkvn
=====================================================
python lsfix2.py pwkvn2 temp_pwkvn_0.txt lsfix2_pwkvn2_0.txt

24 lines written to lsfix2_pwkvn2_0.txt
(True, 2) 24

Nothing more to do for pwkvn

=====================================================
Split work for sch
=====================================================
python lsfix2.py sch2 temp_sch_0.txt lsfix2_sch2_0.txt

23 lines written to lsfix2_sch2_0.txt
(True, 2) 23

Nothing more to do for pwkvn

=====================================================
split work for mw

python lsfix2.py mw2 temp_mw_0.txt lsfix2_mw2_0.txt
106 lines written to lsfix2_mw2_0.txt
(None, 2) 106
START

lsfix2 doesn't fully work for MW, since MW writes
 1st parameter in roman numerals.
However, it does list the instances


Manually examine lsfix2_mw2_0.txt
No anomalies found
Nothing more to do for mw


============================================================
Ready
============================================================
sync to github:
------------------
# csl-orig 
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue153fix
diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue153fix  splitting 'GĪT. N,N' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue153fix

---------------------------------------------------
sync to Cologne
# connect to cologne server via ssh
---------------
# pull changed repos
csl-orig #pull

---------------
# redo the displays for pwg
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/

-----------------------------------------------------
# sync issue153fix to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue153fix
git pull
git add .
git commit -m "issue153fix 'GĪT. N,N' link splitting
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
