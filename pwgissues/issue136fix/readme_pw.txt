
pw  
python lsfix2.py pw temp_pw_0.txt lsfix2_pw_0.txt

547 lines written to lsfix2_pw_0.txt
(True, 3) 472
('fixed', 3) 62
(None, 3) 6
(True, 2) 7

cp temp_pw_0.txt temp_pw_1.txt
Correct one None in temp_pw_1.txt

python lsfix2.py pw temp_pw_1.txt lsfix2_pw_1.txt
547 lines written to lsfix2_pw_1.txt
(True, 3) 476
('fixed', 3) 63
(None, 3) 5
(True, 2) 3

----------------------------
# generate temp_pw_2.txt from temp_pw_1.txt and the 'fixed' elements

python dict_replace2.py temp_pw_1.txt lsfix2_pw_1.txt temp_pw_2.txt

547 lines read from lsfix2_pw_1.txt
62 lines to change

-----------------------------------------------------------
# remake xml from temp_pw_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue136fix
cp temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue136fix
-- end of 'remake xml ...'


-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pw temp_pw_2.txt lsfix2_pw_2.txt
623 lines written to lsfix2_pw_2.txt
(True, 3) 615
(None, 3) 5
(True, 2) 3

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pw_0.txt temp_pw_1.txt change_pw_1.txt
5 changes written to change_pw_1.txt

python diff_to_changes_dict.py temp_pw_1.txt temp_pw_2.txt change_pw_2.txt
62 changes written to change_pw_2.txt
