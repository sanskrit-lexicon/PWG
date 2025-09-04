issue152fix/readme.txt
09-02-2025 begun ejf
fix references to  Gitagovinda, ed. Lassen, 1836 

sanskrit-lexicon-scans/

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue152fix
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue152fix

-------------------------------------
# get temporary local copy of koshas
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue152fix
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw_0.txt

--------------------------------------
HIT. 12,26.
forms of reference:
 pwg: 
  HIT. N,N  : ipage, linenum
  HIT. R,N  : tantra, verse
  Hit. Pr. N : prastava N = verse
  
  Hit. N,N  : sch
  Hit. N,N  : mw


We use lsfix2.py, with parmfile lsfix2_parm.py
to examine splitting

============================================================
split work for pwg
python lsfix2.py pwg2 temp_pwg_0.txt lsfix2_pwg2_0.txt
3648 lines written to lsfix2_pwg2_0.txt
(None, 2) 1379
(True, 2) 2056
('fixed', 2) 178
(False, 2) 35


cp temp_pwg_0.txt temp_pwg_1.txt

Resolve the None and False  by edits to temp_pwg_1.txt

 problems noted:
---
pwg 68 matches for "<ls>HIT. ed. JOHNS. [0-9]+.</ls>"
pwg 166 matches for "<ls>HIT. Pr\. [0-9]+.</ls>"
pwg 890 matches for "<ls>HIT. [IV]+,[0-9]+.</ls>"

