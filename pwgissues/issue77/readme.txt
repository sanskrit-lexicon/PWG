09-18-2024 begin

Ref: https://github.com/sanskrit-lexicon/PWG/issues/77
 Remove gratuitous spaces in ls references.
 Start with pwg

This directory:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue77

----
Start with pwg.txt from csl-orig at commit
  ab27f766ce871ec85878e8e9db9cf7ce78cf4b8e

cd /c/xampp/htdocs/cologne/csl-orig
git show ab27f766c:v02/pwg/pwg.txt > /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue77/temp_pwg_0.txt

-------------------------------------------------------------
generate change file temp_change_1.txt
This file will be large. Since a temp file, not tracked by git.

# 1. remove space(s) between comma and digit in <ls...</ls>
# 2. remove space(s) at end of any line.

python make_change.py temp_pwg_0.txt temp_change_1.txt
689860 cases written to temp_change_1.txt
# temp_change_1.txt is 130MB !

# apply the changes
python updateByLine.py temp_pwg_0.txt temp_change_1.txt temp_pwg_1.txt
1149413 lines read from temp_pwg_0.txt
1149413 records written to temp_pwg_1.txt
689860 change transactions from temp_change_1.txt


# regenerate local displays from temp_pwg_1
# This to check xml validity.

cp temp_pwg_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok  No problems noticed
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue77

-----------------------------------------------
# remove empty lines in entry.

python remove_blank.py temp_pwg_1.txt temp_pwg_2.txt
1149413 lines read from temp_pwg_1.txt
adjust: 16000 empty body lines dropped
1133413 written to temp_pwg_2.txt

-----------------------------------------------
The [Pagev-xxxx] lines between entries are not needed,
  as duplicative of the subsequent <L><pc>v-xxxx
python remove_page_between.py temp_pwg_2.txt temp_pwg_3.txt
1133413 lines read from temp_pwg_2.txt
drop 3232 Page lines between entries
1130181 written to temp_pwg_3.txt

(+ 3232 1130181)

-----------------------------------------------
Reduce multiple blank lines to a single blank line

python reduce_multiple_blank.py temp_pwg_3.txt temp_pwg_4.txt
1130181 lines read from temp_pwg_3.txt
drop 138 extra blank lines
1130043 written to temp_pwg_4.txt

-----------------------------------------------
manual changes
cp temp_pwg_4.txt temp_pwg_5.txt
# manual edit temp_pwg_5.txt

(- 1149413 1130050 ) 19363 fewer lines in version 5 from version 0

-----------------------------------------------
# single blank line between entries
python analyze_between.py temp_pwg_5.txt analyze_between.txt

----------------------------------------------
# regenerate local displays from temp_pwg_5
# This to check xml validity.

cp temp_pwg_5.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok  No problems noticed
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue77
---------------------------------------------

sync to github

cd /c/xampp/htdocs/cologne/csl-orig
git add .
git commit -m "Ref: https://github.com/sanskrit-lexicon/PWG/issues/77"
git push

cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue77

---------------------------------------------
sync this issue to Github
git add .
git commit -m "#77"
git push

---------------------------------------------
sync Cologne to github
csl-orig
pwg displays

---------------------------------------------
09-20-2024  Reopened. Further corrections from AB
cp temp_pwg_5.txt temp_pwg_6_work.txt
Ref1: https://github.com/sanskrit-lexicon/PWG/issues/77#issuecomment-2362846857
# manual Emacs edit temp_pwg_6_work.txt
Note: 3 un-needed [Pagev-xxxx] lines preceding <LEND>
 Since these corrections change number of lines, will do them later below
---
39 matches in 35 lines for ">[^<]*>" in buffer: temp_pwg_6_work.txt
Note: compare 36 + 3 in Ref1. above.
---
chg 1. <ls n=">  -> <ls n="  30 occurrences
  Now 9 matches for ">[^<]*>" in buffer
