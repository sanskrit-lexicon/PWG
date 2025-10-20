
readme_pdfpages.txt

Construct folder pdfpages, to be used in rajatarcalc repo.

--------------------------------
Work done in local directory
 /e/pdfwork/rajatarcalc

Step 1:
mkdir extract
extract rajatar_calc.pdf to 453 pages
  using Adobe Acrobat/Document/extract pages/
  extract from 1 to 453
  extract pages as separate files
  "rajatar_calc 1.pdf"

Step 2:
mkdir pdfpages 
# cp extract/'rajatar_calc 1.pdf' => pdfpages/rajatarcalc_001.pdf
python renum.py extract pdfpages renum.sh

sh renum.sh

---------------------------------
Save a copy of renum.py here (in issue169 directory)
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue169
cp /e/pdfwork/rajatarcalc/renum.py .

----------------------------------
