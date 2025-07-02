issue155
06-30-2025
mapping between dlc index and col index.

https://github.com/sanskrit-lexicon/pwg/issues/155

cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue155

----------------------------------------
cp ../issue62/index.txt index_dlc.txt
cp ../issue62/make_js_index.py make_js_index_dlc.py
cp ../issue154/index.txt index_col.txt
cp ../issue154/make_js_index.py make_js_index_col.py


AK.concordance-2.txt

----------------------------------------
# modify the make files to take one extra parm for the 'bcs' file
python  make_js_index_dlc.py index_dlc.txt index_dlc.js bcs_dlc.txt
71 records written to bcs_dlc.txt

python  make_js_index_col.py index_col.txt index_col.js bcs_col.txt
67 records written to bcs_col.txt

---------------------------
construct map between dlc and col for [3,4,s,v] for
python cmp_bcs0.py bcs_dlc.txt bcs_col.txt cmp_bcs0.txt dlc_col.js
 
# lots of checking material.

71 lines read from bcs_dlc.txt
71 from bcs_dlc.txt
67 lines read from bcs_col.txt
67 from bcs_col.txt
1511 verses for dlc
1511 verses for col
dlc has 0 duplicate keys
col has 0 duplicate keys
key (3, 4, 29) unique to dlc
key (3, 4, 30) unique to dlc
key (3, 4, 31) unique to dlc
key (3, 4, 32) unique to dlc
dlc 2 (3, 4, 2, 19, 20) intersect (3, 4, 3, 20, 27)
dlc 8 (3, 4, 8, 35, 36) intersect (3, 4, 9, 36, 42)
dlc 9 (3, 4, 9, 36, 42) intersect (3, 4, 10, 42, 44)
dlc 10 (3, 4, 10, 42, 44) intersect (3, 4, 11, 44, 46)
dlc 14 (3, 4, 14, 60, 88) intersect (3, 4, 15, 88, 90)
dlc 16 (3, 4, 16, 91, 97) intersect (3, 4, 17, 97, 101)
dlc 18 (3, 4, 18, 102, 131) intersect (3, 4, 19, 131, 134)
dlc 20 (3, 4, 20, 135, 135) intersect (3, 4, 21, 135, 136)
dlc 22 (3, 4, 22, 137, 140) intersect (3, 4, 23, 140, 147)
dlc 23 (3, 4, 23, 140, 147) intersect (3, 4, 24, 147, 163)
dlc 24 (3, 4, 24, 147, 163) intersect (3, 4, 25, 163, 194)
dlc 28 (3, 4, 28, 216, 220) intersect (3, 4, 29, 220, 224)
12 non-disjoint sets in dlc
dlc 3 (3, 6, 3, 22, 32) intersect (3, 6, 4, 32, 36)
dlc 7 (3, 6, 7, 42, 42) intersect (3, 6, 8, 42, 47)
2 non-disjoint sets in dlc
col 2 (3, 4, 2, 19, 20) intersect (3, 4, 3, 20, 27)
col 4 (3, 4, 4, 28, 29) intersect (3, 4, 5, 29, 30)
col 8 (3, 4, 8, 35, 36) intersect (3, 4, 9, 36, 42)
col 9 (3, 4, 9, 36, 42) intersect (3, 4, 10, 42, 46)
col 12 (3, 4, 12, 60, 88) intersect (3, 4, 13, 88, 90)
col 14 (3, 4, 14, 91, 98) intersect (3, 4, 15, 98, 107)
col 15 (3, 4, 15, 98, 107) intersect (3, 4, 16, 107, 131)
col 16 (3, 4, 16, 107, 131) intersect (3, 4, 17, 131, 134)
col 18 (3, 4, 18, 135, 135) intersect (3, 4, 19, 135, 147)
col 19 (3, 4, 19, 135, 147) intersect (3, 4, 20, 147, 163)
col 20 (3, 4, 20, 147, 163) intersect (3, 4, 21, 163, 194)
col 24 (3, 4, 24, 216, 220) intersect (3, 4, 25, 220, 227)
12 non-disjoint sets in col
col 3 (3, 6, 3, 22, 32) intersect (3, 6, 4, 32, 36)
col 7 (3, 6, 7, 42, 42) intersect (3, 6, 8, 42, 47)
2 non-disjoint sets in col
write_map sends 261 lines to dlc_col.js


 cp dlc_col.js /c/xampp/htdocs/sanskrit-lexicon-scans/amara_dlc/app1/dlc_col.js
 cp dlc_col.js /c/xampp/htdocs/sanskrit-lexicon-scans/amara_col/app1/dlc_col.js
