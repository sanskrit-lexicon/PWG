From vntxt_2.txt, the 11 [Page lines:

[Page:VN1-001][1-1143][https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpng/pwg1-0000--13.png]
[Page:VN1-002][1-1145][https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpng/pwg1-0000--14.png]
[Page:VN1-003][1-1147][https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpng/pwg1-0000--15.png]
[Page:VN2-001][2-1101][https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpng/pwg2-0000--02.png]
[Page:VN2-002][2-1103][https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpng/pwg2-0000--03.png]
[Page:VN3-001][3-1013][https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpng/pwg3-1013--kor.png]
[Page:VN3-002][3-1015][https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpng/pwg3-1015--kor.png]
[Page:VN4-001][4-1217][https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpng/pwg4-1217--kor.png]
[Page:VN4-002][4-1219][https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpng/pwg4-1219--korabk.png]
[Page:VN5-001][5-1677][https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpng/pwg5-1677--mokSay.png]
[Page:VN6-001][6-1511][https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpng/pwg6-1511--kor.png]

========================================================================================
Manually open each old png (in browser) and save Image As to a (local) folder: pwgvn/png/

done [Page:VN1-001][1-1143][https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpng/pwg1-0000--13.png]
done [Page:VN1-002][1-1145][https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpng/pwg1-0000--14.png]
done [Page:VN1-003][1-1147][https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpng/pwg1-0000--15.png]
done [Page:VN2-001][2-1101][https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpng/pwg2-0000--02.png]
done [Page:VN2-002][2-1103][https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpng/pwg2-0000--03.png]
done [Page:VN3-001][3-1013][https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpng/pwg3-1013--kor.png]
done [Page:VN3-002][3-1015][https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpng/pwg3-1015--kor.png]
done [Page:VN4-001][4-1217][https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpng/pwg4-1217--kor.png]
done [Page:VN4-002][4-1219][https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpng/pwg4-1219--korabk.png]
done [Page:VN5-001][5-1677][https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpng/pwg5-1677--mokSay.png]
done [Page:VN6-001][6-1511][https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpng/pwg6-1511--kor.png]
========================================================================================

I first tried to onvert each of the png files to a pdf file using pillow
This worked, but the resulting pdf file is 10X bigger than the png file.
THis is because pillow requires first conversion of image to RGB.
CONCLUDE: False trail!

# create a virtual environment
# using gitbash
cd to pwgvn
python -m venv venv

# activate
source venv/Scripts/activate
# when done
deactivate

-------------------------------
# With venv activated:
# Install pillow for png to pdf conversion
pip install pillow

------------------
# png_to_pdf.py uses pillow  to convert one file (per Copilot example)

python png_to_pdf.py png/pwg1-0000--13.png pdf/pwg1-0000--13.pdf
file size as almost 2MB!  Too big.
========================================================================================

Convert using Adobe Acrobat 9
For each file in png,
* Open with Adobe acrobat
* Ctrl-S (Save)  to file in pdf

The pdf file sizes are comparable to png file sizes.
Good!

========================================================================================
head -n 5 /c/xampp/htdocs/cologne/csl-websanlexicon/v02/distinctfiles/pwg/web/webtc/pdffiles.txt
1-0001:pwg1-0001.pdf:a
1-0003:pwg1-0003.pdf:a
1-0005:pwg1-0005.pdf:aMSuka
1-0007:pwg1-0007.pdf:aMhasaspati
1-0009:pwg1-0009.pdf:akARqa

Rename the pdfs
mkdir pdfrename

mv pdf/pwg1-0000--13.pdf       pdfrename/pwg1-1143.pdf
mv pdf/pwg1-0000--14.pdf       pdfrename/pwg1-1145.pdf
mv pdf/pwg1-0000--15.pdf       pdfrename/pwg1-1147.pdf
mv pdf/pwg2-0000--02.pdf       pdfrename/pwg2-1101.pdf
mv pdf/pwg2-0000--03.pdf       pdfrename/pwg2-1103.pdf
mv pdf/pwg3-1013--kor.pdf      pdfrename/pwg3-1013.pdf
mv pdf/pwg3-1015--kor.pdf      pdfrename/pwg3-1015.pdf
mv pdf/pwg4-1217--kor.pdf      pdfrename/pwg4-1217.pdf
mv pdf/pwg4-1219--korabk.pdf   pdfrename/pwg4-1219.pdf
mv pdf/pwg5-1677--mokSay.pdf   pdfrename/pwg5-1677.pdf  # exists
mv pdf/pwg6-1511--kor.pdf      pdfrename/pwg6-1511.pdf

example:
https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpdf/pwg1-0005.pdf
========================================================================================
# revise pdffiles.txt
# 
cp /c/xampp/htdocs/cologne/csl-websanlexicon/v02/distinctfiles/pwg/web/webtc/pdffiles.txt .

pwg5-1677.pdf  # exists 5-1677:pwg5-1677.pdf:mokzay-VN

1-1143:pwg1-1143.pdf:VN
1-1145:pwg1-1145.pdf:VN
1-1147:pwg1-1147.pdf:VN
2-1101:pwg2-1101.pdf:VN
2-1103:pwg2-1103.pdf:VN
3-1013:pwg3-1013.pdf:VN
3-1015:pwg3-1015.pdf:VN
4-1217:pwg4-1217.pdf:VN
4-1219:pwg4-1219.pdf:VN
6-1511:pwg6-1511.pdf:VN

change  5-1677:pwg5-1677.pdf:mokzay to  5-1677:pwg5-1677.pdf:mokzay-VN in pdffiles.txt
Note:
sort lines and
save a copy as pdffiles-sorted.txt
insert the 11 lines above into pdffiles-sorted.txt
resort all lines
  Note keeping (for now) two copies of pwg5-1677.pdf.



---------------------------------
# sync csl-websanlexicon to Github
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue76/pwgvn

cp pdffiles-sorted.txt /c/xampp/htdocs/cologne/csl-websanlexicon/v02/distinctfiles/pwg/web/webtc/pdffiles.txt

cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
git add . # pdffiles.txt
git commit -m "Revise pdffiles for VN pages.
Ref: https://github.com/sanskrit-lexicon/PWG/issues/76"

git push

-------------------------------------------------------------------------------------------------------------
# revise cologne server

----------------------------------
1. upload all (10) files in pdfrenames to cologne server (
e.g. upload  pdfrenames/pwg1-1143.pdf to
https://sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpdf/pwg1-1143.pdf

Note: skip uploading pwg5-1677.pdf, as PWGScan/PWGScanpdf/pwg5-1677.pdf exists.
----------------------------------
2. sync csl-websanlexicon
3. csl-pywork: remake pwg displays (this will incorporate new pdffiles.txt).


