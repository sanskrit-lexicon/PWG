issue87fix/bhartr/readme.txt
08-03-2025 begun ejf
fix references to boesp1 Indische Sprüche, O. Böhtlingk, first edition

pwg only
Spr. N
sanskrit-lexicon-scans/boesp1

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue87fix
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue87fix

-------------------------------------
# get temporary local copy of pwg
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue87fix
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt

# generate a copy for manual changes
cp temp_pwg_0.txt temp_pwg_1.txt
--------------------------------------
1 form of reference:
lscode:  Spr.  OR 'Spr. (I)'
1 parameter

Note 'Spr. (II)' is excluded
We use lsfix2.py, with parmfile lsfix2_parm.py to examine splitting

-------------------------------------------------

python lsfix2.py spra temp_pwg_0.txt lsfix2_spra_0.txt
12930 lines written to lsfix2_spra_0.txt
(True, 1) 12660
(False, 1) 6
('fixed', 1) 1
(None, 1) 263



The bulk of the 263 None are acutally using lscode 'Spr. (I)'
This lscode is not currently in basicadjust.php.
TODO --  will need to handle these separately

-----------------------------------------------
make 'sprb'  in lsfix_parm.py  to skip 'Spr. (I)'

python lsfix2.py sprb temp_pwg_0.txt lsfix2_sprb_0.txt
12672 lines written to lsfix2_sprb_0.txt
(True, 1) 12660
(False, 1) 6
('fixed', 1) 1
(None, 1) 5

Now we make changes to resolve the False/None cases


------------------------------------------------
cp temp_pwg_0.txt temp_pwg_1.txt
changes to pwg_1

python lsfix2.py sprb temp_pwg_1.txt lsfix2_sprb_1.txt
12673 lines written to lsfix2_sprb_1.txt
(True, 1) 12668
('fixed', 1) 3
(None, 1) 2

The 2 remaining 'None' items are:
<ls>Spr. 2896, N.</ls>
<ls>Spr. 3524, N.</ls>
'N.' refers to 'Note'.  Not a problem.
----------------------------
# generate temp_pwg_2.txt from temp_pwg_1.txt and the 'fixed' elements

python dict_replace2.py temp_pwg_1.txt lsfix2_sprb_1.txt temp_pwg_2.txt
12673 kept.
12673 lines read from lsfix2_sprb_1.txt
2 lines to change
apply_repls: 2 lines changed

This finishes the work for 'Spr.' lscode.
Now, on to the 'Spr. (I)' code.

===========================================================
Spr. (I)
From lsfix2_spra_0.txt,
208 matches for "<ls n="Spr.">(I) " in buffer: lsfix2_spra_0.txt

pwgbib already has  lscode='Spr. (I)'.
Change basicadjust to link 'Spr. (I) N' to boesp1.

**************************************************
lsfix2.py cannot split the
A wrong turn! with this change, the '(I)' is not displayed  in
 
--------------
prep_spri_input.txt  66 records
from slfix2_spra_0.txt
manually extract records that
- start with
  <ls n="Spr.">(I)
  <ls>Spr. (I)
- and that need to be split
------
Examples
None	1	838734	<ls n="Spr.">(I) 1649. 4239. 4467.</ls>	
None	1	841399	<ls>Spr. (I) 883. 1316. 1505. 2384. 2790. fg. 2950. 4344. 4922. fgg.</ls>	
-------
removed from original prep_spri_input.txt:
None	1	844540	<ls n="Spr.">(I) 2807</ls>	
None	1	904891	<ls n="Spr.">(I) 2197</ls>	
None	1	912901	<ls n="Spr.">(I) 2226</ls>	
None	1	914786	<ls n="Spr.">(I) 2968</ls>	

Add last field as the 'split' of 3rd field
python prep_spri.py prep_spri_input.txt prep_spri_output.txt

python dict_replace2.py temp_pwg_2.txt prep_spri_output.txt temp_pwg_3.txt
apply_repls: 62 lines changed
1129105 lines written to temp_pwg_3.txt


*************************************************
python lsfix2.py sprc temp_pwg_3.txt lsfix2_sprc_3.txt
160 lines written to lsfix2_sprc_3.txt
(True, 1) 160

Correct the False item in temp_pwg_3.txt

python lsfix2.py spra temp_pwg_3.txt lsfix2_spra_3.txt
13044 lines written to lsfix2_spra_3.txt
(True, 1) 12674
(None, 1) 370

===========================================================
# remake xml from temp_pwg_3.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue87fix
cp temp_pwg_3.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue87fix
-- end of 'remake xml ...'

-------------------------------------------------------------
cp temp_pwg_3.txt temp_pwg_4.txt
A small number of changes like
old: <ls n="Spr. (II)">1876. 2054. (I) 1233. 1859.</ls>
new: <ls n="Spr. (II)">1876.</ls> <ls n="Spr. (II)">2054.</ls> <ls n="Spr.">(I) 1233.</ls> <ls n="Spr. (I)">1859.</ls>

===========================================================
# remake xml from temp_pwg_4.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue87fix
cp temp_pwg_4.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue87fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
11 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
181 changes written to change_pwg_2.txt

python diff_to_changes_dict.py temp_pwg_2.txt temp_pwg_3.txt change_pwg_3.txt
62 changes written to change_pwg_3.txt

python diff_to_changes_dict.py temp_pwg_3.txt temp_pwg_4.txt change_pwg_4.txt
16 changes written to change_pwg_4.txt

============================================================
sync to github:
------------------
# csl-orig 
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue87fix
diff temp_pwg_4.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue87fix  splitting 'Spr. (I) N' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue87fix

------------------
# csl-websanlexicon
cd /c/xampp/htdocs/cologne/csl-websanlexicon/
git pull
git add .
git commit -m "issue87fix  splitting 'Spr. (I) N' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02

sh apidev_copy.sh

cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue87fix

------------------
# csl-apidev
cd /c/xampp/htdocs/cologne/csl-apidev/
git pull
git add .
git commit -m "issue87fix  splitting 'Spr. (I) N' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue87fix

---------------------------------------------------
sync to Cologne, pull changed repos, redo the pwg displays

---------------
csl-orig #pull
csl-websanlexicon # pull
csl-apidev # pull

---------------
# update pwg display and pw display and pwkvn display
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/

-----------------------------------------------------
# sync issue87fix to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue87fix
git pull
git add .
git commit -m "issue87fix 'Spr. (I)' link splitting (pwg)
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
