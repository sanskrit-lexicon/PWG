issue92/byvol/readme.txt
03-00-2025 begun ejf
https://github.com/sanskrit-lexicon/PWG/issues/92#issuecomment-2708358312
 Andhrabharati conjectures that Br.pdf (Kern, 1865) could not have
 been used by PWG in volumes 1-4, since these volumes were published
 before 1865. This readme probes that conjecture
 https://sanskrit-lexicon.uni-koeln.de/scans/csldev/csldoc/build/dictionaries/prefaces/pwgpref.html
 
 Title page of PWG for volumes 1-7, with date of publication
  vol. 1 1855
  vol. 2 1858
  vol. 3 1861
  vol. 4 1865
  vol. 5 1868
  vol. 6 1871
  vol. 7 1875

 
09176 VARĀH. BṚH. S. : VARĀHAMIHIRA'S BṚHATSAM̃HITĀ

Ref: https://github.com/sanskrit-lexicon/PWG/issues/92

This issue92 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue92

-----------------
pdf: Br.pdf
/e/pdfwork/brhatsamhita/Br.pdf

----------------------------------------
Index file: index.txt

python adhy_range.py ../index.txt adhy_range.txt
adhy_range returns 107 2-tuples
For each adhy a, show a-maxv (based on index.txt)
All instances of pwg references a,v where v > a-maxv

---------------------


python ref_adhy.py ../temp_pwg.txt adhy_range.txt ref_adhy.txt

error: ref bad adhya <ls>VARĀH. BṚH. S. 164,18
found 7547 entries matching <ls>VARĀH. BṚH. S. ([0-9]+),([0-9]+)

63 0 adhyAyas pwg references within Kern range of verses
15 1 adhyAyas with 1 out of range
 6 2
 3 3
 0 4
 1 5
 2 6
 3 7
 0 8
 1 9
13 10-99
(+ 63 15 6 3 0 1 2 3 0 1 13) = 107, as it should.

 17 out of range references with <pc>5-7
437 out of range references with <pc>1-4

vol 1
vol 2
vol 3
vol 4
------------------------------------------
ref_byvol  number of references by volume of pwg

python ref_byvol.py ../temp_pwg.txt ref_byvol.txt

Statistict derived from ref_byvol.txt  and ref_adhy.txt
TABLE 1: refs by volume
refs: <ls>VARĀH. BṚH. S. a,v
badav: For a, pwg-v > a-maxv (so can't find reference in Br.pdf)
       #refs  %   #badav  
vol 1    22   0%    0
vol 2   370   4%   72
vol 3   667   8%  142
vol 4   999  13%  223
vol 5  1564  20%    9
vol 6  1882  24%    3
vol 7  2043  27%    5
-----  ----  ------  ---
ALL    7547  96%  454


--------------------------------------------

# Generate a few random instances from pwg for detail checking
# filter by volume (1-7) of pc

EXAMPLE CHECKS of 10 PWG refs vs. Br.pdf (uses index.txt)

# vol = 1
python generate_random_vol.py 1 10 ../temp_pwg.txt ../index.txt check_vol_1.txt
found 17 distinct adhy,verse in kosha vol=1
checked all ok

# vol = 2
python generate_random_vol.py 2 10 ../temp_pwg.txt ../index.txt check_vol_2.txt
found 317 distinct adhy,verse in kosha vol=2
checked: 5 NOT FOUND

# vol = 3
python generate_random_vol.py 3 10 ../temp_pwg.txt ../index.txt check_vol_3.txt
found 546 distinct adhy,verse in kosha vol=3
checked: 2 NOT FOUND (of 8 examples)

# vol = 4
python generate_random_vol.py 4 10 ../temp_pwg.txt ../index.txt check_vol_4.txt
found 784 distinct adhy,verse in kosha vol=4
checked: 6 NOT FOUND (of 8 examples)

# vol = 5
python generate_random_vol.py 5 10 ../temp_pwg.txt ../index.txt check_vol_5.txt
found 1107 distinct adhy,verse in kosha vol=5
checked: 1 NOT FOUND (of 10 examples)

# vol = 6
python generate_random_vol.py 6 10 ../temp_pwg.txt ../index.txt check_vol_6.txt
found 1327 distinct adhy,verse in kosha vol=6
checked: all ok (of 10 examples)

# vol = 7
python generate_random_vol.py 7 10 ../temp_pwg.txt ../index.txt check_vol_7.txt
found 1335 distinct adhy,verse in kosha vol=7
checked: all ok (of 10 examples)

--------------------------
TABLE 2:
Example counts (pwg word not found at adhy,verse in Br.pdf)
Examples exclude 'badav'
  vol  #notfound
vol 1   0
vol 2   5
vol 3   2
vol 4   6
vol 5   1
vol 6   0
vol 7   0












