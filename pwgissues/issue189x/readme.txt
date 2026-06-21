
06-16-2026 begin ejf

# PWG 'is' tag markup using Andhrabharati-based version v1e.

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issues/189x

# this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue189x

* Andhrabharati version of pwg.txt
# local copy . See #180 for a zip of this
../issue180/temp_ab_pwg_v1e.txt


-------------------------------------
* temp_pwg_0.txt

cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git log | head -n 1
# commit c10d4c8ed
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue189x

# get temporary local copy of cdsl kosha 
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt

* count_is_v1e.txt
python count_is.py ../issue180/temp_ab_pwg_v1e.txt count_is_v1e.txt

6507 lines written to count_is_v1e.txt
53617 = total number of <is>X</is>



* count_is_0.txt
python count_is.py temp_pwg_0.txt count_is_0.txt

7473 lines written to count_is_0.txt
53961 = total number of <is>X</is>

* abdiff_0_v1e
python abdiff.py count_is_0.txt count_is_v1e.txt abdiff_0_v1e.txt

* temp_pwg_1.txt  
systematic differences 
python change_0_1.py temp_pwg_0.txt temp_pwg_1.txt

9737 line(s) changed

* count_is_1.txt
python count_is.py temp_pwg_1.txt count_is_1.txt

6609 lines written to count_is_1.txt
53961 = total number of <is>X</is>

* abdiff_1_v1e
python abdiff.py count_is_1.txt count_is_v1e.txt abdiff_1_v1e.txt
6609 read from count_is_1.txt
6507 read from count_is_v1e.txt
6826 total distinct abbreviations
6826 lines written to abdiff_1_v1e.txt


* compare_is.py. change_1_2.py temp_pwg_2.txt
# iteratively construct change_1_2.py to construct temp_pwg_2.txt
# so that the sequence of <is>X</is> for temp_pwg_2.txt
# agrees with the sequence in v1e.
# NOTE:  this does not count local-abbreviation differences.

python change_1_2.py temp_pwg_1.txt temp_pwg_2.txt
# 479 lines changed
python compare_is.py temp_pwg_2.txt ../issue180/temp_ab_pwg_v1e.txt compare_is.txt

# 0 lines written to compare_is.txt

* compare_is.py. change_2_3.py temp_pwg_3.txt
For efficiency, continue the resolution using change_2_3.py
# iteratively construct change_2_3.py to construct temp_pwg_3.txt

python change_2_3.py temp_pwg_2.txt temp_pwg_3.txt
# 232 lines changed
python compare_is.py temp_pwg_3.txt ../issue180/temp_ab_pwg_v1e.txt compare_is.txt

* compare_is.py. change_3_4.py temp_pwg_4.txt
For efficiency, continue the resolution using change_3_4.py
# iteratively construct change_3_4.py to construct temp_pwg_4.txt

python change_3_4.py temp_pwg_3.txt temp_pwg_4.txt
# 
python compare_is.py temp_pwg_4.txt ../issue180/temp_ab_pwg_v1e.txt compare_is.txt

sh check_xml.sh 4

* compare_is.py. change_4_5.py temp_pwg_5.txt
For efficiency, continue the resolution using change_4_5.py
# iteratively construct change_4_5.py to construct temp_pwg_5.txt

python change_4_5.py temp_pwg_4.txt temp_pwg_5.txt
# 
python compare_is.py temp_pwg_5.txt ../issue180/temp_ab_pwg_v1e.txt compare_is.txt

sh check_xml.sh 5
# ok

* compare_is.py. change_5_6.py temp_pwg_6.txt
For efficiency, continue the resolution using change_5_6.py
# iteratively construct change_5_6.py to construct temp_pwg_6.txt

python change_5_6.py temp_pwg_5.txt temp_pwg_6.txt
# 
python compare_is.py temp_pwg_6.txt ../issue180/temp_ab_pwg_v1e.txt compare_is.txt
#0 lines written to compare_is.txt

sh check_xml.sh 6
# ok


* compare1_is.py. change_6_7.py temp_pwg_7.txt

python change_6_7_prep.py  temp_pwg_6.txt ../issue180/temp_ab_pwg_v1e.txt change_6_7_prep.txt

# 57 lines written to change_6_7_prep.txt
# Format of change_6_7_prep.txt: 3 tab-delimited fields per line:
#  lnum (in temp_pwg_6.txt),  temp_pwg_6 tag, v1e tag

# use change_6_7_prep.txt to construct change_6_7.py and temp_pwg_7.txt

python change_6_7.py change_6_7_prep.txt temp_pwg_6.txt temp_pwg_7.txt
1128151 lines read from temp_pwg_6.txt
57 lines read from change_6_7_prep.txt
54 lines changed by adjust_lines0
0 line(s) changed by adjust_lines1
1128151 lines written to temp_pwg_7.txt

Now the sequence of <is.*?</is> should be same for temp_pwg_7.txt and v1e

sh check_xml.sh 7
# ok

* dump_is.py  
python dump_is.py temp_pwg_7.txt dump_is_7.txt
53617 lines written to dump_is_7.txt

# generate for v1e 
python dump_is.py ../issue180/temp_ab_pwg_v1e.txt temp_dump_is_v1e.txt
53617 lines written to temp_dump_is_v1e.txt

# compare the two dump files
diff dump_is_7.txt temp_dump_is_v1e.txt | wc -l
# 0  

The sequence of <is.*?</is>  is same for version 7 and version v1e.

* count1_is_7.txt
python count1_is.py temp_pwg_7.txt count1_is_7.txt

6753 lines written to count1_is_7.txt
53617 = total number of <is(.*?)>(.*?)</is>


* check_xml.sh
sh check_xml.sh N   (use temp_pwg_N.txt)
* TODO count_is_2.txt
python count_is.py temp_pwg_2.txt count_is_2.txt
* TODO abdiff_2_v1e.txt
python abdiff.py count_is_2.txt count_is_v1e.txt abdiff_2_v1e.txt

Counts agree for all is abbreviations, as expected.

* check xml validity of temp_pwg_2
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue189x
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
cd /c/xampp/htdocs/cologne/csl-orig/
git restore v02/pwg/pwg.txt
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue189x
# OK !!

49 lines written to count_is_2.txt
998 = total number of <is>X</is>

* sync to github:
------------------
# csl-orig temp_pwg_2
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue189x/
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt 
cd /c/xampp/htdocs/cologne/csl-orig/
git add .
git commit -m "PWG is abbreviations
Ref: https://github.com/sanskrit-lexicon/pwg/issues/189x temp_pwg_2"
#  1 file changed, 418 insertions(+), 418 deletions(-)
git push
# remote: warning: File v02/pwg/pwg.txt is 50.88 MB; 
# this is larger than GitHub's recommended maximum file size of 50.00 MB

