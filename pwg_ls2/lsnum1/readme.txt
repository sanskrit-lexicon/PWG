PWG/pwg_ls2/lsnum1

markup improvement.
Ref: https://github.com/sanskrit-lexicon/PWG/issues/65

--------------------------------------------------------------
Start with a copy of csl-orig/v02/pwg/pwg.txt at commit
  0057893421337a290458f667286e18a9488fc093

# change to csl-orig repository on local installation
# generate temp_pwg_0.txt in this lsnum1 directory
cd /c/xampp/htdocs/cologne/csl-orig/
git show 005789:v02/pwg/pwg.txt > /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/temp_pwg_0.txt
# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
--------------------------------------------------------------
Start with a copy of pwgbib_input.txt in csl-pywork at commit
  c67f58fddca18bce6f63d9a5b4bdcb178d85bdc7

cd /c/xampp/htdocs/cologne/csl-pywork/
# generate temp_pwg_0.txt in this lsnum1 directory
  git show c67f58fd:v02/distinctfiles/pwg/pywork/pwgauth/pwgbib_input.txt > /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/temp_pwg_tooltip_0.txt
  
# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/

===============================================================
# revise lsextract_all.py (starting with version in ../lsunknown)
python lsextract_all.py temp_pwg_0.txt temp_pwg_tooltip_0.txt temp_lsextract_pwg_0.txt temp_lsnum1_0.txt
2803 tooltips from temp_pwg_tooltip_0.txt
32089 lsnums written to temp_lsnum1_0.txt
write_tips Output in  lsextract_pwg_0.txt

===============================================================
temp_pwg_1.txt
 identify with '<ls n="">' markup the ls instances starting with a digit.
 Plan then to manually edit this version to correct
Also  make needed revisions to tooltip file
python mark_lsnum1.py temp_pwg_0.txt temp_lsnum1_0.txt temp_pwg_1.txt

cp temp_pwg_tooltip_0.txt temp_pwg_tooltip_1.txt

Manually change temp_pwg_1.txt (preserve number of lines)
Make changes at locations marked by '**...**'
Also, make changes to temp_pwg_tooltip_1.txt

===============================================================
NOTE holdover print changes from lsunknown
--------------------------------------------
print changes
<L>2471<pc>1-0181<k1>anAkASa BHṚ. -> BṚH.
<L>44051<pc>4-0628<k1>pAYcAlaka
 P. 7, 9148. -> MBH. 7, 9148.
 P. 4, 1224. -> MBH. 4, 1224.
<L>44055<pc>4-0629<k1>pAYcAlya
 P. 1, 3728. -> MBH. 1, 3728.
--------------------------------------------
2553 matches in 2542 lines for ")\.</ls>"
 ).</ls>   ==>  </ls>).
--------------------------------------------
editing pastes
</ls> <ls n="ŚAT. BR.">  </ls> <ls n="KĀTY. ŚR.">  </ls> <ls n="BṚH. ĀR. UP.">
</ls> <ls n="PAÑCAT."> </ls> <ls n="PRAB.">  </ls> <ls n="P.">
</ls> <ls n="M.">   </ls> <ls n="N.">
</ls> <ls n="ŚĀK.">  </ls> <ls n="SUŚR.">
</ls> <ls n="ṚV.">   </ls> <ls n="HIT.">  </ls> <ls n="KATHĀS.">
</ls> <ls n="AIT. BR.">  </ls> <ls n="VS.">  </ls> <ls n="PAÑCAT.">
</ls> <ls n="">  </ls> <ls n="TS.">
 http://localhost/cologne/csl-apidev/simple-search/v1.1/list-0.2s_rw.php
 http://localhost/cologne/simple/
 n="" X n="COLEBR. Misc. Ess."
-----------------------------------------------
-----------------------------------------------
regex change pairs of 3
<ls>\(X\.\) \([0-9]+, [0-9]+, [0-9]+\.\) \([0-9]+, [0-9]+, [0-9]+\.\)</ls>
<ls>\1 \2</ls> <ls n="\1">\3</ls>

regex change pairs of 2
<ls>\(X\.\) \([0-9]+, [0-9]+\.\) \([0-9]+, [0-9]+\.\)</ls> 
<ls>\1 \2</ls> <ls n="\1">\3</ls>

regex change triples of 2
<ls>\(X\.\) \([0-9]+, [0-9]+\.\) \([0-9]+, [0-9]+\.\) \([0-9]+, [0-9]+\.\)</ls>
<ls>\1 \2</ls> <ls n="\1">\3</ls> <ls n="\1">\4</ls>

regex change triples of 3
<ls>\(X\.\) \([0-9]+, [0-9]+, [0-9]+\.\) \([0-9]+, [0-9]+, [0-9]+\.\) \([0-9]+, [0-9]+, [0-9]+\.\)</ls>
<ls>\1 \2</ls> <ls n="\1">\3</ls> <ls n="\1">\4</ls>
https://github.com/sanskrit-lexicon/COLOGNE/tree/master/localinstall/xampp
regex change triples of 4
<ls>\(X\.\) \([0-9]+, [0-9]+, [0-9]+, [0-9]+\.\) \([0-9]+, [0-9]+, [0-9]+, [0-9]+\.\) \([0-9]+, [0-9]+, [0-9]+, [0-9]+\.\)</ls>
<ls>\1 \2</ls> <ls n="\1">\3</ls> <ls n="\1">\4</ls>

-----------------------------------------------
-----------------------------------------------

bib YĀJAÑ.  (circumflex added)
pwg YĀJAÑ.  (preformed)  <<  revised temp_pwg_1.txt and tooltip to use preformed


---------------------------------------------------------------------------
temp_pwg_1a.txt remove unresolved <ls n="">
cp temp_pwg_1.txt temp_pwg_1a.txt
Manually change (via emacs) <ls n=""> → <ls>  29000 changes

---------------------------------------------------------------------------
install  temp_pwg_1a.txt to check xml
cp temp_pwg_1a.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg ' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/

python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1a.txt change_pwg_1.txt

---------------------------------------------------------------------------
About 10% done. Commit csl-orig, and update at Cologne.
cd /c/xampp/htdocs/cologne/csl-orig/
git pull  # to handle other changes, if any
git add .
git commit -m "PWG: numeric orphans, 1
Ref: https://github.com/sanskrit-lexicon/PWG/issues/65"
git push
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/
-------------------------------------------------
# do the necessary at cologne:
# login via ssh.
cd csl-orig
git pull
cd ../csl-pywork/v02
grep 'pwg' redo_cologne_all.sh
# etc.

---------------------------------------------------------------------------
update pwg repository
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsnum1/

---------------------------------------------------------------------------

#install temp_pwg_tooltip_2.txt in csl-pywork
cp temp_pwg_tooltip_2.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pwg/pywork/pwgauth/pwgbib_input.txt
---------------------------------------------------------------------------
# regenerate dictionary displays,  a way to check for errors in new tooltips
One problem noticed:
<ls n="PAÑCAT.">ed. orn. 18, 17</ls>

Tooltip for "PAÑCAT. ed. orn." not recognized in display
  Note: this problem solved by adding entry "PAÑCAT. ed. orn." to
  tooltip file.
---------------------------------------------------------------------------
push repositories to Github:
csl-orig
csl-pywork
PWG repository (repository containing this file)

---------------------------------------------------------------------------
pull repositories from Github to Cologne.
csl-orig
csl-pywork

---------------------------------------------------------------------------
Further comments in https://github.com/sanskrit-lexicon/PWG/issues/64
***************************************************************************
