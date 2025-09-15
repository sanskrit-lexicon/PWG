
issue122fix

pw link forms:
<ls>MĀRK. P. ([0-9]+),([0-9]+)

python lsfix2.py pw temp_pw_0.txt lsfix2_pw_0.txt

(True, 2) 165
(None, 2) 4
('fixed', 2) 5

no change.
The 4 None:
kuSarIra      <ls>MĀRK. P. im ŚKDR.</ls>	
pranftta      <ls>MĀRK. P. Einl. 2</ls>	
BinnamaryAda  <ls>MĀRK. P. S. 660, Z. 6</ls>	
pravftta      <ls>MĀRK. P. 51,42,b</ls>	


--------------------
# generate temp_pw_2.txt from temp_pw_0.txt and the 'fixed' elements

python dict_replace2.py temp_pw_0.txt lsfix2_pw_0.txt temp_pw_1.txt
5 lines to change
a
-----------------------------------------------------------
# remake xml from temp_pw_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue122fix
cp temp_pw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue122fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pw temp_pw_1.txt lsfix2_pw_1.txt

(True, 2) 175
(None, 2) 4


(- 175 165)  10 additional standard links

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pw_0.txt temp_pw_1.txt change_pw_1.txt
5 changes written to change_pw_1.txt
