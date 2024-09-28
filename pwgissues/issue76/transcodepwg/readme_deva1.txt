09-28-2024

compare versions of deva1_slp1.xml

2021 version of deva1_slp1.xml
Ref:https://github.com/sanskrit-lexicon/PWK/blob/master/vn-sch/transcoder/deva1_slp1.xml


Sep 20  2021
/c/xampp/htdocs/sanskrit-lexicon/PWK/vn-sch/transcoder/deva1_slp1.xml

/c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue95/pwtranscode/transcoder/deva1_slp1.xml

Jul 19  2023
https://github.com/sanskrit-lexicon/PWK/blob/master/pwkissues/issue95/pwtranscode/transcoder/deva1_slp1.xml
/c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue95/pwtranscode/transcoder/deva1_slp1.xml

# compare the 2021 and 2023 versions
diff /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue95/pwtranscode/transcoder/deva1_slp1.xml /c/xampp/htdocs/sanskrit-lexicon/PWK/vn-sch/transcoder/deva1_slp1.xml | wc -l
137  lines in the diff file.

diff /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue95/pwtranscode/transcoder/slp1_deva1.xml pwgtranscoder2/slp1_deva1.xml | wc -l
# 0  so slp1_deva1.xml versions are same

diff /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue95/pwtranscode/transcoder/deva1_slp1.xml pwgtranscoder2/deva1_slp1.xml | wc -l
# 61


mkdir pwk2023transcoder
cp /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue95/pwtranscode/transcoder/slp1_deva1.xml pwk2023transcoder/slp1_deva1.xml
cp /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue95/pwtranscode/transcoder/deva1_slp1.xml pwk2023transcoder/deva1_slp1.xml

python pwg_transcode.py pwk2023transcoder deva1 slp1 ../vntxt_0_deva_rev.txt vntxt_1_rev_pwk2023.txt

diff ../vntxt_1_rev.txt vntxt_1_rev_pwk2023.txt | wc -l
# 4

 diff ../vntxt_1_rev.txt vntxt_1_rev_pwk2023.txt
607c607
< <hom>2.</hom> {#var#}  ¦ [6.0706] Z. 3 <ab>v. u.</ab> lies {#dEvya\M#}.
---
> <hom>2.</hom> {#var#}  ¦ [6.0706] Z. 3 <ab>v. u.</ab> lies {#dEvyaM\#}.

note: {#dEvya\M#} is preferred to {#dEvyaM\#}.


diff temppwgdeva1_slp1.xml temppwkdeva1_slp1.xml > temp_diff_deva1_slp1_pwg_pwk.txt

From examining this diff:
1. the current pwg transcoding has these extra rules:
  <e> <s>INIT</s> <in>\u0901\u0951</in> <out>^~</out> </e>
  <e> <s>INIT</s> <in>\u0901\u0952</in> <out>\~</out> </e>
  <e> <s>INIT</s> <in>\u0902\u0951\u0952</in> <out>^\M</out> </e> 
  <e> <s>INIT</s> <in>\u0902\u0952</in> <out>\M</out> </e>
  <e> <s>INIT</s> <in>\u0903\u0951\u0952</in> <out>^\H</out> </e> 
  <e> <s>INIT</s> <in>\u0903\u0952</in> <out>\H</out> </e>
  <e> <s>INIT</s> <in>\u0950</in> <out>o~</out></e>
2. the pwk transcoding has 1 extra rule:
  <e> <s>INIT</s> <in>\u1cf2</in> <out>Z</out> </e>

Action taken:
 add one rule to pwgtranscoder2/deva1_slp1.xml:
 <e> <s>INIT</s> <in>\u1cf2</in> <out>Z</out> </e>
