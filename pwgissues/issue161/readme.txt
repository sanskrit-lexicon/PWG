
PWG better cdsl images
https://github.com/sanskrit-lexicon/PWG/issues/161

# this directory
cd /e/pdfwork/pwgimages

# orig directory
contains the downloads provided by @Andhrabharati
PWG-1.pdf
PWG-2.pdf
PWG-3.pdf
PWG-4.pdf
PWG-5.pdf
PWG-6.pdf
PWG-7.pdf


# orig1 directory
copy orig files with renaming
mkdir orig1

cp orig/'PWG-1.pdf' orig1/pwg1.pdf
cp orig/'PWG-2.pdf' orig1/pwg2.pdf
cp orig/'PWG-3.pdf' orig1/pwg3.pdf
cp orig/'PWG-4.pdf' orig1/pwg4.pdf
cp orig/'PWG-5.pdf' orig1/pwg5.pdf
cp orig/'PWG-6.pdf' orig1/pwg6.pdf
cp orig/'PWG-7.pdf' orig1/pwg7.pdf

# extracts directory
Use Adobe Acrobat9 to extract individual pages from the orig1 pdfs.
file names
'pwg1 1.pdf' ... 'pwg1 575.pdf'   
'pwg2 1.pdf' ... 'pwg2 552.pdf'
'pwg3 1.pdf' ... 'pwg3 508.pdf'
'pwg4 1.pdf' ... 'pwg4 610.pdf'

'pwg5 1.pdf' ... 'pwg5 839.pdf'

'pwg6 1.pdf' ... 'pwg6 755.pdf'
'pwg7 1.pdf' ... 'pwg7 911.pdf'

(+ 575 552 508 610 839 755 911) = 4750 (number of files in extracts folder)

=================================================================
# pdffiles_orig.txt
copied from
cp /c/xampp/htdocs/cologne/csl-websanlexicon/v02/distinctfiles/pwg/web/webtc/pdffiles.txt pdffiles_orig.txt

# sample lines:
1-0001:pwg1-0001.pdf:a
1-0003:pwg1-0003.pdf:a
1-0005:pwg1-0005.pdf:aMSuka

pdffiles_orig.txt has 4747 lines  (3 less than number of extracts)

In pdffiles_orig.txt
pwg1 574 lines  575 extracts  * 1 more extract   extract 'pwg1 572.pdf' is blank
pwg2 552 lines  552
pwg3 508 lines  508
pwg4 609 lines  610 extracts  * 1 more extract  'pwg4 608.pdf' is blank
pwg5 839 lines  839 
pwg6 754 lines  755 extracts  * 1 more extract  'pwg6 754.pdf' is blank
pwg7 911 liens  911


# pdffiles.txt  (NOTE NO CHANGES REQUIRED !)
copy from pdffiles_orig.txt
- remove lines not starting with 1-7  (23 lines starting with 't')
  This leaves 2127 lines.  Exactly matching the number of files in extracts!
- change .png to .pdf  # since extracts are pdf files
- change N.pdf to .pdf # The N indicates Nachtrage pages. No need to distinguish
  - 205 lines changed.

# relation between pdffiles_orig.txt and the extracts
# exploration to understand what is needed
1-0001:pwg1-0001.pdf:a  == pwg1 1.pdf
1-0003:pwg1-0003.pdf:a  == pwg1 2.pdf
1-0005:pwg1-0005.pdf:aMSuka == pwg1 3.pdf
...
M = f(N) = 2*(N - 1) + 1     Emacs:  (+ (* 2 (- N 1)) 1)
pwg1-M.pdf == pwg1 N.pdf ==   M = f(N) for N = 1,2,...,571
check:  M (in pdffiles) is Always odd.
'pwg1 572.pdf' is blank

N = g(M) = ( (M - 1) / 2 ) + 1  
 N = 572  skip
 N = 573, ..., 575  M = f(N-1) == 1143, 


 pwg1 573.pdf == 1-1143:pwg1-1143.pdf:VN
   N = 573, M = 1143 = f(N-1)  
 
  ...
  

 last pwg1-M in pdffiles is 1-1147:pwg1-1147.pdf:VN
  M = 1147  ->  N = (+ (/ (- 1147 1) 2) 1) == 574


# pdfpages directory
mkdir pdfpages

