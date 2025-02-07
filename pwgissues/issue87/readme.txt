issue87/readme.txt
02-05-2025 begun ejf
Indische Sprüche 1st ed. link target

Ref: https://github.com/sanskrit-lexicon/PWG/issues/87

https://github.com/sanskrit-lexicon/PWG/issues/87#issue-2820409982
link to 3 pdfs  (volumes 1-3).

Indische_Spr_v1_Index.txt
  Ref: https://github.com/sanskrit-lexicon/PWG/issues/87#issuecomment-2628934230

Check Indische_Spr_v1_Index.txt for 10 random verses.
No problems noticed !

See readme_checkindex_vol1.txt for details

Note:  the 'column separator' in v1_Index is [ ]+  (one or more spaces).

-----------------------
02-06-2025
make_js_index.py makes index into a javascript module.
It does several validity checks.
This program will be part of the 'app1' in the sanskrit-lexicon-scans
repo for this link source.

------
# apply the program to the index for volume I
python make_js_index.py I Indische_Spr_v1_Index.txt index_1.js
output:
Skipping column title line: volume      page    from v. to v.   ipage
305 Success: Page records read from Indische_Spr_v1_Index.txt
json data written to temp.txt
check1 finds 0 errors
