PWG/pwg_ls2/hariv


Refer:
 https://github.com/

Start with a copy of csl-orig/v02/pwg/pwg.txt at commit
  b44b29b5ffc262b34d1ab18f91017aea10a7bc8f
  
# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_pwg_00.txt in this spruch directory
  git show b44b29b:v02/pwg/pwg.txt > /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/hariv/temp_pwg_00.txt
# return to this mbh directory
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/hariv/
# -------------------------------------------------------------
Focus on ls of form '<ls>HARIV...</ls>'
Also handle those such as ' HARIV.'2
11350 matches in 11338 lines for "<ls>HARIV." in buffer: pwg.txt
270 matches in 269 lines for " HARIV\." in buffer: pwg.txt

procedure similar to that used for MBH, with the difference that there
are no parvans in HARIV, so a full link is of form '<ls>HARIV. N.</ls>',
where N is a digit sequence and the final '.' is optional.
9061 matches in 9056 lines for "<ls>HARIV\. [0-9]+[.]?</ls>" in buffer: temp_pwg_00.txt

# -------------------------------------------------------------
cp temp_pwg_00.txt temp_pwg_01.txt
We will manually add changes contained in change_01.txt to update
 temp_pwg_01.txt.


python listls_abnormal.py 'HARIV.' temp_pwg_01.txt temp_abnormal_hariv_00.txt

NORMAL:
  1a  9061 <ls>HARIV. ([0-9]+[.]?)</ls>
  1b   309<ls>HARIV. ([0-9]+[.]?) fgg?[.]</ls>
  1c    13 <ls>HARIV. ([0-9]+[.,]?) v[.] l[.]</ls>
  1d   254 <ls>HARIV.</ls>
  1e    23 <ls>HARIV.[^<]*ed[.] Bomb[.].*?</ls>
  2a     2 <ls n="HARIV[.]">([0-9]+[.]?)</ls>
  2b     0 <ls n="HARIV[.]">([0-9]+[.]?) fgg?[.]</ls>
  2c     0 <ls n="HARIV[.]">([0-9]+[.,]?) v[.] l[.]</ls>
total: 9639
ABNORMAL:
1714 abnormal ls written to temp_abnormal_hariv_00.txt


# -------------------------------------------------------------
change_01.txt manually constructed in steps
# -------------------------------------------------------------
cp temp_pwg_00.txt temp_pwg_01.txt
touch change_01.txt

# 0th step of markup improvement
  handle ' HARIV.'
  Also, many hidden MBH (e.g. <ls>1, 234</ls> -> <ls n="MBH.">1, 234</ls>)

python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
 270 changes
 
python listls_abnormal.py 'HARIV.' temp_pwg_01.txt temp_listls_abnormal_unm.txt

NORMAL:
  1a  9239 <ls>HARIV. ([0-9]+[.]?)</ls>
  1b   316<ls>HARIV. ([0-9]+[.]?) fgg?[.]</ls>
  1c    13 <ls>HARIV. ([0-9]+[.,]?) v[.] l[.]</ls>
  1d   253 <ls>HARIV.</ls>
  1e     0 <ls>HARIV.[^<]*ed[.] Bomb[.].*?</ls>
  2a     4 <ls n="HARIV[.]">([0-9]+[.]?)</ls>
  2b     0 <ls n="HARIV[.]">([0-9]+[.]?) fgg?[.]</ls>
  2c     0 <ls n="HARIV[.]">([0-9]+[.,]?) v[.] l[.]</ls>
total: 9639
ABNORMAL:
1804 abnormal ls written to temp_listls_abnormal_unm.txt
# -------------------------------------------------------------
1st step 
<ls>HARIV. 234. 678.</ls> ->
 <ls>HARIV. 234.</ls> <ls n="HARIV.">678.</ls>

python make_change_ls.py 1 temp_pwg_01.txt temp_change_01.txt
 634 lines changed
# insert temp_change_01.txt into change_01.txt

python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
1975 change transactions


python listls_abnormal.py 'HARIV.' temp_pwg_01.txt temp_listls_abnormal_01.txt

