
issue147fix/megha

pw link forms:
MEGH. ([0-9]+)

python lsfix2.py pwg temp_pw_0.txt lsfix2_pw_0.txt

128 lines written to lsfix2_pw_0.txt
(None, 1) 9
(True, 1) 116
('fixed', 1) 3

The None cases are of form:
 <ls>MEGH. [IVX]+\.?</ls>

Not known how to interpret these.

No changes to pw


--------------------
# generate temp_pw_1.txt from temp_pw_0.txt and the 'fixed' elements

python dict_replace2.py temp_pw_0.txt lsfix2_pw_0.txt temp_pw_1.txt
3 lines to change

-----------------------------------------------------------
# remake xml from temp_pw_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue147fix/megha
cp temp_pw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue147fix/megha
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pwg temp_pw_1.txt lsfix2_pw_1.txt

(None, 1) 9
(True, 1) 122

(- 122 116)  6 additional standard links

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pw_0.txt temp_pw_1.txt change_pw_1.txt
6 changes written to change_pw_1.txt
