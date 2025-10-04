
issue100fix

mw link forms:
<ls>Ragh. ([0-9]+),([0-9]+)

python lsfix2.py mw temp_mw_0.txt lsfix2_mw_0.txt
(None,766),(all,766) lsfix2_mw_0.txt

lsfix2 doesn't know how to analyze mw




cp temp_mw_0.txt temp_mw_1.txt

Edit temp_mw_1.txt based on the None cases

109039 : nimIlitamuKa : Ragh. xix, 28, C. : Ragh. xix, 28, Ragh. (C) xix, 28 : print change (both editions have link at xix,28.

----------------------------------
python lsfix2.py mw temp_mw_1.txt lsfix2_mw_1.txt
(None,767),(all,767) lsfix2_mw_1.txt

Classification of None:

698 <ls>Ragh. [xivlc]+, [0-9]+\.?</ls> 
 26 <ls n="Ragh.">[xivlc]+, [0-9]+\.?</ls>
  4 <ls n="Ragh. [xivlc]+,">[0-9]+\.?</ls>
  3 <ls>Ragh. [xivlc]+, [0-9]+ [f]+\.?</ls>

  3 <ls>Ragh. (C) [xivlc]+, [0-9]+\.?</ls> links to Calcutta edition
  
  4 <ls>Ragh. [xivlc]+ [f]+\.?</ls> no link
 19 <ls>Ragh. [xivlc]+\.?</ls>  no link
  8 <ls n="Ragh.">[xivlc]+\.?</ls>  no link
  1 <ls n="Ragh.">[xivlc]+ [f]+\.?</ls>  no link
  1 <ls>Ragh. 7</ls> no link
  
(+ 698 26 4  3 3 4  19 8 1 1) 767  (as expected)

--------------------
# generate temp_mw_2.txt from temp_mw_0.txt and the 'fixed' elements
# python dict_replace2.py temp_mw_0.txt lsfix2_mw_0.txt temp_mw_2.txt
# No 'fixed' to expand.

-----------------------------------------------------------
# remake xml from temp_mw_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue100fix
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue100fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

# python lsfix2.py mw temp_mw_1.txt lsfix2_mw_1.txt
#Already done

 no additional standard links

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_mw_0.txt temp_mw_1.txt change_mw_1.txt
2 changes written to change_mw_2.txt

