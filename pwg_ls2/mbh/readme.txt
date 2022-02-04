PWG/pwg_ls2/mbh


Refer:
 https://github.com/

Start with a copy of csl-orig/v02/pwg/pwg.txt at commit
  88fe8659a59df017afc869189541abb43773d5fe
  
# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_pwg_00.txt in this spruch directory
  git show 88fe8659:v02/pwg/pwg.txt > /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/mbh/temp_pwg_00.txt
# return to this mbh directory
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/mbh/
# -------------------------------------------------------------
Focus on ls of form '<ls>Spr. (II)...</ls>'
# -------------------------------------------------------------
5313 matches in 5307 lines for "<ls>Spr. (II)" in buffer: temp_pwg_00.txt


python listls_abnormal.py 'MBH.' temp_pwg_00.txt listls_abnormal_mbh.txt

NORMAL:
  1a 28744 <ls>MBH. ([0-9]+), ([0-9]+[.]?)</ls>
  1b   573<ls>MBH. ([0-9]+), ([0-9]+[.]?) fgg?[.]</ls>
  1c    25 <ls>MBH. ([0-9]+), ([0-9]+[.,]?) v[.] l[.]</ls>
  1d   389 <ls>MBH.</ls>
  1e    23 <ls>MBH.[^<]*ed[.] Bomb[.].*?</ls>
  2a      <ls n="MBH[.]">([0-9]+), ([0-9]+[.]?)</ls>
  2b      <ls n="MBH[.]">([0-9]+), ([0-9]+[.]?) fgg?[.]</ls>
  2c      <ls n="MBH[.]">([0-9]+), ([0-9]+[.,]?) v[.] l[.]</ls>
  2d      <ls n="MBH[.] ([0-9]+),">([0-9]+[.]?)</ls>
  2e      <ls n="MBH[.] ([0-9]+),">([0-9]+[.]?) fgg?[.]</ls>
  2f      <ls n="MBH[.] ([0-9]+),">([0-9]+[.,]?) v[.] l[.]</ls>
total: 29760
ABNORMAL:
 8764


# -------------------------------------------------------------
change_01.txt manually constructed in steps
# -------------------------------------------------------------
cp temp_pwg_00.txt temp_pwg_01.txt
touch change_01.txt

# 1st step of markup improvement
<ls>MBH. 1, 234. 5, 678.</ls> ->
 <ls>MBH. 1, 234.</ls> <ls n="MBH.">5, 678.</ls>

python make_change_ls.py 1 temp_pwg_01.txt temp_change_01.txt
 2691 lines changed
# insert temp_change_01.txt into change_01.txt

python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt

python listls_abnormal.py 'MBH.' temp_pwg_01.txt listls_abnormal_mbh_01.txt

NORMAL:
  1a 31435 <ls>MBH. ([0-9]+), ([0-9]+[.]?)</ls>
  1b   573<ls>MBH. ([0-9]+), ([0-9]+[.]?) fgg?[.]</ls>
  1c    25 <ls>MBH. ([0-9]+), ([0-9]+[.,]?) v[.] l[.]</ls>
  1d   389 <ls>MBH.</ls>
  1e    23 <ls>MBH.[^<]*ed[.] Bomb[.].*?</ls>
  2a  2696 <ls n="MBH[.]">([0-9]+), ([0-9]+[.]?)</ls>
  2b     1 <ls n="MBH[.]">([0-9]+), ([0-9]+[.]?) fgg?[.]</ls>
  2c       <ls n="MBH[.]">([0-9]+), ([0-9]+[.,]?) v[.] l[.]</ls>
  2d       <ls n="MBH[.] ([0-9]+),">([0-9]+[.]?)</ls>
  2e       <ls n="MBH[.] ([0-9]+),">([0-9]+[.]?) fgg?[.]</ls>
  2f       <ls n="MBH[.] ([0-9]+),">([0-9]+[.,]?) v[.] l[.]</ls>
total: 35142
ABNORMAL:
 6073

# -------------------------------------------------------------
# 2nd step of markup improvement
python make_change_ls.py 2 temp_pwg_01.txt temp_change_02.txt
 <ls>MBH. 1, 234. 567.</ls> ->
   <ls>MBH. 1, 234.</ls> <ls n="MBH. 1,">567.</ls>
   
 # insert temp_change_02.txt into change_01.txt

python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
 4441 changes
 
python listls_abnormal.py 'MBH.' temp_pwg_01.txt listls_abnormal_mbh_02.txt