NORMAL:
  1a 10846 <ls>HARIV. ([0-9]+[.]?)</ls>
  1b   414<ls>HARIV. ([0-9]+[.]?) fgg?[.]</ls>
  1c    13 <ls>HARIV. ([0-9]+[.,]?) v[.] l[.]</ls>
  1d   253 <ls>HARIV.</ls>
  1e     0 <ls>HARIV.[^<]*ed[.] Bomb[.].*?</ls>
  2a  2600 <ls n="HARIV[.]">([0-9]+[.]?)</ls>
  2b   210 <ls n="HARIV[.]">([0-9]+[.]?) fgg?[.]</ls>
  2c     0 <ls n="HARIV[.]">([0-9]+[.,]?) v[.] l[.]</ls>
total: 14336
ABNORMAL:
 99  

# -------------------------------------------------------------
 generate prototype change transactions for abnormals
python change_abnormal.py 'HARIV.' temp_pwg_01.txt temp_change_abnormal.txt
99 change transactions temp_change_abnormal.txt
Manually correct these, and insert into change_01.txt

# -------------------------------------------------------------
# 2nd step of markup improvement
  python change_abnormal.py 'HARIV.' tem _pwg_01.txt temp_change_abnormal.txt
   99
  edit temp_change_abnormal.txt manually, insert into change_01.txt

python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
 2056 changes
 
python listls_abnormal.py 'HARIV.' temp_pwg_01.txt temp_listls_abnormal_02.txt

NORMAL:
  1a 10912 <ls>HARIV. ([0-9]+[.]?)</ls>
  1b   422<ls>HARIV. ([0-9]+[.]?) fgg?[.]</ls>
  1c    13 <ls>HARIV. ([0-9]+[.,]?) v[.] l[.]</ls>
  1d   254 <ls>HARIV.</ls>
  1e     0 <ls>HARIV.[^<]*ed[.] Bomb[.].*?</ls>
  2a  2647 <ls n="HARIV[.]">([0-9]+[.]?)</ls>
  2b   211 <ls n="HARIV[.]">([0-9]+[.]?) fgg?[.]</ls>

total: 14459
ABNORMAL:
 21
Details of abnormals:
See change_abnormal.txt

# -------------------------------------------------------------
cp temp_pwg_01.txt temp_pwg_02.txt
change_02.txt :
Find <ls>N...</ls> preceded by <ls>HARIV.  where N is a digit sequence.

python make_change2_ls.py 'HARIV.' temp_pwg_02.txt temp_change2_01.txt
# insert temp_change2_01.txt into change_02.txt

python ../01/updateByLine.py temp_pwg_01.txt change_02.txt temp_pwg_02.txt
#
python make_change_ls.py 1 temp_pwg_02.txt temp_change2_01a.txt
 0 items
# insert temp_change2_01a.txt into change_02.txt
python ../01/updateByLine.py temp_pwg_01.txt change_02.txt temp_pwg_02.txt

python change_abnormal.py 'HARIV.' temp_pwg_02.txt temp_change_pwg_02_abnormal.txt
# resolve temp_change_pwg_02_abnormal.txt and insert into change_02.txt
python ../01/updateByLine.py temp_pwg_01.txt change_02.txt temp_pwg_02.txt
 1189

python change_abnormal.py 'HARIV.' temp_pwg_02.txt temp_change_pwg_02a_abnormal.txt
26 change transactions temp_change_pwg_02a_abnormal.txt

python listls_abnormal.py 'HARIV.' temp_pwg_02.txt temp_pwg_02a_abnormal.txt
 
NORMAL:
  1a 10920 <ls>HARIV. ([0-9]+[.]?)</ls>
  1b   423<ls>HARIV. ([0-9]+[.]?) fgg?[.]</ls>
  1c    13 <ls>HARIV. ([0-9]+[.,]?) v[.] l[.]</ls>
  1d   242 <ls>HARIV.</ls>
  2a  3732 <ls n="HARIV[.]">([0-9]+[.]?)</ls>
  2b   265 <ls n="HARIV[.]">([0-9]+[.]?) fgg?[.]</ls>

total: 15595
ABNORMAL:
 26
#details of abnormals: see change_abnormal.txt
#cp temp_change_pwg_02a_abnormal.txt change_abnormal.txt
 
# -------------------------------------------------------------
install temp_pwg_02.txt into csl-orig.

cp temp_pwg_02.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg ' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
 #prints 'ok'

; -----------------------------------------------
</ls> <ls>
</ls> <ls n="HARIV.">
</ls> <ls n="MBH.">
<ls n="HARIV. ,">
<ls n="R.">
</ls> <ls n="ṚV.">
</ls> <ls n="HARIV.">
</ls> <ls n="P.">
</ls> <ls n="M.">

</ls> <ls n="AV.">
