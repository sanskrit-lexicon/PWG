PWG/pwg_ls2/mbh1


Refer:
 https://github.com/sanskrit-lexicon/PWG/issues/51 ?

Start with a copy of csl-orig/v02/pwg/pwg.txt at commit
  c61a45668168815d9de843bad805ff0bc4cf09df
  
# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_pwg_00.txt in this spruch directory
  git show c61a456:v02/pwg/pwg.txt > /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/mbh1/temp_pwg_00.txt
# return to this mbh directory
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/mbh1/

# -------------------------------------------------------------
 Get a count of <ls> by lsname

cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pwg/pywork/pwgauth/pwgbib_input.txt temp_bib.txt
#python lsextract.py 'ṚV.' temp_pwg_00.txt temp_bib.txt temp_RV.txt

python lsextract_all.py temp_pwg_00.txt temp_bib.txt lsextract_pwg_00.txt

# -------------------------------------------------------------
cp temp_pwg_00.txt temp_pwg_01.txt
 manual changes to temp_pwg_01.txt
 298 '</ls> <ls>Śl.' -> ' Śl.'
  22 '<ls>GOLĀDHY.</ls> <ls>BHUVANAK.' -> '<ls>GOLĀDHY. BHUVANAK.'
  20 '</ls> <ls>Anh.' -> ' Anh.'
 140  '</ls> <ls>an.' -> ' an.'
 450 '<ls>= ' -> '= <ls>'
 138 '<ls>ṚV.</ls> <ls>ANUKR' -> '<ls>ṚV. ANUKR'

python diff_to_changes.py temp_pwg_00.txt temp_pwg_01.txt change_01.txt
1190 changes written to change_01.txt

Note: pwg_tooltip.txt retrieved from another source, probably ../mbh/.
Changes were made (normally additions).
python make_change_space.py temp_pwg_01.txt pwg_tooltip.txt change_02.txt
2668 tooltips from temp_bib.txt
# replacements= 2568
6831 changes

mv temp_space_01.txt change_02.txt

python updateByLine.py temp_pwg_01.txt change_02.txt temp_pwg_02.txt
1149413 lines read from temp_pwg_01.txt
1149413 records written to temp_pwg_02.txt
6831 change transactions from change_02.txt
6831 of type new


cp temp_pwg_02.txt temp_pwg_03.txt
# manually change temp_pwg_03.txt
  15 ' Vgl.</ls>' -> '</ls> Vgl.'
 183 ' vgl.</ls>' -> '</ls> vgl.'
 396 ' zu</ls>' -> '</ls> zu'
 240 '<ls>(\([^<]*\))</ls>' -> (<ls>\1</ls>)'  (Emacs syntax regexp. change)
 206 '<ls>SCHIEFNER,</ls> <ls>Lebensb.' -> '<ls>SCHIEFNER,</ls> <ls>Lebensb.'
 109 ' nach</ls>' -> '</ls> nach'
  99 '<ls>SIDDH. K. zu P.' -> '<ls>SIDDH. K.</ls> zu <ls>P.'
  70 ' aus</ls>' -> '</ls> aus'
3062 '<ls>(' -> '(<ls>'
 566 ',</ls> <ls>Z. \([0-9]\)' -> ', Z. \1' (Emacs regex change)
 225 ';</ls>' -> '</ls>;'
  88 ' bei</ls>' -> '</ls> bei'
 643 '<ls>PAT.</ls> <ls>a. a. O.' -> '<ls>PAT. a. a. O. '
  42 '<ls>Verz. d.</ls> <ls>Tüb.' -> '<ls>Verz. d. Tüb.'
 542 ' in</ls>' -> '</ls> in'
 103 ' und</ls>' -> '</ls> und'
 40 '<ls>vgl.</ls>' -> vgl.
 80 '<ls>KULL. zu M.' -> '<ls>KULL.</ls> zu <ls>M.'
150 '<ls>MED.</ls> <ls>avy.' -> '<ls>MED. avy.'
 95 '<ls>).</ls> ' -> '). '
 And some more
python diff_to_changes.py temp_pwg_02.txt temp_pwg_03.txt change_03.txt
7007 changes written to change_03.txt

cp temp_pwg_03.txt temp_pwg_04.txt
 177  '<ls>=</ls>' -> '='
  73  '<ls>nach</ls>' -> 'nach'
  30   ' BR.' various
  20   ' ŚR.' various
   6    ' GṚHY.'
  20    ' UP.'
 150    ' P.'
 xxx    ' R.'
python diff_to_changes.py temp_pwg_03.txt temp_pwg_04.txt change_04.txt
13886 changes written to change_04.txt
change_04.txt

check xmll validity
cp temp_pwg_04.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg ' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg

# -------------------------------------------------------------
<ls>ĀŚV. GṚHY. 1413
<ls>ŚĀṄKH. GṚHY. 734
<ls>PĀR. GṚHY.  769
<ls>ĀŚR. GṚHY.



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
OLD
 <ls>R.</ls>
 <ls>Gorr.X</ls>
NEW
 <blank line>
 <ls>R. Gorr.X</ls>

python make_change_gorr.py temp_pwg_04.txt temp_change_gorr.txt
1045 possible changes written to temp_change_gorr.txt
; change_05.txt manual.
  temp_change_gorr.txt
  
python updateByLine.py temp_pwg_04.txt change_05.txt temp_pwg_05.txt
2090 change transactions from change_05.txt


# -------------------------------------------------------------
temp_pwg_06.txt manual (misc. cleanup not related directly to <ls>)
 Emacs format regex replacement: {#(\([^)#]*\))#} → ({#\1#})
 Example: {#(vastramAtre)#}  -> ({#vastramAtre#})
 7000+ changes

 Emacs format regex replacement: {%(\([^)%]*\))%} → ({%\1%})
 Example: {%(Heer)%}  -> ({%Heer%})
 120+ changes

python diff_to_changes.py temp_pwg_05.txt temp_pwg_06.txt change_06.txt
7570 changes written to change_06.txt

# -------------------------------------------------------------
install temp_pwg_06.txt into csl-orig.

cp temp_pwg_06.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg ' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
 #prints 'ok'
# -------------------------------------------------------------
Install Revisions made to pwg_tooltip.txt
cp pwg_tooltip.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pwg/pywork/pwgauth/pwgbib_input.txt

Update csl-pywork repository.
# -------------------------------------------------------------
Construct the summary of ls instances.
python lsextract_all.py temp_pwg_06.txt pwg_tooltip.txt lsextract_pwg_06.txt

python diff_to_changes.py temp_pwg_00.txt temp_pwg_06.txt temp.txt
28565 lines changed out of 1149413, about 2.5% of the lines of pwg.txt changed.