NORMAL:
  1a 33185 <ls>MBH. ([0-9]+), ([0-9]+[.]?)</ls>
  1b   573<ls>MBH. ([0-9]+), ([0-9]+[.]?) fgg?[.]</ls>
  1c    25 <ls>MBH. ([0-9]+), ([0-9]+[.,]?) v[.] l[.]</ls>
  1d   389 <ls>MBH.</ls>
  1e    23 <ls>MBH.[^<]*ed[.] Bomb[.].*?</ls>
  2a  2696 <ls n="MBH[.]">([0-9]+), ([0-9]+[.]?)</ls>
  2b     1 <ls n="MBH[.]">([0-9]+), ([0-9]+[.]?) fgg?[.]</ls>
  2c       <ls n="MBH[.]">([0-9]+), ([0-9]+[.,]?) v[.] l[.]</ls>
  2d  2130 <ls n="MBH[.] ([0-9]+),">([0-9]+[.]?)</ls>
  2e       <ls n="MBH[.] ([0-9]+),">([0-9]+[.]?) fgg?[.]</ls>
  2f       <ls n="MBH[.] ([0-9]+),">([0-9]+[.,]?) v[.] l[.]</ls>
total: 39022
ABNORMAL:
 4323

# -------------------------------------------------------------
# 3rd step of markup improvement
python make_change_ls.py 3 temp_pwg_01.txt temp_change_03.txt
 744 changes
<ls>MBH. n1, m1. n2, m2.</ls> ->
 <ls>MBH. n1, m1.</ls> <ls n="MBH.">n2, m2.</ls>
   
 # insert temp_change_03.txt into change_01.txt

python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
 5185 lines changed
 
python listls_abnormal.py 'MBH.' temp_pwg_01.txt listls_abnormal_mbh_03.txt

NORMAL:
  1a 33929 <ls>MBH. ([0-9]+), ([0-9]+[.]?)</ls>
  1b   573<ls>MBH. ([0-9]+), ([0-9]+[.]?) fgg?[.]</ls>
  1c    25 <ls>MBH. ([0-9]+), ([0-9]+[.,]?) v[.] l[.]</ls>
  1d   389 <ls>MBH.</ls>
  1e    23 <ls>MBH.[^<]*ed[.] Bomb[.].*?</ls>
  2a  4423 <ls n="MBH[.]">([0-9]+), ([0-9]+[.]?)</ls>
  2b     1 <ls n="MBH[.]">([0-9]+), ([0-9]+[.]?) fgg?[.]</ls>
  2c       <ls n="MBH[.]">([0-9]+), ([0-9]+[.,]?) v[.] l[.]</ls>
  2d  2130 <ls n="MBH[.] ([0-9]+),">([0-9]+[.]?)</ls>
  2e       <ls n="MBH[.] ([0-9]+),">([0-9]+[.]?) fgg?[.]</ls>
  2f       <ls n="MBH[.] ([0-9]+),">([0-9]+[.,]?) v[.] l[.]</ls>
total: 41493
ABNORMAL:
 3579

# -------------------------------------------------------------
# 4th step of markup improvement
python make_change_ls.py 4 temp_pwg_01.txt temp_change_04.txt
 55 malformed   <ls>MBH. n1 n2 n3 ...</ls>  and each n is a digit
 sequence ending in comma or period.  
Manually changed.
 
 # insert temp_change_04.txt into change_01.txt

python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
 5185 lines changed
 
# -------------------------------------------------------------
# 5th step of markup improvement
python make_change_ls.py 5 temp_pwg_01.txt temp_change_05.txt
 1977 lines changed
 
 997101 new <ls>NÄªLAK.</ls> zu <ls>MBH.</ls>  13, 23, 1. Bombay ed. ?

 # insert temp_change_05.txt into change_01.txt

python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
 7260 lines changed
 
python listls_abnormal.py 'MBH.' temp_pwg_01.txt listls_abnormal_mbh_05.txt

NORMAL:
  1a 35911 <ls>MBH. ([0-9]+), ([0-9]+[.]?)</ls>
  1b   573<ls>MBH. ([0-9]+), ([0-9]+[.]?) fgg?[.]</ls>
  1c    25 <ls>MBH. ([0-9]+), ([0-9]+[.,]?) v[.] l[.]</ls>
  1d   389 <ls>MBH.</ls>
  1e    23 <ls>MBH.[^<]*ed[.] Bomb[.].*?</ls>
  2a  7935 <ls n="MBH[.]">([0-9]+), ([0-9]+[.]?)</ls>
  2b     1 <ls n="MBH[.]">([0-9]+), ([0-9]+[.]?) fgg?[.]</ls>
  2c       <ls n="MBH[.]">([0-9]+), ([0-9]+[.,]?) v[.] l[.]</ls>
  2d  5282 <ls n="MBH[.] ([0-9]+),">([0-9]+[.]?)</ls>
  2e       <ls n="MBH[.] ([0-9]+),">([0-9]+[.]?) fgg?[.]</ls>
  2f       <ls n="MBH[.] ([0-9]+),">([0-9]+[.,]?) v[.] l[.]</ls>
