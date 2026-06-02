
alignv1c/readme.txt
05-31-2026 begin

local directory:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue180/alignv1c

work to align cdsl with ab. (re <ab>, <lex>, and other similar tags)
start with 
cdsl: basevn/temp_pwg_0b_base1.txt  
  AB: temp_ab_files/'pwg_(AB)_v1b.txt'

* compare_meta.txt  identify headword sequence differences
python compare_meta.py ../basevn/temp_pwg_0b_base1.txt ../temp_ab_files/'pwg_(AB)_v1b.txt' compare_meta.txt
598773 lines read from ../basevn/temp_pwg_0b_base1.txt
591087 lines read from ../temp_ab_files/pwg_(AB)_v1b.txt
122738 entries
98868 metalines are identical, 23870 differ

One k1 error in AB:
<L>51234<pc>4-1178<k1>prEpa<k2>prEpa/ ->
<L>51234<pc>4-1178<k1>prEza<k2>prEza/

--------------------------------------------
* temp_pwg_0c_base1.txt
cp ../basevn/temp_pwg_0b_base1.txt temp_pwg_0c_base1.txt
Manual changes
--- change 1
merge L=83442 into 83441
--- change 2
split L=107295 into two entries 107295, 107295.1
  Note: Strange:  the body is same, except for hom
   Result is slightly different from print
--- change 3
L=88385   headword spelling typo
vargIyi -> vargIya
--- change 4
L=100652  headword spelling typo
SUrya -> SUrpa
-------------------------------
* ../temp_ab_files/pwg_(AB)_v1c.txt
 Ref: https://github.com/sanskrit-lexicon/PWG/issues/180#issuecomment-4590915786
python ../count_meta.py
../temp_ab_files/pwg_(AB)_v1c.txt 591087 lines, 122738 metalines
--------------------------------------
* CDSL and AB versions have equal sequences of  (L,k1)
python compare_meta.py temp_pwg_0c_base1.txt ../temp_ab_files/'pwg_(AB)_v1c.txt' temp_compare_meta_0c.txt
598773 lines read from temp_pwg_0c_base1.txt
591087 lines read from ../temp_ab_files/pwg_(AB)_v1c.txt
122738 entries
122738 entries
# metas1 = 122738
# metas2 = 122738
122721 metalines are identical, 17 differ
122738 metalines with same L-k1, 0 with different L-k1
490952 lines written to temp_compare_meta_0c.txt

------------------------------------
* Why different number of lines?  4467
compare # lines per entry 

python compare_lines.py temp_pwg_0c_base1.txt ../temp_ab_files/'pwg_(AB)_v1c.txt' compare_lines_0c.txt
598773 lines read from temp_pwg_0c_base1.txt
591087 lines read from ../temp_ab_files/pwg_(AB)_v1c.txt
122738 entries in both files
4467 lines written to compare_lines_0c.txt

(/ 4467.0 122738.) 3.6%

* temp_pwg_0d_base1.txt:  <F>  4451
cp temp_pwg_0c_base1.txt temp_pwg_0d_base1.txt
0c has 38 <F>;  v1c has 47
Change 0d so also 47.

python compare_lines.py temp_pwg_0d_base1.txt ../temp_ab_files/'pwg_(AB)_v1c.txt' compare_lines_0d.txt
598788 lines read from temp_pwg_0d_base1.txt
591087 lines read from ../temp_ab_files/pwg_(AB)_v1c.txt
122738 entries in both files
4451 lines written to compare_lines_0d.txt

* div alignment is too difficult to handle now.
* AB: compare 51685 87082.1