Construct make_renum.py which generates a bash script for each volume.
This script copies from extracts to pdfpages for the volume, also
 renaming the files to be compatible with pdffiles.txt,
 skipping the 3 blank pages mentioned above
Then, run the script for each volume.

--------------------------------
python make_renum.py 1 renum1.sh
skipping n = 572
574 lines written to renum1.sh
sh renum1.sh
--------------------------------
python make_renum.py 2 renum2.sh
552 lines written to renum2.sh
sh renum2.sh
--------------------------------
python make_renum.py 3 renum3.sh
508 lines written to renum3.sh
sh renum3.sh
--------------------------------
python make_renum.py 4 renum4.sh
skipping n = 608
sh renum4.sh
--------------------------------
python make_renum.py 5 renum5.sh
839 lines written to renum5.sh
sh renum5.sh
--------------------------------
python make_renum.py 6 renum6.sh
skipping n = 754
754 lines written to renum6.sh
sh renum6.sh
--------------------------------
python make_renum.py 7 renum7.sh
911 lines written to renum7.sh
sh renum7.sh

--------------------------------
check number of files:
ls pdfpages | wc -l
4747

$ wc -l pdffiles_orig.txt
4747 pdffiles_orig.txt

Now we have the new pdfpages directory with all 4747 images.
#
----------------------------------------
cd /c/xampp/htdocs/cologne/scans
git clone git@github.com:sanskrit-lexicon-scans/pwg.git
cd /c/xampp/htdocs/cologne/scans/pwg
mv pdfpages pdfpages_v1  # retain the old images
# check the number of old images
ls pdfpages_v1 | wc -l
4747
# same number. Good!

---------------
# compare sizes, just out of curiosity
cd /c/xampp/htdocs/cologne/scans/pwg
du -sh pdfpages
1.7G    pdfpages
du -sh pdfpages_v1
1.5G    pdfpages_v1

----------
# copy the new images to this scans/pwg folder
cd /c/xampp/htdocs/cologne/scans/pwg
cp -r /e/pdfwork/pwgimages/pdfpages .

----------------------------------------------
On local system, check the pwg displays.
  (local system uses /c/xampp/htdocs/cologne/scans/pwg/pdfpages if available)
  Use pdffiles.txt to get headwords in various volumes, use local display
  and check that the right page of new pdfpages is linked.

----------------------------------------------
cd /c/xampp/htdocs/cologne/scans/pwg
revise /c/xampp/htdocs/cologne/scans/pwg/README.md

----------------------------------------------
sync to github
cd /c/xampp/htdocs/cologne/scans/pwg

git add .
git commit -m "move old images pdfpages_v1, new images in pdfpages
Ref: https://github.com/sanskrit-lexicon/PWG/issues/161"

date; git push; date
date; git push; date
Sat Nov 15 16:20:27 EST 2025
Enumerating objects: 6693, done.
Counting objects: 100% (6693/6693), done.
Delta compression using up to 16 threads
Compressing objects: 100% (4751/4751), done.
Writing objects: 100% (4751/4751), 1.52 GiB | 1.20 MiB/s, done.
Total 4751 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:sanskrit-lexicon-scans/pwg.git
   8f124fd..c04bb2a  gh-pages -> gh-pages
Sat Nov 15 16:42:33 EST 2025



--------------------------------

Installation on cologne server

cd to scans directory

clone sanskrit-lexicon-scans/pwg repo in a temporary directory
cd PWGScan
mkdir tempdir
cd tempdir
git clone git@github.com:sanskrit-lexicon-scans/pwg.git

--------------------
cd to scans/PWGSCan

mv PWGScanpdf PWGScanpdf_v1
-------------------
cd to scans/PWGScan
mv tempdir/pwg/pdfpages PWGScanpdf
------------------
# check the Cologne server displays are using the new images for pwg
------------------
# remove tempdir
cd to scans/PWGScan

rm -rf tempdir

=======================================================
cd  /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues
mkdir issue161

cp /e/pdfwork/pwgimages/readme.txt issue161/readme.txt

git add .
git commit -m "Clear images for pwg. #161"
git push

---------------------------
THE END
--------------------------
Additional changes.
1. replacements/readme.txt for 55 page replacements of volume 6 images.
2. issue161/vol6changes/readme.txt  for 5 additional page changes.
