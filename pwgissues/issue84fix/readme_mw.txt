
issue84fix

mw link forms:
'ŚBr.' 4 parms (1st roman)


python lsfix2.py mw temp_mw_0.txt lsfix2_mw_0.txt
(None,1779),(all,1779) lsfix2_mw_0.txt

As usual, lsfix2 cannot handle the roman-first-parameter used by mw

  
cp temp_mw_0.txt temp_mw_1.txt
# edit temp_mw_1.txt for manual changes
  a few small changes.
</ls> <ls n="ŚBr.">


Note later print chg at aRupriyaNgu

python lsfix2.py mw temp_mw_1.txt lsfix2_mw_1.txt
(None,1779),(all,1779) lsfix2_mw_1.txt

Classification of instances 

not linked:
1043 matches for "<ls>ŚBr. [xiv]+\( f+\)?\.?</ls>"
 166 matches for "<ls n="ŚBr.">[xiv]+\( f+\)?\.?</ls>"
  20 matches for "<ls>ŚBr. [xiv]+, [0-9]+, [0-9]+\( f+\)?\.?</ls>"
   6 matches for "<ls n="ŚBr.">[xiv]+, [0-9]+\( f+\)?\.?</ls>"
   2 matches for "<ls n="ŚBr.">[xiv]+, [0-9]+, [0-9]+\( f+\)?\.?</ls>"
   2 matches for "<ls n="ŚBr. [xiv]+,">[0-9]+\( f+\)?\.?</ls>"
  15 matches for "<ls>ŚBr. [xiv]+, [0-9]+\( f+\)?\.?</ls>"
(+ 1043 166 20 6 2 2 15)  1254
linked:
 457 matches for "<ls>ŚBr. [xiv]+, [0-9]+, [0-9]+, [0-9]+\( f+\)?\.?</ls>"
  28 matches for "<ls n="ŚBr.">[xiv]+, [0-9]+, [0-9]+, [0-9]+\( f+\)?\.?</ls>"
  16 matches for "<ls n="ŚBr. [xiv]+, [0-9]+, [0-9]+,">[0-9]+\( f+\)?\.?</ls>"
   4 matches for "<ls n="ŚBr. [xiv]+, [0-9]+,">[0-9]+, [0-9]+\( f+\)?\.?</ls>"
  18 matches for "<ls n="ŚBr. [xiv]+,">[0-9]+, [0-9]+, [0-9]+\( f+\)?\.?</ls>"
   1 matches for "<ls n="ŚBr. [xiv]+,">[0-9]+, [0-9]+\( f+\)?\.?</ls>"
(+ 457 28 16 4 18 1) 524
(+ 1254 524) 1778

1 other instance (not linked)
92116	Arta	<ls>ŚBr. p. 339, l. 20 ff.</ls>	


-----------------------------------------------------------
# remake xml from temp_mw_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue84fix
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue84fix
-- end of 'remake xml ...'

-------------------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_mw_0.txt temp_mw_1.txt change_mw_1.txt
5 changes written to change_mw_1.txt
