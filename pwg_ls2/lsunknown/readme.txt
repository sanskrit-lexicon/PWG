PWG/pwg_ls2/lsunknown

markup improvement.
--------------------------------------------------------------
Start with a copy of csl-orig/v02/pwg/pwg.txt at commit
  4b1d6eff7bf3b771dfe1f68e33d09ed982dd3ad0

# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_pwg_0.txt in this spruch directory
  git show 4b1d6ef:v02/pwg/pwg.txt > /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsunknown/temp_pwg_0.txt
# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsunknown/
--------------------------------------------------------------
Start with a copy of pwgbib_input.txt in csl-pywork at commit
  d56aba07ce78606544257246bae8ebe49e7fc043

cd /c/xampp/htdocs/cologne/csl-pywork/
# generate temp_pwg_0.txt in this spruch directory
  git show d56aba07:v02/distinctfiles/pwg/pywork/pwgauth/pwgbib_input.txt > /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsunknown/temp_pwg_tooltip_0.txt
  
# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsunknown/

===============================================================
# revise lsextract_all.py (starting with version in ../ak)
python lsextract_all.py temp_pwg_0.txt temp_pwg_tooltip_0.txt lsextract_pwg_0.txt lsunknown_0.txt
2711 tooltips from temp_pwg_tooltip.txt
2048 unknown ls written to lsunknown_0.txt
write_tips Output in  lsextract_pwg_0.txt

===============================================================
temp_pwg_1.txt
 identify with **...** markup the ls instances with unknown markup
 Plan then to manually edit this version to correct
Also  make needed revisions to tooltip file
python mark_lsunknown.py temp_pwg_0.txt lsunknown_0.txt temp_pwg_1.txt

cp temp_pwg_tooltip_0.txt temp_pwg_tooltip_1.txt

Manually change temp_pwg_1.txt (preserve number of lines)
Make changes at locations marked by '**...**'
Also, make changes to temp_pwg_tooltip_1.txt

===============================================================
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
 n="AV."  || n="Spr. (I)"
 n="HIT." || n="Spr."  || n="Spr. (II)"
 n="PAÑCAT."   || n="Verz. d. Oxf. H."
 n="" X n="COLEBR. Misc. Ess."
-----------------------------------------------

bib YĀJAÑ.  (circumflex added)
pwg YĀJAÑ.  (preformed)  <<  revised temp_pwg_1.txt and tooltip to use preformed


---------------------------------------------------------------------------
install  temp_pwg_1.txt to check xml
cp temp_pwg_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg ' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsunknown/

===============================================================
Recompute lsextract, to see if any are left
python lsextract_all.py temp_pwg_1.txt temp_pwg_tooltip_1.txt temp_lsextract_pwg_1.txt temp_lsunknown_1.txt

2800 tooltips from temp_pwg_tooltip_1.txt
34 unknown ls written to temp_lsunknown_1.txt
write_tips Output in  temp_lsextract_pwg_1.txt

MUST EXAMINE THOSE 34 !

===============================================================
temp_pwg_2.txt
 identify with **...** markup the ls instances with unknown markup
 Plan then to manually edit this version to correct
Also  make needed revisions to tooltip file
python mark_lsunknown.py temp_pwg_1.txt lsunknown_1.txt temp_pwg_2.txt

cp temp_pwg_tooltip_1.txt temp_pwg_tooltip_2.txt

Manually change temp_pwg_2.txt (preserve number of lines)
Make changes at locations marked by '**...**'
Also, make changes to temp_pwg_tooltip_2.txt

---------------------------------------------------------------------------
Recompute lsextract, to see if any are left
python lsextract_all.py temp_pwg_2.txt temp_pwg_tooltip_2.txt lsextract_pwg_2.txt lsunknown_2.txt

2802 tooltips from temp_pwg_tooltip_2.txt
0 unknown ls written to lsunknown_2.txt
write_tips Output in  lsextract_pwg_2.txt

ALL DONE!

---------------------------------------------------------------------------
install  temp_pwg_2.txt to check xml
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg ' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/lsunknown/

---------------------------------------------------------------------------
Generate change file from 0 to 2
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_2.txt change_lsunknown.txt

---------------------------------------------------------------------------
Make an issue in PWG repository.
https://github.com/sanskrit-lexicon/PWG/issues/64
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
