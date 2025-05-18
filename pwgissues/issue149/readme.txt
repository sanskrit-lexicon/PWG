issue149/readme.txt
05-14-2025 begun ejf

issue94/lsextract_all.txt
01077	MĀLAV.	MĀLAVIKĀGNIMITRA, ed. TULLBERG (GILD. Bi
00010	MĀLAV. ed. Bomb.	 MĀLAVIKĀGNIMITRA, Bombay edition 
00001	MĀLAVIKĀGNIMITRA.	?  

Ref: https://github.com/sanskrit-lexicon/PWG/issues/149

This issue149 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue149

-----------------
pdfs: /e/pdfwork/malavikagni/

----------------------------------------
index prepared by github user OFar0101
cp /e/pdfwork/malavikagni/index_orig.txt .

----------------------------------------
Format observations:
page	anka	vers from	vers to	int page	remarks
16	---	---	---	1	The title page
17	---	---	---	2	
18	0	1	1	3	
19	0	2	3	4	

----------------------------------------
index.txt minor changes
1. Remove 'remarks' field at end
2. discard first two lines (shown above)
3. discard last 4 lines 
90	---	---	---	75	
91	---	---	---	76	
92-109	---	---	---	77-94	Skt. equivalent (Chaya) for Prakrit portions
110-123	---	---	---	95-108	Varietas Scripturae
4. In lines with fromv and to '---',  replace with previous tov
Example:
OLD:
80	5	83	84	65	
81	5	---	---	66	
NEW:
80	5	83	84	65	
81	5	84	84	66	

python make_index.py index_orig.txt index.txt
73 cases written to index.txt

----------------------------------------
# construct index.js, and check for internal consistencies

python make_js_index.py index.txt index.js
72 Success: Page records read from index.txt

Note title line of index.txt does not contribute to index.js

----------------------------------------
 preliminary check of pwg links
 5 Checks succeeded.  See readme_checks.txt

----------------------------------------
'ready for repo' message in https://github.com/sanskrit-lexicon/PWG/issues/149
----------------------------------------
repo ready  malavikagni

app construction.
2 apps needed:  see readme_app.txt
app1 -- (shloka)
app0 -- ipage
app2 -- ipage, linenum
app3 -- anka,shloka  (for MW only)

----------------------------------------
modify basicadjust.php for pwg, pw, pwkvn, sch, mw
see readme_websanlexicon.txt

----------------------------------------
checks of links from dictionaries
see readme_checks.txt  (one NOT FOUND).

sync to github:  csl-websanlexicon, csl-apidev, csl-orig, csl-corrections
pull github to cologne server
regenerate displays for pwg, pw, pwkvn, sch, mw
=============================================================
THE END