total: 50147
ABNORMAL:
 1590

# -------------------------------------------------------------
# 6th step of markup improvement
handle fg. and fgg.
python make_change_ls.py 6 temp_pwg_01.txt temp_change_06.txt
 566 lines changed
 
 # insert temp_change_06.txt into change_01.txt

python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
 7843 lines changed
 
python listls_abnormal.py 'MBH.' temp_pwg_01.txt listls_abnormal_mbh_06.txt

NORMAL:
  1a 36277 <ls>MBH. ([0-9]+), ([0-9]+[.]?)</ls>
  1b   776<ls>MBH. ([0-9]+), ([0-9]+[.]?) fgg?[.]</ls>
  1c    25 <ls>MBH. ([0-9]+), ([0-9]+[.,]?) v[.] l[.]</ls>
  1d   396 <ls>MBH.</ls>
  1e    23 <ls>MBH.[^<]*ed[.] Bomb[.].*?</ls>
  2a  8476 <ls n="MBH[.]">([0-9]+), ([0-9]+[.]?)</ls>
  2b   232 <ls n="MBH[.]">([0-9]+), ([0-9]+[.]?) fgg?[.]</ls>
  2c       <ls n="MBH[.]">([0-9]+), ([0-9]+[.,]?) v[.] l[.]</ls>
  2d  5845 <ls n="MBH[.] ([0-9]+),">([0-9]+[.]?)</ls>
  2e   278 <ls n="MBH[.] ([0-9]+),">([0-9]+[.]?) fgg?[.]</ls>
  2f       <ls n="MBH[.] ([0-9]+),">([0-9]+[.,]?) v[.] l[.]</ls>
total: 52328
ABNORMAL:
 1021

# -------------------------------------------------------------
# 7th step of markup improvement

python make_change_ls.py 7 temp_pwg_01.txt temp_change_07.txt
 670 lines changed
 
 # insert temp_change_07.txt into change_01.txt

python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
 8690 lines changed
 
python listls_abnormal.py 'MBH.' temp_pwg_01.txt listls_abnormal_mbh_07.txt

NORMAL:
  1a 37048 <ls>MBH. ([0-9]+), ([0-9]+[.]?)</ls>
  1b   827 <ls>MBH. ([0-9]+), ([0-9]+[.]?) fgg?[.]</ls>
  1c    25 <ls>MBH. ([0-9]+), ([0-9]+[.,]?) v[.] l[.]</ls>
  1d   424 <ls>MBH.</ls>
  1e    23 <ls>MBH.[^<]*ed[.] Bomb[.].*?</ls>
  2a  8923 <ls n="MBH[.]">([0-9]+), ([0-9]+[.]?)</ls>
  2b   273 <ls n="MBH[.]">([0-9]+), ([0-9]+[.]?) fgg?[.]</ls>
  2c       <ls n="MBH[.]">([0-9]+), ([0-9]+[.,]?) v[.] l[.]</ls>
  2d  6154 <ls n="MBH[.] ([0-9]+),">([0-9]+[.]?)</ls>
  2e   300 <ls n="MBH[.] ([0-9]+),">([0-9]+[.]?) fgg?[.]</ls>
  2f       <ls n="MBH[.] ([0-9]+),">([0-9]+[.,]?) v[.] l[.]</ls>
total: 53997
ABNORMAL:
 176 

# -------------------------------------------------------------
# 8th step of markup improvement
Select lines with ' MBH.'
 about 500 lines. put in file temp_unmarked_mbh.txt
 Manually change.

insert into change_01
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
 9200 lines changed
 
python listls_abnormal.py 'MBH.' temp_pwg_01.txt listls_abnormal_mbh_08.txt

NORMAL:
  1a 37516 <ls>MBH. ([0-9]+), ([0-9]+[.]?)</ls>
  1b   846 <ls>MBH. ([0-9]+), ([0-9]+[.]?) fgg?[.]</ls>
  1c    26 <ls>MBH. ([0-9]+), ([0-9]+[.,]?) v[.] l[.]</ls>
  1d   443 <ls>MBH.</ls>
  1e    23 <ls>MBH.[^<]*ed[.] Bomb[.].*?</ls>
  2a  9178 <ls n="MBH[.]">([0-9]+), ([0-9]+[.]?)</ls>
  2b   285 <ls n="MBH[.]">([0-9]+), ([0-9]+[.]?) fgg?[.]</ls>
  2c       <ls n="MBH[.]">([0-9]+), ([0-9]+[.,]?) v[.] l[.]</ls>
  2d  6324 <ls n="MBH[.] ([0-9]+),">([0-9]+[.]?)</ls>
  2e   312 <ls n="MBH[.] ([0-9]+),">([0-9]+[.]?) fgg?[.]</ls>
  2f       <ls n="MBH[.] ([0-9]+),">([0-9]+[.,]?) v[.] l[.]</ls>
