
ref: https://github.com/sanskrit-lexicon/PWG/issues/161#issuecomment-3557459786

Two independent changes
------------------------------------------
First change: image file names inconsistent
with internap page numbering in volume 6
file            ipage
pwg6-0975.pdf   975, 976  ok
pwg6-0977.pdf   977, 978  ok
pwg6-0979.pdf   983, 984  WRONG x
pwg6-0981.pdf   985, 986  WRONG x
pwg6-0983.pdf   979, 980  WRONG
pwg6-0985.pdf   981, 982  WRONG
pwg6-0987.pdf   987, 988  ok


Those 4 WRONG files need renaming
In local machine, make changes
cd /c/xampp/htdocs/cologne/scans/pwg
mkdir tempdir
mv pdfpages/pwg6-0979.pdf tempdir/pwg6-0983.pdf
mv pdfpages/pwg6-0981.pdf tempdir/pwg6-0985.pdf
mv pdfpages/pwg6-0983.pdf tempdir/pwg6-0979.pdf
mv pdfpages/pwg6-0985.pdf tempdir/pwg6-0981.pdf
# now, cp the tempdir files back into pdfpages
cp tempdir/* pdfpages/

-------------------------------------------
Second change:  replace a bad image
AB replacement file: Vol.6.009-010.pdf
# 
cd /c/xampp/htdocs/cologne/scans/pwg
# remove bad file from pdfpages
mv pdfpages/pwg6-0009.pdf temp_pwg6-0009.pdf
# replace with Vol.6.009-010.pdf 
cp ~/Downloads/Vol.6.009-010.pdf pdfpages/pwg6-0009.pdf

# for convenience with Cologne installation (below),
# copy the replacement page into tempdir
cp pdfpages/pwg6-0009.pdf tempdir/
--------------------------------------------
local installation changes finished.

--------------------------------------------
# push 'pwg' to Github sanskrit-lexicon-scans repo
cd /c/xampp/htdocs/cologne/scans/pwg
git add .
git commit -m "vol6  change 5 image files
Ref: https://github.com/sanskrit-lexicon/PWG/issues/161#issuecomment-3557459786"
git push

--------------------------------------------
# Connect to cologne server are copy the
# tempdir files
cd scans/PWGScan
Drag the tempdir files to scans/PWGScan/PWGScanpdf/
(this will overwrite 5 files)
Check the pwg displays for
(1) vikaNkata  (page 6-0980, file pwg6-0979.pdf
  https://www.sanskrit-lexicon.uni-koeln.de/scans/csl-apidev/servepdf.php?dict=pwg&page=6-0980
(2) yaj  pwg6-0009.pdf
  https://www.sanskrit-lexicon.uni-koeln.de/scans/csl-apidev/servepdf.php?dict=pwg&page=6-0009

Looks good!
Cologne now updated.

-----------------------------------------
