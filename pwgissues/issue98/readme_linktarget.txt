02-23-2025
Guide to providing a CDSL link target.
This focuses on link target "YĀJÑAVALKYA'S Gesetzbuch."
We start with PWG dictionary, where literary source references are numerous.

--------------------
Choose a link target.
 In this case, YĀJÑ. YĀJÑAVALKYA'S Gesetzbuch.
 lsextract_all.txt for pwg is useful for choosing a literary source with
 many references.
 https://github.com/sanskrit-lexicon/PWG/blob/master/pwgissues/issue94/lsextract_all.txt

--------------------
Create a PWG issue to track the progress for the link target.
  https://github.com/sanskrit-lexicon/PWG/issues/98

Make a 'working subdirectory in local copy of PWG repo:
  /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue98

--------------------
choose a pdf.
  Andhrabharati and Gasyoun are adept at finding digital pdf editions
  of the works that Boehtlingk used.
  
  https://archive.org/download/yjnavalkyasgese00yjgoog/yjnavalkyasgese00yjgoog.pdf
  Post a link to the pdf in an issue comment:
   https://github.com/sanskrit-lexicon/PWG/issues/98#issuecomment-2670501326
   
--------------------
index the pdf.
  Marcis assigns one of his students/colleagues as the indexer.
  github user @OFar0101
  Provide the indexer with the pdf.
  The indexer generates an index file.
  The index is a file that associates verses with pages in the pdf. 
   The preferred format of the index file is a text file with
      tab-separated values:  index.txt
   An excel file (index.xslx).
   
  User @AnnaRybakovaT is expert at indexing and is a resource
    that the indexer might consult. @Andhrabharati and @funderburkjim
    may also be helpful.

  When finished, the indexer uploads the index file via an issue comment.
  the issue.
    https://github.com/sanskrit-lexicon/PWG/issues/98#issuecomment-2656490381
    
--------------------
Check the index for internal consistency and make a json form of the index.
     The checking work is done locally here:
     /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue98
     make_js_index.py is adapted to the index (e.g. number of parameters)

Check index for consistency with pwg references and with pdf
     generate_random.py  generates 10 random examples from pwg.txt
     These examples are then compared manually
      
  This step done currently by @funderburkjim
  When checks are complete, a 'ready for repo' comment is posted in the issue:
     https://github.com/sanskrit-lexicon/PWG/issues/98#issuecomment-2672418634

  This comment also suggests a repo-name: yajnavalkya
  
--------------------
Initialize a repo at Github in sanskrit-lexicon-scans orgranization:
     https://github.com/sanskrit-lexicon-scans/yajnavalkya
     Some instructions:
        https://github.com/sanskrit-lexicon-scans/linktarget_howto/issues/1
clone the repo to local machine.
     git clone git@github.com:sanskrit-lexicon-scans/linktarget_howto.git

On the local machine
   Add a .gitignore file
     This can be copied from yajnavalkya
   Add a README.md file
     Adapted to the repo. See yajnavalkya for example
   add, commit, push the local repo to Github.

   Configure github hosting for the repo.
       Reference: https://github.com/sanskrit-lexicon-scans/yajnavalkya/issues/5

       https://sanskrit-lexicon-scans.github.io/yajnavalkya now shows README.md
       
   User @grigoriyt1 is the expert on this step.

--------------------
Make pdfpages folder in the repo.
      On the local machine, all the pages of the pdf are extracted
      and renamed in a form such as X_NNN.pdf.
      The renamed 1-page pdfs are put into 'pdfpages' folder of local repo.
      reference: https://github.com/sanskrit-lexicon-scans/yajnavalkya/issues/4

   Add, commit and push the local repo to Github.

   User @grigoriyt1 knows how to do this.
   
--------------------
Make app1 in repo sanskrit-lexicon-scans/yajnavalkya
   Example url: https://sanskrit-lexicon-scans.github.io/yajnavalkya/app1/?1,30

   This step currently done by @funderburkjim/
   Development is on local machine, then pushed to Github when debugged.
   Current development steps:

cd /c/xampp/htdocs/sanskrit-lexicon-scans/yajnavalkya
mkdir app1
mkdir app1/pywork

# get index.txt by copying from the issue:
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue98/yajn_index_v1_edit.txt /c/xampp/htdocs/sanskrit-lexicon-scans/yajnavalkya/app1/pywork/index.txt

