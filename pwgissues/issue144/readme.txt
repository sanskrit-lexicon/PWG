issue144/readme.txt
04-28-2025 begun ejf
TAITTIRĪYABRĀHMAṆA

Ref: https://github.com/sanskrit-lexicon/PWG/issues/144

This issue144 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue144

-----------------
pdf: in 3 parts:
taittiriyabr_1.pdf  637  pages
taittiriyabr_2.pdf  689  pages  only table of contens and commentary. no verses
taittiriyabr_3.pdf  1057 pages


---------------------------------------
Taittiriya.Brahmana.Index.xlsx

  Ref: https://github.com/sanskrit-lexicon/PWG/issues/144
  index_orig.txt  convert xslx to text file, tab-separators (Google sheets)

872 lines
9 fields per line
Vol	page	kaṇḍa	prapāṭhaka	anuvāka	versefrom	versto	intpage	Comments
I	8	1	1	1	1	2	1	
I	9	1	1	1	3	5	2	
I	10	1	1	2	1	4a	3	

---------------------------------------
index.txt some edits of index_orig.txt
 # remove lines which contain '==' :  These not needed for app1
 # drop the last (9th) parameter (comment)
 # line 45, empty 'vol' -> 'I'
 # line 635: 1c -> 1b
 # line 342: prapath 3 -> 5 
 So now 8 parameters per line in index.txt
 
python make_index.py index_orig.txt  index.txt
9 lines dropped
864 cases written to index.txt

-------------------------------------------
# construct index.js, and check for internal consistencies
python make_js_index.py index.txt index.js
863 Page records read from index.txt
json data written to index.js
pagerecs passes check1_key
pagerecs passes check1_hierarchy

----------------------------------------
# get temporary local copy of dictionaries for checking
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt

----------------------------------------
# preliminary check of temp_pwg.txt and index and pdf

see check_pwg_man.txt
These all passed.

ready for repo !
repo sanskrit-lexicon-scans/taittiriyabr constructed

-----------------------------------
app construction. see readme_app.txt
2 apps are needed: 

app1 -- (kaṇḍa, prapāṭhaka, anuvāka, verse)
app0 -- (external page)

---------------------------------------
Change to basicadjust to activate links.
see readme_websanlexicon.txt

---------------------------------------
Random checks between dictionary and the pdf and index
 for dictionaries pwg, pw, pkwvn, sch, mw.
 see readme_checks.txt

check_mw.txt has one case classified as NOT FOUND.

=============================================================
sync to github:  csl-websanlexicon, csl-apidev
sync to Cologne, and redo the 5 dictionaries.

-------------------------------------------------------------

THE END

