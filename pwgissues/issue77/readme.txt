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
THE END
