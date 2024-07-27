
katha sarit sagara as link target.
This local directory:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue70

All files are in some arbitrarily chosen subfolder on local machine.
For purposes of this documentation, I will use HOME as the path to this
subfolder.

**************************************************************
PDF acquisition
**************************************************************
Andhrabharati provided a clue to find pdfs of two publications by
Hermann Brockhaus:

https://github.com/sanskrit-lexicon/PWG/issues/51#issuecomment-1041429823
Just look for "katha sarit sagara Brockhaus" in Google books; two books with years 1839 (vol.1) and 1862 (vol.2: 1862 & vol.3: 1866) can be downloaded from there.

-------------------------------
volume 1 1839
07-23-2024 Google books 
HOME/Katha_sarit_sagara_1839.pdf local name of pdf downloaded from this link:

 https://www.google.com/books/edition/Katha_sarit_sagara/nWtpAAAAcAAJ?hl=en&gbpv=1&dq=katha+sarit+sagara+Brockhaus&printsec=frontcover

Scanned pages of excellent quality

-------------------------------
volume 2 1862 (poor quality)

HOME/Katha_sarit_sagara_1862.pdf local name of pdf downloaded from this link:

 https://www.google.com/books/edition/Katha_sarit_sagara/1UgBAAAAMAAJ?hl=en&gbpv=1&dq=katha+sarit+sagara+Brockhaus&printsec=frontcover

 internal page 9 ff.  many bad pages.
 This one not used!

-------------------------------
volume 2 1862 This is the one used

HOME/Katha_sarit_sagara_1862_better.pdf local name of pdf downloaded from
  this link:

https://www.google.com/books/edition/Kath%C4%81_Sarit_S%C4%81gara/kjtNAAAAcAAJ?hl=en&gbpv=1&dq=brockhaus+katha+sarit+sagara&printsec=frontcover

Good quality images!
The text here is in an IAST form, rather than Devanagari.

**************************************************************
Extraction as individual pages
**************************************************************

--------------------------------------------------
Extract pages with Adobe Acrobat

Katha_sarit_sagara_1839.pdf
 Acrobat: DOcument/Extract pages
  pages 1-655
  Extract Pages As Separate files
  extract into HOME/vol1 sub-directory
  file names: 'Katha_sarit_sagara_1839 1.pdf' ...
              'Katha_sarit_sagara_1839 655.pdf


Kathā_Sarit_Sāgara_1862_better.pdf

 Acrobat: DOcument/Extract pages
  pages 1-898
  Extract Pages As Separate files
  extract into HOME/vol2 sub-directory
  file names: 'Katha_sarit_sagara_1862_better 1.pdf' ...
              'Katha_sarit_sagara_1862_better 898.pdf'

**************************************************************
pdfpages 
**************************************************************
mkdir HOME/pdfpages

pdfpages to contain all the 1-page pdfs in vol1 and vol2, with
renaming.
The renaming convention chosen is Vppp.pdf (V = 1 or 2, ppp 0-filled)
So vol1/'Katha_sarit_sagara_1839 1.pdf' is copied to pdfpages/1001.pdf
 etc.
and similarly
  vol1/'Katha_sarit_sagara_1862_better 1.pdf' is copied to pdfpages/2001.pdf

This work is done as follows:
-----------------------------
1. generate bash scripts to do the renaming and copying
# python make_renum_pages.py INDIR OUTDIR SCRIPT

python make_renum_pages.py vol1 pdfpages renum_1.sh

python make_renum_pages.py vol2 pdfpages renum_2.sh

2. Run the two scripts
sh renum_1.sh
sh renum_2.sh

