09-25-2024
issue: https://github.com/sanskrit-lexicon/PWG/issues/76

# This directory
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue76

# starting point for vntxt digitization of missing VN material.
https://github.com/user-attachments/files/17129810/PWGVN_1-6_reformatted_.dng.txt

# local copy rename
mv PWGVN_1-6_reformatted_.dng.txt vntxt_0_deva_orig.txt
cp vntxt_0_deva_orig.txt vntxt_0_deva.txt


# transcode
mkdir transcode
cd transcode
python mark_deva.py ../vntxt_0_deva.txt vntxt_0_deva_marked.txt
637 lines read from ../vntxt_0_deva.txt
637 lines written to vntxt_0_deva_marked.txt
Devanagari text has been marked and saved to vntxt_0_deva_marked.txt

Note: This step unnecessary!!  AB has alread marked Devanagari as {#X#},
 which is the pwg convention.
rm vntxt_0_deva_marked.txt

# transcode
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue76/transcode
mkdir pwgtranscoder1
cp /c/xampp/htdocs/sanskrit-lexicon/MWS/mwtranscode/transcoder1/deva_slp1.xml pwgtranscoder1/deva_slp1.xml
cp /c/xampp/htdocs/sanskrit-lexicon/MWS/mwtranscode/transcoder1/slp1_deva.xml pwgtranscoder1/slp1_deva.xml

cp /c/xampp/htdocs/sanskrit-lexicon/MWS/mwtranscode/transcoder.py .
cp /c/xampp/htdocs/sanskrit-lexicon/MWS/mwtranscode/mw_transcode.py pwg_transcode.py

# heavily edit pwg_transcode.py

-----------------
Transcode
# Some editing of vntxt_0_deva.txt related to transcoding to get invertibility
See change_vntxt_0_deva.txt

python pwg_transcode.py pwgtranscoder1 deva slp1 ../vntxt_0_deva.txt ../vntxt_0.txt
# check invertibility
python pwg_transcode.py pwgtranscoder1 slp1 deva ../vntxt_0.txt tempchk.txt
diff ../vntxt_0_deva.txt tempchk.txt | wc -l
0  # invertibility checks.

commit repo and sync to github.
--------------------------------------------------------------

The transcoding mishandled the udAtta accent (and maybe others?)
 Correct several errors. Mostly the Devanagari combining U change to /
 e.g. aÃªÂ£Â« -> a/
Also a few unbalanced parens noticed and changed.
See the 'replacements_data' in the program for details.
cd transcode
python make_vntxt_1.py ../vntxt_0.txt ../vntxt_1.txt

--------------------------------------------------------
09-27-2024
Redo transcoding using the pwg slp1_deva1.xml.
Main task is to create an 'inverse' transcoder deva1_slp1.xml.
Do this in a 'transcodepwg' directory

mkdir transcodepwg
cd transcodepwg
mkdir pwgtranscoder2
cp /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/utilities/transcoder/slp1_deva1.xml pwgtranscoder2/slp1_deva1.xml
cp /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/utilities/transcoder/deva_slp1.xml pwgtranscoder2/deva_slp1.xml

# also copy slp1_deva.xml for reference:
cp /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/utilities/transcoder/slp1_deva.xml pwgtranscoder2/slp1_deva.xml

Of course, deva_slp1.xml was constructed as an inverse for the non-pwg version slp1_deva.xml.
But we need an inverse for the pwg version slp1_deva1.xml.
We will call this inverse deva1_slp1.xml.
It starts as a copy of deva_slp1.xml:
cp pwgtranscoder2/deva_slp1.xml pwgtranscoder2/deva1_slp1.xml
# Manually edit pwgtranscoder2/deva1_slp1.xml

cd pwgtranscoder2
diff slp1_deva.xml slp1_deva1.xml > diff_slp1_deva_deva1.txt

name    slp1  deva      deva1
anudAtta \    u0952     u0952
udAtta   /    u0951     ua8eb  
svarita  ^    u1ce0     u0951

python make_deva1_slp1.py pwgtranscoder2/deva_slp1.xml pwgtranscoder2/deva1_slp1.xml
 a) u0951 -> ua8eb
 b) u1ce0 -> u095a
In addition, manually add the 'special rules ...' section at end of
deva1_slp1.xml.

-------------------------------------------------------
# We want to apply the deva1 transcoding to AB's file.
We had previously used a slightly modified version of AB's file:
  ../vntxt_0_deva.txt (his original file being ../vntxt_0_deva_orig.txt)
