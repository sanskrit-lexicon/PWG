
pwgimages1/readme.txt
 replace pwg6-0301.pdf ... pwg6-0409.pdf

Ref: https://github.com/sanskrit-lexicon/PWG/issues/161#issuecomment-3540585926

cd /e/pdfwork/pwgimages1


# this directory
cd /e/pdfwork/pwgimages1

# orig directory
mkdir orig
cd orig
Vol.6.301-410.pdf contains replacements provided by @Andhrabharati
cp ~/Downloads/Vol.6.301-410.pdf .

# orig1 directory
# copy and rename the pdf
cd /e/pdfwork/pwgimages1
mkdir orig1
cp orig/Vol.6.301-410.pdf orig1/pwg6.pdf

# extracts directory
cd /e/pdfwork/pwgimages1
mkdir extracts
Use Adobe Acrobat9 to extract individual pages from the orig1 pdf.
file names

'pwg6 1.pdf' ... 'pwg6 55.pdf'

# replacements  directory
mkdir replacements

Construct make_renum.py which generates a bash script.
This script copies from extracts to replacementss for the volume,
also renaming the files to be compatible with pdffiles.txt
Thus

python make_renum.py renum.sh
# 55 lines written to renum.sh
sh renum.sh

Now we have the replacements directory with all 55 new images


# local version of git repo 
cd /c/xampp/htdocs/cologne/scans

# IF NECESSARY, clone the pwg repo
git clone git@github.com:sanskrit-lexicon-scans/pwg.git

# local pwg repo
/c/xampp/htdocs/cologne/scans/pwg
mkdir /c/xampp/htdocs/cologne/scans/pwg/replaced
----------------
# remove_old.sh
cd /c/xampp/htdocs/cologne/scans/pwg/
mv pdfpages/pwg6-0301.pdf replaced/
...
mv pdfpages/pwg6-0409.pdf replaced/
----------------
sh remove_old.sh
# 
# check:
cd /c/xampp/htdocs/cologne/scans/pwg/
ls pdfpages | wc -l
# 4692
ls replaced | wc -l
# 55
(+ 4692 55) 4747  (number of files in pdfpages before removal

# insert_new.sh
# copies replacements/X to  /c/xampp/htdocs/cologne/scans/pwg/pdfpages/X
# example: cp replacements/pwg6-0301.pdf /c/xampp/htdocs/cologne/scans/pwg/pdfpages/

cd /e/pdfwork/pwgimages1
sh insert_new.sh

----------
check local display of pwg (e.g. rAjYI) --
  this shows the new page 6-0329(0330) is as intended.
  
**********************************************
Now, local pwg repo has been altered.
Push to Github
cd /c/xampp/htdocs/cologne/scans/pwg
git add .
git commit -m "replace pdfpages pwg6-0301.pdf ... pwg6-0409.pdf
Ref: https://github.com/sanskrit-lexicon/PWG/issues/161#issuecomment-3540585926"
git push


--------------------------------

Installation on cologne server

# using WINScp drag
copy
 from: /e/pdfwork/pwgimages1/replacements (local computer)
   to: scans/PWGScan/  (Cologne)

# using ssh connection
cd /scans/PWGScan
-- before
ls PWGScanpdf | wc -l
4747
---
# overwrite PWGScanpdf files with replacements
cp replacements/*.pdf PWGScanpdf/

# check Cologne display for pwg (rAjYI)

# all looks as it should.

Remove replacements directory at cologne
rm -r replacements/
DONE WITH COLOGNE SERVER INSTALLATION OF REPLACEMENTS

=======================================================
Put the files in this directory (readme.txt, *.py, *.sh)
 into replacements subdirectory
cd  /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue161

mkdir replacements

cp /e/pdfwork/pwgimages/readme.txt issue161/readme.txt

git add .
git commit -m "replacement images pwg6-0301.pdf ... pwg6-0409.pdf.  #161"
git push

---------------------------
THE END