# get make_js_index.js by copying from the issue:
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue98/make_js_index.py /c/xampp/htdocs/sanskrit-lexicon-scans/yajnavalkya/app1/pywork/make_js_index.py

# copy index.js to the app1 folder
cp index.js ../index.js  # move up to app1 directory

-----
modify index.html
---
<title>yajnavalkya</title>
---
<div id="title"> 
<span style="font-size:20px;">Yājñavalkya's Gesetzbuch, Adolf Stenzler, 1849</span>

-----
modify info.html
---
<title>yajnavalkya info</title>
---
<div id="title"> 
<span style="font-size:20px;">Yājñavalkya's Gesetzbuch, Adolf Stenzler, 1849</span>

-----
local app url: http://localhost/sanskrit-lexicon-scans/yajnavalkya/app1/?1,1

-----
modify main.js
This is the 'hard' part.
main.js should be read starting at the bottom of the file.

index.js specifies a 'global' javascript variable 'indexdata' to
  an array of javascript objects, one for each line of the index.
main.js then:
1. retrieves the parameters (e.g. ?1,2) from the app url
2. matches those parameters to indexdata, getting current, previous and
   next objects.
3. shows the pdf corresponding to the current object
4. shows links for previous and next pages.

When debugged locally, git add, commit, push the yajnavalkya repo to Github.

This completes the app.


--------------------
Activating links to our app from dictionary references.
   This step currently done by @funderburkjim

We must add code so the displays generates links to our app.

For example, in pwg.txt under pratideya, there is a literary source
    <ls>YĀJÑ. 2,65.</ls>.  The display code should create the link
    https://sanskrit-lexicon-scans.github.io/yajnavalkya/app1/?2,65

This is done by modifying basicadjust.php in csl-websanlexicon repo:
 c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/

When this is done and the local display regenerated, then such links
can be tested to see whether they work properly.

The way basicadjust.php is currently organized, getting the links to
work for dictionary pwg also works for dictionaries pw and pwkvn.
The code is within function ls_callback_pwg_href in basicadjust.php
  pw  <L>351<pc>1-005-a<k1>akzikUwa  <ls>YĀJÑ. 3,96</ls>
  pwkvn <L>7462<pc>5-256-c<k1>dEvika <ls>YĀJÑ. 2,66</ls>

Dictionary sch is similar, but has a different abbreviation for the work;
  It is governed by code in function ls_callback_sch_href. Example:
  <L>244<pc>004-2<k1>akzayya  <ls>Yājñ. 1,242</ls>

Dictionary mw is also similar, refer function ls_callback_mw_href. Example:
  <L>68560<pc>371,2<k1>grasta   <ls>Yājñ. iii, 245</ls>  [Note 'iii']

See this commit for what was changed in csl-websanlexicon for links
 to yajnavalkya app:
 https://github.com/sanskrit-lexicon/csl-websanlexicon/commit/4bd83e7c66989bbd34bbfa2131b022c8b26dc950

When basicadjust is altered, then new local displays should be generated for
the affected dictionaries

sh generate_web.sh mw  ../../mw
sh generate_web.sh pwg  ../../pwg
sh generate_web.sh pw  ../../pw
sh generate_web.sh pwkvn  ../../pwkvn
sh generate_web.sh sch  ../../sch


-----
For the 'simple-search' displays to work, we must copy basicadjust.php to csl-apidev:
in csl-websanlexicon/v02, run script 'sh apidev_copy.sh' to copy basicadjust.php


When local displays are functioning properly for all dictionaries:

push csl-websanlexcion to github
push csl-apidev to github.

Finally, update cologne server
pull csl-websanlexicon
pull csl-apidev

In pywork/v02,  generate new Cologne displays for
 mw, pwg, pw, pwkvn, sch.

--------------------
Improving markup.

The various dictionaries, most notably PWG, often use an abbreviated form for
multiple references.  For example, in pwg.txt
  <L>1226<pc>1-0091<k1>atikfcCra
    <ls>YĀJÑ. 3,320. 264. 293.</ls>
  At the current stage, only link to <ls>YĀJÑ. 3,320. is 'active'.
  To make the other two implied links active, we have to revise the
  markup in pwg.txt to:
    <ls>YĀJÑ. 3,320.</ls> <ls n="YĀJÑ. 3,">264.</ls> <ls n="YĀJÑ. 3,">293.</ls>

  And some variations are even more indirect.
  Doing this markup change is challenging, and currently poorly automated.
  At the current time, this step is being omitted for pwg and the other
  dictionaries.
  
--------------------


