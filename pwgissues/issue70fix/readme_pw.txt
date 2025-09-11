
issue70fix

pw link forms:
<ls>KATHĀS. ([0-9]+),([0-9]+)

python lsfix2.py pw temp_pw_0.txt lsfix2_pw_0.txt

735 lines written to lsfix2_pw_0.txt
(True, 2) 682
('fixed', 2) 47
(None, 2) 6

cp temp_pw_0.txt temp_pw_1.txt
A few of the None items can be corrected in temp_pw_1.txt

python lsfix2.py pw temp_pw_1.txt lsfix2_pw_1.txt

735 lines written to lsfix2_pw_1.txt
(True, 2) 687
('fixed', 2) 47
(None, 2) 1

735 lines read from lsfix2_pw_1.txt
47 lines to change
apply_repls: 47 lines changed
6
----------------------------------

# generate temp_pw_2.txt from temp_pw_1.txt and the 'fixed' elements

python dict_replace2.py temp_pw_1.txt lsfix2_pw_1.txt temp_pw_2.txt

25004 lines read from lsfix2_pw_0.txt
2 lines to change
apply_repls: 2 lines changed

-----------------------------------------------------------
# remake xml from temp_pw_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue70fix
cp temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue70fix
-- end of 'remake xml ...'


-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pw temp_pw_2.txt lsfix2_pw_2.txt

(True, 2) 808
(None, 2) 1

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pw_0.txt temp_pw_1.txt change_pw_1.txt
5 changes written to change_pw_1.txt

python diff_to_changes_dict.py temp_pw_1.txt temp_pw_2.txt change_pw_2.txt
47 changes written to change_pw_2.txt
