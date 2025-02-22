issue84/readme.txt
02-20-2025 begun ejf
ŚAT. BR.	The ŚATAPATHABRĀHMAṆA

------------------------------------------------------
https://en.wikipedia.org/wiki/Shatapatha_Brahmana

The Shatapatha Brahmana (Sanskrit: शतपथब्राह्मणम्, lit. 'Brāhmaṇa of one hundred paths', IAST: Śatapatha Brāhmaṇam, abbreviated to 'SB')[1] is a commentary on the Śukla Yajurveda. It is attributed to the Vedic sage Yajnavalkya. Described as the most complete, systematic, and important of the Brahmanas[2] (commentaries on the Vedas), it contains detailed explanations of Vedic sacrificial rituals, symbolism, and mythology.

Kanda and Adhyâya
'Kanda' (or 'Khanda', Sanskrit खंड), means 'chapter', 'division of a book', or more loosely 'book'. It also means 'praise' and 'water'.[6]
'Adhyâya' (Sanskrit अध्याय), means 'chapter' (of a book), 'lesson', 'reading' and 'lecture'.[7]
In relation to the Shatapatha Brahmana, a reference such as '14.1.2' means 'Kanda 14, Adhyaya 1, Brahmana 2', or in English, 'Book 14, Chapter 1, Explanation 2'. The addition of a fourth digit at the end (e.g. 17.7.3.11) refers to the verse number.
---------------------------------------------------------
Ref: https://github.com/sanskrit-lexicon/PWG/issues/84

This issue84 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue84

-------

----------------------------------
shatapathabr.pdf  1235 pages

https://www.digitale-sammlungen.de/en/view/bsb10219752?q=%28Catapatha+Brahmana%29&page=6,7

https://rightsstatements.org/page/NoC-NC/1.0/

/e/pdfwork/shatbra/shatapathabr.pdf

----------------------------------
SAT.index.txt 
SAT.Index.xlsx prepared by @AnnaRybakovaT
https://github.com/sanskrit-lexicon/PWG/issues/84#issuecomment-2664012441
SAT.index.tsv converted to tsv form using Google docs
SAT.index.txt renamed


index format:
page	prap.	adhy.	brāhm.	from kaṇḍ.	to kaṇḍ.	ipage

288	3	4	4	26b	27	267
288	3	5	1	1	10a	267

7 tab-separated fields

page 22 - 1130
prap. 1 - 14  प्रपाठ prapAWaka
adhy.  
brāhm. ब्राह्मणम्
from kaṇḍ.  कण्डिका A short section, shortest subdivision; (as in the śuklayajurveda).
to kaṇḍ.
ipage  internal page number

PWG references have 4 parameters
 <ls>ŚAT. BR. prap,adhy,brahm,kand


-----------------------
make_js_index.py makes index into a javascript module.
It does several validity checks.
This program will be part of the 'app1' in the sanskrit-lexicon-scans
repo for this link source.
aa
------
# apply the program to the index 
cp SAT.index.txt SAT.index_edit.txt
manual cahnges to SAT.index_edit.txt
----
# Global change in SAT.index_edit.txt:
 '<TAB>1a<TAB>1a<TAB>' -> '<TAB>1<TAB>1a<TAB>'
 31 lines changed

python make_js_index.py SAT.index_edit.txt index.js

=====================================================================

# get temporary local copy of pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt

   
# generate 10 examples for manual checking. write file temp.txt
python generate_random.py 10 temp_pwg.txt SAT.index_edit.txt temp_check.txt
1333 Page records read from SAT.index_edit.txt
generate_pagerec_keys: 8547 keys
1132566 lines read from temp_pwg.txt
123366 entries found
found 4406 distinct verse keys in kosha
10 examples found
10 written to temp_check.txt


# make readme file for the checks
cp temp_check.txt readme_checkindex.txt
# manually check the examples -  edit readme_checkindex.txt
#  use the pdf in checking: shatapathabr.pdf
# Results of check:
  All ok with index.

Note: errors found in pwg and pw. See evaMvIrya in readme_checkindex.txt

----------------------------
In course of the check, two pwg.txt typos noticed:
  L=76434 "Danda" (धन्द॒) -> Danada धनद  typo 
  L=76435  Dandeva -> Danadeva
  (Ref: https://github.com/sanskrit-lexicon/csl-orig/issues/1775)

install the corrections Danda, Dandeva into csl-orig
cp temp_pwg_0.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt

cd /c/xampp/htdocs/cologne/csl-orig
git pull
git add v02/pwg/pwg.txt
git commit -m "PWG Danda, Dandeva. #1775"
git push

Also update csl-orig and pwg displays at Cologne

# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue84

----------------------------
check index for volume 2
Indische_Spr_v2_Index.txt
  Ref: https://github.com/sanskrit-lexicon/PWG/issues/84#issuecomment-2659012762

The format of lines is space-separated values
Manually edit and change to tab-separated values
global regex replacement lines: "  +" -> \t

# make index_2.js
python make_js_index.py II Indische_Spr_v2_Index.txt  index_2.js

322 Success: Page records read from Indische_Spr_v2_Index.txt
json data written to index_2.js

# get temp copy of pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt

# generate 10 examples for manual checking of v2 index. write file temp.txt
python generate_random.py 10 temp_pwg.txt II Indische_Spr_v2_Index.txt temp_check_2.txt

# make readme file for the checks
cp temp_check_2.txt readme_checkindex_vol2.txt
# manually check the examples -  edit readme_checkindex_vol2.txt
#  use the volume 2 pdf in checking
# Results of check:
  All ok with index.

rm temp_pwg.txt

----------------------------