3.  check counts
ls pdfpages/*.pdf | wc -l
1553

 ls ../vol1/*.pdf | wc -l
655

 ls ../vol2/*.pdf | wc -l
898

(+ 655 898) = 1553  As expected

**************************************************************
New Github repo: https://github.com/sanskrit-lexicon-scans/kss
This is created in the normal way new repositories are made at Github.
It includes a README.md.

In addition, the kss repo is used to 'host' a simple html/javascript app:
https://github.com/sanskrit-lexicon-scans/kss/settings/pages
  Deployed from main branch.

Web link to kss:
https://sanskrit-lexicon-scans.github.io/kss/index.html?3,42

Once kss repo is constructed at Github, we clone it on local machine:
cd /c/xampp/htdocs/sanskrit-lexicon
git clone git@github.com:sanskrit-lexicon-scans/kss.git

/c/xampp/htdocs/sanskrit-lexicon/kss is the local copy of repo.

----------------------------
# provide a .gitignore file in kss
# put the pdfpages into kss
cp -r HOME/pdfpages /c/xampp/htdocs/sanskrit-lexicon-scans/kss/

# push revised kss to github
cd /c/xampp/htdocs/sanskrit-lexicon/kss/
git add .
git commit -m "Initialize pdfpages"
git push


**************************************************************
Indexing pdfpages Volume 1: kssdata1.js
**************************************************************
We aim to make a simple application in kss to serve as a link target.

For PWG dictionary displays, from  `<ls>KATHĀS. 19, 99.</ls>` refers
to taranga 19, shloka 99.
we must construct the name of the pdf file in pdfpages that contains the
text of this shloka.  The name of the pdf file is 1315.pdf
In our repo, this is
https://sanskrit-lexicon-scans.github.io/kss/pdfpages/1315.pdf

Thus we need a map from 19,99 to 1315.

-------------------------------------
Such a map might be created in various ways.
Here is how I did it for volume 1.

shloka map for volume 1
---
begin_map_1_input.txt
constructed manually from Katha_sarit_sagara_1839.pdf
This contains the page numbers for the start of each taranga. 
The tarangas are grouped in 'Books', and these are also mentioned .
The second half of this pdf contains Brockhaus translation, which are
ignored in the map.

---
begin_map_1a.txt

A program fills provides a form for the intervening pages:
python begin_map.py begin_map_1_input.txt begin_map_1_output.txt
32 read from begin_map_1_input.txt
465 lines written to begin_map_1_output.txt

cp begin_map_1_output.txt begin_map_1a.txt

# manual edit  begin_map_1a.txt to provide first shloka on each page,
  While viewing Katha_sarit_sagara_1839.pdf.
  This is the most labor-intensive step.

  When finished, begin_map_1a.txt has for each page the first taranga,shloka
  Also, for the last page for a given taranga, we provide also the last shloka

----
begin_map_1b.txt
# add last shloka on each page. This can be done by a program.
python begin_mapa.py begin_map_1a.txt begin_map_1b.txt

begin_map_1b.txt has information needed to map from a 'taranga and shloka'
to a page.
e.g., given t=2 and s = 57 we search to get
 this line  '37 2,49-58' , so the shloka occurs on pdf page 37

----
kssdata1.js
The anticipated application will use javascript to implement the ts-page map.
While the association from ts='2,57' to page=1037 could be done based on
  '37 2,49-58',  the logic would be complicated.  It was thought better
  to generate a javascript module that contains the mapping as the value of
  a javascript object. 
  : var kssdata1 = {'t,s':'page',...} for all verses
A python program can generate kssdata1.js

python make_kssdata.py 1 begin_map_1b.txt kssdata1.js
465 read from begin_map_1b.txt
457 records from begin_map_1b.txt
4213 lines written to kssdata1.js

kssdata1.js is obviously a bigger file, but the performance at current
internet bandwidth seems acceptable.

**************************************************************
Indexing pdfpages Volume 2: kssdata2.js
**************************************************************
This is completely analogous to the construction of kssdata1.js

begin_map_2_input.txt
constructed manually from Katha_sarit_sagara_1862_better.pdf

python begin_map.py begin_map_2_input.txt begin_map_2_output.txt
32 read from begin_map_2_input.txt
465 lines written to begin_map_2_output.txt

cp begin_map_2_output.txt begin_map_2a.txt

# manual edit  begin_map_2a.txt to provide first shloka on each page,
  While viewing Katha_sarit_sagara_1862_better.pdf

python begin_mapa.py begin_map_2a.txt begin_map_2b.txt

python make_kssdata.py 2 begin_map_2b.txt kssdata2.js

919 read from begin_map_2b.txt
898 records from begin_map_2b.txt
17313 lines written to kssdata2.js

**************************************************************
construct application in kss repo
**************************************************************
This is developed in local /c/xampp/htdocs/sanskrit-lexicon-scans/kss/
We copy kssdata1.js and kssdata2.js to kss as part of this development

Then pushed to Github repo https://sanskrit-lexicon-scans.github.io/kss/

The web link for a particular taranga/shloka is
https://sanskrit-lexicon-scans.github.io/kss/index.html?taranga,shloka

This finishes the current work on the kss repo.

**************************************************************
links in cdsl displays - local install
**************************************************************

----
1. modifications to the basicadjust.php program in the
csl-websanlexicon repository.

See this csl-websanlexicon commit:
 https://github.com/sanskrit-lexicon/csl-websanlexicon/commit/44d3e4f64500733c8f4e75e443984ebe0221e297

----
2. Regeneration of the cdsl BLAM local displays for pwg
   To activate the revisions to csl-websanlexicon 
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
python3 ../../xmlvalidate.py ../../pwg/pywork/pwg.xml ../../pwg/pywork/pwg.dtd
ok

3. csl-apidev
copy the changes to basicadjust.php to csl-apidev
cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
sh apidev_copy.sh

4. push repos to github
'add' and 'commit'
a. /c/xampp/htdocs/cologne/csl-websanlexicon
b. /c/xampp/htdocs/cologne/csl-apidev


**************************************************************
cologne updates   
**************************************************************
1. pull csl-websanlexicon
2. pull csl-apidev
3. cd csl-pywork/v02
   remake pwg displays

**************************************************************
End of work as of 7/27/2024
**************************************************************

