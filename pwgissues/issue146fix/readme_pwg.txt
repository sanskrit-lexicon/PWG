
issue146fix

pwg link forms:
<ls>KUMĀRAS. ([0-9]+),([0-9]+)

python lsfix2.py pwg temp_pwg_0.txt lsfix2_pwg_0.txt

2507 lines written to lsfix2_pwg_0.txt
(None, 2) 24
(True, 2) 2329
('fixed', 2) 151
(False, 2) 3

cp temp_pwg_0.txt temp_pwg_1.txt

Edit temp_pwg_1.txt to resolve the None and False

97800 : Sabda : KUMĀRAS. 1,1,46. : KUMĀRAS. 1,46. : print change

python lsfix2.py pwg temp_pwg_1.txt lsfix2_pwg_1.txt

(True, 2) 2353
('fixed', 2) 155
(None, 2) 1

The one 'None': 49148 : pradAna : KUMĀRAS. 6  : ?

--------------------
# generate temp_pwg_2.txt from temp_pwg_0.txt and the 'fixed' elements

python dict_replace2.py temp_pwg_1.txt lsfix2_pwg_1.txt temp_pwg_2.txt


-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue146fix
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue146fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pwg temp_pwg_2.txt lsfix2_pwg_2.txt

2686 lines written to lsfix2_pwg_2.txt
(True, 2) 2685
(None, 2) 1

(- 2685 2329)  356 additional standard links


---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
27 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
154 changes written to change_pwg_2.txt

