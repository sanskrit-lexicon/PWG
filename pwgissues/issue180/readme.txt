
05-24-2026 begun ejf

enhance PWG markup for common abbreviations, continuation of issue178

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issues/180


this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue180

* pwg history in csl-orig
cd /c/xampp/htdocs/cologne/csl-orig/

git log --follow --pretty=format:"%ad %h %an %s" --date=short -- v02/pwg/pwg.txt > temp_history_pwg.txt


git log --follow --pretty=format:"%ad %h %an %s" --date=short -- app/correction_response/cfr.tsv > temp_history_cfr.tsv

-------------------------------------
* temp_pwg_0.txt
# get temporary local copy of cdsl kosha (at csl-orig commit 81701182)
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt
This version created in issue178

* Andhrabharati provides 5 files:
python count_meta.py TEXTFILE prints the number of lines and metalines in text file TEXTFILE
---
temp.sh:
cd temp_ab_files
for f in pwg*.txt; do
    python ../count_meta.py "$f"
done
---
pwg_(AB)_v1a.txt           591087 lines, 122738 metalines
pwg_(AB)_v1b.txt           591087 lines, 122738 metalines
pwg_(AB)_v1c.txt           591087 lines, 122738 metalines
pwg_(CDSL)_v8.1_VN_1-6.txt   2511 lines,    628 metalines
pwg_(CDSL)_v8.1_base.txt   598725 lines, 122738 metalines
pwg_(CDSL)_v8.2_base.txt   598725 lines, 122738 metalines

(+ 122738 628)  123366  

* pwg_base.txt and pwg_vn.txt
In temp_ab_files. 
Andhrabharati Constructed from (copy of) temp_pwg_0.txt
pwg_base.txt 598773 lines, 122738 metalines
pwg_vn.txt     2511 lines, 628 metalines
* pwg_base_a.txt 
constructed by jim.
See basevn/readme.txt 

* temp_pwg_0a.txt and temp_pwg_0b.txt
See basevn/readme.txt for construction from temp_pwg_0.txt
python count_meta.py temp_pwg_0.txt
temp_pwg_0.txt  1129105 lines, 123366 metalines
temp_pwg_0a.txt 1128474 lines, 123366 metalines
temp_pwg_0b.txt 1128477 lines, 123366 metalines

* temp_pwg_0b_base1.txt and temp_pwg_0b_vn.txt
in basevn directory. 
Constructed from temp_pwg_0b.txt. See basevn/readme.txt for construction

temp_pwg_0b_base1.txt 598773 lines, 122738 metalines
temp_pwg_0b_vn.txt      2511 lines,    628 metalines

* temp_pwg_0b_base1.txt == pwg_base_a.txt
diff basevn/temp_pwg_0b_base1.txt temp_ab_files/pwg_base_a.txt | wc -l
# 0  files are the same
* redo_pwg.sh
  reconstruction of (copy of) temp_pwg_0b.txt from
  temp_pwg_0b_base1.txt and temp_pwg_0b_vn.txt

OBJECTIVE  temp_pwg_1_base1.txt  
from temp_pwg_0b_base1.txt, construct temp_pwg_1_base1.txt  
 Assume there are no changes to <L> and <LEND> lines.
 Or spaces between entries.
sh redo_pwg.sh BASE VN PWG
constructs PWG from BASE and VN.


Here is example of the script invocation with
BASE =  basevn/temp_pwg_0b_base1.txt
VN   =  basevn/temp_pwg_0b_vn.txt
PWG  =  basevn/temp_pwg_0b_vn.txt

sh redo_pwg.sh basevn/temp_pwg_0b_base1.txt basevn/temp_pwg_0b_vn.txt tempwork_pwg_0b.txt

# the result PWG is = temp_pwg_0b.txt.
diff temp_pwg_0b.txt tempwork_pwg_0b.txt  | wc -l
0
# no need for 
# remove 2 intermediate files
rm  tempredo_base.txt tempredo_lend.txt
Aim to constuct temp_pwg_1_base.txt

* v8 refers to csl-orig commit ecd11db
Ref: https://github.com/sanskrit-lexicon/PWG/issues/180#issuecomment-4570605102

* alignv1c directory: alignv1c/temp_pwg_0d_base1.txt
mkdir alignv1c
work to align cdsl with ab. (re <ab>, <lex>, and other similar tags)
start with 
cdsl: basevn/temp_pwg_0b_base1.txt  
  AB: temp_ab_files/'pwg_(AB)_v1c.txt'

Final form here is
alignv1c/temp_pwg_0d_base1.txt
This is aligned with pwg_(AB)_v1c.txt regarding
 - metaline sequences (L,k1)
 - <F> footnote divs.

Unresolved are 4451 <div  in 0d which are not in v1c.
Abandon work to resolve the div differences.
This div-difference resolution is not needed. 
* alignab directory: alignab/temp_pwg_0n_base1.txt
  Alignment of <ab.*?</ab>
  See alignab/readme.txt

* temp_pwg_1.txt 
# merge alignab/temp_pwg_0n_base1.txt and basevn/temp_pwg_0b_vn.txt
# basevn/div_split.py  split base lines at LBC 
# basevn_join.py joins the split base lines and the VN lines

sh redo_pwg.sh alignab/temp_pwg_0n_base1.txt basevn/temp_pwg_0b_vn.txt temp_pwg_1.txt
Restore line breaks from alignab/temp_pwg_0n_base1.txt. Result is tempredo_base.txt
join temp_redo_base.txt and basevn/temp_pwg_0b_vn.txt. Result is tempredo_lend.txt
122738 base entries
   628 vn entries

