issue62 readme1.txt
06-24-2025
Further work

diff /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg1.txt | wc -l
0  # so temp_pwg1.txt is current as of this time.
# make another file which we will change
cp temp_pwg1.txt temp_pwg2.txt
------------------------------
# make 6 changes
per https://github.com/sanskrit-lexicon/PWG/issues/62#issuecomment-3001259201

---
35888 : dvihIna : <ls n="AK.">2,5,37. 3,6,3,22.</ls> : <ls n="AK.">2,5,37.</ls> <ls n="AK.">3,6,3,22.</ls>
---
15758 : kalpana : <ls n="AK.">2. 7,52.</ls> : <ls n="AK.">2,7,52.</ls>
---
108106 : sAti : <ls n="AK.">3,3,39. 3,4,14,70.</ls> : <ls n="AK.">3,3,39.</ls> <ls n="AK.">3,4,14,70.</ls>
---
55731 : Bedya : <ls n="AK.">3,4,19,134. 25,190.</ls> : <ls n="AK.">3,4,19,134.</ls> <ls n="AK. 3,4,">25,190.</ls>
NOTE: 3,4,19,134  uncovers next-page problem with index (see below)
---
15207 : karin : <ls n="AK.">4. 3,4,14,78. 28,219. 1,1,2,6.</ls> : <ls n="AK. 2,8,2,">4.</ls> <ls n="AK.">3,4,14,78.</ls> <ls n="AK. 3,4,">28,219.</ls> <ls n="AK.">1,1,2,6.</ls>
---
15038 : kambala : <ls n="AK.">8,2,22. 3,4,26,196</ls> : <ls n="AK. 2,">8,2,22.</ls> <ls n="AK.">3,4,26,196</ls>

---------------
# install temp_pwg2
cp temp_pwg2.txt   /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
# remake displays for pwg
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg

# generate change_pwg1_pwg2.txt
python diff_to_changes_dict.py temp_pwg1.txt temp_pwg2.txt change_pwg1_pwg2.txt

# sync csl-orig to github

-------------------------------------
next-page problem with index
cp index.txt index_v2.txt

# revise make_js_index.py to identify next-page problems. 8 found.
# revise index.txt re these next-page problem
# remake index.js
python make_js_index.py index.txt index.js

---------------------
# update amara_dlc app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/amara_dlc
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue62/index.txt app1/pywork/
cd app1/pywork
python make_js_index.py index.txt index.js
# copy index.js to app1 
cp index.js ../
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue62/make_js_index.py app1/pywork/

# sync local amara_dlc to github

# return home
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue62 