---
3 matches for "^[^<]*>" in buffer
chg 2. Remove the initial '>'
---
chg 3.1
<ls n="VARĀH. BṚH. S. 14,">>  -> <ls n="VARĀH. BṚH. S. 14,">
---
chg 3.2
<ls n="ŚAT. BR.">">12,9,2,4.</ls> -> <ls n="ŚAT. BR.">12,9,2,4.</ls>
---
chg 3.3
<ls>Mél. asiat. >II,172.</ls> -> <ls>Mél. asiat. II,172.</ls>
---
chg 3.4
<is>Vārtt.</is> 14>, -> <is>Vārtt.</is> 14,
---
chg 3.5
<ls>HALL</ls> in der Einl.> zu  -> <ls>HALL</ls> in der Einl. zu
---
chg 3.6
<ls>Spr. 5251</ls> (>Conj.) -> <ls>Spr. 5251</ls> (Conj.)
---
chg 4.
Reduce multiple spaces to a single space
85 matches in 81 lines for "  +" in buffer: temp_pwg_6_work.txt
'  ' -> ' '  85 instances (there are no triple spaces)

--------------------------------------------
# corrections that change number of lines
cp temp_pwg_6_work.txt temp_pwg_6.txt
# manual edit temp_pwg_6.txt
-------------------
From ref1
Remove [Pagev-xxxx] line when followed by <LEND>
3 matches for "[0-9]\]{{LINE_BREAK}}<LEND>" in buffer: temp_pwg_6.txt
-------------------
Ref2: https://github.com/sanskrit-lexicon/PWG/issues/77#issuecomment-2364157515
chg 2.1
This is a VN from volume 5,
which adds a reference to each of the two homonyms of atrijAta
old:
<L>63080<pc>5-0966<k1>atrijAta<k2>atrijAta<h>12
12. {#atrijAta#}¦ vgl.
<ls>Verz. d. Oxf. H. 120,a,23.</ls>
<LEND>
---
AB suggests to break this into two entries.
Jim no objection -- it will get rid of the improper '<h>12'
---
new:
<L>63080<pc>5-0966<k1>atrijAta<k2>atrijAta<h>1
1. {#atrijAta#}¦ vgl. <ls>Verz. d. Oxf. H. 120,a,23.</ls>
<LEND>

<L>63080.1<pc>5-0966<k1>atrijAta<k2>atrijAta<h>2
2. {#atrijAta#}¦ vgl. <ls>Verz. d. Oxf. H. 120,a,23.</ls>
<LEND>

-------------------
Ref2: https://github.com/sanskrit-lexicon/PWG/issues/77#issuecomment-2364157515
chg 2.2
Similarly
<L>79329<pc>5-1624<k1>pradoza<k2>pradoza<h>23  entry split into two

old:
<L>79329<pc>5-1624<k1>pradoza<k2>pradoza<h>23
23. {#pradoza#}¦
<ls>KĀVYĀD. 2,312.</ls>
<LEND>

new:
<L>79329<pc>5-1624<k1>pradoza<k2>pradoza<h>2
2. {#pradoza#}¦ <ls>KĀVYĀD. 2,312.</ls>
<LEND>

<L>79329.1<pc>5-1624<k1>pradoza<k2>pradoza<h>3
3. {#pradoza#}¦ <ls>KĀVYĀD. 2,312.</ls>
<LEND>

--------------------------------------------
# regenerate local displays from temp_pwg_6
# This to check xml validity.

cp temp_pwg_6.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok  No problems noticed
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue77

--------------------------------------------
sync to github

cd /c/xampp/htdocs/cologne/csl-orig
git add .
git commit -m "PWG:
Ref1: https://github.com/sanskrit-lexicon/PWG/issues/77#issuecomment-2362846857
Ref2: https://github.com/sanskrit-lexicon/PWG/issues/77#issuecomment-2364157515"

git push
# 130 insertions(+), 126 deletions(-)
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue77

--------------
sync Cologne to github
csl-orig
pwg displays

--------------------------------------------

--------------------------------------------
THE END