pwg 'i'  nADIta not found in HIT. Pr. 38 or 39
<ls>HIT. Pr. 23.</ls> {#pustakezu ca nADIto nADIto gurusaMniDO#}
v. l. zu <ls n="HIT. Pr.">38.</ls> <ls n="HIT. Pr.">39.</ls>
pwg 21460 : gaRa HIT. 12,13. :  gaRa not found at page 12 line 13 ?

pwg 53157 : bfhaspati : HIT. Pr. 7,21 : HIT. 7,21 : print change
pwg 87307 : vacana : >HIT. Pr. 6,9. 18,19. : >HIT. 6,9. 18,19. : print change

</ls> <ls n="HIT. I,">
</ls> <ls n="HIT.">
</ls> <ls n="HIT. Pr.">
</ls> <ls n="HIT. II,">

Edited csl-pywork/...pwgbib_input.txt
------------------------------------------------

python lsfix2.py pwg2 temp_pwg_1.txt lsfix2_pwg_1.txt
3829 lines written to lsfix2_pwg_1.txt
(None, 2) 1477
(True, 2) 2164
('fixed', 2) 187
(False, 2) 1


The None cases are using some other mode of reference than adhyaya,verse.
Cannot resolve now.

----------------------------
# generate temp_pwg_2.txt from temp_pwg_1.txt and the 'fixed' elements

python dict_replace2.py temp_pwg_1.txt lsfix2_pwg_1.txt temp_pwg_2.txt
1140 lines read from lsfix2_pwg_1.txt
187 lines to change
apply_repls: 187 lines changed

-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue152fix
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue152fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pwg2 temp_pwg_2.txt lsfix2_pwg_2.txt
4221 lines written to lsfix2_pwg_2.txt
(None, 2) 1477
(True, 2) 2743
(False, 2) 1

Approx. counts for the 'None' and 'False' sub-categories
983 <ls>HIT. [IV]+,[0-9]+\.?</ls>
207 <ls>HIT. Pr\. [0-9]+\.?</ls>
 79 <ls n="HIT.">[IV]+,[0-9]+\.?</ls>
 70 <ls n="HIT. [IV]+,">[0-9]+\.?</ls>
 17 <ls n="HIT. Pr.">[0-9]+\.?</ls>
 16 <ls>HIT. [IV]+,[0-9]+, v. l.</ls>
 89 <ls>HIT. ed. JOHNS.
  4 <ls n="HIT.">ed. JOHNS.
 13 [misc]
 (+ 983 207 79 70 17 16 89 4 13) = 1478 (equals 1477 None + 1 False)
 
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
200 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
187 changes written to change_pwg_2.txt

============================================================
Split work for pw
============================================================
python lsfix2.py pw2 temp_pw_0.txt lsfix2_pw2_0.txt
58 lines written to lsfix2_pw2_0.txt
(True, 2) 48
(None, 2) 7
('fixed', 2) 3

	
The None cases require no editing
1 <ls>HIT. ed. JOHNS. 1336</ls>
6 <ls>HIT. [IV]+,[0-9]+\.?</ls>

----------------------------
# generate temp_pw_1.txt from temp_pw_0.txt and the 'fixed' elements

python dict_replace2.py temp_pw_0.txt lsfix2_pw2_0.txt temp_pw_1.txt
3 lines to change
apply_repls: 3 lines changed

-----------------------------------------------------------
# remake xml from temp_pw_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue152fix
cp temp_pw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue152fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pw2 temp_pw_1.txt lsfix2_pw_1.txt
61 lines written to lsfix2_pw_1.txt
(True, 2) 54
(None, 2) 7

The None cases are discussed above

---- documentation in change files
python diff_to_changes_dict.py temp_pw_0.txt temp_pw_1.txt change_pw_1.txt
3 changes written to change_pw_1.txt

=====================================================
Split work for pwkvn
=====================================================
python lsfix2.py pwkvn2 temp_pwkvn_0.txt lsfix2_pwkvn2_0.txt
11 lines written to lsfix2_pwkvn2_0.txt
(True, 2) 10
(None, 2) 1

The None instance is '<ls>HIT. I,201</ls>' -- No change needed
Nothing more to do for pwkvn

=====================================================
Split work for sch
=====================================================
python lsfix2.py sch2 temp_sch_0.txt lsfix2_sch2_0.txt
10 lines written to lsfix2_sch2_0.txt
(True, 2) 8
(None, 2) 2

One change to make
cp temp_sch_0.txt temp_sch_1.txt
Make change in temp_sch_1.txt

python lsfix2.py sch2 temp_sch_1.txt lsfix2_sch2_1.txt
11 lines written to lsfix2_sch2_1.txt
(True, 2) 10
(None, 2) 1

The None case is '<ls>Hit. I,201.</ls>' --- no change required

-----------------------------------------------------------
# remake xml from temp_sch_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue152fix
cp temp_sch_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh sch  ../../sch
sh xmlchk_xampp.sh sch
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue152fix
-- end of 'remake xml ...'

---- documentation in change files
python diff_to_changes_dict.py temp_sch_0.txt temp_sch_1.txt change_sch_1.txt
1 changes written to change_sch_1.txt


=====================================================
split work for mw

python lsfix2.py mw2 temp_mw_0.txt lsfix2_mw2_0.txt
123 lines written to lsfix2_mw2_0.txt
(None, 2) 123


lsfix2 doesn't fully work for MW, since MW writes
 1st parameter in roman numerals.
However, it does list the instances


Manually examine lsfix2_mw2_0.txt
Some anomalies found

31 matches for "<ls>Hit. [iv]+, [0-9]+\.?</ls>
 2 matches for "<ls>Hit. [0-9]+, [0-9]+\.?</ls>"
10 matches for "<ls>Hit. [iv]+\.?</ls>"   These refer to entire chapter.
31 matches for "<ls>Hit. [iv]+, [0-9]+, [0-9]+\.?</ls>  RNN see note

Problems:
---
94898 : dUram : <ls>Hit. i, 101/102</ls>  dUram not found
62182 : gaganavihArin : Hit. i, 2, 15, Sch.
---
RNN  Change basicadjust - deactivate these links.
  These are of form section, kaTA, verse (local to kaTA)
  Example: mw hw gomayAya HIT. III, 6, 33
    In Schlegel, Lassen:  gomayAyate verse 56 (Book 3, Fable 7)
    Shlegel 'Fab. vi' first verse is 25 (- 56 25) = 31).
    Conclude a. 2nd parameter is kaTA, with verse numbering restart.
    b. Link target is to a different version of Hitopadesha


NO adjustments to mw.txt
Done with analysis of mw references.

============================================================
Ready
============================================================
sync to github:
------------------
# csl-orig 
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue152fix
diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
#0  expected
diff temp_pw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt | wc -l
#0  expected
diff temp_sch_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt | wc -l
#0  expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue152fix  splitting 'HIT. ' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue152fix

------------------
# csl-websanlexicon
cd /c/xampp/htdocs/cologne/csl-websanlexicon
git pull
git add .
git commit -m "issue152fix  splitting 'HIT. ' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue152fix

------------------
# csl-apidev
cd /c/xampp/htdocs/cologne/csl-apidev
git pull
git add .
git commit -m "issue152fix  splitting 'HIT. ' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue152fix

---------------------------------------------------
sync to Cologne
# connect to cologne server via ssh
---------------
# pull changed repos
csl-orig # pull
csl-websanlexicon # pull
csl-apidev # pull
---------------
# redo the displays for pwg, pw, sch
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/
sh generate_dict.sh pw  ../../PWScan/2020/
sh generate_dict.sh sch  ../../SCHScan/2020/

-----------------------------------------------------
# sync issue152fix to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue152fix
git pull
git add .
git commit -m "issue152fix 'HIT. N,N' link splitting
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
