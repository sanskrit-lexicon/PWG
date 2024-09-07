
manusmfti as link target.
This local directory:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue73

All files are in some arbitrarily chosen subfolder on local machine.
For purposes of this documentation, I will use HOME as the path to this
subfolder.

**************************************************************
PDF acquisition
**************************************************************
09-06-2024
manu.pdf download from link provided by Andhrabharati
https://download.digitale-sammlungen.de/BOOKS/download.pl?id=bsb10251095
Lois de Manou
Loiseleur Deslongchamps
Paris
1830
----------------------------------------------------------
<s>mAnavaM DarmmaSAstram</s>
<s>BfguproktA saMhitA</s>

**************************************************************
Extraction as individual pages
**************************************************************

--------------------------------------------------
Extract pages with Adobe Acrobat

open manu.pdf with Adobe Acrobat
 Acrobat: Document/Extract pages
  pages 1-621
  Extract Pages As Separate files
  extract into HOME/manupages
  file names: 'manu 1.pdf' ...
              'manu 621.pdf


**************************************************************
pdfpages 
**************************************************************

mkdir HOME/pdfpages

pdfpages to contain all the 1-page pdfs , with renaming.
The renaming convention:
So 'manu 1.pdf' is copied and renamed to pdfpages/001.pdf
etc

This work is done as follows:
-----------------------------
1. generate bash scripts to do the renaming and copying
# python make_renum_pages.py INDIR OUTDIR SCRIPT

python make_renum_pages.py manupages pdfpages renum_1.sh
621 files in manupages
621 lines written to renum_1.sh

