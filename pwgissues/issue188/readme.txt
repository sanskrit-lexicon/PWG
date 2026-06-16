
06-16-2026 begin ejf

# PWG lang tag markup using Andhrabharati-based version v1e.

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issues/188


# this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue188

* Andhrabharati version of pwg.txt
# local copy . See #180 for a zip of this
../issue180/temp_ab_pwg_v1e.txt


-------------------------------------
* temp_pwg_0.txt

cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git log | head -n 1
# commit ee7e65d2
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue188

# get temporary local copy of cdsl kosha 
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt

* count_lang_v1e.txt
python count_lang.py ../issue180/temp_ab_pwg_v1e.txt count_lang_v1e.txt

49 lines written to count_lang_v1e.txt
998 = total number of <lang>X</lang>

* temp_pwg_1.txt
python mark_lang.py temp_pwg_0.txt count_lang_v1e.txt temp_pwg_1.txt 

49 lines read from count_lang_v1e.txt
1128151 lines read from temp_pwg_0.txt
425 lines changed
1128151 lines written to temp_pwg_1.txt

* count_lang_1.txt
python count_lang.py temp_pwg_1.txt count_lang_1.txt
1012 = total number of <lang>X</lang>
* check xml validity of temp_pwg_1
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue188
cp temp_pwg_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
cd /c/xampp/htdocs/cologne/csl-orig/
git restore v02/pwg/pwg.txt
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue188
# OK !!

* Resolve differences in count between v1e an temp_pwg_1
v1e       :   998
temp_pwg_1:  1012  <lang>X</lang>

* abdiff_1_v1e.txt
python abdiff.py count_lang_1.txt count_lang_v1e.txt abdiff_1_v1e.txt

9 Abbreviations with differences in lang counts:
deutsche	6	4	2
goth.	6	7	-1
Hindi	21	23	-2
Hindust.	2	1	1
litth.	-1	1	-1
prākr.	1	4	-3
Prākrit	29	9	20
Prākṛt	-1	1	-1
ved.	542	543	-1

* compare_ab and change_1-2 make temp_pwg_2.txt
# iteratively construct change_1_2.py to construct temp_pwg_2.txt
# so that the sequence of <lang>X</lang> for temp_pwg_2.txt
# agree with the sequence in v1e
python change_1_2.py temp_pwg_1.txt temp_pwg_2.txt

python compare_lang.py temp_pwg_2.txt ../issue180/temp_ab_pwg_v1e.txt compare_lang.txt

# 0 lines written to compare_lang.txt

* count_lang_2.txt
python count_lang.py temp_pwg_2.txt count_lang_2.txt
* abdiff_2_v1e.txt
python abdiff.py count_lang_2.txt count_lang_v1e.txt abdiff_2_v1e.txt

Counts agree for all lang abbreviations, as expected.

* check xml validity of temp_pwg_2
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue188
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
cd /c/xampp/htdocs/cologne/csl-orig/
git restore v02/pwg/pwg.txt
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue188
# OK !!

49 lines written to count_lang_2.txt
998 = total number of <lang>X</lang>

* sync to github:
------------------
# csl-orig temp_pwg_2
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue188/
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt 
cd /c/xampp/htdocs/cologne/csl-orig/
git add .
git commit -m "PWG lang abbreviations
Ref: https://github.com/sanskrit-lexicon/pwg/issues/188 temp_pwg_2"
#  1 file changed, 418 insertions(+), 418 deletions(-)
git push
# remote: warning: File v02/pwg/pwg.txt is 50.88 MB; 
# this is larger than GitHub's recommended maximum file size of 50.00 MB

