
10-17-2025 begun ejf
references to Rājataraṅgiṇī, Calcutta edition

This issue documents two things:
* creates new repo sanskrit-lexicon-scans/rajatarcalc
* checks the references 'RĀJA-TAR. ed. Calc.'


Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue169
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue169

-------------------------------------
# get temporary local copy of koshas
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw_0.txt

index prepared by Andhrabharati

Rajatarangini_.Calc._index.txt

# RĀJA-TAR. ed. Calc.
python lsfix2.py pwg temp_pwg_0.txt lsfix2_pwg_0.txt
(True,7),(fixed,2),(all,9) lsfix2_pwg_0.txt

# RĀJA-TAR.   taraNga 7,8
python lsfix2.py pwga temp_pwg_0.txt lsfix2_pwg_0_a.txt
(None,60),(True,10230),(all,10290) lsfix2_pwg_0_a.txt

The RĀJA-TAR. refs with taranga 7 or 8.
  rajatarcalc will be the target for these.
1248 matches for "RĀJA-TAR. [78]," in buffer: lsfix2_pwg_0_a.txt
  Saved into file lsfix2_pwg_0_a_78.txt

Preliminary matching of a few from lsfix2_pwg_0_a_78.txt,
  using index with pdf

jayarAja	<ls n="RĀJA-TAR. 7,">1017.</ls>  epage=141
pAja	<ls n="RĀJA-TAR. 7,">1024.</ls>  epage=142
BAgika	<ls n="RĀJA-TAR. 8,">1667.</ls>	 epage=225

Also, check the few RĀJA-TAR. ed. Calc. refs:

jAni	<ls>RĀJA-TAR. ed. Calc. 1,258</ls> epage=19
Takkana	<ls>RĀJA-TAR. ed. Calc. 6,231. 236.</ls> epage=101
mummuni	<ls>RĀJA-TAR. ed. Calc. 3,334. 8,2180.</ls> epage=42, epage=242

All the above checks accepted.

Ready to make index and apps.
---------------------------------------

======================================
Construct index.js

index.txt contains
page	taranga	from v.	to v.	ipage	Remarks
10	1	1	19	1	I: Kalhana
 through
286	8	3538	3551	277	I: Kalhana

Also line 159 is artificially modified
old: 167	7	---	---	158	I: Kalhana  artificial added by Jim
new: 167	7	1745	9999	158	I: Kalhana  artificial added by Jim

8 line-pairs flagged as  problem:  These are unchanged as of now.
fromv problem A
lnum=33, line=41        3       284     313     32      I: Kalhana
lnum=34, line=42        3       310     339     33      I: Kalhana
  A reference to 310-313 will show epage 41.
  This is not an index typo, but an oddity in the pdf.
fromv problem A
lnum=44, line=52        4       49      78      43      I: Kalhana
lnum=45, line=53        4       80      109     44      I: Kalhana
fromv problem A
lnum=61, line=69        4       543b    572     60      I: Kalhana
lnum=62, line=70        4       578     606     61      I: Kalhana
fromv problem A
lnum=65, line=73        4       665     694     64      I: Kalhana
lnum=66, line=74        4       690     718a    65      I: Kalhana
fromv problem A
lnum=132, line=140      7       960     988     131     I: Kalhana
lnum=133, line=141      7       990     1017    132     I: Kalhana
fromv problem A
lnum=181, line=189      8       610     639     180     I: Kalhana
lnum=182, line=190      8       645     673     181     I: Kalhana
fromv problem A
lnum=185, line=193      8       731     760     184     I: Kalhana
lnum=186, line=194      8       756     785     185     I: Kalhana
fromv problem A
lnum=226, line=234      8       1934    1963    225     I: Kalhana
lnum=227, line=235      8       1963    1992    226     I: Kalhana

python make_js_index.py index.txt index.js

==========================================

Creating the rajatarcalc repo, and initializing apps.

See readme_apps.txt

link target sample: https://sanskrit-lexicon-scans.github.io/rajatarcalc/app1?N,N

==========================================
modify basicadjust.php to access rajatarcalc.
/c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php

Checks are made for each kosha.

---------------------------
readme_pwg.txt   1 change  temp_pwg_1.txt
  28 matches in 27 lines for "[I]+," in buffer: tempwork_lsfix2_pwg_1_a.txt
  Andhrabharati may know what these are

--------------------------
readme_pw.txt   no changes

Is the Kern edition rajatarcalc ?
RĀJAT.	Rājat.	RĀJATARAṂGIṆĪ. Die 6 ersten Bücher nach der Ausg. von TROYER. Die Beträge aus dem 7ten und 8ten Buche von KERN.

--------------------------
readme_pwkvn.txt   no changes

--------------------------
readme_sch.txt
Rājat. 7/8,N

No changes.  But many refs to taranga 7,8 where
  word not found in reference target line.

--------------------------
readme_mw.txt  1 change  temp_pw_1.txt

================================================
INSTALLATION
sync to github:

------------------
# csl-orig 
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue169
diff temp_pwg_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
# diff temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt | wc -l
# diff temp_pwkvn_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt | wc -l
# diff temp_sch_1a.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt | wc -l
diff temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt | wc -l
#0  as expected
# xxx
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue169  rajatarcalc 
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue169

------------------------
# csl-corrections 
# print changes: mw 1
cd /c/xampp/htdocs/cologne/csl-corrections
git pull
git add .
git commit -m "issue169  rajatarcalc
Ref: https://github.com/sanskrit-lexicon/pwg/issues/169"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue169

------------------------
# csl-websanlexicon
cd /c/xampp/htdocs/cologne/csl-websanlexicon
git pull
git add .
git commit -m "issue169  rajatarcalc
Ref: https://github.com/sanskrit-lexicon/pwg/issues/169"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue169

------------------------
# csl-apidev
cd /c/xampp/htdocs/cologne/csl-apidev
git pull
git add .
git commit -m "issue169  rajatarcalc
Ref: https://github.com/sanskrit-lexicon/pwg/issues/169"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue169

---------------------------------------------------
# sync to Cologne, pull changed repos, redo displays for
pwg, pw, pwkvn, sch, mw

---------------
csl-orig #pull
csl-websanlexicon #pull
csl-apidev #pull
csl-corrections #pull
# csl-pywork #pull
---------------
# update displays for pwg, pw, pwkvn, sch, mw
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/
sh generate_dict.sh pw  ../../PWScan/2020/
sh generate_dict.sh pwkvn  ../../PWKVNScan/2020/
sh generate_dict.sh sch  ../../SCHScan/2020/ 
sh generate_dict.sh mw  ../../MWScan/2020/

-----------------------------------------------------
# sync issue169 to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue169
git pull
git add .
git commit -m "rajatarcalc link target
Ref: https://github.com/sanskrit-lexicon/pwg/issues/169"
git push

------------------------------------------------------------
THE END