2. Run the script
sh renum_1.sh
3.  check counts
ls pdfpages/*.pdf | wc -l
621
As expected

**************************************************************
New Github repo:
**************************************************************
https://github.com/sanskrit-lexicon-scans/manu
This is created in the normal way new repositories are made at Github.
1. Public repositoryy
2. Add a README file
3. No .gitignore (may add this manually later)
4. Choose a license: None


In addition, the manu repo is used to 'host' a simple html/javascript app:
Build this github site:
https://github.com/sanskrit-lexicon-scans/manu/settings/pages
1. Deploy from a branch
2. Branch: main, /(root)
   Click save
"Your GitHub pages site is currently being built from the main branch"
 Note: This takes several minutes

Web link to manu: 
https://sanskrit-lexicon-scans.github.io/manu/index.html?3,42

Once manu repo is constructed at Github, we clone it on local machine:
cd /c/xampp/htdocs/sanskrit-lexicon-scans
git clone git@github.com:sanskrit-lexicon-scans/manu.git

/c/xampp/htdocs/sanskrit-lexicon/manu is the local copy of repo.

----------------------------
# provide a .gitignore file in manu
  copy from kss
# edit manu/README.md
# put the pdfpages into manu
cp -r HOME/pdfpages /c/xampp/htdocs/sanskrit-lexicon-scans/manu/

# push revised manu to github
cd /c/xampp/htdocs/sanskrit-lexicon-scans/manu/
git add .
git commit -m "Initialize pdfpages"
git push  # this takes several minutes to upload all the pdfpages


**************************************************************
Indexing pdfpages Preliminary Discussion
**************************************************************
Manu.Deslongchamps.index.txt provided by Andhrabharati

  Ref: https://github.com/sanskrit-lexicon/PWG/issues/73#issuecomment-2334523075
  
We aim to make a simple application in manu to serve as a link target.

There are 12 sections.
 Ref: https://sanskrit-lexicon-scans.github.io/manu/pdfpages/019.pdf


Each section contains a sequence of shlokas.
Example: in PWG:
(under headword 'a')
<ls>BṚH. ĀR. UP. 4, 3, 22.</ls> {#abrAhmaRa#} {%ein Nicht-Brahmane%} 
<ls>CHĀND. UP. 4, 4, 5.</ls> 
<ls>M. 7, 85.</ls>


AB's index: 149	7	80	88
 so this should be on internal page 149
 Using manu.pdf, we find this is external page 170
 So the link target should be
 https://sanskrit-lexicon-scans.github.io/manu/pdfpages/170.pdf
 And on this page, under shloka ८५ (85) we do indeed find सममब्राह्मनॉ

 Thus we need a map from 7,85 to 170.

The internal page number (ipage) and external pdf page number (epage)
1. epage = ipage + 21
2. ipage=1,2 are blank
3. ipage=3 first shloka of first section, epage=24
4. last ipage = 310, epage = 331
5. ipages 331-560 Notes by Deslongchamps
6. ipages 561-567 Corrections


**************************************************************
 indexing map creation: manudata.js
**************************************************************
-------------------------------------
Such a map might be created in various ways.
Here is how I did it for volume 1.
manudata.js
The anticipated application will use javascript to implement the map.
It was thought better
  to generate a javascript module that contains the mapping as the value of
  a javascript object.
  'c' in next means 'chapter': 1-12
  's' means shloka number within chapter
  
  : var manudata1 = {'c,s':'page',...} for all verses
  
A python program can generate manudata.js from AB's index:

python make_manudata.py Manu.Deslongchamps.index.txt manudata.js

311 read from Manu.Deslongchamps.index.txt
skip line with page=page
skip line with page=1
skip line with page=2
308 records  from AB index file
308 records from Manu.Deslongchamps.index.txt
2686 lines written to manudata.js

manudata.js is obviously a bigger file (39KB),
but the performance at current internet bandwidth seems acceptable.
=====================================================

**************************************************************
construct application in manu repo
**************************************************************
This is developed in local /c/xampp/htdocs/sanskrit-lexicon-scans/manu/
We copy manudata.js to manu as part of this development

Then pushed to Github repo https://sanskrit-lexicon-scans.github.io/manu/

The web link for a particular taranga/shloka is
https://sanskrit-lexicon-scans.github.io/manu/index.html?taranga,shloka

This finishes the current work on the manu repo.

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

**************************************************************
Other dictionaries

PWG ls abbreviation is KATHĀS.
  All displays revised and functioning
----
PW
ls abbrev = KATHĀS.
links available in csl-apidev displays (simple-search)
BLAM displays need to be regenerated, locally and at cologne.

Regenerate local displays for pw
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
ok

----
PWKVN
ls abbrev = KATHĀS.
links available in csl-apidev displays (simple-search)
BLAM displays need to be regenerated, locally and at cologne.

Regenerate local displays for pwkvn
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwkvn  ../../pwkvn
sh xmlchk_xampp.sh pwkvn
ok

-------------------------------------------------
SCH
ls abbrev = Kathās. (note lower case)
 The link parameters are not within scope of ls.
 Example: <ls>Kathās.</ls> 27, 92.
changes required:
- basicadjust.php  recognize Kathās.
- sch.txt modified : <ls>Kathās.</ls> 27, 92. -> <ls>Kathās. 27, 92.</ls>
- csl-apidev: revise basicadjust
BLAM displays need to be regenerated, locally and at cologne.

147 matches in 144 lines for "<ls>Kathās.</ls>" in buffer: sch.txt
127 matches in 126 lines for "<ls>Kathās.</ls> [0-9]+, [0-9]+\." in buffer: sch.txt
 The 20 different are similiar - can be revised manually.

Global change (Emacs) TO /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt
<ls>Kathās.</ls> \([0-9]+, [0-9]+\.\) → <ls>Kathās. \1</ls>
 The other 20 modified individually
<ls n="Kathās.">

---
in csl-pywork/v02:


---
in csl-websanlexicon:
Change basicadjust.php to recognize "Kathās." (lower case letters)
Generate href for sch.

---
Regenerate local displays for sch
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh sch  ../../sch
sh xmlchk_xampp.sh sch
ok

-----
sync repos to github
 csl-orig
 csl-websanlexicon
 csl-apidev

----
------------------------------------------------
MW
ls abbrev = Kathās. (note lower case)
 taranga parameter given in lower-case roman numerals, e.g.
 <ls>Kathās. lxx, 33.</ls>
 <ls>Kathās. 57, 136</ls>   ! sometimes digits
  Also 
 Thus, changes to basicadjust required.

----
lxx,232  70,232 not found  
838 matches in 837 lines for "<ls>Kathās. " in buffer: mw.txt

830 matches in 829 lines for "<ls>Kathās. [ivxlc]" in buffer: mw.txt
8 matches for "<ls>Kathās. [1-9]" in buffer: mw.txt
---
change to basicadjust.php in csl-websanlexicon:
  So local displays generate links for Kathās..
---
regenerate local display for mw
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
ok

---
# copy basicadjust to csl-apidev
cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
sh apidev_copy.sh

---
# sync repos to Github
csl-websanlexicon, csl-apidev
------------------------------------------------
update repos on cologne server
csl-orig
csl-websanlexicon
csl-apidev
----------
regenerate displays on cologne server for:
pwg, pw, pwkvn, sch, mw

Work completed 07-28-2024
****************************************************************