total: 54953
ABNORMAL:
 208 


# -------------------------------------------------------------
 generate prototype change transactions for abnormals
python change_abnormal.py 'MBH.' temp_pwg_01.txt temp_change_abnormal.txt
204 abnormal lines found
204 change transactions temp_change_abnormal.txt

edit temp_change_abnormal.txt manually to change 'new'.
Then, insert into change_01.txt

# -------------------------------------------------------------
Final situation (after still more changes)

python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
 9379 changes

python listls_abnormal.py 'MBH.' temp_pwg_01.txt listls_abnormal_mbh_08.txt

NORMAL:
  1a 37664 <ls>MBH. ([0-9]+), ([0-9]+[.]?)</ls>
  1b   852 <ls>MBH. ([0-9]+), ([0-9]+[.]?) fgg?[.]</ls>
  1c    26 <ls>MBH. ([0-9]+), ([0-9]+[.,]?) v[.] l[.]</ls>
  1d   454 <ls>MBH.</ls>
  1e    23 <ls>MBH.[^<]*ed[.] Bomb[.].*?</ls>
  2a  9272 <ls n="MBH[.]">([0-9]+), ([0-9]+[.]?)</ls>
  2b   291 <ls n="MBH[.]">([0-9]+), ([0-9]+[.]?) fgg?[.]</ls>
  2c       <ls n="MBH[.]">([0-9]+), ([0-9]+[.,]?) v[.] l[.]</ls>
  2d  6388 <ls n="MBH[.] ([0-9]+),">([0-9]+[.]?)</ls>
  2e   316 <ls n="MBH[.] ([0-9]+),">([0-9]+[.]?) fgg?[.]</ls>
  2f       <ls n="MBH[.] ([0-9]+),">([0-9]+[.,]?) v[.] l[.]</ls>
total: 55286
ABNORMAL:
 27  
27 matches for "Abnormal ls:" in buffer: temp_change_abnormal2.txt
 <ls>MBH. Bd. III, S. 818, Z. 5. u. 4, v. u.</ls>
 <ls>MBH., Kap. 13-58.</ls>
 <ls>MBH. I</ls>
 <ls>MBH. III</ls>
 <ls>MBH. 9, <is>Adhy</is>. 33. fgg.</ls>
 <ls>MBH. 1, <is>Adhy</is>. 188</ls>
 <ls>MBH. 1-3</ls>
 <ls>MBH. 2, <is>Adhy</is>. 45 - 69.</ls>
 <ls>MBH. 2, <is>Adhy</is>. 1</ls>
 <ls n="MBH.">I, S. 418</ls>
 <ls>MBH. 1. 3-9. 12-14</ls>
 <ls>MBH. 1. 3. 5-8. 12-14</ls>
 <ls>MBH. 1-8</ls>
 <ls>MBH. 9-14</ls>
 <ls>MBH. 1. 3. 5-8. 12-14</ls>
 <ls n="MBH.">1, Kap. 142</ls>
 <ls>MBH. I, S. 656. fgg.</ls>
 <ls>MBH. I, S. 407</ls>
 <ls>MBH. I, S. 308.</ls>
 <ls>MBH. I, S. 231.</ls>
 <ls>MBH. I, S. 245.</ls>
 <ls>MBH. I, S. 254.</ls>
 <ls>MBH. I, S. 384. II, S. 179.</ls>
 <ls>MBH. 1, <is>Adhy</is>. 61</ls>
 <ls>MBH. 3, <is>Adhy</is>. 222. fgg.</ls>
 <ls>MBH. IV, 432.</ls>
 <ls>MBH. IV, 433. fgg.</ls>

# -------------------------------------------------------------

# -------------------------------------------------------------
install temp_pwg_01.txt into csl-orig.

cp temp_pwg_01.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg ' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
 #prints 'ok'

; -----------------------------------------------
</ls> <ls>
</ls> <ls n="MBH.">
<ls n="MBH. ,">
<ls n="R.">
</ls> <ls n="ṚV.">
</ls> <ls n="HARIV.">
</ls> <ls n="P.">
</ls> <ls n="M.">

</ls> <ls n="AV.">
