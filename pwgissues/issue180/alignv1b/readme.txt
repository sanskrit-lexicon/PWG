
alignv1b/readme.txt
05-31-2026 begin

local directory:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue180/alignv1b

work to align cdsl with ab. (re <ab>, <lex>, and other similar tags)
start with 
cdsl: basevn/temp_pwg_0b_base1.txt  
  AB: temp_ab_files/'pwg_(AB)_v1b.txt'

python compare_meta.py ../basevn/temp_pwg_0b_base1.txt ../temp_ab_files/'pwg_(AB)_v1b.txt' compare_meta.txt
598773 lines read from ../basevn/temp_pwg_0b_base1.txt
591087 lines read from ../temp_ab_files/pwg_(AB)_v1b.txt
122738 entries
98868 metalines are identical, 23870 differ

One k1 error in AB:
<L>51234<pc>4-1178<k1>prEpa<k2>prEpa/ ->
<L>51234<pc>4-1178<k1>prEza<k2>prEza/

