
issue146fix

pwkvn link forms:
<ls>KUMĀRAS. ([0-9]+),([0-9]+)

python lsfix2.py pwkvn temp_pwkvn_0.txt lsfix2_pwkvn_0.txt

39 lines written to lsfix2_pwkvn_0.txt
(True, 2) 38
(None, 2) 1

cp temp_pwkvn_0.txt temp_pwkvn_1.txt

Edit temp_pwkvn_1.txt to resolve the None 

1 change

python lsfix2.py pwkvn temp_pwkvn_1.txt lsfix2_pwkvn_1.txt
38 lines written to lsfix2_pwkvn_1.txt
(True, 2) 38

Nothing else to do.



-----------------------------------------------------------
# remake xml from temp_pwkvn_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue146fix
cp temp_pwkvn_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwkvn  ../../pwkvn
sh xmlchk_xampp.sh pwkvn
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue146fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pwkvn temp_pwkvn_1.txt lsfix2_pwkvn_1.txt

38 lines written to lsfix2_pwkvn_1.txt
(True, 2) 38


---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwkvn_0.txt temp_pwkvn_1.txt change_pwkvn_1.txt
1 changes written to change_pwkvn_1.txt