(+ 122738 628) = 123366
temp_pwg_1.txt constucted
* misc analyses ??
python alignv1c/compare_meta.py temp_pwg_0.txt temp_pwg_1.txt temp_compare_meta_0_1.txt
(+ 99452 23914) 123366
99452 metalines with same L-k1, 23914 with different L-k1

python alignv1c/compare_meta.py temp_pwg_0.txt temp_pwg_0a.txt temp_compare_meta_0_0a.txt
123366 metalines with same L-k1, 0 with different L-k1

python alignv1c/compare_meta.py temp_pwg_0a.txt temp_pwg_0b.txt temp_compare_meta_0a_0b.txt
123366 metalines with same L-k1, 0 with different L-k1

-- compare metalines of base.  Version c corrects a metaline
python alignv1c/compare_meta.py basevn/temp_pwg_0b_base1.txt alignv1c/temp_pwg_0c_base1.txt compare_meta_base_0b_0c.txt
122738 entries
98882 metalines with same L-k1, 23856 with different L-k1
for details of metaline change, see diff_base_0b_0c.txt
diff basevn/temp_pwg_0b_base1.txt alignv1c/temp_pwg_0c_base1.txt > diff_base_0b_0c.txt

0c_base1 has same metalines as 0d,..., 0n.

python alignv1c/compare_meta.py alignv1c/temp_pwg_0c_base1.txt alignv1c/temp_pwg_0c_base1.txt compare_meta_base_0c_0d.txt
122738 metalines with same L-k1, 0 with different L-k1

python alignv1c/compare_meta.py alignv1c/temp_pwg_0d_base1.txt alignab/temp_pwg_0n_base1.txt compare_meta_base_0d_0n.txt
122738 metalines with same L-k1, 0 with different L-k1

python alignv1c/compare_meta.py 


* check xml validity of temp_pwg_1
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue180
cp temp_pwg_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
cd /c/xampp/htdocs/cologne/csl-orig/
git restore v02/pwg/pwg.txt
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue180
# OK !!

* revise one.dtd in csl-pywork
  Allow <s> to be child of <ls>

* INSTALLATION
* sync to github:
------------------
# csl-orig temp_pwg_1
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue180/
cp temp_pwg_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt 
cd /c/xampp/htdocs/cologne/csl-orig/
git add .
git commit -m "PWG abbreviations
Ref: https://github.com/sanskrit-lexicon/pwg/issues/180 temp_pwg_1"
#  1 file changed, 7899 insertions(+), 8853 deletions(-)
git push
# remote: warning: File v02/pwg/pwg.txt is 50.88 MB; 
# this is larger than GitHub's recommended maximum file size of 50.00 MB

-------------------
# csl-pywork  one.dtd
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue180/
cd /c/xampp/htdocs/cologne/csl-pywork/
git add .
git commit -m "one.dtd Allow 's' to be child of 'ls'. 6 instances in pwg
Ref: https://github.com/sanskrit-lexicon/pwg/issues/180 "
git push

cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue180/

---------------------------------------------------
* sync to Cologne, pull changed repos, redo display
---------------
csl-orig #pull
#  v02/pwg/pwg.txt | 16752 lines changed

csl-pywork # pull
---------------
# update displays for pwg
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/

-----------------------------------------------------
* sync issue180/ to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue180/
git pull
git add .
git commit -m "issue180 PWG abbreviations. #180"
git push

------------------------------------------------------------
************************************************************
* temp_ab_pwg_v1e.txt  
# 
python basevn/basevn_join.py alignab/temp_ab_pwg_v1d.txt basevn/temp_pwg_0b_vn.txt temp_ab_pwg_v1e.txt
# same sequence of L,k1
python alignv1c/compare_meta.py temp_pwg_1.txt temp_ab_pwg_v1e.txt  temp.txt
# 123366 metalines with same L-k1, 0 with different L-k1

* compare global abbrevs
python count_ab.py temp_pwg_1.txt temp_count_ab_pwg_1.txt

python count_ab.py temp_ab_pwg_v1e.txt temp_count_ab_v1e.txt

python abdiff.py temp_count_ab_pwg_1.txt temp_count_ab_v1e.txt abdiff_1_v1e.txt
Only differences are as expected, for 'd.' and 'u.'
d.	28	1	27
u.	2347	1996	351

* compare local abbrevs
python count_ab_local.py temp_pwg_1.txt temp_ablocal_1.txt
169 lines written to temp_ablocal_1.txt
426 = total number of <ab>X</ab>

python count_ab_local.py temp_pwg_1.txt temp_ablocal_1.txt

python count_ab_local.py temp_ab_pwg_v1e.txt temp_ablocal_v1e.txt

python abdiff.py temp_ablocal_1.txt temp_ablocal_v1e.txt abdiff_local_1_v1e.txt

The only differences are relative to d. and u.
<ab n="das">d.</ab>	-1	1	-1
<ab n="dem">d.</ab>	85	97	-12
<ab n="der">d.</ab>	2	9	-7
<ab n="des">d.</ab>	-1	1	-1
<ab n="die">d.</ab>	-1	6	-6
<ab n="und">u.</ab>	5	352	-347
<ab n="unten">u.</ab>	-1	4	-4

---- 
* THE END