However, one of the changes in this file is not needed,
  namely {#रााण꣫#} -> {#राण॑#}  is removed.

In following work will use this as AB version:
  ../vntxt_0_deva_rev.txt
whose changes are noted in change_vntxt_0_deva_rev.txt
  Note: this also corrects a few typos in AB original file.

-------------------------------------------------------
cd transcodepwg
# construct slp1 version ../vntxt_1_rev.txt  from ../vntxt_0_deva_rev.txt
# use the deva1 transcoder files (slp1_deva1.xml and deva1_slp1.xml).
#  these transcoder files are in pwgtranscoder2 sub-directory.

python pwg_transcode.py pwgtranscoder2 deva1 slp1 ../vntxt_0_deva_rev.txt ../vntxt_1_rev.txt
# check invertibility 
python pwg_transcode.py pwgtranscoder2 slp1 deva1 ../vntxt_1_rev.txt tempchk.txt
diff ../vntxt_0_deva_rev.txt tempchk.txt | wc -l
0  # invertibility checks.

# compare to previous vntxt_1.
diff ../vntxt_1.txt ../vntxt_1_rev.txt  > ../diff_vntxt_1-1_rev.txt
64 lines in diff file (so 16 lines changed).
These are corrections to some accents which were incorrect in vntxt_1.txt.

# as a further check, examine the extended ascii charactersin vntxt_1_rev.txt
cd ../
python check_ea.py vntxt_1_rev.txt check_ea_vntxt_1_rev.txt
  Note no Devanagari characters!

conclusion:
vntxt_1_rev.txt looks ok to Jim
----------------------------------------------------------
09-28-2024
compare to prior versions of deva1_slp1.xml
see transcoderpwg/readme_deva1.txt

cd transcoderpwg
#copy deva1_slp1.xml to csl-websanlexicon and csl-apidev
cp pwgtranscoder2/deva1_slp1.xml /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/utilities/transcoder/deva1_slp1.xml

cp pwgtranscoder2/deva1_slp1.xml /c/xampp/htdocs/cologne/csl-apidev/utilities/transcoder/deva1_slp1.xml

# sync csl-websanlexicon 
cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
git add . # deva1_slp1.xml
git commit -m "deva1_slp1.xml transcoder file.
Ref: https://github.com/sanskrit-lexicon/PWG/issues/76"
git push

cp pwgtranscoder2/deva1_slp1.xml /c/xampp/htdocs/cologne/csl-apidev/utilities/transcoder/deva1_slp1.xml

# sync csl-apidev
cd /c/xampp/htdocs/cologne/csl-apidev
# modify .gitignore and simple-search/.gitignore so deva_slp1.xml tracked
git add . # deva1_slp1.xml
git commit -m "deva1_slp1.xml transcoder file.
Ref: https://github.com/sanskrit-lexicon/PWG/issues/76"
git push

# sync cologne server
login to cologne server.
for csl-websanlexicon and csl-apidev, do git pull

# sync this PWG repo to Github
--------------------------------------------------------------------
09-30-2024
cp vntxt_1_rev.txt vntxt_2.txt
---
Change the [Page:VNv-ppp] lines  (
 Add two fields:
* [v-pppp]  This is synthetic for volus 
  pc value
  newurl: https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpng/pwgv-pppp.png
* [https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpng/CDSLFILENAME.png]
  old url

Note:

/c/xampp/htdocs/cologne/csl-websanlexicon/v02/distinctfiles/pwg/web/webtc/pdffiles.txt

sample:
1-0001:pwg1-0001.pdf:a
1-0003:pwg1-0003.pdf:a
1-0005:pwg1-0005.pdf:aMSuka
1-0007:pwg1-0007.pdf:aMhasaspati

See pwg
Construct pdf
---------------------------------------------------
pwgvn/readme_vn_pdfs.txt
1. Update pdffiles.txt (csl-websanlexicon)
2. Cologne server PWGScanpdf
3. sanskrit-lexicon-scans/pwg repo
   Added the 10 pages to pdffiles directory.

---------------------------------------------------
10-01-2024
We now have the 'pc' field represented, and coordinated with the pdfs.
Example:
[Page:VN1-001][1-1143][https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpng/pwg1-0000--13.png]
The 2nd subfield will yield '<pc>1-1143' in metaline.
Note the 3rd field [httpsL// ...]  is no longer needed.

-----------------------------------
vntxt-2.txt 
fill in the 'do.' lines
21 matches for "do[.]" in buffer: vntxt_2.txt


page-name error:
https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpdf/pwg6-0705.pdf
  shows pages 707, 708
https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpdf/pwg6-0707.pdf
  shows pages 705, 706

1. Interchange these on Cologne server
2. Interchange these on github repo sanskrit-lexicon-scans/pwg


-----------------------------------
10-02-2024
Prepare L-nums for the correction entries.
Add field to VN.-001  (. = 1,..., 6)
Example:
[L:14148][Page:VN1-001][1-1143][https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpng/pwg1-0000--13.png]
Here L=14148 is the cdsl L of preceding entry, i.e. of last entry of volume VN1.

----
Start with pwg.txt from csl-orig at commit
  40d3269407ac82a093e98b719598600b9ada68e3

cd /c/xampp/htdocs/cologne/csl-orig
git show 40d326940:v02/pwg/pwg.txt > /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue76/temp_pwg_0.txt

cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue76

-----------------------------------
cp temp_pwg_0.txt temp_pwg_1.txt
Manual change: so the L-nums for VN4 can be 51684.xx
---
old: <L>51684.1<pc>5-0001<k1>ba<k2>ba
new: <L>51685<pc>5-0001<k1>ba<k2>ba
---
old: <L>51685<pc>5-0001<k1>ba<k2>ba
new: <L>51685.1<pc>5-0001<k1>ba<k2>ba
---
Similarly, adjust for VN6
old: <L>96987.1<pc>7-0001<k1>Sa<k2>Sa
new: <L>96988<pc>7-0001<k1>Sa<k2>Sa
---
old: <L>96988<pc>7-0001<k1>Sa<k2>Sa<h>1
new: <L>96988.1<pc>7-0001<k1>Sa<k2>Sa<h>1

-----------------------------------
;; New entry (L-88836.1) suggested
{#vavray#}	 ¦ [6.0817] Hinzuzufügen: {#vavray#} (von {#vavra#}), {#vavra/yate#} {%sich zurückzichen%} <ls>ṚV. 8,40,2.</ls>

AB suggests making a new entry for this in temp_pwg_1.txt
such as

<L>88836.1<pc>6-0817<k1>vavray<k2>vavray
{#vavray#}¦ (von {#vavra#}), {#vavra/yate#} {%sich zurückzichen%} <ls>ṚV. 8,40,2.</ls>
<LEND>

HOWEVER, Jim thinks  This `{#vavray#}	 ¦ [6.0817] ` IS the new entry,
 and there is no need for the duplicative 88836.1
  
============================================================

10-03-2024

python make_vntxt_3.py vntxt_2.txt vntxt_3.txt
638 lines read from vntxt_2.txt
adjust_semicolon changes 9 lines, resulting in 647 lines
21 lines read from vntxt_3_extra.txt
adjust_extra inserts 21 lines, resulting in 668 lines
adjust_question comments out 3 lines, resulting in 668 lines
41 lines read from vntxt_3_change.txt
init_change: 6 changes from vntxt_3_change.txt
adjust_change to  6 lines, resulting in 668 lines
668 lines written to vntxt_3.txt

-----------------------------------
Discussion of  make_vntxt_3.py

1. Some comments start with ';; '
   move this comment to a new record before the entry
   e.g. X;;Y -> ';;Y'<LB>X
-----------------------------------
2. Insert extra lines
???	 ¦ [1.0956] — [1.1016] ist für <ls>ŚĀṄKH. GṚHY.</ls> (wenn drei Zahlen folgen) überall <ls>ŚĀṄKH. ŚR.</ls> zu lesen. ;; This applies to all entries between L-11844 and L-12698 (Sp. 956–1016) [i.e., 20 cases— 12121, 12122, 12145, 12196 (2), 12217, 12247, 12282, 12291, 12350, 12352, 12369, 12448, 12457, 12470, 12513, 12561, 12593, 12602 and 12691]
Comment this line and insert 21 entries, using file vntxt_3_extra.txt

This is the list with associated L.
11847 {#upanayana#} 1-0956  Jim suggests
12106 {#upaSaya/#}  1-0974  Jim suggests
12121 {#upaSruti#} 1-0975
12122 {#upaSrotar#} 1-0976
12145 {#upasa/dya#} 1-0977
12196 {#upa/sTa#} 1-0980
12217 {#upasparSana#} 1-0982
12247 {#upAMSu/#} 1-0984
12282 {#upAna/h#} 1-0987
12291 {#upAya#} 1-0988
12350 {#upottama/#} 1-0992
12352 {#upodayam#} 1-0992
12369 {#uB#} 1-0993
12448 {#uru/#} 1-0999
12457 {#uru/gavyUti#} 1-1000
12470 {#uru/DAra#} 1-1001
12513 {#urva/rA#} 1-1003
12561 {#u/lmuka#} 1-1007
12593 {#uSi/j#} 1-1009
12602 <hom>1.</hom> {#uz#} 1-1010
12691 <hom>1.</hom> {#usri/ya#} 1-1016

-----------------------------------
3. comment out 3 lines beginning with '?'

-----------------------------------
4. misc. changes
 see vntxt_3_change.txt

------------------------------
There are 2 duplicate lines in vntxt_2.txt
    228:DUP <hom>1.</hom> {#anurkAya#}	 ¦ [1.0199] Z. 23 lies: {#anukArya#}.
    255:DUP {#aloha#}	 ¦ [1.0463] lies: <ls>P. 4,1,99.</ls>
These 2 are assumed to be in accordance with the print,
 and no changes are retained in vntxt_3.txt

-----------------------------
END of vntxt_3.txt discussion

------------------------------------------------------
10-04-2024
python make_vntxt_4.py vntxt_3.txt vntxt_4.txt
init_recs finds 619 records
628 entries  NOTE: 619 + 9 extra alternates (see alternates below)
update_entries_ltnum: 131 lines changed
update_entries_page: 619 lines changed
update_entries_revsup: #rev = 627, # sup = 1
225 entries in volume 1
150 entries in volume 2
106 entries in volume 3
70 entries in volume 4
19 entries in volume 5
58 entries in volume 6
check_pc_vol finds 0 problems
1884 lines written to vntxt_4.txt

Note: alternate headwords in VN
{#aDiSrayaRa#} und {#aDiSrayitavE#}
{#anAvraska#} und {#anASIrdA#}
{#kAmAkzI#} und {#kAmAKyA#}
{#jaMh#} und {#jaMhas#}
{#wowaka#}, {#wotalA#} und {#wodalatantra#}
{#AgniveSi#}, {#AgniveSI#}
{#Alapana#} und {#Alapti#}
{#gaganaromanTa#}, {#gaganaromantAyita#}

-----------
(+ 225 150 106 70 19 58)  628
(* 628 3) 1884  # number of lines in vntxt_4.txt
(* 4 628) 2512
(+ 1130054 2512) 1132566 
-------------------------------------------------------------
temp_pwg_2.txt

python merge_vn.py temp_pwg_1.txt vntxt_4.txt temp_pwg_2.txt

----------------------------------------------------------------
local install version 2 of pwg

cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok  No problems noticed
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue76

-------------------------------------------------
revise csl-orig
The missing VN entries are now 'squeezed' in at the
end of the appropriate volumes in pwg.txt

revise csl-websanlexicon
1) '<info n="rev"/>' and `<info n="sup"/>` generate text.
  Currently marked only for the missing VN records.
2) <h> in metaline is represented in list display left panel.
   This also for pw and pwkvn, as well as pwg and mw.
3) [Pagev-nnnn] display changed so it is 'inline' (no line break).
  In the referential pages of the vntxt_4.txt, the representation
  is [vgl. Pagev-nnnn].

revise csl-pywork
1) {{Lbody=L}} generates alternate entries in pwg.xml.

revise csl-apidev
 sh apidev_copy.sh from csl-websanlexicon/v02.

---------------------------------------------
sync to github

-----------------------------------
sync csl-orig to Github
(using temp_pwg_2.txt)
cd /c/xampp/htdocs/cologne/csl-orig

git add . # pwg.txt
git commit -m "PWG: missing VN
Ref: https://github.com/sanskrit-lexicon/PWG/issues/76"
# 2517 insertions(+), 5 deletions(-)

git push

----------------------------------
cd /c/xampp/htdocs/cologne/csl-websanlexicon
git add .
git commit -m "PWG: missing VN
Ref: https://github.com/sanskrit-lexicon/PWG/issues/76"

git push

----------------------------------
cd /c/xampp/htdocs/cologne/csl-pywork
git add .
git commit -m "PWG: missing VN
Ref: https://github.com/sanskrit-lexicon/PWG/issues/76"

git push

----------------------------------
cd /c/xampp/htdocs/cologne/csl-apidev
git add .
git commit -m "PWG: missing VN
Ref: https://github.com/sanskrit-lexicon/PWG/issues/76"

git push

---------------------------------------------
----------------------------------------------------------------
update cologne server

cd scans/csl-orig
git pull
cd scans/csl-websanlexicon
git pull
cd scans/csl-pywork
git pull
cd scans/csl-apidev
git pull
cd scans/csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/
sh generate_dict.sh pw  ../../PWGScan/2020/
sh generate_dict.sh pwkvn  ../../PWGScan/2020/

---------------------------------------------
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue76

sync this repo to github
